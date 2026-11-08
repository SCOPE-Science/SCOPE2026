# Three sharp mode-selection regimes for the Jacobi heat semigroup on Chebyshev pairs

## Finding
Equip \([-1,1]\) with the semicircle probability measure \(d\mu(x)=2\sqrt{1-x^2}\,dx/\pi\). Let \(U_j\) be the second-kind Chebyshev polynomial, uniquely characterized by \(U_j(\cos\theta)=\sin((j+1)\theta)/\sin\theta\). For integers \(1\le m<n\) with \(m+n\) odd, let \(E_{m,n}=\operatorname{span}_{\mathbb R}\{U_m,U_n\}\). The Jacobi diffusion generator is \(L=(1-x^2)\partial_x^2-3x\partial_x\), and \(T_t=e^{tL}\), \(t\ge0\), is its Markov semigroup.

Put \(a=m+1\), \(b=n+1\), \(\lambda_j=j(j+2)\), \(\Delta=\lambda_n-\lambda_m>0\), and \(r=e^{-2\Delta t}\in(0,1]\). Then the exact **fourth power** of the sharp real restricted operator norm is
\[
 \|T_t:E_{m,n}(L^2(\mu))\to L^4(\mu)\|^4
 =e^{-4\lambda_m t}\,\Phi_{a,b}(r),
\]
where \(\Phi_{a,b}(r)=\max_{0\le x\le1}\{a(1-x)^2+br^2x^2+6ar x(1-x)\}\). More explicitly, the complete maximizer classification has three cases:

**(I) \(b<3a\):** the branch is mixed for \(1/3<r\le1\), and the lower-mode branch for \(0<r\le1/3\).

**(II) \(3a<b<9a\):** the upper-mode branch holds for \(3a/b\le r\le1\); the mixed branch holds for \(1/3<r<3a/b\); the lower-mode branch holds for \(0<r\le1/3\). As time increases, the unique maximizing *type* is therefore **upper pure → mixed → lower pure**, a genuine reentrant interval of mode mixing.

**(III) \(b>9a\):** the upper-mode branch holds for \(\sqrt{a/b}\le r\le1\); the lower-mode branch holds for \(0<r\le\sqrt{a/b}\), with both pure modes (and no mixture) extremal at the switch.

The branch values are, respectively,
\[
\Phi_{a,b}^{\mathrm{high}}(r)=br^2,\qquad
\Phi_{a,b}^{\mathrm{mix}}(r)=\frac{ar^2(9a-b)}{6ar-a-br^2},\qquad
\Phi_{a,b}^{\mathrm{low}}(r)=a.
\]
In the strict mixed branch the unique upper-mode input energy share is
\[
x_* = \frac{a(3r-1)}{6ar-a-br^2}\in(0,1).
\]
Every norming real input is a nonzero scalar multiple of \(\varepsilon_1\sqrt{1-x_*}U_m+\varepsilon_2\sqrt{x_*}U_n\), with independent signs \(\varepsilon_i\in\{-1,1\}\); on a strict pure branch only the indicated one-dimensional eigenspace norms the operator. On a pure-switch boundary both pure eigenspaces, but no other inputs, norm it. The nominal equalities \(b=3a\) and \(b=9a\) are impossible under the opposite-parity assumption, so these cases exhaust all permitted integer pairs.

There is exactly one \(t_*(m,n)>0\) with \(\|T_{t_*}|_{E_{m,n}}\|_{2\to4}=1\); the restricted semigroup is \(L^2\)-to-\(L^4\) contractive precisely for \(t\ge t_*\). The displayed explicit piecewise expression determines \(t_*\) uniquely without an unsolved optimization problem.

For example, \((m,n)=(1,6)\) has \((a,b)=(2,7)\): its three successive maximizing branches are separated by \(r=6/7\) and \(r=1/3\). In contrast, \((m,n)=(1,18)\) exhibits a direct pure-to-pure switch at \(r=\sqrt{2/19}\).

## Assumptions and scope
All functions and coefficients are real, the \(L^p\) norms refer to the normalized probability measure \(\mu\), time satisfies \(t\ge0\), and \(1\le m<n\) have opposite parity. The conventional normalization of \(U_j\) is *not* divided by its pointwise maximum: \(\|U_j\|_{L^2(\mu)}=1\). This is the restriction of the classical self-adjoint Markov Jacobi diffusion, not a new semigroup constructed only on a two-dimensional space. No arbitrary complex-coefficient equality classification is asserted.

## Proof
**1. Eigenfunctions and exact fourth moments.** The polynomial recurrence \(U_0=1\), \(U_1=2x\), \(U_{j+1}=2xU_j-U_{j-1}\), or the trigonometric definition, gives
\[
L U_j=-j(j+2)U_j,\qquad \int U_j U_k\,d\mu=\delta_{jk}.
\]
The elementary multiplication identity, valid for integers \(j\ge k\ge0\), is
\[
 U_jU_k=\sum_{h=0}^{k}U_{j-k+2h}.
\]
It follows by multiplying the sine quotients or inducting on \(k\). Squaring this orthogonal expansion and counting terms yields \(\int U_m^4\,d\mu=m+1=a\), \(\int U_n^4\,d\mu=n+1=b\), and \(\int U_m^2U_n^2\,d\mu=m+1=a\). Because \(m+n\) is odd, the measure is symmetric and the odd cross integrals \(\int U_m^3U_n\,d\mu\), \(\int U_mU_n^3\,d\mu\) vanish. Thus for any real coefficients \(c,d\),
\[
\|T_t(cU_m+dU_n)\|_4^4
=a e^{-4\lambda_m t}c^4+b e^{-4\lambda_n t}d^4
+6a e^{-2(\lambda_m+\lambda_n)t}c^2d^2.
\]
Orthonormality makes the square of the input \(L^2\) norm equal to \(c^2+d^2\). On its unit sphere put \(x=d^2\) and factor out \(e^{-4\lambda_m t}\); this proves the stated quadratic maximization exactly, including its endpoint normalization.

