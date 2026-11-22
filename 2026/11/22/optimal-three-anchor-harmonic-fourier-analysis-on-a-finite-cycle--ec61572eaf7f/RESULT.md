# Optimal three-anchor harmonic Fourier analysis on a finite cycle

## Finding
Fix an integer \(N\geq3\). Let \(S\) range over all unordered three-element subsets of the cycle \(C_N=\mathbb Z/N\mathbb Z\). The harmonic completion \(H_S:\mathbb C^S\to\mathbb C^{C_N}\) agrees with the three anchor values and minimizes the ordinary unit-edge Dirichlet energy on the cycle. Analyze \(H_Sx\) with any Parseval family of cyclic Fourier wavelets (or any other Parseval frame) of \(\mathbb C^{C_N}\), and denote the squared optimal upper frame bound of this analysis by \(B(S)\).

**Sharp placement theorem.** For every \(N\ge3\), the smallest possible \(B(S)\) is attained **exactly** when the three positive cyclic spacings between consecutive anchors differ by at most one. The number of optimal unordered anchor sets is \(N/3\) when \(3\mid N\), and \(N\) otherwise. All these statements hold for complex signals and for every Parseval host analysis bank, independently of its choice of filters.

The exact optimum is as follows. Write \(N-3=3q+r\), where \(q\ge0\) and \(r\in\{0,1,2\}\), and put
\[
s_t=\frac{t(2t+1)}{6(t+1)},\qquad c_t=\frac{t(t+2)}{6(t+1)}\quad(t\ge0).
\]
If \(r=0\), the optimal bound is \(B_{N}=N/3\). If \(r=1\), define
\[
 u=1+2s_q+c_q+\tfrac12,\qquad v=1+2s_q,\qquad d=c_q.
\]
If \(r=2\), define
\[
 u=1+2s_{q+1},\qquad v=1+s_q+s_{q+1}+c_q,\qquad d=c_{q+1}.
\]
For either \(r=1\) or \(r=2\), the sharp bound is the explicit radical
\[
\boxed{B_N=\frac{u+v+\sqrt{(u-v)^2+8d^2}}2.}
\]
In particular, \(B_N>N/3\) whenever \(3\nmid N\), and the integer-grid penalty satisfies
\[
 B_N-\frac N3=\frac1{3N}+O(N^{-2})\qquad(N\to\infty,\ 3\nmid N).
\]
The bound controls the sum of squares of all host Fourier-wavelet coefficients of the harmonic extension; it does **not** assert optimality for condition number or for bandlimited recovery.

## Assumptions and scope
The cycle has edges \(\{j,j+1\}\) modulo \(N\), all of unit weight, and all Hilbert norms use counting measure. Choose the ordered anchors \(v_0,v_1,v_2\) cyclically and write their positive edge spacings as \(\ell_i=v_{i+1}-v_i\pmod N\), indices modulo three; thus \(\ell_i\ge1\), \(\sum_i\ell_i=N\). Let \(g_i=\ell_i-1\) be the number of unobserved vertices in each gap. Harmonic completion means the unique minimum of \(\sum_{j\in C_N}|y(j+1)-y(j)|^2\) over all extensions with the prescribed values at the anchors. The host frame is any Parseval frame \(\{\psi_\alpha\}\), and the analysis is \(x\mapsto (\langle H_Sx,\psi_\alpha\rangle)_\alpha\). Hence \(B(S)=\sup_{x\ne0}\|H_Sx\|_2^2/\|x\|_2^2\). A cycle of three vertices, which has no unobserved vertices, is included.

