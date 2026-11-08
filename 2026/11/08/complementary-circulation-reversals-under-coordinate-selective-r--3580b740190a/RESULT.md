# Complementary circulation reversals under coordinate-selective resetting of a Brownian gyrator

## Finding

A two-temperature harmonic Brownian gyrator with Poisson resetting of only its first coordinate has two natural, experimentally distinct stationary circulation observables. Its **continuous-path signed area rate** and the infinitesimal **antisymmetric position-lag rate** have disjoint reversal regimes; in particular, their signs are opposite for every positive resetting rate when the two bath diffusivities are equal.

Write \(S=ab-c^2>0\) and
\[
\Delta_r=b(2a+r)(a+b+r)-c^2[2(a+b)+r]>0.
\]
For stationary positions \((X_t,Y_t)\), define
\[
J_{\mathrm{cont}}=\lim_{T\to\infty}\frac1T\mathbb E\!\left[\int_0^T X_t\circ\mathrm dY_t^{\mathrm{cont}}-Y_t\circ\mathrm dX_t^{\mathrm{cont}}\right],
\qquad
J_{\mathrm{lag}}=\lim_{h\downarrow0}\frac{\mathbb E[X_0Y_h-Y_0X_h]}h.
\]
Here the continuous increments omit the instantaneous coordinate-reset jumps; neither quantity claims to count topological windings. Both limits exist and satisfy
\[
\boxed{J_{\mathrm{cont}}=\frac{c}{\Delta_r}\left[4(D_x-D_y)S+2r\{bD_x-(a+b)D_y\}-D_yr^2\right]},
\]
\[
\boxed{J_{\mathrm{lag}}=\frac{2c}{\Delta_r}\left[2(D_x-D_y)S+br(2D_x-D_y)\right]}.
\]
The complete sign classification for positive \(r\) is:

* If \(D_x>D_y\), \(J_{\mathrm{cont}}\) changes **once**, from positive to negative, at
\[
r_{\mathrm{cont}}=\frac{bD_x-(a+b)D_y+\sqrt{[bD_x-(a+b)D_y]^2+4D_y(D_x-D_y)S}}{D_y},
\]
  while \(J_{\mathrm{lag}}>0\) at every positive resetting rate.
* If \(D_x=D_y\), then \(J_{\mathrm{cont}}<0<J_{\mathrm{lag}}\) for all \(r>0\); both are zero at \(r=0\).
* If \(D_y/2<D_x<D_y\), then \(J_{\mathrm{cont}}<0\) for all \(r\ge0\), whereas \(J_{\mathrm{lag}}\) changes **once**, from negative to positive, at
\[
r_{\mathrm{lag}}=\frac{2(D_y-D_x)S}{b(2D_x-D_y)}.
\]
* If \(D_x\le D_y/2\), both rates are strictly negative at every finite \(r\ge0\).

The sign of the lag observable actually holds at **every positive lag**, not merely in its derivative at zero. Put
\[
m=(a+b+r)/2,\qquad \eta=\sqrt{c^2+(a+r-b)^2/4}.
\]
Then, for each \(t>0\),
\[
\boxed{\mathbb E[X_0Y_t-Y_0X_t]=J_{\mathrm{lag}}e^{-mt}\frac{\sinh(\eta t)}{\eta}.}
\]
Consequently the finite-lag antisymmetry changes sign at exactly the same rate as \(J_{\mathrm{lag}}\), independently of the positive observation lag.

## Assumptions and scope

Fix \(a,b,c,D_x,D_y>0\) with \(ab>c^2\) and \(r\ge0\). Between jumps let
\[
\mathrm dX_t=(-aX_t+cY_t)\,\mathrm dt+\sqrt{2D_x}\,\mathrm dB_t^x,\qquad
\mathrm dY_t=(cX_t-bY_t)\,\mathrm dt+\sqrt{2D_y}\,\mathrm dB_t^y,
\]
where the Brownian motions are independent. Independent Poisson times of rate \(r\) apply the instantaneous map \((X,Y)\mapsto(0,Y)\). At \(r=0\) no jumps occur. All expectations refer to the unique stationary process. A coordinatewise reset is not a reset of the entire two-dimensional state, and the physical interpretation of its instantaneous jump is not specified; the lag observable is defined solely by measured positions.

