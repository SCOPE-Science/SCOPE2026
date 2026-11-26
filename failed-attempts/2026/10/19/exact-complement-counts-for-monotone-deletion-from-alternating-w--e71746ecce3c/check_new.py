"""Independent finite checks for alternating-word monotone-deletion complement theorem."""
from itertools import combinations
from math import comb

def direct_complements(m,k):
    w='01'*m
    out=set()
    for zeros in combinations(range(m),k):
        for ones in combinations(range(zeros[-1],m),k):
            removed={2*i for i in zeros}|{2*j+1 for j in ones}
            out.add(''.join(letter for i,letter in enumerate(w) if i not in removed))
    return out

def gap_compositions(total,prefixes):
    if prefixes==1:
        yield (total,)
    else:
        for i in range(total+1):
            for x in gap_compositions(total-i,prefixes-1):
                yield (i,)+x

def structural_words(r,j):
    if j>r:return set()
    out=set()
    for c in gap_compositions(r-j,2*j+1):
        v=''
        for i,a in enumerate(c):
            v+='01'*a
            if i<j:v+='1'
            elif i<2*j:v+='0'
        assert v.count('0')==v.count('1')==r
        assert len(v)==2*r
        assert v not in out,(r,j,v,c)
        out.add(v)
    assert len(out)==comb(r+j,2*j)
    return out

def independent_shape_words(r,j):
    out=set()
    for z in combinations(range(2*r),r):
        zero_positions=set(z)
        v=''.join('0' if a in zero_positions else '1' for a in range(2*r))
        peaks=excess=0
        for a in v:
            excess+=1 if a=='1' else -1
            peaks=max(peaks,excess)
        ones=[i for i in range(2*r-1) if v[i:i+2]=='11']
        zeros=[i for i in range(2*r-1) if v[i:i+2]=='00']
        if peaks==j and (not ones or not zeros or max(ones)<min(zeros)):
            out.add(v)
    return out

cases=0
for m in range(1,12):
    for k in range(1,m+1):
        if m<2*k-1:
            assert not direct_complements(m,k)
            continue
        r=m-k
        observed=direct_complements(m,k)
        structural=structural_words(r,k)|structural_words(r,k-1)
        assert observed==structural,(m,k,len(observed),len(structural),list(observed^structural)[:5])
        target=comb(m-1,2*k-2)+(comb(m,2*k) if 2*k<=m else 0)
        assert len(observed)==target,(m,k,len(observed),target)
        if r<=8:
            for j in (k-1,k):
                if j<=r:assert structural_words(r,j)==independent_shape_words(r,j)
        cases+=1
print('EXACT ENUMERATION, NORMAL FORM, SHAPE AND BINOMIAL CHECKS PASS; parameter pairs:',cases)
