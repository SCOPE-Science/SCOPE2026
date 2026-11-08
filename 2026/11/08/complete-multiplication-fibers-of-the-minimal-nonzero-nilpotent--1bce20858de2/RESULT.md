# Complete multiplication fibers of the minimal nonzero nilpotent orbit over finite fields

## Finding
Let \(k=\mathbb F_q\) be an arbitrary finite field, \(n\ge2\), and
\[
\mathcal N=\{A\in M_n(k): A^2=0,\ \operatorname{rank}A=1\}.
\]
This is the single nonzero nilpotent similarity class with Jordan type \((2,1^{n-2})\). For each prescribed matrix \(C\), set \(F(C)=\#\{(A,B)\in\mathcal N^2:AB=C\}\). Write
\[
N=|\mathcal N|=\frac{(q^n-1)(q^{n-1}-1)}{q-1}.
\]
Then the **complete product-fiber law** is
\[
F(C)=\begin{cases}
\displaystyle\frac{(q^n-1)(q^{n-1}-1)^3}{(q-1)^2},& C=0,\\[3pt]
(q^{n-1}-1)q^{n-2},&\operatorname{rank}C=1,\ \operatorname{tr}C\ne0,\\[3pt]
q^{n-1}(q^{n-2}-1),&\operatorname{rank}C=1,\ \operatorname{tr}C=0,\ C\ne0,\\[3pt]
0,&\operatorname{rank}C\ge2.
\end{cases}
\]
The target populations in order are \(1\), \((q^n-1)q^{n-1}\), \(N\), and \(q^{n^2}-1-(q^n-1)q^{n-1}-N\). Every nonzero rank-one target of nonzero trace is represented for all \(n\ge2\). A nonzero rank-one nilpotent target is represented **if and only if** \(n\ge3\). Thus dimension two is the exact obstruction.

The product order is essential: whenever \(A,B\in\mathcal N\) have \(AB\ne0\), one has
\[
BA=0\quad\Longleftrightarrow\quad\operatorname{tr}(AB)=0.
\]
In particular, no pair in this orbit has both \(AB\) and \(BA\) nonzero nilpotent. The number of ordered pairs in each of the two asymmetric strata \((AB\ne0\text{ nilpotent},BA=0)\) and \((AB=0,BA\ne0\text{ nilpotent})\) is
\[
Nq^{n-1}(q^{n-2}-1).
\]

## Assumptions and scope
All products and traces are over \(k\), with \(q\) an arbitrary prime power; characteristic two is included. The factors are **nonzero, rank exactly one, square-zero** matrices (not all nilpotent matrices, not all square-zero matrices). All pairs are **ordered**. The target can be any element of \(M_n(k)\). Powers are ordinary integer exponents in the counting expressions. No algebraic-closure assumption is made.

## Proof
**1. Parametrization and orbit size.** A nonzero rank-one endomorphism has a presentation \(A=u\alpha\), with \(0\ne u\in k^n\), \(0\ne\alpha\in (k^n)^*\), unique up to \((u,\alpha)\mapsto(cu,c^{-1}\alpha)\). Since \(A^2=\alpha(u)A\), the square-zero condition is \(\alpha(u)=0\). There are \((q^n-1)/(q-1)\) image lines and, for each, \(q^{n-1}-1\) choices of nonzero annihilating functional after fixing a vector on the line. This gives \(N\).

**2. Fixed nonzero target.** If \(AB=C\ne0\), then \(\operatorname{rank}C=1\). Fix any presentation \(C=u_0\beta_0\), with \(u_0\ne0\) and \(\beta_0\ne0\). Necessarily \(\operatorname{im}A=ku_0\) and \(\operatorname{row}(B)=k\beta_0\). Thus the unique normalized representations are
\[
A=u_0\alpha,\quad B=x\beta_0,\qquad
\alpha(u_0)=0,\quad\beta_0(x)=0,\quad\alpha(x)=1.
\]
Conversely, every solution of these three equations gives a unique factorization in \(\mathcal N^2\). Put \(U=\{\alpha:\alpha(u_0)=0\}\) and \(X=\ker\beta_0\), both of dimension \(n-1\). We must count pairs \((\alpha,x)\in U\times X\) with \(\alpha(x)=1\).

If \(\beta_0(u_0)\ne0\), restriction gives a perfect pairing \(U\times X\to k\), so all \(q^{n-1}-1\) nonzero functionals in \(U\) give \(q^{n-2}\) solutions for \(x\). If \(\beta_0(u_0)=0\), the pairing has one-dimensional left radical \(k\beta_0\) and one-dimensional right radical \(ku_0\); precisely \(q^{n-1}-q\) elements of \(U\) give nonzero functionals on \(X\), each with \(q^{n-2}\) solutions. The resulting counts are \((q^{n-1}-1)q^{n-2}\) and \(q^{n-1}(q^{n-2}-1)\). Since \(\beta_0(u_0)=\operatorname{tr}C\), these are the announced strata.

**3. Zero target.** For a fixed \(A=u\alpha\in\mathcal N\), a factor \(B=x\beta\in\mathcal N\) satisfies \(AB=0\) exactly when \(\alpha(x)=0\). Therefore the image line \(kx\) is one of \((q^{n-1}-1)/(q-1)\) lines in \(\ker\alpha\); for each, there are \(q^{n-1}-1\) nonzero \(\beta\) annihilating \(kx\). Multiply this number by \(N\) to obtain \(F(0)=N(q^{n-1}-1)^2/(q-1)\), as written.

**4. Target populations.** The trace-zero nonzero rank-one matrices are exactly \(\mathcal N\), hence number \(N\). For any prescribed \(t\in k^*\), a rank-one matrix of trace \(t\) has \((q^n-1)q^{n-1}/(q-1)\) presentations modulo nonzero scalar, and there are \(q-1\) choices of \(t\). Thus the nonzero-trace rank-one population is \((q^n-1)q^{n-1}\). All remaining nonzero targets have rank at least two. Summing the target populations weighted by their fibers yields \(N^2\), also independently guaranteed by the exhaustive disjoint fiber partition.

**5. Reversed products.** From the normalized representations in step 2,
\[
BA=x\,\beta_0(u_0)\,\alpha=(\operatorname{tr}C)x\alpha.
\]
Here \(x\) and \(\alpha\) are nonzero because \(\alpha(x)=1\). Therefore \(BA=0\) precisely when \(\operatorname{tr}C=0\); the stated asymmetric pair counts follow by multiplying the trace-zero rank-one target population \(N\) by its fiber count. Interchanging \(A,B\) gives the reverse orientation, completing the proof.

## Verification
The standalone Python file `check_minimal_nilpotent_product.py` constructs every rank-one square-zero matrix by normalized outer products, multiplies each ordered pair by literal finite-field arithmetic, and compares the resulting target-frequency histogram with the proposed formula **for every possible matrix target**, including zero and rank-at-least-two targets. The finite-field implementations include prime fields and the extensions of orders \(4\) and \(8\). The executed cases are \((n,q)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(3,5),(4,2)\); the archived stdout is `verification_output.txt`. Run from the extracted package directory with `python3 check_minimal_nilpotent_product.py`. The code uses only the Python standard library. These exhaustive finite checks corroborate, but do not replace, the general proof.

## Relationship to prior work
The product-existence question for nilpotent matrices is classical. Wu (1987) gives a factorization criterion for general singular matrices over the complex numbers, including the exceptional nonzero two-by-two nilpotent target; Sourour (1992) extends an existence statement to arbitrary fields. Those results motivate a **factorization multiplicity** invariant but do not supply a formula for all ordered pairs of factors from the minimal nilpotent class. Britnell and Wildon (arXiv:1001.0811, first posted January 6, 2010) investigate which nilpotent similarity classes contain **commuting** representatives; commuting-class existence is different from the pushforward of matrix multiplication on one fixed nilpotent orbit. Nearby finite-field idempotent–nilpotent and nilpotent–involution factorization censuses likewise involve different factor classes; their formulas do not imply the present fibers.

## Limitations
No claim is made about arbitrary-rank nilpotent factors, longer products, higher simultaneous product invariants, factorization-orbit classifications, or characteristic-free ring coefficients. The established dimension-two existence obstruction is **not** asserted new. Novelty refers only to the complete exact multiplicity law and reversed-product structural stratification; historical priority is provisional pending broader independent comparison. The computational sample checks finitely many fields and dimensions; the theorem for all prime powers and \(n\ge2\) is proved algebraically.

## References
- P.-Y. Wu, *Products of Nilpotent Matrices*, Linear Algebra and its Applications **96** (1987), 227–232, DOI `10.1016/0024-3795(87)90346-6`. Primary text: https://ir.lib.nycu.edu.tw/bitstream/11536/4603/1/A1987K605100015.pdf.
- A. R. Sourour, *Nilpotent factorization of matrices*, Linear and Multilinear Algebra **31** (1992), 303–308, DOI `10.1080/03081089208818141`. Abstract: https://www.tandfonline.com/doi/abs/10.1080/03081089208818141.
- J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811 (first posted 2010-01-06); Journal of the London Mathematical Society **83** (2011), 470–492. https://arxiv.org/abs/1001.0811.
- J. D. Botha, *Factorization of a singular matrix into nilpotent matrices with prescribed ranks*, Linear and Multilinear Algebra **38** (1994), 145–150, DOI `10.1080/03081089508818347` (abstract consulted).
