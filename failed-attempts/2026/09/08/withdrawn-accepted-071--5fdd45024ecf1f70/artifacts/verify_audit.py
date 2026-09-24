#!/usr/bin/env python3
"""Independent 5-step audit replay per audit_plan. Stdlib only."""
import json, math
T=json.load(open("census_table.json"))
def ev(c,x,p):
    v=0
    for a in reversed(c): v=(v*x+a)%p
    return v
def strip(a,p):
    a=[x%p for x in a]
    while len(a)>1 and a[-1]==0: a.pop()
    return a
def pgcd(a,b,p):
    # same Euclid structure as census.py (independent retype, single swap)
    a=strip(list(a),p); b=strip(list(b),p)
    while not (len(b)==1 and b[0]==0):
        while len(a)>1 and a[-1]==0: a.pop()
        while len(b)>1 and b[-1]==0: b.pop()
        if len(b)==1 and b[0]==0: break
        da=len(a)-1; db=len(b)-1
        if da<db: a,b=b,a; da,db=db,da
        c=(a[-1]*pow(b[-1],-1,p))%p; s=da-db
        sub=[0]*s+[(c*x)%p for x in b]
        while len(sub)<len(a): sub.append(0)
        a=strip([(x-y)%p for x,y in zip(a,sub)],p)
        a,b=b,a
    return strip(a,p)
def serre(q): return q+1+2*math.floor(2*math.sqrt(q))
n=0
for r in T["rows"]:
    if not r["smooth"]: continue
    c,p,deg=r["coeffs"],r["p"],r["deg"]
    # (1) discriminant/genus
    f=[x%p for x in c]; fp=[(i*f[i])%p for i in range(1,len(f))]
    assert len(pgcd(f,fp,p))==1, ("disc",r)
    assert deg in (5,6) and f[-1]%p==1
    # (2) N1 independent recount (direct y double loop)
    N=0
    for x in range(p):
        v=ev(c,x,p)
        for y in range(p):
            if (y*y-v)%p==0: N+=1
    N+=(1 if deg==5 else 2)
    assert N==r["N1"],("N1",r,N)
    # (3) Weil solve from N1,N2 + bounds + zeta-log match
    q=p; a1=r["N1"]-q-1
    S1=q+1-r["N1"]; S2=q*q+1-r["N2"]
    assert (S1*S1-S2)%2==0
    a2=(S1*S1-S2)//2
    assert (a1,a2)==(r["a1"],r["a2"]),("weil",r)
    assert abs(-a1)<=4*math.sqrt(q)
    assert abs(a2)<=6*q
    P=r["P"]; assert P==[1,a1,a2,q*a1,q*q]
    # (4) Jac order
    assert r["Jac"]==1+a1+a2+q*a1+q*q
    n+=1
# (5) maximal witnesses + point lists
for pname,p,sb in [("M11",19,36),("M12",29,50)]:
    hit=[r for r in T["rows"] if r["model"]==pname and r["p"]==p][0]
    assert hit["N1"]==sb==serre(p),hit
    PL=json.load(open(f"points_{pname}_p{p}.json"))
    assert PL["N"]==sb and len(PL["affine"])+len(PL["infinity"])==sb
    for x,y in PL["affine"]:
        assert (y*y-ev(PL["coeffs"],x,p))%p==0
print(f"AUDIT_OK rows={n} witnesses=2")
