import NetVizCorpy

### Step 1: Search companies
# -> it will return a QID (identifier)and the name of the company as it appears in WikiData
# use search 'all' when company name is only partially known
#company_a = Searcher('Volvo', 'all').choose_company()
# use search 'exact' when the company name is known exactly as it appears in WikiData
company_a = NetVizCorpy.Searcher('Volvo Cars', 'exact').choose_company()
# could add more seed companies
#company_b = Searcher('Hyundai Motor Company', 'exact').choose_company()

### Step 2: Prepare QIDs and levels for building the company network
# make a list of the QIDs of the companies in scope
QIDs = [company_a[0][0]]
#QIDs = [company_a[0][0], company_b[0][0], company_c[0][0]]
# in case QIDs are already known, skip step 1 and call them directly
#QIDs = ['Q215293']
# specify the levels of interest, where the first two positions indicate upward relations
# and the last two positions indicate downward relations, such as:
# (parent companies, owned by -shareholders-, subsidiaries, owner of -has share in-)
levels = (3,3,3,3)
companyNetwork = NetVizCorpy.NetworkBuilder(QIDs, levels).get_companies_network()

### Step 3: Clean data for visualisation
cleanedNetwork = NetVizCorpy.Cleaner(companyNetwork).clean_join()

### Step 4: Visualisation (a local file named as VolvoCars_Level3_Demo.html will be created)
NetVizCorpy.Visualiser(cleanedNetwork, "VolvoCars_Level3_Demo").visualise_b2b_network()
