# Exact distributional swap identity for future rooted phylogenetic diversity

## Finding

Let every edge of a non-plane rooted full-binary phylogenetic tree have length one. Independently retain each leaf with probability \(1-q\), where \(0<q<1\). The rooted Faith diversity \(X_T\) is the number of original edges lying on at least one root-to-retained-leaf path; it is zero when no leaf survives. Write \(P_T(q,z)=\mathbb E[z^{X_T}]\).

For **any** two rooted full-binary subtrees \(U,V\), each having the same number \(s\ge1\) of leaves, form
\[
A=((U,U),(V,V)),\qquad B=((U,V),(U,V)).
\]
Let \(F_U(q,z)\) and \(F_V(q,z)\) be the probability generating polynomials of the contributions of those subtrees **including their incoming unit edges**, with an incoming edge counted if and only if some descendant leaf survives. Then the following exact identity holds as a polynomial in \(q,z\):
\[
\boxed{P_A(q,z)-P_B(q,z)=q^{2s}z(1-z)\big(F_U(q,z)-F_V(q,z)\big)^2.} \tag{1}
\]
Consequently the two trees have identical first and second raw moments, and hence identical means and variances, for every extinction probability. Their third raw moments satisfy
\[
\boxed{\mathbb E[X_A^3]-\mathbb E[X_B^3]
=-6q^{2s}\big(\mu_U(q)-\mu_V(q)\big)^2,}\qquad
\mu_W(q)=\partial_z F_W(q,1). \tag{2}
\]
Whenever \(\mu_U(q)\ne\mu_V(q)\), the third-moment gap is strictly negative and the **entire probability laws** differ at that \(q\).

For the four-leaf caterpillar \(C=(L,(L,(L,L)))\) and balanced tree \(D=((L,L),(L,L))\), equation (1) produces the explicit sixteen-leaf pair \(A=((C,C),(D,D))\), \(B=((C,D),(C,D))\), with
\[
\mathbb E[X_A^3]-\mathbb E[X_B^3]=-6q^{12}(1-q)^2,
\qquad \Pr(X_A=5)-\Pr(X_B=5)=q^{14}(1-q)^2>0. \tag{3}
\]

The **sixteen-leaf first-collision threshold, uniqueness of the first pair, and persistence at all larger leaf counts are not claimed as new**. Earlier published work on uniform fixed-size phylogenetic rarefaction already establishes those results for the *same* unit-edge rooted binary tree family, and its complete two-moment profiles are equivalent to the independent-extinction two-moment curves by binomial conditioning and Bernstein-basis invertibility. The contribution here is solely the explicit general **full-distribution swap factorization** (1), its uniform third-moment consequence (2), and concrete polynomial distinction (3).

## Scope

All trees are unlabelled, nonplane, rooted, full-binary, with unit edge lengths and no root stem. Leaf survival indicators are independent and identically distributed. In (1), the input trees \(U,V\) must have the *same* number of leaves; the statement does not assume they are nonisomorphic or have unequal means. The equalities of lower moments hold for all \(q\in[0,1]\), but strict separation is asserted only for \(0<q<1\) and where the incoming-edge means differ. Formula (3) separates the displayed concrete pair for every interior extinction probability. No claim concerns arbitrary branch lengths, unequal extinction risks, nonbinary or unrooted trees, or identification from noisy empirical moments.

## Proof

For an \(s\)-leaf subtree \(W\), \(F_W(q,1)=1\) and the constant coefficient of \(F_W\) in \(z\) is \(q^s\): exactly when every leaf becomes extinct, the incoming edge contributes nothing. For two \(s\)-leaf children \(U,V\), their independent incoming-edge contributions add, and the edge entering their parent contributes one exactly when at least one of the \(2s\) leaves survives. The generating polynomial including this parent's incoming edge is therefore
\[
H_{UV}(q,z)=q^{2s}+z\big(F_U(q,z)F_V(q,z)-q^{2s}\big). \tag{4}
\]
At the root, the two eight-part parents have no additional incoming root edge. Thus
\[
P_A=H_{UU}H_{VV},\qquad P_B=H_{UV}^2.
\]
Writing \(a=q^{2s}\), \(f=F_U\), \(g=F_V\), expanding the two products yields
\[
\begin{aligned}
H_{UU}H_{VV}-H_{UV}^2
&=az(f^2+g^2-2fg)\\
&\quad+z^2\big[(f^2-a)(g^2-a)-(fg-a)^2\big]\\
&=az(1-z)(f-g)^2,
\end{aligned}
\]
which proves (1) as a polynomial identity, not merely as a numerical equality at a selected probability.

