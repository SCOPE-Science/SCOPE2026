# Sharp three-erasure stability of three-frequency cyclic harmonic frames

## Finding
For every integer \(N\ge 6\), let \(F_N\) be the \(3\times N\) Parseval cyclic Fourier matrix with entries
\[
(F_N)_{kj}=N^{-1/2}e^{2\pi i kj/N},\qquad k\in\{0,1,2\},\quad j\in\mathbb Z_N.
\]
For an unordered three-element erasure set \(E\subset\mathbb Z_N\), the retained analysis frame has optimal lower squared frame bound
\[
A_N(E)=\lambda_{\min}\bigl(F_{N,E^c}F_{N,E^c}^{*}\bigr).
\]
Set
\[
d_1=1+2\cos(2\pi/N),\qquad d_2=1+2\cos(4\pi/N).
\]
Then the **exact globally worst retained bound** is
\[
\boxed{\min_{|E|=3}A_N(E)
=1-\frac{1}{N}\left(3+\frac{d_2+\sqrt{d_2^2+8d_1^2}}2\right).}
\]
The inequality is strict for every nonconsecutive erasure triple: equality holds **if and only if**
\[
\boxed{E=\{a,a+1,a+2\}\pmod N\quad\text{for some }a\in\mathbb Z_N.}
\]
There are exactly \(N\) distinct worst erasure sets. The sharp retained bound is positive for every \(N\ge6\); in particular, every three-coefficient erasure leaves a spanning frame.

## Assumptions and scope
The original \(N\) coefficient positions are distinct labelled members of \(\mathbb Z_N\). A deletion discards three distinct indices; no measurement reweighting or decoder optimization is allowed. Every column of \(F_N\) has squared norm \(3/N\), and \(F_NF_N^*=I_3\). All bounds here are **squared singular values**, so the smallest singular value of a retained matrix is the square root of \(A_N(E)\). “Consecutive” is cyclic: a triple may wrap around the last index. The conclusion concerns the fixed three-frequency band \(\{0,1,2\}\); it is not asserted for other bands or more than three deletions.

## Proof
**1. Real-symmetric Gram reduction.** Let \(f_j\) be column \(j\) of \(F_N\), and let \(G_E=N F_{N,E}^*F_{N,E}\). Multiplying column \(j\) by the unimodular phase \(e^{-2\pi i j/N}\) does not alter the eigenvalues and changes its unnormalized entries to \((e^{-2\pi i j/N},1,e^{2\pi i j/N})\). Hence \(G_E\) is real symmetric, with diagonal entries \(3\) and off-diagonal entries
\[
D_N(h)=1+2\cos(2\pi h/N),\qquad h\in\mathbb Z_N.
\]
The full frame is Parseval, so its retained frame operator is
\[
F_{N,E^c}F_{N,E^c}^*=I_3-F_{N,E}F_{N,E}^*.
\]
The nonzero spectra of \(F_{N,E}F_{N,E}^*\) and \(F_{N,E}^*F_{N,E}\) coincide; they are both \(3\times3\). Consequently,
\[
A_N(E)=1-\lambda_{\max}(G_E)/N.
\]
Thus we must maximize the top eigenvalue of the real three-point Dirichlet-kernel Gram matrix.

**2. Consecutive-triple spectrum.** For \(E=\{0,1,2\}\),
\[
G_*=\begin{pmatrix}3&d_1&d_2\\d_1&3&d_1\\d_2&d_1&3\end{pmatrix}.
\]
Reflection in the midpoint gives one antisymmetric eigenvector \((1,0,-1)\) with eigenvalue \(3-d_2\). The remaining two eigenvalues are
\[
3+\frac{d_2}{2}\pm\frac12\sqrt{d_2^2+8d_1^2}.
\]
For \(N\ge6\), one has \(d_1>0\) and \(d_2\ge0\); therefore the plus sign gives \(\lambda_{\max}(G_*)\). Cyclic translations conjugate Gram matrices by diagonal phases and preserve their eigenvalues, so every consecutive triple attains this value.

**3. Strict global comparison for \(N\ge8\).** Let \(h\) be the shorter cyclic distance between two distinct indices. For \(2\le h\le\lfloor N/2\rfloor\), monotonicity of cosine on \([0,\pi]\) gives
\[
-1\le D_N(h)\le D_N(2)=d_2.
\]
Here \(d_2\ge1\) for \(N\ge8\), and \(d_1>d_2>0\). Therefore
\[
|D_N(h)|\le d_2\quad(h\ge2),\qquad |D_N(1)|=d_1.
\]
A three-element set that is not three consecutive cyclic indices has at most one pair at cyclic distance one. Relabel its vertices so any such pair occupies one of the two adjacent edges of \(G_*\). The absolute-value matrix \(|G_E|\) is then bounded entrywise by \(G_*\), with a **strict** inequality in at least one off-diagonal entry. Since \(G_*\) has all entries positive, the strict Perron–Frobenius comparison yields
\[
\lambda_{\max}(G_E)\le\lambda_{\max}(|G_E|)<\lambda_{\max}(G_*).
\]
The first inequality follows directly from the Rayleigh quotient and replacing vector coordinates by absolute values; it does not assume \(G_E\) has nonnegative entries. Thus only consecutive triples maximize the erasure operator when \(N\ge8\).

