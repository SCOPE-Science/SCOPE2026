# Exact short cyclic covers of every even-parity binary window through order seven

## Finding

For every integer \(n\ge 2\), define \(L_n\) to be the least positive integer \(L\) such that a **circular indexed binary word** of length \(L\) contains, among its \(L\) cyclic contiguous length-\(n\) windows, every binary length-\(n\) word of even Hamming weight. Extra windows, including repeated even-weight windows or odd-weight windows, are permitted. Then

\[
(L_2,L_3,L_4,L_5,L_6,L_7)=(4,7,16,24,46,82).
\]

Although \(n=3\) already admits a shorter-than-de-Bruijn cover, order four requires all \(16\) possible windows; shortening reappears at \(n=5\), where \(L_5=24<2^5\). Moreover, for \(n=5\) and \(n=7\), an optimal cover cannot be obtained by supplementing every mandatory even-weight window solely with odd-weight windows: the respective optimal lengths in that restricted model are \(26\) and \(85\), strictly larger than \(24\) and \(82\).

These finite values are accompanied by an exact cycle-hypergraph reduction for arbitrary \(n\ge2\), and by fully reproducible exhaustive certificates for the stated finite range. The claim is only about the displayed six orders, not a formula at larger orders.

## Assumptions and scope

An indexed circular word \(s=s_0\cdots s_{L-1}\) has length-\(n\) window \(s_i s_{i+1}\cdots s_{i+n-1}\), with indices taken modulo \(L\). Distinct starting indices may yield identical windows. Neither reversal nor rotation of the *windows* is identified: all \(2^{n-1}\) even-weight indexed binary words must occur individually. The circular cover itself may be rotated without changing validity.

Let \(D_n\) be the binary de Bruijn digraph with vertices \(\{0,1\}^{n-1}\), and an arc labeled by each length-\(n\) word from its length-\((n-1)\) prefix to its suffix. Let \(E_n\) be the subset of its arcs labeled by even-weight words. An arc multiset is balanced if each vertex has equal in- and out-degree, counting multiplicity. A simple directed cycle has no repeated vertices except its initial/final vertex; loops are permitted.

## Proof

**1. Mandatory arcs form a permutation.** For any vertex \(v\) of length \(n-1\), exactly one appended bit gives an even-weight arc, namely the parity of \(v\). Likewise exactly one prepended bit gives an even-weight arc ending at \(v\). Therefore \(E_n\) has indegree and outdegree one at each vertex and decomposes into disjoint directed cycles, denoted \(C_0,\ldots,C_{r-1}\). By choosing the component containing the all-zero vertex as \(C_0\), we fix an anchor. The total number of mandatory arcs is \(2^{n-1}\).

**2. Exact cycle-hypergraph reduction.** Any circular cover corresponds to a closed directed walk through arcs of \(D_n\) containing every arc of \(E_n\). Subtracting one copy of each mandatory arc from the walk's multiset leaves a nonnegative balanced arc multiset \(H\). Every finite balanced directed multigraph decomposes into simple directed cycles (counted with multiplicities). Each such cycle touches a subset \(F\subseteq\{0,\ldots,r-1\}\) of mandatory components through its visited vertices.

The original walk traverses a connected balanced multigraph, so the hypergraph on the mandatory components whose hyperedges are these touched subsets must be connected. Conversely, any collection of directed simple cycles with connected component-incidence hypergraph, added to the mandatory arcs, yields a connected balanced directed multigraph. It has an Euler circuit, whose bit labels give a circular cover. Consequently, the exact minimum is

\[
L_n=2^{n-1}+\min\left\{\sum_{Q\in\mathcal Q}|Q|:\ \mathcal Q\text{ is a family of simple directed cycles, and its component-incidence hypergraph is connected}\right\}.
\]

Repeated identical supplemental cycles are never needed in an optimum. A cycle touching only one mandatory component cannot assist connectivity and can be discarded. This reduction allows arbitrary duplicated even-weight windows as well as odd-weight windows in the augmentation; excluding either kind can change the answer.

**3. Complete bounded enumeration.** Put \(B_n=(2,3,8,8,14,18)\) at \(n=2,\ldots,7\). The accompanying `witnesses.json` and the constructive Euler traversal in `verify.py` give circular covers with exactly \(2^{n-1}+B_n\) windows. Hence every cycle in a cheapest augmentation has length at most \(B_n\). To exhaust these cycles, the verifier takes each possible least vertex \(u\), traverses both successors \(v\mapsto (2v+b)\bmod 2^{n-1}\), never revisits a vertex other than by returning to \(u\), and visits only vertices greater than \(u\) before closing. Every simple cycle of length at most \(B_n\) appears exactly once, represented from its least vertex.

For each touched-component set \(F\), let \(c(F)\) be the shortest enumerated simple-cycle length with that exact footprint. Keeping one cheapest representative per footprint preserves all possible connectivity improvements. For bitmasks \(S\) of mandatory components containing the anchor, set \(d(\{C_0\})=0\), initially assign infinity to other states, and perform the exhaustive transitions

