"""Exact Gaussian-integer cyclic Fourier checker for onto words over Z/4Z.
Run: python check_cyclic.py [maximum_n]. Default maximum_n=8.
"""
import itertools
import sys

def run(max_n=8):
    assert 4 <= max_n <= 9
    for n in range(4, max_n+1):
        N=4**n
        re=[0]*N
        im=[0]*N
        # Lexicographic digits are base-four little-endian coordinates.
        for word in itertools.product(range(4),repeat=n):
            if len(set(word))==4:
                k=sum(x*(4**i) for i,x in enumerate(word))
                re[k]=1
        onto=sum(re)
        # The 4x4 unnormalized DFT sends (a,b,c,d) to
        # (a+b+c+d, a-c+i(b-d), a-b+c-d, a-c-i(b-d)).
        for i in range(n):
            stride=4**i
            for base in range(0,N,4*stride):
                for offset in range(stride):
                    indices=[base+offset+u*stride for u in range(4)]
                    a,b,c,d=[(re[v],im[v]) for v in indices]
                    values=[
                        (a[0]+b[0]+c[0]+d[0], a[1]+b[1]+c[1]+d[1]),
                        (a[0]-c[0]-(b[1]-d[1]),a[1]-c[1]+b[0]-d[0]),
                        (a[0]-b[0]+c[0]-d[0],a[1]-b[1]+c[1]-d[1]),
                        (a[0]-c[0]+b[1]-d[1],a[1]-c[1]-b[0]+d[0]),
                    ]
                    for v,(x,y) in zip(indices,values):
                        re[v]=x;im[v]=y
        zeros_balanced=0
        for k in range(N):
            freq=[(k//(4**j))%4 for j in range(n)]
            balanced=sum(freq)%4==0
            zero=re[k]==0 and im[k]==0
            expect_zero=not balanced or (n%2==1 and all(v!=0 for v in freq))
            if zero != expect_zero:
                raise AssertionError((n,k,freq,(re[k],im[k]),expect_zero))
            if balanced and zero: zeros_balanced+=1
            if balanced and im[k]!=0:
                raise AssertionError(('imaginary',n,k,im[k]))
        expected_extra=(3**n-3)//4 if n%2 else 0
        assert zeros_balanced==expected_extra
        assert sum(x*x+y*y for x,y in zip(re,im))==N*onto
        assert re[0]==onto==4**n-4*3**n+6*2**n-4 and im[0]==0
        print(f'Cyclic n={n} onto={onto} rank={sum(x!=0 or y!=0 for x,y in zip(re,im))} extra={zeros_balanced}: PASS')
if __name__=='__main__':
    run(int(sys.argv[1]) if len(sys.argv)>1 else 8)
