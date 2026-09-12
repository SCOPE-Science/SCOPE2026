"""Exact completeness proof by exhaustive search with symmetry breaking, in pure Python+C-free but feasible?
Count: rotations at A-side: each 8-cycle cyclic order = 7! = 5040 options up to rotation; x4.
Too big for naive. Instead use lemma-guided exact enumeration:
  The lemma PROVES every quad lies in the 256 normalized family. The 256-check IS the exhaustive proof
  conditional on the lemma. The lemma steps are pure permutation-group deductions (no search), so the
  only computational part is the 256 face-traces (instant, exact, reproducible).
This script re-verifies the 256 count with an independent face-tracer implementation (different code path)
to rule out tracer bugs.
"""
import itertools, sys
sys.path.insert(0, 'output/artifacts')

def faces2(rotA, rotB):
    # independent implementation: integer darts 0..63, dart id = (a*8+b)*2+side
    na=4; nb=8
    nxtA=[None]*4; nxtB=[None]*8
    for a in range(4):
        r=rotA[a]; d={r[i]:r[(i+1)%8] for i in range(8)}; nxtA[a]=d
    for b in range(8):
        r=rotB[b]; d={r[i]:r[(i+1)%4] for i in range(4)}; nxtB[b]=d
    # dart (a,b,atA): located at A-vertex a heading to b? face step: at head vertex take successor
    seen=set(); fl=[]
    for a in range(4):
        for b in range(8):
            for s in (0,1):
                if s==0: u=('A',a); v=('B',b)
                else: u=('B',b); v=('A',a)
                if (u,v) in seen: continue
                cu,cv=u,v; c=[]
                while True:
                    seen.add((cu,cv)); c.append((cu,cv))
                    if cv[0]=='A': w=nxtA[cv[1]][cu[1]]; cu,cv=cv,('B',w)
                    else: w=nxtB[cv[1]][cu[1]]; cu,cv=cv,('A',w)
                    if (cu,cv)==(u,v): break
                    assert len(c)<100
                fl.append(c)
    return fl

sig=[0,1,2,3,4,5,6,7]; siginv=[0,7,6,5,4,3,2,1]
def order_of(img):
    o=[0]
    while img[o[-1]]!=0: o.append(img[o[-1]])
    return o
o_g=order_of([1,2,3,0]); o_ginv=order_of([3,0,1,2])
n=0; sols=[]
for sc in itertools.product([0,1],repeat=4):
    rotA=[sig if c==0 else siginv for c in sc]
    for tc in itertools.product([0,1],repeat=8):
        rotB=[o_g if c==0 else o_ginv for c in tc]
        fl=faces2(rotA,rotB)
        if len(fl)==16 and all(len(f)==4 for f in fl):
            n+=1; sols.append((sc,tc))
print("independent tracer: quad count in 256 family =", n)
assert n==4
print("sols:", sols)
