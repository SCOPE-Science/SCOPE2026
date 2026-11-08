# A period-two Ehrhart law for bounded three-point tropical idempotents

## Finding
Let \(m\) be any nonnegative integer. Consider \(3\times3\) matrices \(D\) whose diagonal entries are zero and whose six off-diagonal entries belong to \(\{0,1,\ldots,m\}\). Their product is the min-plus matrix product \((D\otimes D)_{ij}=\min_k(d_{ik}+d_{kj})\). The number \(N(m)\) satisfying \(D\otimes D=D\) is exactly
\[
N(m)=\frac{54m^6+324m^5+875m^4+1340m^3+1236m^2+656m+160-5\mathbf1_{m\text{ odd}}}{160}.
\]
The first values for \(m=0,1,\ldots,8\) are \(1,29,281,1490,5533,16281,40693,90152,182045\). The function has **minimal quasipolynomial period two** and leading term \((27/80)m^6\). Equivalently, it enumerates integer directed semimetrics with a bounded edge alphabet on three distinctly labeled points; zero off-diagonal distances are allowed.

## Assumptions and scope
Use the min-plus convention \(a\oplus b=\min(a,b)\), \(a\otimes b=a+b\), applied to finite nonnegative integer entries. Bounded entries form a **slice** of the full tropical matrix monoid, not a submonoid: products need not remain bounded. There are no unlabeled identifications, symmetry requirements, strict positivity assumptions, or unrestricted-diagonal assertions.

## Proof
**1. Triangle characterization.** Write the off-diagonal entries in the order
\[(x,y,u,v,s,t)=(d_{12},d_{21},d_{13},d_{31},d_{23},d_{32}).\]
With zero diagonal and nonnegative entries, tropical idempotency is equivalent to the six directed triangle inequalities
\[
 x\le u+t,\quad y\le s+v,\quad u\le x+s,\quad v\le t+y,\quad s\le y+u,\quad t\le v+x.
\]
This is the established tropical-idempotent/directed-distance correspondence, not a new lemma. Together with the box inequalities \(0\le x,y,u,v,s,t\le m\), these define \(mP\) for a fixed rational polytope \(P\subset\mathbb R^6\). The point having all six coordinates \(1/2\) satisfies every inequality strictly except none of them: \(P\) therefore has dimension six.

**2. A complete exact vertex certificate.** The polytope \(P\) has 18 explicitly listed inequalities, twelve box bounds and six triangle bounds. Every vertex is the unique intersection of at least six linearly independent active facets. Exhausting all \(\binom{18}{6}=18564\) choices of six boundaries, solving each nonsingular system exactly over the rationals, and retaining precisely solutions satisfying all 18 inequalities produces **31 distinct vertices**, exactly **29 integral** and **two with denominator two** (for example \((1,1/2,1/2,1,1,1/2)\)). No other vertices can occur, because each six-dimensional vertex has six independent active constraints. The full finite certificate is replayed by the bundled standard-library program `verify.py`, which does rational Gaussian elimination and tests all candidate bases, with no floating-point filtering or external dependencies.

**3. Ehrhart interpolation.** As every vertex of \(P\) belongs to \((\tfrac12\mathbb Z)^6\), the rational Ehrhart theorem shows that \(N(m)=\#(mP\cap\mathbb Z^6)\) is a degree-six quasipolynomial whose period divides two. To evaluate the seven coefficients in each parity class, fix \(x,y,u,v\in\{0,\ldots,m\}\) and count the independently admissible values of \(s\) and \(t\):
\[
\begin{aligned}
 s_{\min}&=\max(0,u-x,y-v),&s_{\max}&=\min(m,y+u),\\
 t_{\min}&=\max(0,x-u,v-y),&t_{\max}&=\min(m,v+x).
\end{aligned}
\]
Define \([z]_+=\max(z,0)\). The **exact**, finite four-variable summation is
\[
N(m)=\sum_{x,y,u,v=0}^{m}[s_{\max}-s_{\min}+1]_+[t_{\max}-t_{\min}+1]_+.
\]
Evaluating this sum at the seven even values \(m=0,2,4,6,8,10,12\) and seven odd values \(m=1,3,5,7,9,11,13\), and interpolating the unique degree-at-most-six polynomials in each class, gives
\[
N(2j)=\left.\frac{54m^6+324m^5+875m^4+1340m^3+1236m^2+656m+160}{160}\right|_{m=2j},
\]
\[
N(2j+1)=\left.\frac{54m^6+324m^5+875m^4+1340m^3+1236m^2+656m+155}{160}\right|_{m=2j+1}.
\]
Since both constituent polynomials agree with seven exact counts, Ehrhart's degree and period bounds prove these formulas for **all** nonnegative integers \(m\), not merely the interpolated range. Their constant terms differ by \(1/32\), so the minimum period is two. The coefficient of \(m^6\) is \(54/160=27/80\).

## Verification
Execute `python3 verify.py`. The program checks all \(18564\) six-facet choices by exact rational arithmetic, identifies the 31 vertices and their denominators, independently evaluates the four-variable count for every \(0\le m\le19\), and matches the claimed closed formula. On completion it prints `VERIFY_OK`. The all-size theorem relies on the rational Ehrhart theorem and complete vertex certificate; the finite computations at \(m\le19\) are not extrapolated into an infinite claim. The first 14 evaluations are sufficient for interpolation once the period-two and degree-six certificate is established.

## Relationship to prior work
Johnson and Kambites (arXiv:1203.2480, §4, Lemma 4.1) prove the general equivalence between diagonal-zero tropical idempotents and functions obeying triangle inequalities; their article studies tropical geometry of metric spaces and their maximal matrix subgroups, rather than the bounded integer three-point enumerator. Aird (arXiv:2201.12166v1, first posted 28 January 2022) studies generators, finite presentations and growth of tropical matrix monoids. Those structural results motivate this exact bounded-entry idempotent census but do not state this six-dimensional lattice-point quasipolynomial. The result is not asserted to be the first study of directed metric polytopes in general; specialized earlier enumeration under other terminology remains a publication-priority risk.

## Limitations
The formula concerns fixed matrix size three, zero diagonal, integral off-diagonal entries bounded above, including possible zero distances. The bounded slice is not closed under multiplication. No claim about size four or higher, orbit counts under relabeling, semimetric separation, or a geometric classification beyond the specified vertex computation is made. Independent mathematical audit and exhaustive publication-priority verification have not been performed.

## References
1. T. Aird, *Generating sets, presentations, and growth of tropical matrix monoids*, arXiv:2201.12166, first submitted 2022-01-28, https://arxiv.org/abs/2201.12166. Relevant §§1, 4–6.
2. M. Johnson and M. Kambites, *Idempotent tropical matrices and finite metric spaces*, arXiv:1203.2480, first submitted 2012-03-12, https://arxiv.org/abs/1203.2480. Relevant §4, especially Lemma 4.1.
3. Standard rational Ehrhart theorem for lattice-point counts in integral dilates of rational polytopes, used here only after the complete vertex-denominator certificate.
