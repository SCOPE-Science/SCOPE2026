#!/usr/bin/env python3
"""Independent finite-state dynamic program and polynomial certificate for all lengths."""

def count_avoid(n):
    # DFA state: longest suffix matching proper prefix of forbidden 010.
    transitions = ((1,0),(1,2),(-1,0))
    vec = [1,0,0]
    out = [1]
    for k in range(1,n+1):
        nxt = [0,0,0]
        for state,value in enumerate(vec):
            for target in transitions[state]:
                if target != -1:
                    nxt[target] += value
        vec=nxt;out.append(sum(vec))
    return out


def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):c[i+j]+=u*v
    return c


def main():
    N=100
    a=count_avoid(N)
    # Certify D(z) A(z)=1+z^2 through the coefficient N.
    D=[1,-2,1,-1]
    for n in range(N+1):
        s=sum(D[k]*a[n-k] for k in range(min(3,n)+1))
        assert s==(1 if n==0 or n==2 else 0),(n,s)
    # A valid edge is u01v, where u is empty, "1", or ends "11",
    # and v is empty, "1", or begins "11"; both avoid 010.
    left=[1,1]+a[:-2]
    assert len(left)==N+1
    formula=poly_mul(left,left)
    formula=[0,0]+formula
    # Check D(z)^2 E(z)=z^2 (1-z)^2 coefficientwise.
    DD=poly_mul(D,D)
    for n in range(N+1):
        s=sum(DD[k]*formula[n-k] for k in range(min(6,n)+1))
        tgt={2:1,3:-2,4:1}.get(n,0)
        assert s==tgt,(n,s,tgt)
    # Independently count locally admissible swaps from each DFA-generated word
    # for small n. This is not based on the deletion-ball implementation.
    def count_swaps(n):
        curr=['']
        for _ in range(n):
            curr=[v+c for v in curr for c in '01' if '010' not in (v+c)]
        edges=0
        for w in curr:
            for j in range(n-1):
                if w[j:j+2]!='01':continue
                v=w[:j]+'10'+w[j+2:]
                if '010' not in v:edges+=1
        return edges
    for n in range(2,18):
        assert count_swaps(n)==formula[n],(n,count_swaps(n),formula[n])
        print('transfer',n,a[n],formula[n])
    print('VERIFY_TRANSFER_OK')

if __name__=='__main__': main()
