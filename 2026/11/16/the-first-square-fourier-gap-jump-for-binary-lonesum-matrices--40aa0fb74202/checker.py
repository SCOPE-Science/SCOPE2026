#!/usr/bin/env python3
"""Exact Walsh census for binary lonesum matrices, with two enumerators.

Usage: python3 checker.py [output_directory]
Requires Python 3 standard library only. No numerical approximations.
"""
import csv
import itertools
import sys
from collections import Counter
from pathlib import Path


def nested_rows(x, n, m):
    mask = (1 << n) - 1
    rows = [(x >> (i*n)) & mask for i in range(m)]
    for i in range(m):
        for j in range(i+1, m):
            z = rows[i] & rows[j]
            if z != rows[i] and z != rows[j]:
                return False
    return True


def no_forbidden_two_by_two(x, n, m):
    for r in range(m):
        for s in range(r + 1, m):
            for c in range(n):
                for d in range(c + 1, n):
                    a = (x >> (r*n+c)) & 1
                    b = (x >> (r*n+d)) & 1
                    u = (x >> (s*n+c)) & 1
                    v = (x >> (s*n+d)) & 1
                    if a == v and b == u and a != b:
                        return False
    return True


def fourier_indicator(m, n):
    size = 1 << (m*n)
    v = [int(nested_rows(x,n,m)) for x in range(size)]
    if m*n <= 16:
        assert all(bool(v[x]) == no_forbidden_two_by_two(x,n,m) for x in range(size))
    for bit in range(m*n):
        half = 1 << bit
        for start in range(0,size,half*2):
            for j in range(half):
                a,b = v[start+j],v[start+j+half]
                v[start+j]=a+b
                v[start+j+half]=a-b
    return v


def symmetry_orbit_certificate(m=4,n=4):
    size = 1 << (m*n)
    valid = [x for x in range(size) if no_forbidden_two_by_two(x,n,m)]
    assert len(valid) == 6902
    assert all(nested_rows(x,n,m) for x in valid)
    col_perms=list(itertools.permutations(range(n)))
    row_perms=list(itertools.permutations(range(m)))
    maps=[]
    for perm in col_perms:
        maps.append([sum(((r>>j)&1)<<perm[j] for j in range(n)) for r in range(1<<n)])
    seen=bytearray(size)
    coeffs=[None]*size
    cert=[]
    mask=(1<<n)-1
    for f in range(size):
        if seen[f]: continue
        rows = [(f >> (n*j))&mask for j in range(m)]
        members=set()
        for rp in row_perms:
            for cp in maps:
                z=0
                for i in range(m): z |= cp[rows[i]] << (n*rp[i])
                members.add(z)
        # Direct character sum; no Fourier transform is used here.
        value=sum(1 if ((f&x).bit_count()&1)==0 else -1 for x in valid)
        for z in members:
            assert not seen[z]
            seen[z]=1
            coeffs[z]=value
        cert.append((f,len(members),value))
    assert all(seen)
    assert sum(row[1] for row in cert) == size
    return cert,coeffs


def verify():
    res={}
    for m in (2,3,4):
        values=fourier_indicator(m,m)
        nonzero=[abs(v) for v in values if v]
        res[m]={'total': values[0], 'minimum':min(nonzero),
                'rank':len(nonzero), 'frequencies':len(values)}
        assert res[m]['rank']==len(values)//2
        if m in (2,3): assert res[m]['minimum']==2
        if m==4: assert res[m]['minimum']==6
    cert, orbit_values=symmetry_orbit_certificate()
    vals=fourier_indicator(4,4)
    assert vals==orbit_values, 'Independent orbit and butterfly censuses differ'
    hist=Counter(abs(v) for v in vals)
    assert hist[0]==32768
    assert hist[6]==6360
    assert len([k for k in hist if k])==34
    assert sum(hist.values())==65536
    assert len(cert)==317
    assert vals[0]==6902
    assert all((v%16 == 6 if (i.bit_count()%2==0) else v==0)
               for i,v in enumerate(vals))
    assert sum(v*v for v in vals)==(1<<16)*6902, 'Parseval failed'
    return res,cert,hist


def main():
    res,cert,hist=verify()
    if len(sys.argv)>1:
        directory=Path(sys.argv[1]);directory.mkdir(parents=True,exist_ok=True)
        with (directory/'ORBIT_SPECTRUM.csv').open('w',newline='',encoding='utf-8') as f:
            w=csv.writer(f,lineterminator='\n');w.writerow(['frequency_hex','orbit_size','signed_walsh'])
            w.writerows((f'{a:04x}',b,c) for a,b,c in cert)
        with (directory/'MAGNITUDE_SPECTRUM.csv').open('w',newline='',encoding='utf-8') as f:
            w=csv.writer(f,lineterminator='\n');w.writerow(['absolute_walsh','frequency_count'])
            w.writerows(sorted(hist.items()))
    print('SQUARE_LONESUM_ORBIT_WALSH_EXACT_PASS',res,'orbits',len(cert),
          'nonzero_abs_levels',len(hist)-1,'minimum_attainers',hist[6])

if __name__=='__main__': main()
