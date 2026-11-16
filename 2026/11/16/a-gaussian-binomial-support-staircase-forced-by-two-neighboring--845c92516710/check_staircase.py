import numpy as np
import math

def build(N,d):
    assert N%d==0 and d>1
    m=N//d; beta=.7; alpha=(1+(-beta)**d)**(1/d)
    omega=np.exp(2j*np.pi/N)
    R=alpha+beta*omega**(m*np.arange(N))
    # ensure cyclic consistency
    assert abs(np.prod(R)-1)<5e-9
    gbar=np.ones(N,dtype=complex)
    for n in range(1,N):gbar[n]=gbar[n-1]/R[n]
    f=1/gbar
    V=np.stack([np.fft.fft(f*np.roll(gbar,x))/np.sqrt(N) for x in range(N)])
    return V

def run():
    tests=0
    for N in range(3,27):
        for d in range(2,N+1):
            if N%d:continue
            V=build(N,d)
            magnitudes=np.abs(V)
            row_sizes=np.count_nonzero(magnitudes>1e-7,axis=1)
            assert row_sizes.tolist()==[1+x%d for x in range(N)], (N,d,row_sizes)
            assert np.max(magnitudes[magnitudes<1e-7],initial=0)<1e-8
            assert row_sizes.sum()==N*(d+1)//2
            tests+=N*N
    print('PASS',tests,'STFT entries checked; all divisor staircases and support totals matched.')
if __name__=='__main__':run()
