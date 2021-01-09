"""
=====================================================
 ordperm_saphana - Create permutations of orderlines over eligible suppliers
=====================================================
:Author: Veikko Nyfors <veikkonyfors@gmail.com>
:Description: To be implemented as SAP/Hana stored procedure

"""

input = {
    "4711": ["A"],
    "4712": ["B","C","D"],
    "4713": ["C","E"]
}

ordlns = {}
n=1
combinations=1
index={}
numsup={}

for item in input.keys():
    index[item]=0
    numsup[item]=len(input[item])
    combinations*=len(input[item])
    
items=len(input)

for line in range(combinations):
    for item in input.keys():
        ordlns[item]=input[item][index[item]]
        if index[item]>=numsup[item]-1:
            index[item]=0
        else:
            index[item]+=1
    print (str(n)+" "+str(ordlns))
    n+=1
