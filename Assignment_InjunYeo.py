import csv
import statistics as stats

def getData():
    path = "Superstore.csv"

    data = []
    with open(path,"r") as store_file:
        reader = csv.DictReader(store_file)
    
        for row in reader:
            record = {}
            record["State"] = row.get("State")
            record["Category"] = row.get("Category")
            record["Sub-Category"] = row.get("Sub-Category")
            record["Sales"] = float(row.get("Sales"))
            record["Quantity"] = int(row.get("Quantity"))
            record["Profit"] = float(row.get("Profit"))
            data.append(record)
    return data

def TotalSales(data):
    sales = []
    for record in data:
        sale = record.get("Sales")
        sales.append(sale)
    ts = 0
    for i in range(len(sales)):
        ts = ts + sales[i]
    print("Total Sales : {0}".format(ts))

def TotalProfit(data):
    profits = []
    for record in data:
        profit = record.get("Profit")
        profits.append(profit)
    tp = 0
    for i in range(len(profits)):
        tp = tp + profits[i]
    print("Total Profit : {0}".format(tp))

## To find out what kinds are in the category
#def kinds_of_category(data):
    #categories = []
    #for record in data:
        #category = record.get("Category")
        #categories.append(category)
    #print(len(categories))
    #count_1 = categories.count("Furniture")
    #count_2 = categories.count("Office Supplies")
    #count_3 = categories.count("Technology")
    #print(count_1 + count_2 + count_3)

def SalesForEachCategory(data):
    data = getData()
    furniture = []
    office_supplies = []
    technology = []
    for record in data:
        category = record.get("Category")
        if(category == "Furniture"):
            sale = record.get("Sales")
            furniture.append(sale)
        elif(category == "Office Supplies"):
            sale = record.get("Sales")
            office_supplies.append(sale)
        elif(category == "Technology"):
            sale = record.get("Sales")
            technology.append(sale)        
    ts_f = 0
    ts_os = 0
    ts_t = 0
    for i in range(len(furniture)):
        ts_f = ts_f + furniture[i]
    for i in range(len(office_supplies)):
        ts_os = ts_os + office_supplies[i]
    for i in range(len(technology)):
        ts_t = ts_t + technology[i]
    print("Sales for Furniture : {0}\nSales for Office Supplies : {1}\nSales for Technology : {2}".format(ts_f,ts_os,ts_t))

def ProfitForEachCategory(data):
    data = getData()
    furniture = []
    office_supplies = []
    technology = []
    for record in data:
        category = record.get("Category")
        if(category == "Furniture"):
            profit = record.get("Profit")
            furniture.append(profit)
        elif(category == "Office Supplies"):
            profit = record.get("Profit")
            office_supplies.append(profit)
        elif(category == "Technology"):
            profit = record.get("Profit")
            technology.append(profit)        
    tp_f = 0
    tp_os = 0
    tp_t = 0
    for i in range(len(furniture)):
        tp_f = tp_f + furniture[i]
    for i in range(len(office_supplies)):
        tp_os = tp_os + office_supplies[i]
    for i in range(len(technology)):
        tp_t = tp_t + technology[i]
    print("Profit for Furniture : {0}\nProfit for Office Supplies : {1}\nProfit for Technology : {2}".format(tp_f,tp_os,tp_t))

