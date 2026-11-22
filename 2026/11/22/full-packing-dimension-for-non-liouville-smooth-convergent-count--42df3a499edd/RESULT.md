# Full packing dimension for non-Liouville smooth-convergent counterexamples

## Finding

For each real \(\tau\ge4\), let \(F_\tau\) denote all \(\xi\in(1,2)\) with irrationality exponent \(\mu(\xi)=\tau\) for which infinitely many regular continued-fraction convergents are exactly \(2^a/3^b\), with positive integers \(a,b\). Then

\[
\dim_{\mathrm H}F_\tau=0,\qquad \dim_{\mathrm P}F_\tau=1.
\]

Moreover, \(F_\tau\) contains a compact perfect Cantor set \(K_\tau\) with the same two dimensions. Thus a set of non-Liouville counterexamples to the Erdős–Mahler conjecture is simultaneously Hausdorff-null in every positive dimension and of maximal packing dimension in the real line.

## Assumptions and scope

The irrationality exponent \(\mu(\xi)\) is the supremum of \(\nu>0\) for which infinitely many reduced fractions \(u/v\) satisfy \(0<|\xi-u/v|<v^{-\nu}\). The Euclidean Hausdorff and packing dimensions are denoted \(\dim_{\mathrm H}\) and \(\dim_{\mathrm P}\). All irrationality exponents \(\tau\) in the assertion are real and at least \(4\). In particular, finite \(\tau\) makes every constructed number non-Liouville.

The proof uses the non-elementary exceptional-approximation Proposition 2.1 of Diego Marques [1] as an explicitly cited input. Only the strengthened multibranch selection, dimension arguments, and the consequent metric classification are derived here. No effective upper bound on the starting stage or branch thresholds is asserted.

## Proof

**1. Prescribed smooth fractions and admissibility.** Put

\[
\alpha=\frac{\log 3}{\log2},\quad
R(b)=\frac{2^{\lceil b\alpha\rceil}}{3^b},\quad
\Phi(y)=1-\frac{\log y}{\log2},\quad
\mathcal D=\{\text{denominators of convergents to }\alpha\}.
\]

As \(\alpha\) is irrational, \(R(b)\) is reduced, lies strictly between \(1\) and \(2\), and is the unique fraction \(2^a/3^b\) in that interval for its denominator \(3^b\). Also \(\Phi(R(b))=\{b\alpha\}\). For all \(N\in\mathcal D\), Marques's Lemma 2.2 [1] gives, **uniformly in every arc** \(I\) on the circle,

\[
\#\{b\in[N,2N):\{b\alpha\}\in I\}=N|I|+O(1).
\tag{1}
\]

Fix \(\tau\ge4\). For a sufficiently large integer \(t\), let \(Q_t=3^t\),

\[
J_t=(R(t)+Q_t^{-\tau},R(t)+2Q_t^{-\tau}),\quad
K(t)=[R(t)+Q_t^{-\tau},R(t)+3Q_t^{-\tau}],
\]

\[
D_t=Q_t^{\tau-1}/6,\qquad \nu_t=4+1/t,\qquad \rho_t=|\Phi(J_t)|>0.
\]

An index \(b\) is admissible for \(t\) if \(R(b)\in J_t\) and there is no reduced rational \(u/v\in[1,2]\), distinct from \(R(b)\), satisfying both \(v>D_t\) and \(|R(b)-u/v|<1/(16v^{\nu_t})\). The exceptional-approximation Proposition 2.1 and Lemma 2.3 of [1] yield, for every sufficiently large \(t\),

