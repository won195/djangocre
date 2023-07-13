from django.shortcuts import render

def index(request):
    labels_completion = ["Label 1", "Label 2", "Label 3"]
    values_completion = [10, 20, 30]
    labels_avg_user_level = ["Label A", "Label B", "Label C"]
    values_avg_user_level = [50, 60, 70]
    labels_pie_chart = ["Label X", "Label Y", "Label Z"]
    values_pie_chart = [40, 80, 120]
    labels_doughnut_chart = ["Label P", "Label Q", "Label R"]
    values_doughnut_chart = [25, 50, 75]
    labels_radar_chart = ["Label M", "Label N", "Label O"]
    values_radar_chart = [30, 60, 90]

    context = {
        "labels_completion": labels_completion,
        "values_completion": values_completion,
        "labels_avg_user_level": labels_avg_user_level,
        "values_avg_user_level": values_avg_user_level,
        "labels_pie_chart": labels_pie_chart,
        "values_pie_chart": values_pie_chart,
        "labels_doughnut_chart": labels_doughnut_chart,
        "values_doughnut_chart": values_doughnut_chart,
        "labels_radar_chart": labels_radar_chart,
        "values_radar_chart": values_radar_chart,
    }

    return render(request, "graph.html", context)