def SalesForEachState(data):
    data = getData()
    Alabama = []
    Arizona = []
    Arkansas = []
    California = []
    Colorado = []
    Connecticut = []
    Delaware = []
    District_of_Columbia = []
    Florida = []
    Georgia = []
    Idaho = []
    Illinois = []
    Indiana = []
    Iowa = []
    Kansas = []
    Kentucky = []
    Louisiana = []
    Maine = []
    Maryland = []
    Massachusetts = []
    Michigan = []
    Minnesota = []
    Mississippi = []
    Missouri = []
    Montana = []
    Nebraska = []
    Nevada = []
    New_Hampshire = []
    New_Jersey = []
    New_Mexico = []
    New_York = []
    North_Carolina = []
    North_Dakota = []
    Ohio = []
    Oklahoma = []
    Oregon = []
    Pennsylvania = []
    Rhode_Island = []
    South_Carolina = []
    South_Dakota = []
    Tennessee = []
    Texas = []
    Utah = []
    Vermont = []
    Virginia = []
    Washington = []
    West_Virginia = []
    Wisconsin = []
    Wyoming = []
    for record in data:
        state = record.get("State")
        if(state == "Alabama"):
            sale = record.get("Sales")
            Alabama.append(sale)
        elif(state == "Arizona"):
            sale = record.get("Sales")
            Arizona.append(sale)
        elif(state == "Arkansas"):
            sale = record.get("Sales")
            Arkansas.append(sale)
        elif(state == "California"):
            sale = record.get("Sales")
            California.append(sale)
        elif(state == "Colorado"):
            sale = record.get("Sales")
            Colorado.append(sale)
        elif(state == "Connecticut"):
            sale = record.get("Sales")
            Connecticut.append(sale)
        elif(state == "Delaware"):
            sale = record.get("Sales")
            Delaware.append(sale)
        elif(state == "District of Columbia"):
            sale = record.get("Sales")
            District_of_Columbia.append(sale)        
        elif(state == "Florida"):
            sale = record.get("Sales")
            Florida.append(sale)  
        elif(state == "Georgia"):
            sale = record.get("Sales")
            Georgia.append(sale)
        elif(state == "Idaho"):
            sale = record.get("Sales")
            Idaho.append(sale)  
        elif(state == "Illinois"):
            sale = record.get("Sales")
            Illinois.append(sale)  
        elif(state == "Indiana"):
            sale = record.get("Sales")
            Indiana.append(sale)  
        elif(state == "Iowa"):
            sale = record.get("Sales")
            Iowa.append(sale)  
        elif(state == "Kansas"):
            sale = record.get("Sales")
            Kansas.append(sale)  
        elif(state == "Kentucky"):
            sale = record.get("Sales")
            Kentucky.append(sale)  
        elif(state == "Louisiana"):
            sale = record.get("Sales")
            Louisiana.append(sale)  
        elif(state == "Maine"):
            sale = record.get("Sales")
            Maine.append(sale)  
        elif(state == "Maryland"):
            sale = record.get("Sales")
            Maryland.append(sale)  
        elif(state == "Massachusetts"):
            sale = record.get("Sales")
            Massachusetts.append(sale)  
        elif(state == "Michigan"):
            sale = record.get("Sales")
            Michigan.append(sale)    
        elif(state == "Minnesota"):
            sale = record.get("Sales")
            Minnesota.append(sale)    
        elif(state == "Mississippi"):
            sale = record.get("Sales")
            Mississippi.append(sale)    
        elif(state == "Missouri"):
            sale = record.get("Sales")
            Missouri.append(sale)    
        elif(state == "Montana"):
            sale = record.get("Sales")
            Montana.append(sale)    
        elif(state == "Nebraska"):
            sale = record.get("Sales")
            Nebraska.append(sale)    
        elif(state == "Nevada"):
            sale = record.get("Sales")
            Nevada.append(sale)    
        elif(state == "New Hampshire"):
            sale = record.get("Sales")
            New_Hampshire.append(sale)    
        elif(state == "New Jersey"):
            sale = record.get("Sales")
            New_Jersey.append(sale)    
        elif(state == "New Mexico"):
            sale = record.get("Sales")
            New_Mexico.append(sale)    
        elif(state == "New York"):
            sale = record.get("Sales")
            New_York.append(sale)    
        elif(state == "North Carolina"):
            sale = record.get("Sales")
            North_Carolina.append(sale)    
        elif(state == "North Dakota"):
            sale = record.get("Sales")
            North_Dakota.append(sale)    
        elif(state == "Ohio"):
            sale = record.get("Sales")
            Ohio.append(sale)    
        elif(state == "Oklahoma"):
            sale = record.get("Sales")
            Oklahoma.append(sale)   
        elif(state == "Oregon"):
            sale = record.get("Sales")
            Oregon.append(sale)   
        elif(state == "Pennsylvania"):
            sale = record.get("Sales")
            Pennsylvania.append(sale)   
        elif(state == "Rhode Island"):
            sale = record.get("Sales")
            Rhode_Island.append(sale)   
        elif(state == "South Carolina"):
            sale = record.get("Sales")
            South_Carolina.append(sale)   
        elif(state == "South Dakota"):
            sale = record.get("Sales")
            South_Dakota.append(sale)   
        elif(state == "Tennessee"):
            sale = record.get("Sales")
            Tennessee.append(sale)   
        elif(state == "Texas"):
            sale = record.get("Sales")
            Texas.append(sale)   
        elif(state == "Utah"):
            sale = record.get("Sales")
            Utah.append(sale)   
        elif(state == "Vermont"):
            sale = record.get("Sales")
            Vermont.append(sale)  
        elif(state == "Virginia"):
            sale = record.get("Sales")
            Virginia.append(sale)  
        elif(state == "Washington"):
            sale = record.get("Sales")
            Washington.append(sale)  
        elif(state == "West Virginia"):
            sale = record.get("Sales")
            West_Virginia.append(sale)      
        elif(state == "Wisconsin"):
            sale = record.get("Sales")
            Wisconsin.append(sale)   
        elif(state == "Wyoming"):
            sale = record.get("Sales")
            Wyoming.append(sale)               
    ts_Alabama = 0
    ts_Arizona = 0
    ts_Arkansas = 0
    ts_California = 0
    ts_Colorado = 0
    ts_Connecticut = 0
    ts_Delaware = 0
    ts_District_of_Columbia = 0
    ts_Florida = 0
    ts_Georgia = 0
    ts_Idaho = 0
    ts_Illinois = 0
    ts_Indiana = 0
    ts_Iowa = 0
    ts_Kansas = 0
    ts_Kentucky = 0
    ts_Louisiana = 0
    ts_Maine = 0
    ts_Maryland = 0
    ts_Massachusetts = 0
    ts_Michigan = 0
    ts_Minnesota = 0
    ts_Mississippi = 0
    ts_Missouri = 0
    ts_Montana = 0
    ts_Nebraska = 0
    ts_Nevada = 0
    ts_New_Hampshire = 0
    ts_New_Jersey = 0
    ts_New_Mexico = 0
    ts_New_York = 0
    ts_North_Carolina = 0
    ts_North_Dakota = 0
    ts_Ohio = 0
    ts_Oklahoma = 0
    ts_Oregon = 0
    ts_Pennsylvania = 0
    ts_Rhode_Island = 0
    ts_South_Carolina = 0
    ts_South_Dakota = 0
    ts_Tennessee = 0
    ts_Texas = 0
    ts_Utah = 0
    ts_Vermont = 0
    ts_Virginia = 0
    ts_Washington = 0
    ts_West_Virginia = 0
    ts_Wisconsin = 0
    ts_Wyoming = 0
    for i in range(len(Alabama)):
        ts_Alabama = ts_Alabama + Alabama[i]
    for i in range(len(Arizona)):
        ts_Arizona = ts_Arizona + Arizona[i] 
    for i in range(len(Arkansas)):
        ts_Arkansas = ts_Arkansas + Arkansas[i]    
    for i in range(len(California)):
        ts_California = ts_California + California[i]
    for i in range(len(Colorado)):
        ts_Colorado = ts_Colorado + Colorado[i]
    for i in range(len(Connecticut)):
        ts_Connecticut = ts_Connecticut + Connecticut[i]
    for i in range(len(Delaware)):
        ts_Delaware = ts_Delaware + Delaware[i]
    for i in range(len(District_of_Columbia)):
        ts_District_of_Columbia = ts_District_of_Columbia + District_of_Columbia[i]
    for i in range(len(Florida)):
        ts_Florida = ts_Florida + Florida[i]
    for i in range(len(Georgia)):
        ts_Georgia = ts_Georgia + Georgia[i]
    for i in range(len(Idaho)):
        ts_Idaho = ts_Idaho + Idaho[i]
    for i in range(len(Illinois)):
        ts_Illinois = ts_Illinois + Illinois[i]
    for i in range(len(Indiana)):
        ts_Indiana = ts_Indiana + Indiana[i]
    for i in range(len(Iowa)):
        ts_Iowa = ts_Iowa + Iowa[i]
    for i in range(len(Kansas)):
        ts_Kansas = ts_Kansas + Kansas[i]
    for i in range(len(Kentucky)):
        ts_Kentucky = ts_Kentucky + Kentucky[i]
    for i in range(len(Louisiana)):
        ts_Louisiana = ts_Louisiana + Louisiana[i]
    for i in range(len(Maine)):
        ts_Maine = ts_Maine + Maine[i]
    for i in range(len(Maryland)):
        ts_Maryland = ts_Maryland + Maryland[i]
    for i in range(len(Massachusetts)):
        ts_Massachusetts = ts_Massachusetts + Massachusetts[i]
    for i in range(len(Michigan)):
        ts_Michigan = ts_Michigan + Michigan[i]
    for i in range(len(Minnesota)):
        ts_Minnesota = ts_Minnesota + Minnesota[i]
    for i in range(len(Mississippi)):
        ts_Mississippi = ts_Mississippi + Mississippi[i]
    for i in range(len(Missouri)):
        ts_Missouri = ts_Missouri + Missouri[i]
    for i in range(len(Montana)):
        ts_Montana = ts_Montana + Montana[i]
    for i in range(len(Nebraska)):
        ts_Nebraska = ts_Nebraska + Nebraska[i]
    for i in range(len(Nevada)):
        ts_Nevada = ts_Nevada + Nevada[i]
    for i in range(len(New_Hampshire)):
        ts_New_Hampshire = ts_New_Hampshire + New_Hampshire[i]
    for i in range(len(New_Jersey)):
        ts_New_Jersey = ts_New_Jersey + New_Jersey[i]
    for i in range(len(New_Mexico)):
        ts_New_Mexico = ts_New_Mexico + New_Mexico[i]
    for i in range(len(New_York)):
        ts_New_York = ts_New_York + New_York[i]
    for i in range(len(North_Carolina)):
        ts_North_Carolina = ts_North_Carolina + North_Carolina[i]
    for i in range(len(North_Dakota)):
        ts_North_Dakota = ts_North_Dakota + North_Dakota[i]
    for i in range(len(Ohio)):
        ts_Ohio = ts_Ohio + Ohio[i]
    for i in range(len(Oklahoma)):
        ts_Oklahoma = ts_Oklahoma + Oklahoma[i]
    for i in range(len(Oregon)):
        ts_Oregon = ts_Oregon + Oregon[i]
    for i in range(len(Pennsylvania)):
        ts_Pennsylvania = ts_Pennsylvania + Pennsylvania[i]
    for i in range(len(Rhode_Island)):
        ts_Rhode_Island = ts_Rhode_Island + Rhode_Island[i]
    for i in range(len(South_Carolina)):
        ts_South_Carolina = ts_South_Carolina + South_Carolina[i]
    for i in range(len(South_Dakota)):
        ts_South_Dakota = ts_South_Dakota + South_Dakota[i]
    for i in range(len(Tennessee)):
        ts_Tennessee = ts_Tennessee + Tennessee[i]
    for i in range(len(Texas)):
        ts_Texas = ts_Texas + Texas[i]
    for i in range(len(Utah)):
        ts_Utah = ts_Utah + Utah[i]
    for i in range(len(Vermont)):
        ts_Vermont = ts_Vermont + Vermont[i]
    for i in range(len(Virginia)):
        ts_Virginia = ts_Virginia + Virginia[i]
    for i in range(len(Washington)):
        ts_Washington = ts_Washington + Washington[i]
    for i in range(len(West_Virginia)):
        ts_West_Virginia = ts_West_Virginia + West_Virginia[i]
    for i in range(len(Wisconsin)):
        ts_Wisconsin = ts_Wisconsin + Wisconsin[i]
    for i in range(len(Wyoming)):
        ts_Wyoming = ts_Wyoming + Wyoming[i]
    print("<Sales for each State>\nAlabama : {0}\nArizona : {1}\nArkansas : {2}\nCalifornia : {3}\nColorado : {4}\nConnecticut : {5}\nDelaware : {6}\nDistrict of Columbia : {7}\nFlorida : {8}\nGeorgia : {9}\nIdaho : {10}\nIllinois : {11}\nIndiana : {12}\nIowa : {13}\nKansas : {14}\nKentucky : {15}\nLouisiana : {16}\nMaine : {17}\nMaryland : {18}\nMassachusetts : {19}\nMichigan : {20}\nMinnesota : {21}\nMississippi : {22}\nMissouri : {23}\nMontana : {24}\nNebraska : {25}\nNevada : {26}\nNew Hampshire : {27}\nNew Jersey : {28}\nNew Mexico : {29}\nNew York : {30}\nNorth Carolina : {31}\nNorth Dakota : {32}\nOhio : {33}\nOklahoma : {34}\nOregon : {35}\nPennsylvania : {36}\nRhode Island : {37}\nSouth Carolina : {38}\nSouth Dakota : {39}\nTennessee : {40}\nTexas : {41}\nUtah : {42}\nVermont : {43}\nVirginia : {44}\nWashington : {45}\nWest Virginia : {46}\nWisconsin : {47}\nWyoming : {48}".format(ts_Alabama,ts_Arizona,ts_Arkansas,ts_California,ts_Colorado,ts_Connecticut,ts_Delaware,ts_District_of_Columbia,ts_Florida,ts_Georgia,ts_Idaho,ts_Illinois,ts_Indiana,ts_Iowa,ts_Kansas,ts_Kentucky,ts_Louisiana,ts_Maine,ts_Maryland,ts_Massachusetts,ts_Michigan,ts_Minnesota,ts_Mississippi,ts_Missouri,ts_Montana,ts_Nebraska,ts_Nevada,ts_New_Hampshire,ts_New_Jersey,ts_New_Mexico,ts_New_York,ts_North_Carolina,ts_North_Dakota,ts_Ohio,ts_Oklahoma,ts_Oregon,ts_Pennsylvania,ts_Rhode_Island,ts_South_Carolina,ts_South_Dakota,ts_Tennessee,ts_Texas,ts_Utah,ts_Vermont,ts_Virginia,ts_Washington,ts_West_Virginia,ts_Wisconsin,ts_Wyoming))

