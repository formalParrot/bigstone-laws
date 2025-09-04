---
layout: home
title: "Court Cases"
---

If you want to file your own case, please do so by <a href="https://forms.gle/t9QWVK5CxcE2vEGB7" target="_blank" rel="noopener noreferrer">clicking here</a>

<ul>
{% for case in site.cases %}
  <li>
    <a href="{{ site.baseurl }}{{ case.url }}">{{ case.title }}</a>  
    <small>({{ case.date | date: "%Y-%m-%d" }})</small>
  </li>
{% endfor %}
</ul>


https://drive.google.com/drive/folders/1eTy_aG1bZkw3AmELUF3PiYnLBTJ8RKlW?usp=sharing