# Five vertices are sharp for reentrant positivity in graph biharmonic resolvents

## Finding
For a finite connected simple unweighted graph \(G\), let \(L_G=D-A\) be its combinatorial graph Laplacian and define the biharmonic backward-Euler resolvent
\[
R_G(h)=(I+hL_G^2)^{-1},\qquad h\geq0.
\]
**The smallest graph order at which an off-diagonal entry of \(R_G(h)\) can have the sign pattern positive, negative, positive at three strictly increasing positive values of \(h\) is five.** No connected simple graph on at most four vertices has such a reentrant entry.

The unweighted five-vertex path \(P_5\), with vertices \(0,1,2,3,4\) in path order, realizes this obstruction at its two endpoints:
\[
(R_{P_5}(h))_{0,4}=\frac{h^2(5h^2-21h+1)}{(h^2+7h+1)(25h^2+15h+1)}.
\]
Set \(h_{\pm}=(21\pm\sqrt{421})/10\). Then this entry is strictly positive for \(0<h<h_-\) and \(h>h_+\), strictly negative for \(h_-<h<h_+\), and zero at the two endpoints. Moreover the **entire matrix** is entrywise nonnegative precisely for
\[
\boxed{h=0\quad\text{or}\quad h\geq h_+.}
\]
For \(h>h_+\), every entry is strictly positive. In particular the entrywise positivity-restoration threshold is \(h_+\), even though the endpoint-to-endpoint transfer is positive at arbitrarily small steps.

## Assumptions and scope
The graph is finite, undirected, connected, unweighted, without loops or multiple edges, with its counting-measure Laplacian \(L_G=D-A\). All matrices are real; \(h\) is a real nonnegative scale. Strict reentrance of one entry means existence of \(0<h_1<h_2<h_3\) at which that entry is respectively positive, negative, and positive. The assertion concerns the resolvent \((I+hL_G^2)^{-1}\), **not** the heat semigroup \(e^{-hL_G^2}\) or the distinct Padé filter \((I+hL_G+h^2L_G^2/2)^{-1}\).

## Proof
**1. Positive denominators.** Since \(L_G\) is symmetric positive semidefinite, the eigenvalues of \(I+hL_G^2\) are \(1+h\lambda_j^2\), all strictly positive for every \(h\geq0\). Therefore its determinant is positive, and every resolvent entry has the same sign as its corresponding polynomial cofactor, i.e. the numerator of the adjugate entry. Every diagonal resolvent entry is strictly positive for \(h\geq0\) by the positive-definite inverse.

**2. Exact exhaustive small-order certificate.** There is one connected simple graph on two vertices, two on three vertices (path and triangle), and six on four vertices (two trees, two four-edge graphs, the five-edge diamond, and the six-edge complete graph). This classification follows immediately by edge counts: three-edge graphs are a star or a path; four-edge graphs are a four-cycle or a triangle with a pendant; five and six edges uniquely specify the diamond and complete graph. On one vertex the only matrix entry is diagonal.

For each of these nine graph isomorphism types, all off-diagonal cofactor numerators not listed in the final column below are **strictly positive for every \(h>0\)**. In the final column we list every possible sign-changing off-diagonal numerator up to graph automorphism. All displayed positive factors have the sign of the final parenthesized factor.

| Graph | \(\det(I+hL_G^2)\) | Potentially sign-changing off-diagonal cofactors |
|---|---|---|
| \(P_2\) | \(4h+1\) | none |
| \(P_3\) | \((h+1)(9h+1)\) | \(h(3h-1)\) |
| \(K_3\) | \((9h+1)^2\) | none |
| \(P_4\) | \((4h+1)(4h^2+12h+1)\) | \(h(4h^2+4h-1)\); \(2h^2(2h-3)\) |
| \(K_{1,3}\) | \((h+1)^2(16h+1)\) | \(h(h+1)(4h-1)\) |
| \(C_4\) | \((4h+1)^2(16h+1)\) | \(2h(4h+1)(8h-1)\) |
| paw (triangle with pendant) | \((h+1)(9h+1)(16h+1)\) | \(h(4h-1)(9h+1)\) |
| diamond (\(K_4\) minus one edge) | \((4h+1)(16h+1)^2\) | \(2h(8h-1)(16h+1)\) |
| \(K_4\) | \((16h+1)^3\) | none |

All other cofactor numerators have nonnegative coefficients and a positive coefficient at some positive power of \(h\), as verified by direct adjugate multiplication. The complete exact expressions and all nine adjacency lists are reproduced and checked independently by `checker.py`; no floating-point enumeration is invoked. Each listed sign-changing numerator has exactly **one** positive root, because its only factor with a negative constant has a strictly positive derivative on \(h\geq0\). Hence its sign cannot be positive, then negative, then positive as \(h\) increases. This proves the order-four impossibility by exact finite classification, not numerical sampling.

