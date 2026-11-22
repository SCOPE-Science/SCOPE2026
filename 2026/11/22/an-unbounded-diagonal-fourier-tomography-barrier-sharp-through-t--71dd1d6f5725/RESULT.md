# An unbounded diagonal-Fourier tomography barrier, sharp through ten vertices

## Finding

Let \(n\ge4\) and let \(\mathcal T_n\) be the set of all triangulations of a convex polygon with labelled vertices \(0,1,\ldots,n-1\). Embed each triangulation in the Boolean cube of its \(n(n-3)/2\) possible internal diagonals. For \(d\ge0\), let \(V_{n,d}\) be the real span, on \(\mathcal T_n\), of all Walsh characters depending on at most \(d\) diagonal coordinates. Define the **tomography degree**
\[
\tau_n=\min\{d:V_{n,d}=\mathbb R^{\mathcal T_n}\}.
\]
Then
\[
\boxed{\tau_n\ge\left\lfloor\frac{n-2}{2}\right\rfloor\quad(n\ge4),\qquad
\tau_n=\left\lfloor\frac{n-2}{2}\right\rfloor\quad(4\le n\le10).}
\]
Consequently the joint probabilities of the presence of at most \(\tau_n\) specified diagonals identify every probability distribution on \(\mathcal T_n\) when \(4\le n\le10\); at any smaller degree two distinct probability distributions are indistinguishable. For arbitrary \(n\ge4\), such distributions are explicitly constructed whenever fewer than \(\lfloor(n-2)/2\rfloor\) diagonals may be queried jointly.

| Polygon vertices \(n\) | Triangulations \(|\mathcal T_n|\) | Exact least observation degree \(\tau_n\) |
|---:|---:|---:|
| 4 | 2 | 1 |
| 5 | 5 | 1 |
| 6 | 14 | 2 |
| 7 | 42 | 2 |
| 8 | 132 | 3 |
| 9 | 429 | 3 |
| 10 | 1430 | 4 |

## Assumptions and scope

All vertices and all diagonals are labelled. A polygon triangulation consists of exactly \(n-3\) pairwise noncrossing internal diagonals. A diagonal means a pair of nonadjacent vertices, excluding the boundary pair \((0,n-1)\). Put \(x_e(T)=\mathbf1_{\{e\in T\}}\). For a set \(F\) of internal diagonals let
\[
\chi_F(T)=\prod_{e\in F}(-1)^{x_e(T)},\qquad
m_F(T)=\prod_{e\in F}x_e(T).
\]
The spaces spanned by \(\chi_F\) and \(m_F\) for \(|F|\le d\) are identical over \(\mathbb R\), because \(\chi_e=1-2x_e\) and \(x_e=(1-\chi_e)/2\). Query data are probabilities of joint presence of \(F\), including \(F=\varnothing\), with no assumption that the distribution is uniform. The statement does not concern recovering a single unknown deterministic triangulation from adaptive queries or recovering probabilities from noisy observations.

## Proof

**An obstruction for every polygon size.** Set \(r=\lfloor(n-2)/2\rfloor\) and start with the fan triangulation whose diagonals are \((0,2),(0,3),\ldots,(0,n-2)\). Independently flip the \(r\) diagonals
\[
(0,2j)\longleftrightarrow(2j-1,2j+1),\qquad 1\le j\le r.
\]
These flips occupy distinct quadrilaterals in the fan; the replacement diagonals are mutually noncrossing and compatible with every unflipped fan diagonal. Thus every Boolean choice \(\varepsilon\in\{0,1\}^{r}\) yields a distinct triangulation \(T_\varepsilon\). On these \(2^r\) triangulations, each diagonal-presence indicator is constant, \(\varepsilon_j\), or \(1-\varepsilon_j\) for some \(j\). Therefore the restriction of any degree-at-most-\(r-1\) presence monomial is a multilinear polynomial in the flip bits of degree at most \(r-1\). Hence
\[
\sum_{\varepsilon\in\{0,1\}^r}(-1)^{\varepsilon_1+\cdots+\varepsilon_r}m_F(T_\varepsilon)=0\quad\text{whenever }|F|<r.
\]
The signed vector is nonzero and annihilates all degree-below-\(r\) Walsh data. Equivalently, let \(\mu_+\) and \(\mu_-\) be uniform distributions on the \(2^{r-1}\) even- and odd-parity flip choices. They agree on every joint presence event involving fewer than \(r\) diagonals. For the event consisting of all \(r\) replacement diagonals, precisely one flip choice qualifies, so the two event probabilities differ by \(2^{1-r}\). This proves \(\tau_n\ge r\).

