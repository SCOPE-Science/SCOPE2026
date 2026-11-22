"""Independent trace/cube calculation for an irreducible quadratic base extension.
All arithmetic is exact over F_p[sqrt(d)] with nonsquare d.  No external modules.
"""

def nonsquare(p):
    return next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)

def mul(x,y,p,d):
    a,b=x;c,e=y
    return ((a*c+d*b*e)%p,(a*e+b*c)%p)

def power(x,n,p,d):
    acc=(1,0)
    while n:
        if n&1:acc=mul(acc,x,p,d)
        x=mul(x,x,p,d)
        n//=2
    return acc

def check(p):
    d=nonsquare(p)
    expected={0:(p-1)//2}
    expected.update({s:(p-5)//6 for s in range(1,p)})
    counts={s:0 for s in range(p)}
    cuberoot_counts={s:0 for s in range(p)}
    for a in range(p):
        for b in range(p):
            s=(2*a)%p
            if (a,b)!=(0,0):
                if power((a,b),(p*p-1)//3,p,d)==(1,0) and b:
                    counts[s]+=1
                cube=power((a,b),3,p,d)
                cuberoot_counts[(2*cube[0])%p]+=1
            else:
                cuberoot_counts[0]+=1
    assert all(v%2==0 for v in counts.values())
    counts={s:v//2 for s,v in counts.items()}
    assert counts==expected, (p,counts,expected)
    assert cuberoot_counts[0]==3*p-2
    assert all(cuberoot_counts[s]==p-2 for s in range(1,p))
    print(f'p={p}: quadratic cubes at trace 0: {counts[0]}, trace nonzero: {counts[1]}; verified')
for prime in (5,11,17,23,29,41):check(prime)
print('CUBIC_TRACE_DISTRIBUTION_VERIFIED')
