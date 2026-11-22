# Sharp eccentricities for size-constrained connected bipartitions of cycles

## Finding
Fix integers \(n\ge3\) and \(1\le s\le\lfloor n/2\rfloor\). The single-vertex-switch graph on **unordered** connected two-district partitions of \(C_n\), requiring each district to contain at least \(s\) vertices, has \(n(n-2s+1)/2\) states. At \(n=2s\) its \(n/2\) states are all isolated. If \(n>2s\), it is connected with \(n(n-2s)\) edges, and for a partition whose smaller district has size \(d\) its eccentricity is
\[
\operatorname{ecc}(d)=\max\{\lfloor n/2\rfloor,\ n-s-d\}.
\]
Consequently its radius is \(\lfloor n/2\rfloor\) and its diameter is \(\max\{\lfloor n/2\rfloor,n-2s\}\).

## Assumptions and scope
The underlying cycle has **labelled** vertices \(0,\ldots,n-1\) and edges indexed cyclically by \(0,\ldots,n-1\). The two districts themselves are unlabelled; swapping district names leaves a single state. Each district induces a connected graph. A move changes one vertex's district and is allowed only when both resulting districts remain connected and have at least \(s\) vertices. Eccentricity, radius and diameter refer to the ordinary *undirected*, unweighted reconfiguration graph; the diameter of disconnected frozen cases is not asserted. The parameter \(s\) is a lower bound on **both** district sizes, not a bound on their difference.

## Proof
**Cut-edge encoding.** Each connected unordered two-part partition of a cycle corresponds uniquely to the unordered pair \(\{a,b\}\) of its two boundary edges. If its clockwise edge separation is \(h\), its district sizes are \(h\) and \(n-h\). Feasibility is precisely \(s\le h\le n-s\). Moving one boundary vertex corresponds to moving exactly one of the two cut edges by one edge, provided feasibility is maintained. Thus the state graph is the hard-core two-particle sliding graph on the labelled edge cycle, with cyclic separation at least \(s\). Summing allowed separations gives \(n(n-2s+1)/2\) states. If \(n=2s\), both districts have exactly \(s\) vertices, and any switch violates the bound; hence there are \(n/2\) isolates.

**Exact distance.** Assume \(n>2s\). A feasible state has an integer lift \((x,y)\in\mathbb Z^2\) with \(s\le y-x\le n-s\). The graph on such lifts uses horizontal and vertical unit edges. It is isometric for the Manhattan metric: to reach another lift, move each coordinate monotonically toward its target. If a proposed monotone coordinate move leaves the strip at \(y-x=s\), then the other remaining monotone move must lead inward, unless the target lies outside the strip; the same holds at \(y-x=n-s\). Thus a monotone feasible move always exists until the target is attained. Projecting integer lifts to the edge cycle, the only lifts of a target \(\{c,e\}\) (where \(0\le c<e<n\)) are \((c+qn,e+qn)\) and \((e+qn,c+(q+1)n)\), for integers \(q\). Consequently, for a source \(\{a,b\}\) with \(0\le a<b<n\),
\[
\operatorname{dist}(\{a,b\},\{c,e\})=\min_{q\in\mathbb Z}\left\{\begin{array}{l}
|c+qn-a|+|e+qn-b|,\\
|e+qn-a|+|c+(q+1)n-b|
\end{array}\right\}.
\]
Only \(-2\le q\le2\) need be searched for positions in the canonical range. This formula proves connectivity. It is also valid in the unconstrained cycle's two-token graph; the **new extremal assertion below** concerns the size-constrained state's eccentricity, not priority for this transport principle.

**Upper eccentricity bound.** Rotate the source to \(\{0,d\}\), with \(s\le d\le m=\lfloor n/2\rfloor\). Let \(T\) be an arbitrary feasible pair. If the four cuts alternate around the cycle, the two noncrossing order-preserving pairings have complementary total lengths \(v\) and \(n-v\); hence distance at most \(m\). If both target cuts lie on the shorter source arc of length \(d\), their pairings from the two bounding source cuts have sum at most \(d\le m\). If both target cuts lie on the longer source arc, with target-pair separation there at least \(s\), its two outside gaps together have length at most \(n-d-s\); the pairing along these gaps is feasible by the lift argument. Cases with shared cuts are limiting instances of these cases (with zero gaps). Therefore
\[
\operatorname{ecc}(\{0,d\})\le\max\{m,n-s-d\}.
\]

