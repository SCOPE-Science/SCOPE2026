"""Dependency-free exhaustive bitangent count for Ciani quartics over prime fields.
A bitangent here includes a hyperflex; the line restriction must be a
nonzero scalar times a squared homogeneous quadratic over the algebraic closure.
"""

def lines(p):
    yield from ((1,a,b) for a in range(p) for b in range(p))
    yield from ((0,1,b) for b in range(p))
    yield (0,0,1)

def mul(a,b,p):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]=(z[i+j]+x*y)%p
    return z

def restricted_quartic(line,lam,p):
    k=max(i for i,v in enumerate(line) if v)
    i,j=[i for i in range(3) if i!=k]
    t=pow(line[k],-1,p)
    f=[[0,0] for _ in range(3)]
    f[i]=[1,0]; f[j]=[0,1]
    f[k]=[(-t*line[i])%p,(-t*line[j])%p]
    powers=[]
    for a in f:
        h=[[1]]
        for _ in range(4):h.append(mul(h[-1],a,p))
        powers.append(h)
    out=[0]*5
    for i in range(3):
        for n,v in enumerate(powers[i][4]):out[n]=(out[n]+v)%p
    for i,j in ((0,1),(0,2),(1,2)):
        h=mul(powers[i][2],powers[j][2],p)
        for n,v in enumerate(h):out[n]=(out[n]+lam*v)%p
    return out

def squared_binary_quartic(coefs,p):
    # Coefficient order is v^4, u*v^3, u^2*v^2, u^3*v, u^4.
    E,D,C,B,A=coefs
    inv=lambda a:pow(a%p,-1,p)
    if A:
        b=B*inv(2*A)%p
        c=(C*inv(A)-b*b)*inv(2)%p
        return (D-A*2*b*c)%p==0 and (E-A*c*c)%p==0
    if B:return False
    if C:
        t=D*inv(2*C)%p
        return (E-C*t*t)%p==0
    return D==0

def square(x,p):
    return pow(x%p,(p-1)//2,p)==1

def predicted(lam,p):
    v=int(square(-lam-1,p))
    return 4+12*v+12*v*int(square(lam+2,p))

def main():
    cases=0; nums={4:0,16:0,28:0}
    for p in (3,5,7,11,13,17,19,23,29,31,37,41):
        for lam in range(p):
            if lam in (-1%p,2%p,-2%p):continue
            n=sum(squared_binary_quartic(restricted_quartic(t,lam,p),p)
                  for t in lines(p))
            want=predicted(lam,p)
            assert n==want,(p,lam,n,want)
            assert n in nums
            nums[n]+=1; cases+=1
    print('VERIFY_PRIME_FIELDS_OK',cases,nums)

if __name__=='__main__':main()
