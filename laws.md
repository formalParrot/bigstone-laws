---
layout: default
title: "Laws & Regulations"
---

# Laws & Regulations

<ol>
  {% for law in site.laws %}
    <li>
      <a href="{{ law.url | relative_url }}">{{ law.title }}</a>
      
      {% comment %} Find clauses for this law {% endcomment %}
      {% assign law_clauses = site.clauses | where: "law", law.slug %}
      {% if law_clauses.size > 0 %}
        <ol type="a">
          {% for clause in law_clauses %}
            <li>
              <a href="{{ clause.url | relative_url }}">{{ clause.title }}</a>
              
              {% comment %} Find subclauses for this clause {% endcomment %}
              {% assign clause_subclauses = site.subclauses | where: "law", law.slug | where: "clause", clause.slug %}
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