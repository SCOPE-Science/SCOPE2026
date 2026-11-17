# Endpoint Schatten convergence for bilateral shifts and weighted partial permutations

## Finding

Fix \(0<p<\infty\) and \(0<t<1\). For a complex separable Hilbert space with a countable orthonormal basis, consider a weighted partial-permutation operator \(T\) with at most one nonzero coefficient in every matrix row and column, and \(\sum_i|w_i|^p<\infty\). Write \(\Delta_t(T)=|T|^tU|T|^{1-t}\), with \(T=U|T|\) its polar decomposition. Every connected component of the nonzero-entry graph is a finite directed cycle or a directed path (finite, one-sided, or two-sided). If \(\mathcal C\) denotes the set of finite cycles, with length \(L_C\) and absolute edge weights \(a_{C,1},\dots,a_{C,L_C}>0\), then

\[
\boxed{\lim_{n\to\infty}\|\Delta_t^n(T)\|_{\mathcal S_p}^{p}
=\sum_{C\in\mathcal C}L_C\left(\prod_{j=1}^{L_C}a_{C,j}\right)^{p/L_C}.}
\]

Equivalently this is the sum of the \(p\)-th powers of the nonzero eigenvalue moduli of \(T\), counting algebraic multiplicity. In particular every \(\mathcal S_p\) bilateral weighted shift has \(\|\Delta_t^n(T)\|_{\mathcal S_p}\to0\), including two-sided shifts with all coefficients nonzero. All of these statements hold for \(0<p<1\) with \(\mathcal S_p\) understood as a quasi-normed ideal.

There is an explicit quantitative tail estimate for the bilateral case. Set \(Te_j=w_je_{j+1}\) on \(\ell^2(\mathbb Z)\), \(u_j=|w_j|^p\), \(U=\sum_{j\in\mathbb Z}u_j>0\), and for an integer \(R\ge0\) set \(E_R=\sum_{|j|>R}u_j\). For integers \(n\ge2R+1\), let

\[
b_{n,i}=\binom ni t^i(1-t)^{n-i},\quad
\beta_{n,R}=\max_{k\in\mathbb Z}\sum_{i=0}^nb_{n,i}\mathbf1_{\{|k+i|\le R\}},\quad
\alpha_{n,R}=1-\beta_{n,R}.
\]

Then \(0<\beta_{n,R}<1\) and

\[
\boxed{\|\Delta_t^n(T)\|_{\mathcal S_p}^{p}\le
\left(\frac{E_R}{\alpha_{n,R}}\right)^{\alpha_{n,R}}
\left(\frac{U}{\beta_{n,R}}\right)^{\beta_{n,R}}.}
\]

The right side is interpreted as zero when \(E_R=0\). In addition, \(\beta_{n,R}\le(2R+1)\max_i b_{n,i}=O_{t,R}(n^{-1/2})\). The bound is valid with zero and complex weights. For any fixed positive integer \(n\), the supremum of \(\|\Delta_t^n(T)\|_{\mathcal S_p}/\|T\|_{\mathcal S_p}\) over nonzero finite-support bilateral weighted shifts is exactly \(1\), so no universal rate follows without a tail profile.

## Assumptions and scope

The complex Hilbert space may be finite or countably infinite dimensional. The nonzero-entry directed graph has vertices indexed by the chosen orthonormal basis and a directed edge \(i\to j\) of complex weight \(w_i\ne0\) whenever \(Te_i=w_ie_j\). The at-most-one-per-row-and-column assumption ensures that distinct edges have different sources and targets. Every edge weight is included exactly once in the \(\mathcal S_p\) sum. Components with no edges contribute zero. Finite cycles of length one (diagonal entries) are allowed. The unilateral and bilateral shifts in the proof may contain zero weights by adjoining zero tails; a component is taken to have nonzero weights internally.

## Proof

