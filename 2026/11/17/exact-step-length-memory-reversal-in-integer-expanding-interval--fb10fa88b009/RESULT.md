# Exact step-length memory reversal in integer expanding interval maps

## Finding

For each integer \(b\ge 2\), let \(T_b:[0,1)\to[0,1)\) be \(T_b(x)=bx-\lfloor bx\rfloor\). Let \(X\) be uniformly distributed on \([0,1)\), let \(x_j=T_b^j(X)\), and define the *coordinate-Euclidean step length* \(Y_j=|x_{j+1}-x_j|\). This is the natural one-step contribution to the discrete path-length statistic \(\Omega_N=N^{-1}\sum_{j=0}^{N-1}Y_j\), measured in the indicated interval coordinates.

The stationary mean and lag-zero covariance are
\[
\mu_b=\mathbb E Y_0=\frac{2b-1}{6b},\qquad
C_b(0)=\operatorname{Var}(Y_0)=\frac{2b^2-2b-1}{36b^2}.
\]
Every positive-lag covariance is **exactly geometric**:
\[
\boxed{\displaystyle
C_b(n)=\operatorname{Cov}(Y_0,Y_n)=
\frac{(b-4)(b-2)(b^2-b-1)}{180b^4}\,b^{-2(n-1)}\quad(n\ge1).}
\]
Thus the complete positive-lag covariance sequence is negative at \(b=3\), vanishes at **every** positive lag for \(b=2\) and \(b=4\), and is positive at every positive lag for every integer \(b\ge5\). Neither the vanishing covariance nor the geometric law asserts independence of the step lengths.

The exact finite-window variance is
\[
\operatorname{Var}(\Omega_N)
=\frac1{N^2}\left[NC_b(0)+2C_b(1)\sum_{r=1}^{N-1}(N-r)b^{-2(r-1)}\right]\quad(N\ge1).
\]
In particular,
\[
\boxed{\displaystyle
\lim_{N\to\infty}N\operatorname{Var}(\Omega_N)
=\sigma_b^2
=\frac{12b^4-24b^3+11b^2+6b-11}{180b^2(b^2-1)}>0.}
\]
Moreover, with respect to uniform random initial conditions,
\[
\sqrt N(\Omega_N-\mu_b)\ \Longrightarrow\ \mathcal N(0,\sigma_b^2).
\]
The exact variance constants include \(\sigma_2^2=1/48\), \(\sigma_3^2=43/1296\), and \(\sigma_4^2=23/576\).

## Assumptions and scope

The parameter \(b\) is any **integer at least two**; the map uses the half-open interval convention and the ordinary absolute distance of two representatives in \([0,1)\), **not** the shorter-arc geodesic metric on a circle. Discontinuity values on the finite branch boundaries do not affect Lebesgue-statistical assertions. All probability statements sample one initial state from Lebesgue probability and iterate it deterministically. No independent random driving is assumed. The central limit theorem is distributional over that initial-state law, not a pointwise Gaussian claim about individual orbits.

## Proof

**1. Invariance and elementary moments.** The map has \(b\) affine full branches, each of slope \(b\); hence Lebesgue measure is invariant and the map is the one-sided full \(b\)-shift, therefore mixing and ergodic. Put \(f_b(x)=|T_b(x)-x|\). On the branch \(j/b\le x<(j+1)/b\), write \(c_j=j/(b-1)\); then
\[
f_b(x)=(b-1)|x-c_j|,\qquad 0\le j\le b-1.
\]
The left and right branch subinterval lengths are \(\ell_j=j/[b(b-1)]\) and \(r_j=(b-1-j)/[b(b-1)]\). Integrating these V-shaped functions and their squares gives
\[
\int_0^1 f_b\,dx=\frac{1}{2b^2(b-1)}\sum_{j=0}^{b-1}[j^2+(b-1-j)^2]=\frac{2b-1}{6b},
\]
\[
\int_0^1f_b^2\,dx=\frac{1}{3b^3(b-1)}\sum_{j=0}^{b-1}[j^3+(b-1-j)^3]=\frac{b-1}{6b},
\]
which imply the stated lag-zero variance.