\[
\liminf_{\substack{N\to\infty\\N\in\mathcal D}}
\frac{\#\{b\in[N,2N):b\text{ admissible for }t\}}{N}
\ge\frac{\rho_t}{2}>0.
\tag{2}
\]

Indeed the error in the cited proposition is \(O(D_t^{2-\nu_t})=O(Q_t^{-2(\tau-1)})\), smaller than \(\rho_t\asymp Q_t^{-\tau}\) for \(\tau\ge4\). We use (1) and (2) with their stated uniformity, not merely the existence of two successors in [1].

**2. A separated linear-size supply of children.** Since \(|\Phi'(y)|\le1/\log2\) for \(y\in[1,2]\), (1) implies that for every \(N\in\mathcal D\), **every** interval in \([1,2]\) of length \(20/N\) contains at most an absolute number \(C_0\) of values \(R(b)\) with \(N\le b<2N\). In particular, after the admissible count in (2), a greedy deletion of all points within \(20/N\) of a selected point leaves at least \(c_tN\) pairwise \(20/N\)-separated admissible centers for all sufficiently large \(N\in\mathcal D\), with a fixed \(c_t>0\) depending on \(t\). For example a sufficiently small constant multiple of \(\rho_t/C_0\) works. The key gain over a binary choice is that \(c_t\) is independent of \(N\).

**3. A common block and many branches at every level.** Start with one sufficiently large \(t_0\) and its interval \(K(t_0)\). Suppose level \(j-1\) has finitely many pairwise disjoint closed intervals \(K(t)\), with positive mutual distance. For each of those parents let \(c_t\) be as in Step 2, and set \(c_j>0\) smaller than every \(c_t\). Choose a **common** \(N_j\in\mathcal D\) arbitrarily large, *after* these finitely many parents and \(c_j\) are fixed, so that all parent-specific thresholds of Step 2 are met, \(N_j>3^t\) for every parent, and the following additional conditions hold:

\[
\frac{|\log c_j|}{\log N_j}<\frac1j,\qquad
3\cdot 3^{-\tau N_j}<N_j^{-1},
\]

and \(20/N_j\) is much smaller than the positive separation of distinct parent intervals. The unbounded set \(\mathcal D\) permits all these choices simultaneously. Put \(B_j=\lfloor c_j N_j\rfloor\), choosing \(N_j\) sufficiently large to ensure \(B_j\ge2\). For every parent independently retain exactly \(B_j\) admissible indices \(b\in[N_j,2N_j)\) whose centers \(R(b)\) are pairwise separated by at least \(20/N_j\). Their intervals \(K(b)\) lie strictly inside \(K(t)\): this follows from \(R(b)\in J_t\), \(b>t\), and \(3\cdot3^{-\tau b}<Q_t^{-\tau}\), exactly as verified in [1, proof of the theorem]. The intervals have diameter \(2\cdot3^{-\tau b}\le2\cdot3^{-\tau N_j}\), so the selected level-\(j\) intervals are separated by more than \(5/N_j\) both within and across parents, upon enlarging \(N_j\) as needed.

The resulting nested intersection \(K_\tau\) is compact, nonempty and perfect: each interval has \(B_j\ge2\) disjoint descendants and the maximum depth-\(j\) interval diameter tends to zero. Every branch corresponds to a sequence \(t_0<t_1<\cdots\) of admissible successors with \(t_j\in[N_j,2N_j)\).

**4. Exact irrationality exponent and convergents.** Every \(\xi\in K_\tau\) along its branch satisfies

\[
3^{-\tau t_j}<\xi-R(t_j)<3\cdot3^{-\tau t_j}.
\tag{3}
\]

As \(t_j\to\infty\), rational separation makes \(\xi\) irrational. The right-hand inequality in (3) is eventually below \(1/(2\cdot3^{2t_j})\), so Legendre's criterion shows that each \(R(t_j)\) is a regular continued-fraction convergent. Equation (3) implies \(\mu(\xi)\ge\tau\). For the converse, fix a reduced \(u/v\in[1,2]\), and take the unique \(j\) with \(3^{t_j}\le v<3^{t_{j+1}}\). When \(u/v=R(t_j)\), the left side of (3) bounds the approximation from below by \(v^{-\tau}\). Otherwise, if \(v\le D_{t_j}\), rational separation from \(R(t_j)\) and (3) give \(|\xi-u/v|\ge1/(2v^2)\). If \(v>D_{t_j}\), rational separation from \(R(t_{j+1})\) and its admissibility at \(t_j\) give

\[
|\xi-u/v|\ge\tfrac12|R(t_{j+1})-u/v|
\ge\frac1{32v^{4+1/t_j}}.
\]

These are precisely the inequalities proved for **any admissible branch** in [1, proof of the theorem, equations (3) and following]. Because \(t_j\to\infty\), for every \(\varepsilon>0\) all sufficiently large \(v\) satisfy \(|\xi-u/v|\ge v^{-\tau-\varepsilon}\); thus \(\mu(\xi)\le\tau\). So \(K_\tau\subset F_\tau\).

**5. Sharp packing dimension.** Give each depth-\(j\) cylinder equal mass \(M_j^{-1}\), where \(M_j=\prod_{i=1}^{j}B_i\). Equal branching makes this a consistent Borel probability measure \(\sigma\) supported on \(K_\tau\). By the \(5/N_j\) level separation, any Euclidean ball of radius \(r_j=1/N_j\) meets at most one level-\(j\) interval, hence

\[
\sup_{x\in\mathbb R}\sigma(B(x,r_j))\le M_j^{-1}\le B_j^{-1}.
\tag{4}
\]

The choice of \(N_j\) makes \(\log B_j/\log N_j\to1\). Indeed \(B_j=\lfloor c_jN_j\rfloor\) and \(|\log c_j|/\log N_j<1/j\). To see packing dimension \(1\) without invoking a local-dimension theorem, suppose \(\dim_{\mathrm P}K_\tau< s<1\). By the standard countable-upper-box characterization of packing dimension, \(K_\tau=\bigcup_m E_m\), where each \(E_m\) has upper box dimension smaller than \(s\). For every fixed \(m\), sufficiently small \(r_j\) permit covering \(E_m\) by at most \(C_mr_j^{-s}\) balls of radius \(r_j\); by (4),

\[
\sigma(E_m)\le\frac{C_mN_j^s}{B_j}\longrightarrow0.
\]

Thus \(\sigma(K_\tau)=0\), contradiction. Since \(K_\tau\subset\mathbb R\), its packing dimension is at most \(1\). Therefore \(\dim_{\mathrm P}K_\tau=\dim_{\mathrm P}F_\tau=1\).

**6. Hausdorff dimension of the entire set.** Each smooth convergent \(2^a/3^b\in(1,2)\) must equal \(R(b)\). Every convergent to an irrational number obeys \(|\xi-R(b)|<3^{-2b}\). Consequently

\[
F_\tau\subset\limsup_{b\to\infty}
\big(R(b)-3^{-2b},R(b)+3^{-2b}\big).
\]

For every \(s>0\), the sum of the \(s\)-powers of these interval diameters converges. The Hausdorff–Cantelli covering argument yields \(\dim_{\mathrm H}F_\tau=0\), and therefore \(\dim_{\mathrm H}K_\tau=0\) too. This completes the classification.

## Verification

The analytic dependencies were checked against the primary text of [1]: Proposition 2.1 (exceptional approximations), Lemma 2.2 (uniform circle-arc count), Lemma 2.3 (positive lower density), and the complete irrationality-exponent argument in Section 2. The new steps requiring separate checking are the bounded local multiplicity from uniform discrepancy, the finite-parent common-block construction, the uniform same-level separation, and the countable-upper-box contradiction. All are proved above with explicit quantifiers. The result is non-effective because the cited exceptional-approximation input invokes a Subspace Theorem; no finite sample or program is claimed to certify the infinite theorem.

## Relationship to prior work

Marques [1] constructs a binary-branch Cantor set for every \(\tau\ge4\) but does not give a packing-dimension law for the two-prime smooth-convergent locus. The density statement implicit in his Lemma 2.3, combined with uniform distribution at convergent-denominator blocks, allows a distinct many-branch construction of maximal packing dimension. The Hausdorff-zero part is consistent with the bounded-cofactor Hausdorff-dimension result of Fraenkel and Borosh, cited in [1], and also follows directly from the summable convergent-cover argument above. Schleischitz [2] proves packing-dimension results for irrationality-exponent sets without the simultaneous exact numerator \(2^a\), denominator \(3^b\), and continued-fraction-convergent requirements; its stated results do not imply this theorem. The published results compared do not settle the new exact joint dimension classification.

## Limitations

This theorem concerns fixed finite \(\tau\ge4\), not exact irrationality exponents in \((2,4)\), arbitrary pairs of prime bases, or quantitative measures finer than dimension. It does not give effective admissibility thresholds or algorithmically generate an explicitly bounded initial stage. The construction relies materially on the validity of Proposition 2.1 of [1]. A logically equivalent unindexed general packing-dimension theorem may exist; originality is reported with that residual literature risk. No independent audit has been conducted.

## References

[1] Diego Marques, *A counterexample to the Erdős–Mahler conjecture*, arXiv:2611.13604v1, first posted 2026-11-10, https://arxiv.org/html/2611.13604v1 . In particular Proposition 2.1, Lemmas 2.2–2.3, and the proof of the main theorem in Section 2.

[2] Johannes Schleischitz, *Metric results on sumsets and Cartesian products of classes of Diophantine sets*, arXiv:2002.08228, first posted 2020-02-19, https://arxiv.org/abs/2002.08228 . Relevant comparison: packing dimension of much less arithmetically restricted irrationality-exponent sets.

[3] A. S. Fraenkel and I. Borosh, bounded-cofactor Hausdorff-dimension work as identified and cited in [1]; consulted here through the discussion in [1], not claimed to be independently inspected in full.
