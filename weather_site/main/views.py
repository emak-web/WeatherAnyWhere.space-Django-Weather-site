from django.shortcuts import render, redirect
from django.views.generic import View
from django.conf import settings
from .services.weather_getter import get_weather_context


class Weather_by_city(View):

    # available http methods
    http_method_names = ['get', ]

    # if http method = GET
    def get(self, request, *args, **kwargs):

        if 'city' in request.GET.keys():
            r_city = request.GET['city']

            try:
                return render(
                    request,
                    'main/get_weather.html',
                    get_weather_context(
                        settings.WEATHER_API,
                        settings.URL,
                        request.GET['city'],
                        )
                    )
            except ConnectionError:

                return render(request, 'main/get_weather.html', {
                    'error': 'No internet connection'
                })

        else:

            return render(request, 'main/default.html')
