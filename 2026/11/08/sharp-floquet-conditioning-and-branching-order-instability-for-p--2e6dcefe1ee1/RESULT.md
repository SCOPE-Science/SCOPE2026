# Sharp Floquet conditioning and branching-order instability for periodic tree shifts

## Finding
Consider an unweighted backward parent shift \(S\) on a rooted spherically homogeneous tree with positive, periodic offspring numbers \(b_0,b_1,\ldots,b_{p-1}\), repeated indefinitely, where \(p\ge 2\) and at least one \(b_j\ge2\). Let \(w_j=\sqrt{b_j}\), and let \(C\) denote the \(p\)-by-\(p\) cyclic weighted-shift matrix given by \(Ce_j=w_j e_{j+1\pmod p}\). For \(r\ge0\), write \(s(r)=\sigma_{\min}(C-rI)\). Then the **sharp global surjectivity modulus** satisfies
\[
\inf_{\|h\|=1}\|(S^*-\overline\lambda I)h\|=s(|\lambda|)\qquad(\lambda\in\mathbb C).
\]
In particular \(S-\lambda I\) is onto exactly when \(|\lambda|\ne r_*\), where \(r_*=(\prod_{j=0}^{p-1} b_j)^{1/(2p)}\); where it is onto, the least possible operator norm of a bounded right inverse is exactly \(1/s(|\lambda|)\). The radius \(r_*\) is the sole circle where the range is dense but nonclosed. The point spectrum is the open disk of radius \(r_*\), and every eigenspace in that disk is infinite-dimensional; the full spectrum is the corresponding closed disk. These spectral consequences agree with the established growth-radius theory; the new quantitative assertion is the exact, all-parameter surjectivity modulus and its critical conditioning law.

There is an exact, strictly positive critical coefficient. Put \(a_0=1\) and
\[
a_j=\frac{\prod_{k=0}^{j-1}w_k}{r_*^j}\quad(1\le j<p),\qquad
L=\frac{p}{\sqrt{\left(\sum_{j=0}^{p-1}a_j^2\right)\left(\sum_{j=0}^{p-1}a_j^{-2}\right)}}.
\]
As \(r\to r_*\),
\[
s(r)=L|r-r_*|+O((r-r_*)^2),\qquad 0<L\le1.
\]
Equality \(L=1\) holds **if and only if all offspring numbers are equal**. Thus any nontrivial periodic modulation strictly worsens the sharp right-inverse blow-up coefficient, even when its geometric-mean branching radius is unchanged.

Branching order matters beyond the geometric mean. For \(d\ge2\), the period-four patterns \((1,d,1,d)\) and \((1,1,d,d)\) have the same critical radius \(d^{1/4}\), but with \(q=\sqrt d\) their respective critical slopes are
\[
L_{\mathrm{alt}}=\frac{2\sqrt q}{1+q},\qquad
L_{\mathrm{cluster}}=\frac{4q}{(1+q)^2}=L_{\mathrm{alt}}^2<L_{\mathrm{alt}}.
\]
Hence clustered branching is strictly worse conditioned near the critical circle than alternating branching, although the qualitative spectrum is identical.

## Assumptions and scope
The tree has one root and a finite nonempty level \(H_n\) at each depth \(n\). Every vertex at depth \(n\) has exactly \(b_{n\pmod p}\) children, with each \(b_j\) a positive integer. Define \(S e_v=e_{\operatorname{parent}(v)}\) for nonroot vertices and \(Se_{\mathrm{root}}=0\). All operators and Hilbert spaces are complex, and all norms are Hilbert-space operator norms. The modulus \(s(r)\) is the minimum ordinary singular value of the *finite* matrix \(C-rI\); this is an exact formula valid for every \(r\), not a large-level approximation. The new modulus theorem holds for all finite periods, and the explicit rearrangement comparison uses period four.

