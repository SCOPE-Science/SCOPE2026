from fractions import Fraction as F

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def mv(A,x):
    return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

I=[[F(1),F(0)],[F(0),F(1)]]

for k in map(F,[2,3,4,7]):
    d=[k,F(1)]
    e=[F(1),-k]
    B=[[F(1),F(0)],[F(0),k*k]]
    Bd=mv(B,d)
    den=dot(d,Bd)

    # P = I - d (Bd)^T / den
    P=[[I[i][j]-d[i]*Bd[j]/den for j in range(2)] for i in range(2)]
    assert P == [[F(1,2),-k/F(2)],[-F(1,2)/k,F(1,2)]]
    assert mm(P,P)==P

    # Rank-one Frobenius norm squared equals the sole nonzero singular value squared.
    frob2=sum(x*x for row in P for x in row)
    sharp=((k*k+1)/(2*k))**2
    assert frob2==sharp

    eta= -dot(d,mv(B,e))/den
    assert eta==(k*k-1)/(2*k)
    ep=[e[i]+eta*d[i] for i in range(2)]
    assert ep==[(k*k+1)/2, -(k*k+1)/(2*k)]

    err_ratio_sq=dot(ep,ep)/dot(e,e)
    assert err_ratio_sq==sharp

    Ae=[e[0],k*e[1]]
    Aep=[ep[0],k*ep[1]]
    res_ratio_sq=dot(Aep,Aep)/dot(Ae,Ae)
    expected=(k*k+1)**2/(2*(k**4+1))
    assert res_ratio_sq==expected
    if k>1:
        assert res_ratio_sq<1

# Concrete kappa=3 witness.
k=F(3)
assert ((k*k+1)/(2*k))==F(5,3)
assert (k*k+1)**2/(2*(k**4+1))==F(25,41)

print("VERIFY_OK")
print("kappa3_error_ratio", F(5,3))
print("kappa3_residual_ratio_sq", F(25,41))
