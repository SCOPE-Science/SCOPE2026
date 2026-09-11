"""Focused builder: constants + linear pencil sharing structure.
Families: (a) many constants: constants never collide -> each coord's top-2
covers exactly 2 constants; other polys must hit {c1,c2} values.
(b) arithmetic line family f_a = a*h with h fixed (vanishes at Z, |Z|=11):
at z in Z all 9 share value 0 (agree 9>=... contributes), else values a*h(x)
distinct -> only 2 covered. Try to maximize overlap via h with many collisions.
(c) low-degree perturbations of 2 constants: f = c_i + small*h_a.
Direct random sampling + local search over h choice.
"""
import random, math, time, sys
Q=97; N=48; K=12; T=9; NEED=32
EVAL=list(range(N))
POW=[[1]*K for _ in range(N)]
for x in range(N):
    for j in range(1,K):
        POW[x][j]=(POW[x][j-1]*x)%Q

def eval_row(c):
    return [sum(c[j]*POW[x][j] for j in range(K))%Q for x in EVAL]

def stats(mat):
    row=[0]*T
    for j in range(N):
        cnt={}
        for i in range(T):
            v=mat[i][j]; cnt[v]=cnt.get(v,0)+1
        s=sorted(cnt.items(),key=lambda kv:-kv[1])
        S=set([s[0][0]]) if len(s)==1 else set([s[0][0],s[1][0]])
        for i in range(T):
            if mat[i][j] in S: row[i]+=1
    return min(row),sum(row),row

def rand_poly_deg(rng,d):
    c=[0]*K
    for j in range(d+1): c[j]=rng.randrange(Q)
    return c

def trial_const_pencil(rng):
    # 2 constants + 7 polys of form c_i + h where h vanishes at random Z (11 pts)
    c1=rng.randrange(Q); c2=rng.randrange(Q)
    while c2==c1: c2=rng.randrange(Q)
    Z=rng.sample(range(N),11)
    h=[1]
    for p in Z:
        nh=[0]*(len(h)+1)
        for i,c in enumerate(h):
            nh[i]=(nh[i]-p*c)%Q; nh[i+1]=(nh[i+1]+c)%Q
        h=nh
    while len(h)<K: h.append(0)
    h=h[:K]
    polys=[[c1]+[0]*(K-1),[c2]+[0]*(K-1)]
    for _ in range(7):
        base=c1 if rng.random()<0.5 else c2
        a=rng.randrange(1,Q)
        polys.append([ (base if j==0 else 0) + a*h[j] for j in range(K)])
        for j in range(K): polys[-1][j]%=Q
    return polys

def trial_lowdeg(rng):
    # 9 random polys of degree <=2 (heavy collisions since range small? no, still 97 values)
    return [rand_poly_deg(rng,2) for _ in range(T)]

def trial_two_clusters(rng):
    # 4 near-const polys around c1 (c1 + small multiples of h1), 5 around c2
    polys=[]
    for (c,n) in [(rng.randrange(Q),4),(rng.randrange(Q),5)]:
        Z=rng.sample(range(N),11)
        h=[1]
        for p in Z:
            nh=[0]*(len(h)+1)
            for i,cc in enumerate(h):
                nh[i]=(nh[i]-p*cc)%Q; nh[i+1]=(nh[i+1]+cc)%Q
            h=nh
        while len(h)<K: h.append(0)
        h=h[:K]
        for _ in range(n):
            a=rng.randrange(1,Q)
            polys.append([((c if j==0 else 0)+a*h[j])%Q for j in range(K)])
    return polys

if __name__=="__main__":
    budget=float(sys.argv[1]) if len(sys.argv)>1 else 120.0
    t0=time.time(); best=(0,0); n=0; s=0
    while time.time()-t0<budget:
        rng=random.Random(5000+s)
        kind=s%4
        if kind in (0,1): p=trial_const_pencil(rng)
        elif kind==2: p=trial_lowdeg(rng)
        else: p=trial_two_clusters(rng)
        mat=[eval_row(c) for c in p]
        m,t,_=stats(mat)
        n+=1
        if (m,t)>best:
            best=(m,t)
            print(f"[{time.time()-t0:.0f}s] trial {n} kind {kind}: min={m} total={t}",flush=True)
            if m>=NEED:
                import json; json.dump({"coeffs":p},open("output/artifacts/counterexample.json","w"))
                print("FOUND"); break
        s+=1
    print("done",n,best)
