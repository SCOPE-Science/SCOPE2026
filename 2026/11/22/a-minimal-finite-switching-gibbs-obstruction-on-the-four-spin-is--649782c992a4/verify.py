"""Exact symbolic and independent full-state verification of a kinetic-Ising claim.
Run: python verify.py (requires SymPy)."""
import sympy as sp

u, g = sp.symbols('u g', positive=True)
w = u + 1/u

def reduced(t):
    return sp.Matrix([
        [-4/t, t, 0, 0],
        [4/t, -t-2-1/t, 4, 4*t],
        [0, 2, -4, 0],
        [0, 1/t, 0, -4*t],
    ])

def joint_matrix(t, gamma):
    I = sp.eye(4)
    return sp.BlockMatrix([[reduced(t)-gamma*I, gamma*I],
                           [gamma*I, reduced(sp.Integer(1))-gamma*I]]).as_explicit()

def stationarity(Q):
    A = sp.Matrix(Q); A[-1, :] = sp.ones(1, Q.rows)
    rhs = sp.zeros(Q.rows, 1); rhs[-1] = 1
    return A.inv() * rhs

D = ((w+2)*(w+6)*g**3 + 2*(w+2)*(7*w+18)*g**2 +
     8*(7*w*w+14*w+24)*g+64*(w*w+4))
B_expr = (4*g**3*(w+2) + 2*g*g*(w*w+16*w+28) +
          2*g*(6*w*w+28*w+80) + 16*(w*w+12))/D
E_expr = (-4*(u-1/u)*(g+2)*((w+2)*g*g+(9*w+6)*g+16*w)/D)
H = (8*g**4*(w+2) + g**3*(7*w*w+108*w+140) +
     g*g*(78*w*w+424*w+504) +
     g*(256*w*w+512*w+1024) + 256*(w*w+4))
Delta_expr = 4*(g+2)*(w*w-4)*H / D**2

Q = joint_matrix(u, g)
p = stationarity(Q)
P = [sp.factor(p[k]+p[k+4]) for k in range(4)]
assert sp.cancel(P[2]-P[1]/2) == 0
assert sp.cancel(P[1]-B_expr) == 0
assert sp.cancel(4*(P[3]-P[0])-E_expr) == 0
assert sp.cancel(16*P[0]*P[3]-P[1]**2-Delta_expr) == 0
assert sp.cancel(sp.limit(g*Delta_expr, g, sp.oo) - 32*(w*w-4)/((w+2)*(w+6)**2)) == 0
assert sp.cancel(sp.limit(P[1],g,sp.oo)-4/(w+6)) == 0
assert sp.cancel(sp.limit(g*Delta_expr/P[1]**2,g,sp.oo)-2*(w-2)) == 0
print('PASS: symbolic quotient, positive-defect factorization, and high-rate limits')

# An entirely separate construction on all 2^4 spin configurations x 2 bath states.
def full_generator(U, G):
    Q = sp.zeros(32)
    for h in range(2):
        t = U if h == 0 else sp.Integer(1)
        for m in range(16):
            index = 16*h + m
            spins = [1 if (m >> k)&1 else -1 for k in range(4)]
            energy = -sum(spins[k]*spins[(k+1)%4] for k in range(4))
            for k in range(4):
                flip = m^(1<<k)
                spins2 = spins.copy();spins2[k]*=-1
                energy2 = -sum(spins2[j]*spins2[(j+1)%4] for j in range(4))
                rate = t**(-sp.Rational(energy2-energy,4))
                Q[16*h+flip,index] += rate
                Q[index,index] -= rate
            other=16*(1-h)+m
            Q[other,index] += G; Q[index,index] -= G
    return Q

def orbit(m):
    spins=[1 if (m>>k)&1 else -1 for k in range(4)]
    E=-sum(spins[k]*spins[(k+1)%4] for k in range(4))
    if E==-4:return 0
    if E==4:return 3
    if abs(sum(spins))==2:return 1
    return 2

for U,G in [(sp.Rational(2),sp.Rational(1,3)),
            (sp.Rational(3),sp.Rational(2)),
            (sp.Rational(5,2),sp.Rational(7))]:
    Qf=full_generator(U,G)
    assert all(sum(Qf[:,j]) == 0 for j in range(32))
    pf=stationarity(Qf)
    Pr=[sum(pf[16*h+m] for h in range(2) for m in range(16) if orbit(m)==k)
        for k in range(4)]
    for k in range(4):
        assert Pr[k] == P[k].subs({u:U,g:G})
    assert 16*Pr[0]*Pr[3] > Pr[1]**2
    print('PASS: full 32-state rational generator; u=%s, gamma=%s'%(U,G))
print('PASS: all exact mathematical checks')
