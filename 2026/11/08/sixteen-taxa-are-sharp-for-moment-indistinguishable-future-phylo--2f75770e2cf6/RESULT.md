# Sixteen taxa are sharp for moment-indistinguishable future phylogenetic-diversity laws

## Finding

Consider nonplane, unlabeled rooted full-binary tree shapes with unit length on every edge and no edge above the root. Let each leaf independently become extinct with a common probability \(q\in(0,1)\), and let \(X_T(q)\) be rooted Faith phylogenetic diversity of the surviving leaves (the number of edges on their paths to the original root). The empty survival set has diversity zero.

**Theorem.** For every \(2\le n\le15\), the pair of complete response functions \((q\mapsto\mathbb E[X_T(q)],\ q\mapsto\operatorname{Var}(X_T(q)))\) determines the isomorphism class of every such \(n\)-leaf tree. At \(n=16\), exactly one unordered pair of distinct tree shapes has both response functions identical. The two members have different full probability laws at every \(q\in(0,1)\), and their third raw moments differ by

\[
\mathbb E[X_A(q)^3]-\mathbb E[X_B(q)^3]=-6q^{12}(1-q)^2.
\]

Consequently sixteen is the sharp minimum, and such moment-indistinguishable but distribution-distinct pairs exist for every larger leaf count as well.

Write \(L\) for a leaf, \(C=(L,(L,(L,L)))\) for the four-leaf caterpillar and \(B=((L,L),(L,L))\) for the four-leaf balanced shape; parentheses represent unordered sister subtrees. The exceptional pair is

\[
T_A=((C,C),(B,B)),\qquad T_B=((C,B),(C,B)).
\]

In particular, the exact probability difference at diversity score five is

\[
\Pr(X_A(q)=5)-\Pr(X_B(q)=5)=q^{14}(1-q)^2>0.
\]

All equalities of mean and variance above are **identities in the entire parameter** \(q\); no statement is made that equality at an individual parameter identifies a tree.

## Assumptions and scope

Trees are unordered, rooted, full-binary, unlabelled **shapes**, not general branch-length-weighted or multifurcating trees. Each of the \(2n-2\) edges has length one. The two sibling edges leaving the root are counted, but no hypothetical root stem is counted. Taxon extinction is mutually independent with the same probability \(q\). Comparison always takes place between trees with the same number of leaves. This is future rooted phylogenetic diversity under the homogeneous field-of-bullets model, not unrooted diversity or fixed-size rarefaction.

A *collision* means equality of both entire polynomials \(\mathbb E[X_T(q)]\) and \(\operatorname{Var}(X_T(q))\), not equality merely at a selected parameter. Since equality of means also makes equality of variances equivalent to equality of second raw moments, either pair of invariants can be used.

## Proof

**1. Exact moment signatures.** For every edge \(e\), let \(d_e\) denote its number of descendant leaves and let \(Y_e\) indicate that at least one of those leaves survives. Then \(X_T=\sum_eY_e\) and \(\mathbb E Y_e=1-q^{d_e}\). If distinct edges \(e,f\) have disjoint descendant sets, their indicators are independent. If \(e\) is a proper ancestor of \(f\), then \(Y_f=1\) implies \(Y_e=1\), and

\[
\operatorname{Cov}(Y_e,Y_f)
=q^{d_e}(1-q^{d_f}).
\]

Therefore the entire mean and variance polynomials are

\[
\mathbb E[X_T]=\sum_e(1-q^{d_e}),
\]

\[
\operatorname{Var}(X_T)
=\sum_e q^{d_e}(1-q^{d_e})
+2\sum_{e\supsetneq f}q^{d_e}(1-q^{d_f}),
\]

where \(e\supsetneq f\) ranges once over ordered proper ancestor–descendant edge pairs. In particular, all coefficients are integers, and these two formulas constitute an exact finite collision test.

**2. Exhaustive first-exception computation.** Define \(\mathcal S_1=\{L\}\). For each \(n\ge2\), generate every tree as one unordered pair \((U,V)\) with \(|U|+|V|=n\), \(|U|\le |V|\), resolving equal-sized sister ordering by a fixed total canonical order. Induction on the number of leaves proves that this generates every unordered rooted full-binary isomorphism type once and only once. For each generated shape, recursively list its edge descendant sizes and its proper ancestor–descendant edge-size pairs; evaluate the two integer coefficient vectors in step 1; group by the ordered pair of coefficient vectors.

For leaf counts \(2,3,\ldots,16\), the exact generated shape counts are respectively

\[
1,1,2,3,6,11,23,46,98,207,451,983,2179,4850,10905.
\]

There are **zero** nontrivial collision classes for \(n=2,\ldots,15\). At \(n=16\), there is exactly **one** collision class, of cardinality two, and canonical comparison identifies its members precisely as \(T_A,T_B\) displayed above. The accompanying `checker.py` performs every generation and signature comparison in integer arithmetic, asserting these counts and identifying the unique colliding class. This computationally exhaustive finite step is part of the proof; its assumptions and finite range are explicit. It does not infer any infinite statement from finite samples.

**3. Distributional distinction and general swap identity.** For any rooted \(s\)-leaf subtree shape \(U\), define \(F_U(q,z)\) as the probability generating polynomial of its surviving-edge contribution **including one incoming unit edge**, counted only when some descendant leaf survives. Thus \(F_U(q,1)=1\) and its constant coefficient in \(z\) is \(q^s\). For two same-sized shapes \(U,V\), the incoming-edge contribution of their binary parent has generating polynomial

