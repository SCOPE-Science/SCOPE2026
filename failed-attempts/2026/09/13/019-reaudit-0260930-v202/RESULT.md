# Small-cap L4 decoupling for the 3+1 cone at R^{-3/4} is false at exponent 1/16: a one-cap Knapp sliver forces R^{1/8}

## Context

Let Gamma = {(xi,|xi|) : 1 <= |xi| <= 2} be the truncated light cone in R^{3+1}
frequency space with surface measure dsigma and extension
Ef(x,t) = int e^{i(x.xi + t|xi|)} f(xi) dsigma(xi).
For R >= 2 partition Gamma into canonical caps theta of angular aperture
~R^{-1/2} and thickness ~R^{-1}, and refine each theta into small caps gamma
of angular aperture R^{-3/4} and the same thickness.
Let B_R be any ball of radius R in R^{3+1} with polynomial weight w_{B_R}.
Define D(R) as the least constant with

  ||Ef||_{L^4(B_R)} <= D(R) (sum_gamma ||Ef_gamma||_{L^4(w_{B_R})}^2)^{1/2}

for all f, where f_gamma = f 1_gamma.
The admitted target asked whether D(R) <= C_eps R^{1/16+eps} with 1/16 sharp.

## Definitions

- Canonical cap theta: angular aperture ~R^{-1/2}, thickness ~R^{-1}.
- Small cap gamma: angular aperture R^{-3/4}, thickness ~R^{-1}; each theta
  contains ~(R^{-1/2}/R^{-3/4})^2 ~ R^{1/2} small caps (purely angular count).
- Thin sliver: theta_sliver = {|xi'| <= r0 R^{-1/2}, s := xi_3 in
  [s0 - R^{-1} r1, s0 + R^{-1} r1]} with fixed small r0, r1 > 0, s0 = 3/2.
  Its surface measure is sigma ~ R^{-1} x R^{-1} = R^{-2}, and it lies in a
  single official canonical cap under every reading of "thickness".
