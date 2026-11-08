"""Independent bit-matrix checks for parity-sum dynamics on square open grids."""

def rank(rows):
    piv={}
    for v in rows:
        while v:
            j=v.bit_length()-1
            if j in piv:
                v^=piv[j]
            else:
                piv[j]=v
                break
    return len(piv)

def prod(A,C):
    out=[]
    for v in A:
        r=0
        while v:
            b=v&-v
            r^=C[b.bit_length()-1]
            v-=b
        out.append(r)
    return out

def pred(n,t):
    h=(n+1)&-(n+1)
    u=(n+1)//h
    if h==1: return (u-1)*min(t,2)
    return min(t,1)+(h-2)*min(t,h)+(u-1)*h*min(t,2*h)

def main():
    tests=0
    for n in range(2,19):
        N=n*n
        B=[]
        for y in range(n):
            for x in range(n):
                v=0
                for xx,yy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                    if 0<=xx<n and 0<=yy<n:
                        v|=1<<(yy*n+xx)
                B.append(v)
        P=[1<<i for i in range(N)]
        h=(n+1)&-(n+1)
        u=(n+1)//h
        cutoff=(2*h if u>1 else h)
        last=None
        for t in range(cutoff+3):
            dim=N-rank(P)
            expected=pred(n,t)
            assert dim==expected,(n,t,dim,expected)
            if t==1: assert dim==n
            tests+=1
            last=dim
            P=prod(B,P)
        print('n=%2d h=%2d u=%2d recurrent=%3d Tmax=%2d kernelT=%3d' % (n,h,u,N-last,cutoff,last))
    print('ALL PASS: %d GF(2) exact matrix power/nullity comparisons' % tests)
if __name__=='__main__':main()
