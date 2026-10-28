---
layout: page
title: Projects
permalink: /projects/
---
Selected academic and technology projects.

{% for project in site.projects %}## [{{ project.title }}]({{ project.url | relative_url }})

{{ project.description }}

{% else %}Project case studies will be added after verification.
{% endfor %}
