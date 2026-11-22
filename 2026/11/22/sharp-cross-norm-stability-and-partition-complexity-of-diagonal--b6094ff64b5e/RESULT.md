# Sharp cross-norm stability and partition complexity of diagonal-quadratic simplex prediction

## Finding

Let \(n\ge2\), let \(a_1,\ldots,a_n>0\), and set \(A=\sum_{i=1}^n a_i\). Define the probability simplex \(\Delta_{n-1}=\{p\in\mathbb R^n:p_i\ge0,\ \sum_i p_i=1\}\). The *diagonal-quadratic simplex prediction* operator is

\[
S_a(z)=\operatorname*{argmax}_{p\in\Delta_{n-1}}
\left\{\sum_{i=1}^n z_ip_i-\frac12\sum_{i=1}^n\frac{p_i^2}{a_i}\right\}.
\]

Define the two-way discrepancy of the curvature-reciprocal weights by

\[
\delta(a)=\min_{\sigma_i\in\{-1,1\}}\left|\sum_{i=1}^n a_i\sigma_i\right|.
\]

**Theorem.** For every such \(n\) and \(a\), the exact global cross-norm sensitivity is

\[
\boxed{\sup_{z\ne z'}\frac{\|S_a(z)-S_a(z')\|_1}{\|z-z'\|_\infty}
=A-\frac{\delta(a)^2}{A}.}
\]

The supremum is achieved by distinct score vectors in a common **full-support** affine chamber. In particular the coefficient equals \(A\) if and only if the weights can be split into two groups of equal total mass. For positive integer weights encoded in binary, deciding whether that equality holds is NP-complete, even though each individual prediction is obtained by a one-dimensional threshold search. An exact dynamic program requires \(O(nA)\) arithmetic steps and \(O(A)\) memory for these integer weights. At fixed \(n\ge2\) and fixed total \(A>0\), the largest coefficient \(A\) is attained by balanced positive weights; the infimum over positive weights with total \(A\) is \(0\) but is not attained.

## Assumptions and scope

All statements concern **finite-dimensional real** score vectors, strictly positive finite \(a_i\), and the global two-input Lipschitz coefficient with the *unweighted* input maximum norm and output sum norm. The outcome \(S_a(z)\) has probability mass one. The regularizer \(\sum_i p_i^2/(2a_i)\) is strongly convex, so the maximizer is unique. No coefficient for arbitrary non-diagonal quadratic forms, other input/output norms, or infinite-dimensional simplexes is claimed. The NP-completeness claim concerns an exact decision with **binary-encoded positive integer** weights; it does not imply hard approximation or difficult evaluation of \(S_a(z)\).

## Proof

**1. Threshold formula.** Strict convexity and the Karush–Kuhn–Tucker conditions supply a unique real threshold \(\tau\) satisfying

\[
S_a(z)_i=a_i(z_i-\tau)_+,\qquad
\sum_{i=1}^n a_i(z_i-\tau)_+=1.
\]

The left-hand side of the threshold equation is continuous and strictly decreasing wherever positive, with limits \(+\infty\) and \(0\) as the threshold moves from \(-\infty\) to above all scores. Therefore the required threshold exists and is unique. On the open chamber with active set \(T=\{i:z_i>\tau\}\), put \(A_T=\sum_{i\in T}a_i\). Then \(\tau=(\sum_{i\in T}a_i z_i-1)/A_T\), and the Jacobian is

\[
(J_T)_{ij}=
\begin{cases}
 a_i\mathbf1_{i=j}-\dfrac{a_i a_j}{A_T},&i,j\in T,\\
 0,&\text{otherwise}.
\end{cases}
\]

Every nonempty active set occurs on some open chamber (choose a simplex point positive on \(T\) and zero elsewhere, and move excluded scores strictly below the threshold). The prediction map is continuous and piecewise affine with finitely many chambers. Hence its global Lipschitz coefficient is the largest \(\ell_\infty\)-to-\(\ell_1\) operator norm among the matrices \(J_T\).

**2. Positive-semidefinite sign identity.** Every \(J_T\) is positive semidefinite, as

\[
 v^\mathsf TJ_Tv=\min_{c\in\mathbb R}\sum_{i\in T}a_i(v_i-c)^2\ge0.
\]

For any real symmetric positive-semidefinite matrix \(J\), the dual representation of the two endpoint norms and Cauchy–Schwarz for its quadratic form give

\[
\|J\|_{\infty\to1}
=\max_{s,t\in\{-1,1\}^n}t^\mathsf TJs
=\max_{s\in\{-1,1\}^n}s^\mathsf TJs.
\]

Indeed \(|t^\mathsf TJs|\le(t^\mathsf TJt)^{1/2}(s^\mathsf TJs)^{1/2}\), so the maximum occurs when \(t=s\) is a quadratic-form maximizer. For any sign vector \(s\), adding the terms indexed outside \(T\) cannot decrease the minimum over \(c\), and therefore

\[
 s^\mathsf TJ_Ts
=\min_c\sum_{i\in T}a_i(s_i-c)^2
\le\min_c\sum_{i=1}^na_i(s_i-c)^2
=s^\mathsf TJ_{[n]}s.
\]

Thus the full-support Jacobian dominates **all** other active-set Jacobians in this induced norm, even though the nonnegative-cone projection can change active supports.

**3. Optimize the full-support norm.** For \(s_i\in\{-1,1\}\),

