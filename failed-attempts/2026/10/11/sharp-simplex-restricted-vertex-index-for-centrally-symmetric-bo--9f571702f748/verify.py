from fractions import Fraction


def lower_from_lambdas(lam):
    return sum((1-x)/x for x in lam)


# Deterministic exact barycentric checks.
for d in range(2, 13):
    m=d+1
    raw=[Fraction((i+1)*(d+2-i),1) for i in range(m)]
    s=sum(raw)
    lam=[x/s for x in raw]
    assert sum(lam)==1
    lhs=lower_from_lambdas(lam)
    alt=sum(1/x for x in lam)-m
    assert lhs==alt
    assert lhs >= d*(d+1)

    uniform=[Fraction(1,m)]*m
    assert lower_from_lambdas(uniform)==d*(d+1)

    # In centered-simplex barycentric-difference coordinates, p_i=(d+1)a_i
    # has coefficients d at i and -1 elsewhere.  The gauge of Delta-Delta
    # is the total positive part (equivalently half the l1 norm).
    for i in range(m):
        z=[Fraction(-1,1)]*m
        z[i]=Fraction(d,1)
        assert sum(z)==0
        gauge=sum(x for x in z if x>0)
        assert gauge==d
        assert sum(abs(x) for x in z)==2*d

        # -a_i/d is the average of the other d simplex vertices:
        coeff=[Fraction(0,1)]*m
        for j in range(m):
            if j!=i:
                coeff[j]=Fraction(1,d)
        assert sum(coeff)==1
        assert coeff[i]==0

print('VERIFY_OK')
print('barycentric_dimensions = 2..12')
print('reciprocal_bound = exact')
print('difference_body_sharpness = exact')