The continuous area rate counts only the drift and continuous Brownian increments and is **not** the signed area of a path completed by a prescribed interpolation of reset jumps. For each fixed finite \(r\), the required stationary moments are finite.

## Proof

**1. Stationarity and moments.** Let \(H=\begin{pmatrix}a&-c\\-c&b\end{pmatrix}\). Its smallest eigenvalue \(\lambda>0\), since \(ab>c^2\). Couple two solutions with the same Brownian noises and Poisson resets. Their difference contracts by at least \(e^{-\lambda t}\) between resets, and each reset applies the nonexpansive orthogonal projection \((u,v)\mapsto(0,v)\). Thus their distance contracts by at least \(e^{-\lambda t}\). The quadratic generator drift is
\[
\mathcal L(X^2+Y^2)=-2(X,Y)H(X,Y)^{\mathsf T}+2(D_x+D_y)-rX^2,
\]
which gives uniform quadratic moment bounds. The usual pullback/synchronous coupling construction yields a unique stationary law. Higher polynomial moments exist by the same dissipative Lyapunov argument. Symmetry and the contracting first-moment equation give zero stationary means.

**2. Stationary covariance.** Write \(u=\mathbb E[X^2]\), \(v=\mathbb E[Y^2]\), and \(z=\mathbb E[XY]\). Applying the full drift–diffusion–jump generator to \(X^2,Y^2,XY\) yields
\[
(2a+r)u-2cz=2D_x,\quad 2bv-2cz=2D_y,\quad (a+b+r)z=c(u+v).
\]
The determinant of this linear system is \(2\Delta_r\). Explicit elimination gives
\[
u=\frac{2\{D_x[b(a+b+r)-c^2]+D_yc^2\}}{\Delta_r},
\]
\[
v=\frac{2D_xc^2+D_y[(2a+r)(a+b+r)-2c^2]}{\Delta_r},
\qquad z=\frac{c[2bD_x+(2a+r)D_y]}{\Delta_r}.
\]
The denominator is positive: its constant term as a polynomial in \(r\) is \(2(a+b)S\), its linear coefficient is \(b(3a+b)-c^2>0\), and its quadratic coefficient is \(b>0\). In particular, \(z>0\).

**3. Two circulating observables.** The continuous Stratonovich contributions have zero noise expectation because the driving Brownian motions are independent, so
\[
J_{\mathrm{cont}}=c(u-v)+(a-b)z.
\]
For the time-lag observable, the full generator acts on coordinates as \(\mathcal LX=-(a+r)X+cY\) and \(\mathcal LY=cX-bY\). Hence
\[
J_{\mathrm{lag}}=c(u-v)+(a+r-b)z
=J_{\mathrm{cont}}+rz.
\]
Substituting the preceding explicit \(u,v,z\) produces the two boxed rational expressions. The difference is strictly positive when \(r>0\); it is a consequence of the unobserved instantaneous reset events in the continuous-area observable, not a Gaussian-noise correction.

**4. Sharp sign classification.** Since \(c/\Delta_r>0\), the sign of \(J_{\mathrm{cont}}\) is the sign of the quadratic
\[
P(r)=4(D_x-D_y)S+2r[bD_x-(a+b)D_y]-D_yr^2.
\]
If \(D_x>D_y\), its constant coefficient is positive and its leading coefficient negative, giving exactly one positive root (the two roots have opposite signs). Solving the quadratic gives \(r_{\mathrm{cont}}\). If \(D_x\le D_y\), both its constant term and its linear coefficient are nonpositive, with strict negativity for \(r>0\), and for \(D_x<D_y\) strict negativity already at zero.

The sign of \(J_{\mathrm{lag}}\) equals that of the affine function
\[
Q(r)=2(D_x-D_y)S+br(2D_x-D_y).
\]
If \(D_x\ge D_y\), it is positive for \(r>0\). If \(D_y/2<D_x<D_y\), it has exactly one positive zero, \(r_{\mathrm{lag}}\), and changes from negative to positive there. If \(D_x\le D_y/2\), both terms are nonpositive and the first strictly negative. These cases exhaust all positive diffusivity ratios.

