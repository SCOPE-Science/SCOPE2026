#!/usr/bin/env python3
"""Generate an exhaustive finite obstruction certificate for path-grid ladders.
For n=2,3,4, all subsets; for n=5,6,8 all three-element subsets.
Use verify_certificate.py to check it without trusting this generator.
"""
import json
from itertools import combinations
from verify_bfs import graph

def first_collision(E,D,S):
    seen={}
    for k,e in enumerate(E):
        h=tuple(sorted(min(D[v][e[0]],D[v][e[1]]) for v in S))
        if h in seen: return [seen[h],k]
        seen[h]=k
    return None

def main():
    out={"schema_version":1,"vertex_rule":"(column,rail) -> 2*column+rail","edge_rule":"rungs in column order, followed by rail edges in column order with top then bottom","cases":[]}
    for n in [2,3,4,5,6,8]:
        E,D=graph(n)
        sizes=list(range(2*n+1)) if n<=4 else [3]
        for k in sizes:
            rec=[]
            for S in combinations(range(2*n),k):
                pair=first_collision(E,D,S)
                assert pair is not None,(n,k,S)
                rec.append(pair)
            out['cases'].append({'n':n,'k':k,'pairs':rec})
    open('/mnt/data/r05work/finite_obstructions.json','w').write(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
    print('OBSTRUCTION_CERTIFICATE',[(x['n'],x['k'],len(x['pairs'])) for x in out['cases']])
if __name__=='__main__':main()
