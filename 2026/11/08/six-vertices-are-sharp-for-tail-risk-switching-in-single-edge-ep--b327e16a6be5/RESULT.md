# Six vertices are sharp for tail-risk switching in single-edge epidemic interdiction

## Finding

Fix a uniformly chosen infection seed on a finite tree. Delete exactly one edge before infection and let each of the remaining edges independently transmit with probability \(p\). For an integer outbreak threshold \(h\), write \(Q_e(p)\) for the probability that the final infected component of the seed has at least \(h\) vertices after deleting edge \(e\).

**Sharp-order theorem.** For every tree with \(2\le n\le5\) vertices and every \(2\le h\le n\), some edge \(e_*\) satisfies \(Q_{e_*}(p)\le Q_e(p)\) for *every* \(p\in[0,1]\) and every edge \(e\). Six is the least order at which there can be no such fixed optimal edge. In the six-vertex tree with edge set
\[
\{(0,1),(0,2),(0,3),(3,4),(4,5)\},
\]
and threshold \(h=3\), the unique optimal cut is \((0,3)\) for \(0<p<3/5\), the two cuts \((0,3)\) and \((3,4)\) tie at \(p=3/5\), and the unique optimal cut is \((3,4)\) for \(3/5<p<1\).

## Assumptions and scope

A tree is a finite, simple, undirected, connected acyclic graph with \(n\ge2\) labeled vertices. A single edge is removed before a seed is drawn uniformly among **all original vertices**. Independent open/closed Bernoulli \(p\) trials are then assigned to the remaining edges; all vertices in the seed's open connected component are counted as infected. No other transmission, recovery, reassignment of the seed distribution, or effect of edge removal on per-edge transmissibility is assumed. The nontrivial comparison is for \(p\in(0,1)\). For \(h=n\), after any cut the threshold event is impossible.

This is the independent-bond transmission model; a general SIR epidemic with random infectious periods does not necessarily have the same joint transmission law.

## Proof

**1. Exact nonnegative-basis identity.** After cutting one edge, \(n-2\) edges remain. For each \(k=0,\ldots,n-2\), define the integer \(c_{e,h,k}\) as follows: among all retained-edge subsets of cardinality \(k\), sum the number of original vertices that lie in a connected component of size at least \(h\). Since the uniform seed lies in such a component with that summed fraction, conditioning on the exact open-edge subset gives
\[
Q_e(p)=\frac1n\sum_{k=0}^{n-2}c_{e,h,k}p^k(1-p)^{n-2-k}.
\]
Every summand basis function is nonnegative on \([0,1]\). Therefore any candidate cut satisfying \(c_{e_*,h,k}\le c_{e,h,k}\) for all other cuts and all \(k\) is optimal simultaneously for all \(p\).

**2. Exhaustive lower-order certificate.** By the Prüfer bijection, each labeled tree on \(n\) vertices is obtained exactly once from a word of length \(n-2\) on its vertex labels. For each \(n=2,3,4,5\), enumerate all \(n^{n-2}\) words, every threshold \(h=2,\ldots,n\), and all \(n-1\) possible cuts. For each cut, enumerate the \(2^{n-2}\) open-edge subsets, compute component sizes by exact integer union-find, and calculate the full integer vector \((c_{e,h,0},\ldots,c_{e,h,n-2})\). In every case, at least one edge has vector componentwise no greater than all competing vectors. The numbers of certified labeled-tree/threshold cases for \(n=2,3,4,5\) are respectively \(1,6,48,500\), totaling \(555\). The full exhaustive procedure, exact assertions, and deterministic replay are in `checker.py`; the general identity above turns these finite exact comparisons into inequalities for the entire continuum of \(p\) values. No floating-point interpolation or finite grid is used to infer the universal assertion.

**3. Exact witness on six vertices.** Direct enumeration of the \(2^4\) retained-edge subsets gives the following polynomial identities for the threshold \(h=3\):
\[
\begin{aligned}
Q_{01}(p)=Q_{02}(p)&=\frac{p^2(9-4p)}6,\\
Q_{03}(p)&=p^2,\\
Q_{34}(p)&=\frac{p^2(9-5p)}6,\\
Q_{45}(p)&=\frac{p^2(12-9p+2p^2)}6.
\end{aligned}
\]
Subtracting gives
\[
Q_{34}(p)-Q_{03}(p)=\frac{p^2(3-5p)}6,
\]
\[
Q_{01}(p)-Q_{34}(p)=\frac{p^3}6>0,
\quad
Q_{45}(p)-Q_{34}(p)=\frac{p^2(3-4p+2p^2)}6>0.
\]
The last quadratic is strictly positive for every real \(p\), since \(3-4p+2p^2=2(p-1)^2+1\). Hence a leaf cut and the terminal-handle cut never minimize. The remaining difference changes sign exactly once, at \(p=3/5\); this proves all three optimality regimes and strict uniqueness away from the tie.

Combining the universal lower-order certificate with this explicit six-vertex witness proves sharp minimality.

## Verification

Execute `python3 checker.py` with Python 3.9 or later; it needs only the standard library. It computes each Prüfer tree, all eligible thresholds, every candidate edge cut, and every independent bond configuration; asserts the complete componentwise-minimum certificates for all \(555\) lower-order cases; and checks all five exact rational witness polynomials and their factorized differences. The polynomial identities, rather than the three sample points used as auxiliary consistency checks, establish the continuous-range conclusions.

The proof uses exhaustive *finite* enumeration of all trees up to five vertices, not an extrapolation from samples of larger trees. For the fixed six-vertex witness, identities follow from complete finite enumeration of its retained-edge states, not merely numerical simulation.

## Relationship to prior work

Kenah and Robins (2006) distinguish independent bond-percolation outbreaks from general SIR epidemic size laws, motivating the explicit independence assumption. Enns and Brandeau (2015) compare link-removal interventions in stochastic epidemic networks with expected final infections as the optimization criterion; their full article also illustrates outbreak-size distributions empirically. Enright and Meeks (2015) develop edge-deletion algorithms limiting deterministic worst-case component size. Neither inspected article states this all-transmissibility, all-tree-up-to-five, threshold-tail optimality result or the exact six-vertex switch. A full proof of historical priority across all graph-reliability literature is not asserted.

## Limitations

The theorem covers one preemptive cut, a uniformly random seed, identical independently transmitting edges, tree networks, and the risk event \(\{\text{infected size}\ge h\}\). It does not assert a similar minimum order for multiple cuts, other seed distributions, cycles, heterogeneous transmissibility, common infectious-period dependence, mean outbreak size, or an empirical disease-control policy. The lower-order argument is computer-assisted but exact and entirely reproducible with the provided source. Related reliability identities could exist in literature not inspected here; no independent audit has been performed.

## References

- Eben Kenah and James M. Robins, *Second look at the spread of epidemics on networks*, first public October 30, 2006. https://arxiv.org/abs/q-bio/0610057
- Eva A. Enns and Margaret L. Brandeau, *Link removal for the control of stochastically evolving epidemics over networks: A comparison of approaches*, first published online February 16, 2015, doi:10.1016/j.jtbi.2015.02.005. https://pmc.ncbi.nlm.nih.gov/articles/PMC4372451/
- Jessica Enright and Kitty Meeks, *Deleting edges to restrict the size of an epidemic*, first public April 22, 2015. https://arxiv.org/abs/1504.05773