Because \(F_U(q,1)=F_V(q,1)=1\), the difference \(F_U-F_V\) is divisible by \(z-1\). The right side of (1) is therefore divisible by \((z-1)^3\); its first and second derivatives at \(z=1\) vanish. Its third derivative there is \(-6q^{2s}(\mu_U-\mu_V)^2\). Equality of the first two factorial moments implies equality of first two raw moments and variances, while equality of these lower moments makes the third derivative equal to the third raw-moment difference. This proves (2).

For the explicit trees, direct recursive use of (4), starting from the incoming-edge leaf polynomial \(F_L=q+(1-q)z\), yields
\[
F_C-F_D=q^2z^2(q-1)(z-1)(qz^2-2qz+q-z^2).
\]
Consequently \(\mu_C-\mu_D=q^2(1-q)\), and substituting \(s=4\) in (2) gives the first identity in (3). Inserting the displayed difference in (1) and extracting the \(z^5\) coefficient yields \(q^{14}(1-q)^2\). The latter is positive on \((0,1)\), proving strict full-law separation throughout that range. The trees are nonisomorphic because the two root children of \(A\) are respectively isomorphic paired caterpillars and balanced pairs, while both root children of \(B\) have a mixed pair.

## Verification and limitations

The assigned scientific package's `checker.py` independently verifies the bivariate probability generating polynomial factorization using sparse integer polynomials in \(q,z\), and it directly enumerates all \(65,536\) leaf-survival subsets at \(q=1/2\). Its reported score-five count difference and third-moment gap agree with (3). These finite checks support the explicit example; the general identity (1) follows from the algebraic argument above for **every** eligible pair \(U,V\).

The published prior two-moment rarefaction theorem is stronger than any claim here to discover the first collision; this note claims neither that threshold nor its uniqueness as new. Exact full-distribution swap factorization is a narrower, independently motivated structural identity, useful for distinguishing moment-equivalent constructions and calculating higher-order differences. A similar factorization might exist in unindexed generating-function literature; historical priority is best-of-knowledge only. The small probability difference in the example is not an empirical detectability claim.

## Related work and attribution

- *Sixteen leaves are the sharp threshold for two-moment phylogenetic-rarefaction ambiguity*, published October 18, 2026, https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-sixteen-leaves-are-the-sharp-threshold-for-two-moment-phylogenet--462f3e638fdc. Establishes the unique sixteen-leaf collision and every lower-size noncollision for complete fixed-size mean/variance profiles. The conditional-binomial transform transfers these statements to the homogeneous extinction model; this is decisive prior coverage.
- *Sixteen taxa are sharp for two-moment phylogenetic-rarefaction ambiguity*, published October 26, 2026, https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-sixteen-taxa-are-sharp-for-two-moment-phylogenetic-rarefaction-a--8c5fc1eb40b1. Gives the same pair, higher-moment witness, and an equal-subtree interchange argument.
- B. Faller, F. Pardi and M. Steel, *Distribution of phylogenetic diversity under random extinction*, arXiv:0708.0425; J. Theor. Biol. 251 (2008), 286–296. Establishes the independent-extinction model and distribution recursion.
- D. A. Nipperess and F. A. Matsen IV, *The mean and variance of phylogenetic diversity under rarefaction*, Methods Ecol. Evol. 4 (2013), 566–572, DOI:10.1111/2041-210X.12042. Establishes the fixed-size moment framework used in the prior sharp classification.
