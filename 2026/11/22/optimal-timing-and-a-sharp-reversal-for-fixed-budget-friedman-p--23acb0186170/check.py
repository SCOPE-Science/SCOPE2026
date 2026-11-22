#!/usr/bin/env python3
"""Exact finite sanity checks for open-loop mixed two-colour urn ordering."""
from fractions import Fraction as Q
from itertools import product

ASSERTIONS = 0

def check(a, b):
    global ASSERTIONS
    ASSERTIONS += 1
    if a != b:
        raise AssertionError(f'{a!r} != {b!r}')


def brute(initial_u, initial_v, a, b, schedule):
    states = {(initial_u, initial_v): Q(1)}
    c = a + b
    for op in schedule:
        out = {}
        for (u,v), w in states.items():
            if op == 'P':
                red, blue = (u+c,v),(u,v+c)
            else:
                red, blue = (u+a,v+b),(u+b,v+a)
            for pair, weight in [(red,w*Q(u,u+v)),(blue,w*Q(v,u+v))]:
                out[pair] = out.get(pair, Q(0)) + weight
        states=out
    check(sum(states.values()), Q(1))
    return sum(w*(u-v)**2 for (u,v), w in states.items())


def recurrence(initial_u, initial_v, a,b,ops):
    T = initial_u+initial_v
    V = Q((initial_u-initial_v)**2)
    for op in ops:
        alpha=(a+b) if op=='P' else (a-b)
        V=(1+Q(2*alpha,T))*V + alpha*alpha
        T+=a+b
    return V


def swap(initial_u,initial_v,a,b,prefix,suffix):
    c=a+b; d=a-b; T=initial_u+initial_v+c*len(prefix)
    v=recurrence(initial_u,initial_v,a,b,prefix)
    vpf=recurrence(initial_u,initial_v,a,b,prefix+'PF'+suffix)
    vfp=recurrence(initial_u,initial_v,a,b,prefix+'FP'+suffix)
    delta=Q(2*(c-d),T+c)*(Q(c,T)*v+c*d)
    for t,op in enumerate(suffix):
        alpha=c if op=='P' else d
        delta *= 1+Q(2*alpha,T+2*c+t*c)
    check(vpf-vfp, delta)


def run():
    for a,b in [(2,1),(3,1),(5,2),(1,2),(1,3),(2,2)]:
        for u,v in [(1,1),(2,1),(5,5),(9,1),(1,9)]:
            for n in range(6):
                for seq in product('PF', repeat=n):
                    ops=''.join(seq)
                    check(recurrence(u,v,a,b,ops),brute(u,v,a,b,ops))
                    if a>b:
                        k=ops.count('F')
                        small=recurrence(u,v,a,b,'F'*k+'P'*(n-k))
                        large=recurrence(u,v,a,b,'P'*(n-k)+'F'*k)
                        cur=recurrence(u,v,a,b,ops)
                        check(small<=cur<=large,True)
                        if k and k<n:
                            check(small == cur, ops=='F'*k+'P'*(n-k))
                            check(large == cur, ops=='P'*(n-k)+'F'*k)
                    # Ordinary Pólya tail risk identity: the stopped-at-time-n risk
                    # coefficient must remain invariant under an extra P step.
                    T=u+v+n*(a+b)
                    m=recurrence(u,v,a,b,ops)
                    risk=Q(m+(a+b)*T, 4*T*(T+a+b))
                    future=recurrence(u,v,a,b,ops+'P')
                    T1=T+a+b
                    check(risk,Q(future+(a+b)*T1,4*T1*(T1+a+b)))
    for a,b in [(2,1),(5,2),(1,3),(1,2),(2,2)]:
        for u,v in [(1,1),(5,5),(9,1),(2,3)]:
            for n in range(5):
                for prefix_tpl in product('PF',repeat=n):
                    prefix=''.join(prefix_tpl)
                    for j in range(3):
                        for suffix_tpl in product('PF',repeat=j):
                            swap(u,v,a,b,prefix,''.join(suffix_tpl))
    # The anti-reinforcement boundary is genuinely state-dependent.
    check(recurrence(5,5,1,3,'PF') < recurrence(5,5,1,3,'FP'),True)
    check(recurrence(9,1,1,3,'PF') > recurrence(9,1,1,3,'FP'),True)
    print(f'{ASSERTIONS} exact-rational assertions passed')

if __name__=='__main__':run()
