# A universal defect-rank law in two-block flag-preserving matrix monoids

## Finding
Fix a prime power \(q\) and positive integers \(a,b\). Let \(\mathcal P_{a,b}(q)\) be the multiplicative monoid of all linear endomorphisms of \(\mathbb F_q^{a+b}\) preserving a distinguished \(a\)-dimensional subspace. With a chosen complement, write every element uniquely as
\[
X=\begin{pmatrix}A&B\\0&D\end{pmatrix},\qquad A\in M_a(\mathbb F_q),\ D\in M_b(\mathbb F_q),\ B\in M_{a\times b}(\mathbb F_q).
\]
Set \(r=\operatorname{rank}A\), \(s=\operatorname{rank}D\), and define the **regularity defect**
\[
\delta(X)=\operatorname{rank}\bigl(\ker D\xrightarrow{\ B\ }\mathbb F_q^a/\operatorname{im}A\bigr).
\]
The definition is independent of the chosen complement. One has \(0\le\delta\le\min(a-r,b-s)\), and \(\operatorname{rank}X=r+s+\delta\). Moreover \(X\) is von Neumann regular in this monoid (there is \(Y\) in the same monoid with \(XYX=X\)) if and only if \(\delta(X)=0\).

Define the number of \(u\times v\) matrices of rank \(t\) by
\[
R_q(u,v,t)={u\brack t}_q{v\brack t}_q\prod_{j=0}^{t-1}(q^t-q^j),
\]
where \({u\brack t}_q\) is the Gaussian binomial coefficient and the empty product is one. The **complete three-parameter defect spectrum**, for every \(0\le r\le a\), \(0\le s\le b\), and \(0\le t\le\min(a-r,b-s)\), is
\[
\boxed{\#\{X:(\operatorname{rank}A,\operatorname{rank}D,\delta)=(r,s,t)\}
=R_q(a,a,r)R_q(b,b,s)\,q^{ab-(a-r)(b-s)}R_q(a-r,b-s,t).}
\]
All the indicated strata are nonempty. In fact \((r,s,t)\) is a complete invariant of the two-sided action of the unit group of \(\mathcal P_{a,b}(q)\): two elements lie in one unit left-right orbit exactly when these triples agree.

For fixed \(q\), independently let \(a,b\to\infty\), without any restriction on their relative growth. Define
\[
P_q=\prod_{j\ge1}(1-q^{-j}),\qquad
\pi_q(i)=\frac{P_q}{q^{i^2}\prod_{j=1}^{i}(1-q^{-j})^2}\quad(i\ge0).
\]
If \(X\) is uniform in \(\mathcal P_{a,b}(q)\), its entire defect distribution converges, with
\[
\boxed{\lim_{\min(a,b)\to\infty}\Pr(\delta(X)=t)
=\sum_{i,j\ge0}\pi_q(i)\pi_q(j)\frac{R_q(i,j,t)}{q^{ij}}\qquad(t=0,1,\ldots).}
\]
The sums are absolutely convergent. In particular, the limiting fraction of regular elements is strictly between zero and one, and is
\[
\boxed{\mathcal R_q=\sum_{i,j\ge0}\pi_q(i)\pi_q(j)q^{-ij}.}
\]
For \(q=2\), \(\mathcal R_2\approx0.6998513223\). Thus nonregularity retains a positive density even when both diagonal blocks tend to arbitrarily large sizes.

## Assumptions and scope
All matrices and ranks are over the same finite field of cardinality \(q\), any prime power, including even characteristic. Both block sizes are positive for the limit statement, and the limit only assumes \(\min(a,b)\to\infty\). The invariant concerns **von Neumann regularity inside the block-preserving monoid**, not regularity in the full matrix monoid, where every matrix is regular. The rank census is exact for every finite \(a,b\).

## Proof
1. **Canonical defect and rank.** Let \(U\) denote the invariant subspace. The image of \(X\), projected to \(V/U\), has dimension \(s\). Its intersection with \(U\) is \(\operatorname{im}A+B(\ker D)\), of dimension \(r+\delta\). This proves \(\operatorname{rank}X=r+s+\delta\) and the complement-free identity \(\delta=\dim((\operatorname{im}X\cap U)/X(U))\).

2. **Regularity.** If \(XYX=X\) with \(Y(U)\subseteq U\), then every \(z\in\operatorname{im}X\cap U\) satisfies \(z=XYz\in X(U)\); hence \(\delta=0\). Conversely, if \(\operatorname{im}X\cap U=X(U)\), choose a linear section of \(X:V\to\operatorname{im}X\) which sends \(\operatorname{im}X\cap U\) into \(U\). Extend the section to an endomorphism \(Y:V\to V\) by taking a complement of \(\operatorname{im}X\cap U\) inside \(U\), then extending to a complement of \(\operatorname{im}X+U\). Set \(Y=0\) on these complements. It preserves \(U\) and gives \(XYX=X\).

