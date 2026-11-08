"""Exact fourth-order cyclic Fourier minor census at order 16.
Run: python3 f16_exact_check.py. Uses only Python standard library.
"""
from collections import Counter
from itertools import combinations, permutations
N=16
SUBSETS=list(combinations(range(N),4))
UNITS=tuple(x for x in range(N) if x%2)
PERMS={m: tuple((p, (-1 if sum(p[i]>p[j] for i in range(m) for j in range(i+1,m))%2 else 1)) for p in permutations(range(m))) for m in (2,3,4)}

def cyclotomic_minor_nonzero(rows,cols):
    m=len(rows)
    coeff=[0]*8
    for pp,sgn in PERMS[m]:
        e=sum(rows[i]*cols[pp[i]] for i in range(m))%16
        coeff[e%8]+=sgn if e<8 else -sgn
    return any(coeff)

def cyclotomic_rank(rows,cols):
    if cyclotomic_minor_nonzero(rows,cols):return 4
    for I in combinations(range(4),3):
        for J in combinations(range(4),3):
            if cyclotomic_minor_nonzero([rows[i] for i in I],[cols[j] for j in J]):return 3
    for I in combinations(range(4),2):
        for J in combinations(range(4),2):
            if cyclotomic_minor_nonzero([rows[i] for i in I],[cols[j] for j in J]):return 2
    return 1

def rank_mod97(rows,cols,root):
    m=len(rows);mat=[[pow(root,rows[i]*cols[j]%16,97) for j in range(m)] for i in range(m)]
    rk=0
    for j in range(m):
        pivot=next((i for i in range(rk,m) if mat[i][j]),None)
        if pivot is None: continue
        mat[rk],mat[pivot]=mat[pivot],mat[rk]
        inv=pow(mat[rk][j],-1,97)
        for i in range(rk+1,m):
            mul=mat[i][j]*inv%97
            if mul:
                for k in range(j,m):mat[i][k]=(mat[i][k]-mul*mat[rk][k])%97
        rk+=1
    return rk

def primitive_roots():
    roots=[z for z in range(1,97) if pow(z,8,97)==96 and pow(z,16,97)==1]
    assert len(roots)==8 and len(set(roots))==8
    return roots

def modular_rank(rows,cols,roots):
    return max(rank_mod97(rows,cols,z) for z in roots)

def affine_orbits():
    left=set(SUBSETS);orbits=[]
    while left:
        rep=min(left)
        orb={tuple(sorted((u*x+b)%16 for x in rep)) for u in UNITS for b in range(16)}
        assert orb<=left
        left-=orb
        orbits.append((rep,len(orb)))
    assert sum(size for _,size in orbits)==1820
    return orbits

EXPECTED={1:16,2:9728,3:293888,4:3008768}
ORBIT_ROWS={
 (0,1,2,3):(64,0,0,0,1820), (0,1,2,4):(128,0,0,28,1792),
 (0,1,2,5):(128,0,0,20,1800), (0,1,2,6):(128,0,0,28,1792),
 (0,1,2,7):(128,0,0,0,1820), (0,1,2,8):(128,0,0,156,1664),
 (0,1,2,9):(32,0,0,236,1584), (0,1,3,4):(64,0,0,52,1768),
 (0,1,3,5):(128,0,0,28,1792), (0,1,3,7):(128,0,0,28,1792),
 (0,1,3,8):(64,0,0,140,1680), (0,1,3,9):(128,0,0,156,1664),
 (0,1,3,12):(64,0,0,52,1768), (0,1,3,14):(64,0,0,0,1820),
 (0,1,4,5):(64,0,4,192,1624), (0,1,4,8):(128,0,4,408,1408),
 (0,1,4,9):(64,0,4,264,1552), (0,1,7,8):(32,0,0,236,1584),
 (0,1,8,9):(16,0,140,896,784), (0,2,4,6):(32,0,28,672,1120),
 (0,2,4,8):(64,0,28,768,1024), (0,2,4,10):(16,0,28,832,960),
 (0,2,6,8):(16,0,28,832,960), (0,2,8,10):(8,0,156,1088,576),
 (0,4,8,12):(4,4,408,1152,256)}

def run():
    roots=primitive_roots();orbits=affine_orbits()
    assert len(orbits)==25
    glob=Counter()
    for rows,mult in orbits:
        counts=Counter()
        for cols in SUBSETS:
            r=cyclotomic_rank(rows,cols)
            assert r==modular_rank(rows,cols,roots), (rows,cols,r)
            counts[r]+=1
        v=(mult,)*(1)+tuple(counts.get(i,0) for i in (1,2,3,4))
        assert v==ORBIT_ROWS[rows],(rows,v)
        for r,n in counts.items():glob[r]+=mult*n
    assert glob==EXPECTED,glob
    assert sum(glob.values())==1820**2
    print('EXACT_F16_FOURTH_MINOR_TWO_METHODS_PASS')
    print('row_orbits',len(orbits),'pairs',sum(glob.values()),'counts',dict(sorted(glob.items())))
    print('singular',sum(glob[k] for k in (1,2,3)),'nonsingular',glob[4])
if __name__=='__main__':run()
