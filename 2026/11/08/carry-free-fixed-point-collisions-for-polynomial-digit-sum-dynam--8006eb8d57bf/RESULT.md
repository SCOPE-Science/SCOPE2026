# Carry-free fixed-point collisions for polynomial digit-sum dynamics

## Finding
Let \(g\in\mathbb Z_{\ge0}[X]\) be any polynomial of degree at least two. For every integer \(a\ge2\), define the integer base
\[
 b=g(a)-a+1.
\]
Then the digit-sum polynomial map \(T_{b,g}(n)=s_b(g(n))\) has two distinct fixed points \(a\) and \(g(a)\), separated by exactly \(b-1\). Consequently, the projection of cycles onto the reduction \(n\mapsto g(n)\pmod{b-1}\) is noninjective, and the two corresponding basins cannot both be unions of residue classes modulo \(b-1\). Every fixed polynomial in the stated class therefore has infinitely many distinct bases displaying this failure.

More quantitatively, for the square map \(T_b(n)=s_b(n^2)\), failure occurs at **every** base \(b\ge7\) with \(b\equiv7\pmod9\), and at **every** base \(b\ge13\) with \(b\equiv4\pmod9\). In particular, among bases up to \(B\), the lower asymptotic proportion having noninjective cycle projection is at least \(2/9\):
\[
\liminf_{B\to\infty}\frac{1}{B}
\#\{2\le b\le B:\gamma_b\text{ is noninjective for }T_b\}\ \ge\ \frac29.
\]
This is a lower-density assertion, not a determination of the density of all exceptional bases.

## Assumptions and scope
For integer \(b\ge2\), \(s_b(N)\) denotes the sum of the digits in the ordinary base-\(b\) expansion of positive integer \(N\). All maps act on positive integers. The polynomial \(g\) has **nonnegative integer coefficients** and degree \(d\ge2\), with nonzero leading coefficient; constant and linear terms are allowed. The explicit infinite-base claim varies \(b\), while fixing \(g\). The square-map positive-density claim varies only \(b\), with \(g(X)=X^2\) fixed. The induced cycle projection \(\gamma_b\) uses ordinary reduction modulo \(b-1\) and the reduced map \(x\mapsto g(x)\bmod(b-1)\).

## Proof
**1. A carry-free polynomial lemma.** Fix \(g(X)=\sum_{i=0}^d u_iX^i\), \(u_i\ge0\), \(u_d\ge1\), and \(a\ge2\). Expand
\[
 g(Y+a-1)=\sum_{j=0}^d c_jY^j,\qquad
 c_j=\sum_{i=j}^d u_i\binom ij(a-1)^{i-j}.
\]
All \(c_j\) are nonnegative integers, and \(\sum_jc_j=g(a)\). In fact,
\[
 0\le c_j\le g(a)-a\qquad(0\le j\le d).
\]
To prove this, the leading monomial \(X^d\) already contributes at least \(a\) to the *sum of all coefficients other than the coefficient indexed by* \(j\). For \(j=0\), its coefficient of \(Y\) is \(d(a-1)^{d-1}\ge a\). For \(1\le j<d\), its constant and degree-\(d\) coefficients sum to \((a-1)^d+1\ge a\). For \(j=d\), its constant and degree-one coefficients sum to \((a-1)^d+d(a-1)^{d-1}\ge a\). Multiplication by \(u_d\ge1\) and the other nonnegative monomials cannot decrease this complement. This proves the bound.

Put \(b=g(a)-a+1\). Since \(g(a)\ge a^2\), one has \(b\ge a^2-a+1\ge3\), and \(a-1<b\). Thus \(g(a)=b+(a-1)\) is its genuine two-digit base-\(b\) expansion and
\[
 T_{b,g}(a)=s_b(g(a))=1+(a-1)=a.
\]
Substitute \(Y=b\) in the carry-free expansion: \(g(g(a))=g(b+a-1)=\sum_jc_jb^j\), with \(0\le c_j\le b-1\). These are genuine base-\(b\) digits, so
\[
 T_{b,g}(g(a))=s_b(g(g(a)))=\sum_jc_j=g(a).
\]
The two fixed points are distinct because \(g(a)>a\), and their difference is \(b-1\). They therefore project to the same fixed residue. Their disjoint basins both meet that residue class, so neither a partition into residue-class basins nor injectivity of the cycle projection is possible. For fixed \(g\), \(g(a+1)>g(a)+1\) for all \(a\ge2\) (the degree-at-least-two monomial suffices), so the constructed bases are distinct and unbounded.

