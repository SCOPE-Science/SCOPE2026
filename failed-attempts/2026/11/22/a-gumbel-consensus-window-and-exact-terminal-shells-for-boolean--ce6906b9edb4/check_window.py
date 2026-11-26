"""Independent exact bit-parallel one/two-step OR and Poisson-moment checks."""
import random, math

def updater(d):
    n=1<<d
    l=[]
    for b in range(d):
        lo=sum(1<<i for i in range(n) if not(i>>b&1))
        hi=((1<<n)-1)^lo
        l.append((1<<b,lo,hi))
    def F(x):
        out=0
        for step,lo,hi in l:
            out |= ((x&lo)<<step)|((x&hi)>>step)
        return out
    return F

def test():
    rng=random.Random(240117)
    for d in (6,8,10,12):
        n=1<<d; F=updater(d); full=(1<<n)-1
        trials=12000
        nozero=zero2=0
        for _ in range(trials):
            x=rng.getrandbits(n)
            y=F(x)
            nozero+=(y==full)
            zero2+=(F(y)!=full)
        p=nozero/trials
        print('d',d,'trials',trials,'P_all_at_1',round(p,6),'target_exp(-1)',round(math.exp(-1),6),'P_not_all_at_2',zero2/trials)
        if d>=10:assert abs(p-math.exp(-1))<.07
        if d>=8:assert zero2==0
    for d in (8,10,12,16,20):
        M=1<<d;Q=.5
        fact2=M*(M-1-math.comb(d,2))*Q**(2*d)+M*math.comb(d,2)*Q**(2*d-2)
        assert 0<fact2-1<2*d*d/(2**d)
        print('d',d,'E_W',1,'E_falling_W2',round(fact2,9))
    print('WINDOW_OK')
if __name__=='__main__':test()
