---
layout: page
title: Contact
permalink: /contact/
---
For academic inquiries, teaching collaboration, and research partnerships.

{% assign p = site.data.profile %}{% if p.email != '' %}**Email:** [{{ p.email }}](mailto:{{ p.email }})  
{% endif %}{% if p.orcid != '' %}**ORCID:** [{{ p.orcid }}](https://orcid.org/{{ p.orcid }})  
{% endif %}{% if p.github != '' %}**GitHub:** [{{ p.github }}](https://github.com/{{ p.github }})  
{% endif %}

**Affiliation:** {{ p.affiliation }}
