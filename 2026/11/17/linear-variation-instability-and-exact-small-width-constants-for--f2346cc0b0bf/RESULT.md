# Linear variation instability and exact small-width constants for two-row isotonic regression

## Finding

Let \(k\ge2\), let \(G_k=P_2\square P_k\) be the two-row, \(k\)-column nearest-neighbor rectangular grid, with vertices \((i,j)\), \(i\in\{0,1\}\) and \(0\le j<k\), and edges connecting horizontally or vertically adjacent vertices. Orient every edge toward the increasing coordinate, and let \(\Pi_k:\mathbb R^{2k}\to\mathbb R^{2k}\) be ordinary *unweighted Euclidean isotonic regression* onto the cone of arrays nondecreasing along both coordinates. Define the (undirected, unweighted) graph variation
\[
 V_k(h)=\sum_{uv\in E(G_k)}|h_u-h_v|,
\]
and the two-input sharp coefficient
\[
 C_k=\sup_{V_k(x-y)>0}\frac{V_k(\Pi_k x-\Pi_k y)}{V_k(x-y)}.
\]
Then the **exact first five coefficients** are
\[
 \boxed{(C_2,C_3,C_4,C_5,C_6)=\left(1,\frac43,\frac32,\frac{19}{10},\frac94\right).}
\]
Every listed coefficient is attained by distinct finite pairs. Thus one square is nonexpansive but two squares already admit amplification, and \(k=6\) is the first size in this family with coefficient exceeding \(2\).

For **every** integer \(k\ge2\), the dimension-dependent coefficient obeys the explicit bounds
\[
 \boxed{\frac12+\frac{\lfloor k^2/4\rfloor}{k}\ \le\ C_k\ \le\ 3k-2.}
\]
In particular \(C_k=\Theta(k)\): fixed-two-row isotonic least-squares regression has **no width-independent graph-variation Lipschitz bound** even though its Euclidean Lipschitz coefficient is \(1\). The upper bound is not claimed sharp for general \(k\), and no exact formula is claimed for \(k\ge7\).

## Assumptions and scope

All signals are real arrays with coordinates ordered row-major: top row vertices \(0,\dots,k-1\), bottom row \(k,\dots,2k-1\). The vertical covers are \(j\to k+j\), and horizontal covers are \(ik+j\to ik+j+1\) for \(i=0,1\). All vertex least-squares masses and variation-edge weights are \(1\). Each undirected cover edge appears once in \(V_k\). The same projection operator is applied independently to the two inputs, with no stochastic data model or constraint on their signs. Constants are invariant under adding a common constant to each input.

The graph has \(3k-2\) edges. In the sharp coefficient, differences with \(V_k(x-y)=0\) are excluded; translation equivariance makes the corresponding output variation zero.

## Proof

**1. Reduction to realizable block averaging.** A Euclidean projection onto a polyhedral order cone is continuous and piecewise affine. At a full-dimensional input cell, the fitted coordinates equal on each connected component \(B\) of tight directed-cover edges, and the projection's linear part \(A_{\mathcal B}\) replaces coordinates in \(B\) by their arithmetic mean. Every such partition \(\mathcal B\) is a partition into blocks connected in the *undirected* grid. The directed quotient on blocks, obtained by contracting all within-block edges, must be acyclic: any directed quotient cycle would force equality between different blocks.

Conversely, every partition into connected blocks whose quotient is acyclic occurs on a full-dimensional input cell. Assign to the blocks strictly increasing fitted values along a topological ordering of the quotient, producing a fitted array \(z\) with exactly the prescribed tight edges. Add to \(z\) a strictly positive linear combination of the outward constraint normals \(e_u-e_v\) for *all* tight cover edges \(u\to v\). The projection optimality conditions hold at \(z\), all non-tight constraints have slack, and the normal lies in the relative interior of that face's normal cone. These strict conditions persist on an open input neighborhood. Hence the corresponding \(A_{\mathcal B}\) is locally realized, with arbitrary sufficiently small perturbation directions.

Since there are finitely many full-dimensional cells, integration of these linear parts along segments (or the finite piecewise-affine selection lemma) gives
\[
 C_k=\max_{\mathcal B\text{ feasible}}\sup_{V_k(h)>0}\frac{V_k(A_{\mathcal B}h)}{V_k(h)}.
\]
The converse local realization proves that this maximum is *attained* by actual pairs, rather than merely being a formal upper bound.