**2. Complete scalar optimization.** Let \(A=a\), \(B=br^2\), and \(C=3ar\). The quadratic is \(Q(x)=A(1-x)^2+Bx^2+2Cx(1-x)\). Its derivative at the left endpoint is \(2(C-A)\) and at the right endpoint is \(2(B-C)\). A strict interior maximum exists if and only if \(C>A\) **and** \(C>B\); then \(Q''=-2(2C-A-B)<0\),
\[
 x_*=(C-A)/(2C-A-B),\quad Q(x_*)=(C^2-AB)/(2C-A-B),
\]
and the exact deficit identity \(Q(x_*)-Q(x)=(2C-A-B)(x-x_*)^2\) proves uniqueness. If no interior maximum exists, \(\max Q=\max(A,B)\). In our parameters the two strict inequalities for interior maximization are exactly \(r>1/3\) and \(r<3a/b\). They can hold simultaneously only when \(b<9a\). Comparing these thresholds with \(r=1\) gives cases I and II. If \(b>9a\), no interior maximization is possible; \(A=B\) occurs only at \(r=\sqrt{a/b}\), proving case III. Substitution gives the three branch values and the input-energy share. At a branch boundary \(C=A\) or \(C=B\), the quadratic has a unique pure maximizer. At the direct switch in case III, \(A=B>C\), and \(Q(x)=A-2(A-C)x(1-x)\), so exactly the two pure choices maximize. Since \(m+n\) is odd, \(n+1\) cannot be an odd integer multiple of \(m+1\); therefore \(b\ne3a,9a\).

**3. Exact contraction threshold.** At \(t=0\), the fourth-power norm is at least \(a=m+1\ge2\), so exceeds one. It tends to zero as \(t\to\infty\) because both eigenvalues are positive. For any fixed unit input the fourth-power expression in Step 1 is a sum of nonnegative terms, each strictly decreasing with \(t\); hence it is strictly decreasing. The norm maximum, taken on the compact input unit circle, is strictly decreasing as well: a maximizer at the later time has a strictly larger value at an earlier time. Continuity follows from compactness, proving existence and uniqueness of \(t_*\) and the contractivity characterization.

## Verification
The accompanying standalone standard-library checker `verify.py` generates \(U_j\) by recurrence, integrates even monomials with the exact semicircle moment \(\int x^{2k}\,d\mu=C_k/4^k\), and independently checks the seven base moments for ten opposite-parity degree pairs. It tests the sharp quadratic branch formula at seven rational spectral ratios per pair, including an exact completed-square identity in all mixed cases, and checks representatives of all three regimes. Invoke `python3 verify.py`. This is a finite diagnostic; the multiplication identity and scalar analysis above prove the theorem for all eligible integers and real times.

## Relationship to prior work
The Jacobi diffusion and its spectral expansion and hypercontractivity are classical: Balderrama–Urbina construct and analyze the multidimensional Jacobi semigroup and its polynomial eigenspaces, without computing the exact restricted two-mode \(L^2\to L^4\) norms or the two spectral-gap transitions. Dooley–Gupta analyze \(L^4\) norms of noncentral matrix coefficients of \(SU(2)\); this is a different family from central polynomial pairs. The published result *High-weight parity localization of central fourth moments on \(SU(2)\)* determines a leading high-weight asymptotic for arbitrary fixed finite character packets and gives an exact tensor-product intersection expansion. It explicitly does **not** determine finite-weight sharp maximizers and does not study spectral heat weights; the present complete all-pair heat-time optimization is not the asymptotic theorem. These classical representation identities are used here as standard input, not asserted as original.

## Limitations
The classification applies only to **real** two-mode subspaces of opposite parity, for the semicircle-weight Jacobi operator and target exponent four. Same-parity pairs have nonvanishing cubic cross terms and need separate analysis. No statement concerns all Jacobi parameters, all polynomial degrees simultaneously, complex coefficients, or an unrestricted \(L^2\to L^4\) semigroup norm. The exact scalar formula defines a generally transcendental contractivity time, not an elementary closed form for it. Possible previously unindexed weighted-character inequalities remain a priority risk; there has been no independent external mathematical audit.

## References
- C. Balderrama and W. Urbina, *Fractional Integration and Fractional Differentiation for d-dimensional Jacobi Expansions*, arXiv:math/0608639, first posted August 25, 2006. Sections 1–3 give the polynomial eigenfunctions and the Jacobi semigroup.
- A. H. Dooley and S. K. Gupta, *On norms of trigonometric polynomials on SU(2)*, Pacific Journal of Mathematics **175** (1996), 491–509. DOI and text accessible through the journal archive.
- *High-weight parity localization of central fourth moments on SU(2)*, published mathematical record 00a2a7bedf04 (2026), particularly its finite-correction formula and explicitly asymptotic scope.
- T. H. Koornwinder, *Clebsch-Gordan coefficients for su(2) and Hahn polynomials*, Stichting Mathematisch Centrum preprint ZW 160/81 (1981), for the classical product-decomposition context.
