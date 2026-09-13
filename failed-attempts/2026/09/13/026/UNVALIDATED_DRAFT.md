# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Codimension-three algebraic Sard containment for Cartan Abn(e) — DRAFT

## 1. Setup and claim

Let G be the free step-3 rank-2 nilpotent Lie group (Cartan group), dim G = 5,
with Lie algebra g = span{e1,...,e5} and nonzero brackets

  [e1,e2] = e3,  [e1,e3] = e4,  [e2,e3] = e5.

Let X1,...,X5 be the corresponding left-invariant frame and D = span{X1,X2}
the left-invariant rank-2 distribution. Fix exponential coordinates of the
first kind x in R^5 ~= G with e = 0.

**Theorem.** Let Abn(e) be the set of endpoints of nonconstant D-horizontal
abnormal curves from e. Then

  Abn(e) = { x in G : x3 = x4 = x5 = 0 },

i.e. the coordinate 2-plane P = exp(span{e1,e2}). In particular Abn(e) is
contained in the proper algebraic subvariety

  V = { x3 = 0, x4 = 0, x5 = 0 },

which has codimension 3 (>= 2, as required), and hence has 5-dimensional
Lebesgue measure zero. The required "explicit polynomial equations" and
"codimension at least 2" are satisfied with margin; the bound is sharp
(Abn(e) contains the whole plane, hence no subvariety of larger codimension
can contain it while the listed equations are each needed).

## 2. Left-invariant frame and horizontal equations

From the BCH formula at step 3 (verified symbolically in
`artifacts/cartan_abnormal.py`, `artifacts/verify_abnormal.py`), the
left-invariant frame is

  X1 = d1 - (x2/2) d3 - (x1 x2/12 + x3/2) d4 - (x2^2/12) d5,
  X2 = d2 + (x1/2) d3 + (x1^2/12) d4 + (x1 x2/12 - x3/2) d5,
  X3 = d3 + (x1/2) d4 + (x2/2) d5,  X4 = d4,  X5 = d5,

with brackets (as vector fields, patient sign) [X1,X2] = -X3,
[X1,X3] = -X4, [X2,X3] = -X5, all other pairs commuting; in particular X4, X5
are central and the nonzero structure constants agree with the abstract Lie
algebra up to the standard sign. Horizontal curves satisfy

  x1' = u1,  x2' = u2,
  x3' = (u2 x1 - u1 x2)/2 =: w/2,
  x4' = (x1 w)/12 - u1 x3/2,
  x5' = (x2 w)/12 - u2 x3/2,

where w := u2 x1 - u1 x2. These factorizations are verified symbolically.

## 3. Abnormal equations force collinear controls and x3 = 0

Let gamma(t) be D-horizontal with control u(t) = (u1,u2) in L^2 (or L^1_loc).
The endpoint map End: u |-> gamma(T) has differential at u given by the
linearized flow. A curve is abnormal iff there is a nonzero covector lambda(T)
annihilating im dEnd, equivalently a nontrivial absolutely continuous lift
h(t) = (h1,...,h5)(t), h(t) != 0 for the abnormal multiplier (nu = 0),
satisfying the Pontryagin conditions for the sub-Riemannian Hamiltonian
H = u1 h1 + u2 h2 maximized over u:

(1) h1(t) = <lambda(t), X1(gamma(t))> = 0 and h2(t) = 0 a.e.,
    (vanishing of the maximized Hamiltonian's u-gradient);
(2) h'(t) = -sum_i u_i(t) ad^*(Xi) h(t), i.e. in coordinates

    h1' =  u2 h3,   h2' = -u1 h3,   h3' = -(u1 h4 + u2 h5),
    h4' = 0,        h5' = 0

    (signs per the vector-field bracket convention; the zero set of the
    right-hand sides, which is all that matters, is convention-independent:
    the derivation uses only which structure constants are nonzero);
(3) (h1,h2,h3,h4,h5) is not identically zero; since h4,h5 are constant,
    write (h4,h5) = (a,b) in R^2.

From (2), a(t) = a, b(t) = b are constant. Differentiating h1 = h2 = 0 gives
u2 h3 = 0 and u1 h3 = 0 a.e. Two cases:

- Case A: h3 = 0 on a set of positive measure accumulating somewhere. Then
  h3' = 0 gives u(t) . (a,b) = 0 a.e. (with the sign convention above,
  h3' = -(u1 a + u2 b)). If (a,b) = (0,0) then h = 0 identically (since
  h1=h2=h3=0 and h4=h5=0), contradicting nontriviality. Hence (a,b) != (0,0)
  and u(t) is a.e. collinear with (-b,a): u(t) = alpha(t)(-b,a) for a scalar
  function alpha. Where h3 != 0, we have u = 0 a.e.; thus globally
  u(t) = alpha(t)(-b,a) a.e. for some scalar alpha in L^1_loc.

