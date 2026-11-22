# Exact essential norms of multipliers on big weighted Lipschitz spaces of rooted trees

## Finding

Let \(T\) be an infinite locally finite rooted tree and let \(c_v>0\) be arbitrary edge weights. For every bounded multiplication operator \(M_\psi\) on the **big** weighted Lipschitz space \(\mathcal L_c(T)\), its distance to compact operators is exactly

\[
\boxed{\|M_\psi\|_{\mathrm e}=\lim_{K\to\infty}\sup_{|v|>K}\left[|\psi(v)|+c_v|\psi(v)-\psi(v^-)|\sum_{\substack{w\in[o,v^-]\\|w|>K}}\frac1{c_w}\right].}
\]

Here the sum is over nonroot edges on the root-to-parent path, and is zero when empty. The formula holds under either the root-plus-supremum norm or the root/max norm below. Consequently, \(M_\psi\) is compact exactly when these tail quantities tend to zero. The finite-prefix subtraction in this formula can be indispensable, even for a compact multiplier whose weighted differences never tend to zero.

## Assumptions and scope

The rooted tree \(T\) is infinite and locally finite, with root \(o\), depth \(|v|\), parent \(v^-\) for every nonroot vertex, and finite root-to-vertex paths \([o,v]\). All \(c_v\) are strictly positive real numbers, with no assumed growth or regularity. Put \(\Delta f(v)=f(v)-f(v^-)\) and

\[
\mathcal L_c(T)=\{f:T\to\mathbb C:\sup_{v\ne o}c_v|\Delta f(v)|<\infty\},\qquad
\|f\|_+=|f(o)|+\sup_{v\ne o}c_v|\Delta f(v)|.
\]

The equivalent norm \(\|f\|_{\max}=\max\{|f(o)|,\sup_{v\ne o}c_v|\Delta f(v)|\}\) is also considered. Assume the pointwise multiplication \(M_\psi f(v)=\psi(v)f(v)\) defines a bounded operator on this **big** space; it need not preserve the associated little space. The essential norm is the infimum of operator-norm distances to all compact linear operators on the respective Banach space. The result uses no hypothesis about regular branching and has no assertion for non-locally-finite trees.

## Proof

**1. Coordinates and exact rows.** Because root-to-vertex paths are finite, the weighted-difference map

\[
Jf=(x_o,(x_v)_{v\ne o}),\quad x_o=f(o),\quad x_v=c_v\Delta f(v),
\]

is onto and isometric from \((\mathcal L_c(T),\|\cdot\|_+)\) to \(\mathbb C\oplus_1\ell^\infty(T\setminus\{o\})\); for the max norm it is onto \(\mathbb C\oplus_\infty\ell^\infty(T\setminus\{o\})\). Indeed, every bounded coordinate family determines a function by

\[
f(v)=x_o+\sum_{\substack{w\in[o,v]\\w\ne o}}\frac{x_w}{c_w}.
\]

Write \(\delta_v=\psi(v)-\psi(v^-)\). The conjugate \(A=JM_\psi J^{-1}\) has coordinates

\[
(Ax)_o=\psi(o)x_o,\qquad
(Ax)_v=\psi(v)x_v+c_v\delta_vx_o+
 c_v\delta_v\sum_{\substack{w\in[o,v^-]\\w\ne o}}\frac{x_w}{c_w}.
\tag{1}
\]

In particular each output row depends on finitely many input coordinates. Boundedness of \(A\) is assumed, so the quantities below are finite.

**2. Finite-rank upper bound.** Let \(P_K\) be the coordinate projection onto the root and all vertices of depth at most \(K\). It has finite rank by local finiteness. Define

\[
F_K=P_KA+(I-P_K)AP_K.
\]

Both terms are finite rank, and \(A-F_K=(I-P_K)A(I-P_K)\). Equation (1) shows that its row at \(|v|>K\) has exactly two types of coefficients: \(\psi(v)\) at the terminal coordinate and \(c_v\delta_v/c_w\) at each ancestor with \(K<|w|<|v|\). On \(\ell^\infty\) the norm of such a finite-supported row is the sum of the absolute values of its coefficients, attained by choosing the phases of the input independently. Since the operator vanishes at the root and on its initial output coordinates, this row norm is the same under either norm on the direct sum. Therefore

