# Universal spectral majorization by staggering two concentric analytic-kernel sampling orbits

## Finding
For integers \(n\ge2\) and \(\alpha\ge1\), radii \(0<r<s<1\), and \(\zeta=e^{2\pi i/n}\), consider the two regular \(n\)-gons
\[
Z_\delta=\{r\zeta^j:0\le j<n\}\cup\{s e^{i\delta}\zeta^j:0\le j<n\}.
\]
Let \(G_\alpha(\delta)\) be the \(2n\)-by-\(2n\) Hermitian Gram matrix of evaluations of the analytic reproducing kernel \(K_\alpha(z,w)=(1-z\overline w)^{-\alpha}\) on \(Z_\delta\). Write \(u\prec v\) for vector majorization, with entries sorted in descending order and equal total sums. For every real \(\delta\),
\[
\boxed{\lambda(G_\alpha(\pi/n))\prec\lambda(G_\alpha(\delta))\prec\lambda(G_\alpha(0)).}
\]
The left endpoint is attained only when \(\delta\equiv\pi/n\pmod{2\pi/n}\), and the right endpoint only when \(\delta\equiv0\pmod{2\pi/n}\), in the sense that every strictly convex spectral trace is strictly intermediate at other offsets.

In particular, **a half-grid angular offset uniquely minimizes every strictly convex spectral trace** \(\operatorname{tr}\Phi(G_\alpha(\delta))\), uniquely minimizes the spectral condition number, uniquely maximizes the least Gram eigenvalue, and uniquely maximizes the Gram determinant. Alignment uniquely has the opposite extremal properties. The conclusions remain true when each kernel vector is independently normalized to norm one (the normalization is constant within each circular orbit).

The exact eigenvalues also admit a rapidly computable \(2\)-by-\(2\) formula. For \(0\le m<n\), define
\[
 H_{\alpha,n,m}(t)=\sum_{k\ge0}\binom{m+nk+\alpha-1}{\alpha-1}t^k,\quad
 A_m=n r^{2m}H_{\alpha,n,m}(r^{2n}),\quad
 C_m=n s^{2m}H_{\alpha,n,m}(s^{2n}),
\]
\[
 D_m(\delta)=n(rs)^m\left|H_{\alpha,n,m}((rs)^n e^{in\delta})\right|.
\]
The spectrum, counted with multiplicity, is the union over \(0\le m<n\) of
\[
\boxed{\mu_m^\pm(\delta)=\frac{A_m+C_m\pm\sqrt{(A_m-C_m)^2+4D_m(\delta)^2}}2.}
\]

## Assumptions and scope
The inner product is the one determined by the positive kernel \(K_\alpha(z,w)\); \(\alpha\) is an integer, and all nodes lie strictly inside the open unit disk. The kernel is positive definite because \((1-t)^{-\alpha}=\sum_{k\ge0}\binom{k+\alpha-1}{\alpha-1}t^k\) has positive coefficients. Distinct nodes yield positive definite Gram matrices: the first \(2n\) monomials in the feature map already form a full-rank Vandermonde matrix. The two circles are disjoint since \(r<s\). Majorization includes equality of the total sum \(n[(1-r^2)^{-\alpha}+(1-s^2)^{-\alpha}]\).

For normalized kernel vectors, replace \(K_\alpha(z,w)\) by \(K_\alpha(z,w)/(K_\alpha(z,z)K_\alpha(w,w))^{1/2}\). More generally, positive constant rescalings separately on the two complete rings have the same extremal orientation; their precise Gram eigenvalues follow by the same block formulas after multiplying \(A_m,C_m,D_m\) by the corresponding factors. The statement is only about angular offsets between two uniformly spaced orbits, not arbitrary point designs, arbitrary positive real \(\alpha\), or more than two rings.