**2. A one-eigenvalue transfer identity.** Define the Lebesgue Perron operator
\[
(\mathcal P_b g)(x)=\frac1b\sum_{j=0}^{b-1}g\left(\frac{x+j}{b}\right).
\]
For the step length, direct substitution gives
\[
(\mathcal P_b f_b)(x)=\frac1{b^2}\sum_{j=0}^{b-1}|(b-1)x-j|=:v_b(x).
\]
The continuous symmetric piecewise-affine function \(v_b\) has precisely the interior possible corners \(c_j\), \(1\le j\le b-2\), and the value at each corner is
\[
A_j=v_b(c_j)=\frac{j(j+1)+(b-1-j)(b-j)}{2b^2}.
\]
For any continuous piecewise-affine function whose only interior corners are among these \(c_j\), the operator \(\mathcal P_b\) preserves this finite-dimensional function space: a corner \(c_j\) can pull back to an interior point only via inverse branch \(j\), where it remains at \(c_j\). Its derivative jump is multiplied by \(b^{-2}\). Hence \(\mathcal P_b v_b-b^{-2}v_b\) is globally affine. Both terms are symmetric about \(1/2\), so this affine difference is constant; integration using invariance identifies the constant. With \(h_b=f_b-\mu_b\) and \(w_b=\mathcal P_bh_b=v_b-\mu_b\), this yields the exact identity
\[
\boxed{\mathcal P_b w_b=b^{-2}w_b,\qquad
\mathcal P_b^n h_b=b^{-2(n-1)}w_b\quad(n\ge1).}
\]

**3. Exact lag-one integration.** On the left and right of \(c_j\), the slopes of \(v_b\) are respectively
\[
s^-_j=\frac{(b-1)(2j-b)}{b^2},\qquad
s^+_j=\frac{(b-1)(2j+2-b)}{b^2}.
\]
Using the lengths \(\ell_j,r_j\) from step 1, elementary integration of the product \(f_bv_b\) on the two sides of each \(c_j\) gives
\[
\int_0^1f_bv_b\,dx
=(b-1)\sum_{j=0}^{b-1}\left[
\frac{A_j(\ell_j^2+r_j^2)}2+
\frac{-s^-_j\ell_j^3+s^+_jr_j^3}{3}\right]
=\frac{21b^4-27b^3+18b^2-2b-8}{180b^4}.
\]
The last equality follows by expansion and the classical sums of powers through degree four, with no limiting approximation. Subtracting \(\mu_b^2\) yields
\[
C_b(1)=\int f_bw_b\,dx=\frac{(b-4)(b-2)(b^2-b-1)}{180b^4}.
\]
For any \(n\ge1\), invariance and transfer duality give
\[
C_b(n)=\int h_b(x)h_b(T_b^nx)\,dx
=\int(\mathcal P_b^nh_b)(x)h_b(x)\,dx
=b^{-2(n-1)}C_b(1).
\]
The sign statement follows because \(b^2-b-1>0\) for all integers \(b\ge2\).

**4. Finite-window law, positive diffusivity, and Gaussian limit.** Stationarity implies
\[
\operatorname{Var}\left(\sum_{j=0}^{N-1}h_b(T_b^jX)\right)
=NC_b(0)+2\sum_{r=1}^{N-1}(N-r)C_b(r),
\]
so the finite-window formula is exact. Summing the geometric series gives
\[
\sigma_b^2=C_b(0)+\frac{2C_b(1)}{1-b^{-2}}
=\frac{12b^4-24b^3+11b^2+6b-11}{180b^2(b^2-1)}.
\]
Its numerator, on writing \(b=2+t\) for \(t\ge0\), is \(12t^4+72t^3+155t^2+146t+45\), proving strict positivity.

