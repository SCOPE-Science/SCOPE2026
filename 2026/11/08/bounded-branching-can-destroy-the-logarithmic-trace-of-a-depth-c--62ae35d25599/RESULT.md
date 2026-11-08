# Bounded branching can destroy the logarithmic trace of a depth commutator without changing the shift

## Finding

Let \(a_0=1\) and let \((a_k)_{k\geq0}\) be any sequence with \(a_k\in\{1,2\}\). Form a rooted, spherically homogeneous tree in which every vertex at depth \(k\) has
\[
b_k=\frac{2a_{k+1}}{a_k}\in\{1,2,4\}
\]
children. Its number of level-\(k\) vertices is \(L_k=2^ka_k\). On \(H=\ell^2(V)\), let \(B\) be the normalized backward shift and \(D\) the depth observable,
\[
Be_w=\begin{cases}b_{k-1}^{-1/2}e_{\operatorname{par}(w)},&|w|=k\geq1,\\0,&w\text{ is the root},\end{cases}
\qquad De_v=2^{-|v|}e_v.
\]
Set \(K=DB-BD\). **The complete nonzero singular-value list** of \(K\) consists of \(2^{-k-1}\) with multiplicity \(2^ka_k\), for every \(k\geq0\). Thus \(K\in\mathcal S_p\) exactly for \(p>1\), and \(K\) is weak trace class but not trace class.

More precisely, with singular values in decreasing order and \(A_N=\sum_{j=1}^{N}s_j(K)\),
\[
\begin{split}
\liminf_{N\to\infty}\frac{A_N}{\log N}
 &=\frac1{2\log2}\liminf_{m\to\infty}\frac1m\sum_{k=0}^{m-1}a_k,\\
\limsup_{N\to\infty}\frac{A_N}{\log N}
 &=\frac1{2\log2}\limsup_{m\to\infty}\frac1m\sum_{k=0}^{m-1}a_k.
\end{split}
\]
Consequently the logarithmic singular-value mean exists **if and only if** the ordinary Cesàro mean of the normalized level populations \(a_k\) exists.

For the regular binary tree (all \(a_k=1\)), this limit is \(1/(2\log2)\). There is also an explicit bounded-branching tree with the same exponential level-growth rate \(\lim_{k\to\infty}L_k^{1/k}=2\), but
\[
\liminf_{N\to\infty}\frac{A_N}{\log N}=\frac1{2\log2},
\qquad
\limsup_{N\to\infty}\frac{A_N}{\log N}=\frac1{\log2}.
\]
For this latter tree, \(|K|\) is **not Connes–Dixmier measurable**, by the established equivalence between such measurability and convergence of logarithmic singular-value means. In both cases, \(B\) is a pure coisometry of countably infinite multiplicity, hence the two shifts are unitarily equivalent. In the oscillating example, **all but a set of levels of natural density zero have exactly two children per vertex**: only block transitions have one or four children. Moreover, the associated unnormalized backward shifts have the same spectral radius \(\sqrt2\), by the branching-radius formula of Buckley and Seco.

## Assumptions and scope

All Hilbert spaces are complex and separable. Levels begin at depth zero, the logarithm is natural, and \(\mathcal S_p\) has its usual singular-value definition for every \(p>0\). By weak trace class we mean \(\sup_{n\geq1}ns_n(K)<\infty\). A positive compact operator is Connes–Dixmier measurable when all Connes–Dixmier traces agree, using the standard logarithmic Marcinkiewicz ideal. The nonmeasurability assertion concerns the positive operator \(|K|\), not the possibly non-self-adjoint commutator \(K\) itself.

## Proof

**Tree realization.** The ratio \(2a_{k+1}/a_k\) is one of \(1,2,4\). Starting with one root and giving every level-\(k\) vertex that many children produces a locally finite, leafless tree. By induction \(L_0=1\) and \(L_{k+1}=b_kL_k=2^{k+1}a_{k+1}\). Hence \(2^k\leq L_k\leq2^{k+1}\), so all trees in the family have exponential population growth exactly two.

**Underlying shift.** For every vertex \(v\) at level \(k\),
\[
B^*e_v=b_k^{-1/2}\sum_{w\in\operatorname{Chi}(v)}e_w.
\]
The displayed vectors are orthonormal because distinct parents have disjoint child sets; each has norm one. Thus \(B^*\) is an isometry and \(BB^*=I\). Its \(n\)-fold range is supported on levels at least \(n\), so \(\bigcap_{n\geq0}(B^*)^nH=\{0\}\); it is a pure isometry. Since infinitely many levels contain branching, \(\ker B\) is infinite-dimensional. The Wold decomposition therefore identifies each such \(B\) with the backward unilateral shift of countably infinite multiplicity.

