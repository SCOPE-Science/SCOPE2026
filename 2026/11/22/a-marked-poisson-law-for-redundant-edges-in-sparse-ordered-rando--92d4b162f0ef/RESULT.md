# A marked Poisson law for redundant edges in sparse ordered random graphs

## Finding

Fix any real constant \(c>0\). On the ordered vertex set \(\{1,\ldots,n\}\), independently include each forward arc \(i\to j\), \(i<j\), with probability \(c/n\), for integers \(n>c\). Let \(R_n\) be the number of arcs deleted by the unique transitive reduction: these are precisely the arcs whose removal leaves directed reachability unchanged. For \(r\ge3\), let \(M_{n,r}\) count these arcs for which the shortest alternative directed path has \(r-1\) edges.

Then, jointly for every finite set of lengths \(r\ge3\),
\[
(M_{n,3},M_{n,4},\ldots,M_{n,L})\ \xrightarrow{\mathrm d}\ (Z_3,Z_4,\ldots,Z_L),\qquad Z_r\text{ independent},\quad Z_r\sim\operatorname{Poisson}(c^r/r!).
\]
Moreover, the total number of removed arcs converges **in total variation** to
\[
R_n\xrightarrow{\mathrm{TV}}\operatorname{Poisson}(\Lambda(c)),\qquad
\Lambda(c)=\sum_{r=3}^{\infty}\frac{c^r}{r!}=e^c-1-c-\frac{c^2}{2}.
\]
Its expectation tends to \(\Lambda(c)\). With probability tending to one, the redundant arcs have pairwise disjoint endpoint sets, and **each has exactly one alternative directed path**. In fact, the vertex sets of the corresponding shortcut cycles are pairwise disjoint with high probability.

Thus the sparse graph typically needs only a finite, Poisson-distributed number of edge deletions to preserve all reachability relations, even though it has order \(n\) arcs.

## Assumptions and scope

The graph is a **simple ordered directed acyclic graph**, not a multigraph or a model conditioned on a degree sequence. Every possible forward arc is independent. The parameter \(c\) is fixed as \(n\to\infty\); the result does not assert uniformity when \(c\) itself grows with \(n\). The alternate path in the definition of \(M_{n,r}\) must avoid the arc being tested. Since paths are increasing in the vertex order, they are necessarily simple. A shortest alternate path exists for every redundant arc.

A *shortcut witness of length \(r\)* is a directed increasing path through \(r\) distinct vertices, with \(r-1\) arcs, together with the direct arc between its endpoints. Its undirected support is a simple cycle on \(r\) vertices. Let \(W_{n,r}\) be the number of such witnesses and \(W_n=\sum_{r=3}^nW_{n,r}\). It has the **exact finite-size expectation**
\[
\mathbb E W_{n,r}=\binom nr\left(\frac cn\right)^r,
\qquad
\mathbb E W_n=\sum_{r=3}^n\binom nr\left(\frac cn\right)^r.
\]
The exact expectation formula is for witnesses, not generally for removed arcs: one arc can admit several alternative paths in a finite graph.

## Proof

**1. Exact witness count.** Given any increasing \(r\)-tuple of vertices \(v_1<\cdots<v_r\), exactly one potential shortcut witness uses them: the edges \(v_1\to v_2\to\cdots\to v_r\), together with \(v_1\to v_r\). These \(r\) distinct arcs are all present with probability \((c/n)^r\). Summing over the \(\binom nr\) tuples proves both finite-size expectation formulas.

**2. Orientation of one undirected cycle.** Conditional on an undirected simple cycle of length \(r\) with its vertices randomly labelled by distinct ranks, it constitutes a directed shortcut witness if and only if one cycle edge joins the minimum and maximum ranks and the complementary path is strictly increasing. There are exactly \(2r\) favorable assignments of the ranks to its cyclically arranged vertices out of \(r!\), hence the probability is
\[
\theta_r=\frac{2r}{r!}=\frac{2}{(r-1)!}.
\]
No undirected simple cycle can be a shortcut witness in two different ways: the direct arc must join its unique minimum and maximum ranks. The usual Poisson limit for the number of fixed-size cycles in \(G(n,c/n)\) has mean \(c^r/(2r)\). Conditioning on the relative orders of labels on vertex-disjoint cycles therefore thins the cycle count with probability \(\theta_r\), giving independent Poisson limits with means \(c^r/r!\).

For completeness, the classical cycle-Poisson calculation follows from factorial moments: disjoint collections of any fixed finite list of cycles have asymptotic factorial moments equal to products of \(c^r/(2r)\), while every collection of distinct overlapping cycles contains a connected component with strictly more edges than vertices and contributes \(O(n^{-1})\). Independently assigning the ranks to disjoint cycles gives independent relative cyclic orders, so the same factorial-moment proof applies to the thinned witness counts \(W_{n,r}\). This does not require \(c<1\).

