---
layout: page
title: Teaching
permalink: /teaching/
---
Courses and teaching resources.

{% for course in site.data.teaching %}## {{ course.name }}

{{ course.description }}

{% endfor %}
