"""Independent exact census for two proper extension fields GF(9), GF(25).
No CAS dependency. GF(p^2) is represented with a nonsquare square-root basis.
"""

def field(p):
    d=next(a for a in range(2,p) if pow(a,(p-1)//2,p)==p-1)
    q=p*p
    mul=[[0]*q for _ in range(q)]; add=[[0]*q for _ in range(q)]
    for x in range(q):
        a,b=x%p,x//p
        for y in range(q):
            c,e=y%p,y//p
            add[x][y]=(a+c)%p+p*((b+e)%p)
            mul[x][y]=(a*c+d*b*e)%p+p*((a*e+b*c)%p)
    def power(x,n):
        out=1
        while n:
            if n&1:out=mul[out][x]
            x=mul[x][x]; n//=2
        return out
    inv=[0]+[power(x,q-2) for x in range(1,q)]
    return q,add,mul,inv,power

def main():
    total=0
    for p in (3,5):
        q,A,M,I,P=field(p)
        def sm(a,b): return M[a][b]
        def plus(a,b): return A[a][b]
        def neg(a):return (-a%p)+p*((-(a//p))%p)
        def sub(a,b):return plus(a,neg(b))
        def val(x):return x%p
        def squared(l):return P(l,(q-1)//2)==1
        projective=[(1,a,b) for a in range(q) for b in range(q)] + [(0,1,b) for b in range(q)]+[(0,0,1)]
        def quartic(line,l):
            k=max(i for i in range(3) if line[i]!=0)
            i,j=[i for i in range(3) if i!=k]
            z=[[0,0] for _ in range(3)]
            z[i]=[1,0]; z[j]=[0,1]
            z[k]=[neg(sm(line[i],I[line[k]])),neg(sm(line[j],I[line[k]]))]
            def multiply(f,g):
                h=[0]*(len(f)+len(g)-1)
                for a,u in enumerate(f):
                    for b,v in enumerate(g):h[a+b]=plus(h[a+b],sm(u,v))
                return h
            pow4=[]
            for w in z:
                powers=[[1]]
                for _ in range(4):powers.append(multiply(powers[-1],w))
                pow4.append(powers)
            out=[0]*5
            for i in range(3):
                for j,c in enumerate(pow4[i][4]):out[j]=plus(out[j],c)
            for i,j in ((0,1),(0,2),(1,2)):
                part=multiply(pow4[i][2],pow4[j][2])
                for k,c in enumerate(part):out[k]=plus(out[k],sm(l,c))
            return out
        def is_sq(v):
            E,D,C,B,T=v
            if T:
                b=sm(B,I[sm(val(2),T)])
                c=sm(sub(sm(C,I[T]),sm(b,b)),I[val(2)])
                return D==sm(T,sm(val(2),sm(b,c))) and E==sm(T,sm(c,c))
            if B:return False
            if C:
                c=sm(D,I[sm(val(2),C)])
                return E==sm(C,sm(c,c))
            return D==0
        for lam in range(q):
            if lam in (neg(1),val(2),neg(val(2))):continue
            x=neg(plus(lam,1));y=plus(lam,val(2))
            want=4+12*int(squared(x)) +12*int(squared(x) and squared(y))
            got=sum(is_sq(quartic(line,lam)) for line in projective)
            assert got==want,(p,lam,want,got)
            total+=1
    print('VERIFY_QUADRATIC_FIELDS_OK',total)

if __name__=='__main__':main()