def ProfitForEachState(data):
    data = getData()
    Alabama = []
    Arizona = []
    Arkansas = []
    California = []
    Colorado = []
    Connecticut = []
    Delaware = []
    District_of_Columbia = []
    Florida = []
    Georgia = []
    Idaho = []
    Illinois = []
    Indiana = []
    Iowa = []
    Kansas = []
    Kentucky = []
    Louisiana = []
    Maine = []
    Maryland = []
    Massachusetts = []
    Michigan = []
    Minnesota = []
    Mississippi = []
    Missouri = []
    Montana = []
    Nebraska = []
    Nevada = []
    New_Hampshire = []
    New_Jersey = []
    New_Mexico = []
    New_York = []
    North_Carolina = []
    North_Dakota = []
    Ohio = []
    Oklahoma = []
    Oregon = []
    Pennsylvania = []
    Rhode_Island = []
    South_Carolina = []
    South_Dakota = []
    Tennessee = []
    Texas = []
    Utah = []
    Vermont = []
    Virginia = []
    Washington = []
    West_Virginia = []
    Wisconsin = []
    Wyoming = []
    for record in data:
        state = record.get("State")
        if(state == "Alabama"):
            profit = record.get("Profit")
            Alabama.append(profit)
        elif(state == "Arizona"):
            profit = record.get("Profit")
            Arizona.append(profit)
        elif(state == "Arkansas"):
            profit = record.get("Profit")
            Arkansas.append(profit)
        elif(state == "California"):
            profit = record.get("Profit")
            California.append(profit)
        elif(state == "Colorado"):
            profit = record.get("Profit")
            Colorado.append(profit)
        elif(state == "Connecticut"):
            profit = record.get("Profit")
            Connecticut.append(profit)
        elif(state == "Delaware"):
            profit = record.get("Profit")
            Delaware.append(profit)
        elif(state == "District of Columbia"):
            profit = record.get("Profit")
            District_of_Columbia.append(profit)        
        elif(state == "Florida"):
            profit = record.get("Profit")
            Florida.append(profit)  
        elif(state == "Georgia"):
            profit = record.get("Profit")
            Georgia.append(profit)
        elif(state == "Idaho"):
            profit = record.get("Profit")
            Idaho.append(profit)  
        elif(state == "Illinois"):
            profit = record.get("Profit")
            Illinois.append(profit)  
        elif(state == "Indiana"):
            profit = record.get("Profit")
            Indiana.append(profit)  
        elif(state == "Iowa"):
            profit = record.get("Profit")
            Iowa.append(profit)  
        elif(state == "Kansas"):
            profit = record.get("Profit")
            Kansas.append(profit)  
        elif(state == "Kentucky"):
            profit = record.get("Profit")
            Kentucky.append(profit)  
        elif(state == "Louisiana"):
            profit = record.get("Profit")
            Louisiana.append(profit)  
        elif(state == "Maine"):
            profit = record.get("Profit")
            Maine.append(profit)  
        elif(state == "Maryland"):
            profit = record.get("Profit")
            Maryland.append(profit)  
        elif(state == "Massachusetts"):
            profit = record.get("Profit")
            Massachusetts.append(profit)  
        elif(state == "Michigan"):
            profit = record.get("Profit")
            Michigan.append(profit)    
        elif(state == "Minnesota"):
            profit = record.get("Profit")
            Minnesota.append(profit)    
        elif(state == "Mississippi"):
            profit = record.get("Profit")
            Mississippi.append(profit)    
        elif(state == "Missouri"):
            profit = record.get("Profit")
            Missouri.append(profit)    
        elif(state == "Montana"):
            profit = record.get("Profit")
            Montana.append(profit)    
        elif(state == "Nebraska"):
            profit = record.get("Profit")
            Nebraska.append(profit)    
        elif(state == "Nevada"):
            profit = record.get("Profit")
            Nevada.append(profit)    
        elif(state == "New Hampshire"):
            profit = record.get("Profit")
            New_Hampshire.append(profit)    
        elif(state == "New Jersey"):
            profit = record.get("Profit")
            New_Jersey.append(profit)    
        elif(state == "New Mexico"):
            profit = record.get("Profit")
            New_Mexico.append(profit)    
        elif(state == "New York"):
            profit = record.get("Profit")
            New_York.append(profit)    
        elif(state == "North Carolina"):
            profit = record.get("Profit")
            North_Carolina.append(profit)    
        elif(state == "North Dakota"):
            profit = record.get("Profit")
            North_Dakota.append(profit)    
        elif(state == "Ohio"):
            profit = record.get("Profit")
            Ohio.append(profit)    
        elif(state == "Oklahoma"):
            profit = record.get("Profit")
            Oklahoma.append(profit)   
        elif(state == "Oregon"):
            profit = record.get("Profit")
            Oregon.append(profit)   
        elif(state == "Pennsylvania"):
            profit = record.get("Profit")
            Pennsylvania.append(profit)   
        elif(state == "Rhode Island"):
            profit = record.get("Profit")
            Rhode_Island.append(profit)   
        elif(state == "South Carolina"):
            profit = record.get("Profit")
            South_Carolina.append(profit)   
        elif(state == "South Dakota"):
            profit = record.get("Profit")
            South_Dakota.append(profit)   
        elif(state == "Tennessee"):
            profit = record.get("Profit")
            Tennessee.append(profit)   
        elif(state == "Texas"):
            profit = record.get("Profit")
            Texas.append(profit)   
        elif(state == "Utah"):
            profit = record.get("Profit")
            Utah.append(profit)   
        elif(state == "Vermont"):
            profit = record.get("Profit")
            Vermont.append(profit)  
        elif(state == "Virginia"):
            profit = record.get("Profit")
            Virginia.append(profit)  
        elif(state == "Washington"):
            profit = record.get("Profit")
            Washington.append(profit)  
        elif(state == "West Virginia"):
            profit = record.get("Profit")
            West_Virginia.append(profit)      
        elif(state == "Wisconsin"):
            profit = record.get("Profit")
            Wisconsin.append(profit)   
        elif(state == "Wyoming"):
            profit = record.get("Profit")
            Wyoming.append(profit)               
    ts_Alabama = 0
    ts_Arizona = 0
    ts_Arkansas = 0
    ts_California = 0
    ts_Colorado = 0
    ts_Connecticut = 0
    ts_Delaware = 0
    ts_District_of_Columbia = 0
    ts_Florida = 0
    ts_Georgia = 0
    ts_Idaho = 0
    ts_Illinois = 0
    ts_Indiana = 0
    ts_Iowa = 0
    ts_Kansas = 0
    ts_Kentucky = 0
    ts_Louisiana = 0
    ts_Maine = 0
    ts_Maryland = 0
    ts_Massachusetts = 0
    ts_Michigan = 0
    ts_Minnesota = 0
    ts_Mississippi = 0
    ts_Missouri = 0
    ts_Montana = 0
    ts_Nebraska = 0
    ts_Nevada = 0
    ts_New_Hampshire = 0
    ts_New_Jersey = 0
    ts_New_Mexico = 0
    ts_New_York = 0
    ts_North_Carolina = 0
    ts_North_Dakota = 0
    ts_Ohio = 0
    ts_Oklahoma = 0
    ts_Oregon = 0
    ts_Pennsylvania = 0
    ts_Rhode_Island = 0
    ts_South_Carolina = 0
    ts_South_Dakota = 0
    ts_Tennessee = 0
    ts_Texas = 0
    ts_Utah = 0
    ts_Vermont = 0
    ts_Virginia = 0
    ts_Washington = 0
    ts_West_Virginia = 0
    ts_Wisconsin = 0
    ts_Wyoming = 0
    for i in range(len(Alabama)):
        ts_Alabama = ts_Alabama + Alabama[i]
    for i in range(len(Arizona)):
        ts_Arizona = ts_Arizona + Arizona[i] 
    for i in range(len(Arkansas)):
        ts_Arkansas = ts_Arkansas + Arkansas[i]    
    for i in range(len(California)):
        ts_California = ts_California + California[i]
    for i in range(len(Colorado)):
        ts_Colorado = ts_Colorado + Colorado[i]
    for i in range(len(Connecticut)):
        ts_Connecticut = ts_Connecticut + Connecticut[i]
    for i in range(len(Delaware)):
        ts_Delaware = ts_Delaware + Delaware[i]
    for i in range(len(District_of_Columbia)):
        ts_District_of_Columbia = ts_District_of_Columbia + District_of_Columbia[i]
    for i in range(len(Florida)):
        ts_Florida = ts_Florida + Florida[i]
    for i in range(len(Georgia)):
        ts_Georgia = ts_Georgia + Georgia[i]
    for i in range(len(Idaho)):
        ts_Idaho = ts_Idaho + Idaho[i]
    for i in range(len(Illinois)):
        ts_Illinois = ts_Illinois + Illinois[i]
    for i in range(len(Indiana)):
        ts_Indiana = ts_Indiana + Indiana[i]
    for i in range(len(Iowa)):
        ts_Iowa = ts_Iowa + Iowa[i]
    for i in range(len(Kansas)):
        ts_Kansas = ts_Kansas + Kansas[i]
    for i in range(len(Kentucky)):
        ts_Kentucky = ts_Kentucky + Kentucky[i]
    for i in range(len(Louisiana)):
        ts_Louisiana = ts_Louisiana + Louisiana[i]
    for i in range(len(Maine)):
        ts_Maine = ts_Maine + Maine[i]
    for i in range(len(Maryland)):
        ts_Maryland = ts_Maryland + Maryland[i]
    for i in range(len(Massachusetts)):
        ts_Massachusetts = ts_Massachusetts + Massachusetts[i]
    for i in range(len(Michigan)):
        ts_Michigan = ts_Michigan + Michigan[i]
    for i in range(len(Minnesota)):
        ts_Minnesota = ts_Minnesota + Minnesota[i]
    for i in range(len(Mississippi)):
        ts_Mississippi = ts_Mississippi + Mississippi[i]
    for i in range(len(Missouri)):
        ts_Missouri = ts_Missouri + Missouri[i]
    for i in range(len(Montana)):
        ts_Montana = ts_Montana + Montana[i]
    for i in range(len(Nebraska)):
        ts_Nebraska = ts_Nebraska + Nebraska[i]
    for i in range(len(Nevada)):
        ts_Nevada = ts_Nevada + Nevada[i]
    for i in range(len(New_Hampshire)):
        ts_New_Hampshire = ts_New_Hampshire + New_Hampshire[i]
    for i in range(len(New_Jersey)):
        ts_New_Jersey = ts_New_Jersey + New_Jersey[i]
    for i in range(len(New_Mexico)):
        ts_New_Mexico = ts_New_Mexico + New_Mexico[i]
    for i in range(len(New_York)):
        ts_New_York = ts_New_York + New_York[i]
    for i in range(len(North_Carolina)):
        ts_North_Carolina = ts_North_Carolina + North_Carolina[i]
    for i in range(len(North_Dakota)):
        ts_North_Dakota = ts_North_Dakota + North_Dakota[i]
    for i in range(len(Ohio)):
        ts_Ohio = ts_Ohio + Ohio[i]
    for i in range(len(Oklahoma)):
        ts_Oklahoma = ts_Oklahoma + Oklahoma[i]
    for i in range(len(Oregon)):
        ts_Oregon = ts_Oregon + Oregon[i]
    for i in range(len(Pennsylvania)):
        ts_Pennsylvania = ts_Pennsylvania + Pennsylvania[i]
    for i in range(len(Rhode_Island)):
        ts_Rhode_Island = ts_Rhode_Island + Rhode_Island[i]
    for i in range(len(South_Carolina)):
        ts_South_Carolina = ts_South_Carolina + South_Carolina[i]
    for i in range(len(South_Dakota)):
        ts_South_Dakota = ts_South_Dakota + South_Dakota[i]
    for i in range(len(Tennessee)):
        ts_Tennessee = ts_Tennessee + Tennessee[i]
    for i in range(len(Texas)):
        ts_Texas = ts_Texas + Texas[i]
    for i in range(len(Utah)):
        ts_Utah = ts_Utah + Utah[i]
    for i in range(len(Vermont)):
        ts_Vermont = ts_Vermont + Vermont[i]
    for i in range(len(Virginia)):
        ts_Virginia = ts_Virginia + Virginia[i]
    for i in range(len(Washington)):
        ts_Washington = ts_Washington + Washington[i]
    for i in range(len(West_Virginia)):
        ts_West_Virginia = ts_West_Virginia + West_Virginia[i]
    for i in range(len(Wisconsin)):
        ts_Wisconsin = ts_Wisconsin + Wisconsin[i]
    for i in range(len(Wyoming)):
        ts_Wyoming = ts_Wyoming + Wyoming[i]
    print("<Profit for each State>\nAlabama : {0}\nArizona : {1}\nArkansas : {2}\nCalifornia : {3}\nColorado : {4}\nConnecticut : {5}\nDelaware : {6}\nDistrict of Columbia : {7}\nFlorida : {8}\nGeorgia : {9}\nIdaho : {10}\nIllinois : {11}\nIndiana : {12}\nIowa : {13}\nKansas : {14}\nKentucky : {15}\nLouisiana : {16}\nMaine : {17}\nMaryland : {18}\nMassachusetts : {19}\nMichigan : {20}\nMinnesota : {21}\nMississippi : {22}\nMissouri : {23}\nMontana : {24}\nNebraska : {25}\nNevada : {26}\nNew Hampshire : {27}\nNew Jersey : {28}\nNew Mexico : {29}\nNew York : {30}\nNorth Carolina : {31}\nNorth Dakota : {32}\nOhio : {33}\nOklahoma : {34}\nOregon : {35}\nPennsylvania : {36}\nRhode Island : {37}\nSouth Carolina : {38}\nSouth Dakota : {39}\nTennessee : {40}\nTexas : {41}\nUtah : {42}\nVermont : {43}\nVirginia : {44}\nWashington : {45}\nWest Virginia : {46}\nWisconsin : {47}\nWyoming : {48}".format(ts_Alabama,ts_Arizona,ts_Arkansas,ts_California,ts_Colorado,ts_Connecticut,ts_Delaware,ts_District_of_Columbia,ts_Florida,ts_Georgia,ts_Idaho,ts_Illinois,ts_Indiana,ts_Iowa,ts_Kansas,ts_Kentucky,ts_Louisiana,ts_Maine,ts_Maryland,ts_Massachusetts,ts_Michigan,ts_Minnesota,ts_Mississippi,ts_Missouri,ts_Montana,ts_Nebraska,ts_Nevada,ts_New_Hampshire,ts_New_Jersey,ts_New_Mexico,ts_New_York,ts_North_Carolina,ts_North_Dakota,ts_Ohio,ts_Oklahoma,ts_Oregon,ts_Pennsylvania,ts_Rhode_Island,ts_South_Carolina,ts_South_Dakota,ts_Tennessee,ts_Texas,ts_Utah,ts_Vermont,ts_Virginia,ts_Washington,ts_West_Virginia,ts_Wisconsin,ts_Wyoming))

