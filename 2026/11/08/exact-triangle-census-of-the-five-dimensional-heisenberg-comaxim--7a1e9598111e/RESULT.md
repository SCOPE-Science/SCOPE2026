# Exact triangle census of the five-dimensional Heisenberg comaximal graph

## Finding
Let \(q\) be any prime power, let \(H=H_5(\mathbb F_q)\) have basis \(x_1,x_2,y_1,y_2,z\) and nonzero basis brackets \([x_i,y_j]=\delta_{ij}z\), and let \(\Gamma(H)\) have as vertices its nonzero proper Lie subalgebras, with an edge between two distinct subalgebras exactly when they generate \(H\) as a Lie algebra. Write \(t_q\) for the number of unordered triangles (three pairwise adjacent vertices). Set
\[
 h=q^3+q^2+q+1,\quad p=(q^2+1)(q^2+q+1),\quad i=(q+1)(q^2+1),
\]
\[
 g=(q^2-1)(q^2-q),\quad s=q^2(q-1),\quad
 e_{22}=\frac{q^4}{2}(p+2q^2i+q^3i).
\]
Then the exact triangle count for **every** finite field is
\[
\boxed{\begin{aligned}
 t_q={}&\binom h3+(1+q)h\binom{q^3}{2}
 +(p+q^2i)\binom{q^3+q^2}{2}\\
 &+e_{22}\big(h-2(q+1)\big)
 +\frac{q^4g}{6}\big(p+3q^2i+3q^3i\big)
 +\frac{q^9is}{6}.
\end{aligned}}
\]
In particular, \(t_2=42105\), \(t_3=8121580\). The last two terms count triangles with all three quotient subspaces two-dimensional; they include the contribution of triples of pairwise complementary Lagrangians. This is the first Heisenberg dimension beyond the three- and four-dimensional comaximal-graph cases considered in the motivating 2026 literature.

## Assumptions and scope
The integer \(q\) is an arbitrary prime power, including nonprime extension fields and characteristic two. The central quotient \(V=H/\mathbb F_qz\) has dimension four with its standard nondegenerate alternating form. A proper nonzero subalgebra projects either to zero (only the center) or to a nonzero proper subspace \(W\) of \(V\). For the latter, the number of subalgebras above \(W\) is \(b(W)=1+q^{\dim W}\) if \(W\) is totally isotropic, and \(b(W)=1\) otherwise. Two such subalgebras are adjacent precisely when the images span \(V\). The one central vertex is isolated. These structural statements are proved directly below and are not the originality claim; the new claim is the explicit complete triangle formula.

## Proof
**The quotient graph.** A subalgebra containing the center is the inverse image of a subspace of \(V\). A subalgebra missing the center must be the graph of a linear functional over a totally isotropic \(W\le V\), yielding the stated multiplicities. A pair generates \(H\) if and only if the projected subspaces sum to \(V\): if their generated algebra projects onto \(V\) yet misses the center, its brackets vanish, contrary to nondegeneracy. Hence triangles are weighted triples of pairwise spanning nonzero proper subspaces in \(V\).

**Dimension patterns.** Since \(\dim(W+U)=4\) is required for every pair, the only unordered dimension profiles are \((3,3,3)\), \((1,3,3)\), \((2,3,3)\), \((2,2,3)\), and \((2,2,2)\). There are \(h\) hyperplanes and \(h\) lines. Each line is absent from exactly \(q^3\) hyperplanes; each 2-plane is absent from exactly \(q^3+q^2\) hyperplanes. The number of 2-planes is \(p\), of which \(i\) are Lagrangian. Every line has multiplicity \(1+q\), and the total 2-plane multiplicity is \(p+q^2i\). This gives the first three summands of the formula.

