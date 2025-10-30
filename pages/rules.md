---
layout: home
title: "Rules"
---

<p>Rules are being taken straight from this <a href="https://raw.githubusercontent.com/SkyExploreWasTaken/bigstone-rules/master/rules-deed.MD" target="_blank">link</a></p>

<p> These rules are SkyExploreWasTaken's rules, and any questions about it, please open a support ticket at <a href="https://discord.com/channels/1382094887004147833/1425887720181600318">this channel</a>.</p>

<div id="rules-container">
  <p id="loading-text">Loading rules...</p>
  <div id="rules" markdown="0" style="display:none;"></div>
</div>

<!-- Marked library for parsing Markdown -->
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>

<script>
window.addEventListener('DOMContentLoaded', () => {
  const rulesDiv = document.getElementById('rules');
  const loadingText = document.getElementById('loading-text');

  fetch('https://raw.githubusercontent.com/SkyExploreWasTaken/bigstone-rules/master/rules-deed.MD')
    .then(res => res.text())
    .then(text => {
      const DELAY_SECONDS = .4;
      setTimeout(() => {
        rulesDiv.innerHTML = marked.parse(text);
        loadingText.style.display = 'none';
        rulesDiv.style.display = 'block';
      }, DELAY_SECONDS * 1000); // Convert seconds to milliseconds
    })
    .catch(() => {
      setTimeout(() => {
        loadingText.innerText = 'Failed to load rules.';
      }, DELAY_SECONDS * 1000);
    });
});
</script>

<style>
/* Mini page style */
#rules-container {
  max-width: 800px;
  margin: auto;
  padding: 1em;
  background: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* Loading text */
#loading-text {
  font-style: italic;
  color: #555;
  text-align: center;
}

/* Markdown headings smaller than page title */
#rules h1 {
  font-size: 1.5em; /* smaller than your page title */
  margin-top: 1em;
}
#rules h2 {
  font-size: 1.3em;
  margin-top: 0.9em;
}
#rules h3 {
  font-size: 1.1em;
  margin-top: 0.8em;
}

/* Optional: style links in rules */
#rules a {
  color: #0366d6;
  text-decoration: underline;
}
</style>

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
