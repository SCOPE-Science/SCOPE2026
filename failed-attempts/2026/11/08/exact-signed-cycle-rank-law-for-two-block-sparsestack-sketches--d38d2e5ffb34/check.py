#!/usr/bin/env python3
"""Check a two-block signed sparse sketch: exact graph rank, enumeration, and sampling.
The mathematical asymptotic limit is proved separately in RESULT.md.
Only standard-library Python is required.
"""
import itertools, math, random


def matrix_rank_integer(columns, q):
    # Integer row operations over Q using Fraction, for tiny exhaustive checks.
    from fractions import Fraction
    k = len(columns)
    mat = [[Fraction(0) for _ in range(k)] for _ in range(2*q)]
    for j, (a,b,sign) in enumerate(columns):
        mat[a][j] = Fraction(1)
        mat[q+b][j] = Fraction(sign)
    rank = 0
    for j in range(k):
        p = next((i for i in range(rank,2*q) if mat[i][j] != 0), None)
        if p is None: continue
        mat[rank],mat[p] = mat[p],mat[rank]
        v = mat[rank][j]
        for col in range(j,k): mat[rank][col] /= v
        for i in range(rank+1,2*q):
            if mat[i][j]:
                r=mat[i][j]
                for col in range(j,k): mat[i][col] -= r*mat[rank][col]
        rank += 1
        if rank == 2*q: break
    return rank


def graph_independent(columns,q):
    # Each column is a signed edge between a left and a right vertex.
    # Full column rank iff all signed-graph connected components are trees
    # or unbalanced unicyclic components.
    parent=list(range(2*q)); parity=[1]*(2*q); size=[1]*(2*q)
    cycles=[0]*(2*q); consistent=[True]*(2*q)
    def find(x):
        if parent[x] == x: return x,1
        root,z=find(parent[x]); parity[x]*=z;parent[x]=root
        return root,parity[x]
    for a,b,sign in columns:
        b += q
        # Equation: y_b = -sign*y_a for a null vector of the transpose.
        relation=-sign
        ra,pa=find(a); rb,pb=find(b)
        if ra==rb:
            cycles[ra] += 1
            if pa*pb!=relation: consistent[ra]=False
        else:
            if size[ra]<size[rb]:
                ra,rb=rb,ra; pa,pb=pb,pa
            parent[rb]=ra;parity[rb]=relation*pa*pb
            size[ra]+=size[rb];cycles[ra]+=cycles[rb]
            consistent[ra] &= consistent[rb]
    return all(cycles[i]==0 or (cycles[i]==1 and not consistent[i])
               for i in range(2*q) if parent[i]==i)


def exact_probability(q,k):
    # After independent column sign rescaling, top entries are +1,
    # and bottom signs are fair; no rank is changed by rescaling.
    total=0; good=0
    for columns in itertools.product(
            list(itertools.product(range(q),range(q),(-1,1))),repeat=k):
        rankfull=matrix_rank_integer(columns,q)==k
        graphfull=graph_independent(columns,q)
        if graphfull != rankfull: raise AssertionError((q,k,columns,rankfull,graphfull))
        good+=graphfull;total+=1
    return good,total


def estimate(q,c,trial,seed):
    rg=random.Random(seed)
    k=math.floor(c*q)
    good=0
    for _ in range(trial):
        cols=[(rg.randrange(q),rg.randrange(q),rg.choice((-1,1))) for j in range(k)]
        good += graph_independent(cols,q)
    p=good/trial
    limit=(1-c*c)**.25 if c<1 else 0
    se=math.sqrt(max(0.0000001,limit*(1-limit))/trial)
    return p,limit,se


def main():
    exact=[]
    for q,k in ((1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,2),(3,3)):
        good,total=exact_probability(q,k)
        exact.append((q,k,good,total))
    assert exact[4]==(2,2,56,64), exact[4]  # two columns: 1/(2q^2) rank-loss
    print('EXHAUSTIVE_RANK_OK',exact)
    sims=[]
    for q,c,n in ((100,0.4,3500),(100,0.75,3500),(300,0.4,3000),(300,0.75,3000),(300,1.8,1500)):
        p,limit,se=estimate(q,c,n,q*111+int(c*1000))
        print('SAMPLE q',q,'c',c,'runs',n,'observed',round(p,5),
              'limit',round(limit,5),'sd',round(se,5))
        # broad tolerance: catches gross errors while allowing finite size bias.
        assert abs(p-limit)<max(0.085,7*se+0.015),(q,c,p,limit)
        sims.append((q,c,p,limit))
    print('VERIFY_OK exact cases',len(exact),'simulated settings',len(sims))

if __name__=='__main__': main()
