import cmd
import shlex
import sys
import json
connection = {
    "AnimalFeed":[],
    "AntigravityBoots":[],
    "Backpack":[["Textiles",2],["Plastic",2],["MeasuringTape",1]],
    "BBQGrill":[["Metal",3],["CookingUtensils",1]],
    "Beef":[["AnimalFeed",3]],
    "Bobby'sHelmet":[],
    "BreadRoll":[["FlourBag",2],["Cream",1]],
    "Bricks":[["Minerals",2]],
    "Burgers":[["Beef",1],["BreadRoll",1],["BBQGrill",1]],
    "BusinessSuits":[["Textiles",3],["MeasuringTape",1],["Glue",1]],
    "Cap":[["Textiles",2],["MeasuringTape",1]],
    "CarTire":[["CrudeOil",2],["Glue",1],["Nails",3]],
    "Cement":[["Minerals",2],["Chemicals",1]],
    "Chairs":[["Wood",2],["Nails",1],["Hammer",1]],
    "CheeseFries":[["Vegetables",1],["Cheese",1]],
    "Cheese":[["AnimalFeed",2]],
    "Chemicals":[],
    "CherryCheesecake":[["FlourBag",1],["Watermelon",1],["Cheese",1]],
    "Coffee":[["Cream",1],["Seeds",2],["SugarandSpices",1]],
    "coffeemaker?":[],
    "CookingUtensils":[["Metal",2],["Plastic",2],["Wood",2]],
    "Corn":[["Minerals",1],["Seeds",4]],
    "Couch":[["Textiles",3],["Drill",1],["Glue",1]],
    "Cream":[["AnimalFeed",1]],
    "CrudeOil":[],
    "Cupboard":[["Planks",2],["Glass",2],["Paint",1]],
    "Donuts":[["FlourBag",1],["SugarandSpices",1]],
    "DozerBlade":[],
    "DozerExhaust":[],
    "DozerWheel":[],
    "Drill":[["Metal",2],["Plastic",2],["ElectricalComponent",1]],
    "EcologicalShoes":[["RecycledFabric",2],["Glue",1],["MeasuringTape",1]],
    "ElectricalComponent":[],
    "Engine":[["ElectricalComponent",1],["Drill",1],["Nails",3]],
    "FashionClothes":[],
    "FirePit":[["Bricks",2],["Shovel",1],["Cement",2]],
    "floatingsquares?":[],
    "FlourBag":[["Seeds",2],["Textiles",2]],
    "Freezer?":[],
    "FrozenYogurt":[["Watermelon",1],["Cream",1],["SugarandSpices",1]],
    "GardenFurniture":[["Planks",2],["Plastic",2],["Textiles",2]],
    "GardenGnome":[["Cement",2],["Glue",1]],
    "Glass":[],
    "Glue":[["Plastic",1],["Chemicals",2]],
    "Grass":[["Seeds",1],["Shovel",1]],
    "GreenSmoothie":[["Vegetables",1],["Watermelon",1]],
    "Hammer":[["Metal",1],["Wood",1]],
    "Holoprojector":[],
    "HomeTextiles":[["Textiles",2],["MeasuringTape",1]],
    "Hoverboard":[],
    "IceCreamSandwich":[["BreadRoll",1],["Cream",1]],
    "Jetpack":[],
    "LaBaguette":[],
    "Ladder":[["Planks",2],["Metal",2]],
    "Lantern":[],
    "LawnMower":[["Metal",3],["Paint",1],["ElectricalComponent",1]],
    "LemonadeBottle":[["Glass",2],["SugarandSpices",2],["Watermelon",1]],
    "Lifebelt":[],
    "LightingSystem":[["Chemicals",1],["ElectricalComponent",1],["Glass",1]],
    "MeasuringTape":[["Metal",1],["Plastic",1]],
    "Metal":[],
    "MicrowaveOven":[["Metal",4],["Glass",1],["ElectricalComponent",1]],
    "Minerals":[],
    "MotorOil":[["CrudeOil",2]],
    "Nails":[["Metal",2]],
    "Paint":[["Metal",2],["Minerals",1],["Chemicals",2]],
    "ParisBag":[],
    "Pizza":[["FlourBag",1],["Cheese",1],["Beef",1]],
    "Planks":[["Wood",2]],
    "Plastic":[],
    "Plunger":[],
    "RecycledFabric":[],
    "Refrigerator":[["Plastic",2],["Chemicals",2],["ElectricalComponent",2]],
    "ReusableBag":[["RecycledFabric",2]],
    "RubberBoots":[],
    "ScubaMask":[],
    "Seeds":[],
    "Ship'sWheel":[],
    "Shoes":[["Textiles",2],["Plastic",1],["Glue",1]],
    "Shovel":[["Metal",1],["Wood",1],["Plastic",1]],
    "Snowboard":[],
    "SolarPanels":[],
    "StorageBars":[],
    "StorageCamera":[],
    "StorageLocks":[],
    "SugarandSpices":[],
    "Tables":[["Planks",1],["Nails",2],["Hammer",1]],
    "Teapot":[],
    "Telepod":[],
    "Textiles":[],
    "TreeSaplings":[["Seeds",2],["Shovel",1]],
    "TV":[["Plastic",2],["Glass",2],["ElectricalComponent",2]],
    "Vegetables":[["Seeds",2]],
    "Vu'sBattery":[],
    "Vu'sGloves":[],
    "Vu'sRemote":[],
    "Watch":[["Plastic",2],["Glass",1],["Chemicals",1]],
    "Watermelon":[["Seeds",2],["TreeSaplings",1]],
    "WinterHat":[],
    "YogaMat":[["RecycledFabric",3],["HomeTextiles",2],["Paint",1]],
    "Wood":[]
}
files = ["need.json", "resBuild1.json", "latAmBuil1.json", "resBuild2.json"]

