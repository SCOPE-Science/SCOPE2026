# All-length multiplication fibers and exact alternating mixing for minimal nilpotent matrices

## Finding
Let \(K=\mathbb F_q\) be a finite field of arbitrary characteristic, \(n\ge2\), and \(k\ge2\). Consider the minimal nonzero nilpotent orbit
\[
\mathcal N=\{X\in M_n(K):\operatorname{rank}X=1,\ X^2=0\}.
\]
For every prescribed \(Z\in M_n(K)\) let \(F_k(Z)\) be the number of ordered \(k\)-tuples of elements of \(\mathcal N\) whose product is exactly \(Z\). Set
\[
P=\frac{q^n-1}{q-1},\quad H=\frac{q^{n-1}-1}{q-1},\quad t=q^{n-2}(q-1),\quad r=k-1,
\]
\[
N=(q-1)PH,\qquad \lambda=t(P-1)=q^{n-1}(q^{n-1}-1).
\]
Then the **complete all-length prescribed-product law** is
\[
\boxed{F_k(Z)=\begin{cases}
N^k-N\lambda^r,&Z=0,\\[3pt]
\displaystyle t^r\left[H\frac{(P-1)^r-(-1)^r}{P}+(-1)^r\mathbf1_{\{\operatorname{tr}Z=0\}}\right],&\operatorname{rank}Z=1,\\[5pt]
0,&\operatorname{rank}Z\ge2.
\end{cases}}
\]
The bracket in the middle case is a nonnegative integer. The difference between the rank-one trace-zero and nonzero-trace fibers is exactly \((-t)^r\), so its sign alternates with word-length parity. The only positive-rank image obstruction is \(n=2\), \(k=2\), \(\operatorname{tr}Z=0\). Thus **every rank-one matrix is a product of \(k\) orbit elements for every \(k\ge3\)**, even over \(\mathbb F_2\).

If the factors are sampled uniformly and independently, the probability of a nonzero product is
\[
\Pr(X_1\cdots X_k\ne0)=\left(\frac{\lambda}{N}\right)^r
=\left(\frac{q^{n-1}(q-1)}{q^n-1}\right)^r.
\]
Conditioned on survival, the distribution on the \((q-1)P^2\) nonzero rank-one matrices differs from the uniform distribution by the **exact total-variation distance**
\[
\boxed{d_{\mathrm{TV}}=\frac{P-H}{P(P-1)^r}.}
\]
These formulas hold for all finite extension fields and all positive characteristics.

## Assumptions and scope
Every factor belongs to the **single similarity orbit** of rank-one square-zero matrices; zero and higher-rank nilpotents are not factors. Ordered words count different positions separately. The target ranges over the entire matrix algebra, not merely the orbit. All matrix products are associative ordinary products, not Lie brackets or Jordan products. Total variation is one-half of the sum of absolute probability differences over the finite target set; the conditional distribution is defined because \(\lambda>0\).

## Proof
**1. Orbit size and nonzero extension count.** Every rank-one matrix has an outer-product presentation \(u\alpha\) with nonzero column \(u\) and nonzero linear functional \(\alpha\), unique up to simultaneous inverse rescaling. The condition \((u\alpha)^2=0\) is exactly \(\alpha(u)=0\). There are \(P\) image lines and \(q^{n-1}-1=(q-1)H\) nonzero annihilating functionals after fixing one representative per image line, yielding \(N=(q-1)PH\). For any fixed rank-one \(A=u\alpha\), \(AB\ne0\) with \(B=v\beta\in\mathcal N\) if and only if \(\alpha(v)\ne0\). There are \(q^{n-1}\) projective lines not contained in \(\ker\alpha\), and each permits \((q-1)H\) choices of \(B\). Thus there are exactly \(\lambda=q^{n-1}(q-1)H=q^{n-1}(q^{n-1}-1)\) ways to extend any surviving product by one further factor without killing it. Consequently exactly \(N\lambda^{k-1}\) words survive, and \(F_k(0)=N^k-N\lambda^{k-1}\).