**Finite sharpness through ten vertices.** For \(4\le n\le10\), construct the \(0/1\) matrix \(M_{n,r}\) with rows indexed by all polygon triangulations \(T\), columns indexed by all noncrossing diagonal sets \(F\) with \(|F|\le r\), and entries \(m_F(T)\). The accompanying standalone program `verify_recursive.py` enumerates the triangulations recursively by the unique triangle incident with the boundary edge of an interval, then uses exact bit-vector Gaussian elimination over \(\mathbb F_2\). It establishes
\[
\operatorname{rank}_{\mathbb F_2} M_{n,r}=|\mathcal T_n|=\frac1{n-1}\binom{2n-4}{n-2}
\quad\text{for each }n=4,5,6,7,8,9,10.
\]
A second standalone program, `verify_flips.py`, independently generates triangulations by all legal diagonal flips, checks their Catalan counts, and obtains the same full row rank from an independently indexed row-wise incidence matrix. The exact pivot computations are exhaustive, not a sample. Since an integer minor whose determinant is nonzero modulo two is nonzero over \(\mathbb Q\), the real matrix \(M_{n,r}\) has full row rank. The monomial/Walsh span equivalence gives \(V_{n,r}=\mathbb R^{\mathcal T_n}\). Combined with the obstruction, this gives equality in the stated finite range.

**Recovery interpretation.** If the columns of \(M_{n,d}\) span \(\mathbb R^{\mathcal T_n}\), the vector of all marginal probabilities \(\sum_T\mu(T)m_F(T)\) uniquely determines an arbitrary signed measure and hence any probability distribution \(\mu\). If the columns do not span, the parity contrast above produces two genuine, positive, distinct probability distributions with identical marginal data. Thus the algebraic ranks give precisely the nonparametric identifiability threshold claimed.

## Verification

The two complete verifier sources accompany this document and use only the Python standard library. Run `python3 verify_recursive.py` and `python3 verify_flips.py`. The recursive verifier prints the exact modulo-two rank progressions, respectively
\[
\begin{array}{c|l}
 n&\text{ranks through }\lfloor(n-2)/2\rfloor\\\hline
4&(1,2)\\5&(1,5)\\6&(1,9,14)\\7&(1,14,42)\\8&(1,20,100,132)\\9&(1,27,198,429)\\10&(1,35,350,1195,1430).
\end{array}
\]
These are ranks *modulo two*, not asserted exact real ranks at every intermediate degree; only the final full-rank entries are used for the real-rank proof. The flip-graph verifier separately checks both full-rank endpoints and the explicit parity-cube cancellation for all eligible small polygons. The included code and its invariant assertions are the finite proof certificates; transcript logs alone are not used as evidence.

## Relationship to prior work

The identification of triangulations with maximal noncrossing diagonal sets and the associahedron's face structure is classical; see Devadoss, Shah, Shao and Winston (2009), and Dochtermann (2015). Dochtermann counts faces and studies resolutions of the Stanley–Reisner ideal of a cycle, not ranks of the face-to-facet evaluation matrix. De Loera, Hoşten, Santos and Sturmfels (1996) describe affine spans of incidence-vector polytopes of triangulations, using triangle coordinates and linear equations; this is not the full hierarchy of arbitrary-distribution diagonal-marginal identifiability. The present statement concerns exact Walsh interaction degree and a parity-cube obstruction; neither the standard Catalan counts nor the full associahedron face vector alone implies its finite full-rank assertions.

## Limitations

The matching upper bound is proved here only for \(4\le n\le10\). For \(n\ge11\) the theorem supplies a lower bound, not an assertion of equality. It does not give a sharp noise-stability or conditioning constant, a description of all low-degree null vectors, or all real intermediate ranks. The existence of an equivalent result in a difficult-to-search historical face-incidence literature cannot be excluded by indexed search alone. Independent expert assessment has not been performed.

## References

- S. L. Devadoss, R. Shah, X. Shao, E. Winston, *Visibility graphs and deformations of associahedra*, arXiv:0903.2848, first posted 2009-03-16. https://arxiv.org/abs/0903.2848
- A. Dochtermann, *Face rings of cycles, associahedra, and standard Young tableaux*, arXiv:1503.06243, first posted 2015-03-20. https://arxiv.org/abs/1503.06243
- J. A. de Loera, S. Hoşten, F. Santos, B. Sturmfels, *The polytope of all triangulations of a point configuration*, Documenta Mathematica 1 (1996), 103–119. https://doi.org/10.4171/DM/4