**1. Local update and binomial formula.** For a weighted directed partial permutation, \(|T|e_i=|w_i|e_i\) on the nonzero-edge sources, while the polar factor sends \(e_i\) to \((w_i/|w_i|)e_j\). Thus the new edge on \(i\to j\) has phase \(w_i/|w_i|\) and modulus \(|w_i|^{1-t}|w_j|^t\), interpreted as zero if the target has no outgoing edge. The directed-graph structure is preserved, possibly with deleted edges. Along an oriented path or bilateral line, iterative application yields

\[
\bigl|w^{(n)}_j\bigr|^p=\prod_{i=0}^n u_{j+i}^{b_{n,i}},\qquad
b_{n,i}=\binom ni t^i(1-t)^{n-i}.
\]

This follows by induction from the scalar update \(\log|w_j^{(n+1)}|=(1-t)\log|w_j^{(n)}|+t\log|w_{j+1}^{(n)}|\) where all weights are positive, and extends to zero weights by direct multiplicative induction with the convention \(0^s=0\) for \(s>0\). The nonzero singular values of a weighted partial permutation are precisely the nonzero absolute edge weights, so its Schatten power sum is the sum of these expressions.

**2. Quantitative two-sided concentration escape.** In the bilateral case with \(n\ge 2R+1\), for each starting index \(j\) define \(q_j=\sum_{i:|j+i|\le R}b_{n,i}\le\beta=\beta_{n,R}\); thus \(q_j<1\). Put \(\alpha=1-\beta\), \(v_{j,i}=\alpha b_{n,i}/(1-q_j)\) outside \([-R,R]\) and \(v_{j,i}=0\) inside; set \(h_{j,i}=b_{n,i}-v_{j,i}\). The nonnegative weights \(v_{j,i}\) sum to \(\alpha\), while \(h_{j,i}\) sum to \(\beta\). Weighted arithmetic--geometric mean, applied to these two sets separately, gives

\[
\prod_i u_{j+i}^{b_{n,i}}
\le\left(\frac{X_j}{\alpha}\right)^\alpha
\left(\frac{Y_j}{\beta}\right)^\beta,
\quad X_j=\sum_{i:|j+i|>R}b_{n,i}u_{j+i},\quad
Y_j=\sum_i b_{n,i}u_{j+i}.
\]

Indeed the exterior part has normalized weighted arithmetic mean \(X_j/(1-q_j)\le X_j/\alpha\); the remaining part's weighted arithmetic mean is at most \(Y_j/\beta\). Hölder's inequality in the summation over \(j\), with conjugate exponents \(1/\alpha\) and \(1/\beta\), yields

\[
\sum_j\prod_i u_{j+i}^{b_{n,i}}
\le\left(\frac{\sum_jX_j}{\alpha}\right)^\alpha
\left(\frac{\sum_jY_j}{\beta}\right)^\beta.
\]

Absolute summability and translation invariance give \(\sum_jX_j=E_R\) and \(\sum_jY_j=U\). This proves the quantitative inequality. A binomial distribution with \(0<t<1\) has maximal atom \(O_t(n^{-1/2})\), by elementary Stirling bounds, and a window of \(2R+1\) indices has at most that many atoms. Consequently \(\beta_{n,R}\to0\) at each fixed \(R\). The upper limit of the inequality is at most \(E_R\); sending \(R\to\infty\) gives the asserted zero limit. If \(U=0\), the operator vanishes. Zero weights can also be handled by approximation or by the multiplicative convention just used.

**3. Paths, cycles, and summation.** Any directed finite or one-sided path can be embedded in the oriented integer line by extending its weights to zero off that path, and hence obeys the bilateral bound. For a finite directed cycle of length \(L\), the vector of logarithmic positive edge moduli is repeatedly multiplied by \(P=(1-t)I+tS\), where \(S\) is cyclic rotation. Its Fourier eigenvalues are \((1-t)+t e^{2\pi ik/L}\), which have modulus strictly smaller than one except at \(k=0\). Hence the edge moduli converge to their geometric mean \(g_C=(\prod_{j=1}^La_{C,j})^{1/L}\), giving the limit \(Lg_C^p\) of that component's Schatten \(p\)-power.