def BestSellingSubCategory(data):
    data = getData()
    Alabama = []
    Arizona = []
    Arkansas = []
    California = []
    Colorado = []
    Connecticut = []
    Delaware = []
    District_of_Columbia = []
    Florida = []
    Georgia = []
    Idaho = []
    Illinois = []
    Indiana = []
    Iowa = []
    Kansas = []
    Kentucky = []
    Louisiana = []
    Maine = []
    Maryland = []
    Massachusetts = []
    Michigan = []
    Minnesota = []
    Mississippi = []
    Missouri = []
    Montana = []
    Nebraska = []
    Nevada = []
    New_Hampshire = []
    New_Jersey = []
    New_Mexico = []
    New_York = []
    North_Carolina = []
    North_Dakota = []
    Ohio = []
    Oklahoma = []
    Oregon = []
    Pennsylvania = []
    Rhode_Island = []
    South_Carolina = []
    South_Dakota = []
    Tennessee = []
    Texas = []
    Utah = []
    Vermont = []
    Virginia = []
    Washington = []
    West_Virginia = []
    Wisconsin = []
    Wyoming = []
    for record in data:
        state = record.get("State")
        if(state == "Alabama"):
            sub_category = record.get("Sub-Category")
            Alabama.append(sub_category)
        elif(state == "Arizona"):
            sub_category = record.get("Sub-Category")
            Arizona.append(sub_category)
        elif(state == "Arkansas"):
            sub_category = record.get("Sub-Category")
            Arkansas.append(sub_category)
        elif(state == "California"):
            sub_category = record.get("Sub-Category")
            California.append(sub_category)
        elif(state == "Colorado"):
            sub_category = record.get("Sub-Category")
            Colorado.append(sub_category)
        elif(state == "Connecticut"):
            sub_category = record.get("Sub-Category")
            Connecticut.append(sub_category)
        elif(state == "Delaware"):
            sub_category = record.get("Sub-Category")
            Delaware.append(sub_category)
        elif(state == "District of Columbia"):
            sub_category = record.get("Sub-Category")
            District_of_Columbia.append(sub_category)       
        elif(state == "Florida"):
            sub_category = record.get("Sub-Category")
            Florida.append(sub_category)
        elif(state == "Georgia"):
            sub_category = record.get("Sub-Category")
            Georgia.append(sub_category)
        elif(state == "Idaho"):
            sub_category = record.get("Sub-Category")
            Idaho.append(sub_category)
        elif(state == "Illinois"):
            sub_category = record.get("Sub-Category")
            Illinois.append(sub_category)
        elif(state == "Indiana"):
            sub_category = record.get("Sub-Category")
            Indiana.append(sub_category) 
        elif(state == "Iowa"):
            sub_category = record.get("Sub-Category")
            Iowa.append(sub_category)
        elif(state == "Kansas"):
            sub_category = record.get("Sub-Category")
            Kansas.append(sub_category) 
        elif(state == "Kentucky"):
            sub_category = record.get("Sub-Category")
            Kentucky.append(sub_category) 
        elif(state == "Louisiana"):
            sub_category = record.get("Sub-Category")
            Louisiana.append(sub_category) 
        elif(state == "Maine"):
            sub_category = record.get("Sub-Category")
            Maine.append(sub_category)
        elif(state == "Maryland"):
            sub_category = record.get("Sub-Category")
            Maryland.append(sub_category)
        elif(state == "Massachusetts"):
            sub_category = record.get("Sub-Category")
            Massachusetts.append(sub_category)
        elif(state == "Michigan"):
            sub_category = record.get("Sub-Category")
            Michigan.append(sub_category)   
        elif(state == "Minnesota"):
            sub_category = record.get("Sub-Category")
            Minnesota.append(sub_category)   
        elif(state == "Mississippi"):
            sub_category = record.get("Sub-Category")
            Mississippi.append(sub_category) 
        elif(state == "Missouri"):
            sub_category = record.get("Sub-Category")
            Missouri.append(sub_category)   
        elif(state == "Montana"):
            sub_category = record.get("Sub-Category")
            Montana.append(sub_category)  
        elif(state == "Nebraska"):
            sub_category = record.get("Sub-Category")
            Nebraska.append(sub_category)  
        elif(state == "Nevada"):
            sub_category = record.get("Sub-Category")
            Nevada.append(sub_category) 
        elif(state == "New Hampshire"):
            sub_category = record.get("Sub-Category")
            New_Hampshire.append(sub_category)   
        elif(state == "New Jersey"):
            sub_category = record.get("Sub-Category")
            New_Jersey.append(sub_category)  
        elif(state == "New Mexico"):
            sub_category = record.get("Sub-Category")
            New_Mexico.append(sub_category)  
        elif(state == "New York"):
            sub_category = record.get("Sub-Category")
            New_York.append(sub_category)  
        elif(state == "North Carolina"):
            sub_category = record.get("Sub-Category")
            North_Carolina.append(sub_category)   
        elif(state == "North Dakota"):
            sub_category = record.get("Sub-Category")
            North_Dakota.append(sub_category)   
        elif(state == "Ohio"):
            sub_category = record.get("Sub-Category")
            Ohio.append(sub_category)  
        elif(state == "Oklahoma"):
            sub_category = record.get("Sub-Category")
            Oklahoma.append(sub_category)
        elif(state == "Oregon"):
            sub_category = record.get("Sub-Category")
            Oregon.append(sub_category)  
        elif(state == "Pennsylvania"):
            sub_category = record.get("Sub-Category")
            Pennsylvania.append(sub_category)  
        elif(state == "Rhode Island"):
            sub_category = record.get("Sub-Category")
            Rhode_Island.append(sub_category)
        elif(state == "South Carolina"):
            sub_category = record.get("Sub-Category")
            South_Carolina.append(sub_category) 
        elif(state == "South Dakota"):
            sub_category = record.get("Sub-Category")
            South_Dakota.append(sub_category)
        elif(state == "Tennessee"):
            sub_category = record.get("Sub-Category")
            Tennessee.append(sub_category) 
        elif(state == "Texas"):
            sub_category = record.get("Sub-Category")
            Texas.append(sub_category) 
        elif(state == "Utah"):
            sub_category = record.get("Sub-Category")
            Utah.append(sub_category) 
        elif(state == "Vermont"):
            sub_category = record.get("Sub-Category")
            Vermont.append(sub_category) 
        elif(state == "Virginia"):
            sub_category = record.get("Sub-Category")
            Virginia.append(sub_category)
        elif(state == "Washington"):
            sub_category = record.get("Sub-Category")
            Washington.append(sub_category)
        elif(state == "West Virginia"):
            sub_category = record.get("Sub-Category")
            West_Virginia.append(sub_category)     
        elif(state == "Wisconsin"):
            sub_category = record.get("Sub-Category")
            Wisconsin.append(sub_category) 
        elif(state == "Wyoming"):
            sub_category = record.get("Sub-Category")
            Wyoming.append(sub_category)             
    print("<Best-selling Sub-Category for each State>\nAlabama : {0}\nArizona : {1}\nArkansas : {2}\nCalifornia : {3}\nColorado : {4}\nConnecticut : {5}\nDelaware : {6}\nDistrict of Columbia : {7}\nFlorida : {8}\nGeorgia : {9}\nIdaho : {10}\nIllinois : {11}\nIndiana : {12}\nIowa : {13}\nKansas : {14}\nKentucky : {15}\nLouisiana : {16}\nMaine : {17}\nMaryland : {18}\nMassachusetts : {19}\nMichigan : {20}\nMinnesota : {21}\nMississippi : {22}\nMissouri : {23}\nMontana : {24}\nNebraska : {25}\nNevada : {26}\nNew Hampshire : {27}\nNew Jersey : {28}\nNew Mexico : {29}\nNew York : {30}\nNorth Carolina : {31}\nNorth Dakota : {32}\nOhio : {33}\nOklahoma : {34}\nOregon : {35}\nPennsylvania : {36}\nRhode Island : {37}\nSouth Carolina : {38}\nSouth Dakota : {39}\nTennessee : {40}\nTexas : {41}\nUtah : {42}\nVermont : {43}\nVirginia : {44}\nWashington : {45}\nWest Virginia : {46}\nWisconsin : {47}\nWyoming : {48}".format(max(Alabama),max(Arizona),max(Arkansas),max(California),max(Colorado),max(Connecticut),max(Delaware),max(District_of_Columbia),max(Florida),max(Georgia),max(Idaho),max(Illinois),max(Indiana),max(Iowa),max(Kansas),max(Kentucky),max(Louisiana),max(Maine),max(Maryland),max(Massachusetts),max(Michigan),max(Minnesota),max(Mississippi),max(Missouri),max(Montana),max(Nebraska),max(Nevada),max(New_Hampshire),max(New_Jersey),max(New_Mexico),max(New_York),max(North_Carolina),max(North_Dakota),max(Ohio),max(Oklahoma),max(Oregon),max(Pennsylvania),max(Rhode_Island),max(South_Carolina),max(South_Dakota),max(Tennessee),max(Texas),max(Utah),max(Vermont),max(Virginia),max(Washington),max(West_Virginia),max(Wisconsin),max(Wyoming)))

