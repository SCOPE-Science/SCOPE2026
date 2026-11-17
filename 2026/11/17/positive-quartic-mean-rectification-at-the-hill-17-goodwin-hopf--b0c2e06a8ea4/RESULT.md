# Positive quartic mean rectification at the Hill-17 Goodwin Hopf point

## Finding

In the equal-decay Goodwin oscillator with Hill exponent \(17\), the order-two average-concentration displacement vanishes at the Hopf onset, but the first nonzero shift is a **positive fourth-order term**. Specifically, if \(e_*=(8/9)^{1/17}\), \(K_*=17e_*/9\), \(E(K)>0\) solves \(K=E(K)(1+E(K)^{17})\), and \(z_K(t)\) denotes the attracting small oscillation born for \(K>K_*\), then, with its **half peak-to-trough amplitude** \(A(K)=(\max_t z_K(t)-\min_t z_K(t))/2\),

\[
\boxed{\frac{1}{T(K)}\int_0^{T(K)}z_K(t)\,dt-E(K)=\frac{60}{e_*^3}A(K)^4+o(A(K)^4).}
\]

The equivalent gain-parameter version is

\[
\boxed{\frac{1}{T(K)}\int_0^{T(K)}z_K(t)\,dt-E(K)=\frac{15}{289e_*}(K-K_*)^2+o((K-K_*)^2).}
\]

Thus quadratic rectification degeneracy does **not** imply an unbiased oscillatory mean. The strict positive sign is robust throughout a sufficiently small supercritical interval.

## Assumptions and scope

Consider the autonomous smooth system on strictly positive concentrations

\[
\dot x=\frac{K}{1+z^{17}}-x,\qquad \dot y=x-y,\qquad \dot z=y-z,\qquad K>0.
\]

All degradation rates are one, the feedback gain \(K\) is constant, and the Hill exponent is exactly the integer \(17\). The equilibrium is \((E,E,E)\), where \(E=E(K)>0\) is the unique root of \(K=E(1+E^{17})\). The claim concerns the unique sufficiently small periodic-orbit branch near the Hopf point, up to time translation; it is not an assertion about all large-gain cycles or other nonlinearities. Averages are physical-time averages over a complete period, not midpoints of extrema. All limits are as \(K\downarrow K_*\) from above. The normalized value \(e_*\) is fixed and positive.

## Proof

