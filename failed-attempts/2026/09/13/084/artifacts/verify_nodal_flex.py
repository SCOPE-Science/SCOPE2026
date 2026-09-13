"""Verify explicit nodal cubic data for lane-1663 target.

N: F = y^2 z - x^3 - x^2 z in P^2.
Checks:
 1. deg N = 3 (anticanonical), irreducible (Eisenstein on z=1 chart).
 2. Unique singularity at P=[0:0:1], ordinary double point (node).
 3. Smooth flex Q=[0:1:0] with tangent line L={z=0} of contact order 3.
 4. Log GW virtual dimension: vdim = -1 + n = 1 for n=2 markings.
"""
import sympy as sp

x, y, z = sp.symbols('x y z')
F = y**2 * z - x**3 - x**2 * z
Fx, Fy, Fz = sp.diff(F, x), sp.diff(F, y), sp.diff(F, z)

# 1. Irreducibility: affine chart z=1, f in C[x][y], Eisenstein at prime (x+1)
xa = sp.Symbol('xa')
f = ya**2 - xa**3 - xa**2 if False else None
xa, ya = sp.symbols('xa ya')
f = ya**2 - xa**3 - xa**2
const = -xa**2 * (xa + 1)          # constant term in y
q, r = sp.div(const, xa + 1)       # divisible once
print('1a. const/(x+1) =', sp.expand(q), ' rem', r)
q2, r2 = sp.div(q, xa + 1)         # quotient not divisible again
print('1b. second division rem =', sp.expand(r2), '(nonzero => exactly one factor => Eisenstein applies)')
print('1c. leading coeff 1 not in (x+1); y-coeff 0 in (x+1) => f irreducible => N irreducible, deg 3')

# 2. Singular locus
sols = sp.solve([Fx, Fy, Fz], [x, y], dict=True)
print('2a. singular affine solutions (x,y) with z free:', sols)
H2 = sp.hessian(ya**2 - xa**3 - xa**2, (xa, ya))
print('2b. affine Hessian at node =', H2.subs({xa: 0, ya: 0}),
      ' det =', H2.det().subs({xa: 0, ya: 0}), '(nonzero => ordinary double point)')
print('2c. quadratic part =', sp.expand((ya**2 - xa**3 - xa**2) + xa**3),
      '= (y-x)(y+x): distinct tangents => node')

# 3. Flex line
print('3a. F(Q)=', F.subs({x: 0, y: 1, z: 0}), ' grad(Q)=',
      (Fx.subs({x: 0, y: 1, z: 0}), Fy.subs({x: 0, y: 1, z: 0}), Fz.subs({x: 0, y: 1, z: 0})),
      '(nonzero => Q smooth, tangent z=0)')
print('3b. F(x,1,0) =', sp.expand(F.subs({y: 1, z: 0})), '=> ord 3 contact of L={z=0} at Q')
H = sp.hessian(F, (x, y, z))
print('3c. det Hessian at Q =', H.det().subs({x: 0, y: 1, z: 0}), '(zero => flex)')
print('3d. beta.N for beta=[H]:', 3, '= maximal contact order at d=1')

# 4. Virtual dimension (log CY: c1(T(-log N)) = -(K+N) = 0)
for d in (1, 2, 3):
    vdim = (2 - 3) * (1 - 0) + 0 + 2   # (dimX-3)(1-g) + c1log.beta + n, n=2 markings
    print(f'4. d={d}: vdim={vdim}, minus point-insertion codim 2 => virtual degree {vdim - 2} => M_d = 0')
