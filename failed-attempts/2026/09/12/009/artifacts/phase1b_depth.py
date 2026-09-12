"""Deeper falsification pressure: (a) integer solutions c<=1e13 list is complete via sieve-style;
(b) v>=4 search with larger m-range; (c) small-exponent exact S-unit sweep: for exponents of
2,3,7,11 bounded, c=prod p_i^e_i * 50069^f for small f, test c+-1 smoothness exactly."""
import math, time, itertools
t0=time.time()
P=50069; S3=[2,3,7,11,50069]; SP=[2,3,7,11]
def is_smooth(n,primes):
    if n<=0: return False
    for p in primes:
        while n%p==0: n//=p
    return n==1
def gen_smooth(primes,limit):
    out=[]
    def rec(i,cur):
        if i==len(primes):
            out.append(cur); return
        p=primes[i]; v=cur
        while v<=limit:
            rec(i+1,v)
            if v>limit//p: break
            v*=p
    rec(0,1); out.sort(); return out
# (b) wider witness: n {2,3,7,11}-smooth <=1e15, m<=10^5 S'-smooth, v=4
nlist=gen_smooth(SP,10**15); mlist=gen_smooth(SP,10**5)
pv=P**4
print(f"#n={len(nlist)} #m={len(mlist)}", flush=True)
hits=0; checked=0
for n in nlist:
    if n<2: continue
    for m in mlist:
        if pv*m >= n and (pv*m-n) % 1 == 0: pass
        for e in (1,-1):
            s=n-e*pv*m
            if s==0: continue
            checked+=1
            if is_smooth(abs(s),S3):
                print(f"WITNESS v=4 e={e} m={m} n={n} s={s}", flush=True); hits+=1
    if hits: break
print(f"checked={checked} hits={hits} ({time.time()-t0:.1f}s)")
# (c) exponent sweep: exponents 2..7 each in -6..6, f in -3..3 on 50069, test x=c, y=1-c
from fractions import Fraction
import itertools
hits=0; tot=0
rng=range(-6,7)
for exps in itertools.product(rng, repeat=4):
    c=Fraction(1)
    for b,e in zip(SP,exps): c*=Fraction(b)**e
    for f in range(-3,4):
        cc=c*Fraction(P)**f
        if cc<=0 or cc==1: continue
        tot+=1
        num,den=cc.numerator,cc.denominator
        yy=1-cc; yn,yd=yy.numerator,yy.denominator
        if is_smooth(num,S3) and is_smooth(den,S3) and is_smooth(yn,S3) and is_smooth(yd,S3):
            # ord_p of x(1-x): vals
            def op(n):
                k=0
                while n%P==0: n//=P; k+=1
                return k
            o=op(abs(num))+op(abs(yn))-0  # x(1-x)= num*yn/(den*yd) -> careful
            # need denom contributions: ord(x(1-x)) = ord(num)+ord(yn)-ord(den)-ord(yd)
            o=op(abs(num))+op(abs(yn))-op(abs(den))-op(abs(yd))
            print(f"SOL x={cc} ord_p(x(1-x))={o}")
            hits+=1
            if hits>30: break
    if hits>30: break
print(f"sweep total={tot} sols>30stopped={hits>30} ({time.time()-t0:.1f}s)")
