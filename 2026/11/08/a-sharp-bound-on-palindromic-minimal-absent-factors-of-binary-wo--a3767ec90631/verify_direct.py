"""Independent exhaustive palindrome generator, not based on palindromic factors."""
from itertools import product

def direct(w):
    n=len(w)
    res=[]
    for k in range(1,n+2):
        for half in product('01',repeat=(k+1)//2):
            h=''.join(half)
            p=h+h[:k//2][::-1]
            if p in w:continue
            if k==1 or (p[:-1] in w and p[1:] in w):res.append(p)
    return sorted(res)

def verify():
    from verify_earliest import pal_maws
    for n in range(1,13):
        for wv in product('01',repeat=n):
            w=''.join(wv)
            assert direct(w)==sorted(pal_maws(w)),(w,direct(w),pal_maws(w))
    for n in range(3,30):
        w='0'+'1'*(n-2)+'0'
        expected={'00','101','1'*(n-1)}|{'0'+'1'*k+'0' for k in range(1,n-2)}
        assert set(direct(w))==expected,(n,direct(w),expected)
    print('DIRECT_VERIFY_OK')

if __name__=='__main__':verify()
