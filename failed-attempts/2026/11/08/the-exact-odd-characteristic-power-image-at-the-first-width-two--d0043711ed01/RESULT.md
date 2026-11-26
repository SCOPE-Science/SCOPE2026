# The exact odd-characteristic power image at the first width-two unitriangular threshold

## Finding
Let \(p\ge3\) be prime, \(k\) any field of characteristic \(p\), and \(G=\operatorname{UT}_{p+3}(k)\). Put \(\mathcal P=\{g^p:g\in G\}\). Every element of \(\mathcal P\) belongs to the subgroup \(\gamma_p(G)\), whose matrices are \(I+T\) with entries of \(T\) zero whenever the column-minus-row difference is smaller than \(p\). Its six potentially nonzero coordinates are
\[
(\alpha,\beta,\gamma,\delta,\varepsilon,\zeta)=
(T_{1,p+1},T_{2,p+2},T_{3,p+3},T_{1,p+2},T_{2,p+3},T_{1,p+3}).
\]
The exact image criterion is
\[
\boxed{\ I+T\in\mathcal P\iff
\bigl(\beta=0\Rightarrow\alpha\gamma=0\bigr)
\ \text{and}\
\bigl(\beta\ne0,\ \alpha=\gamma=0\Rightarrow\beta\zeta=\delta\varepsilon\bigr).\ }
\]
For every finite field \(\mathbb F_q\) of characteristic \(p\ge3\),
\[
\boxed{\#\mathcal P=q^6-q^5+q^4+q^3-q^2.}
\]
The claim is a complete element-membership classification and exact image count for every odd prime characteristic, not a statement about the number of preimages of a particular element.

## Assumptions and scope
All matrices are upper unitriangular of size \(p+3\). No algebraic-closure or finiteness hypothesis is imposed for the criterion; finiteness is required only for the cardinality formula. Positions use one-based indices. By definition \(\gamma_p(G)\) is the \(p\)-th lower-central-series term, so its matrices have zero entries on superdiagonals of order less than \(p\). The six displayed coordinates are unrestricted as coordinates on that subgroup. The claim does not cover \(p=2\) or matrix sizes greater than \(p+3\).

## Proof
**Power-path reduction.** Write \(g=I+N\), and set \(a_i=N_{i,i+1}\) for \(1\le i\le p+2\), \(b_i=N_{i,i+2}\) for \(1\le i\le p+1\), and \(c_i=N_{i,i+3}\) for \(1\le i\le p\). In characteristic \(p\), the binomial identity gives \(g^p=I+N^p\). Each entry of \(N^p\) is a sum of products along strictly increasing paths of exactly \(p\) edges. Since the matrix size is \(p+3\), only the six specified positions survive. Directly,
\[
\alpha=\prod_{i=1}^{p}a_i,\qquad
\beta=\prod_{i=2}^{p+1}a_i,\qquad
\gamma=\prod_{i=3}^{p+2}a_i.
\]
For the next two coordinates the one-skipped-vertex formulas are
\[
\delta=\sum_{j=1}^{p}
 \left(\prod_{i=1}^{j-1}a_i\right)b_j
 \left(\prod_{i=j+2}^{p+1}a_i\right),\qquad
\varepsilon=\sum_{j=2}^{p+1}
 \left(\prod_{i=2}^{j-1}a_i\right)b_j
 \left(\prod_{i=j+2}^{p+2}a_i\right).
\]
Here an empty product equals \(1\). In \(\zeta=(N^p)_{1,p+3}\), every path has either one jump of length three (some \(c_j\)) or two jumps of length two (some \(b_j,b_l\)); all other steps have length one. Entries farther than three above the diagonal of \(N\) never enter these six expressions.

**Necessity.** If \(\beta=0\) but \(\alpha\ne0\), then \(a_1,\ldots,a_p\) are nonzero and necessarily \(a_{p+1}=0\), forcing \(\gamma=0\). The symmetric argument deals with \(\gamma\ne0\), proving the first implication. If \(\beta\ne0\) and \(\alpha=\gamma=0\), then \(a_2,\ldots,a_{p+1}\ne0\) but \(a_1=a_{p+2}=0\). The path formulas collapse to
\[
\delta=b_1\prod_{i=3}^{p+1}a_i,\quad
\varepsilon=b_{p+1}\prod_{i=2}^{p}a_i,\quad
\zeta=b_1b_{p+1}\prod_{i=3}^{p}a_i.
\]
Thus \(\beta\zeta=\delta\varepsilon\).

**Sufficiency by explicit sparse roots.** It is enough to choose the first three superdiagonals of \(N\); set all other entries to zero. In the following prescriptions every unmentioned \(a_i,b_i,c_i\) is zero.

If \(\beta\ne0\), choose \(a_2=\cdots=a_p=1\), \(a_{p+1}=\beta\), \(a_1=\alpha\), \(a_{p+2}=\gamma/\beta\), \(b_1=\delta/\beta\), and \(b_{p+1}=\varepsilon\). These choices produce the required first five coordinates and initially give \(\zeta=\delta\varepsilon/\beta\). If \(\gamma\ne0\), set \(c_1=(\zeta-\delta\varepsilon/\beta)/\gamma\); otherwise, when \(\alpha\ne0\), set \(c_p=(\zeta-\delta\varepsilon/\beta)/\alpha\). If both vanish, the second implication says that no correction is needed.

If \(\beta=0,\alpha\ne0\), take \(a_1=\alpha\), \(a_2=\cdots=a_p=1\), \(a_{p+1}=0\), \(a_{p+2}=1\), \(b_p=\delta/\alpha\), \(b_{p+1}=\varepsilon-b_p\), and \(c_p=\zeta/\alpha\). If \(\beta=0,\gamma\ne0\), take \(a_1=1\), \(a_2=0\), \(a_3=\cdots=a_{p+1}=1\), \(a_{p+2}=\gamma\), \(b_2=\varepsilon/\gamma\), \(b_1=\delta-b_2\), and \(c_1=\zeta/\gamma\). In either case the other outer coordinate vanishes as required.

Finally assume \(\alpha=\beta=\gamma=0\). Four disjoint cases construct every \((\delta,\varepsilon,\zeta)\):

- If \(\delta\varepsilon\ne0\), let \(a_1=\delta\), \(a_{p+2}=\varepsilon\), \(a_3=0\), all \(a_i=1\) for \(2\le i\le p+1\) except \(i=3\), and choose \(b_2=1\), \(c_2=\zeta/(\delta\varepsilon)\). The index \(2\) for \(c_2\) exists because \(p\ge3\).
- If \(\delta\ne0,\varepsilon=0\), let \(a_3=\cdots=a_{p+1}=1\), \(b_1=\delta\), \(b_{p+1}=\zeta/\delta\).
- If \(\delta=0,\varepsilon\ne0\), let \(a_2=\cdots=a_p=1\), \(b_1=\zeta/\varepsilon\), \(b_{p+1}=\varepsilon\).
- If \(\delta=\varepsilon=0\), let \(a_3=\cdots=a_p=1\), \(b_1=\zeta\), \(b_{p+1}=1\).

Substituting in the path formulas checks all six desired coordinates. In the final three cases, omitted first-superdiagonal entries are zero. This completes sufficiency over an arbitrary field of characteristic \(p\ge3\).

**Exact finite-field count.** When \(\beta=0\), the allowed pairs \((\alpha,\gamma)\) number \(2q-1\), and each permits all \(q^3\) choices of \((\delta,\varepsilon,\zeta)\). When \(\beta\ne0\) and \((\alpha,\gamma)\ne(0,0)\), there are \((q-1)(q^2-1)\) choices of the three leading coordinates, each permitting \(q^3\) other choices. When \(\beta\ne0\) and \(\alpha=\gamma=0\), the final coordinate is uniquely determined by \(\beta\zeta=\delta\varepsilon\), giving \((q-1)q^2\) choices. The sum is
\[
(2q-1)q^3+(q-1)(q^2-1)q^3+(q-1)q^2
=q^6-q^5+q^4+q^3-q^2.
\]

## Verification
The standalone program `power_test.py` constructs a root for every target satisfying the criterion over \(\mathbb F_3\) and \(\mathbb F_5\), checking each result using an independently implemented matrix-power routine. It also enumerates all \(3^{12}=531441\) choices for the only source entries that can influence cubes in \(\operatorname{UT}_6(\mathbb F_3)\); the other three source entries are immaterial to the power map. The image has exactly \(585\) elements, matching the theorem and an earlier published single-field computation. For characteristic five the complete target sweep yields \(13225\) images, as predicted. Random constructor tests for primes seven and eleven also passed but are not part of the standalone evidence file. These finite checks do not constitute the proof for arbitrary primes or fields.

## Relationship to prior work
Bier (2012), Theorem 3, determines when the \(p\)-power word has width two in unitriangular groups; in particular the first failure of width one is the size \(p+3\). Sosnovsky (2012) studies the corresponding verbal-width phenomenon in triangular groups. Neither inspected statement supplies an exact six-coordinate image description or its uniform point count. Dolfi, Singh and Yadav (2019), Theorem A and Proposition 3.5, prove properness and give lower bounds for the power image; their Example 4.5 and table already record the particular number \(585\) for \(\operatorname{UT}_6(\mathbb F_3)\). That numerical case is not claimed as new. A separate characteristic-two size-five classification was already available; the present theorem is explicitly restricted to odd primes and gives a uniform statement for an unbounded family of group sizes. Historical priority outside the checked sources remains unverified.

## Limitations
No formula is asserted for individual root-fiber multiplicities, for general matrix size \(n>p+3\), or for powers other than \(p\). The finite-field count is only for \(q\) a power of \(p\). The proof is an elementary coordinate argument, and independent historical-priority and mathematical audit have not been performed.

## References
1. A. Bier, *The Width of Verbal Subgroups in the Group of Unitriangular Matrices over a Field*, International Journal of Algebra and Computation **22** (2012), 1250019, DOI:10.1142/S0218196712500191. Open manuscript: https://pdfs.semanticscholar.org/ce40/e2080f04704859e482e378de546406687d2c.pdf.
2. Yu. V. Sosnovsky, *On the Width of Verbal Subgroups of the Groups of Triangular Matrices over a Field of Arbitrary Characteristic*, arXiv:1201.6513v1, first posted 2012-01-31. https://arxiv.org/abs/1201.6513.
3. S. Dolfi, A. Singh, M. K. Yadav, *\(p\)-Power Conjugacy Classes in \(U(n,q)\) and \(T(n,q)\)*, arXiv:1905.04244v1, first posted 2019-05-10. https://arxiv.org/abs/1905.04244.