## Proof
**Gap interpolation and exact Gram matrix.** Over a gap of \(g\ge0\) missing vertices between two anchors of values \(a,b\), the harmonic values are \((1-t/(g+1))a+(t/(g+1))b\), for integers \(1\le t\le g\). The squared norm of this missing-vertex vector is the quadratic form in \((a,b)\) of the matrix
\[
 M_g=\begin{pmatrix}s_g&c_g\\c_g&s_g\end{pmatrix},
\]
because the power sums give \(\sum_{t=1}^g(t/(g+1))^2=s_g\) and \(\sum_{t=1}^g t(g+1-t)/(g+1)^2=c_g\). Let \(E_i:\mathbb C^3\to\mathbb C^2\) select the two endpoint coordinates of gap \(i\). Then
\[
 H_S^*H_S=I_3+\sum_{i=0}^2 E_i^*M_{g_i}E_i.
\]
The host Parseval analysis \(W\) satisfies \(W^*W=I\), so the induced frame operator is \(H_S^*W^*WH_S=H_S^*H_S\); consequently the problem is completely filter-independent.

**Strict matrix-convex balancing.** Let \(P_+\) and \(P_-\) denote the orthogonal projections in \(\mathbb C^2\) onto the symmetric and antisymmetric lines. Direct algebra yields
\[
 M_t=\frac t2P_++f(t)P_-,\qquad f(t)=\frac{t(t-1)}{6(t+1)},\qquad f''(t)=\frac{2}{3(t+1)^3}>0\quad(t\ge0).
\]
Thus \(t\mapsto M_t\) is matrix-convex in the Loewner order, with a strictly convex antisymmetric component. Therefore the largest eigenvalue \(F(g_0,g_1,g_2)\) of the Gram matrix is a convex function of nonnegative real gap lengths. It is symmetric under **every permutation** of its three arguments: the symmetry group of a triangle permutes its edges arbitrarily.

For strictness, take two distinct gaps \(g_i\ne g_j\), and let \(\sigma\) exchange them. For any \(0<\theta<1\), matrix convexity gives \(A(\theta g+(1-\theta)\sigma g)\preccurlyeq\theta A(g)+(1-\theta)P A(g)P^*\), where \(P\) permutes the three anchors and \(A(g)=H_S^*H_S\). If the largest eigenvalue of the left side equaled \(F(g)\), a maximizing vector would need to be an eigenvector of both endpoint matrices and give equality in the strictly convex scalar terms on **both** changed edges. Its values at the endpoints of each of these edges must coincide. Two different edges of the triangle connect all three vertices, hence the vector must be constant. But the row sums of \(A(g)\) are \(1+(g_{i-1}+g_i)/2\). A constant vector can be an eigenvector of \(A(g)\) only if \(g_0=g_1=g_2\), contradicting the two different gaps. Therefore
\[
 F(\theta g+(1-\theta)\sigma g)<F(g)\qquad(g_i\ne g_j,\ 0<\theta<1).
\]
If two integer gaps differ by at least two, transferring one missing vertex from the larger to the smaller is exactly such a nontrivial convex combination of the original and its transposition (the mixing parameter is the reciprocal of their difference). This strictly lowers the sharp upper bound. Repeating the transfers terminates exactly at triples whose entries differ by at most one. Conversely the balanced triples are all mutually permuted by triangle symmetries, so all attain the same value. This proves global optimality and all equality cases for every \(N\).

**Values and counting.** When \(r=0\), the three missing-vertex counts all equal \(q\). Every row sum of \(A\) equals \(1+q=N/3\), and \(A\) has nonnegative entries, so its largest eigenvalue is this row sum. For \(r=1\), one edge carries \(q+1\) missing sites and two carry \(q\). The symmetry interchanging the endpoints of the longer gap reduces the Perron eigenvalue to the larger eigenvalue of the explicit symmetric matrix \(\bigl(\begin{smallmatrix}u&\sqrt2d\\\sqrt2d&v\end{smallmatrix}\bigr)\) with the first pair of \((u,v,d)\) above. For \(r=2\), two gaps carry \(q+1\) and the remaining one carries \(q\); reflection through their common endpoint gives the second pair. The displayed radical follows from the two-by-two characteristic polynomial. Positivity of the relevant off-diagonals identifies the larger root with the full matrix's largest eigenvalue, including \(q=0\).

