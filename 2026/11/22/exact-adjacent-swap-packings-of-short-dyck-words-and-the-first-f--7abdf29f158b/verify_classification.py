"""Independent exhaustive enumeration of all maximal ten-bit Dyck one-swap codes.
Run: python verify_classification.py
Requires Python standard library only.
"""
from pathlib import Path
import json

def dyck_words(k):
    out=[]
    def rec(pre,opened,closed):
        if closed==k:
            out.append(pre);return
        if opened<k:rec(pre+'0',opened+1,closed)
        if closed<opened:rec(pre+'1',opened,closed+1)
    rec('',0,0)
    return out

def swap_ball(w):
    ans={w}
    for j in range(len(w)-1):
        if w[j]!=w[j+1]:ans.add(w[:j]+w[j+1]+w[j]+w[j+2:])
    return ans

W=dyck_words(5)
assert len(W)==42
BALLS=[swap_ball(w) for w in W]
N=len(W)
# Distinct error channels cannot be substituted for one another:
# exact-one-deletion balls have a different conflict graph.
def deletion_ball(w):
    return {w[:j]+w[j+1:] for j in range(len(w))}
DEL=[deletion_ball(w) for w in W]
sw_edges={ (i,j) for i in range(N) for j in range(i+1,N) if BALLS[i]&BALLS[j] }
del_edges={ (i,j) for i in range(N) for j in range(i+1,N) if DEL[i]&DEL[j] }
assert (len(sw_edges),len(del_edges),len(sw_edges-del_edges),len(del_edges-sw_edges)) == (252,263,77,88)
# Compatibility graph: an edge means disjoint one-swap output balls.
ADJ=[sum(1<<j for j in range(N) if i!=j and BALLS[i].isdisjoint(BALLS[j]))
     for i in range(N)]
MAXIMAL=[]

def maximal_cliques(chosen,pool,excluded):
    if not pool and not excluded:
        MAXIMAL.append(tuple(sorted(chosen)))
        return
    union=pool|excluded
    if union:
        pivot=max((i for i in range(N) if union>>i&1),key=lambda i:(ADJ[i]&pool).bit_count())
        candidates=pool&~ADJ[pivot]
    else:candidates=pool
    while candidates:
        vbit=candidates&-candidates;v=vbit.bit_length()-1
        maximal_cliques(chosen+(v,),pool&ADJ[v],excluded&ADJ[v])
        pool ^=vbit;excluded|=vbit;candidates^=vbit

maximal_cliques((),(1<<N)-1,0)
size=max(map(len,MAXIMAL))
optima={tuple(W[j] for j in ids) for ids in MAXIMAL if len(ids)==size}
DATA=json.loads(Path(__file__).with_name('certificates.json').read_text(encoding='utf-8'))
listed={tuple(c) for c in DATA['length_ten_maximum_codebooks']}
assert size==9 and len(optima)==len(listed)==11 and optima==listed

def reflect(w):return ''.join('1' if c=='0' else '0' for c in reversed(w))
def rc(code):return tuple(sorted(reflect(w) for w in code))
assert all(rc(code) in optima for code in optima)
fixed=sum(rc(code)==code for code in optima)
assert fixed==9
print('Dyck words:',N,'Maximal compatibility cliques:',len(MAXIMAL))
print('Largest correctable code size:',size,'Number of maximum codebooks:',len(optima))
print('Reflection-complementation fixed maximum codebooks:',fixed)
print('Incomparable channel confusabilities: swap-only',len(sw_edges-del_edges),'deletion-only',len(del_edges-sw_edges))
