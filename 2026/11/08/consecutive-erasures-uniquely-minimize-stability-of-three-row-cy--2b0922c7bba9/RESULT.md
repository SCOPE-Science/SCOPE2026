# Consecutive erasures uniquely minimize stability of three-row cyclic harmonic frames

## Finding
For every integer \(N\ge6\), set \(\omega=e^{2\pi i/N}\) and consider the Parseval cyclic harmonic frame in \(\mathbb C^3\)
\[
\varphi_j=N^{-1/2}(1,\omega^j,\omega^{2j})^{\mathsf T},\qquad j\in\mathbb Z_N.
\]
For every three-element erasure set \(E\subset\mathbb Z_N\), its retained frame operator is \(S_E=\sum_{j\notin E}\varphi_j\varphi_j^*\). Define
\[
 a_N=\frac{1+2\cos(2\pi/N)}3,\qquad b_N=\frac{1+2\cos(4\pi/N)}3,
\]
and
\[
 \Lambda_N=1+\frac{b_N+\sqrt{b_N^2+8a_N^2}}2.
\]
Then the sharp, strictly positive lower stability bound is
\[
 \boxed{\lambda_{\min}(S_E)\ \ge\ 1-\frac3N\Lambda_N>0.}
\]
**Equality holds if and only if** \(E\) consists of three cyclically consecutive coefficient positions \(\{k,k+1,k+2\}\) modulo \(N\). There are exactly \(N\) such erased sets. Thus a three-consecutive mask is the unique worst geometry up to cyclic translation, including the small exceptional orders \(N=6,7\).

## Assumptions and scope
The signal space is \(\mathbb C^3\) with its usual Hermitian norm. All frame coefficients are labelled by \(\mathbb Z_N\). Erasing a coefficient removes the corresponding rank-one term from the analysis operator. We consider exactly three **distinct** erased labels, uniformly weighted frame atoms, and every integer \(N\ge6\). This is a worst-case retained lower frame bound, not an average reconstruction error or a condition number of the erased submatrix. The operator is positive definite for every admitted erasure mask.

## Proof
**1. Parseval reduction and real three-point Gram matrix.** The orthogonality of the three distinct characters \(1,\omega^j,\omega^{2j}\) on \(\mathbb Z_N\) gives \(\sum_j\varphi_j\varphi_j^*=I_3\). Let \(v_j=\sqrt{N/3}\,\varphi_j=(1,\omega^j,\omega^{2j})^{\mathsf T}/\sqrt3\). If \(E\) has three elements, the nonzero eigenvalues of \(\sum_{j\in E}v_jv_j^*\) equal those of its \(3\times3\) Gram matrix. Multiplying the \(j\)-th Gram column by \(\omega^{-j}\), and its row by the conjugate, makes its entries real:
\[
G_E(j,k)=g_N(j-k),\qquad
 g_N(d)=\frac{1+2\cos(2\pi d/N)}3.
\]
In particular \(G_E\) has diagonal entries \(1\), and
\[
\lambda_{\min}(S_E)=1-\frac3N\lambda_{\max}(G_E).
\]
Thus it is enough to determine the exact maximal largest eigenvalue of the real Gram matrices for three distinct cyclic positions.

**2. The consecutive candidate.** For \(E=\{k,k+1,k+2\}\), translation invariance gives the real symmetric matrix
\[
 C_N=\begin{pmatrix}1&a_N&b_N\\a_N&1&a_N\\b_N&a_N&1\end{pmatrix}.
\]
For \(N\ge6\) we have \(a_N>0\) and \(b_N\ge0\). Its antisymmetric eigenvector has eigenvalue \(1-b_N\). On the symmetric two-dimensional subspace the eigenvalues are \(1+\frac12(b_N\pm\sqrt{b_N^2+8a_N^2})\). The plus sign gives the Perron eigenvalue \(\Lambda_N\), strictly larger than every other eigenvalue. This proves that the announced bound and its candidates are attainable.

