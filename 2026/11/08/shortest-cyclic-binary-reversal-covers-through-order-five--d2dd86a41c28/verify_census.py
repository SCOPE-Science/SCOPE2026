#!/usr/bin/env python3
"""Independent exhaustive word-by-word census, including cyclic symmetry."""
from itertools import product
from pathlib import Path
import sys

EXPECTED = {1:(2,1,1),2:(4,1,1),3:(8,2,1),4:(14,8,3),5:(26,128,36)}
HERE = Path(__file__).resolve().parent

def canon(w):
    return min(w[i:]+w[:i] for i in range(len(w)))

def flip(w):
    return ''.join('1' if v=='0' else '0' for v in w)

def enumerate_cyclic(n,L):
    classes = {min(''.join(t),''.join(t)[::-1]) for t in product('01',repeat=n)}
    rooted = []
    cycles = set()
    for suffix in product('01',repeat=L-n):
        w = '0'*n+''.join(suffix)
        circular = w+w[:n-1]
        observed = {min(circular[i:i+n],circular[i:i+n][::-1]) for i in range(L)}
        if observed == classes:
            rooted.append(w)
            cycles.add(canon(w))
    return len(classes),rooted,sorted(cycles)

def main():
    make = sys.argv[1:]==['--write']
    assert sys.argv[1:] in ([],['--write'])
    for n,(opt,count,bracelet_count) in EXPECTED.items():
        n_classes=None
        for L in range(max(1,n),opt+1):
            n_classes,rooted,cycles = enumerate_cyclic(n,L)
            if L>=n_classes and L<opt: assert not rooted
        assert len(rooted)==len(cycles)==count
        assert all(sum((w+w[:n-1])[i:i+n]=='0'*n for i in range(len(w)))==1 for w in cycles)
        bracelets = {min(canon(w),canon(w[::-1]),canon(flip(w)),canon(flip(w[::-1]))) for w in cycles}
        assert len(bracelets)==bracelet_count
        if n in (4,5):
            path=HERE/f'cycles_order{n}.txt'
            content='\n'.join(cycles)+'\n'
            if make:path.write_text(content,encoding='utf-8')
            else:assert path.read_text(encoding='utf-8')==content
        print(f'order={n} min_length={opt} necklaces={count} reversal_complement_orbits={bracelet_count}')
    print('CENSUS_VERIFY_OK')

if __name__ == '__main__': main()
