from fractions import Fraction
from itertools import permutations
from math import factorial

def rho_of(p):
    n=len(p)
    d2=sum((i+1-p[i])**2 for i in range(n))
    return Fraction(1,1)-Fraction(6*d2, n*(n*n-1))

def check(max_n=9):
    perms_checked=0
    local_checks=0
    global_checks=0
    projection_checks=0
    for n in range(2,max_n+1):
        count=factorial(n)
        sumF=0
        sumF2=0
        sumR=Fraction(0)
        sumR2=Fraction(0)
        sumFR=Fraction(0)
        fixed_count=[0]*n
        fixed_rho=[Fraction(0) for _ in range(n)]
        for p in permutations(range(1,n+1)):
            perms_checked+=1
            r=rho_of(p)
            inds=[int(p[i]==i+1) for i in range(n)]
            F=sum(inds)
            sumF+=F
            sumF2+=F*F
            sumR+=r
            sumR2+=r*r
            sumFR+=F*r
            for i,z in enumerate(inds):
                if z:
                    fixed_count[i]+=1
                    fixed_rho[i]+=r
        EF=Fraction(sumF,count)
        VF=Fraction(sumF2,count)-EF*EF
        ER=sumR/count
        VR=sumR2/count-ER*ER
        CFR=sumFR/count-EF*ER
        assert EF==1
        assert VF==1
        assert ER==0
        assert VR==Fraction(1,n-1)
        assert CFR==Fraction(1,n-1)
        global_checks+=5
        for i in range(1,n+1):
            assert fixed_count[i-1]==factorial(n-1)
            cond=fixed_rho[i-1]/fixed_count[i-1]
            target=Fraction(3*(2*i-n-1)**2,(n-1)**2*(n+1))
            assert cond==target
            cov=Fraction(fixed_rho[i-1],count) # E[I_i rho], since E rho=0
            assert cov==Fraction(3*(2*i-n-1)**2,n*(n-1)**2*(n+1))
            local_checks+=2
        # Projection residual F-1-rho is orthogonal to rho.
        cov_res=(sumFR/count)-ER - (sumR2/count) - (EF-1-ER)*ER
        assert cov_res==0
        projection_checks+=1
    print('VERIFY_OK')
    print(f'permutations_checked={perms_checked}')
    print(f'local_checks={local_checks}')
    print(f'global_checks={global_checks}')
    print(f'projection_checks={projection_checks}')

if __name__=='__main__':
    check()
