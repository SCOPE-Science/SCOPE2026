"""Reproducible finite-state proof for shattering minimal dominating sets of paths.

Python 3, standard library only. No precomputed transition tables are trusted.
The checker reconstructs local membership, all reachable subset-family states,
all weighted transitions, and the five-step max-plus recurrence certificate.
"""
from collections import deque
from functools import lru_cache
from hashlib import sha256
import json

@lru_cache(None)
def edge(s, b, pad=0):
    """A single local verifier transition; -1 means impossible.

    State (p,h) stores min(3,number of ordinary bits read) and four
    trailing bits h, oldest first. The new 5-window checks its center.
    pad=1 is the first right padding zero, pad=2 the second.
    """
    p, h = divmod(s, 16)
    if p >= 2:
        v = [(h >> 3)&1, (h >> 2)&1, (h >> 1)&1, h&1, b]
        if v[2] == 0:
            if sum(v[1:4]) == 0:
                return -1
        else:
            first = p == 2
            last = pad == 2
            if not any(sum(v[j-1:j+2]) == 1 for j in (1,2,3)
                       if not(first and j == 1) and not(last and j == 3)):
                return -1
    return 16*min(3,p+1) + ((h << 1)&15) + b

@lru_cache(None)
def advance(Q, b, pad=0):
    ans=0
    while Q:
        lsb=Q&-Q
        s=lsb.bit_length()-1
        t=edge(s,b,pad)
        if t >= 0:
            ans |= 1 << t
        Q-=lsb
    return ans

@lru_cache(None)
def move(F, marked):
    output=set()
    for Q in F:
        left=advance(Q,0)
        right=advance(Q,1)
        if marked:
            output.add(left)
            output.add(right)
        else:
            output.add(left|right)
    if 0 in output:
        return None
    return tuple(sorted(output))

@lru_cache(None)
def state_accept(Q):
    return advance(advance(Q,0,1),0,2)!=0

def family_accept(F):
    return all(state_accept(Q) for Q in F)

def construct_graph():
    initial=(1,)
    states=[initial]
    indexes={initial:0}
    edges=[]
    for F in states:
        successors=[]
        for b in (0,1):
            G=move(F,b)
            if G is None:
                successors.append(-1)
            else:
                if G not in indexes:
                    indexes[G]=len(states)
                    states.append(G)
                successors.append(indexes[G])
        edges.append(tuple(successors))
    accept=[family_accept(F) for F in states]
    return states,edges,accept

def weight_vectors(edges, steps):
    W=[{0:0}]
    for n in range(steps):
        new={}
        for i,w in W[-1].items():
            for b,j in enumerate(edges[i]):
                if j >= 0:
                    new[j]=max(new.get(j,-10**12),w+b)
        W.append(new)
    return W

def count_polynomials(edges,accept,N):
    P={0:(1,)}
    allcounts=[]
    for n in range(N+1):
        sums=[0]*(n+1)
        for i,pol in P.items():
            if accept[i]:
                for k,c in enumerate(pol):sums[k]+=c
        allcounts.append(sums)
        if n==N:break
        nxt={}
        for i,pol in P.items():
            for b,j in enumerate(edges[i]):
                if j<0:continue
                r=nxt.setdefault(j,[0]*(n+2))
                for k,c in enumerate(pol):r[k+b]+=c
        P=nxt
    return allcounts

def direct_minimal_dom_masks(n):
    # Independent from the local automaton: domination and literal removal.
    neigh=[]
    for v in range(n):
        neigh.append(sum(1<<j for j in range(max(0,v-1),min(n,v+2))))
    def dominates(mask):
        return all(mask&nb for nb in neigh)
    return [mask for mask in range(1<<n)
            if dominates(mask) and all(not dominates(mask^(1<<v))
            for v in range(n) if (mask>>v)&1)]

def brute_faces(n):
    D=direct_minimal_dom_masks(n)
    ans=[0]*(n+1)
    for S in range(1<<n):
        k=S.bit_count()
        if (1<<k)>len(D):continue
        if len({d&S for d in D})==(1<<k):ans[k]+=1
    return ans

def main():
    states,edges,accept=construct_graph()
    fingerprint=sha256(json.dumps(edges,separators=(',',':')).encode()).hexdigest()
    assert len(states)==206, len(states)
    assert sum(accept)==140
    assert sum(j<0 for row in edges for j in row)==79
    assert fingerprint=='745e40a73b2b4c98aa3dee965bd42ffe216cefd75c1ccb361d3d905f7650bd1d'
    print('GRAPH',len(states),'accepting',sum(accept),'dead transitions',79)
    print('GRAPH_SHA256',fingerprint)
    W=weight_vectors(edges,25)
    for n in range(16,21):
        left,right=W[n],W[n+5]
        # An absent dictionary component represents minus infinity; check
        # the equality including those components at all 206 states.
        assert all((i not in left and i not in right) or
                   (i in left and i in right and right[i] == left[i]+2)
                   for i in range(len(states)))
    print('FIVE_STEP_PERIODIC_VECTORS',list(range(16,21)))
    print('FINITE_STATES_AT_LENGTH_16',len(W[16]),'OF',len(states))
    for n,w in enumerate(W[:21]):
        vc=max((v for i,v in w.items() if accept[i]),default=-1)
        expected=(2*n+2)//5
        assert vc==expected,(n,vc,expected)
    print('VC_BASE_0_TO_20',[max(v for i,v in w.items() if accept[i]) for w in W[:21]])
    polynomials=count_polynomials(edges,accept,13)
    for n in range(14):
        check=brute_faces(n)
        assert polynomials[n]==check,(n,polynomials[n],check)
    print('DIRECT_ENUMERATION_MATCHES_ALL_FACES_N_0_TO_13')
    print('FACE_POLYNOMIAL_N_11',polynomials[11])
    print('FACE_POLYNOMIAL_N_13',polynomials[13])
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