**5. Every-lag formula.** Conditional first moments evolve under the symmetric positive-definite matrix
\[
B=\begin{pmatrix}a+r&-c\\-c&b\end{pmatrix}:
\qquad\mathbb E[(X_t,Y_t)^{\mathsf T}\mid X_0,Y_0]=e^{-Bt}(X_0,Y_0)^{\mathsf T}.
\]
Writing \(\Sigma=\begin{pmatrix}u&z\\z&v\end{pmatrix}\), stationary two-time covariance is \(\Sigma e^{-Bt}\) when the first observation is on the left. The \((1,2)\) minus \((2,1)\) element equals
\[
(u-v)(e^{-Bt})_{12}+z[(e^{-Bt})_{22}-(e^{-Bt})_{11}].
\]
The explicit symmetric matrix exponential gives \((e^{-Bt})_{12}=ce^{-mt}\sinh(\eta t)/\eta\) and \((e^{-Bt})_{22}-(e^{-Bt})_{11}=(a+r-b)e^{-mt}\sinh(\eta t)/\eta\). This proves the boxed identity. Its scalar multiplier is strictly positive at every \(t>0\), establishing lag-independent sign and uniqueness of the same transition.

## Verification

Run `python3 checker.py` with Python 3's standard library. The supplied `CHECKER_OUTPUT.txt` records 3,380 successful deterministic assertions. The checker uses exact rational Gaussian elimination of the moment system, separately evaluates the closed rational formulas and both observable definitions, tests the sign regimes, and independently computes the two-time antisymmetry with the explicit matrix exponential. These tests are finite diagnostics, not the proof of the all-parameter theorem; the proof is given above.

For an illustrative test take \(a=2,b=1,c=1/2,D_x=2,D_y=1\). The continuous-area current crosses at \(r_{\mathrm{cont}}=\sqrt8-1\), while every positive-lag antisymmetric covariance retains a positive sign for all \(r>0\). At equal diffusivities \(D_x=D_y\), the continuous and lag signs are always opposite for positive \(r\).

## Relationship to prior work

Olsen and Löwen (arXiv:2401.12685, first posted January 23, 2024) analyze resetting of a hidden coordinate and exact transport formulas, chiefly in spatially homogeneous position–velocity systems. Their full text explicitly relies on homogeneity of the non-reset variable, unlike the mutually coupled harmonic confinement here, and does not provide these two circulation reversal classifications. Cerasoli et al. (Physical Review E 106, 014137, 2022) develop a two-temperature Gaussian gyrator's spectral fingerprints without coordinate resetting; its reset-free model provides a baseline but not the \(r>0\) comparison. Abdoli and Sharma (arXiv:2010.02103, 2020) reset a coordinate in a magnetic-field-driven active system with a periodic transverse direction; its model, observables and flux mechanism differ from the harmonic two-temperature model here. The exact reset-free and overlapping-model comparisons, and the limitation of not excluding every unindexed related calculation, are further documented in `REVIEW.md` and `AUDIT.json`.

## Limitations

The classification assumes a symmetric positive-definite harmonic drift, independent strictly positive diffusivities, coordinate-one-only instantaneous Poisson resets to zero, and \(c>0\). Reversing the sign of \(c\) reverses the orientations but is not needed here. The result does not compute entropy production, optimal mechanical work, a winding number, or physical motion during a finite-duration return. The continuous-path and lag observables are deliberately distinct: neither is asserted to be an absolute, convention-free definition of rotation for instantaneous jumps. Publication priority is subject to independent literature checking beyond the named material.

## References

1. K. S. Olsen and H. Löwen, *Dynamics of inertial particles under velocity resetting*, arXiv:2401.12685 (first posted 2024-01-23), https://arxiv.org/abs/2401.12685.
2. S. Cerasoli, S. Ciliberto, E. Marinari, G. Oshanin, L. Peliti and L. Rondoni, *Spectral fingerprints of nonequilibrium dynamics: The case of a Brownian gyrator*, Physical Review E 106, 014137 (2022), https://doi.org/10.1103/PhysRevE.106.014137.
3. I. Abdoli and A. Sharma, *Stochastic resetting of active Brownian particles with Lorentz force*, arXiv:2010.02103 (first posted 2020-10-05), https://arxiv.org/abs/2010.02103.
4. K. S. Olsen and D. Gupta, *Thermodynamic work of partial resetting*, arXiv:2401.11919 (first posted 2024-01-22), https://arxiv.org/abs/2401.11919. This paper uses proportional resetting of a scalar coordinate rather than coordinate-selective resetting of a coupled pair.
