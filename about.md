---
layout: home
title: "About"
permalink: /about/
---

<img src="../assets/images/courthouse/def-vs-judge.png" alt="alternative" style="width: 840px; height: 600px;">

## **What do we do?**
This projects helps the bigstone community server have peace & justice. The real explanation for this project is so: `SpionLennart` was going to get banned. `Minekey98` built a small courthouse that helped ban the player in a really cool and chill way that seemed like real life. We do **not** want to have *full* roleplay on the server, but finding out the verdicts with a court case is really cool in our opinion.

## **How do we do it?**
We follow semi-roleplay standards and use the courthouse building built by a group of builders. Shout out to `CrazyDuck24`, `Minekey98`, `Codeapotamus`, `BastienA`, `TheHuckle` and many more that I probably forgot to list.

## **Who does it?**
The builders are the keepers of the courthouse and they keep the courthouse in shape, write court cases and store it in their archives, build additions and many more. These are their discord profiles:

<!-- profiles -->
{% for profile in site.data.profiles %}
  {% if profile.avatar %}
    {% assign avatar_url = profile.avatar %}
  {% else %}
    {% assign avatar_url = "https://cdn.discordapp.com/avatars/" | append: profile.discord_id | append: "/" | append: profile.avatar_id | append: ".png?size=160" %}
  {% endif %}

  {% include profile.html 
    name=profile.name 
    username=profile.username 
    description=profile.description 
    avatar=avatar_url %}
{% endfor %}
