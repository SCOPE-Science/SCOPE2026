#!/usr/bin/env python3
import math, random

def local_constant(m,p):
    q=p/2.0
    return ((m-1)**q + (m-1)**(1-q))/(m**q)

def hermite_q(m,p,t):
    q=p/2.0
    r=1.0/(m*(m-1))
    M=(m-1)/m
    fr=r**q
    dfr=q*r**(q-1)
    a=(M**q-fr-dfr*(M-r))/((M-r)**2)
    return fr+dfr*(t-r)+a*(t-r)**2, a

def check():
    max_majorant=0.0
    majorant_checks=0
    for m in range(3,31):
        M=(m-1)/m
        for p in (4.01,4.1,4.5,5.0,6.0,7.25,10.0,20.0):
            for j in range(1001):
                t=M*j/1000.0
                Q,a=hermite_q(m,p,t)
                assert a>0
                err=t**(p/2.0)-Q
                max_majorant=max(max_majorant,err)
                assert err <= 2e-12
                majorant_checks+=1

    rng=random.Random(27052026)
    random_checks=0
    max_excess=-1e99
    for m in range(2,25):
        for p in (4.01,4.2,5.0,6.0,8.0,12.0):
            A=local_constant(m,p)
            for _ in range(120):
                z=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(m-1)]
                z.append(-sum(z))
                s2=sum(abs(w)**2 for w in z)
                if s2==0: continue
                lhs=sum(abs(w)**p for w in z)/(s2**(p/2.0))
                excess=lhs-A
                max_excess=max(max_excess,excess)
                assert excess <= 5e-12
                random_checks+=1

    equality_checks=0
    for m in range(2,50):
        for p in (4.01,4.5,5.0,6.0,9.5,16.0):
            big=math.sqrt((m-1)/m)
            small=-1.0/math.sqrt(m*(m-1))
            z=[big]+[small]*(m-1)
            assert abs(sum(z)) < 1e-12
            lhs=sum(abs(w)**p for w in z)
            A=local_constant(m,p)
            assert abs(lhs-A) < 5e-12
            equality_checks+=1

    specialization_checks=0
    for m in range(2,80):
        for k in range(1,9):
            p4=(k/m)*((m-1)**2+(m-1)**-1)
            ref4=k*(m*m-3*m+3)/(m-1)
            assert abs(p4-ref4)<1e-10
            p6=(k*k/m)*((m-1)**3+(m-1)**-2)
            ref6=k*k*(m**4-5*m**3+10*m**2-10*m+5)/(m-1)**2
            assert abs(p6-ref6)<1e-9
            specialization_checks+=2

    fourier_checks=0
    for m in range(2,11):
        for k in range(1,7):
            N=m*k
            K=set((t*m)%N for t in range(k))
            for p in (4.1,5.0,6.0,8.3):
                vals=[]
                for x in range(N):
                    s=0j
                    for j in range(N):
                        if j not in K:
                            s += complex(math.cos(2*math.pi*j*x/N),math.sin(2*math.pi*j*x/N))
                    vals.append(s)
                normp=(sum(abs(v)**p for v in vals)/N)**(1.0/p)
                coeff2=math.sqrt(N-k)
                kp_p=(k**(p/2.0-1)/m)*((m-1)**(p/2.0)+(m-1)**(1-p/2.0))
                predicted=(kp_p**(1.0/p))*coeff2
                assert abs(normp-predicted) <= 2e-10*max(1.0,predicted)
                fourier_checks+=1

    print('VERIFY_OK')
    print(f'hermite_majorant_checks={majorant_checks} max_signed_excess={max_majorant:.3e}')
    print(f'random_zero_sum_checks={random_checks} max_excess={max_excess:.3e}')
    print(f'equality_checks={equality_checks}')
    print(f'p4_p6_specialization_checks={specialization_checks}')
    print(f'cyclic_fourier_extremizer_checks={fourier_checks}')

if __name__=='__main__':
    check()
