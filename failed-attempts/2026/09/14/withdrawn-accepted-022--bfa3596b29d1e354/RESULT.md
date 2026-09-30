# Certified trapping obstruction block for a real quadratic Cremona family

## Context

The admitted target asks for a maximal-versus-trapped real entropy dichotomy with
uniform gap for real quadratic plane Cremona maps with proper one-real plus
conjugate-pair base points. While pursuing that target, an explicit diagonal
subfamily collapsed to an attracting regime instead of chaos. That attracting
structure is converted here into a fully proved horn-(B)-type obstruction block:
certified complex dynamical degree plus a certified forward-invariant real
trapping region with uniform contraction over an open parameter set.

## Definitions

Work in homogeneous coordinates `[X:Y:Z]` on P2 and the affine chart `X = 1`
with coordinates `(y, z)`. Define

sigma0[X:Y:Z] = [Y^2+Z^2 : XY : XZ],

and for real parameter `a`, `L_a[x:y:z] = [x : 2y+ax : z]` (det = 2, a projective
automorphism). Set `f_a = L_a o sigma0`. In the affine chart:

f_a(y,z) = (a + 2y/(y^2+z^2), z/(y^2+z^2)), N := y^2+z^2.  (1)

Let `S' = {(y,z) : y >= 2.9, |z| <= 0.2}` and `a in [2.9, 3.1]`.

## Result

There exists an explicit real quadratic plane Cremona family `f_a = L_a o sigma0`
with proper base points `[1:0:0]` (real) plus `[0:1:i],[0:1:-i]` (conjugate pair)
such that for every `a` in the open real parameter interval `(2.9, 3.1)`:

(i) `f_a` is algebraically stable with `deg(f_a^n) = 2^n` for all `n >= 1`,
hence complex dynamical degree `lambda = 2`.

(ii) The strip `S'` in the `X = 1` chart is forward invariant under `f_a`,
disjoint from the indeterminacy point `(0,0)`, contains a unique sink fixed
point, and `f_a` is a uniform contraction on `S'` with Frobenius-norm bound
`sqrt(13)/8.41 < 0.43`, so the trapped block contributes zero real entropy.

This is a fully certified real trapping-region obstruction of exactly the kind
named in horn (B) of the target, over an open parameter set.

## Proof / evidence

Proposition A: sigma0 is involutive quadratic Cremona
(`sigma0 o sigma0 = X(Y^2+Z^2) Id`), with base locus exactly the three proper
points above and contracted lines `<p2,p3>={X=0} -> [1:0:0]`,
`<p1,p2>={Z-iY=0} -> [0:1:i]`, `<p1,p3>={Z+iY=0} -> [0:1:-i]`,
by direct expansion and solving `XY = XZ = 0`, `Y^2+Z^2 = 0`.

Proposition B: the contracted values of `f_a` are `q1 = [1:a:0]`,
`q2 = [0:2:i]`, `q3 = [0:2:-i]`, none a base point. Their images land on the
`z = 0` line at affine `y = a`: `s([0:2:i]) = [3:0:0]`, so
`f_a(q2) = [1:a:0]`; `f_a(q1)` is affine `(a+2/a, 0)`. On `z = 0` the dynamics
is `g(y) = a+2/y`, and the ray `y >= 2.9` is forward invariant
(`g(y) > a >= 2.9`). Hence all forward orbits of contracted values stay on the
positive real `z = 0` ray, never hitting `p1 = (0,0)` and, being real, never the
nonreal `p2, p3`. By the orbit-avoidance criterion, no degree drop ever occurs.

Proposition C: for `(y,z)` in `S'`, `N >= 8.41`, so
`|z'| = |z|/N <= 0.2/8.41 < 0.024 < 0.2` and `y' = a+2y/N > a >= 2.9`,
`y' <= a+2/y <= 3.1+2/2.9 < 3.8`. Hence `f_a(S')` is contained in `S'`, far from
`(0,0)`. The Jacobian entries `2(z^2-y^2)/N^2, -4yz/N^2, -2yz/N^2,
(y^2-z^2)/N^2` satisfy `|2(y^2-z^2)| <= 2N`, `|4yz| <= 2N`, `|2yz| <= N`, so the
Frobenius norm is at most `sqrt(4+4+1)/N = sqrt(13)/N <= sqrt(13)/8.41 < 0.43`.
A uniform contraction of a closed set has a unique fixed point attracting
everything in the set; all orbits in `S'` converge to it, so entropy on `S'`
is zero. The sink at `y(a)* = (a+sqrt(a^2+8))/2` has multipliers bounded by
0.16 in absolute value.

All steps are verified by exact integer/Fraction/sympy arithmetic in
`artifacts/stability_proof.py` (9 checks pass), independently re-verified with
rational interval arithmetic during audit.

## Limitations

Global `h_R(f_a) = 0` is NOT proved: a second real saddle fixed point exists
outside `S'`, and horseshoes outside `S'` are not ruled out. The uniform gap
`h_R <= log lambda - c` over an open set is NOT proved: only the entropy-zero
contribution of the trapped block is certified. Maximality (`h_R = log 2`)
and any golden-mean subshift are NOT claimed. The target dichotomy itself is
neither proved nor disproved.

## Reproducibility

Run `python3 artifacts/stability_proof.py`: 9 exact checks pass (involution
identity, base points, contracted lines, `det L_3 = 2`, degree/gcd,
contracted-value avoidance, first images, sink bounds, trapping-box
invariance). The interval estimates use only the rational bounds displayed
above and can be rechecked with `Fraction`s.

## References

E. Bedford, J. Diller, Real dynamics of a family of plane birational maps:
trapping regions and entropy zero, arXiv:math/0609113.
E. Bedford, J. Diller, Dynamics of a two parameter family of plane birational
maps: maximal entropy, arXiv:math/0505062.
E. Bedford, J. Diller, Real and complex dynamics of a family of birational
maps of the plane: the golden mean subshift, Amer. J. Math. 127 (2005).
J. Diller, research page, University of Notre Dame.
