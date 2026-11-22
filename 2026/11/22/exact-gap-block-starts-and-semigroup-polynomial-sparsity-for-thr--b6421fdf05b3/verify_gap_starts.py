"""Reproduce the exact gap-start and semigroup-polynomial sparsity theorem.

No third-party packages are required. Independent membership uses unbounded-coin
reachability rather than the Apéry formulas in the proof.
"""

def predicted_starts(n):
    a=n*n
    starts=[]
    for u in range(n):
        jumps=[(u//2+1,(u+1)//2)]
        j2=(n+u)//2+1
        if j2<n:
            jumps.append((j2, u-j2+n+2))
        for j,q0 in jumps:
            starts += [(q0+t)*a+u*n+j for t in range(n)]
    assert len(starts)==len(set(starts))==2*n*(n-1)
    return sorted(starts)

def verify(n):
    a,b,c=n*n,n*(n+1),(n+1)**2
    frob=2*n**3-2*n-1
    member=bytearray(frob+2)
    member[0]=1
    for s in range(frob+2):
        if member[s]:
            for step in (a,b,c):
                if s+step<=frob+1:
                    member[s+step]=1
    starts=[s for s in range(1,frob+2) if not member[s] and member[s-1]]
    assert predicted_starts(n)==starts,(n,'start mismatch')
    assert sum(1-v for v in member)==n**3-n,(n,'genus mismatch')
    assert not member[frob] and member[frob+1],(n,'Frobenius mismatch')
    assert all(member[i] for i in range(frob+1-a+1,frob+2) if i>frob), (n,'conductor')
    coefficients=[member[s]-(member[s-1] if s else 0) for s in range(frob+2)]
    negative=[s for s,c in enumerate(coefficients) if c==-1]
    assert negative==starts,(n,'negative coefficient mismatch')
    assert coefficients[0]==1 and coefficients[-1]==1
    assert sum(c!=0 for c in coefficients)==4*n*(n-1)+1,(n,'coefficient count mismatch')
    assert starts[0]==1,(n,'initial gap mismatch')
    return len(member),len(starts)

if __name__=='__main__':
    total=0
    for n in range(2,81):
        positions, runs=verify(n)
        total += positions
        if n in (2,3,8,80):
            print(f'n={n} gaps={n**3-n} gap_blocks={runs} frobenius={2*n**3-2*n-1} nonzero_coefficients={4*n*(n-1)+1}')
    print(f'VERIFY_OK cases=79 checked_positions={total} n_range=2..80')
