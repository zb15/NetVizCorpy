from B2BIdentifyQIDs import Searcher
from B2BDeriveNetwork import NetworkBuilder
from B2BVisualiseNetwork import Visualiser
from B2BPostProcess import Cleaner

# Step 1: Search companies
company_a = Searcher('Tesla, Inc.', 'exact').choose_company()
company_b = Searcher('Polestar', 'exact').choose_company()

# Step 2: Prepare QIDs and levels for building company network
QIDs = [company_a[0][0], company_b[0][0]]
levels = (2,2,2,2)
companyNetwork = NetworkBuilder(QIDs, levels).get_companies_network()

# Step 3: Clean data for visualisation
cleanedNetwork = Cleaner(companyNetwork).clean_join()

# Step 4: Visualisation (a local file named as B2BWiki_Demo.html will be created)
Visualiser(cleanedNetwork, "B2BWiki_Demo").visualise_b2b_network()
