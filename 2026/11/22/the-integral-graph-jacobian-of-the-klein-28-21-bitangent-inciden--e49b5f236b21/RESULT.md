# The integral graph Jacobian of the Klein 28–21 bitangent incidence configuration

## Finding

Let \(C\subset\mathbb P^2_{\mathbb C}\) be Klein's smooth quartic, for example in the cyclic model \(X^3Y+Y^3Z+Z^3X=0\). Use the projectively equivalent symmetric model below for the tabulated equations. Let \(\mathcal B\) be the set of its 28 geometric bitangents and \(\mathcal Q\) the set of the 21 points at which exactly four of those bitangent lines meet. Form the bipartite *Levi graph* \(\Gamma\) with 28 line-vertices, 21 point-vertices, and an edge for containment.

The graph is connected, its line-vertices all have degree three, its point-vertices all have degree four, and its critical group (the degree-zero integral divisor class group of the graph) is
\[
K(\Gamma)\cong(\mathbb Z/2\mathbb Z)^4\oplus\mathbb Z/18\mathbb Z\oplus\mathbb Z/54\mathbb Z\oplus\mathbb Z/108\mathbb Z\oplus(\mathbb Z/756\mathbb Z)^5.
\]
In particular it has order \(2^{18}3^{23}7^5\), exponent \(756\), and minimum generator number \(12\). The Smith normal form of any reduced Laplacian has 36 unit entries and positive nonunits \(2\) (four times), \(18\), \(54\), \(108\), and \(756\) (five times).

There is an explicit incidence-preserving graph isomorphism from \(\Gamma\) to the Levi graph of the 21 classical Klein lines and their 28 ordinary triple points. The latter is **not** the Levi graph using their 21 ordinary quadruple points.

## Assumptions and scope

All configurations and critical groups are over characteristic zero. Work over \(\mathbb Q(e)\), where \(e^2+e+2=0\). The 28 bitangent line triples in Janasz–Pokora–Zieliński [2], Table 2, use the symmetric Klein model
\[
x^4+y^4+z^4+3e(x^2y^2+x^2z^2+y^2z^2)=0,
\]
not the displayed cyclic coordinates. In [2, §3] this is the Klein member of the Ciani pencil with parameter \(\lambda=3e\) satisfying \(\lambda^2+3\lambda+18=0\). The two models are projectively equivalent: they represent the same smooth curve, and adjunction identifies their plane embeddings with the canonical embedding. Such a coordinate change preserves bitangency and incidence, so it is not necessary to apply the change to each line. For the 21 reflection-line triples we use the equations of Gévay–Pokora [4, §2.1], with their parameter \(a=e\). Bauer et al. [1, §4.1] describe the classical reflection arrangement and its singular points. The arithmetic in both lists is exact over the quadratic field or over the integers. The equations and incidence certificates are included in `VERIFY.py` and `INCIDENCE.json`.

For a connected graph \(G\), \(K(G)=\mathbb Z^{|V(G)|-1}/\operatorname{im}L'\) for a reduced Laplacian \(L'\) obtained by deleting the row and column of the same vertex. Here the bipartite graph has 49 vertices and 84 edges; it has cycle rank \(84-49+1=36\). No claim is made about the Jacobian of the original smooth Klein quartic.

## Proof

**Exact enumeration of the two configurations.** Work in \(\mathbb Q[e]/(e^2+e+2)\). Two projective lines with coefficient triples \(u,v\) meet at the projective point represented by the exact cross product \(u\times v\). Normalize each nonzero triple by its first nonzero coordinate. Applying this to all \(\binom{28}{2}=378\) bitangent pairs gives 273 distinct points: 252 points incident to two lines and 21 points incident to four lines. The multiplicity count exhausts all pairs because \(252+21\binom42=378\). The set of four-line points yields an incidence matrix \(B\in\{0,1\}^{28\times21}\) with all row sums equal to 3 and all column sums equal to 4. The entire 21-column incidence list is provided in `INCIDENCE.json`.

Apply the same cross-product enumeration independently to the specified 21 classical Klein lines. Their \(\binom{21}{2}=210\) pairs give 49 distinct points, 28 of multiplicity three and 21 of multiplicity four. These counts exhaust the pairs because \(28\binom32+21\binom42=210\). Every Klein line is incident to four of the 28 triple points. The associated dual Levi graph therefore has 28 degree-three triple-point vertices and 21 degree-four line vertices, and 84 edges. The second incidence list is independently included in `INCIDENCE.json`.

**A labelled isomorphism.** Index the bitangents \(0,\ldots,27\) in the listed equation order, their four-line points \(0,\ldots,20\) in first-pair encounter order, the triple points of the 21-line arrangement lexicographically by their three line indices, and the Klein lines in their displayed equation order. The two explicit permutations in `INCIDENCE.json` respectively send 28 bitangents to triple points and 21 four-line points to Klein lines. For each of the 21 four-line points, its four incident bitangents map bijectively to the four triple points incident to the corresponding Klein line. These 84 exact checks certify the graph isomorphism independently of unproved geometric symmetry assertions.