- Case B: h3 != 0 a.e. on some interval forces u = 0 there, contributing
  nothing to motion; the curve is a reparametrization of a Case-A motion on
  the remaining set.

Consequently every abnormal control is a.e. collinear: there are constants
(a,b) != (0,0) and scalar alpha with u1 = -alpha b, u2 = alpha a.
Nonconstancy of the curve forces alpha nonzero on a set of positive measure.

Then w = u2 x1 - u1 x2 = alpha(a x1 + b x2). Moreover x1, x2 evolve by
x1' = -alpha b, x2 = alpha a (up to constants), so d/dt(a x1 + b x2) = 0;
with x(0) = 0 one gets a x1(t) + b x2(t) = 0 for all t, hence w(t) = 0 for
all t. Then x3' = w/2 = 0 with x3(0) = 0 gives x3 = 0 identically along every
abnormal curve. Substituting x3 = w = 0 into the x4', x5' equations gives
x4' = x5' = 0, so x4 = x5 = 0 identically. Hence every abnormal endpoint lies
in P = {x3 = x4 = x5 = 0}.

Conversely, for any (v1,v2) in R^2 and any T, the constant-control horizontal
curve with u = (v1,v2) reaches (T v1, T v2, 0, 0, 0) (checked: x3' = x4' =
x5' = 0 along collinear rays in the symbolic script), and this curve is
abnormal: take h3 = 0, (a,b) = (-v2,v1) (or any nonzero orthogonal vector if
(v1,v2) = 0 is excluded — constant nonzero controls suffice to reach every
point of P), h1 = h2 = 0. Thus every point of P is an abnormal endpoint
(arising from a nonconstant curve unless the point is e itself). So

  Abn(e) = P \ {e}-qualification aside = P as a set including e's trivial
  limit; precisely, Abn(e) = P \ {e} union possibly e, and in any case
  Abn(e) subset P with P \ {e} subset Abn(e).

## 4. Sard conclusion

P is cut out by the three explicit polynomial (indeed coordinate) equations
x3 = x4 = x5 = 0, a proper algebraic subvariety of codimension 3 >= 2. Its
5-dimensional Lebesgue measure is zero. This proves the target claim
(containment in codimension >= 2 with explicit equations and measure-zero
consequence), and in fact determines Abn(e) exactly.

## 5. Sharpness and conventions

Each of the three equations is needed: projections of Abn(e) onto the
(x1,x2)-plane cover all of R^2. The codimension-3 statement implies the
required codimension-2 statement. The sign conventions for left- vs
right-invariant brackets affect only signs in the adjoint system, never the
zero sets used above; the symbolic scripts verify the exact identities
x3' = w/2 etc. and the collinear-ray invariance of P, so the argument is
reproducible. Standard references: Montgomery, _A Tour of Subriemannian
Geometries_; Agrachev–Barilari–Boscain, _A Comprehensive Introduction_;
Barilari et al. on the Cartan group and abnormal geodesics; the endpoint-map
Sard set-up is the usual Pontryagin/maximized-Hamiltonian one.

## 6. Boundary of the result

The result uses left-invariance and the free step-3 rank-2 structure (central
X4, X5 forcing constant (a,b) and collinearity). It does not extend
automatically to non-free quotients. No numerics beyond exact symbolic algebra
are used; limitations: abnormal minimizers vs. merely abnormal curves are not
distinguished (not required by the claim).
