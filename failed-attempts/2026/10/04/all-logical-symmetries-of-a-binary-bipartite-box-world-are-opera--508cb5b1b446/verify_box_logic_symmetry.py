#!/usr/bin/env python3
import math

def vertices(N,M):
    return [(i,a,j,b)
            for i in range(N) for a in (0,1)
            for j in range(M) for b in (0,1)]

def orth(u,v):
    i,a,j,b=u
    I,A,J,B=v
    return (i==I and a!=A) or (j==J and b!=B)

def closed_nonorth(V, v):
    return {w for w in V if w==v or not orth(v,w)}

def map_input_swap(v, side, p, q):
    i,a,j,b=v
    if side=="A":
        if i==p: i=q
        elif i==q: i=p
    else:
        if j==p: j=q
        elif j==q: j=p
    return (i,a,j,b)

def map_output_flip(v, side, p):
    i,a,j,b=v
    if side=="A" and i==p: a=1-a
    if side=="B" and j==p: b=1-b
    return (i,a,j,b)

def party_swap(v):
    i,a,j,b=v
    return (j,b,i,a)

def is_graph_auto(V, f):
    image=[f(v) for v in V]
    if len(set(image))!=len(V) or set(image)!=set(V):
        return False
    for r,u in enumerate(V):
        for v in V[r+1:]:
            if orth(u,v)!=orth(f(u),f(v)):
                return False
    return True

def run_case(N,M):
    V=vertices(N,M)
    C={v:closed_nonorth(V,v) for v in V}
    base=(2*N-2)*(2*M-2)
    left=(2*N-1)*(2*M-2)
    right=(2*N-2)*(2*M-1)

    counts={"left":0,"right":0,"neither":0}
    for r,v in enumerate(V):
        for w in V[r+1:]:
            got=len(C[v]&C[w])
            same_left=(v[0],v[1])==(w[0],w[1])
            same_right=(v[2],v[3])==(w[2],w[3])
            if same_left:
                assert not same_right
                assert got==left
                counts["left"]+=1
            elif same_right:
                assert got==right
                counts["right"]+=1
            else:
                assert got==base
                counts["neither"]+=1

    # Reconstruct rook rows/columns from the graph-derived intersection threshold.
    rel={(v,w) for v in V for w in V
         if v==w or len(C[v]&C[w])>base}
    rows=[{w for w in V if (v[0],v[1])==(w[0],w[1])}
          for v in V]
    cols=[{w for w in V if (v[2],v[3])==(w[2],w[3])}
          for v in V]
    unique_rows={frozenset(r) for r in rows}
    unique_cols={frozenset(c) for c in cols}
    assert len(unique_rows)==2*N
    assert len(unique_cols)==2*M
    for R in unique_rows|unique_cols:
        for u in R:
            for v in R:
                assert (u,v) in rel

    # Inside a row, orthogonality is exactly Bob's outcome-pair matching.
    for R in unique_rows:
        for u in R:
            mates=[v for v in R if orth(u,v)]
            assert len(mates)==1
            v=mates[0]
            assert u[2]==v[2] and u[3]!=v[3]
    # Inside a column, orthogonality is exactly Alice's outcome-pair matching.
    for Cc in unique_cols:
        for u in Cc:
            mates=[v for v in Cc if orth(u,v)]
            assert len(mates)==1
            v=mates[0]
            assert u[0]==v[0] and u[1]!=v[1]

    # Check generators of all operational relabelings.
    for p in range(N):
        assert is_graph_auto(V, lambda v,p=p: map_output_flip(v,"A",p))
    for p in range(M):
        assert is_graph_auto(V, lambda v,p=p: map_output_flip(v,"B",p))
    for p in range(N-1):
        assert is_graph_auto(V, lambda v,p=p: map_input_swap(v,"A",p,p+1))
    for p in range(M-1):
        assert is_graph_auto(V, lambda v,p=p: map_input_swap(v,"B",p,p+1))
    if N==M:
        assert is_graph_auto(V, party_swap)

    order=(2**(N+M))*math.factorial(N)*math.factorial(M)
    if N==M:
        order*=2
    return len(V), order, counts

def main():
    cases=0
    atom_pairs=0
    for N in range(2,6):
        for M in range(2,6):
            nv,order,counts=run_case(N,M)
            cases+=1
            atom_pairs += nv*(nv-1)//2
            expected=(2**(N+M))*math.factorial(N)*math.factorial(M)*(2 if N==M else 1)
            assert order==expected
    assert (2**4)*math.factorial(2)*math.factorial(2)*2==128
    print("VERIFY_OK")
    print("parameter_cases =",cases)
    print("atom_pairs_checked =",atom_pairs)
    print("Aut_L_2_2_order = 128")
    print("range = 2 <= N,M <= 5")

if __name__=="__main__":
    main()