\[
 s^\mathsf TJ_{[n]}s
=\sum_i a_i-\frac{(\sum_i a_i s_i)^2}{A}
=A-\frac{(\sum_i a_i s_i)^2}{A}.
\]

Maximizing over signs gives exactly \(A-\delta(a)^2/A\). This proves the upper bound for all finite score pairs by integrating the finitely many Jacobians along the input line segment.

**4. Exact finite sharpness.** Fix a sign vector \(s\) minimizing the discrepancy, take the full-support point \(p_i^0=1/n\), and choose \(z_i^0=p_i^0/a_i\). Its threshold is \(0\). For all sufficiently small \(\varepsilon>0\), both \(z^+=z^0+\varepsilon s\) and \(z^-=z^0-\varepsilon s\) remain in the same full-support affine chamber. Consequently

\[
\frac{\|S_a(z^+)-S_a(z^-)\|_1}{\|z^+-z^-\|_\infty}
=\|J_{[n]}s\|_1
=s^\mathsf TJ_{[n]}s
=A-\frac{\delta(a)^2}{A}.
\]

The middle equality holds because \((J_{[n]}s)_i=a_i(s_i-\bar s)\) has the sign of \(s_i\), where \(\bar s=\sum_i a_i s_i/A\in[-1,1]\). Since \(\varepsilon>0\), the two inputs are distinct. Therefore the global optimum is *attained*, not merely approached by an infinitesimal sequence.

**5. Computational boundary and design range.** For integer \(a_i>0\), \(\delta(a)=0\) exactly when the classical PARTITION decision instance is a yes-instance. That decision problem is NP-complete under binary encoding, and a subset witnessing equality gives membership in NP. This is a many-one identity reduction; it proves NP-completeness of deciding whether the exact Lipschitz coefficient equals its explicit upper bound \(A\). Subset-sum dynamic programming over totals \(0,1,\ldots,A\) finds \(\delta(a)=\min_{s\in\mathrm{Reach}}|A-2s|\) in \(O(nA)\) time and \(O(A)\) memory. For real weights of fixed total, balanced groups (e.g. equal masses in two groups) give \(\delta=0\), while a family \((A-(n-1)h,h,\ldots,h)\) with \(h\downarrow0\) yields \(\delta\uparrow A\) and coefficient decreasing to zero. Strictly positive weights ensure \(\delta<A\) for \(n\ge2\), hence zero is never attained.

## Verification

`checker.py` uses only the Python standard library and exact rational arithmetic. Run `python3 checker.py` beside this file. It checks the KKT threshold solver, the discrepancy formula against independently enumerated matrix endpoint norms, all sampled active-set norms against the full-support coefficient, exact finite sharpness pairs, and a separate subset-sum dynamic program. The randomized rational instances use a fixed seed and cover sizes \(2\) through \(7\). These finite checks supplement but do not substitute for the analytic proof or the classical PARTITION reduction.

## Relationship to prior work

The sparsemax Jacobian and its unweighted quadratic simplex construction occur in Martins and Astudillo (2016). Blondel, Martins, and Niculae (initially public in January 2019; expanded journal presentation 2020) provide the general regularized-prediction/Fenchel–Young framework in which the present diagonally quadratic map naturally lies. Perez, Ament, Gomes, and Barlaud (arXiv September 2020) derive efficient thresholding algorithms for weighted-simplex and weighted-\(\ell_1\) projection problems. Those works supply the relevant objects and computational context. The claim here is the **sharp global cross-norm coefficient for arbitrary positive diagonal curvature**, its full-support attainment, and the exact PARTITION-complexity boundary. The uniform-curvature special case and the elementary threshold/Jacobian calculation are not claimed as new. Previously published partition-discrepancy formulas for Lipschitz observables on graph metrics concern different maps, and do not imply this prediction-operator norm formula by the investigated reductions.

## Limitations

Originality is assessed by searches and inspection of the cited primary works, not by an exhaustive proof that the result is absent from all historical literature. The coefficient formula has a transparent relationship to known weighted-variance and PARTITION identities; an older result under those formulations remains possible. Strongest relevant technical risk is an unlocated earlier induced-norm calculation for diagonal-metric simplex projection. The NP-hardness is *weak* and concerns exact worst-case sensitivity, not pointwise prediction or approximation. All proof claims are finite-dimensional; no independent mathematical audit is asserted.

## References

1. Mathieu Blondel, André F. T. Martins, Vlad Niculae, *Learning with Fenchel–Young Losses*, arXiv:1901.02324, first posted 2019-01-08; JMLR 21 (2020), 1–69. https://arxiv.org/abs/1901.02324 and https://www.jmlr.org/papers/v21/19-021.html
2. Guillaume Perez, Sebastian Ament, Carla Gomes, Michel Barlaud, *Efficient Projection Algorithms onto the Weighted \(\ell_1\) Ball*, arXiv:2009.02980, first posted 2020-09-07. https://arxiv.org/abs/2009.02980
3. André F. T. Martins, Ramón F. Astudillo, *From Softmax to Sparsemax: A Sparse Model of Attention and Multi-Label Classification*, PMLR 48 (2016), 1614–1623. https://proceedings.mlr.press/v48/martins16.html
4. R. M. Karp, *Reducibility Among Combinatorial Problems*, in *Complexity of Computer Computations* (1972), 85–103 (classical PARTITION hardness).
