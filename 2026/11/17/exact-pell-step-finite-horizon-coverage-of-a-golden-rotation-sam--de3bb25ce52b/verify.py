"""Reproducible finite checks for golden half-window two-shift coverage.

All-horizon optimality and limit claims require the accompanying proof.
"""
from decimal import Decimal, getcontext
from math import sqrt

getcontext().prec = 65
S = Decimal(5).sqrt()
alpha = (S-1)/2
r = S-2


def pell_records(n):
    # Each (l,k) approximates sqrt(5) with the parity for a half-circle hit.
    a,b=(2,1),(9,4)
    out=[]
    for _ in range(n):
        out.append(a)
        a,b=b,(4*b[0]+a[0],4*b[1]+a[1])
    return out


def critical_loss(k):
    # Twice the distance from k*alpha modulo 1 to the antipode.
    # Equivalently, minimum over integers l with l-k odd.
    v = Decimal(k)*S
    z = int(v)
    return min(abs(v-Decimal(l)) for l in range(z-1,z+3) if (l-k)%2==1)


def main():
    pairs=pell_records(9)
    for j,(l,k) in enumerate(pairs):
        assert (l-k)%2==1
        assert l*l-5*k*k==(-1)**(j+1)
        assert abs(Decimal(l)-S*k-r**(j+1)*((-1)**(j+1)))<Decimal('1e-50')
        assert abs(critical_loss(k)-r**(j+1)) < Decimal('1e-50')
        if j: assert abs(pairs[j-1][0]*k-l*pairs[j-1][1])==1
    # All positive horizons up to 5472 checked independently of the proof.
    record_k=[]
    best=Decimal(9)
    for k in range(1,5473):
        loss=critical_loss(k)
        if loss<best:
            record_k.append(k)
            best=loss
    assert record_k == [k for l,k in pairs if k<5473], (record_k,pairs)
    # Direct sampling verifies that the finite set density approaches the
    # precise circular interval-union measure for several finite shifts.
    aa=(sqrt(5)-1)/2
    for k in (1,2,3,4,5,17,72,305):
        t=(k*aa)%1
        union_ratio=2-2*abs(t-0.5)
        N=100000
        count=sum(1 for j in range(N) if ((j*aa+0.173)%1<0.5) or (((j-k)*aa+0.173)%1<0.5))
        assert abs(count/(N*0.5)-union_ratio)<0.0015,(k,union_ratio,count)
    print('VERIFY_OK Pell_identities=9 horizon_minimizers=5472 direct_density_tests=8')
    print('FINITE_CHECK_ONLY: irrational equidistribution and infinite staircase follow analytically')

if __name__=='__main__': main()