For completeness, the Gaussian assertion does not follow merely from a covariance computation. Set
\[
u_b=\sum_{n=1}^{\infty}\mathcal P_b^nh_b
=\frac{w_b}{1-b^{-2}},\qquad
m_b=h_b+u_b-u_b\circ T_b.
\]
These are bounded functions, and \(\mathcal P_b(u_b\circ T_b)=u_b\), so \(\mathcal P_bm_b=0\). Thus the sequence \(m_b\circ T_b^j\) is a stationary bounded reverse martingale difference sequence with respect to the decreasing future sigma fields. The standard ergodic reverse-martingale central limit theorem applies: its conditional quadratic variation averages converge by ergodicity, and boundedness supplies Lindeberg's condition. The bounded telescoping correction in
\[
\sum_{j=0}^{N-1}h_b\circ T_b^j
=\sum_{j=0}^{N-1}m_b\circ T_b^j+u_b\circ T_b^N-u_b
\]
is negligible after division by \(\sqrt N\). The variance of the martingale difference equals the previously calculated positive \(\sigma_b^2\) (compare normalized variances, since the correction is bounded), proving the asserted central limit theorem.

## Verification

The standard-library checker `verify.py` integrates the product of two piecewise-affine observables exactly over a rational common refinement of all breakpoints. It independently compares the exact covariances at lags one through three for integer slopes two through seven against the formula, and checks the closed asymptotic-variance identity and every integer sign regime through slope fifteen. Invoke `python3 verify.py` from the directory containing this document. The checker prints `VERIFY_OK transfer_eigen_checks=96 exact_piecewise_integrals=18 covariance_lags=1..3 slopes=2..7 sign_and_variance_cases=14` on success. Finite checks corroborate, but do not prove, the all-integer and all-lag assertions. The mathematical proof is the branch integration and exact transfer-eigenfunction argument above.

## Relationship to prior work

Jiménez-López and García-Garrido (2026) motivate time-averaged trajectory arclength and establish correlation-based fluctuation scaling for suitable Hamiltonian flows. Daquin and coauthors (2022) explicitly define discrete orbit path lengths for mapping-based Lagrangian descriptors, and analyze standard and nearly-integrable maps. The present claim instead gives an exact, all-integer and all-lag **coordinate-Euclidean discrete step-length** covariance law for the expanding interval family, including two exact decorrelation slopes and a sign reversal. It is not a theorem about continuous Hamiltonian flow arclength.

Jenkinson, Pollicott and Vytnova (2018) give general diffusion-coefficient computation techniques and an exact example for a *different observable*, the centered linear coordinate under doubling. Those results establish general methodology but do not supply this explicit step-length formula or its slope-dependent sign pattern. A related published result on self-displacement **circle phases** of expanding maps concerns the conditional law of modular phases, rather than the absolute difference between the two interval representatives. Such phase information alone does not identify the present branch-dependent Euclidean step-length process; the available description does not establish an implication either way. Earlier unindexed direct calculations remain a genuine priority risk.

## Limitations

The finding is exact for integer slopes and Lebesgue initial sampling, not arbitrary noninteger beta transformations or invariant densities. Its step length is dependent on the interval embedding and on taking the non-geodesic absolute difference at branch jumps; replacing it by circular geodesic distance changes the observable and need not preserve the formulas. The zero-covariance cases do not imply statistical independence. The claim provides an explicit calibration and sign comparison for discrete path-length fluctuations, not a universal chaos classifier. Independent expert validation and a comprehensive historical-priority assessment have not been performed.

## References

1. J. Jiménez-López and V. J. García-Garrido, *Trajectory arclength reveals chaos*, arXiv:2602.07660v3 (first posted 2026-02-07), https://arxiv.org/html/2602.07660v3.
2. J. Daquin, R. Pédenon-Orlanducci, M. Agaoglou, G. García-Sánchez, and A. M. Mancho, *Global dynamics visualisation from Lagrangian Descriptors. Applications to discrete and continuous systems*, arXiv:2206.04467 (2022), https://arxiv.org/abs/2206.04467.
3. O. Jenkinson, M. Pollicott, and P. Vytnova, *Rigorous Computation of Diffusion Coefficients for Expanding Maps*, J. Stat. Phys. 170 (2018), 221–253, https://doi.org/10.1007/s10955-017-1930-8.
4. M. I. Gordin, *The central limit theorem for stationary processes*, Soviet Math. Dokl. 10 (1969), 1174–1176; https://sovietrxiv.org/items/ru-196901.82106.
