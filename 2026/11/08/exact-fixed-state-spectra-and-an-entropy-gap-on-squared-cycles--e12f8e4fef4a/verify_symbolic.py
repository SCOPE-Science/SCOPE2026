"""Complement-block integer transfer certificate and spectral factors (SymPy)."""
import sympy as s
x = s.Symbol('x')
expect = {
'T-minority': x**4*(x-1)*(x+1)*(x**5-x**3-2*x**2-x-1)*(x**5+x**3+x-1),
'T-majority': x**8*(x-1)*(x+1)*(x**3-x**2-1)*(x**3-x**2+1),
'P-minority': x**2*(x-1)*(x**5-x**3-2*x**2-x-1),
'N-minority': x**2*(x+1)*(x**5+x**3+x-1),
'P-majority': x**4*(x-1)*(x**3-x**2-1),
'N-majority': x**4*(x+1)*(x**3-x**2+1),
}
for mode in ('minority','majority'):
    T = s.zeros(16)
    for k in range(16):
        b=[(k>>j)&1 for j in (3,2,1,0)]
        for c in (0,1):
            same = sum(v==b[2] for v in (b[0],b[1],b[3],c))
            if same<=2 if mode=='minority' else same>=2:
                T[k,(2*k+c)%16] += 1
    assert all(T[15-i,15-j]==T[i,j] for i in range(16) for j in range(16))
    P=s.Matrix(8,8,lambda i,j:T[i,j]+T[i,15-j])
    N=s.Matrix(8,8,lambda i,j:T[i,j]-T[i,15-j])
    for name,M in (('T',T),('P',P),('N',N)):
        polynomial=s.factor(M.charpoly(x).as_expr())
        assert s.expand(polynomial-expect[f'{name}-{mode}'])==0
        print(f'{mode} {name} det(XI-M): {polynomial}')
    for n in (5,6,7,8,9,10,11,12,13,14,15,16,25):
        tr=s.trace(T**n)
        # Newton power-sum via p_k - coefficient recurrence is implicit charpoly
        assert tr == s.trace(P**n)+s.trace(N**n)
    print('mode', mode, 'SPECTRAL_CERTIFIED')
p=x**5-x**3-2*x**2-x-1
a=x**3-x**2-1
rp=max(float(s.re(z)) for z in s.nroots(p) if abs(float(s.im(z)))<1e-12)
ra=max(float(s.re(z)) for z in s.nroots(a) if abs(float(s.im(z)))<1e-12)
print('minority_root', format(rp,'.12f'))
print('majority_root', format(ra,'.12f'))
print('root_ratio',format(rp/ra,'.12f'))
print('VERIFY_SYMBOLIC_OK')
