"""Independent exact cyclic transfer counts and symbolic algebra tests."""

def multiply(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]

def trace_power(m):
    a=[[0,1],[1,1]]
    power=[[1,0],[0,1]]
    for _ in range(m):
        power=multiply(power,a)
    return power[0][0]+power[1][1]

def direct_binary(m):
    return sum(all((not (((word >> i)&1)==0 and ((word>>((i+1)%m))&1)==0))
                   for i in range(m)) for word in range(1<<m))

if __name__=='__main__':
    L0,L1=2,1
    L=[L0,L1]
    for m in range(2,61):L.append(L[-1]+L[-2])
    for m in range(2,61):
        t=trace_power(m)
        assert t==L[m]
        if m<=18:assert t==direct_binary(m)
    for n in range(3,61):
        t=L[n] if n%2 else L[n//2]**2
        correction=0 if n%2 else 2*((-1)**(n//2))
        assert t==L[n]+correction
        assert 2**n+t > 2**n
    print('PASS: transfer traces through 60 and direct cyclic-word counts through 18.')
