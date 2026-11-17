# A constructive smooth reverse-endpoint counterexample for Gaussian Fock Toeplitz operators

## Finding
On the Gaussian Fock space \(\mathcal F^2(\mathbb C)\) with \(d\mu(z)=(2\pi)^{-1}e^{-|z|^2/2}dA(z)\), there is a uniquely specified **computable, real-valued, smooth** symbol \(g\) such that \(gk_z\in L^2(d\mu)\) for every normalized kernel \(k_z\), its critical heat transform
\[
(Hg)(z)=\pi^{-1}\int_{\mathbb C}g(w)e^{-|w-z|^2}\,dA(w)
\]
exists absolutely and belongs to \(C_0(\mathbb C)\), but the densely defined Toeplitz operator \(T_g=P(g\cdot)\) has no bounded extension. In particular, an explicitly specified sequence of unit vectors \(F_j,G_j\) in its form domain satisfies
\[
|\langle T_gF_j,G_j\rangle|>j-2^{-j-4}.
\]
This constructs, rather than merely proves existence of, a smooth real witness to failure of the reverse Berger–Coburn endpoint implication.

## Assumptions and scope
Let \(e_m(z)=z^m/\sqrt{2^m m!}\) and \(k_a(z)=e^{\bar a z/2-|a|^2/4}\). Write \(W_af(z)=k_a(z)f(z-a)\), a unitary operator for each \(a\in\mathbb C\). For integers \(n\ge1\) set \(b=n^2\) and
\[
C_n=\frac{2^{n/2+1}(b+1/2)^{n+1}}{\sqrt{n!}},\qquad h_n(z)=C_n\bar z^{\,n}e^{-b|z|^2},\qquad p_n=h_n+\overline{h_n}.
\]
For \(j\ge1\), let \(n_j=(j+1)^{12}\) and \(u_{j,a}(z)=j p_{n_j}(z-a)\), where \(a\) ranges over positive integers. The following deterministic finite-stage rule specifies centers \(a_j\). Put \(a_0=0\). Having chosen \(a_1,\ldots,a_{j-1}\), define \(F_k=W_{a_k}e_{n_k}\), \(G_k=W_{a_k}e_0\), \(u_k=u_{k,a_k}\) for \(k<j\). Choose \(a_j\) as the least integer \(a>a_{j-1}+1\) satisfying all of these strict inequalities:

1. \(\sup_{|z|\le j}|\partial_x^r\partial_y^s u_{j,a}(z)|<2^{-j}\) for every pair \(r,s\ge0\) with \(r+s\le j\).
2. \(\sup_{|z|\le j}\|u_{j,a}k_z\|_{L^2(d\mu)}<2^{-j}\).
3. For each \(k<j\), \(\|u_{j,a}F_k\|_{L^2(d\mu)}<2^{-j-k-4}\).
4. For each \(k<j\), both \(|\langle T_{u_{j,a}}F_k,G_k\rangle|<2^{-j-k-4}\) and \(|\langle T_{u_k}W_ae_{n_j},W_ae_0\rangle|<2^{-j-k-4}\).

All tests are finite Gaussian-polynomial integrals or suprema of explicit analytic functions on compact disks. Strict passing inequalities can be certified using rational interval bounds, with increasing precision, in an integer search. The termination proof below establishes a computable prescription; the infinite sequence need not be calculated in advance. Set
\[
g(z)=\sum_{j=1}^{\infty}u_{j,a_j}(z),\quad F_j=W_{a_j}e_{n_j},\quad G_j=W_{a_j}e_0.
\]
No membership in unweighted \(L^1\), bounded-symbol classes, or a fixed Schatten class is asserted.

## Proof
**1. Exact packet operator and moment.** With \(q=(1+2b)^{-1}\), angular integration and the Gaussian moment identity show that
\[
T_{h_n}e_{k+n}=q^k\sqrt{\binom{n+k}{k}}\,e_k\quad(k\ge0),\qquad T_{h_n}e_m=0\quad(m<n).
\]
Moreover, \(T_{\overline{h_n}}e_n\) is a multiple of \(e_{2n}\), orthogonal to \(e_0\). Consequently \(\langle T_{p_n}e_n,e_0\rangle=1\). The weight ratio \(q\sqrt{(n+k+1)/(k+1)}\le q\sqrt{n+1}<1\) for \(b=n^2\), so \(\|T_{h_n}\|=1\), \(\|T_{p_n}\|\le2\). Every packet is bounded and smooth and its Toeplitz operator is bounded.

**2. Quantitative critical-heat decay.** Directly integrating the shifted Gaussian gives
\[
(Hh_n)(z)=\frac{C_n\bar z^{\,n}}{(1+b)^{n+1}}\exp\!\left(-\frac{b}{1+b}|z|^2\right).
\]
Maximizing the radial factor yields the exact value
\[
M_n=\|Hh_n\|_{\infty}=2\frac{(1+1/(2b))^{n+1}}{(1+1/b)^{n/2+1}}\frac{(n/e)^{n/2}}{\sqrt{n!}}.
\]
The elementary estimates \(\log(1+t)\le t\) and \(n!\ge\sqrt{2\pi n}(n/e)^n\) imply
\[
\|Hp_n\|_\infty\le2M_n\le\frac{4e}{(2\pi n)^{1/4}}.
\]
Heat transform commutes with translations. Therefore
\[
\|Hu_j\|_\infty\le \frac{4e}{(2\pi)^{1/4}}\frac{j}{(j+1)^3},
\quad
\sum_{j>J}\|Hu_j\|_\infty\le \frac{4e}{(2\pi)^{1/4}J}\quad(J\ge1).
\]
Every heat packet lies in \(C_0(\mathbb C)\). Uniform convergence and the displayed effective tail bound imply that their sum lies in \(C_0\).

