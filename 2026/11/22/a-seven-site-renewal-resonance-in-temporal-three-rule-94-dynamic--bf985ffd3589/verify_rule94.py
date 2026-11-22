#!/usr/bin/env python3
"""Exact transfer-graph determinant and all-size coefficient certificate for ECA 94.

Requires Python 3 standard library only. All matrix coefficients are integers.
"""

RULE = 94

def bit(word, i):
    return (word >> i) & 1

def local(l, c, r):
    return (RULE >> (4*l+2*c+r)) & 1

def graph(period):
    # State (u,v) represents two adjacent complete temporal columns.
    size = 1 << period
    out = [[] for _ in range(size*size)]
    for u in range(size):
        for v in range(size):
            for w in range(size):
                if all(bit(v, (t+1) % period) == local(bit(u,t),bit(v,t),bit(w,t))
                       for t in range(period)):
                    out[u*size+v].append(v*size+w)
    return out

def traces(graph, upto):
    """Trace of powers computed by walking each starting vertex."""
    N = len(graph)
    output = [0] * (upto+1)
    for root in range(N):
        counts = [0]*N
        counts[root] = 1
        for k in range(1,upto+1):
            nxt = [0]*N
            for u, val in enumerate(counts):
                if val:
                    for v in graph[u]:
                        nxt[v] += val
            counts = nxt
            output[k] += counts[root]
    return output

def determinant_coefficients(graph):
    """Newton identities: det(I-zA) exactly, through its matrix dimension."""
    N = len(graph)
    t = traces(graph, N)
    d = [1]
    for k in range(1,N+1):
        s = sum(d[k-j]*t[j] for j in range(1,k+1))
        assert s % k == 0
        d.append(-s//k)
    return d, t

def coefficients_from_determinant(d, maxn):
    t=[0]*(maxn+1)
    for n in range(1,maxn+1):
        t[n] = -n*(d[n] if n<len(d) else 0)-sum(
            d[j]*t[n-j] for j in range(1, min(n,len(d)-1)+1))
    return t

def main():
    expected = {
        1: {0:1,1:-1,2:-1,4:1},
        3: {0:1,1:-1,2:-1,4:1,7:-3,8:3},
    }
    det={}
    for p in (1,3):
        G = graph(p)
        d, trace = determinant_coefficients(G)
        wanted = [expected[p].get(i,0) for i in range(len(d))]
        assert d == wanted, (p, d)
        print('period',p,'states',len(G),'edges',sum(len(a) for a in G),
              'nonzero det coeffs',[(i,x) for i,x in enumerate(d) if x])
        det[p]=d
    f1=coefficients_from_determinant(det[1],100)
    f3=coefficients_from_determinant(det[3],100)
    cycle={n:(f3[n]-f1[n])//3 for n in range(1,101)}
    for n in cycle:
        assert (f3[n]-f1[n])%3==0 and cycle[n]>=0
        assert (cycle[n]>0)==(n==7 or n>=9)
    print('primitive 3-orbit counts n=3..20:',[(n,cycle[n]) for n in range(3,21)])
    print('all 100 support checks passed; polynomial identity is finite all-size certificate')

if __name__=='__main__': main()