**2. A positive-density square-map subfamily.** For each \(j\ge0\), put \(b=9j+7\), \(a=3j+3\), and \(c=12j+9\). Then \(c-a=b-1\), and exact expansions are
\[
 a^2=(j+1)b+(2j+2),\qquad
 c^2=b^2+(7j+4)b+(5j+4).
\]
All displayed coefficients lie in \(\{0,\ldots,b-1\}\); their respective sums are \(a\) and \(c\). Hence \(a,c\) are distinct fixed points of \(T_b\).

For each \(j\ge1\), put \(b=9j+4\), \(a=6j+3\), and \(c=15j+6\). Again \(c-a=b-1\), and
\[
 a^2=(4j+2)b+(2j+1),\qquad
 c^2=2b^2+(7j)b+(8j+4).
\]
All coefficients are base-\(b\) digits, including \(8j+4<b\) precisely because \(j\ge1\). Their sums are \(a\) and \(c\). Hence every base in both indicated arithmetic progressions has noninjective cycle projection. Those two disjoint residue classes have combined asymptotic density \(2/9\) among positive integers \(b\), which proves the lower-density bound.

## Verification
The included standalone `verify.py` uses exact integer arithmetic and the standard library. It verifies the polynomial carry-free identities and both fixed points across 11,880 polynomial/base examples, checks 3,999 examples in the two square-base progressions, and separately compares a two-lift residue criterion to direct digit sums for 124,251 smaller cases. Execute `python3 verify.py` from the extracted package directory. These finite diagnostics are consistency checks; the arbitrary-polynomial and asymptotic-base assertions are proved in the preceding algebraic argument.

## Relationship to prior work
The 2026 work *Digit-Sum Maps of Polynomial Generators over Arbitrary Bases: Global Descent, Cycle Localization and Arithmetic Basins* establishes global finite cycle localization and a semiconjugacy modulo \(b-1\). It supplies a finite table of injectivity behavior for \(2\le b\le16\) and \(2\le k\le5\), together with specific noninjective examples. It does not state an all-polynomial carry-free collision construction or a positive lower density of failing bases for the square map. Its general finite-search theorem can settle any particular base, but it does not by itself imply the uniform base families or their arithmetic-progression density.

Koppelaar and Nasehpour's *On Hardy's Apology Numbers* establishes finiteness of generalized Dudeney fixed points for fixed bases under growth hypotheses. Its fixed-base finiteness statement is consistent with, but does not imply, the varying-base collision families here. The earlier decimal-only cycle study likewise does not cover the varying-base theorem. No novelty is claimed for the fundamental digit-sum congruence or the binomial theorem.

## Limitations
Nonnegative polynomial coefficients are essential to the simple carry-free argument; no assertion is made for arbitrary signed-coefficient polynomials. A lower asymptotic proportion of \(2/9\) does not imply the total exceptional-base density exists or equals that value, and no density for an individual split basin is claimed. The construction provides at least two coincident projected fixed cycles, not a full classification of all cycles in those bases. The mathematical proof and source comparisons have not been independently audited; the historical-priority search may miss unindexed literature or equivalent constructions.

## References
1. M. V. P. Alcântara, *Digit-Sum Maps of Polynomial Generators over Arbitrary Bases: Global Descent, Cycle Localization and Arithmetic Basins*, first public version July 13, 2026, Zenodo record 21348127, DOI 10.5281/zenodo.21348127. Relevant complete source text in version 2, DOI 10.5281/zenodo.21435937, `digit_sum_maps_journal.tex`.
2. H. Koppelaar and P. Nasehpour, *On Hardy's Apology Numbers*, *Journal of Algorithms and Computation* 52(2) (2020), 67-83, arXiv:2008.08187, especially Section 5.
3. M. V. P. Alcântara, *Digit-Sum Power Maps: A Critical Survey of Cycles, Fixed Points and Arithmetic Dynamics*, Zenodo record 21436434 (2026), introductory survey and bibliography.
4. M. A. C. Alcântara and M. V. P. Alcântara, *Dynamics of the Digit Sum of Integer Powers: Cycle Structure and Finite Search*, first public version March 26, 2026, Zenodo record 19240837, decimal-map study.
