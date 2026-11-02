from fractions import Fraction

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
            for i in range(len(A))]

def quad(A,x):
    return sum(x[i]*A[i][j]*x[j]
               for i in range(len(x)) for j in range(len(x)))

for n in range(3,81):
    rdim = n-1
    L2 = Fraction(4,1)  # choose L=2 so G has integral entries

    # G=(L^2/4)(2I+J)=2I+J.
    G = [[Fraction(3 if i==j else 1,1) for j in range(rdim)]
         for i in range(rdim)]

    # G^{-1}=(2/L^2)(I-J/(n+1))=(1/2)(I-J/(n+1)).
    Gi = [[Fraction(1,2)*((Fraction(1,1) if i==j else Fraction(0,1))
                          - Fraction(1,n+1))
           for j in range(rdim)] for i in range(rdim)]

    P = matmul(G,Gi)
    for i in range(rdim):
        for j in range(rdim):
            assert P[i][j] == (1 if i==j else 0)

    # Deterministic exact covector r.  The norm reconstructed through the basis
    # is r^T G^{-1} r, which must equal the closed quadratic formula.
    rv = [Fraction(((7*i+3*n) % 11)-5, i+2) for i in range(rdim)]
    lhs = quad(Gi,rv)
    s2 = sum(x*x for x in rv)
    ss = sum(rv)
    rhs = Fraction(2,4)*(s2 - ss*ss/Fraction(n+1,1))
    assert lhs == rhs

    # Eigenvalue comparison:
    # Q=s2-ss^2/(n+1), with 2/(n+1)*s2 <= Q <= s2.
    Q = s2 - ss*ss/Fraction(n+1,1)
    assert Q <= s2
    assert Q >= Fraction(2,n+1)*s2

    # Abstract reflection-defect normalization:
    # choose rational q and define epsilon so that
    # |a_perp|^2=(q-1)^2 epsilon=Q*2/L^2.
    q = Fraction(3,2)
    aperp2 = Fraction(2,4)*Q
    eps = aperp2 / ((q-1)*(q-1))
    reconstructed_Q = Fraction(4,2)*(q-1)*(q-1)*eps
    assert reconstructed_Q == Q

print("VERIFY_OK")
print("dimensions=3..80")
print("gram_inverse=exact_rational")
print("quadratic_identity=exact_rational")
print("eigenvalue_bounds=exact_rational")
