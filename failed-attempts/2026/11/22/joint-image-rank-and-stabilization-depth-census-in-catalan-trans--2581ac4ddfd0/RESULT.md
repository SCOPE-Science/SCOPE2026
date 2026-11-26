# Joint image-rank and stabilization-depth census in Catalan transformation monoids

## Finding
For every integer \(n\ge1\), let \(\mathcal C_n\) be the Catalan transformation monoid of weakly increasing maps \(f:[n]\to[n]\) such that \(f(i)\le i\). Define \(r(f)=|\operatorname{im} f|\) and \(d(f)=\min\{h\ge0:f^{h+1}=f^h\}\), with \(f^0\) the identity. The **entire joint rank–stabilization-depth census** has a finite rational recurrence. Treat \(x\) and \(u\) as formal variables, and define
\[
T_0=x,\qquad T_h=x\left(1+\frac{uT_{h-1}}{1-T_{h-1}}\right)\quad(h\ge1),
\]
\[
F_0=\frac1{1-ux},\qquad F_h=\left(1-\frac{ux}{1-T_{h-1}}\right)^{-1}\quad(h\ge1).
\]
For every \(h\ge0\), \(n\ge1\), and \(1\le r\le n\),
\[
[x^nu^r]F_h=\#\{f\in\mathcal C_n:r(f)=r,\ d(f)\le h\}.
\]
Thus exact depth \(h\ge1\) is counted by \([x^nu^r](F_h-F_{h-1})\), while depth zero is counted by \([x^nu^r]F_0\). In addition, \(d(f)\le r(f)\). For every \(n\ge2\) and \(1\le r\le n-1\), the **sharp rank–depth boundary** has the closed form
\[
\#\{f\in\mathcal C_n:r(f)=d(f)=r\}=\binom{n+r-3}{2r-2}>0.
\]
The unique rank-\(n\) transformation is the identity, with depth zero. The formula captures the joint invariant, rather than either of its previously studied marginals.

## Assumptions and scope
All transformations are **full** functions on the labelled chain \([n]=\{1,\ldots,n\}\), and multiplication is composition. Rank means image cardinality, not generating rank of the semigroup. Because maps are regressive, each forward orbit reaches a fixed point and the stabilization index \(d(f)\) is well defined, including \(d=0\) for the identity. The coefficient identities are identities of formal power series over \(\mathbb Z\); for any given \(n\), only finitely many arithmetic operations are needed by truncating the series at degree \(n\) in \(x\). There are no probability, large-\(n\), or field-size hypotheses.

## Proof
**1. Canonical breadth-first plane-forest bijection.** Every fixed point of \(f\) is the first element of a maximal contiguous interval ending before the next fixed point. Indeed, if \(i\) lies strictly between successive fixed points \(a<b\), monotonicity gives \(a=f(a)\le f(i)\le f(b)=b\), and regressivity forces \(f(i)<b\); the absence of another fixed point and monotonicity force \(f(i)<i\). For the last block the same argument holds. Draw the edge from each nonfixed \(i\) to its parent \(f(i)\). Parent labels are weakly increasing as child labels increase; consequently the children of each vertex form a consecutive block in breadth-first order. Conversely, breadth-first labelling of an ordered forest of plane rooted trees, with each root sent to itself and each other vertex sent to its parent, gives exactly such a map. This is a bijection preserving vertex number.

**2. Translation of the invariants.** In each component the iterates traverse parent edges until reaching the fixed root. Hence \(d(f)\) is the maximum component-tree height (number of edges on a longest root-to-leaf path). A nonroot vertex belongs to \(\operatorname{im}f\) if and only if it has at least one child, and every root belongs to \(\operatorname{im}f\) by being fixed. Thus rank equals the total number of component roots **plus** the number of nonroot internal vertices. In particular, the rank is exactly the number of vertices on any deepest root-to-leaf path except its terminal leaf, together with all other contributing vertices; hence \(d(f)\le r(f)\).

**3. Rational series.** Give every vertex weight \(x\) and each nonleaf vertex in an ordinary child-subtree an additional weight \(u\). A height-zero tree contributes \(T_0=x\). A tree of height at most \(h\ge1\) is either a leaf of weight \(x\), or a root with a nonempty ordered sequence of height-at-most-\(h-1\) child trees, giving \(xuT_{h-1}/(1-T_{h-1})\). This proves the recurrence for \(T_h\). A component root is always weighted \(u\), including when it is a singleton, since it is fixed and in the image; a height-at-most-\(h\) component has weight \(ux/(1-T_{h-1})\) when \(h\ge1\), and \(ux\) at height zero. An ordered forest is an arbitrary sequence of these components, proving the stated series \(F_h\). By step 2, its coefficient of \(x^nu^r\) counts exactly the claimed joint stratum.

