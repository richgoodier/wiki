# Project 1: Wiki

This project, part of the CS50W curriculum, is designed to create a Wikipedia-like online encyclopedia.

#### Video Demo: <https://youtu.be/hQhobCuLF3c>

## Overview
The project provides a lightweight online encyclopedia, similar to Wikipedia, where users can search, view, create and edit entries. Each entry is stored in Markdown format, making it more human-friendly to write and edit. 

## Setup
1. Clone the repository to your local machine.
2. Make sure you have Django installed. If not, install Django by running the command: `pip install django`.
3. Run the Django server by using the command: `python manage.py runserver`.

## Project Structure
The project includes a Django project called `wiki` that contains a single app called `encyclopedia`.

- The `encyclopedia/urls.py` file defines the URL configuration for this app.

- The `encyclopedia/util.py` file contains helper functions that can be used to interact with the encyclopedia entries.

- The `encyclopedia/views.py` file contains Django views that handle rendering templates and processing data.

- The `encyclopedia/templates/encyclopedia` directory contains HTML templates that define the layout and structure of the web pages.

## Features

- **Entry Page**: Visiting `/wiki/TITLE`, where TITLE is the title of an encyclopedia entry, displays the contents of that encyclopedia entry.

- **Index Page**: The index page lists the names of all pages in the encyclopedia. Users can click on any entry name to be taken directly to that entry page.

- **Search**: Users can type a query into the search box in the sidebar to search for an encyclopedia entry.

- **New Page**: Users can create a new encyclopedia entry by clicking "Create New Page" in the sidebar.

- **Edit Page**: On each entry page, users can click a link to be taken to a page where they can edit that entry’s Markdown content in a textarea.

- **Random Page**: Clicking "Random Page" in the sidebar takes the user to a random encyclopedia entry.

- **Markdown to HTML Conversion**: Any Markdown content in the entry file is converted to HTML before being displayed to the user.

## Built With
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Markdown](https://daringfireball.net/projects/markdown/syntax)

## Disclaimer
Please note that the problem set specifications are owned by [Harvard University](https://cs50.harvard.edu/web/2020/projects/1/wiki/) and this solution is only meant as a guide, not for plagiarism.
