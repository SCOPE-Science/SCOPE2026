# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Triviality of the single-slide wall-crossed Floer chart in monotone dP1

## Setting

Let X1 be CP^2 blown up at one point with its monotone symplectic form.
Its smooth toric fan can be taken as the rays (1,0), (0,1), (-1,-1), (0,-1),
with monotone moment polytope

  Q = {(u,v) : u >= -1, v >= -1, u+v <= 1, v <= 1}
    = conv{(-1,-1), (2,-1), (0,1), (-1,1)},

every facet at affine distance 1 from the origin. The toric monotone fibre
L0 at the origin bounds four Maslov-index-2 disks, one per facet, with
boundary classes given by the ray generators. Its disk potential is

  W0(x,y) = x + y + 1/(xy) + 1/y.

## Log-critical scheme of the toric chart

The rank-one local systems with nonvanishing pearl Floer homology are the
critical points of W0 on (C*)^2. The logarithmic derivatives are

  x dW0/dx = x - 1/(xy),  y dW0/dy = y - 1/y - 1/(xy).

The exact lex Groebner basis of the numerators is

  {xs - 4ys^6 - 2ys^5 + 7ys^4 + 7ys^3, ys^7 - 2ys^5 - ys^4 + ys^3},

and on (C*)^2 the factor ys^3 is a unit, leaving the quartic
ys^4 - 2ys^2 - ys + 1 = 0: exactly four critical points, matching
rank H*(dP1) = 4. Numerically the critical values (eigenvalues of c1* on
quantum cohomology) are approximately

  3.799605,  -0.330500,  -2.234552 + 1.940705i,  -2.234552 - 1.940705i,

all with nonzero log-Hessian determinant (table in verification_output.txt).

## Single nodal-slide mutation

Consider the almost-toric partial hull obtained by a single nodal slide with
width vector w = (0,1) and wall factor f = 1+x. Decomposing
W0 = P_1 + P_0 + P_{-1} with P_1 = y, P_0 = x, P_{-1} = (1+x)/(xy) and
changing charts via X = x, Y = y/(1+x) gives the wall-crossed potential

  We(X,Y) = X + Y + XY + 1/(XY),

whose Newton quadrilateral conv{(1,0),(0,1),(1,1),(-1,-1)} has the same
normalized volume 4 as the toric quadrilateral.

## Theorem (triviality)

We(X,Y) = W0(X, 1/(XY)) holds as an exact identity of Laurent polynomials.
The exponent map (a,b) -> (a-b,-b) has matrix [[1,-1],[0,-1]] of determinant
-1, hence is an automorphism of (C*)^2 (torus reparametrization). The exact
lex Groebner basis of the We log-critical system is {xs - ys, ys^5 + ys^4 - ys},
i.e. x = y and t^4 + t^3 - 1 = 0. All four critical values and all four
log-Hessian determinants coincide with those of W0 (max paired deviation
2.2e-16). Consequently this mutated chart is Floer-theoretically identical to
the toric chart up to relabeling of local systems: it defines no exotic fibre
and yields no new pearl or mixed-link displacement obstruction.

## Consequence for the link question

Naive five-term ansatze that keep both 1/y and a new wall term (e.g.
x + x/y + y + 1/y + 1/(xy)) have Newton normalized volume 5 and critical
values disjoint from the dP1 spectrum (e.g. 4.2148 versus the spectrum above),
violating the closed-open eigenvalue constraint, and are therefore ruled out
as wall-crossings. Hence no exotic Floer chart — and no joint-displacement
obstruction built from one — arises within the prescribed single-slide
non-triangular setup. A genuinely exotic fibre would require iterated
mutations or a triangular Vianna-type hull, outside the stated construction.

## Verification

All claims are reproduced by output/artifacts/verify_mutation.py; see
output/artifacts/verification_output.txt for the exact identities, both
Groebner bases, and the full numerical tables.
