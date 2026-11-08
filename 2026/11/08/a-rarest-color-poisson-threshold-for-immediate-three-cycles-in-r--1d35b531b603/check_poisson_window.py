"""Seeded independent sparse-graph simulation of the Poisson critical window.
Run with: python check_poisson_window.py
No nonstandard dependencies.
"""
import math, random

def trial(n,pi,t,rng):
    m=min(pi)
    p=(math.log(n)+t)/(m*n)
    c=rng.choices((0,1,2),weights=pi,k=n)
    nbr=[[] for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if rng.random()<p:
                nbr[i].append(j);nbr[j].append(i)
    bad=sum(not any(c[u]==(c[v]+1)%3 for u in nbr[v]) for v in range(n))
    if bad==0:
        def step(z):
            return [int(any(z[u]==1 for u in nbr[v])) if z[v]==0 else (z[v]+1)%3 for v in range(n)]
        z1=step(c);z2=step(z1);z3=step(z2)
        assert z3==c and z1!=c
    return bad

if __name__=='__main__':
    for pi,seed in (((1/3,1/3,1/3),7182),((1/2,1/3,1/6),9238)):
        n=300;count=500;rng=random.Random(seed)
        bs=[trial(n,pi,0.0,rng) for _ in range(count)]
        m=min(pi)
        lam=sum(pi[i] for i in range(3) if abs(pi[(i+1)%3]-m)<1e-12)
        mean=sum(bs)/count
        zero=sum(b==0 for b in bs)/count
        print(f'pi={pi} n={n} trials={count} predicted_mean={lam:.6f} observed_mean={mean:.6f} predicted_zero={math.exp(-lam):.6f} observed_zero={zero:.6f}')
        assert abs(mean-lam)<0.24 and abs(zero-math.exp(-lam))<0.13
    print('PASS seeded critical-window and direct-cycle checks')