## Proof
**1. Canonical orthogonal shift channels.** On \(\ell^2(V)\), define \(Ue_v=b_{|v|}^{-1/2}\sum_{u\in\operatorname{Chi}(v)}e_u\). Disjoint children make \(U\) an isometry. For \(D e_v=\sqrt{b_{|v|}}e_v\) one has \(S^*=UD\). Let \(H_n\) be the level-\(n\) coordinate subspace and set \(K_0=H_0\) and \(K_n=H_n\ominus UH_{n-1}\) for \(n\ge1\). Induction using \(H_n=UH_{n-1}\oplus K_n\) gives the orthogonal decomposition
\[
\ell^2(V)=\bigoplus_{n\ge0}\bigoplus_{j\ge0}U^jK_n.
\]
The terms at a fixed level are orthogonal because each later-arriving wandering term is perpendicular to the image of the preceding level. Since \(U^jK_n\subset H_{n+j}\), the map \(S^*\) sends \(U^j k\) to \(w_{n+j}U^{j+1}k\). After choosing an orthonormal basis of each \(K_n\), this is an orthogonal direct sum of scalar forward unilateral shifts \(W_n\) with weights \(w_n,w_{n+1},\ldots\). Periodicity makes these shifts cyclic phase translates of a single pattern, but the argument below treats all phases simultaneously.

**2. Exact bilateral comparison.** Extend a phase-shifted periodic weight sequence to all integer indices and denote the resulting bilateral forward shift by \(B_n\). The unilateral operator \(W_n-rI\) is the restriction of \(B_n-rI\) to nonnegative-coordinate vectors, extended by zero to negative coordinates; hence
\[
m(W_n-rI):=\inf_{\|x\|=1}\|(W_n-rI)x\|\ \ge\ m(B_n-rI).
\]
Conversely, any compactly supported bilateral test vector can be translated by a multiple of \(p\) into the nonnegative half-line without changing its residual norm. Such vectors are dense, so the reverse inequality holds. Thus every unilateral channel has exactly the same lower modulus as its periodic bilateral extension. Multiplication by a diagonal sequence of phases shows \(m(W_n-\overline\lambda I)=m(W_n-|\lambda|I)\), so the answer is radial. The orthogonal sum in Step 1 preserves the common lower modulus.

**3. One cyclic finite matrix, rather than an infinite operator.** The discrete Fourier transform over periods realizes the bilateral shift as the direct integral of matrices \(C(\theta)\) obtained from \(C\) by multiplying its wraparound entry by \(e^{i\theta}\). It follows that
\[
m(B_n-rI)^2=\min_{\theta\in[0,2\pi]}\lambda_{\min}\big((C(\theta)-rI)^*(C(\theta)-rI)\big).
\]
For any finite vector \(z\), taking absolute values coordinatewise and using \(|a-b|\ge\big||a|-|b|\big|\) in each cyclic edge gives
\[
\|(C(\theta)-rI)z\|^2\ge \|(C-rI)|z|\|^2\ge \sigma_{\min}(C-rI)^2\|z\|^2.
\]
At \(\theta=0\), equality in the minimum over twists is tautologically available. Therefore \(m(B_n-rI)=\sigma_{\min}(C-rI)\), proving the exact global formula. The determinant of \(C-rI\) vanishes at nonnegative \(r\) precisely when \(r^p=\prod w_j\), which is the stated \(r_*\). By the Hilbert closed-range theorem, \(S-\lambda I\) is onto iff the adjoint is bounded below. For a surjective operator \(A\), the Moore–Penrose right inverse \(A^*(AA^*)^{-1}\) has minimum possible norm \(1/m(A^*)\). At \(r=r_*\), the unilateral forward channels are injective but have arbitrarily small residuals, so \(S-\lambda I\) has dense nonclosed range.

**4. Critical singular-value coefficient.** The positive vector \(a=(a_0,\ldots,a_{p-1})\) satisfies \(Ca=r_*a\), and \(a^{-1}\) componentwise satisfies \(C^*a^{-1}=r_*a^{-1}\). The eigenvalue \(r_*\) of \(C\) is simple (its other eigenvalues are the distinct \(p\)-th-root rotations of \(r_*\)), so \(C-r_*I\) has one-dimensional kernel and cokernel. First-order singular-value perturbation for \(C-rI\), or its elementary Schur complement across the one-dimensional kernel/cokernel, yields
\[
\lim_{r\to r_*}\frac{\sigma_{\min}(C-rI)}{|r-r_*|}
=\frac{|\langle a^{-1},a\rangle|}{\|a^{-1}\|\|a\|}=L.
\]
The error is \(O((r-r_*)^2)\): the complementary block of \(C-r_*I\) is invertible and the scalar Schur complement is linear to first order. Since \(\sum a_j a_j^{-1}=p\), Cauchy–Schwarz gives \(L\le1\), with equality precisely when all \(a_j\) are the same. Together with \(a_{j+1}/a_j=w_j/r_*\), this is equivalent to constant offspring numbers.