**3. Uniform strict comparison for \(N\ge8\).** Write \(d\) for the least cyclic distance between two distinct indices. The function \(g_N(d)\) decreases on the integer interval \(1\le d\le\lfloor N/2\rfloor\), with minimum at least \(-1/3\). For \(N\ge8\), \(b_N\ge1/3\), and \(a_N>b_N>0\). It follows that
\[
 |g_N(d)|\le a_N\quad(d\ge1),\qquad
 |g_N(d)|\le b_N\quad(d\ge2).
\]
Any three distinct sites have at least one pair at cyclic distance at least two. Relabel that pair as vertices \(1,3\) of the Gram matrix. Then \(|G_E|\le C_N\) entrywise. For every real vector \(x\),
\[
 x^{\mathsf T}G_Ex\le |x|^{\mathsf T}|G_E||x|\le |x|^{\mathsf T}C_N|x|,
\]
whence \(\lambda_{\max}(G_E)\le\lambda_{\max}(C_N)=\Lambda_N\). The Perron eigenvector of \(C_N\) has all entries strictly positive because \(a_N>0\), so strict entrywise deficiency in a comparison implies strict spectral inequality. Equality therefore forces two pairs to have distance exactly one and the third pair to have distance two (the only way to attain both \(a_N\)-entries); this is precisely a cyclic consecutive triple. For \(N=8\), the equality \(|g_N(4)|=b_N\) cannot create another extremizer, because having two distance-one pairs already forces the third distance to be two. The case \(N\ge8\) follows.

**4. The order \(N=6\).** Cyclic gap types for three labels, up to permutation, are \((1,1,4)\), \((1,2,3)\), and \((2,2,2)\). Since \(g_6(1)=2/3\), \(g_6(2)=0\), and \(g_6(3)=-1/3\), their largest Gram eigenvalues are respectively
\[
 1+\frac{2\sqrt2}{3},\qquad 1+\frac{\sqrt5}{3},\qquad 1.
\]
The first is strictly the largest, and it is exactly the consecutive case.

**5. The order \(N=7\).** Put \(a=g_7(1)\), \(b=g_7(2)\), and \(c=-g_7(3)\), so \(a>c>b>0\). The cyclic gap types are \((1,1,5)\) (consecutive), \((1,2,4)\), \((1,3,3)\), and \((2,2,3)\). The latter two types other than \((1,3,3)\) have absolute off-diagonal weights \((a,b,c)\) and \((b,b,c)\), respectively; after permuting vertices they are strictly entrywise dominated by the weights \((a,a,b)\) of the consecutive Gram matrix. Thus their largest eigenvalues are strictly below \(\Lambda_7\), by the same positive-eigenvector argument.

For the remaining \((1,3,3)\) type, the absolute off-diagonal weights are \((a,c,c)\), so the maximal absolute row sum is \(1+a+c\). On the other hand \(\Lambda_7>1+\sqrt2a\), since \(b>0\). Finally \(c<(\sqrt2-1)a\): indeed, using \(2\pi/7<3\pi/10\) and \(\pi/7>\pi/8\), elementary cosine monotonicity gives \(a>(1+2\cos(3\pi/10))/3>0.72\) and \(c<(2\cos(\pi/8)-1)/3<0.29\), while \(\sqrt2-1>0.41\) gives \((\sqrt2-1)a>0.2952>0.29\). Therefore \(\lambda_{\max}(G_E)\le1+a+c<\Lambda_7\) for this type too. Order seven is settled.

**6. Strict positivity and exact equality count.** Every triple of distinct atoms \(v_j\) is linearly independent: the corresponding Vandermonde determinant is a nonzero product of pairwise differences of distinct \(N\)-th roots. Since \(N-3\ge3\), any retained subset contains a spanning triple. Thus \(S_E\) is strictly positive, proving \(1-3\Lambda_N/N>0\). The preceding strict spectral comparisons show that exactly the \(N\) cyclic translates of \(\{0,1,2\}\) are equality masks; for \(N\ge6\) these translated three-element sets are distinct. This completes the proof.