**Exact singular spectrum.** If \(w\) is a child of a level-\(k\) vertex \(v\), then
\[
Ke_w=\frac{2^{-k}-2^{-k-1}}{\sqrt{b_k}}e_v
=\frac{2^{-k-1}}{\sqrt{b_k}}e_v.
\]
Different parents have disjoint sets of children, so \(KK^*\) is diagonal in the vertex basis and
\[
KK^*e_v=b_k\frac{2^{-2k-2}}{b_k}e_v=2^{-2k-2}e_v.
\]
The multiplicity at depth \(k\) is \(L_k\), proving the complete nonzero singular-value list. No finite truncation is used in this argument. Also \(\|K\|=1/2\) and \(K\) is compact. Since \(2^k\leq L_k\leq2^{k+1}\),
\[
\sum_{j=1}^\infty s_j(K)^p
=\sum_{k\geq0}L_k2^{-p(k+1)}
\]
converges exactly when \(p>1\). If \(M_k=\sum_{j=0}^kL_j\), then \(2^{k+1}-1\leq M_k\leq2^{k+2}-2\). On the rank interval ending at \(M_k\), the singular value equals \(2^{-k-1}\); hence \(ns_n(K)\leq2\) at every rank. The trace diverges because every level contributes at least \(1/2\).

**Logarithmic criterion.** At completed levels the partial sum is exactly
\[
A_{M_k}=\sum_{j=0}^kL_j2^{-j-1}=\frac12\sum_{j=0}^ka_j.
\]
For any \(M_{k-1}<N\leq M_k\), the two neighboring partial sums differ by at most one and \(\log N=k\log2+O(1)\), uniformly for large \(k\). It follows that
\[
\frac{A_N}{\log N}
=\frac1{2\log2}\frac1k\sum_{j=0}^{k-1}a_j+O(k^{-1}),
\]
with a uniform error term. The liminf, limsup and convergence equivalence follow.

**Nonconvergent example.** Partition the nonnegative levels into successive blocks of lengths \(T_r=2^{2^{r+2}}\), for \(r=0,1,2,\ldots\). Define \(a_k=1\) on even-numbered blocks and \(a_k=2\) on odd-numbered blocks. Since \(T_r/\sum_{j<r}T_j\to\infty\), the Cesàro mean of \(a_k\) approaches one along even block endpoints and two along odd block endpoints. Every mean lies in \([1,2]\), so its precise liminf and limsup are one and two. All but the first level of each block have \(b_k=2\); the exceptional transition levels have zero natural density because the block lengths diverge. For every starting level \(j\) and depth increment \(m\), the number of descendants of a vertex after \(m\) steps is \(2^m a_{j+m}/a_j\), which lies between \(2^{m-1}\) and \(2^{m+1}\). Thus the upper and lower exponential descendant-growth rates both equal \(\log2\); the standard branching-radius formula yields \(\sqrt2\) for the spectral radius of the unnormalized backward shift. Applying the logarithmic criterion proves the displayed distinct limits. The usual Connes–Dixmier measurability criterion for positive elements of the logarithmic ideal (Lord–Sedaev–Sukochev, Theorem 6.6) then implies that \(|K|\) is not measurable. This uses an existing theorem about singular traces, not a new characterization of those traces.

## Verification

The complete proof is analytic. The companion script `verification_checker.py` uses exact rational arithmetic to check tree-population recurrences, disjoint sibling Gram blocks, the squared singular weights, monotone ordering and finite partial-trace identities for several branching patterns. In the recorded execution it passed 29,532 assertions. This is a corroboration of the finite algebra, not evidence by itself for any infinite statement or for publication priority. Reproduce with `python3 verification_checker.py`.

## Relationship to prior work

Buckley and Seco (2026), arXiv:2610.40089, study Rota universality and the spectral radius of tree shifts in terms of branching. Their operator is the unnormalized backward shift; the present normalized coisometry, its depth commutator, and the spectral logarithmic trace are different objects and questions. Budzyński, Dymek, Planeta and Ptak (2017), arXiv:1702.00765, treat multiplier algebras, reflexivity and Wold-type decompositions of weighted tree shifts, providing background rather than the trace criterion above. Lord, Sedaev and Sukochev (2005), arXiv:math/0501131, already proved the abstract equivalence of Connes measurability and convergence of logarithmic singular-value means; we use it verbatim after computing the tree-specific singular spectrum. Guido and Isola (2002), arXiv:math/0202108, investigate general singular traces and fractal spectral triples, which are different operator realizations. The specific contribution here is the sharp level-population criterion together with bounded-branching realization of divergent logarithmic trace means **for unitarily equivalent tree coisometries**.

## Limitations

The criterion uses a particular depth diagonal and normalized coisometry, with normalized populations restricted to one or two. It does not give a theory for arbitrary weighted tree shifts, arbitrary radial functions, or the unnormalized backward shift. Nonconvergence of a logarithmic mean is not a claim about nonexistence of all generalized singular traces. The independent priority of this tree-specific construction remains subject to specialist review; abstract Tauberian and Wold results are acknowledged as known.

## References

1. J. Buckley and D. Seco, *Rota universality of shifts on trees*, arXiv:2610.40089, first submitted 2026-10-29. https://arxiv.org/abs/2610.40089.
2. P. Budzyński, P. Dymek, A. Planeta and M. Ptak, *Weighted shifts on directed trees. Their multiplier algebras, reflexivity and decompositions*, arXiv:1702.00765. https://arxiv.org/abs/1702.00765.
3. S. Lord, A. Sedaev and F. Sukochev, *Dixmier Traces as Singular Symmetric Functionals and Applications to Measurable Operators*, arXiv:math/0501131, Theorem 6.6. https://arxiv.org/abs/math/0501131.
4. D. Guido and T. Isola, *Dimensions and singular traces for spectral triples, with applications to fractals*, arXiv:math/0202108. https://arxiv.org/abs/math/0202108.
