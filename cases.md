---
layout: page
title: "Court Cases"
---

<ul>
{% for case in site.cases %}
  <li>
    <a href="{{ site.baseurl }}{{ case.url }}">{{ case.title }}</a>  
    <small>({{ case.date | date: "%Y-%m-%d" }})</small>
  </li>
{% endfor %}
</ul>
