# Fourier recognition and Torelli recovery from Prym-volume profiles of banana curves

## Finding

For each integer \(n\ge3\), consider the genus-\((n-1)\) metric banana graph \(B_n(\ell)\): two vertices joined by \(n\) labeled edges of strictly positive lengths \(\ell_1,\ldots,\ell_n\). Every nonconstant sign pattern \(s=(s_1,\ldots,s_n)\in\{\pm1\}^n\), modulo simultaneous negation, determines a connected free double cover \(\pi_s\). Put
\[
Q_\ell(s)=\operatorname{Vol}^2\bigl(\operatorname{Prym}(\pi_s)\bigr)
\]
using the principally polarized metric Prym volume convention of Len–Zakharov. Extend this function to the trivial (disconnected) covering class by the **formal definition** \(Q_\ell(1)=0\), not by taking a Prym volume.

**Theorem (profile recognition and inversion).** Set \(w_{ij}=\prod_{k\notin\{i,j\}}\ell_k\). For every sign class,
\[
Q_\ell(s)=\sum_{1\le i<j\le n}w_{ij}\frac{1-s_is_j}{2}.
\tag{1}
\]
Write \(Q_i\) and \(Q_{ij}\) for values at the covers whose negative-edge sets are respectively \(\{i\}\) and \(\{i,j\}\), modulo simultaneous sign reversal. Then
\[
w_{ij}=\frac{Q_i+Q_j-Q_{ij}}2.
\tag{2}
\]
Writing \(P=(\prod_{i<j}w_{ij})^{1/\binom{n-1}{2}}\), for any distinct \(j,k\ne i\) the unique lengths are recovered by
\[
\ell_i=\sqrt{\frac{P\,w_{jk}}{w_{ij}w_{ik}}}.
\tag{3}
\]
Thus the labeled collection of **scalar Prym volumes** for all connected free double covers determines the entire metric banana graph, not merely its Jacobian volume.

The image has an intrinsic finite test. For a real function \(Q\) on \(\{\pm1\}^{n}/\{\pm1\}\) with \(Q(1)=0\), define its Walsh coefficient
\[
\widehat Q(S)=2^{1-n}\sum_{[s]}Q(s)\prod_{i\in S}s_i
\]
for each even-cardinality subset \(S\subseteq\{1,\ldots,n\}\). Then \(Q=Q_\ell\) for a unique positive length vector if and only if:
1. \(\widehat Q(S)=0\) whenever \(|S|\ge4\);
2. \(w_{ij}:=-2\widehat Q(\{i,j\})>0\) for all \(i<j\);
3. \(w_{ij}w_{kl}=w_{ik}w_{jl}=w_{il}w_{jk}\) for every four distinct indices \(i,j,k,l\).

For \(n=3\), condition 3 is vacuous. These conditions give a complete semialgebraic recognition theorem in every genus \(n-1\ge2\).

## Assumptions and scope

All edge lengths are positive real numbers. The vertices of \(B_n\) and its \(n\) parallel edges are distinguished to index monodromy classes; if edge labels are forgotten, uniqueness is understood modulo the induced simultaneous edge permutation. The volume is the square of the natural Riemannian volume of the principally polarized **tropical** Prym. The cover associated with the all-equal sign class is disconnected, so its zero profile value is an algebraic extension rather than a geometric Prym measurement. No assertion concerns branched or dilated covers or algebraic Pryms without tropicalization.

In genus one (\(n=2\)), this reconstruction is impossible: connected free double covers have zero-dimensional Pryms with volume \(1\), independent of the two edge lengths. Hence the lower bound \(n\ge3\) is sharp.

## Proof

**1. Reduction to weighted cuts.** The graph has genus \(g=n-1\). In the Len–Zakharov Kirchhoff–Prym volume formula, an odd genus-one decomposition \(F\) consists of \(g-1=n-2\) edges whose deletion leaves a graph with genus-one components having connected preimages. For the banana graph, the complement has exactly two edges, say \(i,j\), making one connected genus-one component. Its preimage in the sign-cover is connected exactly when the monodromy on this two-edge cycle is nontrivial, or \(s_i\ne s_j\). This decomposition has rank one and contributes precisely \(\prod_{k\ne i,j}\ell_k=w_{ij}\), with the formula's factor \(4^{1-1}=1\). Summing gives (1) for every nontrivial class; both sides vanish at the formally defined trivial class.

**2. Pairwise reconstruction.** The singleton cut \(Q_i\) sums weights of pairs incident to \(i\). The cut \(Q_{ij}\) sums weights with exactly one endpoint in \(\{i,j\}\). Hence \(Q_i+Q_j-Q_{ij}=2w_{ij}\), proving (2) even when \(\{i,j\}\) is represented by its complementary cut.

Writing \(P_\ell=\prod_{k=1}^{n}\ell_k\), we have \(w_{ij}=P_\ell/(\ell_i\ell_j)\). In the product over all pairs, each \(\ell_k\) occurs exactly \(\binom{n-1}{2}\) times; thus
\[
\prod_{i<j}w_{ij}=P_\ell^{\binom{n-1}{2}}.
\]
The exponent is positive when \(n\ge3\). Therefore the positive root \(P\) equals \(P_\ell\). For distinct \(j,k\ne i\),
\[
\frac{P\,w_{jk}}{w_{ij}w_{ik}}=\ell_i^2.
\]
Taking its positive square root proves (3), existence of the inverse on actual volume profiles, and uniqueness.

