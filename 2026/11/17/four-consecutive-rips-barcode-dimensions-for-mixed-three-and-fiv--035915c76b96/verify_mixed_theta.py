"""Exact finite checks for mixed-length theta graph Rips attachments.

Run: python3 verify_mixed_theta.py
Uses only the Python standard library. The uniform theorem is proved separately.
"""
from collections import defaultdict, deque
from itertools import combinations


def theta(short_count, long_lengths):
    E = set()
    names = ['u', 'v']
    def add_path(index, length):
        x = ['u'] + [f'{index}_{i}' for i in range(1, length)] + ['v']
        names.extend(x[1:-1])
        for a, b in zip(x, x[1:]): E.add(tuple(sorted((a,b))))
    for j in range(short_count): add_path(f's{j}', 3)
    for j, length in enumerate(long_lengths): add_path(f'l{j}', length)
    return names, E


def paths_dists(vertices, edges):
    N = {x: set() for x in vertices}
    for a,b in edges: N[a].add(b); N[b].add(a)
    D = {}
    for x in vertices:
        d={x:0}; todo=deque([x])
        while todo:
            a=todo.popleft()
            for b in N[a]:
                if b not in d: d[b]=d[a]+1; todo.append(b)
        assert len(d)==len(vertices)
        D[x]=d
    return D


def rips_faces(vertices, distances, scale):
    # Incremental flag-complex enumeration; includes all nonempty faces.
    order = sorted(vertices)
    nbr = {v: {w for w in order if w>v and distances[v][w]<=scale} for v in order}
    faces=set()
    def rec(prefix, available):
        for x in sorted(available):
            f=prefix+(x,)
            faces.add(f)
            rec(f, available.intersection(nbr[x]))
    rec((), set(order))
    return faces


def remove_pair(faces, low, high):
    low=tuple(sorted(low)); high=tuple(sorted(high))
    assert len(high)==len(low)+1 and set(low).issubset(high)
    assert low in faces and high in faces
    co=[f for f in faces if len(f)>len(low) and set(low).issubset(f)]
    assert co==[high], (low,high,co)
    faces.remove(low); faces.remove(high)


def collapse_attachment(old_vertices, old_edges, length):
    nvs=list(old_vertices)+[f'z{i}' for i in range(1,length)]
    es=set(old_edges)
    chain=['u']+[f'z{i}' for i in range(1,length)]+['v']
    es.update(tuple(sorted(pair)) for pair in zip(chain,chain[1:]))
    Dnew=paths_dists(nvs,es)
    Dold=paths_dists(old_vertices,old_edges)
    assert Dold['u']['v']>=3
    for x in old_vertices:
        for y in old_vertices:
            assert (Dnew[x][y]<=2)==(Dold[x][y]<=2)
    faces=rips_faces(nvs,Dnew,2)
    init_count=len(faces)
    oldfaces=rips_faces(old_vertices,Dold,2)
    NL=rips_faces(chain,Dnew,2)
    expected=(oldfaces|NL)
    Nu=sorted(x for x in old_vertices if Dold['u'][x]==1)
    Nv=sorted(x for x in old_vertices if Dold['v'][x]==1)
    assert not set(Nu).intersection(Nv)
    pred=set(expected)
    for center, z, near in [('u','z1',Nu),('v',f'z{length-1}',Nv)]:
        for m in range(1,len(near)+1):
            for T in combinations(near,m):
                pred.add(tuple(sorted((z,)+T)))
                pred.add(tuple(sorted((z,center)+T)))
    assert faces==pred, ('unexpected simplex',len(faces^pred))
    count=0
    for center,z,near in [('u','z1',Nu),('v',f'z{length-1}',Nv)]:
        for k in range(len(near),0,-1):
            for T in combinations(near,k):
                remove_pair(faces,(z,)+T,(z,center)+T)
                count+=1
    assert faces==expected
    for j in range(0,length-1):
        low=(chain[j],chain[j+2]); high=(chain[j],chain[j+1],chain[j+2])
        remove_pair(faces,low,high)
        count+=1
    assert faces==(oldfaces|{tuple(sorted((x,y))) for x,y in zip(chain,chain[1:])}|{(z,) for z in chain})
    assert init_count-len(faces)==2*count
    return count, init_count


def gf2_rank(rows):
    piv={}; rank=0
    for r in rows:
        while r:
            k=r.bit_length()-1
            if k not in piv: piv[k]=r;rank+=1;break
            r^=piv[k]
    return rank


def bettis_mod2(faces):
    B=defaultdict(list)
    for f in faces: B[len(f)-1].append(f)
    for k in B:B[k].sort()
    ranks={}
    for k in B:
        if k==0:ranks[k]=0;continue
        idx={f:j for j,f in enumerate(B[k-1])}
        rows=[]
        for f in B[k]:
            b=0
            for i in range(len(f)):
                b^=1<<idx[f[:i]+f[i+1:]]
            rows.append(b)
        ranks[k]=gf2_rank(rows)
    return {k:len(f)-ranks.get(k,0)-ranks.get(k+1,0) for k,f in B.items()}


def theta_check(p, lengths):
    V,E=theta(p,lengths)
    D=paths_dists(V,E)
    K=rips_faces(V,D,2)
    b=bettis_mod2(K)
    assert b.get(0)==1,(p,lengths,b)
    assert b.get(1,0)==len(lengths),(p,lengths,b)
    assert b.get(2,0)==p-1,(p,lengths,b)
    assert all(b[k]==0 for k in b if k>2),(p,lengths,b)
    if all(t==4 for t in lengths):
        # Pick s0_1: every vertex is at graph distance <=3.
        cone='s0_1'
        assert all(D[cone][w]<=3 for w in V)
    return len(V), len(K)


def main():
    counter=0; total=0; sample=[]
    for p in range(2,6):
        for lengths in ([4],[5],[7],[4,4],[4,6],[5,7],[4,4,4]):
            V,E=theta(p,[])
            for length in lengths:
                x,c=collapse_attachment(V,E,length)
                total+=x;counter+=1
                # extend original graph with path for next test
                nvs=[f'new{counter}_{i}' for i in range(1,length)]
                path=['u']+nvs+['v']
                V+=nvs
                E|={tuple(sorted(e)) for e in zip(path,path[1:])}
            nv,nf=theta_check(p,lengths)
            sample.append((p,tuple(lengths),nv,nf))
    # Structural checks beyond the theta family, including longer pole separation,
    # triangles at poles and a shortened old distance still exceeding two.
    arbitrary=[
      (['u','a','b','v'],{('u','a'),('a','b'),('b','v')}),
      (['u','a','b','c','v'],{('u','a'),('a','b'),('b','c'),('c','v')}),
      (['u','a','b','c','d','v'],{('u','a'),('a','b'),('b','c'),('c','d'),('d','v')}),
      (['u','a','b','v','x','y'],{('u','a'),('a','b'),('b','v'),('u','x'),('u','y'),('x','y')}),
      (['u','a','b','v','x','y','z'],{('u','a'),('a','b'),('b','v'),('u','x'),('u','y'),('x','y'),('b','z'),('v','z')}),
    ]
    for V,E in arbitrary:
        for length in (4,5,8):
            pairs, _=collapse_attachment(V,E,length)
            total+=pairs;counter+=1
    print('MIXED_THETA_PATH_ATTACHMENTS_OK',counter,'relative collapses;',total,'elementary collapse pairs')
    print('MIXED_THETA_HOMOLOGY_OK',len(sample),'cases; samples',sample[0],sample[-1])
    print('MIXED_THETA_VERIFIED')


if __name__=='__main__': main()
