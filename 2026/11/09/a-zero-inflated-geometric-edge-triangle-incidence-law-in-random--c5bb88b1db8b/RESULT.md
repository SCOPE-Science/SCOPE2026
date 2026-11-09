# A zero-inflated geometric edge–triangle incidence law in random recursive simplicial complexes

## Finding
In the two-dimensional random recursive simplicial complex defined below, let \(A_k(n)\) denote the number of edges lying in exactly \(k\) two-dimensional triangular faces after \(n\) vertices have arrived; \(E_n\) is the number of edges. For every fixed integer \(k\ge0\), almost surely,
\[
\frac{A_k(n)}{E_n}\longrightarrow q_k,
\qquad
q_0=\frac{3\sqrt5-5}{10},\qquad
q_k=\frac35\left(\frac{5-\sqrt5}{10}\right)^{k-1}\quad(k\ge1).
\]
The convergence holds simultaneously over all \(k\ge0\) and, more strongly, in total variation for the empirical probability measures on \(\{0,1,2,\ldots\}\):
\[
\sum_{k=0}^{\infty}\left|\frac{A_k(n)}{E_n}-q_k\right|\longrightarrow0\quad\text{almost surely}.
\]
In particular, the limiting chance for a uniformly sampled existing edge to belong to **exactly one** triangular face is \(3/5\). A positive proportion \((3\sqrt5-5)/10\) of edges remain in no triangular face, while the positive-incidence tail is geometric, not power-law.

## Assumptions and scope
The complex starts at \(n=1\) with one isolated vertex. After \(n\) vertices, choose one of the \(n+E_n\) currently existing vertices and edges **uniformly from their pooled set**. Add a new vertex. If an old vertex was chosen, join it to the new vertex by one edge. If an old edge was chosen, add the two edges joining its endpoints to the new vertex and include the corresponding filled triangular two-face. Every newly created face and its subfaces are retained permanently. All choices are made using the current complex; no initial random seed beyond the selections is required.

Every edge has a well-defined nonnegative triangle-incidence count. All assertions concern the limit as the number \(n\) of vertices increases; no moving-index or finite-size convergence rate is asserted. Write \(\varphi=(1+\sqrt5)/2\).

