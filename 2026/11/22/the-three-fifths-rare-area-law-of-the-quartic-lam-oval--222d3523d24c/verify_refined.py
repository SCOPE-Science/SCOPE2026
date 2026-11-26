import mpmath as M

# Split speed at the diagonal, where x and y are interchanged by symmetry.
for digits in (30, 55):
    M.mp.dps = digits
    P = M.mpf
    L = 8*M.quad(lambda y: M.sqrt(1+y**6/(1-y**4)**P('1.5')),
                 [0, P(2)**(-P(1)/4)])
    # v=4z(1-z) transforms the gap integral to Euler's hypergeometric integral.
    a, b = P(2)/5, P(1)/10
    J = 2*4**(-a)*M.beta(a, P(1)/2)*M.hyp2f1(a,b,a+P(1)/2,P(1)/4)
    # Independent smooth quadrature: on each half set z=x**5/2.
    def integrand(x):
        z=x**5/2
        return 10*2**(-a)*x*(1-z)**(-P(3)/5)*(1-z+z*z)**(-b)
    assert abs(M.quad(integrand,[0,1])-J)<M.eps*64
    I = 2*8**(P(3)/5)*M.sqrt(M.pi/6)*M.gamma(b)/M.gamma(P(3)/5)*3**b*J
    print('L', M.nstr(L,25), 'I', M.nstr(I,25), 'C', M.nstr(4*I/L**3,25))
