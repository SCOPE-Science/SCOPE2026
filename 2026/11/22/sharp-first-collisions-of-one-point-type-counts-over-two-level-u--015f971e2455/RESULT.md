# Sharp first collisions of one-point type counts over two-level ultrametric parameter sets

## Finding

Let \(\mathbb U_3\) be the countable universal homogeneous metric space with positive distances \(\{1,2,3\}\). Fix \(n\ge1\) individually named points partitioned into \(k\ge1\) nonempty classes of sizes \(a_1,\ldots,a_k\), with \(n=\sum_i a_i\), such that distinct points have distance \(1\) within each class and distance \(3\) between classes. This is a two-level ultrametric.

Define \(\Theta_A(x,y,z)\) to be the generating polynomial of complete nonalgebraic one-point types, where a monomial has exponents equal to the numbers of named parameters at distances \(1,2,3\), respectively. Then
\[
\boxed{\Theta_A(x,y,z)=(y+z)^n+\sum_{i=1}^{k}\big((x+y)^{a_i}-y^{a_i}\big)(y+z)^{n-a_i}.}
\]
Its unweighted count is
\[
\boxed{N(A)=\Theta_A(1,1,1)=(k+1)2^n-\sum_{i=1}^{k}2^{n-a_i}.}
\]

At fixed \(n\), \(N(A)\) distinguishes every possible unordered class-size partition if and only if \(n\le9\). The **unique first pair** of different partitions with equal count occurs at \(n=10\):
\[
(1,1,1,1,3,3),\quad (2,2,2,2,2),\qquad N=4864.
\]
For every \(n\ge10\), different partitions of \(n\) having the same count exist.

Even when both \(n\) and the number \(k\) of clusters are supplied, the scalar fails eventually: it is injective for every \(n\le15\); at \(n=16\) there are **exactly two** unordered colliding pairs:
\[
\begin{aligned}
(1,3,3,3,3,3)&\longleftrightarrow(2,2,2,2,4,4), & k&=6,&N&=385024,\\
(1,3,4,4,4)&\longleftrightarrow(2,2,2,5,5),&k&=5,&N&=339968.
\end{aligned}
\]
Equal-\(k\) collisions exist for every \(n\ge16\). By contrast, the entire distance-refined polynomial uniquely determines the class-size partition for every \(n\).

## Assumptions and scope

All finite base points are individually named. Nonalgebraic types exclude equality with old points, and every new point has distances in \(\{1,2,3\}\) to named parameters. The ambient language names its finitely many distance predicates. The base metric is exactly \(1\) within classes and \(3\) across classes; singleton classes are allowed. A class-size partition always means the unordered list of positive class sizes, which classifies these bases up to isometry when point labels are forgotten. Comparisons of scalar counts are made at **fixed** \(n\), and the equal-class-number comparison also fixes \(k\).

## Proof

**One-point orbit classification.** The extension property and ultrahomogeneity of \(\mathbb U_3\) identify complete nonalgebraic one-point types over a finite named base with functions \(f:A\to\{1,2,3\}\) satisfying
\[
|f(u)-f(v)|\le d(u,v)\le f(u)+f(v)
\]
for each distinct pair of old points. When the old distance is \(1\), the only excluded pair of new distances is \(\{1,3\}\). When it is \(3\), the only excluded pair is \((1,1)\). Thus, either (i) no old parameter is at new distance \(1\), or (ii) exactly one old class has any members at new distance \(1\), all its values lie in \(\{1,2\}\), with at least one \(1\), and all values on all other classes lie in \(\{2,3\}\). These cases are disjoint and sufficient. Case (i) has polynomial \((y+z)^n\); case (ii) with active class \(i\) contributes \(((x+y)^{a_i}-y^{a_i})(y+z)^{n-a_i}\). This proves the displayed polynomial, including for singleton classes and \(k=1\).

**Scalar and inverse information.** Evaluating at unit weights gives \(N(A)=2^n+\sum_i(2^{a_i}-1)2^{n-a_i}\), equivalent to the scalar formula. At \(y=1,z=0\), let \(B_A(x)=\Theta_A(x,1,0)\). Then
\[
B_A(x)=1+\sum_i\big((1+x)^{a_i}-1\big),\qquad [x^j]B_A(x)=\sum_{s\ge j}m_s\binom sj\quad(j\ge1),
\]
where \(m_s\) is the number of old classes of size \(s\). Starting from the largest \(s\) with a nonzero coefficient and proceeding downward, the equations uniquely recover each \(m_s\):
\[
m_s=[x^s]B_A(x)-\sum_{j>s}m_j\binom js.
\]
The original class sizes, and hence the base isometry type, are therefore fully determined by the refined one-point polynomial.

