"""Independent truncated-polynomial calculation of wheel local Jordan blocks."""

def mod_mul(a,b,h):
    mask=(1<<h)-1
    out=0
    while b:
        bit=b&-b
        b ^= bit
        out ^= (a << (bit.bit_length()-1)) & mask
    return out

def poly_rank(cols):
    piv = {}
    for c in cols:
        while c:
            k=c.bit_length()-1
            if k in piv: c ^= piv[k]
            else:
                piv[k]=c
                break
    return len(piv)

def local_map(a,f,h):
    c=sum(1<<i for i in range(2,h))
    return (f & 1, mod_mul(c,f,h) ^ (a<<(h-1)))

def local_matrix(h):
    # Coordinate zero is the hub, coordinates 1..h are polynomial coefficients.
    cols=[]
    for j in range(h+1):
        a=1 if j==0 else 0
        f=0 if j==0 else 1<<(j-1)
        A,F=local_map(a,f,h)
        cols.append(A | (F<<1))
    return cols

def apply_cols(cols,v):
    out=0
    while v:
        bit=v&-v
        out ^= cols[bit.bit_length()-1]
        v ^= bit
    return out

def predicted(h,t):
    if h==2: blocks=[3]
    elif h==4: blocks=[3,1,1]
    else: blocks=[h//2,h//2,1]
    return sum(min(t,j) for j in blocks)

checks=0
for h in (2,4,8,16,32,64,128):
    cols=local_matrix(h)
    curr=[1<<i for i in range(h+1)]
    for t in range(1,h+4):
        curr=[apply_cols(cols,x) for x in curr]
        dim=h+1-poly_rank(curr)
        assert dim==predicted(h,t),(h,t,dim,predicted(h,t))
        checks+=1
    c=sum(1<<i for i in range(2,h))
    c3=mod_mul(mod_mul(c,c,h),c,h)
    for j in range(h+1):
        a=1 if j==0 else 0
        f=0 if j==0 else 1<<(j-1)
        for _ in range(3): a,f=local_map(a,f,h)
        assert a==0 and f==mod_mul(c3,0 if j==0 else 1<<(j-1),h)
        checks+=1
    print('local',h,'Jordan',([3] if h==2 else [3,1,1] if h==4 else [h//2,h//2,1]))
print('LOCAL_MODULE_OK',checks)
