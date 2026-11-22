# Square-zero growth and the inverse-length persistence law for graph inverse semigroups

## Finding
Let \(E\) be any finite directed multigraph with adjacency matrix \(A\), and let \(G(E)\) denote its graph inverse semigroup with zero. The normal form of a nonzero element is uniquely \(\alpha\beta^{-1}\), where the finite directed paths \(\alpha\) and \(\beta\) have the same terminal vertex. Grade this element by the **normal-form length** \(\ell(\alpha\beta^{-1})=|\alpha|+|\beta|\). This is a grading of a set, not an assertion that length is additive under multiplication.

Define the following rational formal power series at the vertices:
\[
P_v(t)=\sum_{k\geq0}\sum_u(A^k)_{uv}t^k,
\qquad C_v(t)=\sum_{k\geq0}(A^k)_{vv}t^k.
\]
Thus \(P_v\) enumerates all directed paths ending at \(v\), and \(C_v\) enumerates all closed directed walks based at \(v\), including the length-zero path. If \(T_n\) is the number of nonzero elements of normal-form length \(n\), and \(Q_n\) is the number of such elements whose square is nonzero, then the complete ordinary generating functions satisfy
\[
\boxed{T(t)=\sum_{n\geq0}T_nt^n=\sum_vP_v(t)^2,\qquad
Q(t)=\sum_{n\geq0}Q_nt^n=\sum_vP_v(t^2)\bigl(2C_v(t)-1\bigr).}
\]
In particular, the generating series for **nonzero square-zero elements** is \(T(t)-Q(t)\). No nonzero element has a nilpotency index exceeding two: every nonzero element either squares to zero or has all its positive powers nonzero.

For an additional asymptotic conclusion, suppose \(A\) is primitive and has Perron root \(\rho>1\). Choose its positive right and left Perron eigenvectors \(r,l\) with \(l^{\mathsf T}r=1\), and set \(R=\sum_vr_v\), \(L=\sum_vl_v^2\). Then
\[
\boxed{\frac{Q_n}{T_n}=\frac{c_E}{n}+O(n^{-2}),\qquad
c_E=\frac{2\sum_v P_v(\rho^{-2})r_vl_v}{R^2L}>0.}
\]
Consequently, a uniformly selected nonzero normal form of exactly length \(n\) has square zero with probability \(1-c_E/n+O(n^{-2})\).

