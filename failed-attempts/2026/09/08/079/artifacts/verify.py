"""Independent verifier (stdlib only): replays certificates.json + grid_phis.json in exact integer arithmetic.
Checks: (1) token counts/marginals; (2) primal perm cost == claimed; (3) assignment-dual feasibility+strong duality;
(4) grid phi 1-Lipschitz + value == W1; (5) P05S strict splitting: only doubled demand node is q, nonsplit cost > opt;
(6) midpoint relations."""
import json
from collections import Counter
def manh(a,b): return abs(a[0]-b[0])+abs(a[1]-b[1])
cert=json.load(open("output/artifacts/certificates.json"))
phis=json.load(open("output/artifacts/grid_phis.json"))
N={4:[(x,y) for x in range(4) for y in range(4)],5:[(x,y) for x in range(5) for y in range(5)]}
def adj(NN):
    S=set(NN); e=[]
    for (x,y) in NN:
        for (dx,dy) in ((1,0),(0,1)):
            if (x+dx,y+dy) in S: e.append((NN.index((x,y)),NN.index((x+dx,y+dy))))
    return e
A={4:adj(N[4]),5:adj(N[5])}
assert len(cert["pairs"])==16
for p in cert["pairs"]:
    S=[tuple(q) for q in p["S"]]; T=[tuple(q) for q in p["T"]]
    assert len(S)==len(T)==8
    g=p["grid"]; NN=N[g]
    assert all(q in NN for q in S+T)
    C1=[[manh(a,b) for b in T] for a in S]; C2=[[manh(a,b)**2 for b in T] for a in S]
    for tag,C,opt,pk,uk,vk in (("W1",C1,p["W1_num8"],"W1_perm","W1_u","W1_v"),("W2sq",C2,p["W2sq_num8"],"W2_perm","W2_u","W2_v")):
        perm=p[pk]; u=p[uk]; v=p[vk]
        assert sorted(perm)==list(range(8)),(p["id"],tag)
        assert sum(C[i][perm[i]] for i in range(8))==opt,(p["id"],tag)
        for i in range(8):
            for j in range(8): assert u[i]+v[j]<=C[i][j],(p["id"],tag,i,j)
        assert sum(u)+sum(v)==opt,(p["id"],tag)
    assert p["W1"]=="%d/8"%p["W1_num8"] and p["W2sq"]=="%d/8"%p["W2sq_num8"]
    phi=phis[p["id"]]
    mu=[0]*len(NN); nu=[0]*len(NN)
    for q in S: mu[NN.index(q)]+=1
    for q in T: nu[NN.index(q)]+=1
    for a,b in A[g]: assert abs(phi[a]-phi[b])<=1,(p["id"],a,b)
    assert sum(phi[i]*(mu[i]-nu[i]) for i in range(len(NN)))==p["W1_num8"],p["id"]
    print("PASS",p["id"],"W1=%s"%p["W1"],"W2sq=%s"%p["W2sq"])
# splitting
s=next(p for p in cert["pairs"] if p["id"]=="P05S")
S=[tuple(q) for q in s["S"]]; T=[tuple(q) for q in s["T"]]
cT=Counter(T)
dbl=[q for q,c in cT.items() if c==2]; assert dbl==[(3,3)],dbl
C1=[[manh(a,b) for b in T] for a in S]; C2=[[manh(a,b)**2 for b in T] for a in S]
import itertools
def brute(C):
    best=None
    for perm in itertools.permutations(range(len(C))):
        x=sum(C[i][perm[i]] for i in range(len(C)))
        if best is None or x<best: best=x
    return best
r1=brute([[C1[i][j] for j in range(6)] for i in range(6)])
r2=brute([[C2[i][j] for j in range(6)] for i in range(6)])
ns1=C1[6][6]+C1[7][7]+r1; ns2=C2[6][6]+C2[7][7]+r2
assert ns1==10 and s["W1_num8"]==6 and ns1>s["W1_num8"]
assert ns2==36 and s["W2sq_num8"]==16 and ns2>s["W2sq_num8"]
print("PASS P05S splitting: nonsplit W1 10/8>6/8, W2sq 36/8>16/8; only doubled demand node (3,3)")
# midpoint
m={p["id"]:p for p in cert["pairs"]}
assert m["M1"]["W1_num8"]==m["M2"]["W1_num8"]+m["M3"]["W1_num8"]==16
assert m["M1"]["W2sq_num8"]==32 and m["M2"]["W2sq_num8"]==8 and m["M3"]["W2sq_num8"]==8
print("PASS midpoint: W1 16/8=8/8+8/8; legs W2sq 8/8 each, full 32/8")
print("ALL VERIFIED: 16 pairs, dual certificates, grid potentials, splitting, midpoint")