3. **Two-sided unit orbits.** Independent invertible row and column changes inside each diagonal block reduce \(A\) and \(D\) to rank-standard matrices. Right multiplication by a block-upper unit changes \(B\) by \(AC\), and left multiplication changes \(B\) by \(CD\). These remove all entries outside the induced map \(\ker D\to\operatorname{coker}A\). The residual rank-\(t\) matrix is reduced to an identity block by independent invertible changes of bases on \(\ker D\) and \(\operatorname{coker}A\). Conversely \(r,s,\delta\) are invariant under these operations. Thus the triple classifies unit double orbits.

4. **Finite enumeration.** There are \(R_q(a,a,r)\) choices for \(A\) and \(R_q(b,b,s)\) for \(D\). For fixed diagonal blocks, the map from the vector space of all \(B\)'s onto \(\operatorname{Hom}(\ker D,\mathbb F_q^a/\operatorname{im}A)\), of dimension \((a-r)(b-s)\), is surjective. Every fiber has cardinality \(q^{ab-(a-r)(b-s)}\). Exactly \(R_q(a-r,b-s,t)\) of the quotient maps have rank \(t\). This proves the displayed formula and normalization to \(q^{a^2+ab+b^2}\).

5. **Asymptotics.** The independent uniform diagonal blocks have nullities \(I_a=a-r\) and \(J_b=b-s\). A direct rank count gives
\[
\Pr(I_n=i)=q^{-i^2}\frac{\bigl(\prod_{j=1}^{n}(1-q^{-j})\bigr)^2}{\bigl(\prod_{j=1}^{i}(1-q^{-j})\bigr)^2\prod_{j=1}^{n-i}(1-q^{-j})}.
\]
As \(n\to\infty\), this tends to \(\pi_q(i)\). It is dominated by \(q^{-i^2}/P_q\), an absolutely summable sequence, so convergence of the full nullity laws is in total variation and \(\sum_i\pi_q(i)=1\). Conditional on these nullities, \(\delta\) has precisely the rank distribution of a uniformly chosen \(i\times j\) matrix, independent of the remaining blocks. Dominated convergence proves the entire limiting law. Since \(\pi_q(0)>0\), \(\mathcal R_q>0\); since \(\pi_q(1)>0\) and \(\Pr(\operatorname{rank}M_{1,1}=1)=1-q^{-1}\), \(\mathcal R_q<1\).

## Verification
`checker.py` performs independent finite-field Gaussian elimination and full enumeration, comparing the theoretical count to the rank of every allowed block matrix. Tested \((q,a,b)=(2,1,1),(3,1,1),(5,1,1),(2,1,2),(2,2,1),(3,1,2),(2,2,2)\). For \(a=b=1\), it also directly tests existence of \(Y\) with \(XYX=X\) by enumerating every candidate \(Y\). The stored output is `checker_output.txt`; the checker uses prime fields only, while the proof handles all prime powers. Finite tests corroborate but do not establish the unbounded theorem.

## Relationship to prior work
Patrício and Puystjens (2001) develop criteria for regularity of triangular block matrices over rings. The established regularity characterization is baseline, **not** claimed as new. Kambites and Steinberg (2005), especially Proposition 3.2 and Section 5, establish regular-element structure for scalar triangular matrix semigroups and optimal wreath decompositions; their results do not state this two-block all-defect finite-field spectrum or its limit. Fulman and Goldstein (arXiv first posted 2012) determine the limiting nullity distributions for independent uniform rectangular matrices, which are used as a known input rather than reclaimed. Wright (2020) treats regular triangular matrices and implicit finite-ring counting but is focused on scalar triangular rings, rather than this complete joint block-defect distribution. No claim of uniqueness follows from absence in search results.

## Limitations
The new claim is confined to exact defect multiplicities, the unit double-orbit refinement, and their two-large-block limit. The regularity criterion by itself is not new. The full text of Patrício–Puystjens (2001) and Wright (2020) was not accessible for a definitive priority comparison; they remain priority risks. No results are asserted for flags with three or more proper layers. No independent mathematical audit has occurred.

## References
- P. Patrício and R. Puystjens, *About the von Neumann regularity of triangular block matrices*, Linear Algebra Appl. 332–334 (2001), 485–502, DOI: 10.1016/S0024-3795(01)00295-6 (public date recorded as 2001-08-01).
- M. Kambites and B. Steinberg, *Wreath product decompositions for triangular matrix semigroups*, arXiv:math/0512024, first posted 2005-12-01, https://arxiv.org/abs/math/0512024.
- J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, arXiv:1211.0504, first posted 2012-11-02, https://arxiv.org/abs/1211.0504.
- S. E. Wright, *Constructing and counting regular triangular matrices*, Linear Multilinear Algebra 70 (2022), 3936–3943, first online 2020-12-08, DOI: 10.1080/03081087.2020.1857679.
