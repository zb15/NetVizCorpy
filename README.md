[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![ORCID: Baruwa](https://img.shields.io/badge/ORCID-0000--0003--2933--0890-brightgreen)](https://orcid.org/0000-0003-2933-0890)

# B2BNetworkWiki
# Exploring companies' (B2B) networks from the publicly available WikiData

## Overview

Currently the package has 3 main functions:            

1.   choose_company(input_name, search_option='all')
2.   get_companies_network(QIDs, num_runs=(5,5,5,5))
3.   visualise_b2b_network(df)

The **choose_company()** allows user to search companies with various search options: exact match; starts with the input plus space; 
starts with the input plus comma plus space, or as default all options.
User can search and choose any number of companies, and will need to save the QIDs only to a list to use them in the next function.

The **get_companies_network(QIDs, num_runs=(5,5,5,5))** has 4 set of sub-functions (e.g., has_parent() and if it does then get_parent_info()) 
to query the different realations (parent, owned by, subsidiary and owner of) plus some cleaning functions. It returns the max 4 dataframes
(p_df, ob_df, s_df, oo_df) (empty if it is requested to be 0).  

The **visualise_b2b_network()** function has 2 steps at the moment (that can easily be made into 1 function). 
The 1st step (with clean_and_join(p_df, ob_df, s_df, oo_df) function) is to clean the 4 datasets and join them together into a "final_df". 
The wikidata requires a lot of cleaning, handling duplicates etc. and comments are included within (the quite long) code. 
And the function that visualising the network from "final_df" dataframe (visualise_b2b_network()). 

The materials and methods in this repository support researchers and industry professionals to explore the sometimes over complicated corporate group structures in 
a user friendly interface as percieved by the public. 

## Author ORCIDs

[![ORCID: Baruwa](https://img.shields.io/badge/ORCID-0000--0003--2933--0890-brightgreen)](https://orcid.org/0000-0003-2933-0890)

## Dependencies

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)

The following packages need to be installed:

> `pip install pyvis`

> `pip install pycountry`

> `pip install pycountry-convert`

**Online Alternatives**:
EXAMPLE - NEED TO UPDATE WITH CURRENT PROJECT IF NEEDED

[![Read the Docs](https://readthedocs.org/projects/pip/badge/?version=latest)](https://github.com/zb15/B2BNetworkWiki/README.md)

* Visit our [jupyter book](https://...) for interactive code and explanatory text
* Run out Jupyter notebooks in binder [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/.../HEAD)

## Citation

**If you use the work contained in the repository for your research or job then a citation would be very welcome when you write up.**

Please cite the code and work in this repository as follows:

> Baruwa, Zsofia, & Li, Shujun & Zhu, Zhen. (2023). ... https://doi.org/ ...


### Bibtex citation

```bibtex
@software{baruwa_zsofia_2023_001,
  author       = {Baruwa, Zsofia and
                  Li, Shujun and
                  Zhu, Zhen},
  title        = {{B2BNetworkWiki: Exploring companies'
                  (B2B) networks from the publicly available WikiData}},
  month        = aug,
  year         = 2023,
  publisher    = {...},
  version      = {v1},
  doi          = {...},
  url          = {...}
}
```

## Repo Overview

```
.
├── binder
│   └── environment.yml
├── CITATION.cff
├── _config.yml
├── content
│   ├── 01_setup
│   ├── 02_funtion1
│   ├── 03_function2
│   ├── 04_function3
│   └── front_page.md
├── imgs
├── LICENSE
├── main.py
├── README.md
└── _toc.yml

```


* `binder` - contains the environment.yml file and all dependencies managed via conda - UPDATE THIS
* `_config.yml` - configuration of our Jupyter Book - UPDATE THIS
* `content` - the notebooks and markdown arranged by setup, funtion 1, function 2 and function 3. - UPDATE: DOES IT OK LIKE THIS OR JUST IN ONE FILE???
* `imgs` - all image files used in the tutorial material
* `LICENSE` - details of the MIT permissive license of this work.
* `main.py` - an example to use B2BNetworkWiki
* `README` - what you are reading now!
* `_toc.yml` - the table of contents for our Jupyter Book.
