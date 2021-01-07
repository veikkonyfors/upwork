input = {
    "4711": ["A"],
    "4712": ["B","C","D"],
    "4713": ["C","E"]
}

ordlns = {}
n=0
combinations=1
index={}
numsup={}

for item in input.keys():
    index[item]=0
    numsup[item]=len(input[item])
    combinations*=len(input[item])
    
items=len(input)

for line in range(combinations):
    print("line "+str(line))
    for item in input.keys():
        ordlns[item]=input[item][index[item]]
        if index[item]>=numsup[item]-1:
            index[item]=0
        else:
            index[item]+=1
    print (str(n)+" "+str(ordlns))
      
n+=1
