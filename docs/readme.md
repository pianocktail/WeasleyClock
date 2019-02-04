---
label: Readme
---

# Jekyll &amp; Hyde for GitHub Pages Sites

_Hyde_ is a minimalistic _[Jekyll]_ theme &amp; lib for quickly building _[GitHub Pages]_ sites. Particularly tailored for documentation. 


## Setup 

* Simply [_download from GitHub_](archive/master.zip) and use it as a template for your project. 
* Do not delete and avoid touching these files:
* `_config.yml` &ndash;  essential _[config]_ for Jekyll  and hence GitHup Pages.
* `jekyll/*` &ndash; except for the ones mentioned in _[Usage](#usage)_ below
* `Gemfile` &ndash; required if you want to run Jekyll locally


## Usage

* **Start Page**  &rarr;  edit _[index.md](index.md)_ in your project root
* **Menu Bar**  &rarr;   edit _[jekyll/_data/menu.yml](jekyll/_data/menu.yml)_ 
* **Links List** &rarr;   go into _[jekyll/_includes/links.md](jekyll/_includes/links.md)_ 
* **Custom Styles** &rarr;   go into _[jekyll/_sass/styles.scss](jekyll/_sass/styles.scss)_ 
* **Site Menu**  &rarr;  is automatically compiled from TOCs in your pages
* **Content Pages**  &rarr;  just add markdown files and see below...
* **Embed Chapters**  &rarr;  [as shown here](02-Large-Sample/02-Guides/index.md)
* **List Chapters**  &rarr;  [as shown here](02-Large-Sample/index.md)
* **Table of Contents**  &rarr; are added [as shown here](01-Medium-Sample/01-About.md)
* **Code Samples**  &rarr;  can be included [as shown here](01-Medium-Sample/02-Guides.md)
* **Search**  &rarr;  is automatically on; exclude sub-chapters by a suffix **_`-.md`_**
* **Responsive Design** is rudimentary in place &rarr; try on your iPhone.
* **Print Layout Styles** are also there &rarr; just print

<br>

> See these very samples live at http://danjoa.github.io/hyde.  
> Yes, this repo is a _Hyde_ site itself. 


<!-- ----------------------------------------------------- -->
[GitHub Pages]: https://pages.github.com
[config]: (https://jekyllrb.com/docs/configuration)
[jekyll]: https://jekyllrb.com
[hyde]: https://danjoa.github.io/hyde
[hyde.git]: https://github.com/danjoa/hyde
