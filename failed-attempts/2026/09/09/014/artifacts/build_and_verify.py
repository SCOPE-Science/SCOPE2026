"""Build + verify full certificate package. Stdlib only. Prints VERIFY_OK on success."""
import json, math, itertools, sys
sys.path.insert(0, "output/artifacts")
from c4tools import is_c4_free, kst_floor, pair_log, er_q
from gf import MUL, INV, ADD

EX = {"1":0,"2":1,"3":3,"4":4,"5":6,"6":7,"7":9,"8":11,"9":13,"10":16,
      "11":18,"12":21,"13":24,"14":27,"15":30,"16":33,"17":36,"18":39}

def er4():
    pts=[]; seen=set()
    for x in itertools.product(range(4), repeat=3):
        if x==(0,0,0): continue
        l=next(c for c in x if c!=0); inv=INV[l]
        key=tuple(MUL[c][inv] for c in x)
        if key not in seen: seen.add(key); pts.append(key)
    E=[]
    for i in range(21):
        for j in range(i+1,21):
            d=0
            for k in range(3): d=ADD[d][MUL[pts[i][k]][pts[j][k]]]
            if d==0: E.append([i,j])
    return 21, E

n3,E3 = er_q(3); E3s=[tuple(sorted(e)) for e in E3]
n4,E4 = er4();  E4s=[tuple(sorted(e)) for e in E4]
assert (n3,len(E3s))==(13,24) and (n4,len(E4s))==(21,50)
assert is_c4_free(13,E3s) and is_c4_free(21,E4s)

ER3_KEEP = {13:[0,1,2,3,4,5,6,7,8,9,10,11,12],12:[0,1,2,3,4,5,6,7,9,10,11,12],
            11:[0,1,2,4,5,6,7,9,10,11,12],10:[0,1,2,4,5,6,7,9,10,11],
            9:[0,1,4,5,6,7,9,10,11],8:[0,1,5,6,7,9,10,11],7:[0,1,5,6,7,10,11],
            6:[0,1,6,7,10,11],4:[0,7,10,11],3:[0,7,10],2:[7,10],1:[10]}
ER4_KEEP = {14:[0,1,2,3,5,7,8,12,13,14,15,17,19,20],
            15:[0,1,3,4,5,7,8,11,12,13,14,15,17,18,20],
            16:[0,1,2,3,4,5,7,8,11,12,13,14,15,17,18,20],
            17:[0,1,2,3,4,5,6,7,8,11,12,13,14,15,17,18,20],
            18:[0,1,2,3,4,5,6,7,8,9,11,12,13,14,15,17,18,20]}
F2 = [(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)]
F2_PHI = {"0":0,"1":1,"2":4,"3":7,"4":10}  # embedding into ER_3 (0-indexed)

def induced(keep, Eset):
    S=set(keep); mp={v:i for i,v in enumerate(sorted(S))}
    return sorted([(mp[u],mp[v]) if mp[u]<mp[v] else (mp[v],mp[u]) for u,v in Eset if u in S and v in S])

W={}; host={}
for k,keep in ER3_KEEP.items():
    W[str(k)]=induced(keep,E3s); host[str(k)]="ER_3"
W["5"]=[list(e) for e in F2]; host["5"]="ER_3"
for k,keep in ER4_KEEP.items():
    W[str(k)]=induced(keep,E4s); host[str(k)]="ER_4"

ok=True
for n in range(1,19):
    k=str(n); E=[tuple(e) for e in W[k]]
    assert len(E)==EX[k], (n,len(E),EX[k])
    assert is_c4_free(n,E), n
    deg,s,cap=pair_log(n,E)
    assert s<=cap, n
S={str(n):EX[str(n)]-1 for n in range(2,19)}  # n=1 has a single graph; no second tier
for n in range(2,19):
    k=str(n); E=[tuple(e) for e in W[k]][:-1] if EX[k]>0 else []
    assert len(E)==S[k] and is_c4_free(n,E), (n, len(E), S[k])
# KST residuals
for n in range(1,19):
    assert kst_floor(n)-EX[str(n)] in (0,1,2), n
# F2 embedding edges
A3=[set() for _ in range(13)]
for u,v in E3s: A3[u].add(v); A3[v].add(u)
for u,v in F2:
    assert int(F2_PHI[str(v)]) in A3[int(F2_PHI[str(u)])]
json.dump({"extremal":W,"host":host,"second_max":S,"F2_phi":F2_PHI}, open("output/artifacts/witnesses.json","w"))
print("VERIFY_OK")
