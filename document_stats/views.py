import json

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from document_stats.algorithms.bigrams import bigramsAll,bigrams
from document_stats.algorithms.frequency import frequency,frequencySep
from document_stats.algorithms.wordCloudGenerator import wordCloudAll,wordCloud
from document_stats.algorithms.zipfslaw import zipf
from document_stats.models import Report
from project.models import Project,ProjectFile


def stats_algorithms(request, pk):
    project = get_object_or_404(Project, pk=pk)
    reports = Report.objects.filter(project_id=pk)

    content = {'project': project, 'reports': reports,
               'title': f'Document Stats - {project.title}'}

    breadcrumb = {
        "Projects": reverse('all_projects'),
        project.title: reverse('show_project', args=[project.id]),
        "Document Stats": ""
    }

    content['breadcrumb'] = breadcrumb

    return render(request, 'document_stats/index.html', content)


def apply_stats_algorithm(request, pk, algorithm):
    project = get_object_or_404(Project, pk=pk)
    reports = Report.objects.filter(project_id=pk, algorithm=algorithm.lower())

    content = {'project': project, 'algorithm': algorithm, 'reports': reports, 'files': project.get_files(),
               'title': f'{algorithm.upper()} - {project.title}'}

    breadcrumb = {
        "Projects": reverse('all_projects'),
        project.title: reverse('show_project', args=[project.id]),
        "Document Stats": reverse('stats_algorithms', args=[pk]),
        algorithm.upper(): ""
    }

    content['breadcrumb'] = breadcrumb

    if request.method == 'POST':
        print(request.POST)

        post = dict(request.POST)

        n_word = int(request.POST['n_word'])
        n_most = int(request.POST['n_most'])

        selected_corpus_type = request.POST['selected_corpus']
        print("corpus_type: ",selected_corpus_type)

        selected_files_id = post['file'] #['73','74','75']
        selected_files = ProjectFile.objects.filter(id__in=selected_files_id) #Kullanıcının seçtigi dosyalar
        corpus = []

        for selected_file in selected_files:
            file = open(selected_file.file.path, "r", encoding='utf8')
            lines = file.read()
            file.close()
            corpus.append(lines)
        print(selected_files)


        # print(corpus)

        # print("seçilen dosyaların tutuldugu array'in uzunlugu ",len(selected_files_id))
        # print("ilk eleman",selected_files_id[0])
        # print("ikinci eleman",selected_files_id[1])
        #
        # print("length of selected files ",len(selected_files_id))


        # files = project.get_files()

        # for file_id in selected_files_id_array:
        #
        #     selected_file=ProjectFile.objects.filter(id=file_id)
        #     print("secilen fileların querysi ",selected_file)

            # file = open(selected_file.file.path, "r", encoding='utf8')
            # lines = file.read()
            # file.close()
            # corpus.append(lines)

        # print(corpus)

        if algorithm.lower() == 'frequency':
            if selected_corpus_type == 'all_corpus':
                outputs = frequency(corpus, n_most)
            else:
                outputs = frequencySep(corpus, n_most)
            print("algoritmadan donen sonuc: ",outputs)

        elif algorithm.lower() == "n-gram":
            if selected_corpus_type == 'all_corpus':
                outputs = bigramsAll(corpus, n_word, n_most)
            else:
                outputs = bigrams(corpus, n_word, n_most)

        elif algorithm.lower() == "wordcloud":
            if selected_corpus_type == 'all_corpus':
                outputs = wordCloudAll(corpus)
            else:
                outputs = wordCloud(corpus)

        elif algorithm.lower() == "zipf law":
                outputs = zipf(corpus)

                # outputs = yeni zipf algosu gelecek(corpus)


        content['outputs'] = outputs


        report = Report()
        report.project = project
        report.algorithm = algorithm.lower()
        report.all_data = json.dumps(outputs, separators=(',', ':'))
        # report tablosunda kullanıcının sectigi txt dosyalarının kaydını array de tutmak gerek
        report.save()
        report.selected_files.add(*selected_files)
        return redirect('view_stats_report', project.id, algorithm, report.id)

    return render(request, 'document_stats/params.html', content)



def view_stats_report(request, project_pk, algorithm, report_pk):
    project = get_object_or_404(Project, pk=project_pk)
    report = get_object_or_404(Report, pk=report_pk, algorithm=algorithm.lower())
    files = report.selected_files.all()
    report_output = report.get_output()

    content = {
        'project': project,
        'algorithm': algorithm,
        'files': [file.filename() for file in files],
        'report': report,
        'title': f'{algorithm.upper()} Report - {project.title}',
        'output': report_output,
    }


    # print(report_output)
    #
    # content.update(report_output)

    breadcrumb = {
        "Projects": reverse('all_projects'),
        project.title: reverse('show_project', args=[project.id]),
        "Document Stats": reverse('stats_algorithms', args=[project_pk]),
        algorithm.upper(): reverse('apply_stats_algorithm', args=[project_pk, algorithm]),
        f"Report (id:{report.id})": ""
    }

    content['breadcrumb'] = breadcrumb

    return render(request, 'document_stats/report.html', content)
