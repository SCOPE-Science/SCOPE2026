"""Independent direct enumeration of all inputs on binary cyclic rings."""
from collections import deque

def images(n):
    m=(1<<n)-1
    seen=set()
    for x in range(1<<n):
        left=((x<<1)&m)|(x>>(n-1))
        right=(x>>1)|((x&1)<<(n-1))
        y=(x|right)^(left&x&right)
        assert (0<=y<=m)
        seen.add(y)
    return len(seen)

def main():
    expected=[1,2,5,10,22,41,79,154,302,582,1113,2125,4058,7737,14725,27994,53195,101048]
    for n, target in enumerate(expected,1):
        val=images(n)
        assert val==target,(n,val,target)
    print('VERIFY_DIRECT_OK all 18 cyclic ring sizes compared by direct brute force')
if __name__=='__main__': main()
