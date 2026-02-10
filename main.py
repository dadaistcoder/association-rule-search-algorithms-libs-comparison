from apriori_python import apriori
from efficient_apriori import apriori as effAp
from fpgrowth_py import fpgrowth
import time
import matplotlib.pyplot as plt

def load_transactions(filename):
    trans = {}
    with open(filename) as file:
        next(file)
        for line in file:
            parts = line.strip().split(',')
            trans_id, item = parts[2], parts[3]
            if item == 'NONE':
                continue
            if trans_id not in trans:
                trans[trans_id] = []
            if item not in trans[trans_id]:
                trans[trans_id].append(item)
    return list(trans.values())


def run_apriori(trans, min_sup, min_conf):
    return apriori(trans, minSup=min_sup, minConf=min_conf)

def run_eff_apriori(trans, min_sup, min_conf):
    return effAp(trans, min_support=min_sup, min_confidence=min_conf)

def run_fpgrowth(trans, min_sup, min_conf):
    return fpgrowth(trans, minSupRatio=min_sup, minConf=min_conf)

runs = {
    "\nAPRIORI PYTHON\n":run_apriori,
    "\nEFFICIENT APRIORI\n":run_eff_apriori,
    "\nFPGROWTH\n":run_fpgrowth
    }

def run(name, func, trans, min_sup, min_conf):
        start = time.time()
        freq, rules = func(trans, min_sup, min_conf)
        total_time = time.time() - start
        return rules, total_time

        

# main

min_sup = float(input("min_sup: "))
min_conf = float(input("min_conf: "))

print("\nVERSION FROM REPO")
trans = load_transactions('BreadBasket_DMS.csv')

for name, func in runs.items():
    print(name)
    print(run(name, func, trans, min_sup, min_conf))
    


    
trans1 = [
    ["ball", "cleats"],
    ["dumbbells", "jump rope", "mat"],
    ["goggles", "cap"],
    ["tent", "backpack", "thermos"],
    ["snowboard", "helmet", "gloves"],
    ["swimsuit", "goggles"],
    ["sleeping bag", "tent"],
    ["skis", "poles", "helmet"],
    ["uniform", "leggings"],
    ["gloves", "helmet"],
    ["backpack", "thermos"],
    ["resistance bands", "dumbbells", "mat"],
    ["fins", "swim trunks"],
    ["ball", "leggings", "cleats"],
    ["thermos", "sleeping bag", "tent"],
    ["skis", "gloves"],
    ["cap", "goggles"],
    ["mat", "backpack"],
    ["jump rope", "dumbbells"],
    ["snowboard", "gloves", "helmet"],
    ["uniform", "cleats"],
    ["swimsuit", "cap", "goggles"],
    ["resistance bands", "jump rope"],
    ["leggings", "ball"],
    ["fins", "swim trunks", "goggles"],
    ["tent", "mat", "thermos"],
    ["cleats", "ball", "uniform"],
    ["dumbbells", "resistance bands", "expander", "mat"],
    ["backpack", "sleeping bag"],
    ["skis", "poles", "helmet", "gloves"]
]

print("\nTEST")
for name, func in runs.items():
    print(name)
    print(run(name, func, trans1, min_sup, min_conf))
  
names = [name for name, _ in runs.items()]
total_times = [run(name, func, trans, min_sup, min_conf)[1] for name, func in runs.items()]

plt.bar(names, total_times)
plt.show()

names1 = [name for name, _ in runs.items()]
total_times1 = [run(name, func, trans1, min_sup, min_conf)[1] for name, func in runs.items()]

plt.bar(names1, total_times1)
plt.show()