"""Independent exact Eisenstein-ring computation and orbit walk.
Run: python crosscheck.py
"""
from itertools import product
from collections import defaultdict

# omega^2 = -1 - omega, and 1,omega is a Z-basis.
root = ((1,0), (0,1), (-1,-1))
def mul(a,b):
    A,B=a; C,D=b
    return (A*C-B*D, A*D+B*C-B*D)
def conjugate(a):
    A,B=a
    return (A-B, -B)
def autocorr(t):
    z = [root[j] for j in t]
    N = len(z)
    return tuple(tuple(sum(mul(z[j],conjugate(z[(j+k)%N]))[i]
                  for j in range(N)) for i in (0,1)) for k in range(N))
def normalized(t):
    v=t[0]
    return tuple((a-v)%3 for a in t)
def orbit(t):
    N=len(t)
    seen={normalized(t)}
    frontier=list(seen)
    while frontier:
        v=frontier.pop()
        transforms = (
            normalized(v[1:]+v[:1]),
            normalized(tuple((-v[(-j)%N])%3 for j in range(N))),
        )
        for u in transforms:
            if u not in seen:
                seen.add(u); frontier.append(u)
    return seen

def main():
    for N in range(1,7):
        words={(0,)+tail for tail in product((0,1,2), repeat=N-1)}
        assert len(words)==3**(N-1)
        spectra=defaultdict(set)
        for w in words:
            spectra[autocorr(w)].add(w)
        ambiguous=[]
        orbit_count=0
        for bucket in spectra.values():
            remaining=set(bucket);num=0
            while remaining:
                o=orbit(next(iter(remaining)))
                assert o <= bucket
                remaining-=o
                num+=1
            orbit_count+=num
            if num>1:ambiguous.append((bucket,num))
        assert (len(spectra),orbit_count,len(ambiguous)) == {
            1:(1,1,0),2:(2,2,0),3:(4,4,0),4:(7,7,0),5:(13,13,0),6:(30,32,1)
        }[N]
        if N==6:
            bucket,num=ambiguous[0]
            assert num==3 and len(bucket)==18
            assert autocorr(next(iter(bucket))) == ((6,0),(0,0),(0,0),(3,0),(0,0),(0,0))
        print(N,len(spectra),orbit_count,len(ambiguous))
    print('PASS')
if __name__ == '__main__':main()