**2. Projective path reduction for one fixed nonzero target.** Fix \(Z=ab\ne0\), with nonzero column \(a\) and nonzero functional \(b\). In any nonzero product \(A_1\cdots A_k=Z\), the first factor's image is \(Ka\), and the last factor's row line is \(Kb\). For prescribed image lines \(L_1=Ka,L_2,\ldots,L_k\), fix nonzero vectors \(u_i\in L_i\) with \(u_1=a\). Write
\[
 A_i=u_i\alpha_i\ (1\le i<k),\qquad A_k=u_k\gamma b,
\]
where the functionals and \(\gamma\in K^\times\) are uniquely specified by the factors once the vectors have been fixed. The square-zero conditions are \(\alpha_i(u_i)=0\) for \(i<k\), and \(b(u_k)=0\). The product is \(Z\) exactly when
\[
 \gamma\,\alpha_1(u_2)\alpha_2(u_3)\cdots\alpha_{k-1}(u_k)=1.
\]
For fixed nonzero vector representatives at two consecutive projective points, a functional annihilating the first point and nonzero on the second exists precisely when the points are distinct, and there are exactly \(q^{n-2}(q-1)=t\) such functionals. The final row \(b\) restricts the last image point to the \(H\) projective points in \(\ker b\). For each allowed choice of the \(k-1\) functionals, the displayed equation uniquely determines \(\gamma\) as the inverse of their product of pairings. Thus the path has exactly \(t^{k-1}\) factorizations, with no rescaling still to divide out. Hence \(F_k(Z)=t^r\) times the number of length-\(r\) walks in the loopless complete graph on the \(P\) projective points, starting at \([a]\) and ending in the \(H\)-point hyperplane \(\mathbb P(\ker b)\).

**3. Exact projective path count.** The adjacency matrix of the loopless complete graph is \(J-I\), with eigenvalue \(P-1\) on constants and \(-1\) on the orthogonal complement. Its \(r\)-th power has entries
\[
((J-I)^r)_{xy}=\frac{(P-1)^r-(-1)^r}{P}+(-1)^r\mathbf1_{\{x=y\}}.
\]
Summation over the terminal hyperplane gives
\[
H\frac{(P-1)^r-(-1)^r}{P}+(-1)^r\mathbf1_{\{[a]\in\mathbb P(\ker b)\}}.
\]
Since \(b(a)=\operatorname{tr}Z\), this proves the displayed rank-one fiber formula. Rank at least two is impossible because each factor has rank one.

**4. Positivity and the sharp length obstruction.** At \(r=1\) the only failure occurs when \(H=1\) and the initial point is that sole terminal point: this means \(n=2\) and \(\operatorname{tr}Z=0\). For \(r=2\) every ordered pair of vertices of the complete graph has a walk of length two between them, by taking an intermediate vertex different from both endpoints; \(P\ge3\). Inductively, prepend an edge from the desired initial vertex to any other vertex, then take a walk of the preceding length from there to the desired terminal vertex. Hence every rank-one target occurs for every \(r\ge2\).

**5. Exact conditional mixing.** The number of nonzero rank-one targets is \(R=(q-1)P^2\). Of these exactly \(N=(q-1)PH\) have trace zero. Write \(d=(-t)^r\). The trace-zero fibers differ from the remaining rank-one fibers by exactly \(d\), and their weighted mean equals \(N\lambda^r/R\). Thus the absolute deviations of fibers from the mean are \(|d|(1-H/P)\) on the trace-zero targets and \(|d|H/P\) on the other targets. The half-sum of these deviations, divided by the surviving word count \(N\lambda^r\), equals
\[
\frac{|d|}{N\lambda^r}\frac{N(P-H)}{P}
=\frac{P-H}{P(P-1)^r},
\]
using \(\lambda=t(P-1)\). This proves the exact total-variation law and completes the proof.

