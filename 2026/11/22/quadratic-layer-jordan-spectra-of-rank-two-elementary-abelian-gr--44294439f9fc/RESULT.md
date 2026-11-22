# Quadratic-layer Jordan spectra of rank-two elementary-abelian group algebras in odd characteristic

## Finding

Let \(p\geq5\) be prime, \(q=p^e\) with \(e\geq1\), and let \(E=C_p\times C_p\). For the group algebra
\[
 A=\mathbb F_q[E]\cong\mathbb F_q[x,y]/(x^p,y^p),\qquad \mathfrak m=(x,y),
\]
this result determines the entire Jordan-block distribution of regular multiplication \(L_f:A\to A\) as \(f\) ranges over the **first nonlinear radical layer** \(\mathfrak m^2\setminus\mathfrak m^3\), over every finite extension of the prime field.

For a nonzero quadratic symbol \(Q=ax^2+bxy+cy^2\), define \(\Delta=b^2-4ac\). The two possibilities are as follows.

**Nondegenerate symbol:** If \(\Delta\neq0\), the Jordan partition is
\[
 \lambda_{\mathrm{nd}}=(p,\,(p-1)^2,\,(p-2)^2,\ldots,2^2,1^2),
\]
where \(j^2\) denotes two Jordan blocks of size \(j\). Its multiplicity is
\[
 (q^3-q^2)q^{p^2-6}.
\]
In this stratum \(\operatorname{rank}(L_f^t)=(p-t)^2\) for each \(0\le t\le p\).

**Rank-one symbol:** If \(\Delta=0\) and \(Q\neq0\), there is a well-defined integer \(s\in\{3,4,\ldots,p\}\), called the *transverse residual order*, computed by the normalization in the proof. For \(s<p\), let
\[
 a_0=\left\lceil\frac p2\right\rceil,\quad a_1=\left\lfloor\frac p2\right\rfloor,\quad
 b_j=\left\lfloor\frac{p-1-j}{s}\right\rfloor+1\quad(0\le j<s).
\]
Then the Jordan partition \(\lambda_{p,s}\) is the multiset, with multiplicities,
\[
 \lambda_{p,s}=\bigsqcup_{i=0}^{1}\ \bigsqcup_{j=0}^{s-1}
 \{a_i+b_j-2r+1:1\le r\le\min(a_i,b_j)\}.
\]
For \(s=p\) the same rule applies with \(b_j=1\) for \(0\le j<p\). Exact numbers of elements in these residual strata are
\[
 \#\{f:s(f)=s\}=
 \begin{cases}
 (q^2-1)(q-1)q^{p^2-s-4},&3\le s<p,\\
 (q^2-1)q^{p^2-p-3},&s=p.
 \end{cases}
\]
The rank-one and nondegenerate contributions sum to
\[
 (q^3-1)q^{p^2-6}=\#(\mathfrak m^2\setminus\mathfrak m^3).
\]
If two values of \(s\) ever yield an equal partition, their displayed counts must be added; no distinctness of these partitions is required for the complete distribution.

For example, in characteristic five the nondegenerate type is \((5,4^2,3^2,2^2,1^2)\). The three rank-one residual normal forms are \(x^2+y^3\), \(x^2+y^4\), and \(x^2\), with their partitions obtained by the uniform rule above. The theorem includes higher-order perturbations of every quadratic symbol, not merely homogeneous elements.

## Assumptions and scope

The rings are the regular representations of elementary-abelian groups of rank two, in their defining odd characteristic \(p\ge5\). They have vector-space dimension \(p^2\); \(\dim\mathfrak m^2=p^2-3\), \(\dim\mathfrak m^3=p^2-6\). The element \(f\) has zero constant and linear coefficients, and its quadratic coefficient triple is nonzero. Characteristic three is omitted because its complete Jordan census is already published. The field size may be any \(p^e\).

The residual order \(s\) is an invariant of the rank-one quadratic singularity under automorphisms tangent to the identity that fix the chosen quadratic normal direction. Scaling \(f\) by a nonzero scalar and passing to an extension field do not alter its Jordan partition. The proof provides the normal-form construction and the counting fibers, so no external classification of formal singularities is needed.

## Proof

**Step 1: filtered coordinate changes.** Every element of \(\mathfrak m\) has \(p\)-th power zero by Frobenius and the relations \(x^p=y^p=0\). Thus any assignments \(x\mapsto X\in\mathfrak m\), \(y\mapsto Y\in\mathfrak m\) extend to an algebra homomorphism. If their linear terms form an invertible two-by-two matrix, the associated graded map is surjective, hence the homomorphism is an automorphism of this finite filtered algebra. Conjugation by an algebra automorphism carries multiplication by \(f\) to multiplication by its transformed image, preserving the complete Jordan partition. Because \(f^p=0\), only blocks of length at most \(p\) occur.

