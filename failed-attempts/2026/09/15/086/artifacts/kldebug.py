import sys
sys.path.insert(0,'output/artifacts')
from klproof2 import C, INTERVAL, LEN, KEYS, kseen, descR, multR, Ppoly_q, P1
# find smallest w with bad poly
for w in sorted(INTERVAL.keys(), key=lambda i: LEN[i]):
    for x in INTERVAL[w]:
        sh={k+LEN[w]-LEN[x]:v for k,v in C[w].get(x,{}).items()}
        if any(k<0 or k%2==1 for k in sh):
            print("BAD w=",kseen[KEYS[w]],"x=",kseen[KEYS[x]],"C=",C[w].get(x),"shifted=",sh)
            raise SystemExit
print("none bad?")
