# Exact radial shells and a Gaussian vertex-radius law for biclique graphical zonotopes

## Finding
For every integer \(q\ge2\), let \(Z_q\) be the centered graphical zonotope of the complete bipartite graph \(K_{2,q}\), realized in the ambient Euclidean space \(\mathbb R^{q+2}\):
\[
Z_q=\sum_{\{i,j\}\in E(K_{2,q})}\left[-\frac{e_i-e_j}{2},\frac{e_i-e_j}{2}\right].
\]
For a vertex \(v\) of \(Z_q\), write \(R(v)=\|v\|_2\). The **complete** radial shell enumerator, with multiplicity, is
\[
\boxed{F_q(z)=\sum_{a+b+c=q}\left(2-\mathbf1_{\{c=0\}}\right)\frac{q!}{a!b!c!}\,z^{(a-b)^2+c^2+2(a+b)}
=\sum_{v\in\operatorname{Vert}(Z_q)}z^{2R(v)^2}.}
\]
All summation indices are nonnegative integers. In particular, \(F_q(1)=2\cdot3^q-2^q\). The nearest-to-origin **vertex** squared radius, its number of attaining vertices, and the farthest squared radius are
\[
\min_v R(v)^2=\begin{cases}q-\frac12,&q=2m+1,\\q,&q=2m,\end{cases}
\qquad
\#\operatorname*{argmin}_v R(v)=\begin{cases}2(2m+1)\binom{2m}{m},&q=2m+1,\\ (m^2+4m+1)\binom{2m}{m},&q=2m,\end{cases}
\]
\[
\max_v R(v)^2=\frac{q(q+2)}2,\qquad\#\operatorname*{argmax}_v R(v)=2.
\]
When \(q\) is even, every vertex squared radius is an **even integer**; when \(q\) is odd, every such squared radius is a half-integer (not an integer).

For a uniformly sampled vertex \(V_q\) of \(Z_q\), let \(R_q=\|V_q\|_2\). Then
\[
\mathbb E R_q^2=\frac{2\cdot3^q(q^2/18+10q/9)-2^q(3q/2)}{2\cdot3^q-2^q},
\]
and, as \(q\to\infty\),
\[
\frac{R_q}{q}\xrightarrow{\mathsf P}\frac{1}{3\sqrt2},\qquad
\frac{R_q-q/(3\sqrt2)}{\sqrt q}\xrightarrow{\mathrm d}N(0,1/9),
\]
\[
\frac{R_q^2-q^2/18}{q^{3/2}}\xrightarrow{\mathrm d}N(0,2/81).
\]
Thus the complete vertex-radius spectrum is an explicit weighted lattice-square spectrum, while uniform-vertex radii have Gaussian fluctuations around a radius linear in \(q\).

## Assumptions and scope
All coordinates use the standard inner product on \(\mathbb R^{q+2}\) and unit-weight graph-edge segments with endpoints \(\pm(e_i-e_j)/2\). The ambient affine span is the zero-sum hyperplane. A **uniform vertex** means uniform counting measure on distinct vertices, not uniform polytope volume or Gaussian normal-cone exposure. The near-origin radius refers only to vertices: it is not the inradius of \(Z_q\), which contains the origin. The central-symmetry center is the origin.

## Proof
**Acyclic orientations and exact coordinates.** Label the two high-degree vertices \(h_1,h_2\) and the remaining \(q\) vertices \(w_1,\ldots,w_q\). Represent each edge orientation by a sign: \(s_{ji}=+1\) for an arrow from \(h_j\) to \(w_i\), and \(-1\) for the reverse arrow. Each leaf gives one of four ordered pairs \((s_{1i},s_{2i})\). An orientation has a directed cycle if and only if both mixed types \((+1,-1)\) and \((-1,+1)\) occur. Indeed, their two leaves form a directed four-cycle. Conversely, every simple directed cycle in this complete bipartite graph must use both hubs and therefore has length four, requiring opposite mixed types.

A vertex of a graphical zonotope corresponds bijectively to an acyclic edge orientation: a generic linear objective determines the edge signs, and conversely a topological ordering exposes the vertex for any acyclic orientation. The corresponding centered zonotope vertex is half its signed outdegree-minus-indegree vector. If the allowed mixed type is \((+1,-1)\) and the counts of \((+1,+1),(-1,-1),(+1,-1)\) are respectively \(a,b,c\), its coordinates at the two hubs are \((a-b+c)/2\) and \((a-b-c)/2\), while its leaf coordinates are \(-1\) for type \((+1,+1)\), \(+1\) for type \((-1,-1)\), and zero for a mixed type. Thus
\[
2R(v)^2=(a-b)^2+c^2+2(a+b),\qquad a+b+c=q.
\]
The other allowed mixed type exchanges the hubs and yields exactly the same radial formula. For \(c>0\), the two choices are disjoint orientation families, while for \(c=0\) they coincide. There are \(q!/(a!b!c!)\) placements of each triple, proving the displayed polynomial and total vertex count.

