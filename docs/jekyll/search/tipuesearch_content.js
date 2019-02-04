---
# Content index for Tipue Search
# https://github.com/jekylltools/jekyll-tipue-search
# v1.4
layout: null
---

const tipuesearch = {pages:[ 
  {% for p in site.html_pages %}{% unless p.path contains "-.md" %}{
      title: {{ p.title | smartify | strip_html | normalize_whitespace | jsonify }},
      text: {{ p.content | strip_html | normalize_whitespace | jsonify }},
      tags: {{ p.tags | join: " " | normalize_whitespace | jsonify }},
      url: {{ p.url | relative_url | jsonify }}
  }, {% endunless %}{% endfor %}
]}