**3. All lengths and structural uniqueness.** For each fixed \(L\), the expected number of pairs of distinct witnesses of lengths at most \(L\) sharing a vertex is \(O_{c,L}(n^{-1})\), by the same excess-edge argument. The large-witness tail obeys
\[
\sup_{n>c}\mathbb E\sum_{r>L}W_{n,r}
\le \sum_{r>L}\frac{c^r}{r!}\xrightarrow[L\to\infty]{}0.
\]
Thus, with probability tending to one, **all** witnesses are pairwise vertex-disjoint. Every redundant arc has at least one witness, and distinct alternative paths for the same arc would yield two vertex-overlapping witnesses. Therefore, on this high-probability event, \(R_n=W_n\), every removed arc has exactly one alternative path, and its witness cycle is disjoint from all others. In particular the path-length marks of removed arcs match the witness marks.

**4. The joint and total limits.** For fixed \(L\), the joint Poisson limit of the witness counts gives a Poisson sum of mean \(\sum_{r=3}^Lc^r/r!\). The preceding expected-tail bound allows \(L\to\infty\) and yields convergence in distribution to \(\operatorname{Poisson}(\Lambda(c))\). Since these variables take nonnegative integer values, this convergence is also in total variation (truncate to a sufficiently large finite support). The coupling \(R_n=W_n\) with probability \(1-o(1)\) transfers the limit and the finite-dimensional marked limits to the actual transitive reduction.

Finally, \(R_n\le W_n\) and the finite-size witness expectation give \(\limsup\mathbb E R_n\le\Lambda(c)\). For any fixed \(L\), the number of redundant arcs witnessed at lengths at most \(L\) equals \(\sum_{r=3}^LW_{n,r}\) with probability \(1-o(1)\); a uniformly bounded second moment for this finite sum follows from the same disjoint-cycle factorial-moment calculation. Hence \(\liminf\mathbb E R_n\ge\sum_{r=3}^Lc^r/r!\). Let \(L\to\infty\) to conclude \(\mathbb E R_n\to\Lambda(c)\).

## Verification

The accompanying self-contained Python 3 file `verify.py` checks the orientation identity for every assignment of ranks on cycles of lengths 3 through 8. It exhaustively enumerates every ordered simple digraph on 3, 4, 5 and 6 vertices, checking that redundancy is equivalent to having an alternate-path witness and verifying the exact witness expectation at arc probability \(1/2\) through integer arithmetic. It runs without external packages via `python3 verify.py`. The test produced `PASS finite checks 67738`. The enumeration is **not** evidence for the infinite Poisson theorem; steps 2–4 are its proof.

## Relationship to prior work

Random graph orders and their transitive closure were studied by Albert and Frieze (1989), principally for height and related statistics. Rödl and Thoma (2005) studied cover graphs and dependent arcs, including extremal deletion counts for substantially denser random graphs; the bounds described in their publicly available abstract have lower density \(n^{-1+1/\ell}\), not the present \(c/n\) regime. Karrer and Newman (2009) introduced independently placed *Poisson-multiplicity* arcs for acyclic network null models and studied degrees and pair connection probabilities; their model is not the present Bernoulli simple graph. Clough and collaborators (2013) applied transitive reduction to citation data and null models; their reported results concern empirical network structure rather than this length-marked Poisson limit. Standard small-cycle Poisson asymptotics are used and not claimed as a new ingredient.

The distinctive statement is the **distribution of the number of Bernoulli arcs removed by transitive reduction**, the entire independent Poisson spectrum of alternative-path lengths, and the disjoint-unique-certificate law. This is not implied solely by the known unmarked counts of undirected cycles without the orientation and witness-to-reduction argument.

## Limitations

The claim is limited to fixed \(c>0\), a uniform independent-edge model and asymptotic \(n\to\infty\). No finite-\(n\) total-variation rate is asserted, and no analogous claim is made for fixed-degree, preferential-attachment or Poisson-multigraph models. The full text of a potentially relevant 2005 paper on dependent arcs was not accessible; its public abstract covers an extremal problem in another density regime, but historical priority would benefit from independent checking of its complete contents. An undiscovered stronger general theorem on oriented random cycles could imply this specialization.

## References

- M. H. Albert and A. M. Frieze, *Random Graph Orders*, Order 6 (1989), 19–30. Full text: https://www.math.cmu.edu/~af1p/Texfiles/RANDGRAPHORD.pdf
- V. Rödl and L. Thoma, *On Cover Graphs and Dependent Arcs in Acyclic Orientations*, Combinatorics, Probability and Computing 14 (2005), 585–617, https://doi.org/10.1017/S0963548305006760 (public online date July 21, 2005).
- B. Karrer and M. E. J. Newman, *Random graph models for directed acyclic networks*, arXiv:0907.4346 (first posted July 24, 2009), https://arxiv.org/abs/0907.4346
- J. R. Clough, J. Gollings, T. V. Loach and T. S. Evans, *Transitive reduction of citation networks*, arXiv:1310.8224 (first posted October 30, 2013), https://arxiv.org/abs/1310.8224