**4. Sharp boundary.** If a map has depth \(r\) and rank \(r\), a maximal-depth root-to-leaf path already uses all \(r\) image vertices (its first \(r\) vertices). Therefore there is exactly one component and all other vertices are leaves attached to vertices of that path. The \(r\) nonterminal vertices comprise a single spine with \(r-1\) obligatory continuation edges; each of the first \(r-1\) spine vertices can support an arbitrary ordered sequence of leaves on either side of the continuation, while the last internal vertex must have a **nonempty** sequence of terminal leaves. The generating function by total number of vertices is therefore
\[
\frac{x^{r+1}}{(1-x)^{2r-1}},
\]
whose \(x^n\) coefficient equals \(\binom{n+r-3}{2r-2}\). It is strictly positive for \(n\ge r+1\), proving sharpness of \(d\le r\). The only rank-\(n\) map is the identity because an increasing regressive surjection of \([n]\) is the identity, completing the boundary cases.

## Verification
The separately implemented integer-arithmetic \(\texttt{verify.py}\) enumerates **every** nondecreasing regressive map of \([n]\) for \(1\le n\le9\), computes its image rank directly from the value set, and computes its depth by following every point to its fixed point. A separate truncated bivariate-polynomial implementation of the rational recurrence matches **every** rank-and-exact-depth coefficient. It independently checks the boundary binomial formula for every admissible rank. The run covers \(6917\) transformations and ends with \(\texttt{VERIFY\_OK}\). Finite tests are regression evidence only: the proof of the all-\(n\) result is the bijection and the symbolic generating-function argument above. Run \(\texttt{python3 verify.py}\) with Python's standard library; the embedded \(\texttt{check_output.txt}\) contains the captured output.

## Relationship to prior work
Ganyushkin and Mazorchuk [1] establish the Catalan-transformation realization of a type-A Hecke–Kiselman quotient, as well as classical idempotent properties. Yağcı and Korkmaz [2] count elements by exact stabilization depth, including at prescribed fixed-point sets. Ayık, Ayık and Koç [3] give earlier fixed-point enumerations; rank and Catalan/Narayana counting are classical. The breadth-first plane-forest representation also appears in the published 2026 image-rank asymptotic analysis [4], which proves that the image rank of the \(k\)-th power, normalized by \(n\), approaches \(1/(k+1)\) for fixed \(k\). Konieczny and Korkmaz [5] use a related forest model for centralizers. Sönmez and Ünlü [6] explicitly associate potency bounds in the wider order-preserving transformation semigroup with ordered-tree depth and derive unweighted counting functions. Laradji and Umar [7] enumerate fixed image-rank strata of the decreasing, order-preserving semigroup. Neither paper has been confirmed to supply the combined rank–depth refinement; the abstract available for [6] lists univariate potency counts, and [7] addresses rank strata independently. None of the closely inspected full texts states the **joint exact coefficient law of image rank of the original map and its stopping depth**, or the sharp rank-equals-depth multiplicity. In particular, potency counts marginalize over image rank, and power-rank asymptotics do not specify the joint finite-size law. The forest representation, single-parameter marginals and standard tree-sequence generating functions are **not** asserted to be new. The novelty claim is limited to the combined rank–depth census and its sharp extremal coefficient, subject to the residual possibility of an equivalent unindexed weighted-forest enumeration.

## Limitations
The formulas are finite rational recurrences, not a closed single-binomial formula for every interior joint coefficient. The sharp closed formula concerns the boundary \(d=r\). The result does not determine the full joint ranks of *all* iterates, nor any asymptotic fluctuations. Independently confirming historical priority would require full-text inspection of [6] and [7] and a wider manual search of older semigroup-enumeration publications; neither the inaccessible text nor an abstract alone proves absence of overlap. No independent audit has occurred.

## References
[1] O. Ganyushkin and V. Mazorchuk, “On Kiselman quotients of 0-Hecke monoids,” arXiv:1006.0316, first public June 2, 2010; *International Electronic Journal of Algebra* 10 (2011), 174–191. https://arxiv.org/abs/1006.0316

[2] M. Yağcı and E. Korkmaz, “On Elements of Finite Semigroups of Order-Preserving and Decreasing Transformations,” *Bulletin of the Malaysian Mathematical Sciences Society* 43 (2020), 3863–3870, DOI:10.1007/s40840-020-00899-7. https://doi.org/10.1007/s40840-020-00899-7

[3] G. Ayık, H. Ayık and M. Koç, “Combinatorial results for order-preserving and order-decreasing transformations,” *Turkish Journal of Mathematics* 35 (2011), 617–625, DOI:10.3906/mat-1010-432. https://doi.org/10.3906/mat-1010-432

[4] “A harmonic power-rank law for uniformly random Catalan transformations” (2026), public research record: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-harmonic-power-rank-law-for-uniformly-random-catalan-transform--26a48beb2bce

[5] J. Konieczny and E. Korkmaz, “Centralizers in Catalan Monoids,” arXiv:2611.21071 (November 2026). https://arxiv.org/abs/2611.21071

[6] O. Sönmez and Y. Ünlü, “m-Potent Elements in Order-Preserving Transformation Semigroups and Ordered Trees,” *Communications in Algebra* 42 (2014), 332–342, DOI:10.1080/00927872.2012.716115. https://doi.org/10.1080/00927872.2012.716115

[7] A. Laradji and A. Umar, “On Certain Finite Semigroups of Order-decreasing Transformations I,” *Semigroup Forum* 69 (2004), 184–200, DOI:10.1007/s00233-004-0101-9. https://doi.org/10.1007/s00233-004-0101-9
