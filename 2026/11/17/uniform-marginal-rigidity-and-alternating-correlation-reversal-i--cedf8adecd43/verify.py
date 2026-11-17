from fractions import Fraction as F

def integrate_poly2(a,b,c,d,l,r):
    return (a*c*(r**3-l**3)/3+(a*d+b*c)*(r*r-l*l)/2 + b*d*(r-l))/2

def generate(betas,N):
    # open interval endpoints, assigned null mass; coefficients give every time coordinate
    segs=[(F(-1),F(1),[(F(1),F(0))])]
    for n in range(N):
        new=[]
        for l,r,terms in segs:
            a,b=terms[-1]
            breaks=[l,r]
            if a!=0 and l< -b/a <r: breaks=[l,-b/a,r]
            for left,right in zip(breaks[:-1],breaks[1:]):
                mid=(left+right)/2
                s=1 if a*mid+b>0 else -1
                new.append((left,right,terms+[(betas[n%2]*a,betas[n%2]*b-F(s))]))
        segs=new
    return segs

def cross(betas,i,j):
    segs=generate(betas,max(i,j))
    result=F(0)
    for l,r,terms in segs:
        a,b=terms[i];c,d=terms[j]
        result+=integrate_poly2(a,b,c,d,l,r)
    return result

def variance_block(m):
    segs=generate([F(2),F(1)],2*m)
    result=F(0)
    for l,r,terms in segs:
        a=sum((terms[i][0] for i in range(1,2*m+1)),F(0))
        b=sum((terms[i][1] for i in range(1,2*m+1)),F(0))
        result+=integrate_poly2(a,b,a,b,l,r)
    return result

def test():
    e0=[F(2),F(1)]; e1=[F(1),F(2)]
    for phase,beta in [('even',e0),('odd',e1)]:
        for k in range(0,13):
            got=cross(beta,0,k)
            if k==0: expected=F(1,3)
            elif phase=='even':
                expected=F(1,3*2**((k+1)//2)) if k%2 else -F(1,6*2**(k//2))
            else:
                expected=-F(1,6*2**((k-1)//2)) if k%2 else F(1,3*2**(k//2))
            assert got==expected,(phase,k,got,expected)
            print(phase,k,str(got))
    for m in range(1,9):
        got=variance_block(m)
        want=F(m)-F(4,3)+F(4,3*2**m)
        assert got==want, (m,got,want)
        print('block_variance',m,got)
    print('all rational integration checks PASSED')

if __name__=='__main__':test()