**Tree count and prime support.** The Laplacian is
\[
L=\begin{pmatrix}3I_{28}&-B\\-B^{\mathsf T}&4I_{21}\end{pmatrix}.
\]
Exact characteristic-polynomial calculation using the enumerated integer incidence gives
\[
\det(tI-L)=t(t-7)(t-3)^7(t^2-7t+9)^8(t^4-14t^3+65t^2-112t+56)^6.
\]
The zero eigenvalue is simple, so the graph is connected. The nonzero eigenvalue product divided by 49 is the number of spanning trees by Kirchhoff's theorem. Evaluating the derivative at zero gives
\[
\tau(\Gamma)=\frac{7\cdot3^7\cdot9^8\cdot56^6}{49}=2^{18}3^{23}7^5.
\]
Thus no primes other than \(2,3,7\) can occur in the critical group.

**Integral elementary divisors.** Delete the last row and column of \(L\), yielding an integral \(48\times48\) matrix. Exact prime-local diagonal elimination at powers of 2, 3, and 7, independently applied to the 21-line triple-point presentation, returns the following valuations of the 48 Smith diagonal entries (multiplicities, including valuation zero):

| prime | valuation spectrum |
|---|---|
| 2 | \(0^{36},1^6,2^6\) |
| 3 | \(0^{40},2^1,3^7\) |
| 7 | \(0^{43},1^5\) |

The precision moduli are respectively \(2^{20}\), \(3^{24}\), and \(7^7\); all pivots have valuation below the precision. Pivot selection of minimal valuation guarantees each pivot divides the remaining entries in the corresponding local principal ideal ring, so unimodular row and column elimination yields the Smith exponents. Combining valuations in nondecreasing order and using the established prime support gives precisely 36 units and the twelve nonunit invariant factors listed above. Direct exact-integer Smith normal form, independently calculated from each of the two incidence constructions, agrees. The quotient modulo twice the group is a 12-dimensional binary vector space, so the twelve displayed cyclic factors also give a minimum generating set.

## Verification

`VERIFY.py` rebuilds both configurations from their coefficient triples (in the coordinate systems of the cited tables); normalizes every projective pairwise intersection; checks all intersection multiplicities; compares their incidence graphs by a complete 49-vertex labelled bijection; verifies the Laplacian characteristic polynomial; calculates two Smith normal forms; and also runs a prime-local elimination without a library Smith call. It checks incidence and the integer calculations, not the projective equivalence of Klein models. To reproduce, place `VERIFY.py` and `INCIDENCE.json` together and run `python VERIFY.py` with Python and SymPy. Expected terminal line: `KLEIN_BITANGENT_LEVI_SMITH_AND_LOCAL_CERTIFICATE_OK`. All arithmetic is exact, including the number-field and modular computations.

## Relationship to prior work

The geometric configuration and its 28 bitangents are classical. Bauer et al. (2014) give the 21-line arrangement and its 28 triple and 21 quadruple points. Jeurissen–van Os–Steenbrink (1994) describe the Klein bitangents and a self-dual 21-and-28-element configuration. Janasz–Pokora–Zieliński (2023) explicitly list the 28 bitangents and their 21 quadruple crossings. The current exact graph Jacobian is an *integral refinement* of that known incidence geometry, not a claim to discover the graph or its geometric duality.

A separate existing calculation of the Levi graph using 21 Klein lines and **21 quadruple** points concerns a different 42-vertex graph; its group is not this 49-vertex, 28-triple-point group. Other graph critical groups for Fermat and Schur line configurations and an integral Steiner-complex incidence lattice are similarly distinct. No checked primary text or queried database summary supplied the stated 49-vertex group or its exact Smith invariants; priority remains provisional.

## Limitations

The result concerns this one naturally defined finite Levi graph over characteristic zero. It does not claim an algebraic Jacobian decomposition, that graph isomorphism is new, nor uniform preservation under positive-characteristic reductions. The 1994 Jeurissen–van Os–Steenbrink full paper could not be accessed; its abstract and bibliographical metadata were checked, leaving a residual risk of an earlier equivalent integral calculation. No independent expert review or machine proof certificate is claimed.

## References

1. T. Bauer, S. Di Rocco, B. Harbourne, J. Huizenga, A. Lundman, P. Pokora, T. Szemberg, *Bounded Negativity and Arrangements of Lines*, arXiv:1407.2966, first posted 2014-07-10, §4.1. https://arxiv.org/abs/1407.2966
2. M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514, first posted 2023-08-31, §3 and Table 2. https://arxiv.org/abs/2308.16514
3. R. H. Jeurissen, C. H. van Os, J. H. M. Steenbrink, *The configuration of bitangents of the Klein curve*, Discrete Math. 132 (1994), 83–96, DOI:10.1016/0012-365X(94)90233-X (full text not accessed).
4. G. Gévay, P. Pokora, *Klein's arrangements of lines and conics*, arXiv:2211.15309 (2022; geometric incidence/duality, not a critical-group computation).
