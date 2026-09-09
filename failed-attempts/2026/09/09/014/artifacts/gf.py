"""GF(4) arithmetic: GF(2)[t]/(t^2+t+1). Elements 0..3; 0=0,1=1,2=t,3=t+1."""
ADD = [[0]*4 for _ in range(4)]
MUL = [[0]*4 for _ in range(4)]
def _add(a,b):
    return ((a&1)^(b&1)) | (((a>>1)^(b>>1))<<1)
for a in range(4):
    for b in range(4):
        ADD[a][b]=_add(a,b)
def _mul(a,b):
    # polys over GF2: a0+a1 t
    a0,a1=a&1,(a>>1)&1; b0,b1=b&1,(b>>1)&1
    # product: a0b0 + (a0b1+a1b0) t + a1b1 t^2; t^2=t+1
    c0=a0&b0; c1=(a0&b1)^(a1&b0); c2=a1&b1
    return (c0^c2) | ((c1^c2)<<1)
for a in range(4):
    for b in range(4):
        MUL[a][b]=_mul(a,b)
INV={1:1,2:3,3:2}
assert all(MUL[a][INV[a]]==1 for a in INV)