\[
d(S\cup F)\leftarrow\min\{d(S\cup F),d(S)+c(F)\}\qquad (S\cap F\ne\varnothing).
\]

Each transition strictly increases the bitmask if it changes the state; processing masks in increasing integer order is therefore exhaustive. In any connected hypergraph of chosen cycles there is an ordering, starting at the anchor, in which every new hyperedge meets the already covered components. Thus the recurrence considers every connecting family and cannot underestimate its minimum total cost. The terminal values of the recurrence are precisely \(B_n\).

| \(n\) | Mandatory component count | Simple cycles enumerated | Distinct footprints | Minimum supplementary arcs | Exact \(L_n\) |
|---:|---:|---:|---:|---:|---:|
| 2 | 2 | 3 | 3 | 2 | 4 |
| 3 | 2 | 5 | 3 | 3 | 7 |
| 4 | 4 | 19 | 11 | 8 | 16 |
| 5 | 4 | 41 | 12 | 8 | 24 |
| 6 | 8 | 697 | 90 | 14 | 46 |
| 7 | 10 | 10377 | 529 | 18 | 82 |

**4. Optimal examples and the odd-only boundary.** Every witness in `witnesses.json` is an explicit binary circular word of the indicated length. The checker independently rebuilds its cyclic length-\(n\) factor set and verifies inclusion of all \(2^{n-1}\) required factors. If supplemental arcs are restricted to odd-weight words, the odd arcs alone form a one-in/one-out permutation digraph. A balanced selection must contain whole odd-permutation cycles, possibly repeated; repetitions cannot help connectivity. Exhausting all subsets of these cycles gives the exact restricted augmentation costs \((2,3,8,10,14,21)\) for \(n=2,\ldots,7\). Hence mixing the parity of supplemental windows first improves the optimum at \(n=5\), and improves it again at \(n=7\). The displayed finite evaluations are rigorous because the exhaustive state spaces and termination bounds are specified in the included executable verifier.

## Verification

From the directory containing the supplied artifacts, run `python3 verify.py`; it must print `VERIFY_OK`. It checks the mandated permutation decomposition, enumerates every simple directed cycle within each mathematically sufficient length budget, performs integer-only connected-hypergraph optimization, reconstructs the stated witnesses, and checks every required binary window. Independently, `python3 crosscheck_small.py` enumerates ordinary circular bitstrings for \(n=2,3,4\) and prints `CROSSCHECK_OK`. No integer-programming solver, downloaded data, floating-point approximation, or external library is needed.

## Relationship to prior work

Burstein and Kitaev (public arXiv preprint dated November 23, 2003) study unavoidable word patterns and graph overlap methods, and prove existence of universal cycles for *patterns*. Their equivalence notion is not the set of indexed even-Hamming-weight binary factors, and the statements examined do not give these optimal circular covering lengths.

Sawada, Williams, and Wong (IWOCA 2013) give efficient exact universal cycles for **consecutive weight intervals** \(c,c+1,\ldots,d\). Their method uses Eulerian de Bruijn subgraphs and a gluing lemma. The parity-selected weight set \(\{0,2,4,\ldots\}\cap[0,n]\) is nonconsecutive for \(n\ge2\); its required subgraph is disconnected, and the current problem permits extra windows to make a shortest connected Eulerian supergraph. The consecutive-weight construction does not provide these minima.

Campbell's 2013 thesis also advertises universal cycles for selected contiguous weight ranges. Its abstract was accessible, but the institution-hosted full thesis download returned access denied; it has not been used to assert a whole-document exclusion. The exact historical-priority claim remains qualified by possible unindexed studies of parity-restricted superstrings.

## Limitations

No exact result is asserted for \(n\ge8\), linear (noncyclic) covers, nonbinary alphabets, or parity classes other than even parity. No census of all optimizing circular words is claimed. The finite optimality argument uses explicit exhaustive computation with transparent complete search spaces; the short verifier is a proof checker, not a substitute for independent scientific validation. Priority outside the inspected sources is not independently certified.

## References

1. A. Burstein and S. Kitaev, *On unavoidable sets of word patterns*, arXiv:math/0311399, first submitted 2003-11-23. https://arxiv.org/abs/math/0311399
2. J. Sawada, A. Williams, and D. Wong, *Universal cycles for weight-range binary strings*, IWOCA 2013, LNCS 8288, pp. 388–401, doi:10.1007/978-3-642-45278-9_33. Public author manuscript: https://www.socs.uoguelph.ca/~sawada/papers/den-range.pdf
3. A. A. Campbell, *Universal Cycles for Some Combinatorial Objects*, East Tennessee State University thesis, May 2013, https://dc.etsu.edu/etd/1130/ (abstract accessible; full document inaccessible during inspection).