For each component \(D\), the weighted AM--GM inequality implies \(\|\Delta_t^n(T_D)\|_{\mathcal S_p}^p\le\|T_D\|_{\mathcal S_p}^p\) for all \(n\), because the binomial weights are probability weights and the cyclic or zero-padded linear index shift cannot increase the total \(\ell_1\) mass of the nonnegative powers \(u_i\). As \(\sum_D\|T_D\|_{\mathcal S_p}^p<\infty\), dominated convergence for the countable component sum proves the displayed formula. All noncycle components have spectral radius zero: for any \(\varepsilon>0\), only finitely many of the globally summable weights have modulus greater than \(\varepsilon\), and a directed simple path meets those edges at most once, giving a uniform decaying upper bound on powers. Since the operator is compact, every nonzero eigenvalue therefore comes from a finite cycle, and each cycle contributes \(L\) eigenvalues of modulus \(g_C\), counted algebraically.

**4. Absence of a uniform decay rate.** For an arbitrary integer \(L>n\), take weights equal to one on \(L\) consecutive edges and zero elsewhere. The initial Schatten \(p\)-power is \(L\); after \(n\) transforms it is \(L-n\), because precisely the \(L-n\) edges whose forward binomial windows stay inside the plateau survive. The ratio \(((L-n)/L)^{1/p}\) tends to one with \(L\), and the general weighted AM--GM bound proves one is an upper bound.

## Verification

The accompanying `checker.py` checks the binomial recursion in exact rational arithmetic, evaluates the proposed quantitative bound for randomized finite zero-padded integer-line data with different \(t,n,R\), and checks exact preservation of the mean in finite-cycle logarithmic dynamics with numerical convergence checks. The checker is a finite diagnostic, not a proof of the infinite-dimensional claims. Every analytic step needed for the full theorem is given above, including the zero-support boundary case and the passage from components to an infinite direct sum.

## Relationship to prior work

Stanković, *Singular values of iterated Aluthge transforms of compact operators*, arXiv:2611.07728v1, establishes singular-value convergence for all compact operators, Schatten convergence when the starting operator belongs to a smaller Schatten class, and Schatten-endpoint convergence for unilateral weighted shifts (Proposition 5.8 and Corollary 5.9). The present theorem addresses arbitrary summable bilateral weights, including shifts with two-sided nonvanishing weights, and a weighted-permutation graph class; it adds a quantitative concentration-escape estimate and a proof that no uniform rate exists. For example, \(|w_j|^p\) comparable to \(((2+|j|)\log^2(3+|j|))^{-1}\) is summable but \((w_j)\) belongs to no smaller \(\ell_q\), so the smaller-ideal hypothesis does not subsume the result. Antezana--Massey--Stojanoff study \(\lambda\)-Aluthge transforms and Schatten ideals, including norm comparisons, but the parts inspected do not establish this endpoint limit. Rion studies weighted-shift Aluthge sequences under different hypotheses; Tran studies different, invertible bilateral shifts.

## Limitations

This is an exact classification only for compact weighted partial permutations, not an assertion of Schatten-endpoint convergence for arbitrary compact operators. It is a self-review, not an independently audited theorem. The novelty comparison is based on accessible primary material and targeted searches; possible earlier equivalent formulations in general permutation or weighted-shift terminology remain a priority risk. The finite checker does not establish infinite claims. No quantitative rate independent of the distribution of input weights is asserted.

## References

- H. Stanković, *Singular values of iterated Aluthge transforms of compact operators*, arXiv:2611.07728v1 (first publicly available 2026-11-05), https://arxiv.org/abs/2611.07728 .
- J. Antezana, P. Massey, D. Stojanoff, *\(\lambda\)-Aluthge transforms and Schatten ideals* (2005), published research article.
- K. Rion, *Convergence Properties of the Aluthge Sequence of Weighted Shifts* (2016).
- L. T. T. Tran, *Shadowing, Generalized hyperbolic and Aluthge transforms*, arXiv:2209.07260 (2022), https://arxiv.org/abs/2209.07260 .