\[
\|A-F_K\|=E_K:=\sup_{|v|>K}
\left(|\psi(v)|+c_v|\delta_v|
\sum_{\substack{w\in[o,v^-]\\|w|>K}}c_w^{-1}\right).
\tag{2}
\]

Consequently \(\|A\|_{\mathrm e}\le\inf_KE_K\). The sequence \(E_K\) decreases, since both its domain and each ancestral sum shrink as \(K\) increases, so its limit \(E\ge0\) exists.

**3. Sharp lower bound in the nonseparable domain.** Choose positive integers \(K_j\) recursively such that \(K_j\to\infty\) and \(K_j>|v_{j-1}|\). For each \(j\), choose \(v_j\), \(|v_j|>K_j\), whose row quantity in (2) exceeds \(E_{K_j}-1/j\). This is possible by the definition of supremum, including when it is zero. Build a vector \(x^{(j)}\) in the coordinate model, zero at the root and outside the finite set consisting of \(v_j\) and the ancestral vertices with depths strictly between \(K_j\) and \(|v_j|\). Give its nonzero coordinates modulus one and phases aligning the coefficient terms in the row \(v_j\) of (1). If the row vanishes, take one terminal coordinate of modulus one. In either case

\[
\|x^{(j)}\|=1,\qquad
\big|(Ax^{(j)})_{v_j}\big|\ge E_{K_j}-1/j.
\tag{3}
\]

These vectors have pairwise disjoint coordinate supports, because the successive depth bands are disjoint. Any bounded disjointly supported sequence in \(\ell^\infty\) is **weakly null**: for any functional represented by a bounded finitely additive measure \(\mu\), its action on the \(j\)-th vector is at most \(\|x^{(j)}\|_\infty|\mu|(\operatorname{supp}x^{(j)})\); the variations of disjoint sets are summable and therefore tend to zero. The finite-dimensional root coordinate is identically zero. Thus the sequence is weakly null under either direct-sum norm.

Every compact operator \(Q\) sends a weakly null bounded sequence to a norm-null sequence. Applying \(A-Q\) to (3) gives

\[
\|A-Q\|\ge\limsup_{j\to\infty}
\left(\big|(Ax^{(j)})_{v_j}\big|-\|Qx^{(j)}\|\right)\ge E.
\]

Taking the infimum over compact \(Q\), then combining with step 2, proves the exact identity for both norms. The compactness characterization follows because compact operators form a norm-closed ideal.

**4. A sharp distinction from the little space.** On the rooted ray with vertices \(n\ge0\), take \(c_n=2^n\) and \(\psi(n)=2^{-n}\). For every \(n\ge1\),

\[
c_n|\psi(n)-\psi(n-1)|=1.
\]

Nevertheless, for every \(K\ge0\), (2) yields exactly \(E_K=2^{-K}\). The supremum is approached as \(n\to\infty\), since

\[
2^{-n}+\sum_{j=K+1}^{n-1}2^{-j}
=2^{-K}-2^{-n}.
\]

Boundedness is direct from (1): the nonroot row sizes on the max-coordinate space are at most \(2^{-n}+1+\sum_{j=1}^{n-1}2^{-j}<3\), and the root row is bounded. Thus \(M_\psi\) is compact on the big weighted Lipschitz space although its symbol is not in the little space: the constant function \(1\) belongs to the little space but its image \(\psi\) does not. This demonstrates that the older little-space theorem cannot be transplanted to the big space without changing the formula.

**5. Classical unweighted specialization.** If \(c_v=1\), boundedness of \(M_\psi\) and the terminal-row norm in (1) give

\[
(|v|-1)|\delta_v|\le\|M_\psi\|_+\quad (|v|\ge2).
\]

