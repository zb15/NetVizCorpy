[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![ORCID: Baruwa](https://img.shields.io/badge/ORCID-0000--0003--2933--0890-brightgreen)](https://orcid.org/0000-0003-2933-0890)
[![ORCID: Yuan](https://img.shields.io/badge/ORCID-0000--0001--6084--6719-brightgreen)](https://orcid.org/0000-0001-6084-6719)
[![ORCID: Li](https://img.shields.io/badge/ORCID-0000--0001--5628--7328-brightgreen)](https://orcid.org/0000-0001-5628-7328)
[![ORCID: Zhu](https://img.shields.io/badge/ORCID-0000--0003--0258--1454-brightgreen)](https://orcid.org/0000-0003-0258-1454)


# NetVizCorpy
**NetVizCorpy** is a Python toolkit for constructing and exploring multi-level corporate ownership networks using WikiData. It enables customisable visualisations of parent-subsidiary relationships, shareholder links, and B2B connectivity, supporting research, due diligence, and network analysis. Since, the data is queried from WikiData with each run, slight differences could occur once a new or updated item is searched again.

## 🚀 Features

- 🔍 Query WikiData for corporate ownership and shareholder data  
- 🕸️ Build nested network graphs of legal entities and relationships  
- 🖼️ Generate interactive visualisations for stakeholder engagement  
- 📦 Modular API designed for extensibility and reproducibility  
- 💼 Supports a broad range of analysis  

## 📦 Installation

The package is hosted at [https://github.com/zb15/NetVizCorpy](https://github.com/zb15/NetVizCorpy) and can be installed as,

> `pip install NetVizCorpy`

Or clone the repository directly:

```bash
git clone https://github.com/zb15/NetVizCorpy.git
cd NetVizCorpy
pip install -e .
```

## Dependencies

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)

The following packages need to be installed:

> `pip install pyvis`

> `pip install pycountry`

> `pip install pycountry-convert`



## 🧩 Usage Example

> `import NetVizCorpy as nvc`

**Step 1: Search companies**
-> it will return a QID (identifier)and the name of the company as it appears in WikiData
use search 'all' when company name is only partially known
> `company_a = nvc.Searcher('Volvo', 'all').choose_company()`
or use search 'exact' when the company name is known exactly as it appears in WikiData
> `company_a = nvc.Searcher('Volvo Cars', 'exact').choose_company()`
could add more seed companies
> `company_b = nvc.Searcher('Hyundai Motor Company', 'exact').choose_company()`

**Step 2: Prepare QIDs and levels for building the company network**
-> make a list of the QIDs of the companies in scope
> `QIDs = [company_a[0][0]]`
or
> `QIDs = [company_a[0][0], company_b[0][0], company_c[0][0]]`
in case QIDs are already known, skip step 1 and call them directly
> `QIDs = ['Q215293']`
specify the levels of interest, where the first two positions indicate upward relations
and the last two positions indicate downward relations, such as:
parent companies, owned by -shareholders-, subsidiaries, owner of -has share in-
> `levels = (3,3,3,3)`
> `companyNetwork = nvc.NetworkBuilder(QIDs, levels).get_companies_network()`

**Step 3: Clean data for visualisation**
> `cleanedNetwork = nvc.Cleaner(companyNetwork).clean_join()`
cleanedNetwork will return as a dataframe that could be exported as an .csv file if needed for other analysis

**Step 4: Visualisation (a local file named as VolvoCars_Level3_Demo.html will be created)**
> `nvc.Visualiser(cleanedNetwork, "VolvoCars_Level3_Demo").visualise_b2b_network()`

*   The code will return a .html file that can be downloaded from colab and opened in any browser. It is a dynamic graph, that could be dragged if User wishes to explore the details more.

*   Once the graph .html file opened, on top of the screen there are some built in filter functions. Each company could be searched by name (Select node..).  The Select a network item has the option of nodes or edges. For example, certain industries could be highlighted from the nodes -> groups -> then any industries from the graph can be chosen from a list (or typed in).

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
       2.   proportion of shares that are greater than 0, but smaller than 0.5 (colour: turquoise)
       3.   proportion of shares that are >=0.5 but <=1 (colour: violet)
       4.   where no data available on WikiData commented as "unknown" (colour: lime)
       5.   those relations that ended are commented with their end date (colour: grey)

   *   There is also an option for user to adjust the physics of the network graph. It's panel is located below the graph.


The materials and methods in this repository support researchers and industry professionals to explore the sometimes over complicated corporate group structures in a user friendly interface as perceived by the public. 

MIT Licence
Zsofia Baruwa
Copyright (c) 2025 University of Kent


## Citation

**A citation to the repository would be appreciated if you use any of its contents in your research or job.**

Please cite the code and work in this repository as follows:

> Baruwa, Zsofia, & Yuan, Haiyue & Li, Shujun & Zhu, Zhen. 2025. "Constructing and Analysing Global Corporate Networks
With Wikidata: The Case of Electric Vehicle Industry". *Global Networks*. https://doi.org/10.1111/glob.70029


### Bibtex citation

```bibtex
@article{baruwa_constructing_2025,
  author       = {Baruwa, Zsofia and
                  Yuan, Haiyue and
                  Li, Shujun and
                  Zhu, Zhen},
  title        = {{Constructing and Analysing Global Corporate Networks
                  With Wikidata: The Case of Electric Vehicle Industry}},
  abstract     = {Constructing comprehensive datasets for corporate network analysis remains a significant challenge for the business research community. This study introduces a novel Python tool, NetVizCorpy, which leverages Wikidata to generate such a dataset. We demonstrate its applications by constructing and analysing a global corporate network based on 44 seed electric vehicle (EV) companies and their three-level ownership structures. This dataset includes 1354 unique companies and 1575 ownership relations spanning 58 countries. We provide network characteristics, metrics and statistical insights, along with three detailed analytical applications. First, betweenness centrality identifies key influential companies, highlighting the role of financial institutions in industry resilience. Second, community detection reveals strategic positioning by EV manufacturers within global markets. Third, we find a nonlinear inverse U-shaped relationship between Global Network Connectivity (GNC) and Gross Competitive Intensity (GCI) at the country level. These findings offer new directions for understanding the resilience and competitiveness of the global EV industry},
  journal      = {Global Networks},
  volume       = {25},
  issue        = {4},
  month        = aug,
  year         = {2025},
  publisher    = {John Wiley & Sons Ltd},
  doi          = {10.1111/glob.70029},
  url          = {https://doi.org/10.1111/glob.70029}
}
```




