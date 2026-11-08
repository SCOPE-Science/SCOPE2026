# The five orbit types and exact minimum-zero-forcing propagation-time spectrum of Möbius ladders

## Finding

Let \(M_{2n}=C_{2n}(1,n)\) be the Möbius ladder on the vertex set \(\mathbb Z/(2n)\), with edges joining each vertex to its two cyclic neighbours and its antipode. For every integer \(n\ge4\), its minimum zero-forcing number is \(\operatorname Z(M_{2n})=4\). Its minimum four-vertex zero-forcing sets form precisely five orbits under rotations and reflections of the underlying \(2n\)-cycle, with a total of \(13n\) labelled sets.

Write \(\operatorname{pt}(S)\) for the number of synchronous rounds required when every possible zero-forcing move is made at each round. The complete generating polynomial \(F_n(z)=\sum_{S:\,|S|=4,\,S\text{ zero forcing}}z^{\operatorname{pt}(S)}\) is
\[
F_n(z)=\begin{cases}
nz^{m-1}+8nz^m+4nz^{m+1},&n=2m,\\
3nz^m+6nz^{m+1}+4nz^{m+2},&n=2m+1.
\end{cases}
\]
In particular, the minimum and maximum propagation times are \(\lfloor(n-1)/2\rfloor\) and \(\lfloor(n+3)/2\rfloor\). There are exactly \(n\) fastest minimum sets for even \(n\) and \(3n\) for odd \(n\). Each of the three consecutive integers in the propagation-time interval occurs.

The five orbit representatives and exact data are:

| Type | Initial four vertices | Orbit size | Propagation time |
|---|---|---:|---|
| A | \(\{0,1,2,3\}\) | \(2n\) | \(\lfloor(n+1)/2\rfloor\) |
| B | \(\{0,1,2,n\}\) | \(4n\) | \(\lfloor(n+1)/2\rfloor\) |
| C | \(\{0,1,3,n+1\}\) | \(4n\) | \(\lfloor(n+3)/2\rfloor\) |
| D | \(\{0,1,n-1,n\}\) | \(2n\) | \(\lfloor n/2\rfloor\) |
| E | \(\{0,1,n,n+1\}\) | \(n\) | \(\lfloor(n-1)/2\rfloor\) |

## Assumptions and scope

All graphs are finite, simple, undirected. The vertices are individually labelled by residues modulo \(2n\), and only \(n\ge4\) is asserted. A blue vertex with exactly one white neighbour makes that white neighbour blue at the next synchronous round. The process never reverses a blue colour. The theorem concerns **all** minimum-cardinality zero-forcing sets of the stated graph, not larger starting sets or other forcing rules. It does not assert a formula for the full zero-forcing polynomial at larger cardinalities. The six-vertex graph \(M_6\cong K_{3,3}\) lies outside the uniform orbit statement.

## Proof

**1. The lower bound and the finite list of candidates.** The graph is cubic. A first force from a starting set of at most three blue vertices requires a blue centre with two blue neighbours, hence exactly a blue triple of one of the two types, up to rotation and reflection:
\[
T_{\rm rim}=\{0,1,2\},\qquad T_{\rm mixed}=\{0,1,n\}.
\]
Starting from either triple alone, the first round colours just one more vertex, after which no further force is possible. Thus no three-set forces the entire graph. The four-set of type E listed above does force the graph, as shown by the explicit timings below, so \(\operatorname Z(M_{2n})=4\).

Any successful four-set has a first force and therefore contains one of these triples. Let its fourth vertex be \(k\). A direct examination of the three-neighbour rule shows that after at most one round the process stalls unless
\[
\begin{aligned}
T_{\rm rim}:\quad &k\in\{3,n,n+2,2n-1\},\\
T_{\rm mixed}:\quad &k\in\{2,n-1,n+1,2n-2\}.
\end{aligned}
\]
For completeness, with \(T_{\rm rim}\) the only possible first new blue vertex away from the fourth seed is \(n+1\). To permit a further force, the fourth seed must touch an existing exposed frontier at \(0\), \(2\), or \(n+1\), yielding precisely the four displayed options. With \(T_{\rm mixed}\), the analogous new vertex is \(2n-1\), and the only possible frontier supports yield the other four options. If the fourth seed itself is the would-be forced vertex, that first force is blocked rather than helped. These checks remain valid at \(n=4\).

