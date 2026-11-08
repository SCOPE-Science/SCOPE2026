"""Finite exhaustive cross-check of the annealed Greenberg-Hastings period-three formula.
Run with: python check_exact_random_gh.py
"""
from fractions import Fraction
from itertools import product
from math import factorial

def direct(n, p_num, p_den, weights):
    E = [(i,j) for i in range(n) for j in range(i+1,n)]
    M = len(E)
    colorings = list(product(range(3), repeat=n))
    weighted_good = 0
    connected_period_mismatches = 0
    connected_cases = 0
    for edge_mask in range(1<<M):
        nbr=[[] for _ in range(n)]
        for k,(i,j) in enumerate(E):
            if edge_mask>>k&1:
                nbr[i].append(j); nbr[j].append(i)
        e=edge_mask.bit_count()
        gw=p_num**e * (p_den-p_num)**(M-e)
        # independently check 3-step dynamics versus all-site rotation on connected graphs
        reach={0}
        for _ in range(n):
            reach |= {u for v in list(reach) for u in nbr[v]}
        connected=len(reach)==n
        for c in colorings:
            rotates = all(any(c[u]==(c[v]+1)%3 for u in nbr[v]) for v in range(n))
            if connected:
                connected_cases+=1
                def update(z):
                    return tuple((1 if any(z[u]==1 for u in nbr[v]) else 0) if a==0 else (a+1)%3 for v,a in enumerate(z))
                f1=update(c)
                f3=update(update(f1))
                primitive3=(f3==c and f1!=c)
                if primitive3 != rotates:
                    connected_period_mismatches+=1
            if rotates:
                cw=1
                for v in c:cw*=weights[v]
                weighted_good+=gw*cw
    return Fraction(weighted_good, (p_den**M)*(sum(weights)**n)), connected_period_mismatches, connected_cases

def analytic(n,p_num,p_den,weights):
    p=Fraction(p_num,p_den); q=1-p
    prob=[Fraction(w,sum(weights)) for w in weights]
    out=Fraction(0)
    for a in range(n+1):
        for b in range(n-a+1):
            c=n-a-b; count=[a,b,c]
            w=Fraction(factorial(n),factorial(a)*factorial(b)*factorial(c))
            for j,k in enumerate(count): w*=prob[j]**k
            for j,k in enumerate(count):w*=(1-q**count[(j+1)%3])**k
            out+=w
    return out

if __name__=='__main__':
    for n in range(1,6):
        for p_num,p_den,weights in ((1,2,(1,1,1)),(1,3,(3,2,1))):
            a,err,ct=direct(n,p_num,p_den,weights)
            b=analytic(n,p_num,p_den,weights)
            print(f'n={n} p={p_num}/{p_den} weights={weights} exact={a} agreement={a==b} connected_cases={ct} connected_mismatches={err}')
            assert a==b and err==0
    print('PASS exact exhaustive graph/color/dynamics test')
