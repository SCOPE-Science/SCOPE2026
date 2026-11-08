"""Exact rational checks for two-barrier biased walks with reset-neutral restarting.

Run with Python 3.10+: python reset_neutral_checker.py
No external packages or data files are required.
"""
from fractions import Fraction as Q

checks = 0


def check(statement, context=''):
    global checks
    checks += 1
    if not statement:
        raise AssertionError(context or f'check {checks}')


def linear_solve(A, b):
    """Independent exact Gauss-Jordan solution of a rational linear system."""
    n = len(b)
    M = [list(A[i]) + [b[i]] for i in range(n)]
    for k in range(n):
        pivot = next((j for j in range(k, n) if M[j][k]), None)
        if pivot is None:
            raise ValueError('singular system')
        M[k], M[pivot] = M[pivot], M[k]
        d = M[k][k]
        M[k] = [v / d for v in M[k]]
        for i in range(n):
            if i != k and M[i][k]:
                c = M[i][k]
                M[i] = [M[i][j] - c*M[k][j] for j in range(n+1)]
    return [M[i][-1] for i in range(n)]


def free_hit_transform(a, p, v, left_only=False):
    """E_z[v^tau] or E_z[v^tau 1_{X_tau=0}] without resetting."""
    q = 1 - p
    A = [[Q(int(i == j)) for j in range(a-1)] for i in range(a-1)]
    b = [Q(0)]*(a-1)
    for i in range(a-1):
        if i == 0:
            b[i] += v*q
        else:
            A[i][i-1] -= v*q
        if i == a-2:
            if not left_only:
                b[i] += v*p
        else:
            A[i][i+1] -= v*p
    return linear_solve(A, b)


def neutral_pair(a, p, x):
    """Correct reflected-pair weights, including odd intervals with rational sqrt(q/p)."""
    assert 1 <= x <= a//2
    out = [Q(0)]*(a-1)
    if 2*x == a:
        out[x-1] = Q(1)
        return out
    r = (1-p)/p
    if a%2 == 0:
        w = r**(a//2-x)
    else:
        h = {Q(1,5):Q(2), Q(1,2):Q(1), Q(4,5):Q(1,2)}[p]
        w = h**(a-2*x)
    out[x-1] = w/(1+w)
    out[a-x-1] = Q(1)/(1+w)
    return out


def dot(u, v):
    return sum((x*y for x,y in zip(u,v)),Q(0))


def restarted_chain(a,p,gamma,pi,z,kind='pgf'):
    """Direct absorbing-chain linear solve, independent of renewal formulas."""
    q=1-p
    A=[[Q(int(i==j))-z*gamma*pi[j] for j in range(a-1)] for i in range(a-1)]
    b=[Q(0)]*(a-1)
    for i in range(a-1):
        if i==0:
            if kind == 'pgf': b[i]+=z*(1-gamma)*q
            if kind == 'ruin': b[i]+=(1-gamma)*q
        else: A[i][i-1]-=z*(1-gamma)*q
        if i==a-2:
            if kind == 'pgf': b[i]+=z*(1-gamma)*p
        else: A[i][i+1]-=z*(1-gamma)*p
        if kind == 'mean':b[i]+=Q(1)
    return dot(pi,linear_solve(A,b))


def check_case(a,p,gamma):
    r=(1-p)/p
    if a%2 == 0:
        c=r**(a//2)/(1+r**(a//2))
    else:
        h={Q(1,5):Q(2), Q(1,2):Q(1), Q(4,5):Q(1,2)}[p]
        c=h**a/(1+h**a)
    v=1-gamma
    free=free_hit_transform(a,p,v)
    ufree=free_hit_transform(a,p,v,left_only=True)
    S=[];means=[]
    for x in range(1,a//2+1):
        pi=neutral_pair(a,p,x)
        check(sum(pi)==1, 'bad reset weights')
        s=dot(pi,free)
        S.append(s)
        check(Q(0)<s<Q(1), 'bad free hitting transform')
        check(restarted_chain(a,p,gamma,pi,Q(1),'ruin')==c,
              f'ruin neutrality failed: {a,p,gamma,x}')
        check(dot(pi,ufree)==c*s, 'discounted channel ratio failed')
        predicted_mean=(1-s)/(gamma*s)
        means.append(predicted_mean)
        check(restarted_chain(a,p,gamma,pi,Q(1),'mean')==predicted_mean,
              f'mean mismatch: {a,p,gamma,x}')
        for z in [Q(1,4),Q(1,2),Q(3,4)]:
            sz=dot(pi,free_hit_transform(a,p,(1-gamma)*z))
            F=(1-(1-gamma)*z)*sz/(1-z+gamma*z*sz)
            check(restarted_chain(a,p,gamma,pi,z)==F,
                  f'pgf mismatch: {a,p,gamma,x,z}')
    for j in range(len(S)-1):
        check(S[j]>S[j+1], 'discounted hitting times not strictly ordered')
        check(means[j]<means[j+1], 'restarted means not strictly ordered')
        for z in [Q(1,4),Q(1,2),Q(3,4)]:
            ss=free_hit_transform(a,p,(1-gamma)*z)
            pi1=neutral_pair(a,p,j+1)
            pi2=neutral_pair(a,p,j+2)
            v1=dot(pi1,ss);v2=dot(pi2,ss)
            f1=(1-(1-gamma)*z)*v1/(1-z+gamma*z*v1)
            f2=(1-(1-gamma)*z)*v2/(1-z+gamma*z*v2)
            check(f1>f2,'Laplace order failed')


for a in [4,6,8,10]:
    for p in [Q(1,3),Q(1,2),Q(2,3)]:
        for gamma in [Q(1,5),Q(1,2),Q(3,4)]:
            check_case(a,p,gamma)
for a in [5,7,9]:
    for p in [Q(1,5),Q(1,2),Q(4,5)]:
        for gamma in [Q(1,5),Q(1,2),Q(3,4)]:
            check_case(a,p,gamma)

# One fully explicit independent test: 6 sites, unbiased, gamma=1/3.
a=6;p=Q(1,2);gamma=Q(1,3)
s=free_hit_transform(a,p,1-gamma)
check(dot(neutral_pair(a,p,1),s)==Q(7,18))
check(dot(neutral_pair(a,p,2),s)==Q(1,6))
check(dot(neutral_pair(a,p,3),s)==Q(1,9))
check(restarted_chain(a,p,gamma,neutral_pair(a,p,1),Q(1),'mean')==Q(33,7))
check(restarted_chain(a,p,gamma,neutral_pair(a,p,2),Q(1),'mean')==Q(15))
check(restarted_chain(a,p,gamma,neutral_pair(a,p,3),Q(1),'mean')==Q(24))

print(f'PASS: {checks} exact rational assertions (full absorbing chains, pgfs, exit laws, ordering).')
