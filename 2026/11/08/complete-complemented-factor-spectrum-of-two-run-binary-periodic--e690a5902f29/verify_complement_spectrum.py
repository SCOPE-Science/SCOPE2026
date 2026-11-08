#!/usr/bin/env python3
"""Exhaustive direct factor-language checker for the independent two-run complement-spectrum theorem."""

def complement(s):
    return s.translate(str.maketrans('01','10'))

def actual(a,b,n):
    period='0'*a+'1'*b
    length=len(period)
    seq=(period*((n//length)+3))
    factors={seq[i:i+n] for i in range(length)}
    return {w for w in factors if complement(w) in factors}

def formula_set(a,b,n):
    m=min(a,b)
    if a!=b:
        forms={c*n for c in '01' if 1<=n<=m}
        forms|={x*i+y*j for x,y in ('01','10') for i in range(1,m+1) for j in range(1,m+1) if i+j==n}
        return forms
    # Equal-run case: complement symmetry means all factors.
    period='0'*a+'1'*b
    seq=(period*((n//len(period))+3))
    return {seq[i:i+n] for i in range(len(period))}

def run():
    configs=0
    lengths=0
    summed=0
    for a in range(1,17):
        for b in range(1,17):
            configs+=1
            p=a+b
            for n in range(1,3*p+3):
                got=actual(a,b,n)
                expect=formula_set(a,b,n)
                assert got==expect,(a,b,n,sorted(got^expect))
                count=2*min(n,2*min(a,b)-n+1) if a!=b and n<=2*min(a,b) else 0
                if a!=b:
                    assert len(got)==count,(a,b,n,len(got),count)
                else:
                    assert len(got)==2*min(n,a),(a,b,n,len(got))
                lengths+=1
                summed+=len(got)
            if a!=b:
                assert sum(len(actual(a,b,n)) for n in range(1,2*min(a,b)+1))==2*min(a,b)*(min(a,b)+1)
    print('PASS',configs,'parameter pairs,',lengths,'length profiles,',summed,'total per-length complemented-word occurrences checked')
if __name__=='__main__':run()
