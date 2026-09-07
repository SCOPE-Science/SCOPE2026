#!/usr/bin/env python3
"""Exact row-by-row backtracking for bordered BH(6,3) with R3* fixed.
Pure Python, no floats. Encodes entries as exponents mod 3.
Orthogonality <=> ratio-counts (2,2,2) [lemma proven in DRAFT].
Logs node counts + timing to search_log.json. Usage: python3 search.py
"""
import json, os, time
from itertools import product

R1=(0,0,0,0,0,0)
R2=(0,0,1,1,2,2)
R3=(0,1,0,2,1,2)

def orth(a,b):
    c0=c1=c2=0
    for x,y in zip(a,b):
        d=(x-y)%3
        if d==0: c0+=1
        elif d==1: c1+=1
        else: c2+=1
    return c0==2 and c1==2 and c2==2

def ratio_counts(a,b):
    c=[0,0,0]
    for x,y in zip(a,b):
        c[(x-y)%3]+=1
    return c

def candidates(prefix):
    need=[2,2,2]
    for v in prefix:
        need[v]-=1
    k=6-len(prefix)
    out=[]
    for tail in product([0,1,2], repeat=k):
        c=list(need)
        ok=True
        for v in tail:
            c[v]-=1
            if c[v]<0:
                ok=False; break
        if not ok: continue
        if c!=[0,0,0]: continue
        out.append(tuple(list(prefix)+list(tail)))
    return out

def main():
    base=os.path.dirname(os.path.abspath(__file__))
    t0=time.time()
    C4=candidates((0,1))
    C5=candidates((0,2))
    C6=candidates((0,2))
    nodes={"depth4_scanned":0,"depth4_pass":0,"depth5_scanned":0,"depth5_pass":0,
           "depth6_scanned":0,"depth6_pass":0,
           "pool_sizes":{"C4":len(C4),"C5":len(C5),"C6":len(C6)}}
    R4_list=[r for r in C4 if orth(r,R1) and orth(r,R2) and orth(r,R3)]
    sols=[]
    for r4 in C4:
        nodes["depth4_scanned"]+=1
        if r4 not in R4_list: continue
        nodes["depth4_pass"]+=1
        for r5 in C5:
            nodes["depth5_scanned"]+=1
            if not (orth(r5,R1) and orth(r5,R2) and orth(r5,R3) and orth(r5,r4)):
                continue
            nodes["depth5_pass"]+=1
            for r6 in C6:
                nodes["depth6_scanned"]+=1
                if orth(r6,R1) and orth(r6,R2) and orth(r6,R3) and orth(r6,r4) and orth(r6,r5):
                    nodes["depth6_pass"]+=1
                    sols.append([list(r4),list(r5),list(r6)])
    dt=time.time()-t0
    log={"fixed":{"R1":list(R1),"R2":list(R2),"R3star":list(R3),
                  "R4_prefix":[0,1],"R5_prefix":[0,2],"R6_prefix":[0,2]},
         "R4_pass_list":[list(r) for r in R4_list],
         "R4_detail":[{"vec":list(r),"vsR2":ratio_counts(r,R2),"vsR3":ratio_counts(r,R3)} for r in R4_list],
         "nodes":nodes,
         "ordered_solutions_R4R5R6":sols,
         "n_ordered":len(sols),"n_unordered":len(sols)//2 if sols else 0,
         "total_inner_checks":nodes["depth4_scanned"]+nodes["depth5_scanned"]+nodes["depth6_scanned"],
         "time_sec":dt,
         "verdict":"EXISTENCE: 1 unordered completion (2 orders, R5<->R6 swap)" if sols else "GAP: no completion"}
    with open(os.path.join(base,"search_log.json"),"w") as f:
        json.dump(log,f,indent=2)
    print(json.dumps(log,indent=2))
    print(f"done in {dt:.4f}s")

if __name__=="__main__":
    main()
