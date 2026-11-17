"""Exact-rational interface-chain and arm-balance checks, independent of full CTMC."""
from fractions import Fraction
from itertools import combinations

def solve(A, b):
    n=len(b)
    for c in range(n):
        pivot=next(i for i in range(c,n) if A[i][c])
        if pivot!=c:A[c],A[pivot]=A[pivot],A[c];b[c],b[pivot]=b[pivot],b[c]
        d=A[c][c];A[c]=[x/d for x in A[c]];b[c]/=d
        for j in range(n):
            if j==c:continue
            a=A[j][c]
            if a:
                A[j]=[v-a*w for v,w in zip(A[j],A[c])]
                b[j]-=a*b[c]
    return b

def arm_survival(r,k):
    # j=0,...,r-1 infected-prefix interface states; all-r absorbs successfully.
    M=[[Fraction(0) for _ in range(r)] for _ in range(r)]; y=[Fraction(0)]*r
    for j in range(r):
        if j==0:
            out=Fraction(1 if r==1 else 1,1 if r==1 else 2)
            kill=Fraction(1,k)
            M[j][j]+=out+kill
            if r==1:y[j]+=out
            else: M[j][j+1]-=out
        else:
            down=Fraction(1,2);up=Fraction(1 if j==r-1 else 1,1 if j==r-1 else 2)
            M[j][j]+=down+up
            M[j][j-1]-=down
            if j==r-1:y[j]+=up
            else:M[j][j+1]-=up
    return solve(M,y)[0]

def compositions(N,k):
    if k==1:yield (N,)
    else:
        for breaks in combinations(range(1,N),k-1):
            cuts=(0,)+breaks+(N,)
            yield tuple(cuts[i+1]-cuts[i] for i in range(k))

def p(arms):
    k=len(arms)
    ans=Fraction(1)
    for r in arms:ans*=Fraction(k,k+2*r-1)
    return ans

def main():
    arm_checks=0
    for r in range(1,13):
        for k in range(1,10):
            x=arm_survival(r,k)
            assert x==Fraction(k,k+2*r-1),(r,k,x)
            arm_checks+=1
    extremal_checks=0
    for k in range(2,7):
        for L in range(k,min(k+8,15)):
            vals=[(p(arms),arms) for arms in compositions(L,k)]
            q,t=divmod(L,k)
            balanced=(q,)*(k-t)+(q+1,)*t
            extreme=(1,)*(k-1)+(L-k+1,)
            assert min(v for v,_ in vals)==p(balanced)
            assert max(v for v,_ in vals)==p(extreme)
            extremal_checks+=1
    print('PASS:',arm_checks,'independent exact-rational interface-chain cases')
    print('PASS:',extremal_checks,'all-positive-composition extremal parameter cases')
    for arms in [(2,2,2), (1,1,4), (2,3,5), (1,2,3,4)]:
        print('Exact spider persistence:',arms,p(arms))
if __name__=='__main__':main()