**2. Exact binary-cut reduction.** For every fixed real linear \(A\) with \(A\mathbf1=\mathbf1\) and every nonconstant \(h\), the level-set/coarea identity gives
\[
 h=\min_v h_v\,\mathbf1+\int_{\min h}^{\max h}\mathbf1_{\{h>t\}}\,dt,
 \qquad V_k(h)=\int V_k(\mathbf1_{\{h>t\}})\,dt.
\]
Because \(A\) preserves constants, homogeneity and the triangle inequality yield
\[
 \sup_{V_k(h)>0}\frac{V_k(Ah)}{V_k(h)}
 =\max_{\varnothing\ne S\subsetneq V(G_k)}
   \frac{V_k(A\mathbf1_S)}{V_k(\mathbf1_S)}.
\]
The denominator is positive because the grid is connected. Thus exact finite enumeration of connected equality partitions, rejection of cyclic directed quotients, and enumeration of the \(2^{2k}-2\) proper nonempty binary cuts constitute a finite *proof certificate* for each specified \(k\).

**3. Exhaustive certificates for \(2\le k\le6\).** The standalone accompanying `verify_ladder.py` implements the preceding finite characterization. It generates every subset of the \(3k-2\) directed covers; for each subset it computes connected components, deduplicates the resulting partitions, and retains a partition exactly when a standard topological-sort test confirms its quotient is acyclic. Every connected block partition arises from its within-block spanning forests, so this procedure omits none. For every retained partition it evaluates every nontrivial binary cut, using integer arithmetic after multiplication by \(D=\operatorname{lcm}(1,\dots,2k)\). It checks **all** inequalities by exact integer cross multiplication, not floating-point optimization. At least one equality witness is explicitly found for each claimed coefficient.

| Number of columns \(k\) | Feasible block partitions | Exact binary-cut checks | Maximum |
|---:|---:|---:|---:|
| 2 | 10 | 140 | \(1\) |
| 3 | 52 | 3,224 | \(4/3\) |
| 4 | 272 | 69,088 | \(3/2\) |
| 5 | 1,424 | 1,455,328 | \(19/10\) |
| 6 | 7,456 | 30,524,864 | \(9/4\) |

The exact upper-bound verification is reproducible with `python verify_ladder.py` and NumPy. Every equality listed in the table is witnessed by an attainable face and a binary cut. For example, when \(k=3\), pool only the two vertices in the middle vertical rung, \(\{1,4\}\), and take the upper-row cut \(S=\{0,1,2\}\). Its input variation is \(3\), whereas the pooled signal's variation is \(4\), yielding \(4/3\). For \(k=4\), pooling the top-row middle edge \(\{1,2\}\) and taking \(S=\{0,1,4,5\}\) gives input variation \(2\) and output variation \(3\), yielding \(3/2\). The complete checker includes the less elementary extremal faces for \(k=5,6\).

**4. Explicit linear-growth lower bound.** For arbitrary \(k\), take the realizable block partition with the *entire top row as one block*, while every bottom-row vertex remains a singleton. Feasibility follows by setting the fitted top row constant and the bottom row strictly increasing above it, then perturbing the input in the relative-interior outward normal direction of the top-row equalities. Let \(s=\lfloor k/2\rfloor\), and use the binary perturbation \(h_{i,j}=0\) for \(j<s\) and \(h_{i,j}=1\) for \(j\ge s\), in both rows. Then \(V_k(h)=2\). After top-row averaging, the top row becomes constant \((k-s)/k\); the bottom row retains the step. The output has horizontal variation \(1\) and vertical variation \(2s(k-s)/k\). Therefore
\[
 C_k\ge\frac{1+2s(k-s)/k}{2}
 =\frac12+\frac{\lfloor k^2/4\rfloor}{k}.
\]
This is an actual local two-input witness, not a claim that the nonlinear regression of the cut by itself equals the block average.