For a fixed two-dimensional subspace \(P\), there are \(q^4\) complementary two-planes. Of the \(i\) Lagrangian planes, each has \(q^3\) complementary Lagrangians: after fixing a complementary Lagrangian, these are graphs of symmetric 2-by-2 matrices. Therefore the weighted number of unordered complementary plane pairs is
\[
 e_{22}=\frac{q^4p}{2}+q^6i+\frac{q^7i}{2}.
\]
For every complementary pair \(P,Q\), the number of hyperplanes containing neither is \(h-2(q+1)\), since each plane is contained in \(q+1\) hyperplanes and no hyperplane contains both. The \((2,2,3)\) contribution is \(e_{22}(h-2(q+1))\).

**Three complementary two-planes.** Fix two complementary two-planes \(P,Q\). Any plane complementary to both is the graph of an invertible linear map \(Q\to P\), so there are \(g=|\operatorname{GL}_2(\mathbb F_q)|\) possibilities. Expand \(b(P)b(Q)b(R)\) into constant, linear, quadratic and cubic isotropy terms. The respective unordered-triple contributions are
\[
 \frac{pq^4g}{6},\qquad \frac{q^2iq^4g}{2},\qquad
 \frac{q^4iq^3g}{2},\qquad \frac{q^6iq^3s}{6}.
\]
The cubic term uses that, for two fixed complementary Lagrangian planes, a third plane transverse to both is Lagrangian precisely when its graph is a symmetric **invertible** 2-by-2 matrix. There are \(q^3\) symmetric matrices, of which exactly \(q^2\) are singular: for matrices \(\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)\), the equation \(ac=b^2\) has \(2q-1+(q-1)^2=q^2\) solutions, valid even in characteristic two. Hence \(s=q^2(q-1)\). Combining these four contributions gives \(q^4g(p+3q^2i+3q^3i)/6+q^9is/6\). The five dimension patterns exhaust all triangles and establish the formula.

## Verification
The standalone checker enumerates all subspaces of the four-dimensional quotient in reduced-row-echelon form over \(\mathbb F_2\) and \(\mathbb F_3\). It computes the alternating brackets directly, derives each fiber weight by independently testing isotropy, tests pairwise spanning by row reduction, and enumerates all weighted triples. It finds \(42105\) and \(8121580\) triangles respectively; it also records the contribution of each of the five dimension profiles. The program does not use the symbolic triangle formula when generating the graph. The proof covers all finite fields and is not extrapolated from these finite tests.

## Relationship to prior work
Towers, Zuleta and Gutierrez introduced comaximal graphs of Lie algebras and classified dimension three (arXiv:2605.09583v1, May 10, 2026). Their follow-up, *Comaximal Graphs of finite-dimensional Lie algebras over finite fields: Triangle counts and structural invariants* (arXiv:2608.16575v1, August 17, 2026), computes triangle counts in dimension three, studies certain four-dimensional algebras, and gives a general Frattini-quotient graph blow-up theorem. The quotient-blow-up principle and previously available vertex/edge counts or full graph descriptions are not new here; the all-field closed triangle formula in the first five-dimensional Heisenberg case, including the invertible-symmetric-matrix correction, is the claimed contribution. No equivalent formula was located in the searched primary literature or research records; this is not an absolute novelty guarantee.

## Limitations
The theorem covers the five-dimensional Heisenberg algebra, not every higher-rank Heisenberg Lie algebra and not arbitrary two-step nilpotent algebras. The independent-in-implementation enumeration checks only prime fields of orders 2 and 3. The method of quotient weighting is known; the nontrivial new calculation is the exact five-dimensional triple count. The numeric examples are consequences rather than substitutes for the all-field proof. Earlier unindexed triangle enumerations cannot be excluded. Independent mathematical audit has not been performed.

## References
- D. A. Towers, Y. Zuleta, I. Gutierrez, *The comaximal graph of a finite-dimensional Lie algebra*, arXiv:2605.09583v1, 2026-05-10, https://arxiv.org/html/2605.09583v1.
- D. Towers, Y. Zuleta, I. Gutierrez, *Comaximal Graphs of finite-dimensional Lie algebras over finite fields: Triangle counts and structural invariants*, arXiv:2608.16575v1, 2026-08-17, https://arxiv.org/abs/2608.16575.
