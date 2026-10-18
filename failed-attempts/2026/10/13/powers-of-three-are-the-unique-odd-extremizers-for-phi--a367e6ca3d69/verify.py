#!/usr/bin/env python3

def totients_upto(N):
    phi=list(range(N+1))
    if N>=1:
        phi[1]=1
    for p in range(2,N+1):
        if phi[p]==p:
            for j in range(p,N+1,p):
                phi[j]-=phi[j]//p
    return phi

def is_power_of_three(n):
    while n>1 and n%3==0:
        n//=3
    return n==1

# Exact maximization for a finite sanity range, using the proved universal
# odd bound Phi(n) <= 6n to make the search interval exhaustive.
N_exact=1000
phi=totients_upto(6*N_exact)
exact_checked=0
for n in range(1,N_exact+1,2):
    best=0
    for m in range(1,6*n+1):
        if (2*n)%phi[m]==0:
            best=m
    expected=6*n if is_power_of_three(n) else None
    if (best==6*n) != is_power_of_three(n):
        raise AssertionError((n,best,expected))
    exact_checked+=1

# Larger check of the critical top candidate m=6n.
N_top=200000
phi2=totients_upto(6*N_top)
top_checked=0
for n in range(1,N_top+1,2):
    admissible=((2*n)%phi2[6*n]==0)
    if admissible != is_power_of_three(n):
        raise AssertionError((n,phi2[6*n],2*n))
    top_checked+=1

print(f"VERIFY_OK exact_odd_n={exact_checked} exact_n_max={N_exact} top_candidate_odd_n={top_checked} top_n_max={N_top}")
