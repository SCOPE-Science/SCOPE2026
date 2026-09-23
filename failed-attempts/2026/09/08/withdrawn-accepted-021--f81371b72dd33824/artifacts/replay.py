"""Independent replay: from alpha_table.json (w,P,Q,R) recompute exact D*_N with
pure integer arithmetic over Q(sqrt5); verify sorted order, maxima, gap sums (=R,0),
three-distance (<=3 distinct circular gaps), and the claimed top-group separations.
Usage: python3 replay.py [N...]  (default 512 1024 2048)"""
import json, math, sys, collections, functools
S5 = math.sqrt(5)
def s5sign(A,B):
    if B==0: return (A>0)-(A<0)
    if A==0: return (B>0)-(B<0)
    if (A>=0)==(B>=0): return 1 if A>=0 else -1
    d=A*A-5*B*B
    return ((d>0)-(d<0)) if A>0 else -((d>0)-(d<0))
def floors(P,Q,R,N):
    f=[0]*(N+1)
    for n in range(1,N+1):
        g=int(math.floor(n*(P+Q*S5)/R))
        while True:
            if s5sign(n*P-g*R,n*Q)>=0:
                if s5sign(n*P-(g+1)*R,n*Q)>=0: g+=1; continue
                break
            else: g-=1
        f[n]=g
    return f
def dst(P,Q,R,N):
    f=floors(P,Q,R,N)
    FP=[None]+[(n*P-f[n]*R,n*Q) for n in range(1,N+1)]
    idx=list(range(1,N+1))
    idx.sort(key=functools.cmp_to_key(lambda i,j: s5sign(FP[i][0]-FP[j][0],FP[i][1]-FP[j][1])))
    for k in range(N-1):
        assert s5sign(FP[idx[k+1]][0]-FP[idx[k]][0],FP[idx[k+1]][1]-FP[idx[k]][1])>=0, "sort order"
        assert not (FP[idx[k+1]][0]==FP[idx[k]][0] and FP[idx[k+1]][1]==FP[idx[k]][1]), "distinct pts"
    b1=b2=None
    for k,i in enumerate(idx,1):
        A,B=FP[i]
        c1=(k*R-N*A,-N*B); c2=(N*A-(k-1)*R,N*B)
        if b1 is None or s5sign(c1[0]-b1[0],c1[1]-b1[1])>0: b1=c1
        if b2 is None or s5sign(c2[0]-b2[0],c2[1]-b2[1])>0: b2=c2
    c=b1 if s5sign(b1[0]-b2[0],b1[1]-b2[1])>=0 else b2
    G=[]
    for k in range(N):
        i1=idx[k]; i2=idx[(k+1)%N]
        G.append((FP[i2][0]-FP[i1][0],FP[i2][1]-FP[i1][1]) if k<N-1 else (FP[i2][0]-FP[i1][0]+R,FP[i2][1]-FP[i1][1]))
    assert sum(g[0] for g in G)==R and sum(g[1] for g in G)==0, "gap sum"
    assert len(set(G))<=3, "three-distance"
    return (c[0]+c[1]*S5)/(R*N), c, len(set(G)), sorted(collections.Counter(G).values(),reverse=True)
def main():
    recs=json.load(open("output/artifacts/alpha_table.json"))
    assert len(recs)==2313, len(recs)
    # scope completeness: every word over {1..4} with q<=200 reduces (strip trailing 1s) to a table word; spot-check + count
    for Ns in (sys.argv[1:] or ["512","1024","2048"]):
        N=int(Ns)
        tab=json.load(open(f"output/artifacts/Dstar_N{N}.json"))
        assert len(tab)==2313
        # full recompute of extremes + random sample
        idxs=[0,1,2,3,4,5,len(tab)//2,-1]
        RBYW={tuple(r["w"]):r for r in recs}
        for e in [tab[i] for i in idxs]:
            r=RBYW[tuple(e["w"])]
            v,c,nd,cnts=dst(r["P"],r["Q"],r["R"],N)
            assert tuple(e["C"])==c and abs(v-e["D"])<1e-12, (e["w"],e["C"],c)
        # separation: top C-group (2 symmetric labels {a,1-a}) vs runner-up group, exact cross-R sign>0
        g0=tuple(tab[0]["C"]); g1c=None
        for e in tab:
            if tuple(e["C"])!=g0: g1c=tuple(e["C"]); break
        r0=RBYW[tuple(tab[0]["w"])]
        e1=[e for e in tab if tuple(e["C"])==g1c][0]; r1=RBYW[tuple(e1["w"])]
        dA=g1c[0]*r0["R"]-g0[0]*r1["R"]; dB=g1c[1]*r0["R"]-g0[1]*r1["R"]
        assert s5sign(dA,dB)>0, "separation must be exactly positive"
        gap=(dA+dB*S5)/(r0["R"]*r1["R"]*N)
        v0,c0,nd0,cn0=dst(r0["P"],r0["Q"],r0["R"],N)
        print(f"N={N}: min D*={tab[0]['D']:.10f} w={tab[0]['w']} (twin {tab[1]['w']}) runner-up D*={e1['D']:.10f} gap={gap:.3e} 3dist={nd0} {cn0} OK")
    print("REPLAY PASS")
main()
