# Polynomial-time two-cycle census on fully subdivided complete graphs

## Finding
For each integer \(n\ge3\), let \(G_n=S(K_n)\) be the graph formed by subdividing every edge of the labelled complete graph \(K_n\) exactly once. Under ordinary synchronous, conservative, degree-threshold parallel chip-firing, the number \(T_n\) of **distinct primitive temporal two-cycle orbits** has the following explicit finite formula, evaluable in \(O(n^4)\) integer/rational arithmetic operations.

Write \(m=\binom n2\), \(b=n-a\), and, for \(0\le k\le a\), \(0\le\ell\le b\), set
\[
H_{a,b}(k,\ell)=\sum_{j=0}^{\min(k,\ell)}(-1)^j\binom kj\binom\ell j j!\,b^{k-j}a^{\ell-j}.
\]
Then
\[
\boxed{
T_n=2^{m-1}\sum_{a=0}^{n}\binom na
\sum_{k=0}^{a}\sum_{\ell=0}^{n-a}
\frac{\binom ak\binom{n-a}{\ell}(a-1)^{a-k}(n-a-1)^{n-a-\ell}}
{2^{k+\ell}}\,H_{a,n-a}(k,\ell).
}
\]
All powers with exponent zero are interpreted as one, including \(0^0\). Although displayed intermediate terms are rational and alternating, the final count is a nonnegative integer. The initial values for \(n=3,4,5,6,7,8\) are respectively
\[
100,\quad12312,\quad3759616,\quad2764042240,\quad4765773791232,\quad18876597230632960.
\]
The novelty of this result is the polynomial-sized evaluation for this symmetric incidence-graph family, not an assertion that the general cut-degree representation of two-cycles is new.

## Assumptions and scope
The graph \(G_n\) has \(n+m\) labelled vertices: one original vertex for each element of \(\{1,\ldots,n\}\), and one degree-two subdivision vertex for each two-element subset. It has \(2m\) edges. Original vertices have degree \(n-1\); subdivision vertices have degree two.

A state assigns each vertex a nonnegative integer chip count. Every vertex holding at least its degree sends one chip to each neighbor, simultaneously, in one update \(F\). No sinks, loops, randomization, or sequential updates are present. A primitive two-cycle is an unordered pair \(\{x,F(x)\}\) satisfying \(F^2(x)=x\) and \(F(x)\ne x\). The result counts only these orbits, not fixed points, basins, transients, or primitive orbits of other periods. Complexity means arithmetic operation count on exact integers/rationals, not constant-cost bit complexity.

## Proof
**Step 1: classify temporal two-cycles by a firing bipartition.** For any finite connected graph, write \(f_v\in\{0,1\}\) and \(g_v\in\{0,1\}\) for the firing indicators on the first and second steps. The update equation gives \(F^2(x)-x=-L(f+g)\), where \(L\) is the graph Laplacian. On a connected graph, its real kernel consists of constant vectors. For a primitive two-cycle this constant cannot be zero or two, since all vertices neither firing nor all firing give a fixed point. Therefore \(g=\mathbf1-f\).

Set \(c_v(f)=|\{w\sim v:f_w\ne f_v\}|\). If \(f_v=1\), the allowable first-step chip counts are the \(c_v(f)\) integers \(d_v,\ldots,d_v+c_v(f)-1\). If \(f_v=0\), they are \(d_v-c_v(f),\ldots,d_v-1\). These conditions are necessary and sufficient for the firing pattern to complement at the next update; the second update restores the initial chip counts. Thus for a fixed firing pattern \(f\) there are precisely \(\prod_v c_v(f)\) qualifying states. Each primitive orbit has exactly two complementary first-step firing patterns. Hence
\[
T_n=\frac12\sum_{f\in\{0,1\}^{V(G_n)}}\prod_{v\in V(G_n)}c_v(f).
\]
This general cut-degree identity is already known; it is the starting point, not the new evaluation.

**Step 2: eliminate subdivision spins.** Fix the firing colors of the \(n\) original vertices. Let \(A\) be the first color class, of size \(a\), and \(B\) the other, of size \(b\). For each original edge with both ends in the same class, its inserted vertex must have the opposite color; otherwise its own opposite-neighbor count vanishes. Each such edge contributes a factor two from the inserted vertex and one opposite neighbor to each endpoint. There are \(\binom a2+\binom b2=m-ab\) such edges.

On an original edge joining \(A\) to \(B\), either color for the subdivision vertex gives its opposite-neighbor count one. In either case the edge contributes exactly one opposite neighbor to **one** original endpoint, chosen by that subdivision color. Thus the \(ab\) cross edges are independently oriented toward one endpoint. For a chosen orientation \(\omega\), let \(d_\omega(v)\) count the cross edges oriented to \(v\). The resulting exact contribution of all permitted subdivision colors is
\[
2^{m-ab}\sum_{\omega}\prod_{u\in A}\bigl(a-1+d_\omega(u)\bigr)
\prod_{v\in B}\bigl(b-1+d_\omega(v)\bigr),
\]
with the sum over all \(2^{ab}\) orientations.

