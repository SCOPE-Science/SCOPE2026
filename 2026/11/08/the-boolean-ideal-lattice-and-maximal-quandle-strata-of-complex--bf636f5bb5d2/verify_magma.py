#!/usr/bin/env python3
"""Independent finite-field multiplication checks for core-quandle idempotent multiplication.

Uses only finite field arithmetic and the literal bilinear structure constants;
phase model is compared with the full multiplication table, not assumed by it.
"""
import itertools
from math import prod, gcd, lcm
from random import Random


def members(mods):return list(itertools.product(*(range(m) for m in mods)))
def action(a,k,mods):return tuple((k*x)%m for x,m in zip(a,mods))
def order(a,mods):return lcm(*(m//gcd(m,x) for x,m in zip(a,mods)))
def orbit_info(mods):
    avail=set(members(mods)); out=[]
    while avail:
        a=min(avail); O={a};queue=[a]
        while queue:
            t=queue.pop()
            for v in [action(t,-1,mods),action(t,2,mods)]:
                if v not in O: O.add(v);queue.append(v)
        avail-=O
        if a!=tuple(0 for _ in mods):
            m=order(a,mods);d=1
            while pow(2,d,m)!=1:d+=1
            antipodal=(d%2==0 and pow(2,d//2,m)==m-1)
            M=2**(d//2)+1 if antipodal else 2**d-1
            out.append((a,O,d,M))
    return out

def primitive(q,m):
    if m==1:return 1
    assert (q-1)%m==0
    for g in range(2,q):
        x=pow(g,(q-1)//m,q)
        if len({pow(x,k,q) for k in range(m)})==m:return x
    raise AssertionError((q,m))

def fourier_inverse(c,mods,q):
    n=prod(mods); assert (q-1)%lcm(*mods)==0
    roots={m:primitive(q,m) for m in mods}
    result={}
    for g in members(mods):
        s=0
        for a,val in c.items():
            phase=prod(pow(roots[m],(a_i*g_i)%m,q) for a_i,g_i,m in zip(a,g,mods))%q
            s+=(val*pow(phase,-1,q))%q
        result[g]=(s*pow(n,-1,q))%q
    return result

def coord_points(mods,q):
    zero=tuple(0 for _ in mods); O=orbit_info(mods);points=[]
    factor_roots=[primitive(q,M) for _,_,_,M in O]
    for aug in [0,1]:
        for settings in itertools.product(*[range(-1,M) for _,_,_,M in O]):
            coords={zero:aug}
            for (a,orbit,d,M),k,z in zip(O,settings,factor_roots):
                if k==-1:
                    coords.update({b:0 for b in orbit});continue
                for j in range(d):
                    p=pow(z,(k*pow(2,j,M))%M,q)
                    ap=action(a,2**j,mods);an=action(ap,-1,mods)
                    if ap in coords:assert coords[ap]==p
                    coords[ap]=p
                    if an in coords:assert coords[an]==pow(p,-1,q)
                    coords[an]=pow(p,-1,q)
            assert len(coords)==prod(mods)
            points.append((aug,settings,coords,fourier_inverse(coords,mods,q)))
    return O,points

def direct_product(u,v,mods,q):
    n=prod(mods);G=members(mods); w={g:0 for g in G}
    for x in G:
        for y in G:
            z=tuple((2*yy-xx)%m for xx,yy,m in zip(x,y,mods))
            w[z]=(w[z]+u[x]*v[y])%q
    return w

def predicted(a,b,M):
    return -1 if min(a,b)<0 else None  # phase tuple depends on multiplicative powers, calculated below

def run():
    tests=[((1,),5),((3,),7),((5,),31),((9,),19),((11,),67),((13,),131),((3,3),7)]
    rng=Random(261108)
    total=0
    for mods,q in tests:
        O,points=coord_points(mods,q); m=(len(points)//2)
        index={(aug,settings):i for i,(aug,settings,_,_) in enumerate(points)}
        # Direct source multiplication of every constructed vector is idempotent.
        for aug,settings,c,u in points:
            assert direct_product(u,u,mods,q)==u
            total+=1
        pairs=itertools.product(range(len(points)),repeat=2) if len(points)<=132 else [(rng.randrange(len(points)),rng.randrange(len(points))) for _ in range(500)]
        paircount=0
        for i,j in pairs:
            aug1,settings1,_,u=points[i];aug2,settings2,_,v=points[j]
            tgt=(aug1*aug2,tuple(-1 if min(x,y)<0 else (2*y-x)%P[3] for x,y,P in zip(settings1,settings2,O)))
            assert tgt in index
            w=direct_product(u,v,mods,q)
            assert w==points[index[tgt]][3],(mods,i,j,tgt)
            paircount+=1
        total+=paircount
        # Every support stratum is stable, its nonzero factor orders are odd,
        # and the total number of maximal strata is 2^(1 + number of nontrivial orbits).
        strata={(aug,tuple(x>=0 for x in settings)) for aug,settings,_,_ in points}
        assert len(strata)==2**(len(O)+1)
        assert all(P[3]%2==1 for P in O)
        print('CHECK',mods,'field',q,'idempotents',len(points),'direct_products',paircount,'maximal_quandle_strata',len(strata))
    # Exhaustively classify all nonempty two-sided ideals of the idempotent magma
    # for orders 1, 3, and 5: compare to downsets of the support Boolean lattice.
    for mods,q in [((1,),5),((3,),7),((5,),31)]:
        orbit_data, pts=coord_points(mods,q)
        N=len(pts)
        idx={(u[0],u[1]):i for i,u in enumerate(pts)}
        tbl=[]
        for ai,at,_,_ in pts:
            row=[]
            for bi,bt,_,_ in pts:
                target=(ai*bi,tuple(-1 if min(x,y)<0 else (2*y-x)%P[3]
                                   for x,y,P in zip(at,bt,orbit_data)))
                row.append(idx[target])
            tbl.append(row)
        ideals=[]
        for mask in range(1,1<<N):
            I={i for i in range(N) if mask>>i&1}
            if all(tbl[a][b] in I and tbl[b][a] in I for a in I for b in range(N)):
                ideals.append(I)
                # A support-stratum is either wholly in or wholly out.
                supports={j: (u[0],tuple(x>=0 for x in u[1])) for j,u in enumerate(pts)}
                assert all((i in I)==(j in I) for i in range(N) for j in range(N) if supports[i]==supports[j])
        assert len(ideals)==({1:2,3:5,5:5}[prod(mods)]),(mods,len(ideals))
        print('IDEALS',mods,'exact_nonempty',len(ideals))
    print('VERIFY_OK group_types=7 direct_checks='+str(total)+' maximal_strata=all_pass ideal_lattices=3')
if __name__=='__main__': run()