**3. Walsh characterization (necessity).** Characters of the sign quotient are precisely \(\chi_S([s])=\prod_{i\in S}s_i\) for even subsets \(S\). Formula (1) is a linear combination of the trivial character and characters \(\chi_{\{i,j\}}\). Their nonconstant Walsh coefficients are \(-w_{ij}/2\); all higher even-degree coefficients vanish. Positivity is immediate. Because \(w_{ij}=P_\ell/(\ell_i\ell_j)\), all three pairwise products of four distinct indices equal \(P_\ell^2/(\ell_i\ell_j\ell_k\ell_l)\). This gives all three necessary conditions.

**4. Walsh characterization (sufficiency).** Suppose the three conditions hold. For \(n=3\), any three positive weights \(w_{12},w_{13},w_{23}\) admit a unique positive factorization \(w_{ij}=u_i u_j\); for example \(u_1=\sqrt{w_{12}w_{13}/w_{23}}\), \(u_2=w_{12}/u_1\), \(u_3=w_{13}/u_1\). For \(n\ge4\), define the same first three values and put \(u_k=w_{1k}/u_1\) for \(k\ge4\). The four-distinct-index product identities imply \(u_i u_j=w_{ij}\) for every remaining pair. This proves existence of the positive rank-one factorization; uniqueness follows from the first three pair values.

Set \(c=(\prod_i u_i)^{1/(n-2)}\) and \(\ell_i=c/u_i>0\). Since \(\prod_i\ell_i=c^2\), we obtain
\[
\prod_{k\ne i,j}\ell_k=\frac{c^2}{(c/u_i)(c/u_j)}=u_i u_j=w_{ij}.
\]
By the Fourier-support hypothesis, \(Q(s)=a-\frac12\sum_{i<j}w_{ij}s_is_j\) for some real \(a\). The condition \(Q(1)=0\) forces \(a=\frac12\sum_{i<j}w_{ij}\), so \(Q=Q_\ell\) by (1). The uniqueness already proved completes the if-and-only-if statement.

**5. Concrete recognition in genus two and three.** For \(n=3\), the three nontrivial volumes \(Q_1,Q_2,Q_3\) satisfy precisely the strict triangle inequalities, since \(Q_1=\ell_2+\ell_3\), \(Q_2=\ell_1+\ell_3\), and \(Q_3=\ell_1+\ell_2\). For \(n=4\), the seven volumes obey one independent linear Walsh constraint and two tetrad equations, together with strict weight positivity; they form a four-dimensional positive realization locus inside the seven-dimensional space of labeled volume data.

## Verification

The standalone standard-library script `VERIFY.py` implements the signed-cut formula, exact rational Walsh inversion, singleton/two-edge inversion, positive-profile checks, higher Fourier-band vanishing, tetrad relations, and the multiplicative reconstruction identity. It checks \(n=3,4,5,6,7\), including nonuniform rational length vectors. It also constructs a positive cut profile satisfying the Fourier-support property but violating a tetrad, illustrating why the nonlinear image conditions are essential. Execution produces `EXACT_PROFILE_CHECKS_PASS`. The all-\(n\) theorem rests on the symbolic proof above, not finite experimentation.

## Relationship to prior work

Len and Zakharov's *Kirchhoff's theorem for Prym varieties* (2020 preprint; 2022 publication), Theorem 3.4, supplies the forward volume formula used explicitly in Step 1. That general theorem is **not** claimed as new. The contribution here is the inverse theorem and the exact semialgebraic image/recognition conditions across all genus-\((n-1)\) banana strata, from the entire labeled family of double-cover **scalar** volumes. Capobianco's 2026 *Continuity of the tropical Prym–Torelli map* motivates studying functorial Prym data but addresses continuity rather than inverse recognition. Zakharov's 2025 study of the second moment of tropical Pryms uses signed matroids and Voronoi moments; it does not state this all-genus volume-profile inverse and image characterization in the inspected text. No claim of exhaustive historical priority is made.

## Limitations

The recovery requires identifying the covering monodromy class relative to the edge-labeled banana combinatorial type. It does not assert reconstruction from an unlabeled multiset of volumes, from one Prym, or from the abstract group of covering classes without its edge coordinates. It does not generalize automatically to arbitrary metric graphs, ramified covers or vertex-weighted degenerations. A general inverse theorem elsewhere could imply this family; historical priority remains provisional. No independent mathematical audit has been performed.

## References

1. Y. Len and D. Zakharov, *Kirchhoff's theorem for Prym varieties*, arXiv:2012.15235, first submitted 30 December 2020; *Forum of Mathematics, Sigma* 10 (2022), e11, Theorem 3.4. https://arxiv.org/abs/2012.15235 and https://doi.org/10.1017/fms.2021.75.
2. G. Capobianco, *Continuity of the tropical Prym–Torelli map*, arXiv:2608.21625v1, 21 August 2026, especially Introduction and Theorems A–B. https://arxiv.org/abs/2608.21625.
3. D. Zakharov, *The trigonal construction and the second moment of the tropical Prym variety*, arXiv:2507.06401v1, 8 July 2025, especially Introduction and Sections 2–3. https://arxiv.org/abs/2507.06401.
