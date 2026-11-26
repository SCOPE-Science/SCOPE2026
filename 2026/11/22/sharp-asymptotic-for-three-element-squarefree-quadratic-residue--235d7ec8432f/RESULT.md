# Sharp asymptotic for three-element squarefree quadratic-residue covers

## Finding

Let \(H(N)\) count unordered three-element subsets of the squarefree integers in \(\{2,\ldots,N\}\) such that for every prime \(p\) at least one of the three elements is a square modulo \(p\), with zero counted as a square. As \(N\to\infty\),
\[
H(N)=(\kappa+o(1))N^{3/2},\qquad
\kappa=\frac23\prod_{p\ \mathrm{prime}}(1-p^{-1})^3(1+3p^{-1}).
\]
The Euler product converges absolutely to a positive number. For every integer \(N\ge2\) the exact count is
\[
H(N)=\sum_{\substack{1\le u<v<w\\vw\le N}}\mu^2(uvw).
\]

## Assumptions and scope

The elements being counted are positive, distinct, squarefree and strictly greater than one; they need not be pairwise coprime. This is a count of sets, not of ordered triples. On this domain the every-prime condition is equivalent to the almost-every-prime condition. The asymptotic gives the leading term only.

## Proof

**1. Reduction to square products.** The Fried–Filaseta–Richman criterion, as stated by Mishra [1, Proposition 2.1], says that a finite set of nonzero integers contains a square modulo almost every prime precisely when the product of some odd-cardinality subset is an integer square. Here no singleton is square, so necessity reduces to \(abc\) being square. For sufficiency, the prime 2 is automatic. If an odd prime divides \(abc\), one entry is zero modulo that prime; otherwise the three Legendre symbols have product \(+1\), so they cannot all be \(-1\). This proves the every-prime statement.

**2. Unique factor coordinates.** Order the elements as \(a<b<c\). Because each is squarefree, every prime occurs in exactly zero or two entries. The factors \(u=\gcd(a,b)\), \(v=\gcd(a,c)\), \(w=\gcd(b,c)\) therefore have squarefree product and give \((a,b,c)=(uv,uw,vw)\). The order and height are exactly \(1\le u<v<w\) and \(vw\le N\). Conversely these bounds together with squarefreeness of \(uvw\) produce three distinct squarefree elements, none equal to one, and their product is square. These maps are inverse and give the exact sum.

**3. Region volume and cusp bound.** Put \(X=\sqrt N\) and \(\mathcal R=\{(x,y,z)\in\mathbb R_{>0}^3:x<y<z,\ yz\le1\}\). Then
\[
\operatorname{vol}(\mathcal R)=\int_0^1\int_y^{1/y}y\,dz\,dy=\frac23.
\]
For \(B\ge1\), cutting at \(z=B\) removes volume \(1/(2B)\) by integrating \(\int_0^{1/z}y\,dy\) over \(z>B\). The number of integer points with \(w>BX\), even without arithmetic restrictions, is at most
\[
\frac12\sum_{w>BX}(N/w)^2=O(N^{3/2}/B).
\]
Indeed for fixed \(w\) there are at most \(\binom{\lfloor N/w\rfloor}{2}\) increasing pairs \(u<v\).

**4. Local density and removal of the prime cutoff.** Modulo \(p^2\), squarefreeness of the product allows no coordinate divisible by \(p\), or exactly one coordinate with valuation one. The density is
\[
\delta_p=(1-p^{-1})^3+3(p^{-1}-p^{-2})(1-p^{-1})^2
=(1-p^{-1})^3(1+3p^{-1}).
\]
These factors are positive and \(1+O(p^{-2})\), giving an absolutely convergent positive product. Fix \(B\ge1\) and \(Y\ge2\), and write \(\mathcal R_B=\mathcal R\cap\{z\le B\}\). The region \(\mathcal R_B\) is bounded and Jordan measurable. Equidistribution by Riemann sums in each residue class modulo the fixed integer \(\prod_{p\le Y}p^2\), together with the Chinese remainder theorem, gives the truncated density
\[
\lim_{N\to\infty}X^{-3}\#\{(u,v,w)\in X\mathcal R_B\cap\mathbb Z^3:\ p^2\nmid uvw\ \text{for all primes }p\le Y\}
=\operatorname{vol}(\mathcal R_B)\prod_{p\le Y}\delta_p.
\]
An offending prime \(p>Y\) either divides two distinct coordinates or has its square dividing one coordinate. In \((0,BX]^3\), the number of nonzero integer points for each of the six choices of pattern is at most \((BX)^3/p^2\), using \(\lfloor BX/p^j\rfloor\le BX/p^j\) for \(j=1,2\). Summation over \(p>Y\) therefore costs \(O(B^3X^3/Y)\), uniformly in \(N\). First send \(N\to\infty\), then \(Y\to\infty\) at fixed \(B\), and finally \(B\to\infty\), using the cusp bound. This gives the asserted leading constant.

## Verification

The accompanying `check.py` compares direct integer-square tests on squarefree triples and the factor enumeration at heights \(30,100,200,300\), obtaining \(12,77,222,422\). Factor enumeration gives \(2491,12775,77719\) at \(1000,3000,10000\), respectively. The value \(0.076589731381\) in `check_results.txt` is the prime product with the factor \(2/3\) truncated at \(p\le100000\); it is not a decimal expansion of \(\kappa\) to the displayed precision. The finite checks are diagnostic; the proof supplies the infinite-product formula and asymptotic.

## Relationship to prior work

Mishra [1] gives the general odd-subproduct criterion and a generic upper bound on the number of such residue-covering sets; the bound for triples and squares does not yield the leading squarefree count. The standard pairwise-product coordinates occur in Tao [2, §1, equation (1.3)] in the setting of extremal sets avoiding square products. Erdős–Sárközy–Sós [3] and Skałba [4] concern extremal or forcing problems rather than the exact count of all squarefree triples at a common height. The contribution here is the sharp squarefree counting asymptotic with the explicit volume and local factors, not the residue criterion or factor coordinates themselves. The comparison does not establish exhaustive historical priority.

## Limitations

The exclusion of one is essential: a triple containing one automatically covers every prime. No error rate, results for longer sets or results for a different height region are asserted.

## References

1. B. Mishra, *Almost No Finite Subset of Integers Contains a qth Power Modulo Almost Every Prime*, arXiv:2308.13167, Proposition 2.1 and Theorem 1.1. https://arxiv.org/abs/2308.13167
2. T. Tao, *On Product Representations of Squares*, arXiv:2405.11610, §1, equation (1.3). https://arxiv.org/abs/2405.11610
3. P. Erdős, A. Sárközy and V. T. Sós, *On Product Representations of Powers, I*, European Journal of Combinatorics 16 (1995), 567–588. https://real.mtak.hu/110606/1/1-s2.0-019566989590039X-main.pdf
4. M. Skałba, *Product of Three Numbers Being a Square as a Ramsey Property*, Colloquium Mathematicum 120 (2010), 1–5. https://doi.org/10.4064/cm120-1-1
