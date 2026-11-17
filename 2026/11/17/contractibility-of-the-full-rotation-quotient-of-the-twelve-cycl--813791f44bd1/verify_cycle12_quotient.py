#!/usr/bin/env python3
"""Exact chain certificate for the rotation quotient of the C12 independence complex.

Standard Python 3 only. Run `python verify_cycle12_quotient.py c12_reduction_certificate.json`.
"""
import collections
import itertools
import json
import pathlib
import sys

N = 12

def independent(face):
    s = set(face)
    return all((v+1) % N not in s for v in s)

def shift(face, k):
    return tuple(sorted((x+k) % N for x in face))

def flag_orbit(flag):
    return min(tuple(shift(f,k) for f in flag) for k in range(N))

def build():
    faces = sorted((tuple(i for i in range(N) if bits & (1 << i))
                    for bits in range(1, 1 << N)
                    if independent([i for i in range(N) if bits & (1 << i)])),
                   key=lambda f:(len(f),f))
    supersets = {f: [] for f in faces}
    for i, f in enumerate(faces):
        sf=set(f)
        for e in faces[i+1:]:
            if sf < set(e): supersets[f].append(e)
    flags=[]
    def extend(chain):
        flags.append(tuple(chain))
        for e in supersets[chain[-1]]: extend(chain+[e])
    for f in faces: extend([f])
    orbits=sorted(set(map(flag_orbit,flags)),key=lambda f:(len(f),f))
    index={f:i for i,f in enumerate(orbits)}
    degree={i:len(f)-1 for i,f in enumerate(orbits)}
    boundary={}
    for i,f in enumerate(orbits):
        d={}
        for j in range(len(f)):
            if len(f)==1: continue
            face=index[flag_orbit(f[:j]+f[j+1:])]
            d[face]=d.get(face,0)+(-1)**j
        boundary[i]={j:v for j,v in d.items() if v}
    assert len(faces)==321 and len(flags)==38347
    counts=[sum(degree[i]==d for i in degree) for d in range(6)]
    assert counts==[30,291,912,1190,660,120],counts
    # Burnside count independent of the orbit enumeration.
    for d in range(6):
        fixed=sum(sum(all(shift(f,k)==f for f in flag) for flag in flags if len(flag)==d+1)
                  for k in range(N))
        assert fixed==N*counts[d], (d,fixed)
    # Cellular boundary composition, computed entirely with signed integers.
    for i in boundary:
        dd=collections.defaultdict(int)
        for j,a in boundary[i].items():
            for k,b in boundary[j].items():dd[k]+=a*b
        assert all(x==0 for x in dd.values()),i
    return boundary, degree, counts

def replay(cert, boundary, degree):
    alive=set(boundary)
    for j,i in cert['elementary_pairs']:
        assert i in alive and j in alive and degree[i]==degree[j]+1
        cofaces=[h for h in alive if j in boundary[h]]
        assert cofaces==[i],(j,i,'not free')
        assert not any(i in boundary[h] for h in alive),(j,i,'not maximal')
        assert abs(boundary[i][j])==1
        alive.remove(i)
        alive.remove(j)
    assert len(cert['elementary_pairs'])==1242
    C={i:{j:v for j,v in boundary[i].items() if j in alive} for i in alive}
    # Schur complement for an invertible (+/-1) incidence entry; valid over Z.
    for j,i,a in cert['algebraic_pairs']:
        assert i in C and j in C and degree[i]==degree[j]+1
        assert C[i].get(j)==a and abs(a)==1
        cofaces=[(h,d[j]) for h,d in C.items() if j in d]
        pivot=C[i].copy()
        for h,b in cofaces:
            if h==i:continue
            col=C[h]
            for jj,z in pivot.items():
                val=col.get(jj,0)-b*a*z
                if val:col[jj]=val
                else:col.pop(jj,None)
            assert j not in col
        for h in list(C):
            C[h].pop(i,None)
        del C[i]
        del C[j]
    assert len(cert['algebraic_pairs'])==359
    assert len(C)==1 and next(iter(C.values()))=={}
    only=next(iter(C))
    assert degree[only]==0 and only==cert['expected_final_cell']==1
    assert len(boundary)==1+2*(1242+359)
    return only

def main():
    path=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'c12_reduction_certificate.json')
    cert=json.loads(path.read_text(encoding='utf8'))
    assert cert['n']==N and cert['expected_cell_counts']==[30,291,912,1190,660,120]
    assert independent((0,3,6,9)) and independent((0,4,8))
    assert shift((0,3,6,9),3)==(0,3,6,9)
    assert shift((0,4,8),4)==(0,4,8)
    C,D,counts=build()
    last=replay(cert,C,D)
    print('N=12; 321 nonempty independent faces; 38,347 barycentric flags')
    print('Quotient cell counts: '+repr(tuple(counts)))
    print('Burnside counts and integral boundary-square-zero: VERIFIED')
    print('Elementary collapses: 1242; integral unit cancellations: 359')
    print('Residual chain complex: one degree-zero generator (cell %d)'%last)
    print('Fixed simplex stabilizers: orders 4 and 3, generating C12')
    print('CERTIFICATE_OK')

if __name__=='__main__':main()
