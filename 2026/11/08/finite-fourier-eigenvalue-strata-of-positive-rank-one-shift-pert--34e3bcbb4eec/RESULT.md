# Finite Fourier eigenvalue strata of positive rank-one shift perturbations

## Finding
Fix an integer \(m\ge 2\), let \(\zeta=\exp(2\pi i/m)\), and write \(\mu_m=\{\zeta^k:0\le k<m\}\). Every subset \(E\subseteq\mu_m\setminus\{1\}\) satisfying \(E=\overline E\) is the **entire point spectrum** of a positive operator on the standard complex Banach lattice \(\ell_1\), even when the operator differs by an arbitrarily small, positive, rank-one operator from a fixed positive isometry. More precisely, the operators can all be chosen from the single natural family
\[
 T_a(x,v)=\big(Sx+e_0\sum_{j=0}^{m-1}a_jv_j,\;Pv\big)
 \quad\text{on}\quad X=\ell_1(\mathbb N_0)\oplus_1\mathbb C^m,
\]
where \(a_j>0\), \(Se_j=e_{j+1}\), and \(Pe_j=e_{j+1\pmod m}\). The space \(X\) is lattice-isometric to \(\ell_1\).

For every such positive vector \(a\), the complete spectral and power-norm formulae are
\[
\begin{gathered}
\sigma(T_a)=\{z:|z|\le1\},\qquad
\sigma_{\mathrm{ess}}(T_a)=\sigma_{\mathrm{ap}}(T_a)=\{z:|z|=1\},\\
\sigma_{\mathrm p}(T_a)=\left\{\zeta^k:\sum_{j=0}^{m-1}a_j\zeta^{-kj}=0\right\},\\
\|T_a^n\|=1+\max_{0\le j<m}\sum_{h=0}^{n-1}a_{j+h\pmod m}
\quad(n=0,1,2,\ldots),\\
\lim_{n\to\infty}\frac{\|T_a^n\|}{n}=\frac1m\sum_{j=0}^{m-1}a_j>0.
\end{gathered}
\]
Every eigenvalue is geometrically simple. The Fredholm index of \(\lambda I-T_a\) is \(-1\) for \(|\lambda|<1\) and zero for \(|\lambda|>1\).

The parameter set realizing a fixed \(E\) is a **nonempty relatively open subset of a real linear subspace of codimension exactly \(|E|\)** inside \(\mathbb R^m\). The empty-spectrum stratum is open and dense among all positive couplings. Every stratum accumulates at the zero coupling: for any \(\varepsilon>0\) its operators may be chosen with
\[
\|T_a-(S\oplus P)\|=\max_j a_j<\varepsilon.
\]
Thus arbitrarily small positive rank-one perturbations of a power-bounded isometry can produce *any* conjugation-symmetric root-of-unity eigenvalue pattern that omits \(1\), despite unchanged full and essential spectra. The exact linear growth formula quantifies why the perturbed operators no longer satisfy the growth hypotheses used in peripheral-point-spectrum cyclicity theorems on \(\ell_1\).

## Assumptions and scope
All spaces are over \(\mathbb C\). Positivity uses the coordinatewise Banach-lattice order. The direct sum has the sum norm \(\|(x,v)\|=\|x\|_1+\|v\|_1\). The unilateral right shift \(S\) acts on coordinates indexed by \(\mathbb N_0\), \(P\) permutes the \(m\) finite coordinates, and \(a\in(0,\infty)^m\) is real. The essential spectrum is the Fredholm essential spectrum; the approximate-point spectrum uses unit approximate eigenvectors. The theorem concerns the displayed rank-one block family, not all positive operators. No irreducibility, stochasticity or power boundedness is asserted for \(T_a\).

## Proof
**1. Exact eigenvalue test.** Since the unilateral right shift has no eigenvalues, an eigenpair \(T_a(x,v)=\lambda(x,v)\) must have \(v\ne0\) and \(Pv=\lambda v\). Therefore \(\lambda=\zeta^k\) for some \(0\le k<m\) and, after scaling, \(v_j=\lambda^{-j}\). The other block equation is
\[
 (\lambda I-S)x=c e_0,\qquad c=\sum_{j=0}^{m-1}a_j\lambda^{-j}.
\]
The coordinate recurrence forces \(x_n=c\lambda^{-(n+1)}\) for all \(n\ge0\). Since \(|\lambda|=1\), this sequence belongs to \(\ell_1\) exactly when \(c=0\). Then \(x=0\) and the eigenspace is the one-dimensional eigenspace of \(P\). The zeroth Fourier coefficient \(\sum_j a_j\) is strictly positive, so \(1\) cannot be an eigenvalue.

**2. Converse construction and strata.** Let \(K\subseteq\{1,\ldots,m-1\}\) index \(E\), and let \(A=\{1,\ldots,m-1\}\setminus K\). Because \(E=\overline E\), both \(K\) and \(A\) are invariant under \(k\mapsto -k\pmod m\). Define
\[
 b_j=1+\frac1m\sum_{k\in A}\zeta^{jk}\qquad(0\le j<m).
\]
Conjugate pairing makes \(b_j\) real, while \(b_j\ge1-|A|/m\ge1/m>0\). Character orthogonality gives the **exact** Fourier coefficients
\[
 \sum_{j=0}^{m-1}b_j\zeta^{-\ell j}=
 \begin{cases}m,&\ell=0,\\0,&\ell\in K,\\1,&\ell\in A.\end{cases}
\]
Therefore \(a=\delta b\), for any \(\delta>0\), realizes precisely \(E\). Arbitrary smallness follows by scaling. The discrete Fourier transform is a real-linear isomorphism between real \(a\)-vectors and conjugate-symmetric Fourier vectors. Requiring all coefficients indexed by \(E\) to vanish imposes exactly \(|E|\) independent real linear equations (a conjugate pair contributes two, and the real root \(-1\), when present, one). Requiring the remaining nonzero Fourier coefficients not to vanish is relatively open; our explicit \(b\) proves nonemptiness. For \(E=\varnothing\), the complement of finitely many proper Fourier-kernel subspaces is open and dense inside the positive cone.

