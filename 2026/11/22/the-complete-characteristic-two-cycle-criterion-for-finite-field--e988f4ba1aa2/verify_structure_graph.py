"""Independent finite-field checks for cycles of (a,b)->(a+b,ab).
All fields are polynomial bases over F2; integers encode polynomial coefficients.
"""
MODS={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011,7:0b10000011,8:0b100011101}

def poly_rem(a,b):
    """Remainder in the Euclidean polynomial ring F2[x]."""
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a

def is_irreducible(f,degree):
    for d in range(1,degree//2+1):
        for monic in range(1<<d,1<<(d+1)):
            if poly_rem(f,monic)==0:
                return False
    return True

def mul(a,b,m):
    modulus=MODS[m]; q=1<<m; z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a&q:a^=modulus
    return z

def T(x,m):
    a,b=x
    return (a^b,mul(a,b,m))

def cycles(m):
    q=1<<m; seen=set();found=[]
    for a in range(q):
        for b in range(q):
            z=(a,b)
            if z in seen:continue
            path=[]; position={}
            while z not in position and z not in seen:
                position[z]=len(path);path.append(z);z=T(z,m)
            seen.update(path)
            if z in position:found.append(path[position[z]:])
    return found

def main():
    for m in range(1,9):
        assert is_irreducible(MODS[m],m), (m,MODS[m])
        c=cycles(m);long=[t for t in c if len(t)>1]
        print('m',m,'q',1<<m,'components',len(c),'nontrivial',len(long),'lengths',sorted({len(t) for t in long}))
        assert (len(long)>0)==(m not in (1,2))
    orbit=[(14,11),(5,8),(13,14),(3,10),(9,13),(4,15),(11,9),(2,12)]
    assert len(set(orbit))==8
    assert all(T(orbit[i],4)==orbit[(i+1)%8] for i in range(8))
    for m in (1,2):assert all(len(c)==1 for c in cycles(m))
    for m in (3,5,6,7):
        q=1<<m
        # Nonzero periodic orbit of g, as used in the general proof.
        def g(x):return x^mul(x,x,m)
        visited=set();long=[]
        for x in range(q):
            if x in visited:continue
            chain=[];ind={};y=x
            while y not in ind and y not in visited:
                ind[y]=len(chain);chain.append(y);y=g(y)
            visited.update(chain)
            if y in ind and len(chain[ind[y]:])>1: long.append(chain[ind[y]:])
        assert long, m
        witness=long[0]
        assert T((1,witness[0]),m)==(1^witness[0],witness[0])
        assert T(T((1,witness[0]),m),m)==(1,g(witness[0]))
        print('g_cycle_example',m,len(witness),witness[:20])
    print('STRUCTURE_GRAPH_VERIFY_OK')
if __name__=='__main__':main()