## Proof
**1. Exact Fourier block reduction.** Expand
\[
 K_\alpha(z,w)=\sum_{q\ge0}\binom{q+\alpha-1}{\alpha-1}z^q\overline w^{\,q}.
\]
On each orbit apply the unitary discrete Fourier transform of order \(n\). Only indices \(q\equiv m\pmod n\) survive in its character-\(m\) block. Its two diagonal entries are \(A_m,C_m\), and the off-diagonal entry differs by a unit phase from
\[
 n(rs)^m H_{\alpha,n,m}((rs)^n e^{in\delta}).
\]
The displayed formula for \(\mu_m^\pm\) follows by diagonalizing each positive Hermitian \(2\)-by-\(2\) block. This also explicitly verifies that every block has angle-independent trace \(A_m+C_m\).

**2. Negative-root numerator lemma (known Veronese structure, proved here).** For integers \(j\ge0\), set
\[
 P_j(t)=(1-t)^{j+1}\sum_{k\ge0}\binom{m+nk+j}{j}t^k.
\]
The formal generating series on the right has a polynomial numerator of degree at most \(j\). An exact finite geometric-series coefficient identity is
\[
 P_j(t)=\sum_{h\ge0}[x^{m+nh}](1+x+\cdots+x^{n-1})^{j+1}t^h.
\]
Thus \(P_j\) has nonnegative coefficients, strictly positive constant coefficient \(\binom{m+j}{j}\), and strictly positive leading coefficient. With \(P_0=1\), the binomial recurrence gives
\[
\boxed{P_j(t)=\frac{\bigl[(m+j)+(nj-m-j)t\bigr]P_{j-1}(t)+nt(1-t)P'_{j-1}(t)}j.}
\]
Assume \(P_{j-1}\) has distinct negative roots \(\tau_1<\cdots<\tau_d<0\). At each root, \(P_j(\tau_i)=n\tau_i(1-\tau_i)P'_{j-1}(\tau_i)/j\), and the signs alternate strictly. Thus \(P_j\) has a zero in each interval \((\tau_i,\tau_{i+1})\), and a zero in \((\tau_d,0)\). Since its degree is either \(d\) or \(d+1\), if the degree rises there is one further root in \(( -\infty,\tau_1)\) by the leading-sign comparison. All are negative and distinct. The same base-case argument covers \(d=0\). This establishes inductively that every nonconstant \(P_j\) has only simple negative real zeros. This numerator real-rootedness is **not** claimed as new: it is also subsumed by Jochemko's 2016 Veronese theorem [3].

**3. Strict angular monotonicity.** Put \(j=\alpha-1\) and \(\rho=(rs)^n\in(0,1)\). The lemma gives
\[
 H_{\alpha,n,m}(t)=P_j(t)/(1-t)^\alpha,
 \qquad P_j(t)=c\prod_{h=1}^d(t+u_h),\quad c>0,\ u_h>0.
\]
For \(t=\rho e^{i\theta}\) and \(v=\cos\theta\),
\[
 |H_{\alpha,n,m}(t)|^2=c^2\frac{\prod_{h=1}^d(u_h^2+\rho^2+2u_h\rho v)}{(1+\rho^2-2\rho v)^\alpha}.
\]
Each numerator factor is nonnegative and strictly increasing in \(v\), and the denominator is strictly decreasing and positive. The product quotient is therefore strictly increasing on \([-1,1]\), including when one numerator factor vanishes at the left endpoint. For \(d=0\) the denominator alone gives strict increase. Thus every \(D_m(\delta)\) is minimal precisely when \(\cos(n\delta)=-1\) and maximal precisely when \(\cos(n\delta)=1\). This assertion holds **simultaneously** for all Fourier blocks and all \(m\).

**4. Global majorization and sharp consequences.** At a fixed \(m\), the sum \(\mu_m^++\mu_m^-=A_m+C_m\) is constant, while the gap \(\mu_m^+-\mu_m^-\) increases strictly with \(\cos(n\delta)\). Therefore the two-entry eigenvalue vector at larger cosine majorizes the one at smaller cosine. A direct sum of independent majorization relations is again a majorization relation (combine the corresponding doubly stochastic matrices). Reordering their concatenation proves the claimed \(2n\)-entry majorizations.

For a strictly convex real \(\Phi\) on the positive spectrum, each pair sum \(\Phi(\mu_m^+)+\Phi(\mu_m^-)\) increases strictly with the gap, establishing uniqueness at both offsets and all strictly convex traces. Choosing \(\Phi(t)=1/t\) gives trace-inverse optimality. Since \(\mu_m^+\) strictly increases and \(\mu_m^-\) strictly decreases in the cosine for every \(m\), the global maximum eigenvalue strictly increases and the global minimum strictly decreases; their positive ratio, the spectral condition number, is strictly increasing. Finally \(\det G_\alpha=\prod_m(A_mC_m-D_m^2)\), and each factor strictly decreases with the cosine while remaining positive, proving unique determinant maximality at the half-step and minimality at alignment. For norm-one kernel vectors, fixed positive diagonal block rescaling merely changes \(A_m,C_m,D_m\) by positive constants independent of \(\delta\), so the same argument applies verbatim.

## Verification
The accompanying self-contained mathematical derivation covers arbitrary \(n\ge2\) and all integral \(\alpha\ge1\), not just numerical cases. Run `python checker.py` with Python 3 plus `numpy` and `sympy`. The checker computes 243 positive-coefficient polynomial numerators, uses exact Sturm counting to verify 80 nonconstant cases have all roots real and negative, and independently compares the direct kernel Gram matrix to the Fourier-block formula on 42 parameter-offset instances. It also tests all partial-sum majorization inequalities, strict extreme-eigenvalue ordering, inverse traces, and log determinants on those instances.

The executed output was:
```
PASS root_cases= 80 all_polynomial_cases= 243
PASS independent_kernel_spectrum_cases= 42
```
These finite checks are reproducibility aids, not an infinite mathematical proof; the proof is the preceding symbolic reduction and negative-root induction.

## Relationship to prior work
Jorgensen and Tian [2] develop general RKHS kernel sampling and associated Gram frameworks without this two-ring Fourier-block optimization. Chen, Womersley and Ye [1] optimize Gram condition numbers numerically for general polynomial and spherical-harmonic point sets; their results neither provide this simultaneous spectral majorization nor treat the analytic-kernel two-ring orientation family. Jochemko [3, Theorem 1.1] supplies a substantially broader known real-rootedness theorem for Veronese numerator polynomials. The crucial real-rootedness ingredient therefore belongs to established literature; the statement addressed here is the exact, all-integer-order **two-concentric-ring Gram-spectrum majorization and joint optimizer classification**.

A closely related published circle sampling result studies a *single-radius*, regular Szegő kernel orbit and its sharp determinant stability; it explicitly excludes mixed radii and general optimality of the condition number under irregular placements. Its single-ring claim does not imply the present two-ring angular majorization. Earlier finite-monomial three-orbit Hardy determinant maximization is likewise about a different number of rings and only a determinant, not the full infinite analytic-kernel spectrum. These are comparisons of mathematical implications, not merely titles.

## Limitations
The theorem does not optimize the radii, does not cover noninteger kernel orders, does not assert spectral Loewner monotonicity, and does not compare arbitrary configurations with nonuniform angles. Strict majorization statements refer to strictly convex spectral traces and the distinguished extremal locations; the majorization preorder itself may have unrelated equality degeneracies without strict convexity. Real-rootedness is prior work, not a new theorem. The residual originality risk is an older, differently formulated optimal concentric-node kernel-sampling theorem not detected in available searches. No independent mathematical audit has been performed.

## References
[1] X. Chen, R. S. Womersley, and J. J. Ye, *Minimizing the Condition Number of a Gram Matrix*, SIAM Journal on Optimization **21** (2011), 127–148. Published online 6 January 2011. DOI: 10.1137/100786022. https://doi.org/10.1137/100786022.

[2] P. Jorgensen and F. Tian, *Nonuniform sampling, reproducing kernels, and the associated Hilbert spaces*, arXiv:1601.07380v1, posted 27 January 2016. https://arxiv.org/abs/1601.07380.

[3] K. Jochemko, *On the real-rootedness of the Veronese construction for rational formal power series*, arXiv:1602.09139v1, posted 29 February 2016, Theorem 1.1. https://arxiv.org/abs/1602.09139.