The eight possible completions reduce under the dihedral rotations/reflections to A--E: the first line gives A or B, and the second gives B, C, D, or E. The five types are distinct: A is the four-vertex rim path with no rung edges; B is a four-vertex path with its only rung as an end edge; D is such a path with its only rung as the middle edge; C is an induced three-vertex path with an isolated fourth vertex; E is an induced four-cycle with two rungs. Comparing the stabilizers of the cyclic action and its reflections gives the orbit sizes \(2n,4n,4n,2n,n\), respectively. The total is \(13n\). (Here ``rim path'' means a four-vertex path using only rim edges.)

**2. Exact timed forcing on the five representatives.** Put \(x_i=i\) and \(y_i=n+i\), for \(0\le i<n\). The two layers have horizontal edges between consecutive indices and rungs \(x_i y_i\). At the ends, the horizontal edges are twisted: \(x_0y_{n-1}\) and \(x_{n-1}y_0\). Set \(\tau(v)=0\) for a seed and let \(\tau(v)\) otherwise denote its first blue round. The following table gives **every vertex's** exact arrival time; each row is valid for every \(n\ge4\). The indicated ``otherwise'' range is \(4\le i\le n-1\) in A and C, \(3\le i\le n-1\) in B for \(x_i\), and the other ranges follow the stated cases.

| Type | \(\tau(x_i)\) | \(\tau(y_i)\) |
|---|---|---|
| A | \(0\) for \(i\le3\); otherwise \(\min(i-1,n+2-i)\) | \(2\) for \(i=0,3\), \(1\) for \(i=1,2\); otherwise \(\min(i-1,n+2-i)\) |
| B | \(0\) for \(i\le2\); otherwise \(\min(i,n+1-i)\) | \(0\) for \(i=0\), \(1\) for \(i=n-1\); otherwise \(\min(i,n+1-i)\) |
| C | \(0\) for \(i=0,1,3\), \(1\) for \(i=2\); otherwise \(\min(i,n+3-i)\) | \(3,0,2,3\) at \(i=0,1,2,3\), respectively; otherwise \(\min(i,n+3-i)\) |
| D | \(0\) for \(i=0,1,n-1\); otherwise \(\min(i,n-i)\) | \(0\) for \(i=0\); otherwise \(\min(i,n-i)\) |
| E | \(0\) for \(i=0,1\); otherwise \(\min(i-1,n-i)\) | same as for \(x_i\) |

Here is a direct check that this table proves the times, rather than merely bounding them. If \(\tau=0\) on exactly the four seeds, a proposed integer-valued arrival table is the actual synchronous forcing evolution precisely when, for every nonseed vertex \(v\),
\[
\tau(v)=1+\min_{u\sim v}\ \max_{w\in N[u]\setminus\{v\}}\tau(w).
\tag{1}
\]
The minimum is over its three neighbours. The maximum includes \(u\) and its two neighbours other than \(v\). Indeed, \(u\) can first force \(v\) exactly one round after the last member of that set is blue. The equation and the four seed values determine the successive blue sets by induction on the round.

To check (1) in the displayed table, use \(N(x_i)=\{x_{i-1},x_{i+1},y_i\}\) and \(N(y_i)=\{y_{i-1},y_{i+1},x_i\}\) away from the ends, together with the two twisted end edges. For each type, the explicitly listed first four column values handle the initial front; at interior columns each value is the minimum of the arrival times from the forward and backward fronts, of slopes \(+1\) and \(-1\). On each side of their crossing, substituting the corresponding affine branch into (1) gives the displayed value; at the crossing the two possible predecessor forces agree or meet. The end cases are obtained using \(x_0y_{n-1}\) and \(x_{n-1}y_0\). This proves the five tables for all \(n\ge4\) by the local recurrence, including the small boundary case \(n=4\). The attached programs separately replay the recurrence and the direct forcing dynamics for finite orders.