**1. The Hopf point and its direction.** Define \(f_K(z)=K/(1+z^{17})\). At an equilibrium \((E,E,E)\), the linear characteristic equation is \((\lambda+1)^3=f_K'(E)\), and the equilibrium identity gives

\[
f_K'(E)=-\frac{17E^{17}}{1+E^{17}}.
\]

At \(e_*^{17}=8/9\), this slope equals \(-8\), so the spectrum consists of \(-3\) and \(\pm i\sqrt3\). The derivative of the real part of either critical eigenvalue with respect to gain at \(K_*\) is \(3/(17e_*)>0\), since \(dE/dK=1/17\) there. The Hopf crossing is transversal.

Use the eigenvector \(q=((1+i\sqrt3)^2,1+i\sqrt3,1)^{\mathsf T}\), normalized to give terminal-component amplitude one, and the conjugated first component \(\overline p_1=(-1-i\sqrt3)/24\) of the normalized adjoint eigenvector. The feedback Taylor derivatives at the Hopf point are

\[
f_{K_*}'(e_*)=-8,\qquad f_{K_*}''(e_*)=0,\qquad
f_{K_*}'''(e_*)=\frac{1152}{e_*^2},\qquad
f_{K_*}^{(4)}(e_*)=-\frac{2304}{e_*^3}.
\]

Because the only nonzero multilinear cubic component acts in the first equation and the quadratic part vanishes, the standard Hopf cubic complex coefficient is \(G=\overline p_1 f_{K_*}'''(e_*)=(-48-48i\sqrt3)/e_*^2\). With the convention \(\ell_1=\operatorname{Re}G/(2\sqrt3)\),

\[
\ell_1=-\frac{8\sqrt3}{e_*^2}<0.
\]

The nondegenerate Hopf theorem therefore gives a unique (locally, up to phase) orbitally asymptotically stable branch for all sufficiently small \(K>K_*\), consisting of strictly positive cycles.

**2. Amplitude and moving equilibrium.** Let \(u(t)=z_K(t)-E(K)\) and \(A=A(K)\). Eliminating the first two stages yields the exact third-order scalar equation

\[
(D+1)^3u=f_K(E+u)-E,\quad D=d/dt.
\]

At exponent \(17\), vanishing of the quadratic Taylor derivative at the critical point means that the order-two Fourier correction is zero (after the usual phase and amplitude normalization); hence

\[
u(t)=A\cos(\omega(K)t+\phi)+O(A^3),\qquad \omega(K)=\sqrt3+O(A^2),
\]

where the remainder is uniform over the rescaled period. The first-harmonic cubic solvability condition, or equivalently the real part of the Hopf radial normal form, gives

\[
E(K)-e_*=\frac{2}{e_*}A^2+O(A^4),\qquad
K-K_*=\frac{34}{e_*}A^2+O(A^4).
\]

For clarity, the radial equation is \(\dot r=[3(K-K_*)/(17e_*)+O((K-K_*)^2)]r+[-24/e_*^2+o(1)]r^3\), with \(A=2r+O(r^3)\). Consequently \(A^2=e_*(K-K_*)/34+O((K-K_*)^2)\). These expansions depend only on the local Hopf normal form, not finite-time simulations.

**3. The surviving quartic mean.** Write \(\delta=\langle u\rangle\), with \(\langle\cdot\rangle\) the average over one complete period. The exact scalar equation averaged over a period gives \(\langle u\rangle=\langle f_K(E+u)-f_K(E)\rangle\), and Taylor expansion yields

\[
(1-f_K'(E))\delta=\frac{f_K''(E)}2\langle u^2\rangle+\frac{f_K'''(E)}6\langle u^3\rangle+\frac{f_K^{(4)}(E)}{24}\langle u^4\rangle+O(A^5).
\]

Here \(f_K''(E)=\frac{2304}{e_*^3}A^2+O(A^4)\) by Step 2, while \(1-f_K'(E)=9+O(A^2)\). The absence of an order-two harmonic correction implies

\[
\langle u^2\rangle=\tfrac12 A^2+O(A^4),\quad
\langle u^3\rangle=O(A^5),\quad
\langle u^4\rangle=\tfrac38 A^4+O(A^6).
\]

The terms of order \(A^4\) on the right side are \(576A^4/e_*^3\) from the moving-equilibrium quadratic coefficient and \(-36A^4/e_*^3\) from the intrinsic fourth derivative. Dividing their sum by \(9\) yields

\[
\delta=\frac{576-36}{9e_*^3}A^4+o(A^4)=\frac{60}{e_*^3}A^4+o(A^4).
\]

Substituting \(A^2=e_*(K-K_*)/34+O((K-K_*)^2)\) proves the gain formulation \(60/(34^2e_*)=15/(289e_*)\). Notice that the two quartic contributions have **opposite** signs, so the positivity is not justified by a naive curvature argument at the Hopf point.

## Verification

The companion `goodwin_quartic_checker.py` checks exact rational feedback derivatives in the dimensionless variable \(z/e_*\), the Hopf eigensystem, normalized cubic coefficient, equilibrium-amplitude solvability relation, and the quartic mean coefficient. Run:

```bash
python goodwin_quartic_checker.py
python goodwin_quartic_checker.py --numeric
```

The optional numerical mode integrates full trajectories, locates upward crossings of the moving equilibrium, averages over exactly 20 complete cycles, and compares the fourth-order prediction at three small positive gain detunings. Exact symbolic checks establish algebraic identities; numerical tests are corroboration and do not prove existence, stability, or the asymptotic error terms. The proof above supplies the infinite limiting claims.

## Relationship to prior work

Katz, Giordano, and Margaliot (first public 2024-06-29, arXiv:2407.00461) establish attracting periodic behavior in strongly 2-cooperative systems, with a Goodwin case study; they do not compute the terminal-concentration rectification coefficient. Woller, Gonze, and Erneux (2014) derive the Goodwin near-Hopf amplitude equation; their Appendix A equations (A.10)–(A.20) give the **known order-two** zero-mean harmonic coefficient proportional to \(m-17\). In particular, the quadratic shift vanishes at \(m=17\): that cancellation is **not claimed as new**. Their displayed derivation proceeds through order three and does not state the order-four, strictly positive mean displacement above. The result here addresses precisely what replaces the vanishing quadratic term, with a new nonzero coefficient \(60/e_*^3\). A 2013 strong-feedback analysis and the broader Goodwin literature address other regimes; residual priority risk from equivalent unpublished or unindexed perturbation calculations remains.

## Limitations

The asymptotic holds only near the first Hopf threshold at fixed exponent \(17\) and equal unit decay rates. The statement is about the unique local orbit branch, not global uniqueness, arbitrary relative decay rates, or a bound valid far from threshold. Numerical tests cannot establish the infinite-order error estimates. The original contribution of the explicit quartic coefficient is assessed against inspected accessible literature and is not an independent publication-priority determination. Independent external mathematical audit has not been performed.

## References

1. R. Katz, G. Giordano, and M. Margaliot, *Existence of attracting periodic orbits in 3-dimensional strongly 2-cooperative systems*, arXiv:2407.00461, first publicly posted 2024-06-29. https://arxiv.org/abs/2407.00461
2. A. Woller, D. Gonze, and T. Erneux, *The Goodwin model revisited: Hopf bifurcation, limit-cycle, and periodic entrainment*, Physical Biology 11 (2014), 045002; DOI 10.1088/1478-3975/11/4/045002. Appendix A, especially (A.10)–(A.20). https://doi.org/10.1088/1478-3975/11/4/045002
3. A. Woller, D. Gonze, and T. Erneux, *Strong feedback limit of the Goodwin circadian oscillator*, Physical Review E 87 (2013), 032722; DOI 10.1103/PhysRevE.87.032722. https://doi.org/10.1103/PhysRevE.87.032722
