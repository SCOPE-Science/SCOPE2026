"""Independent breadth-first exhaustive exact modular Waring checks."""

def covering_length(exponent, modulus):
    # Minimal number of elements from the k-th-power residue set required
    # to cover the whole cyclic group, computed by BFS from the residue zero.
    residues=sorted({pow(x,exponent,modulus) for x in range(modulus)})
    seen=bytearray(modulus)
    seen[0]=1
    frontier=[0]
    reached=1
    depth=0
    while reached<modulus:
        depth+=1
        following=[]
        for u in frontier:
            for z in residues:
                v=(u+z)%modulus
                if not seen[v]:
                    seen[v]=1
                    following.append(v)
                    reached+=1
        frontier=following
    return depth

count=0
for s,bound in ((1,180),(2,280)):
    k=2*3**s
    M=3**(s+1)
    for n in range(2,bound+1):
        v=covering_length(k,n)
        assert v<=M,(k,n,v,'upper')
        assert (v==M)==(n%(3**(s+2))==0),(k,n,v,'threshold')
        count+=1
    print('k',k,'moduli_checked',bound-1,'global_max',M,'threshold',3**(s+2))
print('COMPOSITE_PASS',count)
