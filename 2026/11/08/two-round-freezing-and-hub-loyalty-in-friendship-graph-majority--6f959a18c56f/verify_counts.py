"""Independent combinatorial checker for the friendship majority census.

No dynamics simulator is imported. Counts all labelled blade-type orbits
with weights 2**mixed, for each possible initial hub opinion.
"""
from math import comb, factorial, sqrt, pi


def closed(k):
    N = 2*4**k
    R = sum(comb(k,u)*3**(k-u) for u in range((k+1)//2,k+1))
    if k%2==0:
        R -= comb(k,k//2)
    reversal=2*R
    t2=4**k-comb(2*k,k)-reversal
    t0=2*sum(comb(k,u) for u in range(k//2+1))
    return N,t0,N-t0-t2,t2,reversal,2*(3**k+1)


def blade_count(k):
    # Hub 0; u blades 11, m blades mixed, d blades 00.
    t0=t1=t2=reversal=consensus=0
    for u in range(k+1):
        for m in range(k-u+1):
            d=k-u-m
            weight=comb(k,u)*comb(k-u,m)*2**m
            initial_ones=2*u+m
            next_hub=int(initial_ones>k)
            final_hub=int(2*u>k) if 2*u!=k else next_hub
            # Peripheral blades are uniform from update 1 onward.
            if m==0 and next_hub==0:
                t0+=weight
            elif next_hub==final_hub:
                t1+=weight
            else:
                t2+=weight
            if final_hub:
                reversal+=weight
            if (u==0 and final_hub==0) or (d==0 and m==0 and final_hub==1):
                consensus+=weight
    # Complement symmetry exchanges the two initial hub colours.
    return 2*4**k,2*t0,2*t1,2*t2,2*reversal,2*consensus


if __name__=='__main__':
    for k in range(1,101):
        a=closed(k)
        b=blade_count(k)
        assert a==b, (k,a,b)
        assert sum(a[1:4])==a[0]
        if k in (1,2,3,4,5,6,8,10,20,50,100):
            print(f'k={k:3d}: N={a[0]} fixed={a[1]} entry1={a[2]} entry2={a[3]} hub_reversal={a[4]} consensus={a[5]}')
    # Numerical asymptotic cross-checks, not a proof of a limit.
    for k in (100,101,200,201):
        N,_,_,t2,R,_=closed(k)
        p=R/N
        base=(sqrt(3)/2)**k
        parity_factor = 1.5 if k%2==0 else sqrt(3)/2
        estimated=parity_factor * sqrt(2/(pi*k))*base
        print(f'asymptotic k={k}: actual={p:.12g} leading={estimated:.12g} ratio={p/estimated:.9f}, entry2_p={t2/N:.9f}')
    print('ORBIT_COUNT_OK')
