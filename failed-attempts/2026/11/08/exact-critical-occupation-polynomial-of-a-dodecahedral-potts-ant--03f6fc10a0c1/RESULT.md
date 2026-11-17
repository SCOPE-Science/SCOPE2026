# Exact critical occupation polynomial of a dodecahedral Potts antiferromagnet

## Finding

Consider the antiferromagnetic three-state Potts model with a nonnegative cost for state 3 on the dodecahedral graph. At its exact zero-temperature switching field, the ground configurations are classified by a degree-six **occupation polynomial**

\[
P(z)=250+3000z+13800z^2+30400z^3+32760z^4+15840z^5+2720z^6.
\]

Thus the critical ground-state degeneracy is \(P(1)=98{,}770\), rather than merely the minimum energy. For field \(h\geq0\), the full ground energy and degeneracies are

\[
\begin{array}{c|c|c}
\text{field}&E_0(h)&\text{number of ground configurations}\\\hline
h=0&0&7200\\
0<h<1&6h&2720\\
h=1&6&98770\\
h>1&6&250
\end{array}.
\]

The occupation polynomial determines an exact low-temperature rounding of the crossing. If \(Z_\beta(h)\) is the finite-volume partition function, then for every fixed real \(x\),

\[
\lim_{\beta\to\infty}e^{6\beta}Z_\beta(1+x/\beta)=P(e^{-x}),\qquad
\lim_{\beta\to\infty}\Pr_{\beta,1+x/\beta}\{k=j\}
=\frac{c_j e^{-xj}}{P(e^{-x})}\quad(0\leq j\leq6),
\]

where \(c_j=[z^j]P(z)\); the limiting probability is zero for \(j>6\). Both limits are locally uniform in \(x\). At the central crossover \(x=0\), the limiting occupation mean and variance are exactly

\[
\mathbb E k=\frac{34836}{9877},\qquad
\operatorname{Var}(k)=\frac{119729580}{97555129}.
\]

The limiting mean decreases strictly with \(x\), with derivative equal to minus its strictly positive variance.

## Assumptions and scope

The graph \(G=GP(10,2)\) has 20 labeled vertices \(o_i,p_i\) indexed by \(i\in\mathbb Z/10\mathbb Z\) and exactly 30 undirected edges

\[
\{o_i,o_{i+1}\},\quad \{o_i,p_i\},\quad \{p_i,p_{i+2}\}
\qquad (i\in\mathbb Z/10\mathbb Z).
\]

It is the ordinary dodecahedral graph (the connectivity graph of the \(\mathrm C_{20}\) fullerene). Spins are maps \(s:V(G)\to\{1,2,3\}\), with distinct named states. Put

\[
b(s)=\sum_{\{v,w\}\in E(G)}\mathbf1\{s_v=s_w\},\qquad
k(s)=\sum_{v\in V(G)}\mathbf1\{s_v=3\},\qquad
H_h(s)=b(s)+h k(s).
\]

The bond energy is normalized to one, \(h\geq0\), and all sites and edges have uniform couplings. The canonical partition function is \(Z_\beta(h)=\sum_s e^{-\beta H_h(s)}\), for \(\beta>0\). All counts concern the finite labeled graph, without quotienting by color or spatial automorphisms; no infinite-volume transition is asserted.

## Proof

**1. A sharp six-unit bound.** Every two-coloring of the dodecahedron has at least six monochromatic edges: each of its twelve pentagonal faces has at least one such edge, and each graph edge belongs to exactly two faces. The lower bound is attained, for example, by the two-color assignment

\[
(s_{o_0},\ldots,s_{o_9})=(1,1,2,1,2,1,1,2,1,2),
\quad(s_{p_0},\ldots,s_{p_9})=(2,2,1,1,1,2,2,1,1,1),
\]

which has precisely six monochromatic edges. The two-state frustration index therefore equals six.

For an arbitrary three-state configuration, change each state-3 vertex to the less frequent of states 1 and 2 among its neighbors. Because the graph has degree three, each such recoloring increases the number of monochromatic edges by at most one (and removes that state-3 vertex). Iterating gives a two-coloring with at most \(b(s)+k(s)\) monochromatic edges. Consequently

\[
\boxed{b(s)+k(s)\geq6\quad\text{for every configuration }s.}
\]

This directly implies \(H_h(s)\geq 6h\) for \(0\leq h\leq1\), and \(H_h(s)\geq6\) for \(h\geq1\). The exact counts in Step 2 contain configurations attaining these bounds; thus the asserted ground energy is exact. At strict \(0<h<1\), equality requires \((b,k)=(0,6)\); for \(h>1\), equality requires \((b,k)=(6,0)\); at \(h=1\), all and only pairs with \(b+k=6\) are ground configurations. At \(h=0\), exactly the proper three-colorings are ground configurations.

**2. Exact sector enumeration.** Use the nine possible columns \(a=(a_o,a_p)\in\{1,2,3\}^2\). Form a sparse \(81\times81\) matrix \(T(u,v)\), with a row indexed by an ordered pair \((a,b)\) of columns and a column indexed by \((b,c)\) for a third column; all other entries are zero. Its transition is

