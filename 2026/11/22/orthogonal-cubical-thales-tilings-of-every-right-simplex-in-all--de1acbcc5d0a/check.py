from fractions import Fraction as F
from itertools import combinations, product

def verify(n,L,B):
    L=[F(z) for z in L]; B=[F(z) for z in B]
    assert all(z>0 for z in L+B) and sum(B[i]/L[i] for i in range(n))<1
    for v in [-1,*range(n)]:
        projections=[]
        for k in range(1,n+2):
            for face in combinations(range(-1,n),k):
                if v not in face: continue
                I=[i for i in face if i>=0]
                if -1 in face:
                    q=tuple(B[i] if i in I else F(0) for i in range(n))
                else:
                    t=(1-sum(B[i]/L[i] for i in I))/sum(1/(L[i]**2) for i in I)
                    q=tuple(B[i]+t/L[i] if i in I else F(0) for i in range(n))
                projections.append(q)
        predicted=[]
        if v==-1:
            for bits in product((0,1),repeat=n):
                predicted.append(tuple(B[i]*bits[i] for i in range(n)))
        else:
            for bits in product((0,1),repeat=n-1):
                I={v}|{i for i,bit in zip([j for j in range(n) if j!=v],bits) if bit}
                predicted.append(tuple(B[i] if i in I else F(0) for i in range(n)))
                t=(1-sum(B[i]/L[i] for i in I))/sum(1/(L[i]**2) for i in I)
                predicted.append(tuple(B[i]+t/L[i] if i in I else F(0) for i in range(n)))
        assert len(projections)==2**n and len(set(projections))==2**n
        assert set(projections)==set(predicted)
        for q in projections:
            assert all(q[i]>=0 for i in range(n))
            assert sum(q[i]/L[i] for i in range(n))<=1
            if v==-1:
                assert all(q[i]<=B[i] for i in range(n))
            else:
                t=L[v]*(q[v]-B[v])
                assert t>=0
                assert all(t>=L[i]*(q[i]-B[i]) for i in range(n))

if __name__=='__main__':
    count=0
    for n in range(2,7):
        for k in range(4):
            L=[2+i+(k%2) for i in range(n)]
            B=[F(L[i]*(i+1+k),10*n*n) for i in range(n)]
            verify(n,L,B)
            count+=1
    print('PASS: exact rational projection-vertex and normal-cell checks:',count,'cases, dimensions 2 through 6')
