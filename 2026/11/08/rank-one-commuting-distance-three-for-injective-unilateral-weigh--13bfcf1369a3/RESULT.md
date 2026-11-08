# Rank-one commuting distance three for injective unilateral weighted shifts

## Finding

**Theorem.** Fix \(1\le p<\infty\) and let \(W\) be a bounded unilateral forward weighted shift on the **complex** space \(\ell_p(\mathbb N_0)\), with \(W e_n=w_n e_{n+1}\) and every \(w_n\ne0\). Then every bounded non-scalar operator \(S\) commuting with \(W\) has empty point spectrum. In particular, no such \(S\) commutes with a nonzero finite-rank operator. The least length of a chain of commuting non-scalar operators from \(W\) to any rank-one operator is exactly **three**:

\[
 W\ \longleftrightarrow\ W^2\ \longleftrightarrow\ P_{\mathrm{even}}\ \longleftrightarrow\ F_0.
\]

Here \(P_{\mathrm{even}}e_n=e_n\) for even \(n\), otherwise zero, and \(F_0x=x_0e_0\). No chain \(W\longleftrightarrow S\longleftrightarrow F\) exists with non-scalar \(S\) and nonzero finite-rank \(F\).

**Compact quasinilpotent consequence.** On complex \(\ell_2(\mathbb N_0)\) take \(K e_n=2^{-(n+1)}e_{n+1}\). This \(K\) is nonzero, compact, injective, quasinilpotent, and belongs to every Schatten class \(\mathcal S_q\) for \(q>0\). Nonetheless, there is no non-scalar \(S\) and rank-one \(F\) satisfying \(K\longleftrightarrow S\longleftrightarrow F\). Thus the answer to Szczepanski's Problem 4.5 in *On the chain of commuting operators on Banach spaces* (2026 version) is **negative**, even for a particularly regular compact shift.

## Assumptions and scope

All operators and eigenvalues in the theorem are **complex-linear**; \(1\le p<\infty\), the shift weights are bounded in absolute value, and none vanishes. The coordinate basis is the usual Schauder basis of \(\ell_p(\mathbb N_0)\). “Rank-one commuting distance” counts edges of the graph whose vertices are non-scalar bounded operators and whose edges join commuting pairs; the terminal rank-one operator may be chosen freely. This is **not** the minimum chain length to an arbitrary nonzero compact operator. The latter distinction matters: the displayed compact \(K\) already has chain length zero to the class of compact operators.

## Proof

**1. Exact form of every commuting operator.** Put \(d_0=1\) and
\[
 d_n=\prod_{r=0}^{n-1}w_r\ne0\qquad(n\ge1).
\]
Then \(W^n e_0=d_n e_n\). If \(SW=WS\) and \(S e_0=\sum_{k\ge0}c_k e_k\), boundedness of \(S\) and continuity of the coordinate maps give, for every \(n\ge0\),
\[
 S e_n=d_n^{-1}W^nS e_0
   =\sum_{k\ge0}c_k\frac{d_{n+k}}{d_kd_n}\,e_{n+k}.
 \tag{1}
\]
In particular, \(S\) is lower triangular with constant diagonal entry \(c_0\). If all \(c_k\) with \(k\ge1\) are zero, formula (1) gives \(S=c_0I\) on the dense linear span of the basis, hence everywhere.

**2. Empty point spectrum for a non-scalar commutant element.** Suppose \(S\ne c_0I\), and let \(k\ge1\) be the least index with \(c_k\ne0\). Assume \(Sx=\lambda x\) for some nonzero \(x\in\ell_p\). The set of indices of nonzero coordinates of \(x\) has a least element, say \(m\), with \(x_m\ne0\). By (1), the \(m\)-th coordinate of \(Sx\) is \(c_0x_m\), forcing \(\lambda=c_0\). Yet the \((m+k)\)-th coordinate of \((S-c_0I)x\) equals
\[
 c_k\frac{d_{m+k}}{d_kd_m}\,x_m\ne0.
 \tag{2}
\]
Indeed, no term with source index less than \(m\) appears, and every source index greater than \(m\) needs a shift of at least \(k\), so cannot contribute at coordinate \(m+k\). Equation (2) contradicts \((S-c_0I)x=0\). Hence \(\sigma_{\mathrm p}(S)=\varnothing\).

