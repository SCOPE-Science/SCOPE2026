# A three-particle coalescence fingerprint hidden by identical bulk means

## Finding

Consider independent rate-one continuous-time simple random walkers on two six-regular, cospectral graphs: the sixteen-vertex rook graph \(R=K_4\square K_4\) and the Shrikhande graph \(S\). When two walkers meet they immediately merge, and the remaining walker continues at rate one. Write \(T\) for the first time one walker remains, starting from three distinct occupied vertices.

**Theorem.** For *every* initial triple spanning a triangle, the exact mean coalescence times are
\[
\mathbb E_R T=\frac{143}{14},\qquad
\mathbb E_S T=\frac{1145}{112},\qquad
\mathbb E_S T-\mathbb E_R T=\frac1{112}>0.
\]
Both graphs have exactly \(32\) triangles, and each graph's triangles share the indicated value. In contrast, for two walkers starting from adjacent sites the exact mean is \(15/2\), and for a nonadjacent pair it is \(9\), in **both** graphs. Furthermore, choosing the three distinct initial positions uniformly among all \(\binom{16}{3}=560\) triples gives the same unconditional mean on both graphs:
\[
\frac1{560}\sum_{|B|=3}\mathbb E_B T=\frac{2203}{196}.
\]
Thus triangle-conditioned three-particle coalescence distinguishes these spectral twins even though the two-particle means and global three-particle mean agree.

## Assumptions and scope

Vertices are the sixteen ordered pairs \((a,b)\in\mathbb Z_4^2\). In \(R\), distinct pairs are adjacent when their first or second coordinates coincide. In \(S\), the differences of adjacent vertices belong to \(D=\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}\), with arithmetic modulo four. Each occupied vertex has its own independent rate-one exponential jump clock and uniformly chooses one of six neighbors. A jump to an occupied vertex removes one particle, regardless of its identity. No births or splitting occur. All numerical values in this theorem are measured in the mean waiting time of a single walker between jumps. The claim is **not** about synchronous or discrete-time walks.

## Proof

For a nonempty occupied vertex set \(B\) let \(h_G(B)=\mathbb E_B T\), with \(h_G(B)=0\) when \(|B|=1\). The first jump occurs at rate \(|B|\); conditioning on which particle jumps and its target yields, for \(|B|=2\) or \(3\), the exact backward equation
\[
 h_G(B)=\frac{1}{|B|}+\frac{1}{6|B|}\sum_{x\in B}\sum_{y\sim x}h_G((B\setminus\{x\})\cup\{y\}).
\]
The two connected finite graphs permit eventual coalescence almost surely from every initial state; hence this finite transient-chain Poisson system has a unique solution. It contains \(120\) two-site and \(560\) three-site unknowns per graph.

Both graphs have strongly regular parameters \((16,6,2,2)\). On two distinct sites, adjacency and nonadjacency are therefore an exact two-class Markov quotient. Ordering states as nonadjacent and adjacent, the backward system is
\[
 \begin{pmatrix}1&0\\0&1\end{pmatrix}
 \begin{pmatrix}h_N\\h_A\end{pmatrix}
 -\frac1{12}
 \begin{pmatrix}8&4\\6&4\end{pmatrix}
 \begin{pmatrix}h_N\\h_A\end{pmatrix}
 =\begin{pmatrix}1/2\\1/2\end{pmatrix}.
\]
Here the row sums represent transitions that keep two particles distinct; collisions contribute zero. Solving gives \(h_N=9\) and \(h_A=15/2\). (Equivalently, the transient generator has row coefficients \((-2/3,2/3)\) for nonadjacent-to-adjacent and \((1,-4/3)\) for adjacent-to-nonadjacent.)

For triples, apply the displayed backward equation, substituting the already determined pair values after each coalescing jump. Group triples by graph automorphisms, which preserve all transition counts. For \(R\), permuting rows and columns and exchanging coordinates gives \(1152\) distinct automorphisms and four triple orbits. For \(S\), translating \(\mathbb Z_4^2\) and applying the twelve invertible connection-set-preserving linear maps gives \(192\) automorphisms and eight triple orbits. The table records each orbit's least representative \(B\), its size, the number of edges induced by \(B\), and the *exact* solution \(h_G(B)\). Vertex labels use \((a,b)\mapsto 4a+b\).

