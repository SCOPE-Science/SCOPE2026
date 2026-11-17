"""Exact 24-cell tetrahedral-volume spectrum and rigidity checker.

Run with Python >=3.8, standard library only. All computed arithmetic is integer.
"""
from itertools import combinations, product
from collections import Counter, defaultdict


def det3(A):
    a, b, c = A[0]
    d, e, f = A[1]
    g, h, i = A[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def vertices():
    result=[]
    for i in range(4):
        for s in (-1,1):
            a=[0]*4
            a[i]=2*s
            result.append(tuple(a))
    result.extend(product((-1,1),repeat=4))
    assert len(result)==len(set(result))==24
    assert all(dot(w,w)==4 for w in result)
    return tuple(result)


def spectral_certificate():
    W=vertices()
    histogram=Counter()
    maxsets=[]
    shapes=Counter()
    equilateral=0
    for ids in combinations(range(24),4):
        p=W[ids[0]]
        A=[tuple(W[j][i]-p[i] for i in range(4)) for j in ids[1:]]
        G=[[dot(x,y) for y in A] for x in A]
        D=det3(G)
        # Independent exact 3x3 minors, using Cauchy--Binet.
        minor_sum=sum(det3([[x[k] for k in range(4) if k!=omit] for x in A])**2 for omit in range(4))
        assert D==minor_sum>=0, (ids,D,minor_sum)
        histogram[D]+=1
        all_edges=[dot(tuple(W[i][k]-W[j][k] for k in range(4)),
                       tuple(W[i][k]-W[j][k] for k in range(4)))
                   for i,j in combinations(ids,2)]
        if all(z==8 for z in all_edges):
            equilateral+=1
            assert D==256
        if D==512:
            maxsets.append(ids)
            edges=tuple(sorted(dot(tuple(W[i][k]-W[j][k] for k in range(4)),
                                   tuple(W[i][k]-W[j][k] for k in range(4)))
                               for i,j in combinations(ids,2)))
            shorter=[set((i,j)) for i,j in combinations(ids,2)
                     if dot(tuple(W[i][k]-W[j][k] for k in range(4)),
                            tuple(W[i][k]-W[j][k] for k in range(4)))==8]
            assert len(shorter)==2 and shorter[0].isdisjoint(shorter[1])
            shapes[edges]+=1
    expected={0:474,32:2016,64:1344,96:1152,128:2592,160:576,
              192:1152,256:192,288:864,448:192,512:72}
    assert histogram==expected,(histogram,expected)
    assert sum(histogram.values())==10626
    assert len(maxsets)==72
    assert equilateral==48
    assert shapes=={(8,8,12,12,12,12):72}
    assert Counter(sum(i<8 for i in ids) for ids in maxsets)=={0:24,2:48}
    assert Counter(i for ids in maxsets for i in ids)=={i:12 for i in range(24)}
    top_triples=Counter(tri for ids in maxsets for tri in combinations(ids,3))
    assert len(top_triples)==288 and set(top_triples.values())=={1}
    return W, maxsets


def full_symmetry_orbit(W, maxsets):
    # Every ordered orthogonal 4-frame of 24-cell vertices is an isometry.
    Wset=set(W)
    index={p:i for i,p in enumerate(W)}
    orbit=set()
    count=0
    reference=maxsets[0]
    for frame in product(range(24),repeat=4):
        if any(dot(W[frame[i]],W[frame[j]]) for i,j in combinations(range(4),2)):
            continue
        count+=1
        columns=[W[j] for j in frame]
        images=[]
        for w in W:
            nums=[sum(w[i]*columns[i][k] for i in range(4)) for k in range(4)]
            assert all(x%2==0 for x in nums)
            x=tuple(z//2 for z in nums)
            assert x in Wset
            images.append(index[x])
        assert len(set(images))==24
        orbit.add(tuple(sorted(images[j] for j in reference)))
    assert count==1152, count
    assert orbit==set(maxsets), (len(orbit),len(maxsets))
    return count


if __name__=='__main__':
    W, maxsets = spectral_certificate()
    group_size = full_symmetry_orbit(W,maxsets)
    print('VERIFY_OK_24CELL_TETRA_SPECTRUM vertex_subsets=10626 maxima=72 eigengroup_frames=%d no_shared_triple=1' % group_size)
