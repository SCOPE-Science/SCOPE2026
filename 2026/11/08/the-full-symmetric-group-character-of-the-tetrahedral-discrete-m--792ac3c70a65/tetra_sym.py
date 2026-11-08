#!/usr/bin/env python3
"""Exact simplicial Lefschetz characters of the tetrahedral Morse matching complex."""
from itertools import permutations
from collections import Counter
import json

V=tuple(range(4))
F=tuple(range(1,16))
face_index={f:i for i,f in enumerate(F)}
E=tuple((a,b) for a in F for b in F if a&b==a and b.bit_count()==a.bit_count()+1)
assert len(E)==28
Eindex={e:i for i,e in enumerate(E)}
endmask=[(1<<face_index[a])|(1<<face_index[b]) for a,b in E]

def acyclic(sel):
    # Orient all Hasse edges upward except matched edges downward.
    adj=[[] for _ in F]
    ss=set(sel)
    for i,(a,b) in enumerate(E):
        ia=face_index[a];ib=face_index[b]
        if i in ss: adj[ib].append(ia)
        else:adj[ia].append(ib)
    state=[0]*len(F)
    def visit(v):
        state[v]=1
        for w in adj[v]:
            if state[w]==1:return False
            if state[w]==0 and not visit(w):return False
        state[v]=2
        return True
    return all(state[v] or visit(v) for v in range(len(F)))

simp=[]
basecounts=Counter()
def rec(pos,used,sel):
    if pos==len(E):
        if sel and acyclic(sel):
            simp.append(tuple(sel));basecounts[len(sel)-1]+=1
        return
    rec(pos+1,used,sel)
    if not used & endmask[pos]:
        sel.append(pos);rec(pos+1,used|endmask[pos],sel);sel.pop()
rec(0,0,[])
assert [basecounts[i] for i in range(7)]==[28,300,1544,3932,4632,2128,256],basecounts
print('F_VECTOR',json.dumps([basecounts[i] for i in range(7)]))
print('SIMP_TOTAL',len(simp))

def pface(f,p):
    return sum((1<<p[j]) for j in V if f>>j&1)
def pedge(e,p):
    return Eindex[(pface(e[0],p),pface(e[1],p))]
def cycletype(p):
    cycles=[];seen=set()
    for i in V:
        if i not in seen:
            j=i;c=0
            while j not in seen:seen.add(j);j=p[j];c+=1
            cycles.append(c)
    return tuple(sorted(cycles,reverse=True))

def parity(seq):
    return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1

def traces_for(p):
    mapping=[pedge(e,p) for e in E]
    signed_counts=Counter();fixed_counts=Counter();swapped=[]
    for W in simp:
        Wmap=tuple(mapping[i] for i in W)
        if set(Wmap)==set(W):
            positions={k:j for j,k in enumerate(W)}
            sign=parity(tuple(positions[k] for k in Wmap))
            signed_counts[len(W)-1]+=sign
            fixed_counts[len(W)-1]+=1
    L=sum(((-1)**dim)*signed_counts[dim] for dim in signed_counts)
    return L-1,L, [signed_counts[i] for i in range(7)],[fixed_counts[i] for i in range(7)]

bytype={};byclass=Counter()
for p in permutations(V):
    t=cycletype(p);tr=traces_for(p);byclass[t]+=1
    if t in bytype:assert bytype[t][:2]==tr[:2],(t,p,bytype[t],tr)
    else:bytype[t]=tr
print('CONJ_CLASSES',dict((str(t),byclass[t]) for t in sorted(byclass)))
for t,tr in sorted(bytype.items(),key=lambda x: (len(x[0]),x[0])):
    print('CLASS',t,'trace',tr[0],'Lefschetz',tr[1], 'signed_fixed_by_dimension',tr[2], 'fixed_by_dimension',tr[3])
order=[(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)]
chars=[bytype[t][0] for t in order]
char_table={'trivial':[1,1,1,1,1],'standard(3,1)':[3,1,-1,0,-1],'partition(2,2)':[2,0,2,-1,0], 'partition(2,1,1)':[3,-1,-1,0,1],'sign':[1,-1,1,1,-1]}
mults={name:sum(byclass[t]*x*y for t,x,y in zip(order,chars,row))//24 for name,row in char_table.items()}
assert all(24*mults[name]==sum(byclass[t]*x*y for t,x,y in zip(order,chars,row)) for name,row in char_table.items())
assert sum(mults[name]*row[0] for name,row in char_table.items())==99
print('CHARACTER',chars)
print('SPECHT_MULTIPLICITIES',mults)
print('ALL_TETRAHEDRON_CHECKS_OK')
