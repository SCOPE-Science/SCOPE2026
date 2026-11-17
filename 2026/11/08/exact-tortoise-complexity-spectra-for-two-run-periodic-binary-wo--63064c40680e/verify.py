"""Finite checks of the one-iterate tortoise map for a,b >= 2."""
from collections import Counter


def tortoise_delete(w):
    i = w.find('1')
    return w if i < 0 else w[:i] + w[i+1:] + '1'


def tortoise_gaps(w):
    g = w.split('1')
    return w if len(g) == 1 else g[0] + g[1] + '1' + ''.join(z+'1' for z in g[2:])


def factors(a, b, n):
    period = '0'*a + '1'*b
    t = period*(n//len(period)+3)
    return {t[i:i+n] for i in range(len(period))}


if __name__ == '__main__':
    count=0
    for a in range(2, 13):
        for b in range(2, 13):
            p=a+b
            for n in range(1, 4*p+4):
                w=factors(a,b,n)
                assert {tortoise_delete(u) for u in w} == {tortoise_gaps(u) for u in w}
                fibers={}
                for u in w: fibers.setdefault(tortoise_delete(u), []).append(u)
                total=len(fibers)
                expect=2 if n==1 else (min(n,a)+min(n,b)-1 if n<=p else p)
                assert total==expect,(a,b,n,total,expect)
                doubled=[set(v) for v in fibers.values() if len(v)>1]
                if 2<=n<=p:
                    pair={('0'*(n-1)+'1'),('1'+'0'*(n-1))} if n<=a+1 else {'0'*a+'1'*(n-a),'1'+'0'*a+'1'*(n-a-1)}
                    assert doubled==[pair],(a,b,n,doubled,pair)
                else: assert doubled==[],(a,b,n,doubled)
                count+=1
    print('VERIFY_OK one_step_nontrivial_two_run',count)