**Step 2: quadratic symbol of rank two.** Work temporarily over an algebraic closure. When \(\Delta\neq0\), the nondegenerate binary quadratic \(Q\) becomes a nonzero scalar multiple of \(xy\) under an invertible linear change of variables. All higher homogeneous terms can be removed inductively: if the first unwanted term has degree \(d\ge3\), write it as \(xU+yV\) with \(U,V\) homogeneous of degree \(d-1\). The changes \(y\mapsto y-U\), \(x\mapsto x-V\) remove that term in \(xy\), without affecting lower degrees. Iterate to degree \(2p-2\), the largest nonzero degree. Each substitution is a filtered automorphism. Consequently \(f\) is equivalent over an extension to \(xy\), up to nonzero scalar. Multiplication by \((xy)^t\) has image basis \(\{x^iy^j:t\le i,j<p\}\), of dimension \((p-t)^2\). Taking second differences of these power ranks gives one length-\(p\) block and exactly two blocks of each length \(1,\ldots,p-1\). Extension of scalars does not change the ranks of matrices over \(\mathbb F_q\), so the conclusion holds over the original field.

**Step 3: rank-one quadratic normal form and uniformity of the residual coefficients.** Every nonzero rank-one binary quadratic over \(\mathbb F_q\) is \(a\ell^2\), where \(a\neq0\) and \(\ell\) is a linear form; apply a linear automorphism and divide the element by \(a\), so its degree-two part becomes \(x^2\). Inductively suppose the first remaining term containing \(x\) has total degree \(d\ge3\), say \(xH_d(x,y)\), with \(H_d\) homogeneous of degree \(d-1\). Since \(2\) is invertible, substituting \(x\mapsto x-H_d/2\) kills that degree-\(d\) x-divisible term. Repeating through degree \(2p-2\) yields
\[
 x^2+h(y),\qquad h(y)=\sum_{j=3}^{p-1}h_jy^j.
\]
The algorithm is triangular by degree and fixes \(y\). For fixed x-containing input coefficients, each resulting \(h_j\) equals the input pure-y coefficient of degree \(j\) plus a function of earlier coefficients and of the fixed x-containing coefficients. Hence the map on the \(p-3\) pure-y input coefficients is a bijective affine triangular map. The residual polynomial \(h\) is therefore uniformly distributed among the \(q^{p-3}\) possibilities when the higher coefficients of \(f\) vary.

For \(h\neq0\), define \(s=\operatorname{ord}_y h\), necessarily \(3\le s<p\); for \(h=0\), define \(s=p\). This order is unchanged by further transverse changes preserving the split normal form, so it defines an invariant. For a given \(s<p\), precisely \((q-1)q^{p-1-s}\) residual polynomials have that order; the zero residual polynomial occurs once. The map from higher coefficients (dimension \(p^2-6\)) to residual coefficients (dimension \(p-3\)) has constant fibers of cardinality \(q^{p^2-p-3}\).

If \(s<p\), write \(h(y)=c y^s u(y)\) with \(c\neq0\) and \(u(0)=1\). Because \(s<p\), a unique formal truncated \(s\)-th root of \(u(y)\) exists: the recursion at degree \(j\) divides by \(s\), which is invertible in the field. Replacing \(y\) by \(y\,u(y)^{1/s}\) reduces \(h\) to \(c y^s\). After a harmless finite field extension to take an \(s\)-th root of \(c\), this is equivalent to \(y^s\). For \(h=0\) it is equivalent to zero. The Jordan type is thus exactly that of multiplication by \(x^2+y^s\), with the convention \(y^p=0\). The constant-fiber argument proves the multiplicity formulas for each \(s\) after multiplying by the count of nonzero rank-one quadratic symbols.

**Step 4: tensor-sum Jordan decomposition.** Multiplication by \(x^2\) on \(k[x]/(x^p)\) has chains on the even and odd exponent classes, of respective lengths \(a_0=\lceil p/2\rceil\) and \(a_1=\lfloor p/2\rfloor\). Similarly, multiplication by \(y^s\) on \(k[y]/(y^p)\) has \(s\) chains on congruence classes modulo \(s\), with lengths \(b_j=\lfloor(p-1-j)/s\rfloor+1\). The operator \(L_{x^2+y^s}\) is the tensor sum of these two nilpotent operators. On a tensor product of chains of lengths \(a,b\), the classical Jordan tensor-sum rule yields
\[
 (a+b-1,\ a+b-3,\ldots,|a-b|+1),
\]
provided \(a+b-1<p\). For clarity, the rule follows from the standard multiplication-by-\(u+v\) decomposition of \(k[u,v]/(u^a,v^b)\): its successive maximal minors have binomial determinant factors, none divisible by \(p\) when \(a+b-1<p\), so the characteristic-zero chain decomposition survives reduction modulo \(p\). Here \(a\le\lceil p/2\rceil\), \(b\le\lceil p/3\rceil\), and for odd prime \(p\ge5\), \(\lceil p/2\rceil+\lceil p/3\rceil-1<p\). The displayed multiset \(\lambda_{p,s}\) follows, including \(s=p\) (all \(b_j=1\)).