Hence \(\delta_v\to0\) uniformly with depth. For any fixed \(K\), replacing the sum in (2) by the full ancestral sum changes it by at most \(K|\delta_v|\to0\); replacing \(|v|-1\) by \(|v|\) is also asymptotically harmless. Thus, for the ordinary big tree Lipschitz space under either norm,

\[
\|M_\psi\|_{\mathrm e}
=\limsup_{|v|\to\infty}
\left(|\psi(v)|+|v|\,|\psi(v)-\psi(v^-)|\right).
\]

## Verification

The standalone `checker.py` implements the weighted-difference conjugation and exact finite tail-row coefficient norms on independently generated finite rooted trees, tests explicit phase-attaining vectors, and tests the exponentially weighted ray example. Running `python3 checker.py` reported `PASS: 21537 finite identities and estimates`. These computations are finite consistency tests; the equality on infinite trees and weak convergence of disjoint bands follow from the proof above, not from extrapolation.

## Relationship to prior work

Issa-Barbará and Martínez-Avendaño (2026, arXiv:2602.13534, Section 8) give lower and upper **estimates** for essential norms of multipliers on infinite-graph Lipschitz spaces, explicitly leaving a stronger lower-bound issue for further research. In the tree case, the present result gives an exact formula. Colonna and Easley (2010) gave earlier tree estimates. A 2026 publicly recorded theorem titled *Exact essential norms for multipliers on little weighted Lipschitz spaces of rooted trees* proves precise formulas for **little**, \(c_0\)-modeled weighted spaces; it expressly does not claim the big, \(\ell^\infty\)-modeled case. Its untrimmed row formula is not applicable here: the compact weighted-ray example gives an essential norm of zero while its untrimmed row sizes remain bounded away from zero. López-Martínez (2026) independently exhibits the big-space \(\ell^\infty\) coordinate conjugation and computes the exact **operator norm**; it does not state the essential norm, which requires optimizing over compact corrections. The new lower bound uses disjointly supported weakly null vectors in \(\ell^\infty\), and the upper bound subtracts all finite input prefixes by finite-rank maps. The general technique of finitely additive measures on \(\ell^\infty\) is standard; it is not claimed as a new functional-analytic lemma.

## Limitations

The theorem assumes the multiplication operator is bounded and the rooted tree locally finite. It addresses the big weighted Lipschitz Banach space, not arbitrary graphs or all graph Lipschitz spaces, and proves no corresponding formula under other weighted norms. Although accessible recent primary sources and related public classifications do not state the exact big-space formula, older equivalent formulations of weighted triangular operators or inaccessible historical sources may affect bibliographic priority.

## References

1. J. A. Issa-Barbará and R. A. Martínez-Avendaño, *Multiplication Operators on the Lipschitz Space of an Infinite Graph*, arXiv:2602.13534v1 (public 14 February 2026), https://arxiv.org/abs/2602.13534, Section 8.
2. F. Colonna and G. R. Easley, *Multiplication Operators on the Lipschitz Space of a Tree*, Integral Equations and Operator Theory 68 (2010), 391–411, https://doi.org/10.1007/s00020-010-1824-5.
3. R. F. Allen, F. Colonna and G. R. Easley, *Multiplication Operators on the Weighted Lipschitz Space of a Tree*, Journal of Operator Theory 69 (2013), 209–231, https://doi.org/10.7900/jot.2010sep22.1885.
4. *Exact essential norms for multipliers on little weighted Lipschitz spaces of rooted trees*, public mathematical record (21 September 2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/21/SCOPE-exact-essential-norm-little-tree-lipschitz-multipliers--6b05c4d0072a.
5. J. Kong and L. Liu, *Fredholm weighted composition operators on the Lipschitz space of a tree*, arXiv:2611.11737v1 (9 November 2026), https://arxiv.org/abs/2611.11737.

6. A. López-Martínez, *Frequently Hypercyclic Composition Operators on The Little Lipschitz Space of A Rooted Tree*, Mediterranean Journal of Mathematics 23 (2026), article 87, https://doi.org/10.1007/s00009-026-03075-6, Remark 2.1 and Corollary 2.6.
