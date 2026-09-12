import sympy as sp
def chart(dehom):
    vs = sp.symbols('y0 y1 y2')
    subs = {}
    k = 0
    for i in range(4):
        if i == dehom: subs[sp.Symbol(f'x{i}')] = 1
        else: subs[sp.Symbol(f'x{i}')] = vs[k]; k+=1
    x = [sp.Symbol(f'x{i}') for i in range(4)]
    F1 = x[0]*x[3]-x[1]*x[2]
    F2 = x[0]**2+x[1]**2+x[2]**2+x[3]**2-x[0]*x[3]-x[1]*x[2]
    G = sum(z**4 for z in x)
    tval = sp.Rational(1,100)
    H = (F1*F2 + tval*G).subs(subs)
    eqs = [H]+[sp.diff(H,v) for v in vs]
    Gb = sp.groebner(eqs, *vs, order='grlex')
    const = any(p.is_number for p in Gb.polys)
    print(f"chart x{dehom}=1: GB len {len(Gb.polys)}, contains const: {const}")
for j in [0,1,2]:
    chart(j)