## Verification
The standalone file `check_minimal_nilpotent_words.py` independently constructs all minimal-orbit elements from normalized outer products and performs literal finite-field matrix multiplication, including multiplication in \(\mathbb F_4\). It checks the formula for **every possible rank-one target** at each tested parameter, checks the exact zero fiber, excludes nonzero higher-rank targets, and verifies that the sum of target counts is \(N^k\). The accompanying `verification_output.txt` records `VERIFY_OK` after all tested cases. The configurations are \((n,q)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2)\) with respective word-length ranges \(2\)–\(6\), \(2\)–\(6\), \(2\)–\(5\), \(2\)–\(5\), \(2\)–\(5\), \(2\)–\(4\), \(2\)–\(3\), \(2\)–\(3\). Run `python3 check_minimal_nilpotent_words.py` with Python 3 and no third-party modules. These finite checks corroborate, but do not establish, the universal theorem independently of the proof.

## Relationship to prior work
The classical factorization literature of Wu and Sourour addresses existence of nilpotent factorizations of singular matrices. Sourour's historical manuscript explicitly observes that a nonzero nilpotent two-by-two matrix cannot be a product of two nilpotent matrices and can be a product of three. That qualitative result is credited, not claimed original. The published finite-field minimal-nilpotent-orbit result *Complete multiplication fibers of the minimal nonzero nilpotent orbit over finite fields* determines **exactly the two-factor fibers** and explicitly excludes longer products from its scope. Our formula specializes to those already known two-factor values; this is **not** a new two-factor census. The all-length rank-one *idempotent* matrix fiber result has three distinct trace strata because its factors have trace one; it neither counts the disjoint square-zero factor orbit nor implies its alternating-sign projective graph law. Kudryavtseva and Mazorchuk study the overall semigroup structure of matrices, while Britnell and Wildon study commuting nilpotent classes rather than prescribed ordered products of one minimal orbit. In the inspected sources, none supplies the exact full-length minimal-orbit fibers, the alternating trace discrepancy, or the exact conditional mixing distance.

## Limitations
Only the minimal nonzero nilpotent orbit is treated. There is no assertion about general nilpotent factors, prescribed multi-target noncommutative word maps, or powers with identical repeated factors. The length-three existence of every rank-one target is not novel as an existence phenomenon. The two-factor formula is already published; novelty is restricted to the global all-length extension and its projective-walk statistics. The primary-source and indexed literature comparisons do not independently certify global historical priority; earlier semigroup random-walk or matrix factorization works could contain equivalent formulas. The computational sample is finite and does not replace the proof.

## References
1. A. R. Sourour, *Nilpotent factorization of matrices*, University of Victoria departmental manuscript (dated November 1990); published in *Linear and Multilinear Algebra* **31** (1992), 303–308, DOI: `10.1080/03081089208818141`. Accessible primary manuscript: https://dspace.library.uvic.ca/bitstream/1828/2656/1/DMS%20566.pdf.
2. G. Kudryavtseva and V. Mazorchuk, *On the semigroup of square matrices*, arXiv:math/0510624 (first posted 2005-10-28). https://arxiv.org/abs/math/0510624.
3. J. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811 (first posted 2010-01-06). https://arxiv.org/abs/1001.0811.
4. *Complete multiplication fibers of the minimal nonzero nilpotent orbit over finite fields*, public mathematical result, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-complete-multiplication-fibers-of-the-minimal-nonzero-nilpotent--1bce20858de2.
5. *Exact all-arity product fibers of rank-one idempotents over finite fields*, public mathematical result, https://github.com/Resultary/2026/tree/main/2026/10/12/SCOPE-exact-all-arity-product-fibers-of-rank-one-idempotents-over-fini--dfb5f1d17166.
6. P.-Y. Wu, *Products of Nilpotent Matrices*, *Linear Algebra and its Applications* **96** (1987), 227–232, DOI: `10.1016/0024-3795(87)90346-6`.
