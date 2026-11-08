# Nested fourth–sixth cumulant sign boundaries for a trapped direction-reversing active swimmer

## Finding
Consider the stationary planar active swimmer
\[
 d\mathbf X_t=(-\mu\mathbf X_t+v\,\sigma_t(\cos\theta_t,\sin\theta_t))\,dt+\sqrt{2D_{\mathrm t}}\,d\mathbf B_t,
 \qquad d\theta_t=\sqrt{2D_{\mathrm R}}\,dW_t,
\]
where the independent sign \(\sigma_t\in\{-1,+1\}\) reverses at Poisson rate \(\gamma\), and the translational and rotational Brownian motions are independent. Put \(d=D_{\mathrm R}/\mu>0\), \(g=\gamma/\mu\geq0\), and \(s=v/\mu>0\). For any unit direction \(e\), write \(c_j=\operatorname{cum}_j(e\cdot\mathbf X)/s^j\) for the stationary projected cumulants (the dependence on \(D_{\mathrm t}\) vanishes for \(j\geq3\)).

Define
\[
P_d(g)=116d^3+199d^2+98d+15-(32d^2+40d+8)g-(16d+12)g^2.
\]
The exact fourth and sixth cumulants are
\[
c_4=\frac{3(2g-7d-3)}{8(1+2d)(1+d+2g)^2(3+d+2g)}
\]
and
\[
c_6=\frac{15P_d(g)}{4(1+d)(1+2d)(1+d+2g)^3(3+d+2g)(5+d+2g)(3+9d+2g)}.
\]
For every \(d>0\), let \(g_6(d)\) be the unique positive zero of \(P_d\), and let \(g_4(d)=(7d+3)/2\). Then
\[
0<g_6(d)<g_4(d),
\]
with exactly three strict sign regimes as \(g\) increases: \((c_4,c_6)=(-,+)\) below \(g_6\), \((-,-)\) between \(g_6\) and \(g_4\), and \((+,-)\) above \(g_4\). At each crossing only its designated cumulant vanishes. On the entire previously known fourth-cumulant zero line,
\[
\left.c_6\right|_{g=g_4(d)}=-\frac{15(3d+1)}{1024(1+d)^2(1+2d)^3(8d+3)}<0.
\]
The signs and thresholds remain exactly unchanged for any independent isotropic translational Brownian diffusivity \(D_{\mathrm t}\geq0\). These are cumulant sign boundaries, not singularities of the stationary state or thermodynamic phase transitions.

## Assumptions and scope
All parameters are finite and satisfy \(\mu,v,D_{\mathrm R}>0\), \(\gamma,D_{\mathrm t}\geq0\). Orientation is considered modulo \(2\pi\), with a uniform invariant angle law; for \(D_{\mathrm R}>0\) the orientation process is ergodic and the contracting harmonic filter has a unique stationary position law. The independent translational Brownian noise, when present, only adds a Gaussian Ornstein–Uhlenbeck component. Cumulants are unstandardized cumulants of a one-dimensional projection, scaled by \((v/\mu)^j\). By rotational symmetry their value does not depend on the chosen unit direction.

## Proof
First take \(D_{\mathrm t}=0\). The composite heading angle \(\phi_t=\theta_t+\pi N_t\pmod{2\pi}\), where \(N_t\) is the Poisson reversal count, has Fourier generator eigenvalues \(-\{d n^2+g[1-(-1)^n]\}\) in time units \(\mu^{-1}\). In the same units put \(Z=(\mu/v)(X_1+iX_2)\), so \(\dot Z=-Z+e^{i\phi}\). Stationarity, boundedness \(|Z|\leq1\), and the generator applied to \(Z^p\overline Z^{\,q}e^{in\phi}\) imply the **finite triangular recurrence**
\[
[p+q+dn^2+g(1-(-1)^n)]M_{p,q,n}
=pM_{p-1,q,n+1}+qM_{p,q-1,n-1},
\]
where \(M_{p,q,n}=\mathbb E[Z^p\overline Z^{\,q}e^{in\phi}]\), \(M_{0,0,n}=\mathbf1_{n=0}\), and terms with negative exponents are absent. Every denominator at positive total degree is positive; induction determines every moment exactly. Application for \(p=q=1,2,3\) yields the radial moments \(R_j=\mathbb E|Z|^{2j}\):
\[
R_1=\frac1{1+d+2g},\qquad
R_2=\frac{4d+3}{(1+2d)(1+d+2g)(3+d+2g)},
\]
\[
R_3=\frac{3(36d^3+8d^2g+93d^2+18dg+68d+10g+15)}{(1+d)(1+2d)(1+d+2g)(3+d+2g)(5+d+2g)(3+9d+2g)}.
\]
Rotational isotropy gives \(\mathbb E[(\operatorname{Re}Z)^2]=R_1/2\), \(\mathbb E[(\operatorname{Re}Z)^4]=3R_2/8\), and \(\mathbb E[(\operatorname{Re}Z)^6]=5R_3/16\). Odd projected moments are zero. Consequently,
\[
 c_4=\frac38(R_2-2R_1^2),\qquad
 c_6=\frac5{16}R_3-\frac{45}{16}R_2R_1+\frac{15}{4}R_1^3.
\]
Substitution and exact factorization give the displayed rational expressions. Their denominators are strictly positive under the hypotheses. Let \(A_d=16d+12>0\), \(B_d=32d^2+40d+8>0\), and \(C_d=116d^3+199d^2+98d+15>0\). Then \(P_d(g)=C_d-B_dg-A_dg^2\) is strictly decreasing on \(g\geq0\), starts positive, and tends to minus infinity. Therefore its unique positive root is
\[
 g_6(d)=\frac{\sqrt{B_d^2+4A_dC_d}-B_d}{2A_d}>0.
\]
For the fourth cumulant, \(g_4(d)=(7d+3)/2\). The exact identity
\[
 P_d(g_4(d))=-8(2d+1)(3d+1)(4d+3)<0
\]
proves \(g_6(d)<g_4(d)\). Evaluating the rational sixth cumulant at \(g_4\) gives the strictly negative formula stated above; the sign classification follows.

