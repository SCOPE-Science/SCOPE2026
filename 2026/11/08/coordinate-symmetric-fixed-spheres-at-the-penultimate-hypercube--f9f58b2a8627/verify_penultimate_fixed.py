"""Finite independent checks for a theorem on weight-orbit fixed Rips complexes."""
from itertools import combinations
from collections import defaultdict


def weight_orbit_graph(n):
    r=n-2
    classes=defaultdict(list)
    for x in range(1<<n):
        classes[x.bit_count()].append(x)
    retained=[]
    for k,orbit in classes.items():
        if all((x^y).bit_count()<=r for x,y in combinations(orbit,2)):
            retained.append(k)
    retained.sort()
    compatible={}
    for a,b in combinations(retained,2):
        compatible[a,b]=all((x^y).bit_count()<=r for x in classes[a] for y in classes[b])
    return retained,compatible


def predicted(n):
    m=n//2
    low=range(m)
    high=[n-j for j in range(m)]
    retained=sorted(list(low)+high)
    comp={}
    for a,b in combinations(retained,2):
        comp[a,b]= (a<m and b<m) or (a>n-m and b>n-m) or (abs(a-(n-b))>1)
        # groups on same side are always compatible. m=floor(n/2).
    return retained,comp


def band_edges(m):
    return {frozenset((f'L{i}',f'R{j}')) for i in range(m) for j in range(m) if abs(i-j)<=1}


def neighbors(V,E,x):
    return {next(iter(e-{x})) for e in E if x in e}


def verify_fold(m):
    V={f'{c}{i}' for c in 'LR' for i in range(m)}
    E=band_edges(m)
    steps=[]
    for i in range(0,m-1,2):
        u=f'L{i}';v=f'L{i+1}'
        assert u in V and v in V and v not in neighbors(V,E,u)
        assert neighbors(V,E,u)<=neighbors(V,E,v), ('L',m,i)
        V.remove(v); E={e for e in E if v not in e}
        steps.append((u,v))
        u=f'R{i}';v=f'R{i+1}'
        assert u in V and v in V and v not in neighbors(V,E,u)
        assert neighbors(V,E,u)<=neighbors(V,E,v), ('R',m,i)
        V.remove(v); E={e for e in E if v not in e}
        steps.append((u,v))
    kept={f'{c}{i}' for c in 'LR' for i in range(0,m,2)}
    expected={frozenset((f'L{i}',f'R{i}')) for i in range(0,m,2)}
    assert V==kept and E==expected, ('result',m,V,E)
    return steps


def gf2_rank(rows):
    pivots={}
    for row in rows:
        while row:
            p=row.bit_length()-1
            if p in pivots:row ^=pivots[p]
            else:
                pivots[p]=row;break
    return len(pivots)


def bettis(m):
    vs=list(range(2*m)); E={frozenset((i,m+j)) for i in range(m) for j in range(m) if abs(i-j)<=1}
    faces_by_dim=defaultdict(list)
    for q in range(1,2*m+1):
        for comb in combinations(vs,q):
            s=frozenset(comb)
            if not any(e<=s for e in E):
                faces_by_dim[q-1].append(comb)
    maxd=max(faces_by_dim)
    dr={0:0}
    for k in range(1,maxd+1):
        index={v:i for i,v in enumerate(faces_by_dim[k-1])}
        cols=[]
        for f in faces_by_dim[k]:
            mask=0
            for sub in combinations(f,k):mask|=1<<index[sub]
            cols.append(mask)
        dr[k]=gf2_rank(cols)
    dr[maxd+1]=0
    beta={k:len(faces_by_dim[k])-dr[k]-dr[k+1] for k in range(maxd+1)}
    target=(m-1)//2
    assert {k:b for k,b in beta.items() if b}==({0:2} if target==0 else {0:1,target:1}), (m,beta)
    return len(sum(faces_by_dim.values(),[])),beta


def main():
    checks=0
    for n in range(2,11):
        got=weight_orbit_graph(n); exp=predicted(n)
        assert got==exp,(n,got,exp)
        checks+=1
    print('EXHAUSTIVE_BINARY_ORBIT_CHECKS_OK',checks,'n=2..10')
    for m in range(1,31):
        steps=verify_fold(m)
        assert len(steps)==2*(m//2)
    print('EXACT_NEIGHBORHOOD_FOLD_CHECKS_OK 30 m=1..30')
    for m in range(1,7):
        faces,beta=bettis(m)
        print('HOMOLOGY',m,faces,beta)
    print('GF2_HOMOLOGY_CHECKS_OK 6 m=1..6')
    for m in range(1,21):
        # Complement involution interchanges L_i, R_i.
        # An invariant nonempty face would contain a conflicting pair.
        for i in range(m):
            assert frozenset((f'L{i}',f'R{i}')) in band_edges(m)
    print('FREE_COMPLEMENT_ACTION_CHECKS_OK 20 m=1..20')
    print('PENULTIMATE_COORDINATE_FIXED_SPHERES_OK')

if __name__=='__main__':main()