## Assumptions and scope
Vertices are length-zero paths; parallel edges are distinguished. The adjacency convention is \(A_{uv}=\#\{\text{edges }u\to v\}\). The expressions are identities of formal power series in \(t\) with integer coefficients, whether the graph is cyclic, acyclic, disconnected, or periodic. The asymptotic probability theorem assumes **primitive** adjacency and \(\rho>1\) only; it is not asserted for periodic, reducible, or spectral-radius-one graphs. The zero of the semigroup is excluded from every counting series. Normal forms and their uniqueness are standard for graph inverse semigroups.

## Proof
Every nonzero element is uniquely a pair \((\alpha,\beta)\) of paths with the same endpoint. For each endpoint \(v\), the generating function counting the first choice is \(P_v(t)\), and the same function counts the independent second choice. Hence \(T(t)=\sum_vP_v(t)^2\).

The path-cancellation multiplication law says that \((\alpha\beta^{-1})(\gamma\delta^{-1})\) is nonzero precisely when the middle paths \(\beta,\gamma\) are prefix-comparable, meaning that one is obtained by appending a path to the other. In particular, \((\alpha\beta^{-1})^2\ne0\) precisely when \(\alpha,\beta\) are prefix-comparable. Their endpoints coincide, so if \(\alpha=\beta\eta\), the suffix \(\eta\) is a closed path at \(v=r(\beta)\). Likewise, if \(\beta=\alpha\eta\), the suffix is closed. These two cases overlap only when \(\eta\) has length zero, giving \(\alpha=\beta\).

The equal-path (idempotent) case has weight \(\sum_vP_v(t^2)\). The strict-prefix cases come in two disjoint orientations. Choosing a base path \(\beta\) ending at \(v\) contributes weight \(t^{2|\beta|}\), and choosing a nonempty closed suffix \(\eta\) based there contributes \(t^{|\eta|}\). The two orientations therefore contribute \(2\sum_vP_v(t^2)(C_v(t)-1)\). Adding the equal-path case proves the formula for \(Q(t)\).

The same cancellation law gives \((\beta\eta\beta^{-1})^k=\beta\eta^k\beta^{-1}\) in one strict-prefix orientation, and \((\alpha\eta^{-1}\alpha^{-1})^k=\alpha(\eta^k)^{-1}\alpha^{-1}\) in the other, for each \(k\ge1\); these are nonzero because \(\eta\) is closed and can be repeated. Equal paths are idempotent. Conversely, when the pair is not prefix-comparable, its square is zero. This proves the power dichotomy.

Write \(\mathbf1\) for the all-ones vector. Since \(P_v(t)\) is the \(v\)-th entry of \(\mathbf1^{\mathsf T}(I-tA)^{-1}\), and \(C_v(t)\) is the \(v\)-th diagonal entry of \((I-tA)^{-1}\), both series are rational. Under the primitive Perron hypothesis, \(A^k=\rho^krl^{\mathsf T}+O(\tau^k)\) for some \(\tau<\rho\), with an adjustment of \(\tau\) to absorb possible polynomial factors. It follows that near \(t=\rho^{-1}\),
\[
P_v(t)=\frac{Rl_v}{1-\rho t}+H_v(t),\qquad
C_v(t)=\frac{r_vl_v}{1-\rho t}+J_v(t),
\]
where \(H_v,J_v\) are analytic in a disk strictly larger than \(|t|<\rho^{-1}\). Therefore \(T(t)\) has leading double-pole coefficient \(R^2L\), and
\[
T_n=R^2L(n+1)\rho^n+O(\rho^n).
\]
Because \(\rho>1\), \(P_v(t^2)\) is analytic at \(t=\rho^{-1}\) with value \(P_v(\rho^{-2})\). The simple dominant pole of \(Q(t)\) has coefficient \(2\sum_vP_v(\rho^{-2})r_vl_v\), with all other poles farther from the origin. Thus, for some \(\sigma<\rho\),
\[
Q_n=2\left(\sum_vP_v(\rho^{-2})r_vl_v\right)\rho^n+O(\sigma^n).
\]
Dividing gives the stated \(n^{-1}\) law and positive constant. The normalization \(l^{\mathsf T}r=1\) makes the constant unambiguous.

## Verification
The independent, standard-library-only script `CHECK.py` enumerates normal-form path pairs with individually labeled parallel edges. It computes genuine graph-inverse-semigroup products by prefix cancellation and independently computes adjacency-power coefficients of \(T(t)\) and \(Q(t)\). All available degrees through six or eight agree for eight directed graphs, including a strongly connected irregular multigraph, a period-two multigraph, a disconnected zero-edge graph, one loop, and an acyclic graph. It also checks that a nonzero square remains nonzero after the third and fourth powers. This bounded enumeration is a check, not a proof for all graphs.

For a one-vertex graph with \(m\ge2\) loops, \(\rho=m\), \(P(t)=C(t)=(1-mt)^{-1}\), and the constant reduces to \(c_E=2m/(m-1)\). For the full directed two-vertex graph with one edge in each ordered pair, the constant is \(2\). These special cases independently check the leading asymptotic normalization.

## Relationship to prior work
The graph-inverse-semigroup path normal form and cancellation law are established background; the result does not claim their discovery. Jones and Lawson (2011) study abstract characterization and completion; Mesyan and Mitchell (2014) study graph-inverse-semigroup structural properties and congruences. Bezushchak (2024) studies coarse growth of graph inverse semigroups and related Leavitt constructions. Unlike those inspected results, the present calculation is refined by **the elementwise nonzero-square predicate**, supplies a rational enumerator of that predicate, and gives a Perron-Frobenius \(n^{-1}\) persistence constant. No independently verified priority claim is made beyond the reported source comparisons.

## Limitations
The asymptotic law is restricted to primitive \(A\) with \(\rho>1\); general graphs retain the exact rational-series formulas but may have different periodic or polynomial behavior. Normal-form length is not necessarily word length for an arbitrary generating set. The proof is mathematical, and the finite checker does not establish uniqueness in the literature. Earlier implicit or equivalent enumerations may exist and should be independently assessed before a historical priority claim. No independent scientific audit has been performed.

## References
- D. G. Jones and M. V. Lawson, *Graph inverse semigroups: their characterization and completion*, first posted 2011-06-18, https://arxiv.org/abs/1106.3644 .
- Z. Mesyan and J. D. Mitchell, *The Structure of a Graph Inverse Semigroup*, first posted 2014-09-15, https://arxiv.org/abs/1409.4380 .
- D. I. Bezushchak, *Leavitt inverse semigroups of polynomial growth*, Algebra and Discrete Mathematics 37 (2024), 22–34, https://doi.org/10.12958/adm2231 .