- Tube T_R = {|x'| <= c1 R^{1/2}, |x_3+t| <= c1 R, |t| <= c1 R}, volume ~R^3.

## Result

Theorem (disproof): there exist c > 0 and smooth f_R supported in a single
canonical cap theta(R) such that

  ||Ef_R||_{L^4(B_R)} / (sum_gamma ||Ef_{R,gamma}||_{L^4(w_{B_R})}^2)^{1/2}
    >= c R^{1/8},  R -> infinity,

with B_R centred at the origin. In particular D(R) >= c R^{1/8}, so no bound
D(R) <= C_eps R^{1/16+eps} holds for every eps > 0, and 1/16 is not the sharp
exponent; the sharp exponent is at least 1/8. This is the familiar
N^{1/2-1/p} = N^{1/4} bunching law with N = R^{1/2} pieces.

## Proof / evidence

Take f = 1_{theta_sliver} smoothed at scale << R^{-1} (changes estimates by
<= 1%; equivalently a smooth bump 0 <= f <= 1 with f = 1 on half the sliver).

Lower bound ||Ef||_{L^4(B_R)} >= c R^{-5/4}. Write xi = (xi', s), use
|xi| = s + |xi'|^2/(2s) + O(|xi'|^4), and rescale xi' = R^{-1/2} zeta,
s = s0 + R^{-1} tau, dsigma = R^{-2} dzeta dtau (1+o(1)). Then
Ef(x,t) = R^{-2} e^{iPhi0(x,t)} I(a,b,c) + E_err where a = x'/R^{1/2},
b = (x_3+t)/R (up to constants), c = t/R, and
I(a,b,c) = int_{|zeta|<=r0} int_{|tau|<=r1}
  e^{i(a.zeta + b tau + c|zeta|^2/(2s0))} dzeta dtau,
a fixed oscillatory integral independent of R; the O(|xi'|^4 t) remainder has
phase <= C r0^4 R^{-2}|t| <= C c1 r0^4 on |t| <= c1 R, made << 1 by fixing
r0 > 0 small, with |E_err| <= (1/4) R^{-2} vol on T_R.
Since I(0,0,0) = vol = 2 pi r0^2 r1 > 0, continuity gives
|I(a,b,c)| >= vol/2 for |(a,b,c)| <= delta0 absolute. Hence
|Ef(x,t)| >= c0 R^{-2} on T_R with |T_R| ~ R^3; T_R fits in B(0,CR) and, after
fixing constants, in B_R. So
||Ef||_{L^4(B_R)} >= c0 R^{-2} (c R^3)^{1/4} = c R^{-5/4}.
The reproducible check artifacts/check_scaling.py confirms by midpoint
quadrature that I(0,0,0) = 2pi to 4 digits and min|I|/vol >= 0.89 over the box
|a_i|,|b|,|c| <= 1/2.

Upper bound per small cap ||Ef_gamma||_{L^4(w)} <= C R^{-13/8}. For gamma
meeting the sliver, sigma(gamma cap sliver) <= C R^{-3/2} x R^{-1} = CR^{-5/2}.
(a) L^infty: |Ef_gamma| <= sigma <= C R^{-5/2} uniformly.
(b) Local L^2: for fixed t, y -> Ef_gamma(y,t) is the Fourier transform of
e^{it|xi|} f_gamma dsigma, so Plancherel in y gives
int_{R^3} |Ef_gamma(y,t)|^2 dy = ||f_gamma||_{L^2(dsigma)}^2 <= C R^{-5/2}
uniformly in t; integrating |t| <= CR covering B_R gives C R^{-3/2}.
The same order holds for the weighted norm: the weight restricted to the
R-ball covering is summable against (1+|k|)^{-N} tails, and the TT* kernel
K(y,s) = int e^{i(y.xi+s|xi|)} |a_gamma|^2 dxi satisfies
|K| <= C_N sigma(gamma)(1 + R^{-3/4}|y'|+R^{-1}|(y_3,s)|)^{-N} by stationary
phase, whence int_{B_R}|K| <= C sigma(gamma) R and Schur's test gives the same
||Ef_gamma||_{L^2(B_R)}^2 <= C sigma R = C R^{-3/2}.
Interpolating L^4^4 <= L^infty^2 L^2(w)^2 gives
||Ef_gamma||^4 <= (CR^{-5/2})^2 CR^{-3/2} = CR^{-13/2}.

Ratio. Summing over the ~R^{1/2} small caps meeting the sliver,
sum_gamma ||Ef_gamma||^2 <= C R^{1/2} R^{-13/4} = C R^{-11/4}, so the
right-hand side is <= C R^{-11/8} while the left is >= c R^{-5/4}; hence
D(R) >= c R^{-5/4}/R^{-11/8} = c' R^{1/8}. Since R^{1/8}/R^{1/16} -> infinity,
the claimed bound fails (e.g. for eps < 1/32, hence for "every eps").

## Limitations

Disproves the stated upper bound via D(R) >= c R^{1/8} but does not determine
the optimal exponent; the matching upper bound D(R) <= C_eps R^{1/8+eps} is
standard flat-regime decoupling (Bourgain-Demeter flat case / Cauchy-Schwarz)
and is cited, not proved. Constants c, C are not tracked. Smoothing of the
indicator at scale << R^{-1} is asserted to change estimates by <= 1%.

## Reproducibility

Run python3 artifacts/check_scaling.py: verifies rescaled coherence
min|I|/vol = 0.899 over the coherence box and exponent arithmetic
N = R^{1/2}, N^{1/4} = R^{1/8} vs claimed R^{1/16} at R = 2^8, 2^16, 2^24.
Full self-contained proof is in this file; no external data needed.

## References

- Bourgain-Demeter, decoupling for the cone; flat small-cap decoupling gives
  N^{1/2-1/p} loss in the flat regime.
- Demeter-Guth-Wang, Small cap decouplings (arXiv:1908.09166): parabola,
  moment curve, square-like caps for the 2D cone (distinct scale/dimension).
- Maldague-Guth, Amplitude dependent wave envelope estimates for the cone in
  R^3 (arXiv:2206.01093): sharp small-cap for the cone in R^3 (2+1 cone),
  distinct from the R^{3+1} light cone treated here.
- Fu-Guth-Maldague, sharp superlevel/small-cap for the parabola.
- Tao, lecture notes on cone restriction/Knapp example.