**3. Five-path witness.** For \(P_5\), compute \(M(h)=I+hL_{P_5}^2\) with edges \(01,12,23,34\). Direct determinant expansion gives
\[
D(h)=\det M(h)=(h^2+7h+1)(25h^2+15h+1).
\]
The cofactor of row \(4\), column \(0\) is \(h^2(5h^2-21h+1)\). Its quadratic has exactly two distinct positive roots \(h_{\pm}\). As its leading coefficient and constant term are positive, its sign is positive outside the two roots and negative strictly between them. Thus the claimed reentrant entry exists and the order cutoff is sharp.

**4. Entire-matrix positivity on \(P_5\).** By reflection symmetry, all distinct off-diagonal numerators, up to reflected vertex pairs, are exactly
\[
\begin{aligned}
(0,1):&\ h(5h^3+74h^2+38h+3),\\
(0,2):&\ h(5h-1)(h^2+7h+1),\\
(0,3):&\ h^2(5h^2-h-7),\\
(0,4):&\ h^2(5h^2-21h+1),\\
(1,2):&\ h(5h+4)(h^2+7h+1),\\
(1,3):&\ h(5h^3+14h^2+6h-1).
\end{aligned}
\]
All have common denominator \(D(h)>0\). Since \(h_+>2\), and \(5h^2-h-7>0\) and \(5h^3+14h^2+6h-1>0\) for all \(h\geq2\), every off-diagonal numerator is nonnegative at \(h\geq h_+\), strictly positive at \(h>h_+\). The diagonals are always positive. For \(0<h\leq h_-\) the \((0,2)\) entry is negative, since \(h_-<1/5\). For \(h_-<h<h_+\), the \((0,4)\) entry is negative. Thus the resolvent is not entrywise nonnegative at any \(0<h<h_+\). At \(h=0\) it is the identity. This proves the exact full-matrix positivity set.

## Verification
`checker.py` uses exact symbolic integer-polynomial arithmetic with SymPy. It reconstructs each Laplacian from its listed edges, forms the determinant and adjugate of \(I+hL_G^2\), verifies the exhaustive nine-graph table and every five-path cofactor formula, checks the single-positive-root property in all smaller graphs by coefficient sign variations, and confirms the positivity thresholds by exact substitutions and inequalities. Run `python checker.py` with SymPy installed. The certificate is finite and exhaustively symbolic: the graph classification and algebraic sign deductions above, not a floating-point test, establish the theorem.

## Relationship to prior work
Gregorio and Mugnolo, *Bi-Laplacians on graphs and networks* (arXiv:1712.07370, first posted December 20, 2017), Section 2 (particularly Remark 2.2 and Proposition 2.3) and Section 6, establish non-positivity of the biharmonic **heat semigroup** for noncomplete graphs and eventual positivity on finite connected graphs. Those facts motivate the question but neither imply the exact five-vertex reentrant **resolvent-entry** threshold nor its positive-step phase set. Benzi and Simunec (arXiv:2012.08389, 2020) study rational approaches to fractional graph diffusion, but do not give this exact sign classification. Ulm (1999), *The interval of resolvent-positivity for the biharmonic operator*, addresses continuum fourth-order operators with boundary conditions; it is a relevant analogue, not the same graph result. Existing finite-graph Padé-positivity results study distinct rational functions and therefore do not dominate the present statement. Searches of the published mathematical-record corpus did not uncover an equivalent five-vertex formula, although search absence alone is not a novelty proof.

## Limitations
No result is claimed about the smallest graph order for reentrant **heat-semigroup** entries, about weighted graphs, or about asymptotic thresholds on paths of arbitrary length. The exact enumeration is limited intentionally to connected simple graphs on at most four vertices, plus the concrete five-vertex witness. Historical priority is not independently certified; unindexed specialist sources might contain an equivalent rational-kernel calculation. All positive-step formulae use the unnormalized combinatorial Laplacian.

## References
1. F. Gregorio and D. Mugnolo, *Bi-Laplacians on graphs and networks*, arXiv:1712.07370, first version December 20, 2017, Sections 2 and 6, https://arxiv.org/abs/1712.07370.
2. M. Benzi and I. Simunec, *Rational Krylov Methods for Fractional Diffusion Problems on Graphs*, arXiv:2012.08389, December 15, 2020, https://arxiv.org/abs/2012.08389.
3. M. Ulm, *The interval of resolvent-positivity for the biharmonic operator*, Proc. Amer. Math. Soc. 127 (1999), 481–489, https://doi.org/10.1090/S0002-9939-99-04556-6. (Analogue for continuous differential operators.)
