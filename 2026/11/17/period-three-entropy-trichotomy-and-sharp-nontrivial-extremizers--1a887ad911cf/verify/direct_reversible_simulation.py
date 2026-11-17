"""Independent exhaustive dynamical verification on all 256 rules, ring lengths 3..6.
Python 3 standard library only. Run: python verify/direct_reversible_simulation.py.
"""
import hashlib
import json

EXPECTED_SHA256='8b3dd0c8f39afe4fa27d5682c028881e732c0a3f761d8481be4a33301fa4ca4d'

def evolve(rule, past, present, n):
    future=past
    for i in range(n):
        left=(present>>((i-1)%n))&1
        center=(present>>i)&1
        right=(present>>((i+1)%n))&1
        j=4*left+2*center+right
        if (rule>>j)&1:future^=1<<i
    return present,future

rows=[]
for rule in range(256):
    counts=[]
    for n in range(3,7):
        cnt=0
        for a in range(1<<n):
            for b in range(1<<n):
                u,v=a,b
                for _ in range(3):u,v=evolve(rule,u,v,n)
                cnt+=(u==a and v==b)
        counts.append(cnt)
    rows.append(counts)
sha=hashlib.sha256(json.dumps(rows,separators=(',',':')).encode('ascii')).hexdigest()
assert sha==EXPECTED_SHA256,(sha,EXPECTED_SHA256)
print(json.dumps({'all_256_rules_all_states_n_3_to_6':'PASS','sha256':sha,
                  'n_3_to_6':{'50':rows[50],'51':rows[51],
                                '76':rows[76],'110':rows[110],
                                '115':rows[115],'167':rows[167],
                                '204':rows[204]}},sort_keys=True))