**5. Rearrangement and spectral boundaries.** For period four, insert the weights \((1,q,1,q)\) or \((1,1,q,q)\) into the formula for \(a_j\). Their squared-coordinate profiles, respectively, are \((1,q^{-1},1,q^{-1})\) and \((1,q^{-1},q^{-2},q^{-1})\). The claimed slopes follow immediately; the inequality is strict for \(q>1\). Finally, the scalar backward adjoints \(W_n^*\) have eigenvectors determined recursively by \(x_{j+1}=\lambda x_j/w_{n+j}\). The sequence lies in \(\ell^2\) precisely for \(|\lambda|<r_*\), because products of weights grow as \(r_*^j\) times a bounded nonzero periodic factor. Infinitely many branching levels give infinitely many mutually orthogonal channels and hence infinite-dimensional eigenspaces. The spectral-radius identity \(r(S)=r_*\) follows from the exact periodic product growth of powers. These statements complete the asserted spectral description.

## Verification
The accompanying `checker.py` reproduces independent finite-period matrix tests for the Floquet expression, critical eigenvectors and rearrangement coefficients, and compares the predicted sharp modulus against finite unilateral truncations. It uses only Python 3, NumPy and SciPy. Its finite checks do not prove the infinite-dimensional reduction; Steps 1–5 above do. To reproduce, run `python checker.py` in the same directory.

## Relationship to prior work
Buckley and Seco (arXiv:2610.40089v1, 2026) establish a branching-growth criterion for Rota universality and the outer spectral radius of the backward tree shift; their theorem determines qualitative radius information for these periodic trees but not an all-radius optimal right-inverse constant. Budzyński, Dymek, Płaneta and Ptak (arXiv:1702.00765, 2017) develop Wold-type decompositions for forward weighted shifts on trees; the orthogonal channel mechanism is credited as prior structural input. Mandal and Trivedi (arXiv:2508.00763, 2025) analyze unitary models for balanced tree shifts. Classical Floquet theory supplies the bilateral periodic reduction and is not claimed as new. The two-periodic scalar recurrence norm law and earlier tree-shift radius/modulus examples provide further prior benchmarks. The contribution here is the resulting **exact sharp minimum-modulus identity for all finite branching periods**, its explicit critical coefficient, and strict dependence on the ordering of the same offspring multiset.

## Limitations
The tree must be rooted and spherically homogeneous with finitely periodic, positive integer offspring counts; the formula is not asserted for arbitrary nonperiodic or nonradial trees. At the critical circle the range is nonclosed; no bounded right inverse exists there. The exact finite cyclic-matrix formula need not reduce to an elementary radical for general periods. The critical expansion is for each fixed pattern and is not uniform in unbounded period or offspring counts. The qualitative spectral facts are established in earlier general forms and are not an independent novelty claim. Prior literature on general periodic Jacobi operators may provide related finite-matrix reductions; priority beyond the checked sources is not certified.

## References
1. Jeremiah Buckley and Daniel Seco, *Rota universality of shifts on trees*, arXiv:2610.40089v1, first posted 2026-10-29, especially Theorem 1 and Section 3.
2. P. Budzyński, P. Dymek, A. Płaneta and M. Ptak, *Weighted shifts on directed trees: their multiplier algebras, reflexivity and decompositions*, arXiv:1702.00765 (2017), Wold-type decomposition section.
3. Shubhankar Mandal and Shailesh Trivedi, *Unitary equivalence of balanced weighted shifts on rooted directed trees*, arXiv:2508.00763v1 (2025).
4. P. R. Halmos, *A Hilbert Space Problem Book*, second edition, Springer (1982), standard closed-range and shift facts.