## Verification
The standalone file `checker.py` uses Python 3 and NumPy. For each \(6\le N\le36\), it enumerates every unordered erased triple, constructs its real Gram matrix from the original Fourier-character formula, and numerically computes its largest eigenvalue. It checks the explicit radical, positivity and the exact set of equality masks, with a conservative numerical tolerance. Separate explicit assertions check the exceptional order-six formulas and the order-seven rational enclosure. A successful run prints `THREE_ROW_ERASURE_PASS`. The finite replay is diagnostic; the proof above establishes the full theorem for all integers \(N\ge6\).

## Relationship to prior work
Marshall and Waldron's arXiv:1611.07121v1 constructs and enumerates cyclic harmonic frames through Fourier characters and explicitly lists erasures as a motivating application. Its main mathematical theorems concern counts of unitary equivalence classes, not the worst spectral loss under exactly three erasures. Cheng, Lv and Sun (2018) characterize frames for which *every* fixed-size subframe has identical bounds; their uniform-subframe criterion does not determine which erasure mask is worst for the nonuniform three-row family here. Batenkov, Demanet, Goldman and Yomdin (2018) give bounds for clustered-node partial Fourier singular values in a substantially broader off-grid setting; these do not imply the exact discrete extremum or uniqueness count here.

The published result *Exact adversarial-erasure spectra for two-character cyclic harmonic frames* determines the analogous problem for **two** Fourier rows, including larger erasure sizes. It explicitly does not treat three-row frames. The published result *Sharp Riesz conditioning for consecutive triples on finite cycles* treats the same three-row Gram family but **minimizes the ratio** of extreme Gram eigenvalues, and its optimal erased-node geometry is almost equilateral, opposite to the present maximization of the **largest** eigenvalue. The published result *A complete full-spark criterion for every three-row Fourier pattern* settles invertibility of three-column minors, not their spectral sizes or erasure-mask extremizers. None of the inspected mathematical claims implies the exact constant and unique consecutive-erasure equality class above.

## Limitations
This theorem concerns the first nontrivial three-row, three-erasure case; it does not classify four or more erased coefficients, arbitrary three-row Fourier patterns, weighted masks or optimal nonlinear decoders. The perturbation inequalities are elementary matrix tools, and an equivalent unindexed rearrangement result or engineering frame-bound calculation may predate this account. Originality is a literature-dependent assessment rather than a guarantee of historical priority. Numerical replay cannot establish the universal claim; the argument in Steps 1–6 does so.

## References
1. S. Marshall and S. Waldron, *On the number of harmonic frames*, arXiv:1611.07121v1 (first public 2016-11-22), especially Sections 1–3. Primary MSC 42C15, 94A12.
2. Q. Cheng, F. Lv and W. Sun, *Frames of uniform subframe bounds with applications to erasures*, Linear Algebra Appl. 555 (2018), 186–200, DOI:10.1016/j.laa.2018.05.025.
3. D. Batenkov, L. Demanet, G. Goldman and Y. Yomdin, *Conditioning of partial nonuniform Fourier matrices with clustered nodes*, arXiv:1809.00658 (2018), later SIAM J. Matrix Anal. Appl. 41 (2020), 199–220.
4. *Exact adversarial-erasure spectra for two-character cyclic harmonic frames*, published mathematical result: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-adversarial-erasure-spectra-for-two-character-cyclic-harmo--e1e03f96b6f0.
5. *Sharp Riesz conditioning for consecutive triples on finite cycles*, published mathematical result: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-riesz-conditioning-for-consecutive-triples-on-finite-cycle--1200745c9cae.
6. *A complete full-spark criterion for every three-row Fourier pattern*, published mathematical result: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-complete-full-spark-criterion-for-every-three-row-fourier-patt--843fec171d5a.