| Graph | Representative | Size | Induced edges | Mean \(h_G(B)\) |
|---|---|---:|---:|---:|
| \(R\) | (0,1,2) | 32 | 3 | \(143/14\) |
| \(R\) | (0,1,4) | 144 | 2 | \(303/28\) |
| \(R\) | (0,1,6) | 288 | 1 | \(159/14\) |
| \(R\) | (0,5,10) | 96 | 0 | \(83/7\) |
| \(S\) | (0,1,2) | 48 | 2 | \(303/28\) |
| \(S\) | (0,1,4) | 96 | 2 | \(173/16\) |
| \(S\) | (0,1,5) | 32 | 3 | \(1145/112\) |
| \(S\) | (0,1,7) | 96 | 1 | \(1273/112\) |
| \(S\) | (0,1,8) | 192 | 1 | \(159/14\) |
| \(S\) | (0,2,8) | 16 | 0 | \(83/7\) |
| \(S\) | (0,2,9) | 48 | 0 | \(83/7\) |
| \(S\) | (0,6,9) | 32 | 0 | \(1327/112\) |

This table is an exact finite certificate, not sampling: the companion standalone exact-rational program enumerates all \(560\) three-site states, computes both partitions and solves the quotient linear systems with rational Gaussian elimination. It then checks the original (uncompressed) backward equation at *every* three-site state. The unique triangle orbit in each graph proves the triangle claims. The size-weighted sum of the listed rational orbit means, divided by \(560\), gives \(2203/196\) for each graph. Subtracting the triangle means gives \(1/112\).

## Verification

Run `python3 coalescence_exact_check.py` using only the Python standard library. It enumerates graph edges and \(120+560\) states for each graph, reconstructs all \(1152\) and \(192\) automorphisms respectively, derives an independent equitable partition from transitions rather than graph maps, solves both exact-rational quotient systems, and checks all \(560\) individual three-particle backward equations in each graph. Its final output states `PASS exact orbit and equitable refinement, 560-state backward equations per graph`.

Separately run `python3 coalescence_sparse_check.py` with NumPy and SciPy installed. This constructs the full \(680\)-state transient generator directly, with no automorphism compression or exact-solver imports; it independently agrees with all triangle and global averages to better than \(10^{-10}\). These are finite exact Markov-chain computations supported by the uniqueness argument, not extrapolations from a finite experiment to an infinite family.

## Relationship to prior work

Oliveira (2010) establishes general continuous-time coalescence-time bounds for reversible chains and the connection with voter consensus, not this pair of exact three-site initial-condition values. Cooper, Elsässer, Ono and Radzik (2012) study discrete-time coalescing walks and general upper bounds, including walks initially at every vertex; the dynamics and initial condition differ. Kanade, Mallmann-Trenn and Sauerwald (2016) study general coalescence/meeting-time bounds in discrete time. Previously published exact cover-time comparisons and other stochastic models on the Shrikhande–rook pair concern observables different from these triangle-conditioned coalescence times. The theorem asserts no novelty for the general backward equation or strongly regular graph parameters.

## Limitations

This is an exact two-graph, three-particle comparison, not a classification of arbitrary strongly regular graphs, general particle numbers, time distributions, or synchronous coalescence. A difference of \(1/112\) in mean times need not imply a stochastic ordering. The equal uniform initial-triple mean is established only for these two specific graphs. Literature searches and inspected source texts do not definitively establish historical priority; an unindexed or differently formulated earlier exact computation may exist. Independent validation has not been performed.

## References

- R. I. Oliveira, *On the coalescence time of reversible random walks*, first arXiv version 2010-09-03, https://arxiv.org/abs/1009.0664.
- C. Cooper, R. Elsässer, H. Ono and T. Radzik, *Coalescing random walks and voting on connected graphs*, first arXiv version 2012-04-17, https://arxiv.org/abs/1204.4106.
- V. Kanade, F. Mallmann-Trenn and T. Sauerwald, *On coalescence time in graphs—When is coalescing as fast as meeting?*, first arXiv version 2016-11-08, https://arxiv.org/abs/1611.02460.
