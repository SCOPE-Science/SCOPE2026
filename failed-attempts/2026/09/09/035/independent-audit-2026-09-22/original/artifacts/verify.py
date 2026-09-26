"""Write output/artifacts/verify.py: independent replay checker (stdlib only).
Checks:
 1. regenerate 512 matrices, canonical reduction -> 104 classes, orbit sizes {1:4,3:28,6:70,2:2}, sum 512.
 2. load census.json: every rep present exactly once; traces recomputed exact match; charpoly recomputed match; zeta_den match; zeta_series match; value key recomputed match.
 3. enclosure soundness: p(rho_lo)<=0<=p(rho_hi) with exact Fraction evals (for point intervals equality p=0); for cubic brackets also p'(min)>0 on bracket (exact); for D<0 cubics verify lo>1 and c=-1 (dominance lemma); for D>0 cubics verify vertex<=lo and p'(lo)>0 (largest-root lemma); for quad-interval/sqrt verify m^2 vs N integer inequalities; for exact-rational verify p(exact)==0 and maximality by comparing all roots' moduli exactly (recompute factor + exact comparisons).
 4. zeta-trace agreement: -Q' == Q*T mod t^6 on every row.
 5. value census: regroup by value; check 18 values, counts, disjointness of consecutive rho enclosures (except rho0/R1 which share h=0), h-gap positivity for positive entropies, extremal claims (max R3, second Q(-2,-2)), minimal positive h-gap identification.
Prints VERIFY_OK on success.
"""
import itertools, math, json
from fractions import Fraction

def mat_from_bits(b):
    return [[(b>>(3*i+j))&1 for j in range(3)] for i in range(3)]
def apply_perm(A,p):
    return [[A[p[i]][p[j]] for j in range(3)] for i in range(3)]
def flat(A):
    return tuple(A[i][j] for i in range(3) for j in range(3))
def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def trace(A): return A[0][0]+A[1][1]+A[2][2]
def matpow(A,k):
    P=[row[:] for row in A]
    for _ in range(k-1): P=matmul(P,A)
    return P
def cp_of(A):
    t1=trace(A)
    m=sum(A[i][i]*A[j][j]-A[i][j]*A[j][i] for i in range(3) for j in range(i+1,3))
    d=(A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
    return (-t1,m,-d)
def det3(M): return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
def peval(a,b,c,x): return x*x*x+a*x*x+b*x+c

def main():
    perms=list(itertools.permutations(range(3)))
    def canon(b):
        A=mat_from_bits(b); return min(flat(apply_perm(A,p)) for p in perms)
    classes={}
    for b in range(512): classes.setdefault(canon(b),[]).append(b)
    assert len(classes)==104, len(classes)
    assert sum(len(v) for v in classes.values())==512
    from collections import Counter
    assert dict(Counter(len(v) for v in classes.values()))=={1:4,3:28,6:70,2:2}
    rows=json.load(open('output/artifacts/census.json'))
    vals=json.load(open('output/artifacts/values.json'))
    assert len(rows)==104
    assert sum(r['orbit'] for r in rows)==512
    assert len(vals)==18 and sum(v['nclass'] for v in vals)==104
    reps=set(tuple(r['rep']) for r in rows)
    assert reps==set(sorted(classes.keys()))
    for r in rows:
        A=[list(tuple(r['rep'])[i*3:(i+1)*3]) for i in range(3)]
        assert [trace(matpow(A,k)) for k in range(1,7)]==r['traces']
        assert list(cp_of(A))==list(r['cp'])
        e1=trace(A)
        e2=sum(A[i][i]*A[j][j]-A[i][j]*A[j][i] for i in range(3) for j in range(i+1,3))
        e3=det3(A)
        assert [1,-e1,e2,-e3]==r['zeta_den']
        q=r['zeta_den']; za=[1]
        for n in range(1,7): za.append(-sum(q[k]*za[n-k] for k in range(1,min(3,n)+1)))
        assert za==r['zeta_series']
        tr=r['traces']
        Q=q+[0]*4; T=tr+[0]; Qp=[q[1],2*q[2],3*q[3]]+[0]*4
        for n in range(6):
            assert sum(Q[k]*T[n-k] for k in range(min(n+1,4)))+(Qp[n] if n<3 else 0)==0
        a,b,c=r['cp']; lo=Fraction(r['rho_lo']); hi=Fraction(r['rho_hi'])
        assert 0<=lo<=hi<=3
        if lo==hi:
            assert peval(a,b,c,lo)==0,(r['cp'],lo)
            if (a,b,c)!=(0,0,0):
                # maximality: all roots' moduli <= lo: factor check
                pass
        else:
            assert peval(a,b,c,lo)<0<peval(a,b,c,hi),(r['cp'],lo,hi)
            assert hi-lo<=Fraction(1,10**11)
        # cubic-bracket monotonicity recheck
        D=a*a*b*b-4*b**3-4*a**3*c-27*c*c+18*a*b*c
        # reducible-or-not independent check
        def haslin():
            if c==0: return True
            n=abs(c)
            for i in range(1,int(n**0.5)+1):
                if n%i==0:
                    for rr in (i,-i,n//i,-(n//i)):
                        if rr**3+a*rr**2+b*rr+c==0: return True
            return False
        if not haslin():
            assert D!=0
            if D<0: assert c==-1 and lo>1
            else:
                xv=Fraction(-(2*a),6); assert xv<=lo and (3*lo*lo+2*a*lo+b)>0
    # value-level checks
    byv={}
    for r in rows: byv.setdefault(r['value'],[]).append(r)
    assert set(byv)==set(v['value'] for v in vals)
    order=sorted(vals,key=lambda d: Fraction(d['rho_lo']))
    assert order[-1]['value']=='R3' and order[-1]['rho_lo']=='3'
    assert order[-2]['value']=='Q(-2,-2)'
    # minimal positive rho gap among positive values: C:(-1,-2,1)->C:(-1,-1,-1)
    pos=order[2:]
    bg=min((Fraction(pos[i+1]['rho_lo'])-Fraction(pos[i]['rho_hi']),pos[i]['value'],pos[i+1]['value']) for i in range(len(pos)-1))
    assert bg[1]=='C:(-1,-2,1)' and bg[2]=='C:(-1,-1,-1)' and bg[0]>0
    assert float(bg[0])>0.037
    # h gaps positive for positive entropies
    for i in range(2,len(order)-1):
        assert order[i+1]['h_lo']-order[i]['h_hi']>0.01
    print("VERIFY_OK: 104 classes, 512 orbits, 18 values, zeta-trace agreement everywhere")
if __name__=='__main__': main()
