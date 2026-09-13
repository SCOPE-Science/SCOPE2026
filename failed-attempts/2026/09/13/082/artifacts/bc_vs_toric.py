# BC fibre wall-crossing / mutation computation for monotone tori in del Pezzo
# Framework: Vianna / Pascaleff-Tonkonog wall-crossing: if L is obtained from
# toric-descendant L0 by Lagrangian mutation along a disk of class [D] with
# boundary class v in H1(L0), with local coords x=z^v, W_new = mu_v(W_old).
# We test: starting from an 8-critical-point potential, can mutation REDUCE
# the number of (C*)^2 critical points? A mutation preserves #crit in (C*)^2
# when counted with multiplicity?? Actually mutation is a birational change of
# cluster chart: x' = x, y' = y*(1+x)^k style; # critical points in the torus
# chart is preserved (Jac is nonzero). Hmm — standard mutation preserves
# number of critical points in (C*)^2.
#
# Alternative distinguishing route: displacement energy / J-holomorphic
# "disk area spectrum"? Or second-order bulk-deformed potential?
# Let's numerically test the claim that ALL Laurent polys with given Newton
# polytope mutation class have same #crit. Take Bl2 example and mutate.
from sympy import symbols, diff, together, Poly, solve, resultant, N

def ncrit(W, x, y):
    Wx = diff(W, x); Wy = diff(W, y)
    numx, d = together(Wx).as_numer_denom()
    numy, d2 = together(Wy).as_numer_denom()
    ex = Poly(numx, x, y).as_expr(); ey = Poly(numy, x, y).as_expr()
    try:
        sols = solve([ex, ey], [x, y], dict=True)
        sols = [s for s in sols if abs(complex(N(s[x])))>1e-9 and abs(complex(N(s[y])))>1e-9]
        return len(sols), sols
    except Exception as e:
        return -1, str(e)[:200]

x, y = symbols('x y')
# Vianna-type: mutate W by x -> x, y -> y*(1+x): wall-crossing across disk in class x
W0 = x + y + 1/(x*y) + 1/x + 1/y   # 5 crits
print("W0 ncrit:", ncrit(W0, x, y)[0])
# mutation along v=(1,0) with k=1: substitute y -> y*(1+x)?? then multiply out Laurent
W1 = (x + y*(1+x) + 1/(x*y*(1+x)) + 1/x + 1/(y*(1+x)))
W1s = together(W1)
print("W1 =", W1s)
# W1 is rational, not Laurent; the "mutated potential" in new chart: need Laurent form
# Correct wall-crossing: W_new(x', y') has different expression; both charts share
# same critical values. So #crit preserved. Skip.
# Instead test:BC potential proposed in literature for exotic tori often
# has FEWER terms (narrower Newton polytope). E.g., Chekanov torus in CP2:
# W_Chek = y + (1+y)^2/(x*y^2)... has 3 crits? same as Clifford (3). Same count!
# So disproving via #crit alone may FAIL: mutation preserves count.
# Test Chekanov-type formula:
Wchek = y + (1+y)**2/(x*y**2) + (1+y)/y  # guess
print("Wchek ncrit:", ncrit(Wchek, x, y))