**Step 5: quadratic symbol counts and exhaustive partition.** The discriminant-zero quadratic cone \(b^2=4ac\) has \(q^2\) coefficient triples: for \(a\neq0\), \(a,b\) freely determine \(c\), and for \(a=0\), necessarily \(b=0\) and \(c\) is arbitrary. Removing the vertex leaves \(q^2-1\) rank-one symbols; the nondegenerate complement has \(q^3-q^2\) symbols. Every fixed symbol admits \(q^{p^2-6}\) higher-coefficient completions. The rank-one fiber count from Step 3 sums to \((q^2-1)q^{p^2-6}\); adding the nondegenerate contribution gives exactly \((q^3-1)q^{p^2-6}\), the full quadratic-leading layer. This proves every claimed Jordan type and each exact frequency.

## Verification

The standalone Python checker `checks/jordan_quadratic_checker.py` performs direct multiplication in the truncated polynomial ring and exact Gaussian elimination, then derives Jordan partitions from ranks of the powers rather than using the tensor-sum formula. It exhaustively tests the quadratic-leading elements in characteristic three as a comparison with a known adjacent case, and tests nondegenerate and rank-one perturbations in characteristics five and seven, including all monomial normal forms for each possible residual order. These finite checks passed. The general theorem for every \(p\ge5\) and all finite field extensions rests on the algebraic proof, not on finite enumeration.

Run `python3 checks/jordan_quadratic_checker.py` using the standard library; it prints `ALL EXACT CHECKS PASS` when its checks succeed.

## Relationship to prior work

Carlson, Friedlander and Pevtsova [1] established the modular representation-theoretic setting of Jordan types for \(C_p\times C_p\), with emphasis on restrictions along \(\pi\)-points (nonzero first-order directions). Those statements imply the standard free Jordan partition for the nonzero-linear layer of the regular module, but do not count the nonlinear layer \(\mathfrak m^2\setminus\mathfrak m^3\). Öztürk Kaptanoğlu [2] likewise works with first-order radical elements to analyze Jordan types, not the present singular quadratic symbols. Altafi, Iarrobino and Khatami [3] classify multiplication by *linear* forms in homogeneous codimension-two complete intersections under characteristic-zero or sufficiently-large-characteristic hypotheses, which do not cover these nonlinear modular multipliers.

Two previously published exact censuses [4,5] completely treat the exceptional exponent-three algebra \(\mathbb F_q[C_3\times C_3]\). Their quadratic discriminant stratification is a direct adjacent precedent and is not reclaimed here. Unlike those finite p-three results, this theorem establishes every prime \(p\ge5\), with transverse residual orders \(3,\ldots,p\), the corresponding full modular Jordan partitions, and exact finite-field counts. Previously published exponent-three truncated CI results in large characteristic [6] concern a different quotient and do not imply this family. Standard formal splitting and short-chain Jordan sums are used as proof techniques, not claimed as new. No claim of exhaustive historical priority is made.

## Limitations

The theorem deliberately excludes characteristic three, the zero-quadratic layer \(\mathfrak m^3\), elements with a nonzero linear part, nonregular modules, and groups with more than two generators. It gives ranks/Jordan types, not conjugacy classifications of elements or group units. The residual-order strata can combine if identical partitions occur. Full-text literature comparison cannot rule out an earlier equivalent statement in less directly indexed modular representation or singularity theory. The self-review is not independent mathematical validation.

## References

[1] J. F. Carlson, E. M. Friedlander, J. Pevtsova, *Modules of constant Jordan type*, arXiv:0707.3845, first public 2007-07-25. https://arxiv.org/abs/0707.3845

[2] S. Öztürk Kaptanoğlu, *Jordan type of a \(k[C_p\times C_p]\)-module*, New York J. Math. 17a (2011), 307–313. https://nyjm.albany.edu/j/2011/17a-18v.pdf

[3] N. Altafi, A. Iarrobino, L. Khatami, *Complete intersection Jordan types in height two*, arXiv:1810.00716, first public 2018-10-01. https://arxiv.org/abs/1810.00716

[4] *Characteristic-three Jordan strata of the two-generator elementary-abelian group algebra* (published mathematical result, 2026-10-18). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-characteristic-three-jordan-strata-of-the-two-generator-elementa--0d5279498d55

[5] *Jordan strata and cyclic-subgroup census for the modular group algebra of \(C_3\times C_3\)* (published mathematical result, 2026-11-02). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-jordan-strata-and-cyclic-subgroup-census-for-the-modular-group-a--10caf113e43b

[6] *Complete finite-field Jordan spectra in the cubic-by-cubic monomial complete intersection* (published mathematical result, 2026-10-26). https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-complete-finite-field-jordan-spectra-in-the-cubic-by-cubic-monom--74c030e7b6dc
