"""Independent finite-volume checks for two-sink Hamming quantum networks.
Run: python check_hamming.py. Requires numpy and scipy.
The infinite-family formulas are proved analytically in RESULT.md.
"""
from itertools import product
from math import comb
import numpy as np
from scipy.linalg import eigh, expm


def adjacency(q, n):
    sites = list(product(range(q), repeat=n))
    a = np.zeros((len(sites), len(sites)))
    for i, x in enumerate(sites):
        for j in range(i):
            if sum(s != t for s, t in zip(x, sites[j])) == 1:
                a[i, j] = a[j, i] = 1.
    return sites, a


def kraw(q, n, k, d):
    return sum((-1)**j * (q-1)**(k-j) * comb(d,j) * comb(n-d,k-j)
               for j in range(max(0,k-n+d), min(k,d)+1))


def predicted(q, n, d):
    if q == 2 and d == n:
        return n + 1
    if q == 2:
        return 2*n
    return 2*n + 1


def local_bright(q, n, distances):
    a, b, d = distances
    total = 0.0
    Q = q**n
    for k in range(n+1):
        m = comb(n, k)*(q-1)**k
        z = kraw(q,n,k,d)
        f = kraw(q,n,k,a)
        g = kraw(q,n,k,b)
        if z*z == m*m:
            total += f*f/(Q*m)
        else:
            total += (m*(f*f+g*g)-2*z*f*g)/(Q*(m*m-z*z))
    return total


def check():
    comparisons = 0
    local_comparisons = 0
    for q,n in [(2,k) for k in range(1,7)] + [(3,k) for k in range(1,4)] + [(4,k) for k in range(1,3)]:
        sites, h = adjacency(q,n)
        vals, vecs = eigh(h)
        group = []
        for k in range(n+1):
            ev = n*(q-1)-q*k
            inds = np.where(np.abs(vals-ev)<1e-9)[0]
            assert len(inds)==comb(n,k)*(q-1)**k
            group.append(vecs[:,inds])
        for t in range(1,len(sites)):
            d = sum(v != 0 for v in sites[t])
            ranks = [np.linalg.matrix_rank(ee[[0,t],:],tol=1e-8) for ee in group]
            assert sum(ranks)==predicted(q,n,d), (q,n,d,ranks)
            comparisons += 1
            for x in range(len(sites)):
                da = sum(v!=0 for v in sites[x]); db = sum(u!=v for u,v in zip(sites[x],sites[t]))
                estimate = 0.0
                for ee in group:
                    # independently compute the orthogonal projector onto the evaluated eigenspace vectors
                    target_columns = ee @ ee[[0,t],:].conj().T
                    u, singular, _ = np.linalg.svd(target_columns, full_matrices=False)
                    rank = sum(singular>1e-8)
                    estimate += sum(abs(u[x,j])**2 for j in range(rank))
                formula = local_bright(q,n,(da,db,d))
                assert abs(estimate-formula)<5e-9, (q,n,t,x,estimate,formula)
                local_comparisons += 1
    # Direct no-jump evolution on small finite systems, independently of spectral projections.
    dynamical = 0
    for q,n,t,x in [(2,2,3,2),(2,3,7,2),(3,2,8,2),(3,2,4,3)]:
        sites,h = adjacency(q,n)
        d = sum(v!=0 for v in sites[t]); da=sum(v!=0 for v in sites[x]); db=sum(u!=v for u,v in zip(sites[x],sites[t]))
        g = np.zeros_like(h);g[0,0]=.8;g[t,t]=1.9
        heff = h - .5j*g
        b = local_bright(q,n,(da,db,d))
        for time in [200,500,1000]:
            state = expm(-1j*time*heff)[:,x]
            surv = np.vdot(state,state).real
            assert abs(surv-(1-b)) < 2e-5, (q,n,t,x,time,surv,1-b)
            dynamical+=1
    print('PASS rank comparisons:', comparisons)
    print('PASS local Krawtchouk source-survival comparisons:',local_comparisons)
    print('PASS finite no-jump dynamical comparisons:', dynamical)
    print('No finite check is a proof of the dimension-uniform formulas.')

if __name__ == '__main__':
    check()
