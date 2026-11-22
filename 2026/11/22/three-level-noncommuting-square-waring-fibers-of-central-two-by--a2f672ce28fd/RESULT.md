# Three-level noncommuting square-Waring fibers of central two-by-two matrices

## Finding
Let \(q\) be any odd prime power, let \(k=\mathbb F_q\), and let \(\chi:k\to\{-1,0,1\}\) denote the quadratic character, with \(\chi(0)=0\). For each \(c\in k\), put
\[
W_q(c)=\#\{(X,Y)\in\mathrm{GL}_2(k)^2:X^2+Y^2=cI_2,\ XY\ne YX\}.
\]
Then
\[
\boxed{W_q(0)=q^2(q-1)(q^2-1),\qquad W_q(c)=q(q^2-1)\bigl(q(q-2)-2\chi(c)\bigr)\quad(c\ne0).}
\]
Consequently the central targets admit exactly three ordered-fiber sizes, indexed by the zero, nonzero-square, and nonsquare classes; their respective target multiplicities are \(1,(q-1)/2,(q-1)/2\). Every central target has a noncommuting representation by two *invertible* squares, including when \(q=3\). In particular, for all \(c\in k\), the count is positive.

A structural assertion valid over **every** field of characteristic different from two is also established: whenever \(X^2+Y^2\) is scalar and \(XY\ne YX\), both \(X\) and \(Y\) have trace zero. Thus the noncommuting central problem is intrinsically a quadratic-form problem on the trace-zero subspace, not a general eight-variable matrix enumeration.

## Assumptions and scope
The characteristic is odd; finite prime powers, not merely prime fields, are covered. Matrices are labelled and ordered, and both are invertible. The noncommuting inequality is strict. The prescribed output is a *scalar* matrix; no assertion is made about nonscalar targets or larger matrix sizes. The character \(\chi\) is the ordinary multiplicative quadratic character, extended by zero at the origin. Counts are literal integers without probabilistic normalization.

## Proof
**1. Trace rigidity.** Write uniquely \(X=aI_2+U\) and \(Y=bI_2+V\), where \(a,b\in k\) and \(\mathrm{tr}U=\mathrm{tr}V=0\). Cayley--Hamilton gives \(U^2=-\det(U)I_2\) and \(V^2=-\det(V)I_2\), so the traceless component of \(X^2+Y^2\) is \(2(aU+bV)\). If the square sum is scalar, \(aU+bV=0\). If \(a\ne0\), then \(U\) is a scalar multiple of \(V\), and hence \(X,Y\) commute; the same holds if \(b\ne0\). Therefore, for noncommuting solutions, \(a=b=0\). Conversely, any two traceless matrices have scalar squares by Cayley--Hamilton. Invertibility of each is equivalent to its square being a nonzero scalar.

**2. Scalar-square fibers.** Write a traceless matrix as
\[
U=\begin{pmatrix}u&v\\w&-u\end{pmatrix},\qquad U^2=(u^2+vw)I_2.
\]
For \(d\in k^\times\), the number \(n(d)\) of such matrices with square \(dI_2\) is
\[
n(d)=q^2+q\chi(d).
\]
Indeed, for any \(u\), the equation \(vw=d-u^2\) has \(q-1\) solutions if its right side is nonzero and \(2q-1\) if zero; exactly \(1+\chi(d)\) values of \(u\) have \(u^2=d\).

**3. Count all invertible traceless ordered pairs.** Let \(T(c)\) count all ordered traceless, invertible pairs with squares summing to \(cI_2\), without imposing noncommutativity. Then
\[
T(c)=\sum_{d\in k\setminus\{0,c\}}n(d)n(c-d).
\]
The elementary quadratic-character identities, valid in every odd finite field, are
\[
\sum_{d\in k}\chi(d)\chi(c-d)=\begin{cases}(q-1)\chi(-1),&c=0,\\-\chi(-1),&c\ne0,\end{cases}
\]
and for \(c\ne0\), \(\sum_{d\ne0,c}\chi(d)=\sum_{d\ne0,c}\chi(c-d)=-\chi(c)\). These follow by scaling \(d\) and counting solutions to a difference-of-two-squares equation, or directly from the quadratic Jacobi sum. Expanding the product thus gives
\[
T(0)=(q-1)q^4+(q-1)q^2\chi(-1),
\]
\[
T(c)=q^4(q-2)-2q^3\chi(c)-q^2\chi(-1)\qquad(c\ne0).
\]