**3. Reading off the extremal times and multiplicities.** Maximizing each of the five arrival-time rows gives the times shown in the first table. For \(n=2m\), the E sets are at time \(m-1\), types A, B, D at time \(m\), and C at time \(m+1\). Their orbit counts yield \(n,8n,4n\). For \(n=2m+1\), D and E are at time \(m\), A and B at time \(m+1\), and C at time \(m+2\), yielding \(3n,6n,4n\). This is the claimed polynomial, interval and fastest-set count.

## Verification

The attached self-contained Python program enumerates every four-subset and every legal synchronous forcing sequence for \(4\le n\le18\), checks all five dihedral orbit sizes, and separately excludes three-vertex forcing sets through \(n=11\). It does not use the symbolic arrival-time formulas.

The separately implemented C++17 program represents the blue set by a bitmask and exhaustively checks the complete time distribution for \(4\le n\le23\). It also checks the independent local recurrence (1) for all five closed-form timing tables for \(4\le n\le3000\). Both extracted programs were compiled/executed and passed. These finite tests corroborate, but do not replace, the all-order proof above.

## Relationship to prior work

The classical exact zero-forcing number \(\operatorname Z(M_{2n})=4\) is previously known and is not claimed as new; it is restated to identify the minimum-cardinality sets. Chilakamarri--Dean--Kang--Yi (arXiv:1105.1492v1, publicly posted 2011-05-08) introduced the iteration index; Hogben and collaborators (arXiv:1410.4191v1, 2014-10-15) developed propagation-time questions. Boyer and collaborators (arXiv:1801.08910v1, 2018-01-26) studied the zero-forcing polynomial, including its minimum-set coefficient. Duong and collaborators (arXiv:1906.03079v1, 2019-06-07), in Theorems 4.1 and 5.2, explicitly treat the Möbius ladder's zero-forcing number but do not classify the minimum sets or their simultaneous propagation-time spectrum. The assessed contribution is precisely the five-orbit description, exact \(13n\) count, and the complete three-term propagation-time polynomial. It is neither an evaluation of an existing general formula nor a restatement of \(\operatorname Z=4\).

## Limitations

The conclusion is for the Möbius ladder with at least eight vertices, and only for its smallest forcing sets under synchronous standard zero forcing. It does not classify all forcing sets of arbitrary size or assert a similar result for untwisted circular ladders. The original 2008 zero-forcing paper was identified, but its full text was not obtained; its known \(\operatorname Z=4\) conclusion is not novel here. A previously unindexed equivalent enumeration cannot be ruled out solely by literature searches. This is a mathematical proof with reproducible finite checks, not an independent scholarly audit.

## References

- K. B. Chilakamarri, N. Dean, C. X. Kang, E. Yi, *Iteration Index of a Zero Forcing Set in a Graph*, arXiv:1105.1492v1, first posted 2011-05-08, https://arxiv.org/abs/1105.1492.
- L. Hogben, M. Huynh, N. Kingsley, S. Meyer, S. Walker, M. Young, *Propagation time for zero forcing on a graph*, arXiv:1410.4191v1, first posted 2014-10-15, https://arxiv.org/abs/1410.4191.
- AIM Minimum Rank--Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications 428 (2008), 1628--1648, https://doi.org/10.1016/j.laa.2007.10.009 (full text not obtained).
- K. Boyer et al., *The zero forcing polynomial of a graph*, arXiv:1801.08910v1, first posted 2018-01-26, https://arxiv.org/abs/1801.08910.
- L. Duong, B. K. Kroschel, M. Riddell, K. N. Vander Meulen, A. Van Tuyl, *Maximum nullity and zero forcing of circulant graphs*, arXiv:1906.03079v1, first posted 2019-06-07, https://arxiv.org/abs/1906.03079.