For \(3\mid N\), the optimal anchor sets are cosets of the unique subgroup of order three, giving \(N/3\) sets. Otherwise a balanced gap triple has one uniquely exceptional gap, and translating its starting anchor gives exactly \(N\) sets. The strict balancing step rules out all others.

**Asymptotic penalty.** Expanding the two radicals at \(q\to\infty\) yields \(B_{3q+4}-(3q+4)/3=1/(9q)+O(q^{-2})\) and \(B_{3q+5}-(3q+5)/3=1/(9q)+O(q^{-2})\). As \(N=3q+O(1)\), both expressions equal \(1/(3N)+O(N^{-2})\). The integer-grid excess is strictly positive: equality in the Rayleigh-quotient lower bound \(F(g)\ge N/3\) would force constant anchor data to be a maximal eigenvector, which requires all three gap counts equal; this is impossible when \(3\nmid N\).

## Verification
The standalone checker at `verification/check.py` constructs the harmonic-completion matrix directly, validates the exact power-sum Gram coefficients with rational arithmetic, and exhaustively evaluates all ordered nonnegative three-gap allocations up to the stated finite cutoff. It checks the radical optimum, all optimal gap triples, and selected Parseval analysis identities. Execute with Python 3 and NumPy: `python verification/check.py`. Finite enumeration is supporting evidence only; the matrix-convex argument establishes the theorem for every integer \(N\ge3\).

## Relationship to prior work
Fokam Souop and Bitjoka, arXiv:2607.14168v1 (first published July 15, 2026), establish that normalized Fourier filter banks on cyclic hosts are Parseval and that harmonic completion is the unique Dirichlet-energy-minimizing extension (Theorems 1 and 5). They do not optimize the **upper coefficient-energy bound over three arbitrary anchor placements** or give the strict integer balancing law. The published record *Harmonic completion of cyclic graph wavelets: exact frame distortion and a quadratic Dirichlet obstruction* (published-finding corpus, November 16, 2026) analyzes instead a contiguous path of \(n\) anchors in its isometric host; it determines a spectrum for that different boundary set, not the global three-anchor placement optimum. The published *Sharp Riesz conditioning for consecutive triples on finite cycles* (published-finding corpus, October 11, 2026) studies a three-column Fourier Vandermonde Riesz ratio, not the harmonic-completion Gram matrix; its balanced frequency geometry does not imply the present interpolation result. Classical graph sampling and trigonometric interpolation theory supply important background, but their different optimization objectives do not establish the strict matrix-convex balancing statement. A previously published equivalent result under linear-spline knot-placement terminology remains a bibliographic risk.

## Limitations
The optimum is for the **upper** squared frame bound, not the lower bound, frame condition number, noise-sensitive recovery or other completion rules. Three anchors are essential to the full edge-permutation symmetry used in the proof; no equal-spacing theorem is asserted for more anchors, weighted cycles, or noncyclic graphs. The source graph-wavelet construction permits connected isometric embeddings, but here the three samples are simply anchor constraints on a cyclic host; they are not claimed to be an isometric image of an arbitrary connected graph. An independent audit has not been performed and novelty is assessed only relative to the records inspected.

## References
1. R. Fokam Souop and L. Bitjoka, *Tight Wavelet Frames on Graphs via Isometric Group Embedding*, arXiv:2607.14168v1, July 15, 2026, https://arxiv.org/html/2607.14168.
2. *Harmonic completion of cyclic graph wavelets: exact frame distortion and a quadratic Dirichlet obstruction*, published-finding corpus, November 16, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-harmonic-completion-of-cyclic-graph-wavelets-exact-frame-distort--8426f47cda6b.
3. *Sharp Riesz conditioning for consecutive triples on finite cycles*, published-finding corpus, October 11, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-riesz-conditioning-for-consecutive-triples-on-finite-cycle--1200745c9cae.
4. Y. Tanaka et al., *Sampling Signals on Graphs: From Theory to Applications*, arXiv:2003.03957 (2020), https://arxiv.org/abs/2003.03957.
