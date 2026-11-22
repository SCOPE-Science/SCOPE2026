# Complete recolouring-degree spectrum of proper ternary cycle colourings

## Finding
Let \(R_3(C_n)\), for every integer \(n\ge3\), be the simple graph whose vertices are proper colourings of the labelled cycle \(C_n\) by three *named* colours, with edges joining colourings that differ at exactly one vertex. Let \(A_{n,d}\) be the number of vertices of degree \(d\) in this graph, and put \(\binom{j}{k}=0\) when \(k\notin\{0,\dots,j\}\).

Every degree is even. Its **entire distribution** is
\[
A_{n,0}=6\mathbf 1_{3\mid n},\qquad
A_{n,2r}=\frac{3n}{r}\sum_{\substack{r\le a\le n-r\\2a\equiv n\pmod 3}}
\binom{a-1}{r-1}\binom{n-a-1}{r-1}\quad(1\le r\le\lfloor n/2\rfloor).
\]
All other coefficients vanish. The number of undirected recolouring edges is
\[
|E(R_3(C_n))|=n\left(2^{n-2}+2(-1)^n\right).
\]
The maximum degree is \(n\) when \(n\) is even, attained by exactly six colourings. When \(n\) is odd, the maximum is \(n-3\), attained by exactly \(n(n^2-1)/4\) colourings (including \(n=3\), where the graph consists of six isolated vertices). The minimum is zero precisely for \(3\mid n\); otherwise it is two.

## Assumptions and scope
The cycles are simple and labelled, with vertices indexed modulo \(n\); no quotient by rotations or colour permutations is taken. A recolouring changes exactly one vertex to one of the other two named colours and must preserve all edge inequalities. The degree counts distinct permitted target colourings. This is not a swap-move graph and does not concern improper colourings.

## Proof
Fix a proper colouring \(c_i\in\mathbb Z/3\mathbb Z\), and define signs \(\sigma_i\in\{+1,-1\}\) by \(c_{i+1}-c_i\equiv \sigma_i\pmod3\). A cyclic sign string lifts to a proper colouring precisely when \(\sum_i\sigma_i\equiv0\pmod3\). For every admissible sign string there are exactly three choices of the starting colour. If \(a\) of the \(n\) signs are positive, this closure condition is exactly \(2a\equiv n\pmod3\).

At vertex \(i\), a legal alternative colour exists if and only if its two neighbours have the same colour, which is equivalent to \(\sigma_{i-1}=-\sigma_i\); in that case the alternative is unique. Thus the degree is the number of cyclic sign changes, which is even. Degree zero means all signs are equal. Both constant sign strings satisfy closure precisely when \(3\mid n\), producing \(2\cdot3=6\) colourings.

Suppose there are exactly \(2r\) changes, \(r\ge1\), and \(a\) positive signs, \(n-a\) negative signs. There are \(r\) positive runs and \(r\) negative runs. Mark one of the \(r\) positive runs; specifying the first position of that run (\(n\) choices) and positive compositions of \(a\) and \(n-a\) into \(r\) parts gives \(n\binom{a-1}{r-1}\binom{n-a-1}{r-1}\) marked strings. Divide by \(r\) to remove the marking, then multiply by three starting colours. Restricting to the closure congruence proves the complete formula.

For the edge count, mark a vertex at which recolouring is possible. Its two adjacent signs are opposite (two choices), hence contribute zero to the sign sum. Among the remaining \(n-2\) signs, the number of assignments whose sum is zero modulo three is \((2^{n-2}+2(-1)^{n-2})/3\), by the cubic root-of-unity filter: the two nontrivial characters each contribute \((-1)^{n-2}\). Multiplying by three starting colours, two adjacent-sign choices, and \(n\) marked vertices, then dividing by two for undirected edges yields the displayed expression.

For even \(n\), the upper bound of \(n\) cyclic sign changes is attained exactly by the two perfectly alternating sign words. Their sums vanish and their three lifts each give one of the six maximizers. For odd \(n=2m+1\), a sign string has at most \(n-1\) changes, but attaining this would force its sign sum to be \(+1\) or \(-1\), violating closure. Consequently the maximum is at most \(n-3\). For \(m\ge2\), put \(r=m-1\) in the complete formula: of the four possible positive counts \(m-1,m,m+1,m+2\), exactly \(m-1\) and \(m+2\) satisfy closure. Their combined contribution is \(n m(m+1)=n(n^2-1)/4\), which is positive, proving sharpness. For \(n=3\), all six proper colourings are frozen, and the same maximizer-count expression gives six.

If \(3\nmid n\), degree zero is absent. Degree two exists for every \(n\ge4\): there is an integer \(a\in\{1,\dots,n-1\}\) satisfying \(2a\equiv n\pmod3\), with one positive and one negative run. Thus the minimum is two.

## Verification
The standalone `verify.py` checks the binomial-congruence formula by **independent direct enumeration of the named proper colourings** for every \(3\le n\le12\). It also checks the known chromatic total \(2^n+2(-1)^n\), the edge formula, and both exact extremal formulas at all these lengths. It prints `CHECKS PASS` on success. These finite checks are reproducibility tests; the all-length statements follow from the proof above, not from finite enumeration.

## Relationship to prior work
Brewster and Moore (first public preprint 2020-08-27, arXiv:2008.12185) analyze circular colouring reconfiguration and winding invariants; their full preprint's statements and proof concern reachability/mixing, not this degree-multiplicity census. Cereceda, van den Heuvel and Johnson (2010) study paths between three-colourings. Published enumerations of Fourier transforms of proper ternary cycle colourings concern a different observable, and a sector-counting result for the two-layer circular ladder uses a different underlying graph. The present cyclic-sign run count refines the simple information that some colourings are frozen into every local mobility multiplicity, with sharp parity-dependent extrema.

## Limitations
The result concerns exactly three named colours on simple cycles under single-vertex recolouring. It does not describe connected-component sizes, mixing times, spectral gaps, or more than three available colours. A related indexed or otherwise unlocated enumeration could predate this statement; no claim of exhaustive historical priority is made.

## References
1. R. C. Brewster and B. Moore, *Characterizing Circular Colouring Mixing for \(p/q<4\)*, arXiv:2008.12185, first public 2020-08-27, https://arxiv.org/abs/2008.12185.
2. L. Cereceda, J. van den Heuvel, M. Johnson, *Finding paths between 3-colorings*, Journal of Graph Theory 67 (2011), 69–82; first published 2010-12-16, https://doi.org/10.1002/jgt.20514.
3. *Exact winding-sector sizes and exchange counts for three-colourings of circular ladders*, publicly indexed research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-winding-sector-sizes-and-exchange-counts-for-three-colouri--d41f740a6f49.
4. *Complete Fourier zero census for proper ternary cycle colourings*, publicly indexed research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-complete-fourier-zero-census-for-proper-ternary-cycle-colourings--3973681a19d3.
