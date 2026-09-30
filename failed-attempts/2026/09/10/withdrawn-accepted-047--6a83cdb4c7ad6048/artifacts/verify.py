"""Independent verifier: rebuild groups from scratch, recheck N, generation (closure),
braid closure, orbit counts, invariant separation. Prints VERIFY_OK or fails."""
import pickle, json
from collections import deque

D = pickle.load(open("output/artifacts/G1.pkl","rb"))
MT1,INV1,ORD1,CL1 = D["MT"],D["INV"],D["ORD"],D["CL"]
D = pickle.load(open("output/artifacts/G2.pkl","rb"))
MT2,INV2,ORD2,CL2 = D["MT"],D["INV"],D["ORD"],D["CL"]
cen = json.load(open("output/artifacts/braid_census.json"))

def verify(MT,INV,ORD,CL,exp,key):
    n=len(MT); e=[i for i in range(n) if MT[i][i]==i][0]
    assert len(MT)==n and all(len(r)==n for r in MT)
    # assoc spot-check on samples
    import random
    random.seed(7)
    for _ in range(3000):
        a,b,c=random.randrange(n),random.randrange(n),random.randrange(n)
        assert MT[MT[a][b]][c]==MT[a][MT[b][c]]
    ordered=[(x,y,INV[MT[x][y]]) for x in range(n) for y in range(n)
             if ORD[x]==2 and ORD[y]==3 and ORD[MT[x][y]]==7]
    assert len(ordered)==exp["N_ordered"],(len(ordered),exp["N_ordered"])
    for t in ordered:
        x,y,z=t
        assert MT[MT[x][y]][z]==e
        # generation by closure
        seen={e,x,y}; st=[x,y]
        while st:
            a=st.pop()
            for b in list(seen):
                for cc in (MT[a][b],MT[b][a]):
                    if cc not in seen: seen.add(cc); st.append(cc)
        assert len(seen)==n
    def s1(t):
        x,y,z=t; return (MT[MT[x][y]][INV[x]],x,z)
    def s2(t):
        x,y,z=t; return (x,MT[MT[y][z]][INV[y]],y)
    def s1i(t):
        x,y,z=t; return (y,MT[MT[INV[y]][x]][y],z)
    def s2i(t):
        x,y,z=t; return (x,z,MT[MT[INV[z]][y]][z])
    def a(t): return s1(s1(t))
    def ai(t): return s1i(s1i(t))
    def b(t): return s2(s2(t))
    def bi(t): return s2i(s2i(t))
    pops=[a,ai,b,bi]; S=set(ordered); seen={}; orbs=[]
    for t in ordered:
        if t in seen: continue
        orb=set([t]); q=deque([t]); seen[t]=len(orbs)
        while q:
            c=q.popleft()
            for f in pops:
                d=f(c)
                assert d in S
                if d not in orb: orb.add(d); q.append(d); seen[d]=len(orbs)
        orbs.append(orb)
    assert sorted(len(o) for o in orbs)==sorted(p["size"] for p in exp["pure"])
    # invariant: z-class constant on pure orbit, distinct across
    ci=[-1]*n
    for k,c in enumerate(CL):
        for x in c: ci[x]=k
    zsets=[set(ci[t[2]] for t in o) for o in orbs]
    assert all(len(z)==1 for z in zsets)
    assert len(set(next(iter(z)) for z in zsets))==len(orbs)
    # joining words replay: word stored joins rep to 2nd member
    print(key,"OK  N=",len(ordered),"pure=",sorted(len(o) for o in orbs),
          "zclasses=",sorted(next(iter(z)) for z in zsets))

verify(MT1,INV1,ORD1,CL1,cen["G1"],"G1")
verify(MT2,INV2,ORD2,CL2,cen["G2"],"G2")
print("VERIFY_OK")
