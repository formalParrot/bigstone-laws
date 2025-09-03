---
layout: page
title: "Court Cases"
---

<!-- Bigstone DEV watermark -->
<div style="position: fixed; bottom: 15px; left: 15px; opacity: 0.3; font-size: 12px; color: black; pointer-events: none; z-index: 9999; ">This is NOT maintained NOR officiated with Bigstone Development</div>

If you want to file your own case, please do so by <a href="https://forms.gle/t9QWVK5CxcE2vEGB7" target="_blank" rel="noopener noreferrer">clicking here</a>

<ul>
{% for case in site.cases %}
  <li>
    <a href="{{ site.baseurl }}{{ case.url }}">{{ case.title }}</a>  
    <small>({{ case.date | date: "%Y-%m-%d" }})</small>
  </li>
{% endfor %}
</ul>