Finally, for \(D_{\mathrm t}>0\) the stationary position is the independent sum of the above active component and a centered Gaussian vector with variance \(D_{\mathrm t}/\mu\) per coordinate. Cumulants of independent sums add, and all Gaussian cumulants of orders four and six vanish. Thus every formula and sign remains unchanged. This completes the proof.

## Verification
Run `python check.py` with SymPy installed. It reconstructs the triangular generator moments through total degree six, symbolically checks all three radial moment formulas, both cumulant factorizations, the root ordering identity, and the strictly negative sixth cumulant on the fourth-zero line. Independently, it builds finite exact-rational stationary generator matrices at five parameter pairs and solves them without calling the symbolic recurrence implementation. It reports `PASS` if all identities agree. The code checks finite algebraic identities and representative exact-rational instances; the universal claim rests on the displayed recurrence and positive-denominator / polynomial-monotonicity proof, not on parameter sampling.

For example, with \(d=1\), the two thresholds are \(g_6\approx2.73394350980956\) and \(g_4=5\).

## Relationship to prior work
Santra, Basu and Sabhapandit (2021, arXiv:2107.12640) study exactly this direction-reversing trapped swimmer. Their Appendix A gives the stationary second and fourth marginal moments and the fourth-cumulant sign boundary, including the observation that zero kurtosis does not imply Gaussianity. The present claim does **not** count any of those results as new. The additional results are the explicit sixth cumulant, its complete global sign classification, its strict ordering before the fourth-cumulant crossing, the nonvanishing sixth cumulant on the full zero-kurtosis curve, and exact persistence of this two-boundary classification under independent translational thermal noise. Chaudhuri and Dhar (2020, arXiv:2005.14234) give general active-Brownian moment methodology without Poisson directional reversals. Patel, Shee and Chaudhuri (2024, arXiv:2410.22004) study a different Ornstein–Uhlenbeck speed-fluctuation model and its fourth moment. Earlier general generator methods make the formulas in principle computable; implicit prior derivability is a residual originality risk.

## Limitations
The theorem treats stationary single-particle cumulants, not the full stationary density, nonstationary statistics, experimental estimators, or shape-transition locations. The cumulant sign changes need not coincide with morphological transitions and are not thermodynamic phase transitions. At infinite parameter limits, the limiting equations and rates require separate analysis; only finite parameters are asserted. The proof assumes rotational diffusion is strictly positive to ensure unique isotropic stationarity. The originality comparison does not establish publication priority against every unpublished or unindexed source. Independent scientific validation has not been performed.

## References
- I. Santra, U. Basu and S. Sabhapandit, *Direction reversing active Brownian particle in a harmonic potential*, arXiv:2107.12640v1 (first public 2021-07-27), Appendix A; https://arxiv.org/abs/2107.12640 and https://arxiv.org/html/2107.12640v2 .
- D. Chaudhuri and A. Dhar, *Active Brownian particle in harmonic trap: exact computation of moments, and re-entrant transition*, arXiv:2005.14234v1 (2020-05-28), sections 2–4; https://arxiv.org/html/2005.14234v2 .
- M. Patel, A. Shee and D. Chaudhuri, *Dynamical metastability and re-entrant localization of trapped active elements with speed and orientation fluctuations*, arXiv:2410.22004v1 (2024-10-29), sections II and V; https://arxiv.org/abs/2410.22004 .
