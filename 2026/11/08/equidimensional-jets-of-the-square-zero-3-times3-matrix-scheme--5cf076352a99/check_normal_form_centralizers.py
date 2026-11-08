"""Independent small-ring centralizer checks for 3x3 square-zero matrix normal forms."""
from itertools import product

def matmult(a,b,mod):
    return tuple(sum(a[3*i+k]*b[3*k+j] for k in range(3))%mod for i in range(3) for j in range(3))

def invertible_mod2(a):
    z=[list(a[3*i:3*i+3]) for i in range(3)]
    rank=0
    for c in range(3):
        pivot=next((i for i in range(rank,3) if z[i][c]%2),None)
        if pivot is None:continue
        z[pivot],z[rank]=z[rank],z[pivot]
        for i in range(3):
            if i!=rank and z[i][c]%2:
                for j in range(c,3):z[i][j]^=z[rank][j]
        rank+=1
    return rank==3

# R = F_2[t]/(t^2) encoded as bits 0,1,t,1+t. Addition XOR; multiplication bitwise.
def mul(a,b):return (a&1)*(b&1) | (((a&1)*((b>>1)&1) ^ ((a>>1)&1)*(b&1))<<1)
def mm(a,b):return tuple(mul(a[3*i],b[j])^mul(a[3*i+1],b[3+j])^mul(a[3*i+2],b[6+j]) for i in range(3) for j in range(3))
for c in [0,2]:
    J=(0,1,0, 0,0,0, 0,0,c)
    total=0;units=0
    for entries in product(range(4),repeat=9):
        if mm(entries,J)==mm(J,entries):
            total+=1
            if invertible_mod2(tuple(x&1 for x in entries)):units+=1
    assert total==4**5, (c,total)
    assert units==2**5 * 2**3, (c,units)
    print(f'c={c} ring=F2[t]/t^2 centralizer_size={total} invertible_centralizer={units} orbit_size={168*2**9//units}')
print('ALL_3X3_SQUAREZERO_CENTRALIZER_CHECKS_PASS')
