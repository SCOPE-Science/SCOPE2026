import sympy as sp
x,y=sp.symbols('x y')
def degpair(num,den):
    num=sp.expand(num); den=sp.expand(den)
    try:
        Pn=sp.Poly(num,x,y); dn=Pn.total_degree()
    except Exception: dn=None
    try:
        Pd=sp.Poly(den,x,y); dd=Pd.total_degree()
    except Exception: dd=None
    return dn,dd
Xn,Xd=x,sp.Integer(1); Yn,Yd=y,sp.Integer(1)
print("n=0:",degpair(Xn,Xd),degpair(Yn,Yd))
for n in range(1,7):
    nXn, nXd = sp.expand(Xd*Yd), sp.expand(Xn*Yn)
    nYn, nYd = sp.expand(Xn*Yd), sp.expand(Yd*Xd+Xn*Yn)
    # cancel gcd exactly via Poly quo
    for lab,(a,b) in (("X",(nXn,nXd)),("Y",(nYn,nYd))):
        Pa,Pb=sp.Poly(a,x,y),sp.Poly(b,x,y)
        g=sp.gcd(Pa,Pb)
        if g is not None and not g.is_number:
            qa,_=Pa.div(g); qb,_=Pb.div(g)
            a,b=qa.as_expr(),qb.as_expr()
        if lab=="X": Xn,Xd=a,b
        else: Yn,Yd=a,b
    print(f"n={n}: X{degpair(Xn,Xd)} Y{degpair(Yn,Yd)}")
    # print gcd degree
