"""Independent direct sums for parabolic-fiber Fourier identities."""
import cmath, math, itertools

def primes():
    return [3,5,7,11,13,17]

def test_prime(p):
    z=cmath.exp(2j*math.pi/p)
    count=0
    for subset in [(0,),(0,1),(0,2),(0,1,2),tuple(range(p))]:
        H=sorted(set(x%p for x in subset))
        S=[(x,(x*x+h)%p) for x in range(p) for h in H]
        direct=sum(abs(sum(z**((u*x+v*y)%p) for x,y in S)) for u in range(p) for v in range(p))/p**2
        hhat={v:sum(z**((v*h)%p) for h in H) for v in range(p)}
        predicted=len(H)/p +sum(abs(hhat[v]) for v in range(1,p))/math.sqrt(p)
        assert abs(direct-predicted)<1e-8,(p,H,direct,predicted)
        pair={}
        for a in S:
            for b in S:
                t=((a[0]+b[0])%p,(a[1]+b[1])%p)
                pair[t]=pair.get(t,0)+1
        energy=sum(y*y for y in pair.values())
        eh={}
        for a in H:
            for b in H:
                t=(a+b)%p
                eh[t]=eh.get(t,0)+1
        EH=sum(y*y for y in eh.values())
        assert energy==(p*p-p)*len(H)**4 + p*p*EH,(p,H,energy,EH)
        if len(H)==2:
            formula=(2*math.sqrt(p)/p)/math.sin(math.pi/(2*p))-2/math.sqrt(p)+2/p
            assert abs(direct-formula)<1e-8
        count+=3
    return count

def gf9_check():
    p=3
    FF=list(range(9))
    add=lambda x,y:(x%3+y%3)%3+3*((x//3+y//3)%3)
    mul=lambda x,y:((x%3)*(y%3)-x//3*(y//3))%3+3*(((x%3)*(y//3)+(x//3)*(y%3))%3)
    tr=lambda x:add(x,mul(x,mul(x,x)))%3
    psi=lambda x:cmath.exp(2j*math.pi*tr(x)/3)
    for H in [[0],[0,1],[0,3],[0,1,3],[0,1,2,3,4,5,6,7,8]]:
        S=[(x,add(mul(x,x),h)) for x in FF for h in H]
        L=sum(abs(sum(psi(add(mul(u,x),mul(v,y))) for x,y in S)) for u in FF for v in FF)/81
        right=len(H)/9 + sum(abs(sum(psi(mul(v,h)) for h in H)) for v in FF[1:])/3
        assert abs(L-right)<1e-8,(H,L,right)
        c={}
        for x,y in S:
            for a,b in S:
                v=(add(x,a),add(y,b));c[v]=c.get(v,0)+1
        eh={}
        for a in H:
            for b in H:
                v=add(a,b);eh[v]=eh.get(v,0)+1
        assert sum(k*k for k in c.values())==72*len(H)**4+81*sum(k*k for k in eh.values())
    return 10

def main():
    tests=sum(test_prime(p) for p in primes())+gf9_check()
    print('PASS',tests,'independent norm and energy comparisons including F9')
if __name__=='__main__':main()
