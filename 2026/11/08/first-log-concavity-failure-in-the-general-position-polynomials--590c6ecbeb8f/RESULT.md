# First log-concavity failure in general-position polynomials of triangular graphs

## Finding

Let \(T_n=J(n,2)=L(K_n)\) for every integer \(n\ge3\), and let \(\psi_n(z)=\sum_j a_{n,j}z^j\) count its **general-position sets**: sets of vertices such that no geodesic contains three chosen vertices. A nonnegative coefficient sequence is log-concave if \(a_{n,j}^{2}\ge a_{n,j-1}a_{n,j+1}\) for every interior index.

**Finite sharp transition.** Every \(\psi_n\) with \(3\le n\le29\) is log-concave, but \(\psi_{30}\) is not. Its unique failing index is \(j=29\). Exact coefficients are
\[
\begin{aligned}
a_{30,28}&=4575989857607826108600,\\
a_{30,29}&=73770312933671827650,\\
a_{30,30}&=1208883745669600000.
\end{aligned}
\]
Thus \(a_{30,28}a_{30,30}-a_{30,29}^{2}=89780688879179441682809722027255477500>0\). The notation \(T_{30}\) refers to the triangular graph on \(\binom{30}{2}=435\) vertices, not a graph on thirty vertices.

## Assumptions and scope

All graphs are finite, simple, and undirected. A vertex of \(T_n\) is an edge of the complete graph on \(n\) labeled vertices; two such vertices are adjacent if the original edges share an endpoint. The polynomial includes the empty set. The theorem proves log-concavity for the finite range \(3\le n\le29\), and gives the first failure within the natural sequence at \(n=30\). It does **not** assert failure for all subsequent \(n\).

## Proof

**Step 1: admissible components.** For \(n\ge4\), the triangular graph has diameter two. A vertex subset is in general position precisely when its induced graph has no induced three-vertex path: if two selected vertices at distance two share a selected common neighbor, the three lie on a geodesic, and every geodesic of length two has this form. For \(n=3\), the graph is complete and the same characterization holds. Hence its selected subgraph is a disjoint union of cliques. The original chosen edges of \(K_n\) therefore form vertex-disjoint components, each consisting of either a single isolated original vertex, an isolated edge, a star of order at least three, or a triangle. Indeed, a pairwise-intersecting family of at least three distinct edges either shares a common endpoint or forms all three sides of a triangle. These component types are mutually disjoint as *selected edge sets*; a two-edge path is counted among stars, not triangles.

**Step 2: exact all-set recurrence.** Write \(A_n(z)=\psi_n(z)\), with \(A_0(z)=1\) and coefficients \(a_{n,j}\). Condition on the component containing original vertex 1. If it is isolated, the contribution is \(A_{n-1}\). If it is an isolated edge, choose its other vertex in \(n-1\) ways, contributing \((n-1)zA_{n-2}\). A star on \(s\ge3\) original vertices can be chosen by selecting its other \(s-1\) vertices and its center, giving \(s\binom{n-1}{s-1}z^{s-1}A_{n-s}\). A triangle component containing vertex 1 contributes \(\binom{n-1}{2}z^3A_{n-3}\). Therefore, for all \(n\ge1\), with terms omitted if their index is negative,
\[
A_n(z)=A_{n-1}(z)+(n-1)zA_{n-2}(z)+\sum_{s=3}^n s\binom{n-1}{s-1}z^{s-1}A_{n-s}(z)+\binom{n-1}{2}z^3A_{n-3}(z).
\]
Every possible chosen edge set has exactly one component containing vertex 1, so the recurrence has neither missing cases nor duplicates.

**Step 3: independent coefficient identity.** The exponential formula for labeled components gives
\[
\sum_{n\ge0}\frac{A_n(z)x^n}{n!}
=\exp\!\left(x+\frac{zx^2}{2}+x(e^{zx}-1-zx)+\frac{z^3x^3}{6}\right).
\]
Set \(x=t/z\) formally as a Laurent-series substitution and collect the exponent:
\[
\exp\left(\frac{t^3}{6}+z^{-1}B(t)\right),
\qquad B(t)=te^t-\frac{t^2}{2}.
\]
Extracting the \(t^n z^{-d}\) term proves, for all integers \(0\le d\le n\),
\[
\boxed{a_{n,n-d}=\frac{n!}{d!}[t^n]\exp(t^3/6)B(t)^d.}
\]
The right-hand side is a finite, rational, exactly computable coefficient: \(B(t)\) has coefficient \(1\) at \(t\), \(1/2\) at \(t^2\), and \(1/(r-1)!\) at every \(t^r\), \(r\ge3\).

**Step 4: exact finite certificate.** The accompanying executable `verify.py` implements the component recurrence with unbounded Python integers, independently computes the coefficient identity via rational truncated power series, and checks agreement for every \(0\le n\le30\). It then evaluates all integer comparisons \(a_{n,j}^2\ge a_{n,j-1}a_{n,j+1}\) for every interior \(j\) and each \(3\le n\le29\), and verifies that the only negative comparison at \(n=30\) is \(j=29\). In addition it independently enumerates all subsets of \(V(T_n)\) for \(n=3,4,5,6\) and checks their general-position property directly against the coefficients. The integer values displayed above are exact; the positive product defect proves failure at \(T_{30}\). As the loops cover the explicitly specified finite domains using exact arithmetic, this is a finite exhaustive proof of the cutoff, not a statistical inference.

## Verification

Run `python3 verify.py` under Python 3 (standard library only). The script tests \(33,864\) direct vertex subsets across \(n=3,4,5,6\), as well as two exact polynomial computations through \(n=30\). Its expected success line begins `VERIFY_OK n=3..30`. All calculations use arbitrary-precision integers or `fractions.Fraction`; there is no floating-point thresholding. The checks establish a finite property, not a statement about infinitely many future orders.

## Relationship to prior work

Iršič, Klavžar, Rus, and Tuite (arXiv:2401.05696, first posted January 11, 2024) introduce general-position polynomials and investigate unimodality for several graph classes, notably Kneser graphs. Di Stefano, Klavžar, Krishnakumar, Tuite, and Yero (arXiv:2306.09965, June 16, 2023), Theorem 5.2, determine the **minimum size of maximal** general-position sets in line graphs of complete graphs; its proof gives the star/triangle maximal-set structure. Klavžar, Krishnakumar, Tuite, and Yero (arXiv:2209.12631, September 26, 2022), Theorem 3.2, determine **mobile** general-position numbers of these line graphs. These prior results supply useful context, but neither the general-position coefficient sequence nor the finite log-concavity boundary \(T_{30}\) follows immediately from their stated numeric extremal results. The admissible-component structure is standard and **not** claimed as new.

## Limitations

This theorem gives the first failing triangular graph among \(3\le n\le30\). No global sharp threshold, eventual failure theorem, or unimodality assertion for all orders is established. Publication priority remains provisional; a differently indexed prior coefficient computation could exist. The arithmetic is self-contained and reproducible but independent mathematical audit has not been performed.

## References

- V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, arXiv:2401.05696 (first posted 2024-01-11), https://arxiv.org/abs/2401.05696.
- G. Di Stefano, S. Klavžar, A. Krishnakumar, J. Tuite, I. G. Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965 (first posted 2023-06-16), https://arxiv.org/abs/2306.09965.
- S. Klavžar, A. Krishnakumar, J. Tuite, I. G. Yero, *Traversing a Graph in General Position*, arXiv:2209.12631 (first posted 2022-09-26), https://arxiv.org/abs/2209.12631.
