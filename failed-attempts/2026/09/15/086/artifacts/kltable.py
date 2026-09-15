import sys
sys.path.insert(0,'output/artifacts')
from klproof2 import C, INTERVAL, LEN, KEYS, kseen, descR, multR, N
# corrected P: coeff cx(v) of T_x in C'_w with C'_w = v^{-lw} sum P_{x,w}(v^2) T_x
def Ppoly(x,w):
    cx=C[w].get(x,{})
    sh={k+LEN[w]:v for k,v in cx.items()}
    assert all(k>=0 and k%2==0 for k in sh), (x,w,cx,sh)
    return {k//2:v for k,v in sh.items()}
def Pv1(x,w): return sum(Ppoly(x,w).values())
bad=0
for w in sorted(INTERVAL.keys(), key=lambda i: LEN[i]):
    for x in INTERVAL[w]:
        p=Ppoly(x,w)
        import math
        if any(2*d>LEN[w]-LEN[x]-1+(1 if x==w else 0) for d in p if x!=w):
            # deg bound: for x<w, deg <= (lw-lx-1)/2
            print("DEGBAD",kseen[KEYS[x]],kseen[KEYS[w]],p); bad+=1
print("degcheck bad=",bad)
# print full table for len<=3
for w in sorted(INTERVAL.keys(), key=lambda i:(LEN[i],kseen[KEYS[i]])):
    if LEN[w]>3: continue
    print(f"w={kseen[KEYS[w]]} (len {LEN[w]}):")
    for x in sorted(INTERVAL[w],key=lambda i:(LEN[i],kseen[KEYS[i]])):
        print(f"   x={kseen[KEYS[x]]}: P={Ppoly(x,w)} P(1)={Pv1(x,w)}")