**Matching witnesses.** To attain \(m\), put \(t=\lfloor d/2\rfloor\), \(u=m-t\), and choose \(T_1=\{t,d+u\}\) (interpreted modulo \(n\)). Its two cyclic gaps have sizes \(m+(d\bmod2)\) and \(n-m-(d\bmod2)\), both at least \(s\) for \(n>2s\); the lift formula gives distance \(m\). To attain \(L=n-s-d\), put \(\alpha=\lfloor L/2\rfloor\) and \(T_2=\{d+\alpha,d+\alpha+s\}\), taken cyclically. It is feasible since its two gaps are \(s\) and \(n-s\). The distance formula evaluates to
\[
\min\{L,\ d+s+2\alpha,\ 2n-d-s-2\alpha\}=L,
\]
with the last two expressions at least \(L\). Thus the stated eccentricity follows. Its minimum across \(d\in[s,m]\) is \(m\), and maximum is \(\max\{m,n-2s\}\).

**Edge count.** For \(n>2s\) there are precisely \(n\) states with smaller *oriented* gap at the lower boundary \(s\), of degree two; if \(n=2s+1\), these exhaust all \(n\) states. Every other configuration has degree four. Hence degree sum is \(2n+4(\,n(n-2s+1)/2-n\,)=2n(n-2s)\), and the edge count is \(n(n-2s)\).

## Verification
The standalone `verify.py` independently enumerates each unordered cut-pair, generates legal moves by modifying one edge index modulo \(n\), performs breadth-first search for every state, and compares **every** computed distance to the integer-lift formula and every eccentricity to the claimed expression. It additionally checks state and edge counts and the frozen boundary. Run `python3 verify.py` from the directory containing the script. It passed every \(n=3,\ldots,30\) and \(1\le s\le\lfloor n/2\rfloor\): 224 cases, 26,999 state incidences and 5,572,560 ordered-pair comparisons. These finite checks are corroboration; the all-parameter argument above provides the proof.

## Relationship to prior work
Akitaya et al., *Reconfiguration of Connected Graph Partitions* (arXiv:1902.10765, first public 2019-02-27), develop general single-switch partition connectivity and coarse diameter bounds, without this size-constrained two-district cycle eccentricity formula in the examined theorem statements. Their *Reconfiguration of Connected Graph Partitions via Recombination* (arXiv:2011.07378) studies a different move. The original token-graph study by Fabila-Monroy et al. (arXiv:0910.4774) and the cycle token-graph spectral paper arXiv:2403.20148 provide related models but not the exact eccentricity expression in the relevant sections examined. General bounded-gap cyclic token transport-optimality is existing work and is **not** claimed new. The specific claimed contribution is the sharp extremal metric and threshold for minimum-size constrained connected district partitions.

## Limitations
The result is for an unweighted simple labelled cycle, exactly two **unnamed** connected districts and one-vertex switch moves; it does not establish balance-constrained mixing time, higher-district formulae, arbitrary host graphs or a diameter for the disconnected frozen case. An equivalent extremal metric could exist in historical hard-core particle/redistricting terminology not identified by the literature comparison. The manuscript has not undergone independent expert review.

## References
1. H. A. Akitaya et al., *Reconfiguration of Connected Graph Partitions*, arXiv:1902.10765v1 (2019), https://arxiv.org/abs/1902.10765.
2. H. A. Akitaya et al., *Reconfiguration of Connected Graph Partitions via Recombination*, arXiv:2011.07378v1 (2020), https://arxiv.org/abs/2011.07378.
3. R. Fabila-Monroy et al., *Token Graphs*, arXiv:0910.4774 (2009), https://arxiv.org/abs/0910.4774.
4. *General method to find the spectrum and eigenspaces of the \(k\)-token graph of a cycle*, arXiv:2403.20148v1 (2024), https://arxiv.org/abs/2403.20148.