**Sharp finite cutoffs.** Every unordered class-size partition of \(n\) has a unique nondecreasing positive sequence representation. The attached executable proof certificate `artifacts/verify.py` generates them *exhaustively*, by choosing each successive part to be at least the preceding part and recursing on the remaining sum. It enumerates every partition for \(1\le n\le16\), independently checks the standard partition totals (in particular \(p(10)=42\), \(p(16)=231\)), and groups partitions first by \((n,N)\) and then by \((n,k,N)\). No two different partitions agree in the first grouping for \(n\le9\). Exactly one pair agrees at \(n=10\), the displayed pair. No two distinct partitions agree in the second grouping for \(n\le15\), and at \(n=16\) exactly the two displayed pairs occur. This is a finite exhaustive proof of the minimality, uniqueness and completeness assertions at the finite cutoffs; no extrapolation from partial enumeration is involved. The verifier's independent direct Katětov-map enumeration additionally checks the polynomial formula on 54 small cases, while the general identity is proved above.

**All larger sizes.** If a new class of \(t\ge1\) points is appended to a partition of \(n\), the scalar transforms by
\[
N(a_1,\ldots,a_k,t)=2^tN(a_1,\ldots,a_k)+(2^t-1)2^n.
\]
Thus two same-\(n\) bases with equal scalar counts remain equal after adjoining the same new class, irrespective of whether their initial class numbers agree. Append a class of size \(n-10\) to the ten-point pair for any \(n>10\); for the equal-\(k\) phenomenon, append a class of size \(n-16\) to either sixteen-point pair for \(n>16\). They remain nonisometric because a common positive part cannot make two distinct multisets equal. This proves the asserted persistent failures for all larger sizes.

## Verification

Run `python3 artifacts/verify.py` with Python 3 and no third-party packages. The generator's `partitions` function enumerates each positive integer partition exactly once. The `scalar` and `formula` paths evaluate the derived expressions; `direct` separately checks the Katětov inequalities for all distance vectors over 54 small partition bases. The checker confirms the first collision at \(n=10\), both unique fixed-\(k\) collision pairs at \(n=16\), absence of earlier collisions, and binomial inversion through size sixteen. Exact output is provided in `artifacts/verify_output.txt`. Full verification of the general identity is mathematical, not based on finite testing.

## Relationship to prior work

Conant's 2015 manuscript, *Distance structures for generalized metric spaces* (arXiv:1502.05002), identifies Katětov maps with quantifier-free one-types and proves quantifier-elimination results for Urysohn structures. Those are underlying principles; the work does not provide this cluster-partition counting polynomial or its sharp reconstruction failures.

The published 2026 study *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space* treats **graph metrics with distances \(1\) and \(2\)**, whose only local restriction forbids the \(1/3\) pair across distance-\(1\) old edges. The present bases instead have distances \(1\) and \(3\), introducing the independent cross-class prohibition on two new-distance-\(1\) assignments; the cited formula does not cover the present one-point polynomial. Another published 2026 study, *Distance-aware colour refinement on finite ultrametrics*, gives identification via distance-aware refinement signatures rather than via counts of Katětov extension types, and does not imply the sharp scalar collisions here. Related finite-base type results for selected path/cycle, forest, and equilateral metric bases use different parameter domains. All of these are treated as prior context, not independent proof of priority.

## Limitations

The scalar results are at fixed old base size. Only this two-level family of ultrametric bases is considered; they are viewed as parameter sets in the unrestricted (ordinary metric) \(\mathbb U_3\), not as extensions in the category of ultrametric spaces. The polynomial concerns **one-point** types only, and no all-arity inverse theorem is claimed. The finite cutoff census is exhaustive only through sixteen points, supplemented by the explicit all-larger collision construction. Historical priority is not certified by search, and independent mathematical audit has not been performed.

## References

1. Gabriel Conant, *Distance structures for generalized metric spaces*, arXiv:1502.05002, v1 dated 2015-02-17. https://arxiv.org/abs/1502.05002
2. *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space*, published research record (2026). https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-widom-rowlinson-partition-functions-as-1-type-polynomials-of-the--ec80747a5989/RESULT.md
3. *Distance-aware colour refinement on finite ultrametrics: two rounds suffice and eight points first defeat one*, published research record (2026). https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-distance-aware-colour-refinement-on-finite-ultrametrics-two-roun--4e36345f61be/RESULT.md
