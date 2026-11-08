# Counting every minimum Italian dominating function on cyclic prisms

## Finding

For each integer \(n\ge3\), let \(\Pi_n=C_n\square K_2\), with vertices \((r,i)\) for \(r\in\{0,1\}\) and \(i\in\mathbb Z/n\mathbb Z\), horizontal edges within each row and one vertical edge in every column. An Italian dominating function is \(f:V(\Pi_n)\to\{0,1,2\}\) such that every zero-labelled vertex has neighbour-label sum at least \(2\). Its weight is the sum of its labels.

The minimum weight is \(n\) (previously known). Let \(N_n\) denote the **number of labelled functions** attaining that minimum; rotating or reflecting columns or exchanging rows does **not** identify functions. Define

\[
P(z)=(1+z)(1+z^2-z^3+z^4)(1-z-z^2-z^5)(1-z^4)(1-z^2).
\]

Then the complete minimum-function enumeration for every \(n\ge3\) is

\[
\boxed{N_n=-[z^n]z\,\frac{P'(z)}{P(z)}.}
\]

Equivalently, \(\sum_{n\ge3}N_nz^n=-zP'(z)/P(z)-4z^2\). The first values, for \(n=3,4,\ldots,12\), are \(6,12,10,34,42,68,132,214,330,630\).

If \(\lambda=1.704902776\ldots\) is the unique positive root of \(x^5-x^4-x^3-1\), then

\[
\boxed{N_n\sim\lambda^n\quad(n\to\infty).}
\]

Thus a graph family with known, exactly linear Italian domination number has exponentially many minimum functions, with a precise algebraic growth constant. These statements count the full optimum layer, not all Italian dominating functions.

## Assumptions and scope

Graphs are finite, undirected and simple; \(n\ge3\), so \(C_n\) is an ordinary cycle. Columns are individually labelled by their elements of \(\mathbb Z/n\mathbb Z\). The upper/lower rows are named. All generating-series identities are in formal power series over \(\mathbb Q\). No quotient by graph automorphisms is taken.

## Proof

**1. Local transfer bijection.** Encode a column \((a,b)\in\{0,1,2\}^2\) by \(s=3a+b\), so there are nine column symbols \(0,\ldots,8\). For column states \(i,j,k\), write \(i=(a,b)\), \(j=(c,d)\), \(k=(e,g)\). The middle column is Italian-dominated if and only if

\[
(c>0\ \text{or}\ a+d+e\ge2)\quad\text{and}\quad
(d>0\ \text{or}\ b+c+g\ge2).
\]

Build a directed graph on the 81 ordered pairs \((i,j)\), placing an edge \((i,j)\to(j,k)\) exactly when this condition holds. Give that edge cost \(c+d-1\). Closed walks of length \(n\) are in bijection with Italian functions on \(\Pi_n\), and the total edge cost of the walk is the function's weight minus \(n\). The bijection is exact also for \(n=3\), since its two cyclic neighbours are distinct.

**2. Explicit nonnegative reduced costs.** Put the following integer potential on the 81 states:

\[
h(i,j)=\begin{cases}
-2,&i=0,\ j\in\{5,7,8\},\\
-1,&i=0,\ j\notin\{5,7,8\},\\
-1,&i\in\{1,3\},\\
0,&i\in\{2,4,5,6,7,8\}.
\end{cases}
\]

For every permitted edge \(u=(i,j)\to v=(j,k)\), direct substitution of the nine column symbols shows

\[
(c+d-1)+h(u)-h(v)\ge0.
\]

There are 666 permitted edges among the 729 possible triples; the full integer inequality is checked exhaustively in `artifacts/verify.py`. Summing around any closed walk telescopes the potential. Hence every Italian dominating function has weight at least \(n\), and equality holds exactly when **every** edge of its closed walk has reduced cost zero.

To demonstrate attainability for all \(n\ge3\), choose one label \(1\) per column, alternating its row except for one repeated choice if \(n\) is odd. Equivalently, choose a cyclic binary word with no three consecutive symbols equal. Each zero vertex then sees the vertical \(1\) and at least one horizontal \(1\), so this is an Italian dominating function of weight \(n\).

**3. Complete critical-graph census.** Retain only edges of reduced cost zero. The resulting directed graph has 81 vertices and 161 edges. A complete strongly-connected-component computation shows that its only components containing directed cycles have respectively 12, 4 and 2 states. All other components contain no directed cycle and therefore cannot support a closed walk.

A fully reproducible description of the nontrivial 12-state component is given by the following order of state labels (indices from 0 to 11):

```text
(0,1) (0,3) (0,5) (0,7) (1,0) (1,1)
(1,3) (3,0) (3,1) (3,3) (5,0) (7,0)
```

Its internal directed edges, in those indices, are precisely

```text
0: 6       1: 8        2: 10       3: 11
4: 3       5: 6        6: 7,8,9    7: 2
8: 4,5,6   9: 8       10: 1       11: 0
```

The 4-state component, in the order \((0,2),(0,6),(2,0),(6,0)\), has edges \(0\to2\to1\to3\to0\); the 2-state component \((0,4),(4,0)\) is a directed 2-cycle. These lists may be checked directly from the rules in Steps 1–2, independently of any numerical extrapolation. In particular, they give the **complete** cyclic language of optimal configurations for arbitrary length.

**4. Trace and rational series.** Let \(A_{12},A_4,A_2\) be the three component adjacency matrices. The labelled cyclic-walk correspondence and the absence of other cyclic components give

\[
N_n=\operatorname{tr}(A_{12}^n)+\operatorname{tr}(A_4^n)+\operatorname{tr}(A_2^n).
\]

Exact determinant computations on the displayed finite matrices give

\[
\begin{aligned}
\det(I-zA_{12})&=(1+z)(1+z^2-z^3+z^4)(1-z-z^2-z^5),\\
\det(I-zA_4)&=1-z^4,\\
\det(I-zA_2)&=1-z^2.
\end{aligned}
\]

For every finite matrix \(A\), the formal identity
\(\sum_{n\ge1}\operatorname{tr}(A^n)z^n=-z\,\frac{d}{dz}\log\det(I-zA)\)
proves the claimed coefficient formula. Its coefficients at orders 1 and 2 are \(0\) and \(4\), so subtracting \(4z^2\) gives the series starting at the physically defined \(n=3\).

**5. Asymptotic.** The 12-state component is strongly connected and has directed cycles of lengths 2 and 3, so its adjacency matrix is primitive. Its characteristic polynomial is

\[
x^2(x+1)(x^4+x^2-x+1)(x^5-x^4-x^3-1).
\]

The positive Perron eigenvalue cannot come from \(x+1\) or the quartic (which is positive on nonnegative real inputs); it is therefore the unique positive root \(\lambda\) of the quintic (uniqueness follows from Descartes' rule). The two smaller cyclic components have only roots of unity. Since \(\lambda>1\) and the 12-state matrix is primitive, every other eigenvalue of the three components has modulus strictly smaller than \(\lambda\). As the trace counts each simple dominant eigenvalue once, \(N_n\sim\lambda^n\).

## Verification

`artifacts/verify.py` is a standalone Python 3 standard-library checker. Run `python3 artifacts/verify.py` from the directory containing `artifacts`. It independently enumerates all 81 states and 666 permitted edges, checks the potential inequality, constructs all 161 critical edges, computes strong components, determines component determinants by exact integer Newton identities, and compares matrix traces with labelled graph brute force for \(n=3,4,5,6\). It checks 40 trace coefficients and additional binary-word witnesses. Its output ends in `VERIFY_OK`.

The infinite statement follows from the finite directed-graph reduction plus the exact determinant and Perron–Frobenius arguments; direct enumeration through \(n=6\) alone is not a proof for all \(n\).

## Relationship to prior work

Gardner's 2018 thesis, Theorem 3.13 in the prism section, already gives \(\gamma_I(C_n\square K_2)=n\). The present result does **not** claim that minimum value. It refines the known optimum weight to a complete count, rational series, and exponential asymptotic. Shao and Zhao's 2026 paper introduces systematic coefficient counting for Italian domination on paths, trees and cycles and motivates the weight-enumeration viewpoint; inspection of its complete open-access HTML (Sections 1–9 and references) confirms that it does not treat cyclic-prism optimum counts or the critical-state formula. Ordinary, perfect, total, covering and edge versions of Italian domination impose different local rules and are not interchangeable. Searches did not locate an equivalent cyclic-prism minimum-function enumerator; the priority assessment remains provisional.

## Limitations

The result concerns ordinary cyclic prisms \(C_n\square K_2\) with \(n\ge3\), not Möbius ladders, open ladders, wider cylinders, arbitrary prism graphs, or automorphism orbits. It counts minimum functions only. The motivating 2026 preprint was inspected through its open-access full HTML, as was the directly relevant 2018 thesis prism section. An unindexed equivalent older enumeration remains possible; historical priority is provisional. Verification is not independent mathematical certification.

## References

1. P. Shao and C. Zhao, *Counting Weight-\(k\) Italian Dominating Sets on Trees and Cycles*, arXiv:2610.00108v1, first public version dated 2026-09-09. https://arxiv.org/html/2610.00108v1
2. K. B. Gardner, *Italian Domination on Ladders and Related Products*, Master's thesis, East Tennessee State University, 2018, especially §3.3 and Theorem 3.13. https://fileserver-az.core.ac.uk/download/pdf/214087077.pdf
3. A. Almulhim, B. Al Subaiei and S. R. Mondal, *Survey on Roman \(\{2\}\)-Domination*, Mathematics 12 (2024), article 2771. https://www.mdpi.com/2227-7390/12/17/2771