singleBuilding = "resBuild2.json"
class MyCmd(cmd.Cmd):
    def do_quit(self, s):
        '''quit - quit the program'''
        sys.exit(0)

    def do_resources(self, s):
        '''resources - Print the list of resources'''
        list = ["AnimalFeed",	"AntigravityBoots",	"Backpack",	"BBQGrill",	"Beef",	"Bobby'sHelmet",	"BreadRoll",	"Bricks",	"Burgers",	"BusinessSuits",	"Cap",	"CarTire",	"Cement",	"Chairs",	"CheeseFries",	"Cheese",	"Chemicals",	"CherryCheesecake",	"Coffee",	"coffeemaker?",	"CookingUtensils",	"Corn",	"Couch",	"Cream",	"CrudeOil",	"Cupboard",	"Donuts",	"DozerBlade",	"DozerExhaust",	"DozerWheel",	"Drill",	"EcologicalShoes",	"ElectricalComponent",	"Engine",	"FashionClothes",	"FirePit",	"floatingsquares?",	"FlourBag",	"Freezer?",	"FrozenYogurt",	"GardenFurniture",	"GardenGnome",	"Glass",	"Glue",	"Grass",	"GreenSmoothie",	"Hammer",	"Holoprojector",	"HomeTextiles",	"Hoverboard",	"IceCreamSandwich",	"Jetpack",	"LaBaguette",	"Ladder",	"Lantern",	"LawnMower",	"LemonadeBottle",	"Lifebelt",	"LightingSystem",	"Metal",	"MicrowaveOven",	"Minerals",	"MotorOil",	"Nails",	"Paint",	"ParisBag",	"Pizza",	"Planks",	"Plastic",	"Plunger",	"RecycledFabric",	"Refrigerator",	"ReusableBag",	"RubberBoots",	"ScubaMask",	"Seeds",	"Ship'sWheel",	"Shoes",	"Shovel",	"Snowboard",	"SolarPanels",	"StorageBars",	"StorageCamera",	"StorageLocks",	"SugarandSpices",	"Tables",	"TapeMeasurer",	"Teapot",	"Telepod",	"Textiles",	"TreeSaplings",	"TV",	"Vegetables",	"Vu'sBattery",	"Vu'sGloves",	"Vu'sRemote",	"Watch",	"Watermelon",	"WinterHat",	"Wood",	"YogaMat"]
        for resource in list:
            print(resource)

    def do_mainNeed(self, arguments):
        '''mainneed - Edit need file. Enter resources and number space separated'''
        PATH_TO_JSON = singleBuilding #  assuming same directory (but you can work your magic here with os.)
        arguments = arguments.split()
