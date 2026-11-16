"""Independent direct-colouring Fourier-zero verification (exact residue counts)."""
import itertools
import numpy as np

def check(n):
    d = 2*n-1
    states=[]
    for coords in itertools.product(range(3),repeat=d):
        top=(0,)+coords[1::2]
        bottom=coords[0::2]
        if any(a==b for a,b in zip(top,bottom)):continue
        if any(top[j]==top[j+1] or bottom[j]==bottom[j+1] for j in range(n-1)):continue
        states.append(coords)
    assert len(states)==2*3**(n-1), (n,len(states))
    states=np.array(states,dtype=np.int64)
    zeros=0;nonzero=0
    powers=3**np.arange(d-1,-1,-1,dtype=np.int64)
    N=3**d
    for low in range(0,N,2048):
        ids=np.arange(low,min(low+2048,N),dtype=np.int64)
        freq=((ids[:,None]//powers[None,:])%3)
        residues=(freq@states.T)%3
        c0=(residues==0).sum(axis=1)
        c1=(residues==1).sum(axis=1)
        c2=len(states)-c0-c1
        # x0+x1*omega+x2*omega^2 is zero iff all three counts equal.
        z=(c0==c1)&(c1==c2)
        # Separately check the explicit first/last nonzero suffix-frequency criterion.
        predicted=np.zeros(len(ids),dtype=bool)
        for index,frequency in enumerate(freq):
            delta=[int(frequency[0])]+[int(frequency[2*i]) for i in range(1,n)]
            gamma=[0]+[(int(frequency[2*i-1])+int(frequency[2*i]))%3 for i in range(1,n)]
            suffix=[sum(gamma[j+1:])%3 for j in range(n-1)]
            markers=[j for j,t in enumerate(suffix) if t]
            if not markers:
                predicted[index]=any(delta[:j]==[0]*j and delta[j]==delta[j+1]!=0
                    and delta[j+2:]==[0]*(n-j-2) for j in range(n-1))
            else:
                a,b=markers[0],markers[-1]
                left=(delta[:a]==[0]*a and delta[a]==suffix[a])
                right=(delta[b+1]==(-suffix[b])%3 and delta[b+2:]==[0]*(n-b-2))
                predicted[index]=left or right
        assert np.array_equal(z,predicted), (n,low)
        zeros+=int(z.sum()); nonzero+=int((~z).sum())
    expected=(3*9**n-24*n+45)//16
    assert nonzero==expected, (n,nonzero,expected)
    print(f'n={n} colourings={3*len(states)} balanced={N} rank={nonzero} zeros={zeros}')

if __name__=='__main__':
    for n in range(1,6):check(n)
