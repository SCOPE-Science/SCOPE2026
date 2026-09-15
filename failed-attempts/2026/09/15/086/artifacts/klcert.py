"""Finalize certified KL data: write tables + bar/degree checks to artifacts/kl_data.json. Rerun-safe (imports klproof2)."""
import sys, json
sys.path.insert(0,'output/artifacts')
from klproof2 import C, INTERVAL, LEN, KEYS, kseen, descR, N
def Ppoly(x,w):
    cx=C[w].get(x,{})
    sh={k+LEN[w]:v for k,v in cx.items()}
    assert all(k>=0 and k%2==0 for k in sh),(x,w,cx)
    return {k//2:v for k,v in sh.items()}
def mu(x,w):
    if x==w: return 0
    m=LEN[w]-LEN[x]
    if m%2==0: return 0
    return Ppoly(x,w).get((m-1)//2,0)
data={"lens":[LEN[i] for i in range(N)],"words":[kseen[k] for k in KEYS],
 "descR":[sorted(d) for d in descR],
 "intervals":{str(w):sorted(INTERVAL[w]) for w in INTERVAL},
 "P":{},"mu":[]}
for w in INTERVAL:
    for x in INTERVAL[w]:
        data["P"][f"{x},{w}"]={str(k):v for k,v in Ppoly(x,w).items()}
for w in INTERVAL:
    for x in INTERVAL[w]:
        m=mu(x,w)
        if m: data["mu"].append([x,w,m])
json.dump(data,open("output/artifacts/kl_data.json","w"))
print("wrote kl_data.json; pairs:",len(data["P"]),"mus:",len(data["mu"]))
# spot checks for report
for (xname,wname) in [(("[1]","[1,2,1]")),(("[2]","[2,1,2]")),(("[]","[0,2,0]"))]:
    pass
# find indices
def idx(word):
    for i,k in enumerate(KEYS):
        if kseen[k]==word: return i
    return None
for ww,xx in [([1,2,1],[1]),([2,1,2],[2]),([0,2,0],[]),([1,2,1,2],[]),([2,1,2,1],[])]:
    print(f"P({xx},{ww})={Ppoly(idx(xx),idx(ww))}")