**3. The center recursion always terminates.** For any fixed finite Gaussian-polynomial packet, translating it to a real center \(a\to+\infty\) makes all its derivatives uniformly small on any prescribed compact set. Its \(L^2(d\mu)\) product with a kernel whose center ranges over a fixed compact set tends uniformly to zero, because \(|k_z(w)|^2d\mu(w)=(2\pi)^{-1}e^{-|w-z|^2/2}dA(w)\). For each previously selected \(F_k,G_k\), the norms \(\|u_{j,a}F_k\|_2\) and matrix coefficients \(\langle T_{u_{j,a}}F_k,G_k\rangle\) tend to zero as \(a\to\infty\). Likewise the matrix coefficient \(\langle T_{u_k}W_ae_{n_j},W_ae_0\rangle\) tends to zero: the earlier packet is a fixed Gaussian-polynomial function while the latter two vectors carry their Gaussian probability mass to infinity. Each statement reduces to a Gaussian times a fixed polynomial and follows by dominated convergence or completing squares. There are finitely many tests at stage \(j\); all pass at every sufficiently large integer \(a\), so the first passing integer exists. Strict inequalities also make certified search effective.

**4. Smoothness and admissibility.** For every compact disk and derivative order, condition 1 controls all sufficiently late terms by the summable sequence \(2^{-j}\). Hence \(g\) is real and \(C^\infty\). For fixed \(z\), condition 2 eventually controls \(\|u_jk_z\|_2\) by \(2^{-j}\); the finitely many other terms belong to \(L^2(d\mu)\). Thus \(gk_z\in L^2(d\mu)\) for every \(z\). For fixed \(k\), condition 3 applies to all future packets; the earlier and current packets are bounded multipliers. Hence \(gF_k\in L^2(d\mu)\), and \(T_gF_k=P(gF_k)\) is defined. The critical heat integral of \(g\) is absolutely convergent for each \(z\): by Cauchy–Schwarz, \(\int |g(w)|e^{-|w-z|^2}dA(w)\) is bounded by a constant times \(\|gk_z\|_2\). This also justifies exchanging its integral with the convergent series and identifies \(Hg=\sum_j Hu_j\).

**5. Diverging matrix coefficients.** Toeplitz translation covariance \(T_{f(\cdot-a)}=W_aT_fW_a^*\) and step 1 give \(\langle T_{u_j}F_j,G_j\rangle=j\). For every \(k\ne j\), condition 4 from the later index \(\max(j,k)\) bounds the cross term by \(2^{-j-k-4}\). Consequently
\[
\big|\langle T_gF_j,G_j\rangle-j\big|\le\sum_{k\ne j}2^{-j-k-4}<2^{-j-4},
\]
where both \(F_j,G_j\) have unit norm. Hence \(T_g\) cannot have a bounded extension. The statements claimed follow.

## Verification
A standalone standard-library Python checker `verify.py` recomputes the normalized Gaussian moments, decreasing weighted-shift coefficients, exact heat maxima in logarithmic arithmetic, and quantitative packet bounds for representative degrees (including \(n=4096\)). These are finite diagnostic checks, not an infinite proof. The center-existence argument and the operator-domain passage are proved analytically above; no finite list of computed centers is claimed as evidence for them.

## Relationship to prior work
Virtanen, *Critical Schatten exponents for the Berger–Coburn endpoint problem*, arXiv:2609.11853v3, Theorem 1.1(iii), proves existence of a real admissible symbol with critical heat in \(C_0\) and unbounded Toeplitz operator, using closed-graph and Baire-type arguments, and explicitly observes that its endpoint examples are nonconstructive (Remark 1.2). This result **does not claim the existence phenomenon as new**. The contribution here is one deterministic smooth real symbol given by elementary Gaussian monomials, a finite-stage center-selection algorithm and an explicit uniform heat-series tail bound. Looi, arXiv:2601.20859v1, constructs a witness for the *opposite* (bounded operator/unbounded heat) direction. The closest previously published explicit critical-heat constructions located concern that opposite direction; no equivalent explicit reverse-direction witness was identified in the inspected material.

## Limitations
The center recursion may produce very large integers, and efficient numerical implementation or optimal center growth is not established. The result is for a one-dimensional Gaussian Fock space, not an explicit classification of all endpoint counterexamples. This is a constructive strengthening of a previously known existential counterexample, not a new disproof of the original conjecture. Publication priority of a differently formulated constructive reverse example cannot be ruled out by literature searches; no independent audit has been performed.

## References
1. J. A. Virtanen, *Critical Schatten exponents for the Berger–Coburn endpoint problem*, arXiv:2609.11853v3 (first public version 2026-09-10), especially Theorem 1.1(iii), Remark 1.2 and its proof.
2. S. Looi, *A counterexample to the Berger–Coburn conjecture*, arXiv:2601.20859v1 (2026-01-28), Theorem 1.2 and construction.
3. C. A. Berger and L. A. Coburn, *Heat flow and Berezin–Toeplitz estimates*, Amer. J. Math. 116 (1994), 563–590, for the endpoint formulation and normalization.