**Step 3: evaluate the dependent orientation product by a reciprocal-pair sieve.** Expand the last product. Choose \(k\) of the \(a\) vertices of \(A\), and \(\ell\) of the \(b\) vertices of \(B\), to select an incoming cross edge rather than the constant internal-edge contribution. The remaining factors give \((a-1)^{a-k}(b-1)^{b-\ell}\). Each selected vertex chooses one incident cross edge. Such choices are jointly orientable exactly when no cross edge is chosen by both endpoints; these conflicts are precisely reciprocal pairs.

Without the restriction, the choices number \(b^k a^\ell\). A set of \(j\) specified reciprocal pairs consists of \(j\) chosen vertices of each shore and a bijection between them, so inclusion-exclusion gives exactly \(H_{a,b}(k,\ell)\) admissible choices. Distinct selected vertices may choose edges incident to a common *unselected* endpoint; this causes no conflict and is counted. For every admissible choice, the \(k+\ell\) selected edges are distinct and their orientations forced. The other \(ab-k-\ell\) edges have two orientations each. Multiplying by the contributions from same-color edges gives
\[
2^{m}\sum_{k=0}^a\sum_{\ell=0}^b
\frac{\binom ak\binom b\ell(a-1)^{a-k}(b-1)^{b-\ell}}{2^{k+\ell}}
H_{a,b}(k,\ell).
\]
There are \(\binom na\) original firing colorings of class size \(a\). Sum over \(a\) and divide by two for temporal phases to obtain the boxed formula.

**Step 4: complexity.** The indices \(a,k,\ell,j\) range over at most \(O(n^4)\) quadruples. All binomial coefficients, factorials and the powers of integer bases from \(-1\) through \(n\), to exponents at most \(n\), can be tabulated in \(O(n^2)\) arithmetic operations. The displayed formula therefore evaluates in \(O(n^4)\) exact arithmetic operations, rather than enumerating \(2^{n+\binom n2}\) firing patterns. The output itself has polynomially many bits: bounding each opposite-neighbor count by the vertex degree yields \(T_n\le 2^{n+2m-1}(n-1)^n\).

## Verification
The independent program `verify_formula.py` evaluates the stated alternating sieve with exact rational arithmetic, checks its reciprocal-pair count against direct function-pair enumeration for all \(1\le a,b\le3\), and directly enumerates every firing-color pattern on \(G_n\) for \(n=3,4,5\). It verifies the numerical values through \(n=8\).

The independent program `verify_dynamics.cpp` uses the actual parallel-chip-firing update, **not** the cut-degree formula, on every chip state in the finite range \(0\le x_v<2d_v\) for \(n=3,4\). It checks a two-step return with a nontrivial first step and divides the resulting periodic states by two. It enumerates 4,096 and 5,308,416 chip configurations respectively, producing 100 and 12,312 distinct primitive two-cycle orbits. These checks corroborate the all-size proof; they do not replace it. Run instructions appear in each source file and in `VERIFICATION.md`.

## Relationship to prior work
Jiang's 2010 paper establishes the connected-graph equal-firing-count condition, but its complete-bipartite period classification does not enumerate period-two orbits on an incidence graph of a clique. The 2012 paper by Jiang, Scully and Zhang focuses on realizable periodic firing sequences, not the present parameterized census. A prior general cut-degree theorem gives the exponential cut sum for every graph and is explicitly used above; it does **not** state the symmetry-reduced \(O(n^4)\) evaluation or reciprocal-pair sieve for fully subdivided cliques. Known period-two formulas for complete graphs, complete bipartite graphs, trees and ladders concern different graph families. Complete subdivision of \(K_n\) is not complete bipartite and contains cycles, so none of those family-specific formulas directly supplies this answer.

## Limitations
This does not classify chip-firing trajectories of least period greater than two, nor transient attraction or energy-resolved counts. The arithmetic-operation bound is not a bound on a fixed-size machine-word implementation; the integers grow with \(n\). Because a general exact cut polynomial is known, priority is asserted only for the explicit polynomial-time specialization and its reciprocal-pair evaluation, not for the general firing-pattern method. Searches of the accessible literature and indexed records did not reveal this formula, but unindexed treatments of the same incidence graph may exist. Independent external verification has not been performed.

## References
1. T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943, first posted 2010-03-04, especially Proposition 2.5 and Section 3. https://arxiv.org/abs/1003.0943
2. T.-Y. Jiang, Z. Scully and Y. X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, arXiv:1211.6786, first posted 2012-11-29. https://arxiv.org/abs/1211.6786
3. *Cut-degree census and maximum-cut thresholds for period-two chip-firing*, publicly available mathematical manuscript, especially the universal cut polynomial and proof. https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-cut-degree-census-and-maximum-cut-thresholds-for-period-two-chip--5004d505b623/RESULT.md
