#!/usr/bin/env python3
"""Independent combinatorial verification of reachability, sector sizes, and escape flux."""
def count_part(state,n,k):
    return (state >> (k*n) & ((1<<n)-1)).bit_count()

def energy_cut(state,n):
    x,y,z=[count_part(state,n,k) for k in range(3)]
    return 2*n*(x+y+z)-2*(x*y+x*z+y*z)

def can_flip(state,n,k,i):
    bit=(state>>(k*n+i))&1
    s=sum(count_part(state,n,j) for j in range(3) if j!=k)
    # A current 0 flips if there are <= n ones outside;
    # a current 1 flips if there are >= n ones outside.
    return s<=n if bit==0 else s>=n

def show_construction(state,n):
    # Deliberately choose part 0's target as the minority of the other parts.
    s=count_part(state,n,1)+count_part(state,n,2)
    target0=0 if s>=n else 1
    for i in range(n):
        if ((state>>i)&1) != target0:
            assert can_flip(state,n,0,i)
            state ^=1<<i
    target1=1-target0
    for i in range(n):
        if ((state>>(n+i))&1) != target1:
            assert can_flip(state,n,1,i)
            state ^=1<<(n+i)
    assert energy_cut(state,n)==2*n*n
    return state

def sectors(state,n):
    c=[count_part(state,n,k) for k in range(3)]
    return {(i,j) for i in range(3) for j in range(3) if i!=j and c[i]==0 and c[j]==n}

def main():
    for n in range(1,7):
        best_count=0; B=[]
        for state in range(1<<(3*n)):
            show_construction(state,n)
            if energy_cut(state,n)==2*n*n:
                best_count+=1;B.append(state)
                assert len(sectors(state,n)) in (1,2)
        assert best_count==6*(2**n-1),(n,best_count)
        if n>=2:
            R=6*(2**n-1)
            # Sector A=0,B=1 (part 2 unrestricted)
            A={state for state in B if count_part(state,n,0)==0 and count_part(state,n,1)==n}
            assert len(A)==2**n
            exits=0
            for state in A:
                for v in range(3*n):
                    k,i=divmod(v,n)
                    if can_flip(state,n,k,i):
                        nextstate=state^(1<<v)
                        assert nextstate in B
                        if nextstate not in A: exits+=1
            assert exits==2*n,(n,exits)
            assert 4*len(A) <= R  # stationary sector mass <= 1/4
            print(n,best_count,len(A),exits,'flux=',f'2/(3*{R})')
        else:
            print(n,best_count,'small case')
    print('PASS: exhaustive constructive paths and conductance identities, n=1..6')
if __name__ == '__main__': main()
