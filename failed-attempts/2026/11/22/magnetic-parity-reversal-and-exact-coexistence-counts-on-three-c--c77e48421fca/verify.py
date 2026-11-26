"""Independent exact finite checks for Möbius-ladder Potts ground-state formula.
Run with Python 3.10+; no external dependencies.
"""
from itertools import product
from fractions import Fraction
from math import isqrt

def edges(n):
    # Vertices are 0,...,2n-1 on a ring, with n opposite chords.
    return [(i,(i+1)%(2*n)) for i in range(2*n)] + [(i,i+n) for i in range(n)]

def sector_spectrum(n):
    out={}
    for config in product(range(3),repeat=2*n):
        k=sum(v==0 for v in config)
        e=sum(config[a]==config[b] for a,b in edges(n))
        if k not in out or e<out[k][0]: out[k]=[e,1]
        elif e==out[k][0]: out[k][1]+=1
    return out

def indep_poly_at_2(n):
    E=edges(n)
    ans=0
    for bits in range(1<<(2*n)):
        if all(not(bits>>a&1 and bits>>b&1) for a,b in E):
            ans+=2**bits.bit_count()
    return ans

def expectation(n,field):
    if n%2:
        if field==0:return None,3**n-1-2*(-2)**n
        if field<3:return (n,), 2**(n+1)
        if field==3:return None,indep_poly_at_2(n)
        return (2*n,),1
    if field==0:return None,3**n-1-2*(-2)**n
    if field<1:return (n-1,),n*2**(n-1)
    if field==1:return (n-1,n),3*n*2**(n-1)
    if field<2:return (n,),n*2**n
    if field==2:return (n,n+1),n*2**(n+1)
    if field<3:return (n+1,),n*2**n
    if field==3:return None,indep_poly_at_2(n)
    return (2*n,),1

def test():
    checks=0
    fields=[Fraction(0),Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(2),Fraction(5,2),Fraction(3),Fraction(7,2)]
    for n in range(3,7):
        spectra=sector_spectrum(n)
        for field in fields:
            best=min(Fraction(e)-field*k for k,(e,_) in spectra.items())
            ks=tuple(sorted(k for k,(e,_) in spectra.items() if Fraction(e)-field*k==best))
            multiplicity=sum(spectra[k][1] for k in ks)
            predicted_ks,predicted_mult=expectation(n,field)
            if predicted_ks is not None:
                assert ks==predicted_ks,(n,field,ks,predicted_ks)
            assert multiplicity==predicted_mult,(n,field,multiplicity,predicted_mult)
            checks+=1
        # Verify critical transfer eigenvalue recurrence without floating point.
        lucas=[2,3]
        for _ in range(n-1):lucas.append(3*lucas[-1]+2*lucas[-2])
        assert indep_poly_at_2(n)==lucas[n]-(-2)**n
        checks+=1
    # Larger-n ground-sector comparisons from a different 9-state min-plus transfer.
    states=list(product(range(3),repeat=2))
    for n in range(7,18):
        out={}
        for first in states:
            dp={(first,int(first[0]==0)+int(first[1]==0)):(int(first[0]==first[1]),1)}
            for _ in range(n-1):
                nxt={}
                for (last,k),(e,c) in dp.items():
                    for current in states:
                        kk=k+int(current[0]==0)+int(current[1]==0)
                        ee=e+int(current[0]==current[1])+int(current[0]==last[0])+int(current[1]==last[1])
                        key=(current,kk)
                        if key not in nxt or ee<nxt[key][0]:nxt[key]=(ee,c)
                        elif ee==nxt[key][0]:nxt[key]=(ee,nxt[key][1]+c)
                dp=nxt
            for (last,k),(e,c) in dp.items():
                ee=e+int(last[0]==first[1])+int(last[1]==first[0])
                if k not in out or ee<out[k][0]:out[k]=(ee,c)
                elif ee==out[k][0]:out[k]=(ee,out[k][1]+c)
        for field in fields:
            best=min(Fraction(e)-field*k for k,(e,_) in out.items())
            ks=tuple(sorted(k for k,(e,_) in out.items() if Fraction(e)-field*k==best))
            count=sum(out[k][1] for k in ks)
            expected_ks,expected_count=expectation_no_enumeration(n,field)
            if expected_ks is not None:assert ks==expected_ks,(n,field,ks,expected_ks)
            assert count==expected_count,(n,field,count,expected_count)
            checks+=1
    print('ALL_EXACT_CHECKS_PASSED',checks)

def expectation_no_enumeration(n,field):
    if field!=3:return expectation(n,field)
    s0,s1=2,3
    for _ in range(2,n+1):s0,s1=s1,3*s1+2*s0
    return None,s1-(-2)**n

if __name__=='__main__':test()