\[
H_{UV}(q,z)=q^{2s}+z(F_U(q,z)F_V(q,z)-q^{2s}).
\]

For the root-level trees \(A=((U,U),(V,V))\) and \(B=((U,V),(U,V))\), independence of the two root children gives \(P_A=H_{UU}H_{VV}\), \(P_B=H_{UV}^2\). Direct multiplication yields the exact identity

\[
\boxed{P_A(q,z)-P_B(q,z)=q^{2s}z(1-z)(F_U(q,z)-F_V(q,z))^2.}
\]

Because \(F_U(q,1)=F_V(q,1)=1\), the difference is divisible by \((z-1)^3\). Thus its first two derivatives at \(z=1\) vanish: the corresponding trees have the same first two raw moments, hence the same mean and variance, for every \(q\). If \(\mu_U=\partial_zF_U(q,1)\) and \(\mu_V=\partial_zF_V(q,1)\), the third derivative is exactly \(-6q^{2s}(\mu_U-\mu_V)^2\).

For \(U=C\), \(V=B\), we have \(s=4\) and the directly expanded subtree difference

\[
F_C(q,z)-F_B(q,z)
=q^2z^2(q-1)(z-1)(qz^2-2qz+q-z^2).
\]

In particular \(\mu_C-\mu_B=q^2(1-q)\). The boxed identity gives the claimed third-moment gap. Its lowest nonzero power of \(z\) has coefficient \(q^{14}(1-q)^2\), proving a strict law difference for each \(0<q<1\).

**4. Larger trees.** Given a colliding pair on \(m\) leaves, attach to each tree a new root having one common new leaf on one side and the original tree on the other. If the original generating polynomials are \(P_A,P_B\), the new difference is \(z(q+(1-q)z)(P_A-P_B)\), since both old trees have extinction-only mass \(q^m\). This nonzero multiplier preserves the zero of order at least three at \(z=1\) and never makes two different laws equal. Inductively, moment-equivalent but distribution-distinct pairs exist for every \(m\ge16\). This concludes the proof.

## Verification

Run `python3 checker.py` using standard Python 3. It verifies the complete canonical tree enumeration through sixteen leaves, exact coefficient signatures derived independently from the edge-indicator covariance formula, and uniqueness of the first collision. For the witness it **separately enumerates every one of \(2^{16}=65,536\) equally probable survival configurations** at \(q=1/2\), constructing the diversity count directly from descendant-leaf bit masks. Its exact probability-count difference, in order of diversity scores \(5,6,7,8,9,10,11,12\), is

\[
(1,-7,17,-15,-1,7,-1,-1)/65536.
\]

The zeroth, first and second moment differences of this vector vanish, and its third raw-moment difference equals \(-24/65536=-3/8192\). A further independent recursive integer-polynomial moment calculation verifies \(-6q^{12}(1-q)^2\) coefficient by coefficient. These direct checks provide independent computational paths to the explicit witness, rather than only repeating the collision grouping.

## Relationship to prior work

Faller, Pardi and Steel (2007 preprint; 2008 journal article) define the future phylogenetic-diversity distribution under independent extinction and derive mean/variance formulas and an exact distribution algorithm. Their §2 studies normal approximation and §3 gives a full-law recursion. Those established ingredients are not claimed here. The contribution here is the sharp injectivity-failure threshold for the **pair of complete mean and variance response curves**, the unique first-exception shape pair, and the general distribution-polynomial swap identity separating its third moment.

Nipperess and Matsen (2013) derive mean and variance under fixed-count phylogenetic rarefaction. That distinct sampling model supplies context for why first two moments are often reported, but its formulas neither impose the independent-extinction probability model nor prove or disprove the present threshold. Earlier mean-response nonidentification at nine leaves does not imply the present mean-and-variance collision, because the second moments distinguish those smaller shapes. The distribution-recursion literature contains tools from which some identities can be derived, but no exact prior statement with the same scope was identified in the sources inspected. Historical originality is provisional pending independent literature review.

## Limitations

The minimality and uniqueness assertion is for unit-edge, unordered rooted full-binary shapes and **equality across all extinction probabilities**. It does not assert identifiability for arbitrary edge lengths, equality only at a fixed probability, nonbinary trees, unequal extinction risks, or unrooted phylogenetic diversity. The classification through sixteen leaves relies on auditable exhaustive exact computation as a finite mathematical certificate. The displayed infinite family is analytic. Extinction independence and equal risks are simplifications, and the example's probability differences can be small in absolute magnitude. No biological field data, empirical effect size, or independent scientific audit is claimed.

## References

1. B. Faller, F. Pardi and M. Steel, *Distribution of phylogenetic diversity under random extinction*, arXiv:0708.0425, first public version 2 August 2007; *Journal of Theoretical Biology* **251** (2008), 286–296, DOI: 10.1016/j.jtbi.2007.11.034. https://arxiv.org/abs/0708.0425
2. D. A. Nipperess and F. A. Matsen IV, *The mean and variance of phylogenetic diversity under rarefaction*, *Methods in Ecology and Evolution* **4** (2013), 566–572, DOI: 10.1111/2041-210X.12042. https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.12042
3. D. P. Faith, *Conservation evaluation and phylogenetic diversity*, *Biological Conservation* **61** (1992), 1–10, DOI: 10.1016/0006-3207(92)91201-3.
