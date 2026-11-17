"""Independent weighted classification via permutable matched-pair types."""
from math import factorial, comb

def step(pairs):
    n=len(pairs)
    a=sum(x for x,y in pairs)
    b=sum(y for x,y in pairs)
    def opinion(current,total_except):
        d=n-1
        if 2*total_except>d: return 1
        if 2*total_except<d: return 0
        return current
    return tuple((opinion(x,b-y),opinion(y,a-x)) for x,y in pairs)

def prediction(n):
    v={(t,p):0 for t in range(4) for p in (1,2)}
    if n%2==0:
        C=comb(n,n//2); L=(2**n-C)//2
        v[0,1]=2+C
        v[0,2]=(C+2)*(C+1)
        v[1,1]=2*L*L-2
        v[1,2]=4**n-v[0,1]-v[0,2]-v[1,1]
    else:
        k=(n-1)//2; C=comb(n,k); L=sum(comb(n,j) for j in range(k))
        H=L-(k+2)*2**k+1+(k+1)**2
        v[0,1]=2+2*n*comb(n-1,k)+2*C
        v[0,2]=2
        v[1,1]=2*L*L-2+4*C*(2**k-1)+2*C+2*C*k*(k+1)
        v[1,2]=2*L*L-2
        v[2,2]=4*C*H+2*C*(C-1-k*(k+1))
        v[3,1]=4*C*(k+1)*(2**k-k-1)
        v[2,1]=4**n-sum(v.values())
    return v

def count(n):
    weights=factorial(n)
    categories=((0,0),(1,0),(0,1),(1,1))
    result={(t,p):0 for t in range(4) for p in (1,2)}
    for u in range(n+1):
      for v in range(n-u+1):
       for w in range(n-u-v+1):
        z=n-u-v-w
        pairs=(categories[0],)*u+(categories[1],)*v+(categories[2],)*w+(categories[3],)*z
        states=[pairs]
        for _ in range(5):states.append(step(states[-1]))
        valid=[t for t in range(4) if states[t]==states[t+2]]
        assert valid,(n,u,v,w,z)
        t=valid[0]; p=1 if states[t]==states[t+1] else 2
        result[t,p]+=weights//(factorial(u)*factorial(v)*factorial(w)*factorial(z))
    assert result==prediction(n), (n,result,prediction(n))
    return result

if __name__=='__main__':
    for n in range(3,27):
      print('n=',n,'classes=',(n+1)*(n+2)*(n+3)//6,'counts=',count(n),'OK')