**Exact extrema and parity.** Put \(d=a-b\). The radial formula can be completed to a lattice square:
\[
R(v)^2=q-\frac12+\frac12\left(d^2+(c-1)^2\right),\quad d\equiv q-c\pmod2,\quad |d|\le q-c.
\]
For odd \(q=2m+1\), the choice \((d,c)=(0,1)\) is admissible, gives the unique smallest lattice-square value, and has \(a=b=m\), hence multiplicity \(2(2m+1)\binom{2m}{m}\). For even \(q=2m\), \((d,c)=(0,1)\) is inadmissible. The smallest possible squared lattice distance is one, attained exactly at \((0,0),(1,1),(-1,1),(0,2)\). Counting multinomial placements gives \((m^2+4m+1)\binom{2m}{m}\). This establishes both inner-shell claims for all stated dimensions.

For even \(q\), hub coordinates are integers and leaf coordinates are integers; because their sum is zero and every integer square has the parity of its base, the sum of squared coordinates is an even integer. For odd \(q\), both hub coordinates are half-integers and leaf coordinates are integers, so the total squared radius is a half-integer. For the outer radius, \(R^2=q-c+((a-b)^2+c^2)/2\) is strictly convex on the continuous simplex \(a,b,c\ge0\), \(a+b+c=q\). Its maximum is therefore attained only at simplex vertices. The choices \((q,0,0)\) and \((0,q,0)\) each have squared radius \(q(q+2)/2\), strictly larger than \((0,0,q)\), which has squared radius \(q^2/2\). The first two triples each encode one orientation.

**Exact mean and the limit law.** Consider independent uniformly sampled states from just three types \((+1,+1),(-1,-1),(+1,-1)\). Their counts are multinomial with parameters \((q;1/3,1/3,1/3)\). In that model \(d=a-b\) has mean zero and variance \(2q/3\), \(c\sim\operatorname{Bin}(q,1/3)\), and \(\mathbb E c^2=q^2/9+2q/9\). Therefore \(\mathbb E R^2=q^2/18+10q/9\). For the binary overlap \(c=0\), the mean is \(3q/2\). Correcting the double counting of this overlap yields the exact uniform-vertex expectation above.

The actual uniform-vertex radial law differs in total variation by \(O((2/3)^q)\) from the three-state multinomial radial law: each non-overlap orientation has two disjoint mixed-type realizations, and the all-unmixed family has relative mass \(O((2/3)^q)\). Under the multinomial model, \((c-q/3)/\sqrt q\) converges to \(N(0,2/9)\), while \(d^2=O_{\mathsf P}(q)\). Writing \(R^2=(d^2+c^2)/2+q-c\), the central limit theorem and Slutsky's theorem give the asserted limit for the normalized squared radius. The square-root delta method, centered at \(q/(3\sqrt2)\), gives the normalized-radius limit with variance \(1/9\) and the law of large numbers. Exponentially small total-variation error transfers both limits to uniform vertices.

## Verification
Run `python3 check.py` using the Python standard library. The independent routine enumerates all \(4^q\) edge orientations for \(2\le q\le8\), tests directed acyclicity with a topological-sort algorithm rather than the three-state classification, and computes signed-degree Euclidean squared radii. It exactly matches all coefficients of the displayed polynomial, the extrema, contact counts, and the rational expectation. A second integer-only routine checks the algebraic formulas through \(q=150\). Last observed output:

`K2Q_RADIAL_PASS independently_enumerated_dimensions=2..8 independently_enumerated_vertices=19166 symbolic_dimensions=2..150`

The checks are finite and corroborative. The proof above, rather than the enumerations, establishes the results for all \(q\ge2\).

## Relationship to prior work
Padrol, Pilaud and Poullot (arXiv:2111.12422) provide the general graphical-zonotope background and deformation geometry. Chapoton and Pilaud (arXiv:2201.06896) explicitly study complete bipartite graphical zonotopes, their face structure and vertex counts. These establish the family and the acyclic-orientation bijection, not the complete Euclidean radial polynomial or the uniform-vertex Gaussian limit. Previously available complete-multipartite circumsphere results already imply the outermost radius and outer contact classification, which are therefore included only as consistency checks, **not** as claims of novelty. Results about vertex *degrees*, volume covariance, inballs or Gaussian normal cones refer to distinct invariants or sampling measures.

## Limitations
The classification is restricted to the canonical unweighted \(K_{2,q}\) Euclidean embedding and to vertices. It does not describe radial distributions under continuous-volume or normal-cone sampling, general \(K_{p,q}\), or edge-weighted deformations. The originality comparison includes two primary full texts and available research records, but historical priority remains provisional; a differently phrased earlier result may exist. The separate mathematical review is same-model only; independent audit has not been performed.

## References
- A. Padrol, V. Pilaud, G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422 (first public version 2021-11-24), https://arxiv.org/abs/2111.12422 .
- F. Chapoton, V. Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, arXiv:2201.06896 (first public version 2022-01-18), https://arxiv.org/abs/2201.06896 .
- *Complete multipartite graphical zonotopes have cubic-moment circumspheres*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-multipartite-graphical-zonotopes-have-cubic-moment-circ--2fc427ff213b .