# read existing json to memory. you do this to preserve whatever existing data.
        with open(PATH_TO_JSON,'r') as jsonfile:
            needDic = json.load(jsonfile)
        for x in range(0, len(arguments),2):
            if arguments[x+1] in needDic:
                for y in range(int(arguments[x])):
                    needDic[arguments[x+1]] += 1
            else:
                print(arguments[x+1], "not there")

        with open(PATH_TO_JSON,'w') as jsonfile:
            json.dump(needDic, jsonfile, indent=4)

    def do_need(self, arguments):
        '''need - Edit need file. Enter resources and number space separated'''
        PATH_TO_JSON = singleBuilding
        arguments = arguments.split()
        with open(PATH_TO_JSON,'r') as jsonfile:
            needDic = json.load(jsonfile)
        with open('have.json','r') as jsonfile:
            haveDic = json.load(jsonfile)

        goDeeper = []
        for resource in needDic:
            if needDic[resource] - haveDic[resource] > 0:
                goDeeper.append(resource)
        while len(goDeeper) > 0:
            for path in connection[goDeeper[0]]:
                if needDic[goDeeper[0]] - haveDic[goDeeper[0]] > 0:
                    needDic[path[0]] += path[1] * (needDic[goDeeper[0]]- haveDic[goDeeper[0]])
                    goDeeper.append(path[0])
            goDeeper.remove(goDeeper[0])

        PATH_TO_JSON = 'have.json'
        with open(PATH_TO_JSON, 'r') as jsonfile:
            haveDic = json.load(jsonfile)
        total = 0
        for resource in needDic:
            if needDic[resource] != 0 and needDic[resource] - haveDic[resource] > 0:
                total += needDic[resource] - haveDic[resource]
                print(needDic[resource] - haveDic[resource], resource)
        print("Total: ", total)

    def do_have(self, arguments):
        '''have - Edit have file. Enter number then resource space separated'''
        PATH_TO_JSON = 'have.json'
        arguments = arguments.split()
        with open(PATH_TO_JSON,'r') as jsonfile:
            haveDic = json.load(jsonfile)
        for x in range(0, len(arguments),2):
            if arguments[x+1] in haveDic:
                haveDic[arguments[x+1]] = int(arguments[x])
            else:
                print(arguments[x+1], "not there")

        with open(PATH_TO_JSON,'w') as jsonfile:
            json.dump(haveDic, jsonfile, indent=4)

    def do_get(self, s):
        '''get - Only mainNeed Print number of each thing needed'''
        PATH_TO_JSON = 'have.json'
        with open(PATH_TO_JSON,'r') as jsonfile:
            haveDic = json.load(jsonfile)
        PATH_TO_JSON = singleBuilding
        with open(PATH_TO_JSON,'r') as jsonfile:
            needDic = json.load(jsonfile)
        total = 0
        for resource in needDic:
            if needDic[resource] != 0 and needDic[resource]- haveDic[resource] > 0:
                total += needDic[resource]- haveDic[resource]
                print(needDic[resource]- haveDic[resource],resource)
        print("Total: ", total)

    def do_total(self, s):
        '''total - Print total of have and need'''
        PATH_TO_JSON = 'have.json'
        with open(PATH_TO_JSON,'r') as jsonfile:
            haveDic = json.load(jsonfile)
        PATH_TO_JSON = singleBuilding
        with open(PATH_TO_JSON,'r') as jsonfile:
            needDic = json.load(jsonfile)
        haveTotal = 0
        for resource in haveDic:
            haveTotal += haveDic[resource]
        print("have: ", haveTotal)
        needTotal = 0
        for resource in needDic:
            needTotal += needDic[resource]
        print("need: ", needTotal)

    def do_reset(self, argument):
        '''reset - Resets need index of file'''
        print(files)
        if argument != "":
            PATH_TO_JSON = files[int(argument)]
        else:
            PATH_TO_JSON = singleBuilding
        with open(PATH_TO_JSON,'r') as jsonfile:
            needDic = json.load(jsonfile)

        for resource in needDic:
            needDic[resource] = 0

        with open(PATH_TO_JSON,'w') as jsonfile:
            json.dump(needDic, jsonfile, indent=4)

    def do_info(self, s):
        '''files - Print files or singleBuilding'''
        PATH_TO_JSON = 'have.json'
        with open(PATH_TO_JSON, 'r') as jsonfile:
            haveDic = json.load(jsonfile)
        print(files)
        print(singleBuilding)
        if s == "have":
            d = sorted(haveDic, key=haveDic.get)
            for key in d:
                print(haveDic[key], key)


if __name__ == '__main__':
    cmd = MyCmd()
    cmd.cmdloop('type help for a list of valid commands')
