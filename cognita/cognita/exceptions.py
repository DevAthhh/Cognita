from django.shortcuts import redirect


def except404(request, exception):
    return redirect('dashboard')