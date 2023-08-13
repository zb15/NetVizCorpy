[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![ORCID: Baruwa](https://img.shields.io/badge/ORCID-0000--0003--2933--0890-brightgreen)](https://orcid.org/0000-0003-2933-0890)

# B2BNetworkWiki
# Exploring companies' (B2B) networks from the publicly available WikiData

## Overview

The package is hosted at [https://github.com/zb15/B2BNetworkWiki](https://github.com/zb15/B2BNetworkWiki) and can be installed as,

> `pip install B2BNetworkWiki`

Currently it has 3 main functions:            

1.   choose_company()
2.   get_companies_network()
3.   visualise_b2b_network()

The **choose_company(input_name, search_option='all')** allows user to search companies with various search options: exact match; starts with the input plus space; 
starts with the input plus comma plus space, or as default all options.
User can search and choose any number of companies, and will need to save the QIDs only to a list to use them in the next function.

The **get_companies_network(QIDs, num_runs=(5,5,5,5))** has 4 set of sub-functions (e.g., has_parent() and if it does then get_parent_info()) 
to query the different relations (parent, owned by, subsidiary and owner of) plus some cleaning functions. It returns the max 4 dataframes
(p_df, ob_df, s_df, oo_df) (empty if it is requested to be 0).  

The **visualise_b2b_network(final_df)** function has 2 steps at the moment (that can easily be made into 1 function). 
The 1st step (with clean_and_join(p_df, ob_df, s_df, oo_df) function) is to clean the 4 datasets and join them together into a "final_df". 
The WikiData requires a lot of cleaning, handling duplicates etc. and comments are included within (the quite long) code. 
And the function that visualising the network from "final_df" dataframe (visualise_b2b_network()). 

The materials and methods in this repository support researchers and industry professionals to explore the sometimes over complicated corporate group structures in 
a user friendly interface as perceived by the public. 

MIT Licence

Copyright (c) 2023 Zsofia Baruwa

<hr>

**Table of Contents**
- [Overview](#overview)
- [Author ORCIDs](#author-orcids)
- [Dependencies](#dependencies)
- [Citation](#citation)
  - [Bibtex Citation](#bibtex-citation)
- [Usage](#usage)
  - [Repo Structure](#repo-structure)
  - [Download](#download)
  - [Functions](#functions)
- [Example](#example)
- [Reference](#reference)
- [Acknowledgements](#acknowledgements)

<hr>

## Author ORCIDs

[![ORCID: Baruwa](https://img.shields.io/badge/ORCID-0000--0003--2933--0890-brightgreen)](https://orcid.org/0000-0003-2933-0890)

## Dependencies
[[back to top](#b2bnetworkwiki)]

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
[[back to top](#b2bnetworkwiki)]

**A citation to the repository would be appreciated if you use any of its contents in your research or job.**

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

## Usage
[[back to top](#b2bnetworkwiki)]

B2BNetworkWiki allows User to search and choose companies and explore their corporate structure network in a user friendly format, as perceived by the public. Since, the data is queried from WikiData with each run, slight differences could occur once a new or updated item is searched again.

The package has 3 main functions and it has the following characteristics.

### Function 1. **choose_company(input_name, search_options='all')**

This function takes two arguments and returns the QID and company name for every results based on the search option. 

The *first* argument is to add the company's name (case sensitive).
The *second* one have 4 different arguments to choose from, but not necessarily needed. If left out, then by default it is set to return 'all' search options.
In case User knows the exact company name as appears on WikiData (e.g., "Tesla, Inc."), the 'exact' search option is recommended. 

Other search options available are  

*   'space' which will bring results that starts with the given input (e.g., "Tesla ") and
*   'space_comma' which will return results that are starts with user input followed by a comma and a space after (e.g., "Tesla, ").

Once the companies are chosen, which could be any number of companies, their QIDs need to be stored in a list to pass on to the next Function. 

### Function 2. **get_companies_network(QIDs, (5,5,5,5))**

This function takes two arguments and returns 4 dataframes in a dictionary (even if any of the dataframe is empty). 

The *first* argument needs to be a list of unique IDs starting with Q, that could be matched and used for query WikiData.
The *second* one have 4 values in the argument to specify
what level of each relations the user is interested. By default it is set to (5,5,5,5), and in that case could just add the first args. The levels could be specified as >0 integers. Beyond 5 levels in case big corporations it could take several minutes to return the results. The first position is to get parent companies, the second position is still upward relation, is to get owned by relations. For example if User only interested in upwards relations for 3 levels of the chosen companies, then it could be specified as (3,3,0,0). The last two position is for to get subsidiaries and owner of relations.

### Function 3. **visualise_b2b_network(final_df)**

The **visualise_b2b_network()** function has 2 steps at the moment. The 1st step (with *clean_and_join(p_df, ob_df, s_df, oo_df)* function) is to clean the 4 datasets and join them together into one dataframe. It can take up to several minutes depending on the dataset sizes, and that is one of the reason these steps are separated (it could also be used for other tasks not just visualising the network). The WikiData requires lots of cleaning, handling duplicates etc. and comments are included within the code file. It covers the following main cleaning processes (with assumptions):

*   drop duplicates from each datasets (beyond exact same records): 

      *   if proportion has values for both 'authorised capital' and 'voting interest' then only 'authorised capital' is kept;
      *   the record with the most recent date is kept, the older one(s) dropped;
      *   match the industries (it could result in duplicates the same pair with exactly same values for each column except the randomness that could happen when there are more than one industry is listed for either or both of the companies);

*   mark those records that has an end date with a value of "4" in the proportion column in order to differentiate them on the graph

*   mark parent relations (where no proportion is known) with a value of "2" for visualisation purposes

*   mark those proportions that not know values with a value of "3" for the same purpose as before

*   in case a company has more than one industry, then based on the most frequent industries in the ecosystem of the queried companies, the most frequent ones will be used for visualisation purposes (but all industries will be listed next to the company name once User hover over the node) 

*   any record that has no industries, then it will be checked if it is a human and or something else (e.g., a brand) and the brief description will be visible instead of the industries on the graph

*   countries will be visible next to the company names on the graph once User hover over the nodes, while the continent it belongs will be seen as various shapes of the nodes

*   the final joined dataframe will have parent and child classification only for the companies, where the parent means the parent and owned by relations; and the child means both subsidiary and owner of relations.


**Function 3.2** takes the resulting dataframe and visualise the network with the use of PyVis package (with the function *visualise_b2b_network(df)*).

*   The code will return a .html file that can be downloaded from colab and open in any browser. It is a dynamic graph, that could be dragged as User wishes to explore more the details.

*   Once the graph .html file opened, on top of the screen there are some built in filter functions. Each company could searched by name (Select node..).  The Select a network item has the option of nodes or edges. For example, certain industries could be highlighted from nodes -> groups -> then any industries from the graph can be chosen from a list (or typed in).

*   Visual guides:

    *   the **nodes** are colour coded by the top industries (it is randomly assigned each time when the function is being called and a new .html file returned)
    *   the nodes could take up to 7 shapes:

        1.   North America - triangle (pointing up)
        2.   South America - triangleDown (pointing down)
        3.   Europe - star
        4.   Africa - diamond
        5.   Asia - square
        6.   Australia - ellipse
        7.   Antarctica (and anything else, such as unknown values) - dot

   *   The network is directed, **edges** pointing from parent organisation toward child companies. The edges are colour coded and could take up to 5 colours and comments while hovering over:
        
       1.   parent company (colour: salmon)
       2.   proportion of shares that are greater than 0, but smaller than 0.5 (coulour: turquoise)
       3.   proportion of shares that are >=0.5 but <=1 (colour: violet)
       4.   where no data available on WikiData commented as "unknown" (colour: lime)
       5.   those relation that ended are commented with their end date (colour: grey)

   *   There is also an option for user to adjust the physics of the network graph. It's panel is located below the graph.


### Repo Structure
[[back to top](#b2bnetworkwiki)]

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

### Download
[[back to top](#b2bnetworkwiki)]

abc...


### Functions
[[back to top](#b2bnetworkwiki)]

abc...

## Example
[[back to top](#b2bnetworkwiki)]

An example use case for two electric vehicle companies' network can be explored in a [colab notebook](https://github.com/zb15/B2BNetworkWiki/blob/main/Example_B2BNetworkWiki.ipynb).

...


## Reference
[[back to top](#b2bnetworkwiki)]
...

## Acknowledgements

...