**3. Rank-one obstruction.** If a nonzero finite-rank operator \(F\) commuted with a non-scalar \(S\), its nonzero finite-dimensional range would be invariant under \(S\). Over the complex field \(S\) would possess an eigenvector in that range, contrary to Step 2. Thus no such \(F\) exists. This rules out both one-edge and two-edge routes from \(W\) to nonzero finite rank; the one-edge case follows also by taking \(S=W\).

**4. Sharp three-edge route.** The bounded operators \(W\), \(W^2\), \(P_{\mathrm{even}}\), and \(F_0\) are all non-scalar; \(F_0\) has rank one. The identities \(WW^2=W^2W\), \(W^2P_{\mathrm{even}}=P_{\mathrm{even}}W^2\), and \(P_{\mathrm{even}}F_0=F_0P_{\mathrm{even}}\) hold on every basis vector, hence on the full Banach space. Therefore the claimed three-edge chain exists and is shortest.

**5. Compact Schatten counterexample.** For \(K e_n=2^{-(n+1)}e_{n+1}\), the weights tend to zero, making \(K\) a norm limit of finite-rank truncations and hence compact. For every integer \(r\ge1\), decreasing weights give
\[
 \|K^r\|=\sup_{n\ge0}\prod_{j=n}^{n+r-1}2^{-(j+1)}
          =2^{-r(r+1)/2},
\]
so \(\lim_{r\to\infty}\|K^r\|^{1/r}=0\), proving quasinilpotence. Its positive singular values are precisely \(2^{-(n+1)}\), hence
\[
 \sum_{n=0}^{\infty}s_n(K)^q=\sum_{n=0}^{\infty}2^{-q(n+1)}<\infty
 \qquad(q>0).
\]
All weights are nonzero, so the obstruction in Steps 1–3 applies. This supplies the promised negative instance of the two-edge rank-one question.

## Verification

The proof is infinite-dimensional and algebraic: (1) reconstructs the entire commutant from one cyclic basis vector, (2) is a first-nonzero-coordinate contradiction, and the rest uses exact commutator identities and geometric series. The accompanying `check_coefficients.py` tests the coefficient identity, commutativity, parity-projection chain, and product norm formula with **exact rational arithmetic** for finite truncations of sizes 6, 8, 12, and 16 (542 grouped test cases, all passed). Finite truncations are nilpotent and cannot test the infinite-dimensional empty-point-spectrum assertion; that assertion is justified solely by Steps 1–2. Reproduce via `python check_coefficients.py`.

## Relationship to prior work

Szczepanski's Proposition 3.2 proves that weighted shifts admit three-edge chains to rank-one operators, and Remark 3.4 explicitly describes the parity construction for multiplication shifts. The upper bound and the construction in Step 4 are **previously known**, not new. Section 4, Problem 4.5 asks whether **two** edges always suffice when the initial compact operator is quasinilpotent. Its Example 4.4 proves a positive instance for the Volterra operator. Here the new point is the universal **lower bound** for injective unilateral shifts, furnished by (1)–(2), and the resulting negative answer for a compact quasinilpotent example. The full 2025 preprint and the 2026 revised paper were compared by mathematical implication, not title.

Ambrozie, Bračič, Kuzma, and Müller (2013) establish general commuting-graph connectivity for selected operator classes. Only their accessible abstract was inspected for the present comparison, so hidden stronger results in that paper are a residual priority risk; its abstract does not state the present uniform minimality theorem. This is not claimed to settle all compact quasinilpotent operators or to give uniqueness of the exhibited three-edge chain.

## Limitations

The empty-point-spectrum proof uses the natural well-ordered basis of one-sided shifts and assumes every weight is nonzero. It does not cover bilateral shifts, shifts with zero weights, or general compact quasinilpotents. The finite program does not prove the infinite result. Independently established literature priority remains subject to future full-text comparison, especially with older commuting-graph theory; no independent mathematical audit has been performed.

## References

1. T. Szczepanski, *On the chain of commuting operators on Banach spaces*, arXiv:2507.14297v1 (first public July 18, 2025), arXiv:2507.14297v2 (July 20, 2026), Proposition 3.2, Remark 3.4, Example 4.4, Problem 4.5; *Bulletin of the London Mathematical Society* (2026), DOI 10.1112/blms.70471. Full open text: https://arxiv.org/html/2507.14297v2.
2. C. Ambrozie, J. Bračič, B. Kuzma, V. Müller, *The commuting graph of bounded linear operators on a Hilbert space*, *Journal of Functional Analysis* **264** (2013), 1068–1087, DOI 10.1016/j.jfa.2012.11.011 (abstract inspected; full text unavailable in this investigation).