data = getData()
TotalSales(data)
TotalProfit(data)
print()
SalesForEachCategory(data)
print()
ProfitForEachCategory(data)
print()
SalesForEachState(data)
print()
ProfitForEachState(data)
print()
BestSellingSubCategory(data)

path = "report.txt"

with open(path, "w") as report_file:
    report_file.write("[Superstore Report]\n")
    report_file.write("Total Sales : 2297200.860299955\n")
    report_file.write("Total Profit : 286397.0217000013\n\n")
    report_file.write("Sales for Furniture : 741999.7952999998\nSales for Office Supplies : 719047.0320000029\nSales for Technology : 836154.0329999966\n\n")
    report_file.write("Profit for Furniture : 18451.2728\nProfit for Office Supplies : 122490.80080000011\nProfit for Technology : 145454.9480999999\n\n")
    report_file.write("<Sales for each State>\nAlabama: 19510.639999999992, Arizona: 35282.001, Arkansas: 11678.129999999997, Colorado: 32108.117999999995, Connecticut: 13384.356999999996, Delaware: 27451.068999999992, District of Columbia: 2865.0199999999995, Florida: 89473.708, Georgia: 49095.840000000004, Idaho: 4382.486000000002, Illinois: 80166.10099999986, Indiana: 53555.36, Iowa: 4579.759999999999,, Kentucky: 36591.74999999997, Louisiana: 9217.029999999999, Maine: 1270.5300000000002, Maryland: 23705.523, Massachusetts: 28634.433999999994, Michigan: 76269.61400000002, Minnesota: 29863.149999999994, Mississippi: 10771.34, Missouri: 22205.149999999998, Montana: 5589.351999999997, Nebraska: 7464.9299999999985, Nevada: 16729.102, New Hampshire: 7292.523999999999, New Jersey: 35764.31200000001, New Mexico: 4783.521999999999, New York: 310876.2709999998, North Carolina: 55603.16399999997, North Dakota: 919.91, Ohio: 78258.13599999993, Oklahoma: 19683.39, Oregon: 17431.14999999999, Pennsylvania: 116511.91400000003, Rhode Island: 22627.955999999995, South Carolina: 8481.71, South Dakota: 1315.5600000000002, Tennessee: 30661.87299999998, Texas: 170188.04580000002, Utah: 11220.055999999999, Vermont: 8929.369999999999, Virginia: 70636.71999999999, Washington: 138641.26999999993, West Virginia: 1209.824, Wisconsin: 32114.61000000002, Wyoming: 1603.136\n\n")
    report_file.write("<Profit for each State>\nAlabama: 5786.825299999999, Arizona: -3427.9246, Arkansas: 4008.6871, California: 76381.38710000017, Colorado: -6527.857900000001, Connecticut: 3511.4918000000002, Delaware: 9977.374800000001, District of Columbia: 1059.5892999999999, Florida: -3399.3017, Georgia: 16250.043300000003, Idaho: 826.7230999999999, Illinois: -12607.88699999998, Indiana: 18382.936300000005, Iowa: 1183.8119000000002, Kansas: 836.4435000000001, Kentucky: 11199.696600000005, Louisiana: 2196.102300000001, Maine: 454.4862, Maryland: 7031.178799999997, Massachusetts: 6785.501600000005, Michigan: 24463.187599999994, Minnesota: 10823.1874, Mississippi: 3172.9761999999982, Missouri: 6436.210499999999, Montana: 1833.3285, Nebraska: 2037.0942000000007, Nevada: 3316.7659, New Hampshire: 1706.5028, New Jersey: 9772.9138, New Mexico: 1157.1161, New York: 74038.54860000005, North Carolina: -7490.912200000003, North Dakota: 230.14969999999997, Ohio: -16971.376600000018, Oklahoma: 4853.956, Oregon: -1190.4704999999992, Pennsylvania: -15559.960300000013, Rhode Island: 7285.629300000001, South Carolina: 1769.0566000000003, South Dakota: 394.8283, Tennessee: -5341.6936, Texas: -25729.3563, Utah: 2546.5335000000005, Vermont: 2244.9783, Virginia: 18597.9504, Washington: 33402.651699999995, West Virginia: 185.9216, Wisconsin: 8401.800399999998, Wyoming: 100.196\n\n")
    report_file.write("<Best-selling Sub-Category for each State>\nAlabama : Tables, Arizona : Tables, Arkansas : Tables, California : Tables, Colorado : Tables, Connecticut : Tables, Delaware : Tables, District of Columbia : Paper, Florida : Tables, Georgia : Tables, Idaho : Tables, Illinois : Tables, Indiana : Tables, Iowa : Tables, Kansas : Supplies, Kentucky : Tables, Louisiana : Tables, Maine : Phones, Maryland : Tables, Massachusetts : Tables, Michigan : Tables, Minnesota : Tables, Mississippi : Tables, Missouri : Tables, Montana : Storage, Nebraska : Supplies, Nevada : Tables, New Hampshire : Tables, New Jersey : Tables, New Mexico : Supplies, New York : Tables, North Carolina : Tables, North Dakota : Storage, Ohio : Tables, Oklahoma : Tables, Oregon : Tables, Pennsylvania : Tables, Rhode Island : Tables, South Carolina : Storage, South Dakota : Supplies, Tennessee : Tables, Texas : Tables, Utah : Tables, Vermont : Storage, Virginia : Tables, Washington : Tables, West Virginia : Tables, Wisconsin : Tables, Wyoming : Chairs")