## Proof
**1. Density of edges.** Given the complex after \(n\) vertices, the next increment in \(E_n\) equals one when a vertex is chosen and two when an edge is chosen. Consequently,
\[
\mathbb E[E_{n+1}-E_n\mid\mathcal F_n]
=1+\frac{E_n}{n+E_n}.
\]
Put \(e_n=E_n/n\). With \(\eta_{n+1}\) the bounded mean-zero increment error,
\[
e_{n+1}=e_n+\frac{g(e_n)+\eta_{n+1}}{n+1},\qquad
g(e)=1+\frac e{1+e}-e.
\]
For \(n\ge2\), \(1/2\le e_n\le2\). The function \(g\) has the unique root \(\varphi\) on this interval, and \(g'(e)=-1+(1+e)^{-2}\le-5/9\). Expanding the conditional square \(\mathbb E[(e_{n+1}-\varphi)^2\mid\mathcal F_n]\), bounded increments and the preceding strict drift imply
\[
\mathbb E[(e_{n+1}-\varphi)^2\mid\mathcal F_n]
\le\left(1-\frac{10}{9(n+1)}\right)(e_n-\varphi)^2+
\frac{C}{(n+1)^2}
\]
for all sufficiently large \(n\) and a fixed finite \(C\). The nonnegative-supermartingale convergence argument with summable error and divergent harmonic drift shows \(e_n\to\varphi\) almost surely.

**2. Exact conditional face-incidence recurrences.** For \(k\ge0\), write \(A_k=A_k(n)\), \(H_n=n+E_n\), and let \(A_{-1}=0\). A vertex-selection creates exactly one edge of incidence zero. An edge-selection increases the selected old edge's incidence by one and creates exactly two edges of incidence one. Thus, for every finite state,
\[
\begin{aligned}
\mathbb E[\Delta A_0\mid\mathcal F_n]&=\frac{n-A_0}{H_n},\\
\mathbb E[\Delta A_1\mid\mathcal F_n]&=\frac{2E_n+A_0-A_1}{H_n},\\
\mathbb E[\Delta A_k\mid\mathcal F_n]&=\frac{A_{k-1}-A_k}{H_n},\qquad k\ge2.
\end{aligned}
\]
Each coordinate increment is bounded by three in absolute value. In particular its centered martingale noise is bounded.

**3. Almost-sure limits for every fixed incidence count.** Let \(a_{k,n}=A_k(n)/n\). Dividing the preceding equations by the updated vertex number gives one-dimensional stochastic approximation recurrences with bounded martingale errors and strictly negative linear coefficient for the current coordinate. Since \(e_n\to\varphi\), successive induction in \(k\) yields \(a_{k,n}\to a_k\) almost surely, with
\[
\begin{aligned}
a_0&=\frac1{\varphi+2},\\
a_1&=\frac{2\varphi+a_0}{\varphi+2},\\
a_k&=\frac{a_{k-1}}{\varphi+2},\qquad k\ge2.
\end{aligned}
\]
For completeness, the standard linear-recursion step used here follows by writing a centered coordinate as
\(z_{n+1}=(1-b_n/(n+1))z_n+(u_n+\eta_{n+1})/(n+1)\), where \(b_n\to b>0\), \(u_n\to0\), and \(\eta_{n+1}\) are bounded martingale differences. The martingale series \(\sum_n\eta_{n+1}/(n+1)\) converges almost surely because the sum of its conditional variances is finite. Iterating the contractive recursion and summing by parts against this convergent series shows that the martingale contribution tends to zero. The remaining inhomogeneous term tends to zero by the Toeplitz averaging property of the nonnegative contraction weights, whose mass remains bounded while each fixed early weight tends to zero. Therefore \(z_n\to0\) almost surely. This establishes the induction rather than assuming a deterministic mean-field limit.

**4. Normalization and total variation.** Put \(r=(\varphi+2)^{-1}=(5-\sqrt5)/10\). As \(E_n/n\to\varphi\), the limiting mass at \(k\) is \(q_k=a_k/\varphi\). Elementary simplification gives \(q_0=(3\sqrt5-5)/10\), \(q_1=3/5\), and \(q_k=q_1r^{k-1}\) for \(k\ge1\). Directly,
\[
q_0+\frac{q_1}{1-r}=1.
\]
Thus the limit is a probability distribution. By taking the countable intersection of the almost-sure events of coordinate convergence, all coordinates converge simultaneously. Since both empirical and limiting measures have total mass one, truncation to finitely many coordinates and then letting the truncation increase proves convergence in \(\ell^1\), equivalently total variation.

**5. Incidence consistency.** Each inserted triangle contributes exactly three edge–triangle incidences; each insertion contributes either one edge and no triangle or two edges and one triangle. Therefore the number \(F_n\) of triangular two-faces satisfies exactly \(F_n=E_n-n+1\), and
\[
\sum_{k\ge0}kA_k(n)=3F_n.
\]
The proposed limit has finite mean \(\sum_{k\ge0}kq_k=q_1/(1-r)^2=3(\varphi-1)/\varphi\), matching the limiting global incidence-to-edge ratio. This identity is a check, not a substitute for the almost-sure coordinate proof.

## Verification
The accompanying Python checker `check_edge_incidence.py` enumerates every reachable labeled graph state at each size from one through seven vertices. For every state and every possible vertex-or-edge selection, it checks the **exact integer drift numerators** in Step 2 and the total incidence identity in Step 5. It also validates the closed-form constants and performs a seeded large-size simulation as a diagnostic. On the final packaged checker, all 525916 assertions passed. The count of checks is a finite correctness diagnostic only; the infinite conclusions follow from Steps 1–4.

To replay from the package, save `check_edge_incidence.py` and run `python3 check_edge_incidence.py` with Python 3 standard library. No downloaded data or external dependencies are required.

## Relationship to prior work
Krapivsky and Lucas (2026) introduce precisely this uniform vertex-or-edge simplicial growth and analyze global simplex counts, vertex degrees, and extreme observables. Their publicly accessible abstract and indexed overview report a golden-ratio edge density and a power-law **vertex-degree** tail; the present statement concerns **edge triangle-incidence**, which is not determined by vertex-degree frequencies. The primary article's complete text could not be inspected, so absence of the precise theorem from that article is not certified.

Kovalenko and coauthors (2021) derive an exponential edge triangle-degree law in a *different* nonpreferential simplicial growth model, in which every arriving vertex connects to endpoints of selected existing edges and always creates triangles. In particular that model has no edges with zero triangular incidence, whereas the present mixed vertex-or-edge process has the strict positive zero-incidence mass above. The geometric character of edge incidence is therefore not claimed as a new general phenomenon; the present exact mixture and constants concern a different stochastic model.

Ding, Yu and Sun (2024), and Ding and coauthors (2026), investigate growth with face-dimension selection and preferential or other order-heterogeneous mechanisms. Their published abstracts report power-law generalized face degrees. No equivalence between those mechanisms and pooled uniform vertex-or-edge selection has been established; their full texts were not available for a definitive comparison.

## Limitations
This result concerns only the two-dimensional process with pooled **uniform** choices. It gives an almost-sure limiting one-edge incidence law, not a joint distribution of neighboring edges, moving-index maximum-degree results, rates of convergence, or a general dimension-\(m\) theorem. The proof relies on standard stochastic-approximation martingale arguments; the finite enumeration does not independently certify an infinite asymptotic. Mathematical correctness, novelty and significance have received self-review only, with no independent audit. Historical priority remains uncertain where relevant primary full text was unavailable.

## References
1. P. L. Krapivsky and M. Lucas, *Random Recursive Simplicial Complexes*, arXiv:2608.26547 (first publicly submitted 2026-08-27), https://arxiv.org/abs/2608.26547 .
2. V. Kovalenko et al., *Growing scale-free simplices*, Communications Physics 4, article 43 (2021), https://doi.org/10.1038/s42005-021-00538-y .
3. M. Ding, J. Yu and W. Sun, *Growing simplicial complex with face dimension selection and preferential attachment*, Chaos 34, 103107 (2024), https://doi.org/10.1063/5.0210960 .
4. M. Ding et al., *Growing order-heterogeneous simplicial complexes*, Chaos 36, 013143 (2026), https://doi.org/10.1063/5.0288666 .
