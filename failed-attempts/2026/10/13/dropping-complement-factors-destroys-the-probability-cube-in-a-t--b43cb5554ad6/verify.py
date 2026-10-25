from fractions import Fraction

def check_binary_identity():
    # Coefficients of u1,u2 in x*(u1-(x*u1+(1-x)*u2))
    # equal those in x*(1-x)*(u1-u2).
    for x in [Fraction(0),Fraction(1,7),Fraction(1,2),Fraction(6,7),Fraction(1)]:
        for u1,u2 in [(Fraction(3),Fraction(-2)),(Fraction(5,3),Fraction(7,4))]:
            lhs=x*(u1-(x*u1+(1-x)*u2))
            rhs=x*(1-x)*(u1-u2)
            assert lhs==rhs

def check_boundary_witness():
    Bg=Fraction(3); Cg=Fraction(5,2); Cweak=Fraction(3,2)
    reduced=Bg-Cg+Cweak
    assert reduced==2
    x=Fraction(1)
    unreduced=x*(1-x)*reduced
    assert unreduced==0

if __name__=='__main__':
    check_binary_identity(); check_boundary_witness(); print('VERIFY_OK')