**4. The seven-cycle.** Put \(d_1=D_7(1)\) and \(d_2=D_7(2)\). We have \(d_1>2\) because \(2\pi/7<\pi/3\), while
\[
d_2>1+2\cos(3\pi/5)=\frac{3-\sqrt5}{2}
\]
because \(4\pi/7<3\pi/5\). The other nonnearest Dirichlet values, at cyclic distances two and three, have absolute value strictly below one. Every nonconsecutive three-set has at most one nearest-neighbor pair, so the row-sum bound on its absolute Gram matrix gives
\[
\lambda_{\max}(G_E)\le3+d_1+1.
\]
On the other hand, evaluating the Rayleigh quotient of \(G_*\) at \((1,\sqrt2,1)\) gives
\[
\lambda_{\max}(G_*)\ge3+\sqrt2\,d_1+d_2/2.
\]
The latter is strictly greater than \(3+d_1+1\), since
\[
(\sqrt2-1)d_1+d_2/2
>2(\sqrt2-1)+\frac{3-\sqrt5}{4}>1.
\]
The last inequality is exact: \(\sqrt2>24/17\) and \(\sqrt5<9/4\) imply that its left-hand side exceeds \(14/17+3/16=275/272>1\). Therefore only consecutive triples maximize at \(N=7\).

**5. The six-cycle.** The off-diagonal kernel values at cyclic distances one, two, and three are respectively \(2,0,-1\). A nonconsecutive triple either has no nearest-neighbor pair, in which case its top Gram eigenvalue is at most \(3+2=5\), or it has exactly one such pair. In the latter case, up to a cyclic translation and reflection, its three pairwise off-diagonal magnitudes are \(2,1,0\), so the top eigenvalue is \(3+\sqrt5\). For consecutive triples, Step 2 gives \(3+2\sqrt2\), strictly larger in both cases. Again equality occurs only for consecutive triples.

**6. Positivity and equality count.** Every set of \(N-3\ge3\) retained Fourier columns contains three distinct nodes of the unit circle. The corresponding square Vandermonde submatrix, formed by rows \(0,1,2\), is invertible. Thus the retained frame has rank three and its smallest squared singular value is strictly positive. The sets \(\{a,a+1,a+2\}\) for distinct \(a\in\mathbb Z_N\) are distinct when \(N\ge6\), giving exactly \(N\) equality masks. Combining Steps 1–5 proves the displayed sharp formula and every equality case for all \(N\ge6\).

## Verification
The proof is exact and applies to all integer orders in its stated range. The self-contained standard-library program `checker.py`, run as `python3 checker.py`, independently forms the real symmetric three-erasure Gram matrix and computes its largest eigenvalue by Jacobi rotation rather than by the theorem's closed formula. It enumerates every unordered erasure triple for \(6\le N\le48\), tests the maximum and all equality masks, and verifies that the sharp retained bounds are positive. In total it checked \(211861\) erasure triples and exactly \(N\) maximizers at each order. The greatest observed eigenvalue-formula discrepancy was \(1.7764\times10^{-15}\). These finite checks are corroboration, **not** an extrapolated proof for arbitrary \(N\).

## Relationship to prior work
Haikin, Zamir, and Gavish study **expected moments** of frames under random erasures; their result does not control a fixed-cardinality adversarial minimum or characterize its worst masks. Cheng, Lv, and Sun characterize frames for which subframes of a given size have **uniform** bounds; that condition is opposite in quantifier to optimizing the nonuniform worst mask in this specific cyclic family. Batenkov, Demanet, Goldman, and Yomdin give clustered-node **singular-value estimates**, not the exact maximizing three-mask and its full enumeration on every cyclic grid.

Two closer published specializations are *Exact adversarial-erasure spectra for two-character cyclic harmonic frames*, which treats **two Fourier rows** for all deletion counts, and *Sharp Riesz conditioning for consecutive triples on finite cycles*, which minimizes a **largest-to-smallest eigenvalue ratio** across square three-column Fourier submatrices. The present claim instead determines the **largest single Gram eigenvalue** among all three-column masks of a three-row Parseval frame. Neither of those two assertions implies the stated value and strict maximizing classification without an additional extremal comparison. A possible older equivalent result under time-band limiting or finite prolate concentration terminology remains a literature risk.

## Limitations
Only exactly three distinct erasures from the normalized three-row consecutive Fourier Parseval frame are covered, with \(N\ge6\). There is no claim about an optimal alternative dual frame, optimal noise reconstruction beyond this ordinary lower-frame-bound guarantee, other frequency bands, unequal column weights, or four or more deletions. Independent scientific validation remains unperformed; the mathematical originality conclusion is based on inspected sources and semantic overlap checks, not a proof of absence from all literature.

## References
1. M. Haikin, R. Zamir, and M. Gavish, *Frame Moments and Welch Bound with Erasures*, arXiv:1801.04548v1, first public 2018-01-14, https://arxiv.org/abs/1801.04548.
2. D. Batenkov, L. Demanet, G. Goldman, and Y. Yomdin, *Conditioning of partial nonuniform Fourier matrices with clustered nodes*, arXiv:1809.00658v1, first public 2018-09-03, https://arxiv.org/abs/1809.00658.
3. Q. Cheng, F. Lv, and W. Sun, *Frames of uniform subframe bounds with applications to erasures*, Linear Algebra and its Applications 555 (2018), 186–200, DOI:10.1016/j.laa.2018.05.025.
4. *Exact adversarial-erasure spectra for two-character cyclic harmonic frames*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-adversarial-erasure-spectra-for-two-character-cyclic-harmo--e1e03f96b6f0.
5. *Sharp Riesz conditioning for consecutive triples on finite cycles*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-riesz-conditioning-for-consecutive-triples-on-finite-cycle--1200745c9cae.