**4. Subtract exactly the commuting pairs.** A nonzero invertible traceless \(U\) is nonscalar; its centralizer in \(M_2(k)\) is \(kI_2+kU\), and its traceless centralizer is \(kU\). Hence an invertible traceless \(V\) commutes with \(U\) precisely when \(V=tU\) for one \(t\in k^\times\). Let \(r=1+\chi(-1)\) be the number of nonzero roots of \(1+t^2=0\). For the zero target,
\[
C(0)=r(q-1)q^2,
\]
since each such \(t\) permits every invertible traceless \(U\), and \(\sum_{d\ne0}n(d)=(q-1)q^2\). For a nonzero \(c\), the equation \((1+t^2)U^2=cI_2\) requires \(1+t^2\ne0\) and gives
\[
C(c)=\sum_{\substack{t\in k^\times\\1+t^2\ne0}}\left(q^2+q\chi\left(\frac{c}{1+t^2}\right)\right).
\]
The quadratic character sum \(\sum_{t\in k^\times}\chi(1+t^2)=-2\) follows by counting \(z^2=1+t^2\) using \((z-t)(z+t)=1\), which has exactly \(q-1\) ordered solutions, hence \(\sum_{t\in k}\chi(1+t^2)=-1\). Therefore
\[
C(c)=q^2(q-1-r)-2q\chi(c)\qquad(c\ne0).
\]
Subtracting \(C\) from \(T\), and using \(r=1+\chi(-1)\), cancels every dependence on \(\chi(-1)\) and yields the two formulas in the finding.

**5. Range, sharpness, and partition.** Since \(q\ge3\), \(q(q-2)-2\chi(c)\ge q(q-2)-2>0\) except the lower bound at \(q=3\) is exactly \(1>0\). The nonzero-square and nonsquare values differ by \(4q(q^2-1)\), while the zero value is larger than both, so there are exactly three distinct levels. The character classes contain the stated numbers of targets. This proves the complete claim.

## Verification
The standalone `check_waring.py` implements independent literal matrix multiplication, inversion tests, commutator comparisons, and direct square addition. For \(q=3,5\), it searches *all* ordered pairs in \(\mathrm{GL}_2(k)^2\), without assuming the trace-rigidity lemma; all target fibers agree with the formula. For \(q=7,11\) and the extension field \(\mathbb F_9=\mathbb F_3[t]/(t^2+1)\), it independently searches all invertible traceless matrix pairs to corroborate the exact scalar character counts. It prints `MATRIX_SQUARE_WARING_NONCOMMUTING_OK` on success. Run `python3 check_waring.py` from the directory containing this file. These finite tests corroborate, but do not replace, the uniform symbolic proof.

## Relationship to prior work
Datta, Ghosh, Maji and Manik (arXiv:2611.16651v1, submitted 2026-11-12) study the finite-field matrix Waring equation with general invertible coefficients but require \(\gcd(k,p-1)=1\). Their main surjectivity result does not apply to the square exponent over odd fields, and does not give central noncommuting ordered-fiber counts. Panja, Saini and Singh (arXiv:2305.19731 and arXiv:2312.13865) establish image/surjectivity results for polynomial matrix maps under different hypotheses, not the present exact counts. The published matrix-square-graph Fourier-support calculation records character support and convolution singular values of the graph \(\{(X,X^2)\}\subset M_2(k)^2\); neither its stated graph transform nor its singular-value distribution yields this invertible, noncommuting central sum-of-squares enumeration. A distinct known anticommutator formula studies \(XY+YX\), not \(X^2+Y^2\). Classical work on matrices as sums of squares investigates existence and minimal numbers of summands, and is not claimed as new.

## Limitations
The theorem concerns scalar targets and ordered noncommuting *invertible* pairs, not all prescribed matrices. It does not establish novelty of square representability in general, classify similarity orbits of representations, treat even characteristic, or count arbitrary nonscalar outputs. A potentially relevant 1977 article on matrices as sums of squares was only available through abstract-level evidence; its full text was not inspected, leaving a genuine historical-priority risk. A covering unindexed result on central fibers could exist. The finite checker does not establish an infinite theorem without the displayed proof. Independent mathematical validation has not been performed.

## References
- S. Datta, S. Ghosh, A. Maji and A. Manik, *Matrix Waring Problem in finite fields with coefficients from GL(2,F_p)*, arXiv:2611.16651v1, first public 2026-11-12, https://arxiv.org/html/2611.16651v1.
- A. Panja, S. Saini and A. Singh, *Surjectivity of polynomial maps on matrices*, arXiv:2305.19731, https://arxiv.org/pdf/2305.19731.
- A. Panja, S. Saini and A. Singh, *Images of polynomial maps with constants*, arXiv:2312.13865, https://arxiv.org/pdf/2312.13865.
- R. P. Griffin and M. Krusemeyer, *Matrices as sums of squares*, Linear and Multilinear Algebra (1977), DOI:10.1080/03081087708817172 (historical comparison from abstract, not full text).
- *Fourier support of the two-by-two matrix-square graph in all characteristics*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-fourier-support-of-the-2-times2-matrix-square-graph-in-all-chara--75bded936053.
- *Complete prescribed Jordan-product fibers for two-by-two matrices over odd finite fields*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-prescribed-jordan-product-fibers-for-two-by-two-matrice--4bc91560254f.