**5. Linear upper bound.** The isotonic cone is closed under coordinatewise minimum and maximum, implying coordinatewise monotonicity of its Euclidean projector. Indeed if \(a\le b\), compare the minimizing pairs \(\Pi_k a,\Pi_k b\) with their coordinatewise minimum and maximum; the exchange inequality and uniqueness give \(\Pi_k a\le\Pi_k b\). Translation equivariance gives \(\Pi_k(z+c\mathbf1)=\Pi_k(z)+c\mathbf1\). If \(\alpha=\min_v(x_v-y_v)\) and \(\beta=\max_v(x_v-y_v)\), these facts imply
\[
 \alpha\le (\Pi_kx-\Pi_ky)_v\le\beta\quad\text{for every vertex }v.
\]
Every output edge difference is consequently at most \(\beta-\alpha\), which is no greater than \(V_k(x-y)\) because the grid is connected. Summing over its \(3k-2\) edges proves \(C_k\le3k-2\). Combining upper and lower bounds proves \(C_k=\Theta(k)\).

## Verification

Run `python verify_ladder.py` with Python and NumPy installed. The exact tests are based on integer arrays: denominators divide the least common multiple of the block sizes; every comparison is a cross-product of integers within signed 64-bit range for \(2\le k\le6\). The script verifies face counts, exhaustively tests every feasible partition and binary cut, and reports exact rational attainment witnesses. It also checks the arbitrary-width constructive formula at several wider sizes, without misrepresenting those finitely many tests as an asymptotic proof. The infinite-width estimate and legitimacy of the finite search follow from the analytical arguments above.

## Relationship to prior work

Németh and Németh (2012, 2015) prove structural order-monotonicity properties of isotonic metric projection, which support the elementary upper bound but do not yield the grid graph-variation constants or the linear lower bound. Chatterjee, Guntuboyina and Sen (arXiv:1506.03430, first public June 10, 2015) study the *same two-dimensional isotonic least-squares cone*, but their main results concern statistical risks, minimax rates and rectangular-block adaptation, not sharp two-input edge-total-variation amplification. Their full HTML text, including the main theorems and the regression characterization, was compared.

The previously available **cyclic-cover rigidity** result treats orders whose undirected *entire* Hasse graph is one cycle; it establishes contraction for equal variation weights. Its square-grid case \(k=2\) is prior coverage, **not** a novelty claim here. The ladder with \(k\ge3\) has multiple overlapping square cycles and is outside that theorem's hypotheses. The published general \(\ell_p\) isotonic-regression stability theorem measures coordinate \(\ell_p\) input and output norms, not graph-edge variation; its \(p=2\) value \(1\) does not imply the graph-variation coefficients here. General tree isotonic variation results also do not imply the ladder statement, because every \(G_k\) has cycles.

## Limitations

The exact values are established only for \(2\le k\le6\), and no sharp coefficient or precise asymptotic constant is asserted for larger widths. The asymptotic conclusion is only order-of-growth \(\Theta(k)\), with explicit but nonmatching upper/lower bounds. The projector is unweighted quadratic isotonic regression on the ordinary two-row product order; weighted observations, unequal variation weights, higher-row grids, and other losses are not treated. These statements do not concern a statistical risk guarantee. Historical originality is provisional: older book literature and less accessible sources may contain implicit special cases, although inspected closely related results do not state or imply the full ladder conclusion.

## References

1. A. B. Németh and S. Z. Németh, *Isotonicity of the projection onto the monotone cone*, arXiv:1201.4677, first publicly posted 2012-01-23. https://arxiv.org/html/1201.4677v1
2. A. B. Németh and S. Z. Németh, *Isotonic regression and isotonic projection*, arXiv:1503.08458, first publicly posted 2015-03-29. https://arxiv.org/html/1503.08458v2
3. S. Chatterjee, A. Guntuboyina and B. Sen, *On matrix estimation under monotonicity constraints*, arXiv:1506.03430, first publicly posted 2015-06-10. https://arxiv.org/html/1506.03430v3
4. *Cyclic-cover rigidity of weighted-variation stability for isotonic regression*, publicly indexed research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-cyclic-cover-rigidity-of-weighted-variation-stability-for-isoton--c6a0693fe803
5. *Sharp \(\ell_p\) isotonic regression stability on every finite partial order*, publicly indexed research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-ell-p-isotonic-regression-stability-on-every-finite-partia--7bfc7f16ca62