\[
T_{(a,b),(b,c)}(u,v)
=u^{\mathbf1\{a_o=b_o\}+\mathbf1\{a_o=a_p\}+\mathbf1\{a_p=c_p\}}
 v^{\mathbf1\{a_o=3\}+\mathbf1\{a_p=3\}}.
\]

The three bond indicators count, respectively, an outer cycle edge, a spoke, and an inner step-two edge; the two vertex indicators count each third-state spin in the initial column. The trace over ten transitions closes both cyclic directions, counting every labeled configuration once. Therefore the **exact bivariate partition polynomial** is

\[
F(u,v)=\operatorname{tr}\big(T(u,v)^{10}\big)
=\sum_{s:V(G)\to\{1,2,3\}}u^{b(s)}v^{k(s)}.
\]

It follows that

\[
P(z)=[t^6]F(t,tz),\qquad
[u^0]F(u,z)=2720z^6+4160z^7+320z^8.
\]

A finite exact-integer recurrence for the \(81\) transfer states, retaining only partial monomials of total degree at most six, evaluates the first coefficient extraction as

\[
(c_0,c_1,c_2,c_3,c_4,c_5,c_6)
=(250,3000,13800,30400,32760,15840,2720).
\]

The separately computed proper-coloring polynomial in the second identity has value \(7200\) at \(z=1\). The provided executable \(`verify.py`\) implements this recurrence and an independent complete depth-first enumeration of every assignment of total cost six. Its integer comparisons and explicit witness check provide a reproducible finite certificate; they are not an extrapolation from sampling.

**3. Low-temperature crossover.** Write \(h_\beta=1+x/\beta\). Each configuration of total integer cost \(b+k=6\) contributes exactly \(e^{-6\beta-xk}\). Every other configuration has \(b+k\geq7\), so after multiplication by \(e^{6\beta}\) its contribution is bounded by \(e^{-\beta+20|x|}\). There are only \(3^{20}\) labeled configurations, hence the total remainder tends to zero, uniformly for \(x\) in any compact set. The resulting polynomial normalization gives both the partition limit and the limiting occupation law. Differentiating the finite positive polynomial yields the central mean and variance above, as well as strict negativity of the response derivative for every finite \(x\), because all seven coefficients are positive.

## Verification

Run \(`python3 verify.py`\) in the directory containing the provided self-contained verifier. It uses only the Python standard library, constructs the graph as the explicit \(GP(10,2)\) edge list, checks the six-frustrated-edge witness, computes the complete cyclic transfer trace in exact integers, enumerates the critical configurations through a separately implemented vertex-assignment recursion, compares the two exact coefficient vectors, and checks the proper-coloring distribution and exact rational moments. This is an exhaustive finite enumeration, not an approximate numerical experiment. The proof of the crossover follows analytically from finiteness and the strict integral energy gap.

## Relationship to prior work

Choi, Yoo, Kim, Kwon and Won (2026) establish the **universal ground-energy threshold** for subcubic graphs with an expensive third Potts state, including the physical Hamiltonian used here. That energy law and the recoloring mechanism are **not** claimed as new. Shrock and Xu (2010) provide general magnetic-field Potts partition functions and weighted chromatic polynomials; their framework can in principle encode the finite graph's entire polynomial, so no new generic partition-function formalism is claimed. The dodecahedron's ordinary chromatic polynomial and its proper-coloring count are already available in graph references; \(7200\) is reported for consistency, not asserted as a new invariant. Chang (2001) computed chromatic polynomials for generalized-dodecahedron families. The work here concerns the previously unidentified **critical mixed-bond/occupation sector coefficients** and their explicit finite-temperature crossover at the established threshold. Literature and indexed-result comparisons did not identify an evaluated equivalent for that exact graph and field, but cannot prove exhaustive publication priority.

## Limitations

The result is an exact finite-size discrete-spin computation. It neither describes the spin-1 Blume–Capel Hamiltonian when adjacent neutral spins have a different bond energy, nor establishes a thermodynamic-limit phase transition. The general field-dependent partition function in prior literature implies an algorithm to derive the coefficients; originality is restricted to the explicit complete dodecahedral critical-sector evaluation and its resulting scaling law. The coefficients could have been computed in an unindexed source or database not found by the comparisons.

## References

1. J. Choi, S. Yoo, C. Kim, H. Y. Kwon, and C. Won, *Coordination three heals, coordination four is hard: the antiferromagnetic Potts model with a costly third state*, arXiv:2610.41277v1, publicly posted 2026-10-30. https://arxiv.org/html/2610.41277v1
2. R. Shrock and Y. Xu, *Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings*, J. Stat. Phys. 141 (2010), 909–939; arXiv:1009.1182v1. https://arxiv.org/abs/1009.1182
3. S.-C. Chang, *Chromatic polynomials for lattice strips with cyclic boundary conditions*, Physica A 296 (2001), 495–522. https://doi.org/10.1016/S0378-4371(01)00157-1
4. *Dodecahedral Graph*, Wolfram MathWorld (ordinary graph and chromatic polynomial). https://mathworld.wolfram.com/DodecahedralGraph.html
