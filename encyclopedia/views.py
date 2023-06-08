from django import forms
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
from random import choice
import markdown2

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get(request, entry):
    try:
        entry_body = markdown2.markdown(util.get_entry(entry))
        return render(request, "encyclopedia/entry.html", {
            "entry": entry,
            "entry_body": entry_body
        })
    except TypeError:
        return HttpResponse("Error: No Entry Found")
    

def search_results(request):
    search_str = request.GET['q']
    entries = util.list_entries()
    if search_str in entries:
        return get(request, search_str)

    valid_entries = []
    for entry in entries:
        if search_str in entry:
            valid_entries.append(entry)
    print(valid_entries)

    return render(request, "encyclopedia/search_results.html", {
        "entries": valid_entries
    })

def create(request):
    if request.method == "POST":
        form = request.POST
        entry = form["title"]
        entry_body = form["body"]
        # Check if entry exists
        if entry in util.list_entries():
            return HttpResponse("Error: Entry already exists")
        elif entry != "" and entry_body != "":
            # turn info into md file with util.save_entry(title, content)
            util.save_entry(entry, entry_body)
            return get(request, entry)
        else:
            return render(request, "encyclopedia/edit.html", {
                "error_message": "Invalid Entry",
                "entry": entry,
                "entry_body": entry_body
            })
    else:
        return render(request, "encyclopedia/create.html", {
            "entry": "",
            "entry_body": ""
        })

def edit(request, entry, entry_body=""):
    if request.method == "POST":
        form = request.POST
        entry = form["title"]
        entry_body = form["body"]
        if entry != "" and entry_body != "":
            # turn info into md file with util.save_entry(title, content)
            util.save_entry(entry, entry_body)
        else:
            return render(request, "encyclopedia/edit.html", {
                "error_message": "Invalid Entry",
                "entry": entry,
                "entry_body": entry_body
            })
        return get(request, entry)

    else:
        entry_body = util.get_entry(entry)
        return render(request, "encyclopedia/edit.html", {
            "entry": entry,
            "entry_body": entry_body
        })

def random(request):
    entries = util.list_entries()
    entry = choice(entries)
    entry_body = markdown2.markdown(util.get_entry(entry))
    return render(request, "encyclopedia/entry.html", {
        "entry": entry,
        "entry_body": entry_body
    })
