---
layout: home
title: "Laws & Regulations"
---

If you want to suggest new laws, make a submission by <a href="https://forms.gle/VgiwyBtcbrgjqe4j6" target="_blank" rel="noopener noreferrer">clicking here</a>

Rules are being taken straight from this [link](https://raw.githubusercontent.com/SkyExploreWasTaken/bigstone-rules/master/rules-deed.MD)

<div id="rules" markdown="0"></div>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script>
window.addEventListener('DOMContentLoaded', () => {
  fetch('https://raw.githubusercontent.com/SkyExploreWasTaken/bigstone-rules/master/rules-deed.MD')
    .then(res => res.text())
    .then(text => {
      document.getElementById('rules').innerHTML = marked.parse(text);
    })
    .catch(() => {
      document.getElementById('rules').innerText = 'Failed to load rules.';
    });
});
</script>

<!--
<ol>
  {% assign sorted_laws = site.laws | sort: "order" %}
  {% for law in sorted_laws %}
    <li>
      <a href="{{ law.url | relative_url }}">{{ law.title }}</a>

      {% assign law_clauses = site.clauses | where: "law", law.slug | sort: "order" %}
      {% if law_clauses.size > 0 %}
        <ol type="a">
          {% for clause in law_clauses %}
            <li>
              <a href="{{ clause.url | relative_url }}">{{ clause.title }}</a>

              {% assign clause_subclauses = site.subclauses | where: "law", law.slug | where: "clause", clause.slug | sort: "order" %}
              {% if clause_subclauses.size > 0 %}
                <ol type="i">
                  {% for subclause in clause_subclauses %}
                    <li>
                      <a href="{{ subclause.url | relative_url }}">{{ subclause.title }}</a>
                    </li>
                  {% endfor %}
                </ol>
              {% endif %}
            </li>
          {% endfor %}
        </ol>
      {% endif %}
    </li>
  {% endfor %}
</ol>
-->
