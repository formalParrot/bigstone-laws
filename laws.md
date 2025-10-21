---
layout: home
title: "Laws & Regulations"
---

If you want to suggest new laws, make a submission by <a href="https://forms.gle/VgiwyBtcbrgjqe4j6" target="_blank" rel="noopener noreferrer">clicking here</a>

I was forced to put a link instead of rules here, thanks to SkyExploreWT (no hate):

Rule's link: https://raw.githubusercontent.com/SkyExploreWasTaken/bigstone-rules/refs/heads/master/rules-deed.MD

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
