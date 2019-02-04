---
# This is your site's start page. You can freely modify all it's content 
# below, but keep these lines between the ---. They are jekyll's front 
# matter, neccessary to wrap the page into the site's layout frame. 
menu: skip
---

## Welcome to 
# <code> hyde <code>

{% assign home="https://github.com/danjoa/hyde" %}

* [&gt; learn about it &lt;](readme) 
* [&gt; get started &lt;](readme#setup)  
* [&gt; contribute &lt;]({{home}})

<br>
```
 git clone {{home}}  
``` 


<style>
  .content section { 
    /* margin: 77px 55px 0 0;  */
    margin-top: 99px;
    text-align: center; 
  }
  .content section h1 { 
    margin: 0 0 66px; font-size: 100px; 
    text-shadow: 0 0 0.3ex grey
  }
  .content section h2 { 
    margin: 0 0 -55px; font-weight: 100; font-size: 70px; 
    color: #caa; text-shadow: 0 0 0.2ex #ccc; 
  }
  .content section ul li {
    font-size: 111%;  font-weight: 500;  font-style: italic;
    margin: 14px 0; list-style-type: none;
  }
  div.highlight { background-color: inherit; }
  div.highlight pre { display: inline-block; }
  div.highlight pre code { font-style: italic !important; }
  .content section ul { padding: 0}

  @media screen and (max-width: 480px) {
    .content section h1 { font-size: 55px; }
    .content section h2 { font-size: 44px; margin-bottom: -33px; }
  }
</style>
