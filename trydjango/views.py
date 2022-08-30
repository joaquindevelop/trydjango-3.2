"""
To render html web pages
"""
from django.http import HttpResponse
import random
from django.template.loader import render_to_string, get_template

from articles.models import Article

# def article_home_view(request):


def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    name = "Justin"
    random_id = random.randint(1, 4) 

    #from the database?
    article_obj =  Article.objects.get(id=random_id)
    article_queryset = Article.objects.all() #esto nos da una queryset


    context = {
        "object_list": article_queryset,
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }
#una forma de renderizar el html
    # tmpl = get_template("home-view.html")
    # tmpl_string = tmpl.render(context=context)

#otra forma de renderizar el html, esta se usa mas normalmente
    HTML_STRING = render_to_string("home-view.html", context=context)
    # HTML_STRING = """
    # <h1>{title} (id: {id})</h1>
    # <p>{content}</p>
    # """.format(**context)
    return HttpResponse (HTML_STRING)