**3. Norms, spectrum and Fredholm data.** The operator is positive because every matrix coefficient is nonnegative. It differs from \(T_0=S\oplus P\) by the rank-one operator \((x,v)\mapsto(e_0\sum_ja_jv_j,0)\), of norm \(\max_ja_j\). Iteration gives
\[
T_a^n(x,v)=\left(S^nx+\sum_{h=0}^{n-1}S^{n-1-h}e_0\sum_ja_j(P^hv)_j,\;P^nv\right).
\]
On each positive basis vector of the finite summand the chain coordinates have disjoint supports, and the output \(\ell_1\) norm is \(1+\sum_{h=0}^{n-1}a_{j+h\pmod m}\). On a chain basis vector it is \(1\). The norm of a nonnegative \(\ell_1\)-matrix is the supremum of its column sums, proving the exact formula. Splitting \(n\) into full cycles plus a remainder proves the growth limit.

The upper triangular block resolvent shows \(\sigma(T_a)=\sigma(S)\cup\sigma(P)=\{z:|z|\le1\}\). Finite-rank stability of Fredholmness and index reduces the essential spectrum to that of \(S\), namely the unit circle; \(\lambda I-S\) has index \(-1\) on the open disk and is invertible outside the closed disk. On the unit circle, long normalized blocks of the form \((1,\lambda^{-1},\ldots,\lambda^{-N},0,\ldots)\) form approximate eigenvectors of \(S\), hence of \(T_a\), For \(|\lambda|<1\), the reverse-triangle bound \(\|(\lambda I-S)x\|_1\ge(1-|\lambda|)\|x\|_1\) and invertibility of \(\lambda I-P\) show that the upper triangular operator \(\lambda I-T_a\) is bounded below. Outside the closed disk it is invertible. This proves the approximate-point-spectrum formula.

## Verification
A standalone finite checker, `checker.py`, verifies the inverse Fourier construction for all conjugation-symmetric index subsets in sizes \(2\le m\le16\), checks explicit positivity and Fourier selection, and reproduces finite-section power-norm identities by integer matrix multiplication for three families of couplings in sizes \(2\le m\le8\). It reports `POSITIVE_FOURIER_LEAKAGE_FINITE_OK 38474`. The infinite-dimensional claims are proved analytically above; the checker is not an infinite proof.

## Relationship to prior work
Dobrick, *On the Cyclicity Conjecture* (arXiv:2610.10093, first publicly submitted October 7, 2026), Theorem 1.2, proves cyclicity of the **full peripheral spectrum** of every positive Banach-lattice operator. Its Section 2 proves spectral inheritance under positive domination and Section 3 proves cyclicity by critical minorants and ultrapowers; neither constructs the rank-one Fourier coupling or classifies its point-spectrum patterns. The present operators have the entire circle as their peripheral spectrum, so they are compatible with that theorem. Their *peripheral point spectra* are freely prescribed finite patterns.

Glück, *On the Peripheral Spectrum of Positive Operators* (arXiv:1503.02430), Example 5.4, already constructs positive operators with the point spectrum of the form \(G\setminus\{1\}\) for a subgroup \(G\) of the circle. Example 6.2 contains a specific Markov example with a missing eigenvalue \(-1\) despite an eigenvalue \(i\), originating from Glück's 2014 note. These counterexamples are not claimed as new. The difference here is a complete inverse classification for **all** conjugate-symmetric subsets of a fixed root set within one explicitly parameterized rank-one family on the KB-space \(\ell_1\), including the exact codimension and norm-growth formulae and arbitrary proximity to a positive isometry. Glück's 2021 paper (arXiv:2102.03772) realizes finite unions of finite subgroups as the **full** peripheral spectra of irreducible stochastic operators, a different assertion.

## Limitations
The construction is reducible and its positive perturbations are not power bounded; it does not challenge cyclicity of the full peripheral spectrum, nor the existing positive results for power-bounded operators on KB-spaces. The exact Fourier construction is elementary once this one-way leakage model is specified, and publication priority may be affected by older equivalent positive block-operator constructions not located in the literature checks. The full 2026 motivating preprint was inspected, including its spectral-domination theorem, critical-minorant construction and appendices; these develop full-spectrum cyclicity and do not contain the stated rank-one inverse point-spectrum theorem. Earlier equivalent positive block constructions remain a specific publication-priority risk. No independent audit has been performed.

## References
1. A. Dobrick, *On the Cyclicity Conjecture*, arXiv:2610.10093 (first public submission 2026-10-07), https://arxiv.org/abs/2610.10093.
2. J. Glück, *On the Peripheral Spectrum of Positive Operators*, arXiv:1503.02430 (2015), Sections 5–6, https://arxiv.org/abs/1503.02430.
3. J. Glück, *A Markov Operator and a Markov Semigroup on \(C(K)\) with Non-Cyclic Peripheral Point Spectrum*, preprint dated 2014-03-01, https://www.uni-ulm.de/fileadmin/website_uni_ulm/mawi.inst.020/glueck/Dateien_fuer_Homepage/Artikel_und_Preprints/J_Glueck_Markov_Operators_with_Non_Cyclic_Peripheral_Point_Spectrum.pdf.
4. J. Glück, *A note on the spectrum of irreducible operators and semigroups*, arXiv:2102.03772 (2021), https://arxiv.org/abs/2102.03772.
