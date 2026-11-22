# Principal Fourier nonsingularity at order \(255\) from a characteristic-\(17\) certificate

## Finding
Let \(\zeta_N=\exp(2\pi i/N)\) and let \(F_N=(\zeta_N^{jk})_{0\le j,k<N}\). For equally sized subsets \(K,L\subseteq\mathbb Z/255\mathbb Z\), suppose that
\[
\#\{k\in K:k\equiv r\pmod {15}\}
=\#\{\ell\in L:\ell\equiv r\pmod {15}\}
\qquad(0\le r<15).
\]
Then \(\det F_{255}[K,L]\ne0\). **Consequently every principal minor of \(F_{255}\) is nonzero.** The residue-balanced conclusion is stronger than the principal statement; it is the \(15\)-principal case in the sense of Caragea–Lee–Malikiosis–Pfander.

## Assumptions and scope
Rows and columns range over all residues modulo \(255=3\cdot5\cdot17\). They may be in any order, which changes determinants only by a sign. The Fourier root may be any primitive \(255\)-th root: a Galois automorphism transfers the nonvanishing statement. The empty determinant is one by convention. The conclusion concerns exactly the residue-balanced minors above, not arbitrary minors of a composite-order Fourier matrix.

## Proof
**Finite-field model.** In characteristic \(17\), let
\[
K_0=\mathbb F_{17}[t]/(t^4+3).
\]
The residue \(-3=14\) has multiplicative order \(16\) in \(\mathbb F_{17}^{\times}\), since \(14^8\equiv-1\pmod{17}\). If \(y^4=14\), then \(y\) has multiplicative order \(64\). The order of \(17\) modulo \(64\) equals four, so \(y\) has degree four over \(\mathbb F_{17}\), proving irreducibility. Hence \(K_0\) is a field with \(17^4=83521\) elements. Elements are represented uniquely by four base-\(17\) digits; multiplication uses the reduction \(t^4=-3\).

**Two primitive-root orbits.** The standalone code deterministically obtains a primitive fifteenth root \(\omega\in K_0\), with encoded value \(38933\), and checks \(\omega^{15}=1\), \(\omega^3\ne1\), \(\omega^5\ne1\). A primitive fifteenth root has exponent in \((\mathbb Z/15\mathbb Z)^\times\). Frobenius \(x\mapsto x^{17}\) acts on exponents by multiplication by two modulo fifteen, splitting the eight exponents into precisely
\[
\{1,2,4,8\}\quad\text{and}\quad\{7,14,13,11\}.
\]
Therefore it is necessary and sufficient to test the two roots \(\omega\) and \(\omega^7\), rather than just one root.

**Complete exact determinant certificate.** For each root and each nonempty subset \(S=\{s_0<\cdots<s_{k-1}\}\) of \(\{0,\ldots,14\}\), compute the principal determinant \(\det(\omega^{e s_i s_j})_{0\le i,j<k}\), with \(e=1\) or \(7\). The division-free checker uses the recurrence \(D(\varnothing)=1\) and
\[
D(T)=\sum_{j=0}^{|T|-1}(-1)^{|T|-1+j}
  \omega^{e s_{|T|-1}c_j}D(T\setminus\{c_j\}),
\]
where \(c_0<\cdots<c_{|T|-1}\) are the selected column indices in \(T\) and the first \(|T|\) rows are used. This is Laplace expansion along the last row and contains no division. An independent finite-field Gaussian-elimination implementation computes the same zero/nonzero classification via pivots and exact field inverses. For **each** orbit representative, both programs find no vanishing principal determinant among all \(32767\) nonempty subsets. The counts checked at cardinalities \(1,\ldots,15\) are
\[
15,105,455,1365,3003,5005,6435,6435,5005,3003,1365,455,105,15,1.
\]
The two orbit tests together cover every primitive fifteenth-root realization in characteristic seventeen.

**Lift to complex order \(255\).** Theorem 1.4 of Caragea, Lee, Malikiosis and Pfander (*Principal minors of Fourier matrices of square-free order*, arXiv:2505.24326) states: for square-free \(N=pN'\), if all principal minors of \(F_{N'}\) are nonzero in characteristic \(p\), then all \(N'\)-principal minors of complex \(F_N\) are nonzero. Apply it with \(p=17\), \(N'=15\). The exact certificate gives its full hypothesis. Thus every \(15\)-principal minor of \(F_{255}\), and in particular every ordinary principal minor, is nonzero.

## Verification
The self-contained files `verify_255.cpp` and `verify_255_gauss.cpp` independently check the complete finite-field hypothesis. Compile each with `g++ -std=c++17 -O3`; their inputs are fixed and no external data or libraries beyond standard C++ are needed. The first program prints `PASS` twice with \(32767\) nonzero determinants per orbit; the other ends `GAUSSIAN_OK` after reporting `bad=0` twice. Reproduction needs exact arithmetic and the separately identified published lifting theorem. This is not a direct enumeration of the exponentially many principal minors of order \(255\).

## Relationship to prior work
Tao's 2003 prime-cycle uncertainty theorem is a classical introduction to the Fourier-minor nonvanishing problem. Caragea and Lee (2024) formulated the all-principal-minors conjecture for square-free orders. Caragea–Lee–Malikiosis–Pfander (2025) proved the lifting theorem used here and established the conjecture for orders of the form \(2p,3p,5p,6p,7p\) with \(p\) prime, as well as sufficiently spaced prime products; those stated families and bounds do not yield the specific order \(255=3\cdot5\cdot17\). Gu–Zhou–Wang (2026) subsequently established the distinct orders \(70\) and \(143\) by other finite-field certificates. Earlier publicly available computations also address order \(154\) and a characteristic-seven singularity classification for the **base order fifteen**; neither implies the characteristic-seventeen base certificate established here. The order-\(255\) statement was not found under searches for its principal, residue-balanced and finite-characteristic formulations. This is a bounded priority assessment, not a claim of absolute novelty.

## Limitations
This proof depends on the published lifting theorem and a finite exhaustive computation. The exact check covers all primitive-root embeddings in characteristic \(17\) but not all characteristics. It neither proves the conjecture for every square-free order nor asserts arbitrary nonprincipal minors are nonzero. The 2026 order-\(70\)/\(143\) paper was compared from publicly available abstract-level and explanatory material, rather than its complete PDF; an unindexed equivalent treatment of order \(255\) remains possible. Independent verification outside the present mathematical package has not been conducted.

## References
1. T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286, first publicly posted 2003-08-29.
2. A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, arXiv:2409.09793 (2024).
3. A. Caragea, D. G. Lee, R. D. Malikiosis and G. E. Pfander, *Principal minors of Fourier matrices of square-free order*, arXiv:2505.24326 (first posted 2025-05-30), Theorems 1.3–1.5 and Definition 3.2.
4. J. Gu, L. Zhou and Y. Wang, *Principal nonsingularity of the Fourier matrices of orders 70 and 143*, arXiv:2608.17746 (2026).
5. *Principal nonsingularity of the order-154 Fourier matrix*, public mathematical research record (2026).
6. *Exact characteristic-seven principal-minor defects of the order-fifteen Fourier matrix*, public mathematical research record (2026).
