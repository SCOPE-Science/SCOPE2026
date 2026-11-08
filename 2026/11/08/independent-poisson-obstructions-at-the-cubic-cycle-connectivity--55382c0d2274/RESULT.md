# Independent Poisson obstructions at the cubic-cycle connectivity window

## Finding

**Theorem.** Let \(G_n\) be obtained by independently retaining every edge of the third power \(C_n^3\) of the \(n\)-cycle with probability \(1-q_n\). Suppose \(q_n\in(0,1)\) and
\[
nq_n^6\longrightarrow\lambda\in(0,\infty).
\]
Let \(I_n\) count isolated vertices and \(W_n\) count *unbridged cyclic gaps*: a gap between adjacent vertices is unbridged when all six edges of lengths at most three that cross it are absent. Then
\[
(I_n,W_n)\Longrightarrow(P_1,P_2),
\]
where \(P_1,P_2\) are **independent** Poisson random variables of mean \(\lambda\). Moreover,
\[
\Pr\bigl(G_n\text{ disconnected},\ I_n=0,\ W_n\le1\bigr)
=O(q_n+nq_n^7+nq_n^{10})=o(1),
\]
with absolute implicit constants, and therefore
\[
\boxed{\lim_{n\to\infty}\Pr(G_n\text{ connected})=e^{-2\lambda}(1+\lambda).}
\]
The point \(C_n^3\) is the equal-rate finite-bandwidth case in which isolated-vertex and unbridged-gap obstructions coexist on the same scale. This theorem concerns the connectivity probability and the two obstruction counts, not an exact law for every component size.

## Assumptions and scope

Vertices are indexed by \(\mathbb Z/n\mathbb Z\), with \(n\ge16\) for the finite geometric arguments. Each unordered edge \(\{i,i+j\}\), \(j=1,2,3\), is present independently with probability \(1-q_n\). At a gap after vertex \(i\), the six crossing edges are
\[
\{i,i+1\},\ \{i-1,i+1\},\ \{i,i+2\},\ \{i-2,i+1\},\ \{i-1,i+2\},\ \{i,i+3\}.
\]
They are all required absent for the gap to be counted by \(W_n\). Each isolated-vertex event likewise requires six absent edges. The limit assumes \(nq_n^6\to\lambda\in(0,\infty)\); there is no assumption of independence among the *obstruction indicators*.

## Proof

**1. The two rare-event fields have an independent Poisson limit.** Write \(A_i\) for isolation of vertex \(i\), and \(B_i\) for the unbridged gap after vertex \(i\). Each is the event that a specified six-element set of independent edges is deleted, hence
\[
\Pr(A_i)=\Pr(B_i)=q_n^6.
\]
An event depends only on edges within cyclic distance at most three of its center. Any two distinct events whose edge sets intersect require at least **nine distinct deleted edges**: two isolation supports have union size at least eleven, two gap supports at least nine, and mixed isolation/gap supports at least nine. These finite support assertions follow by examining the six listed edges under cyclic shifts; `artifacts/verify.py` independently enumerates them.

For every pair of fixed nonnegative integers \(r,s\), expand the mixed factorial moment \(\mathbb E[(I_n)_r(W_n)_s]\) over distinct indicated vertices and gaps. Tuples with mutually disjoint edge supports contribute \((nq_n^6)^{r+s}(1+o(1))\). All other tuples can be grouped into a bounded number of connected clusters in the finite-range dependence graph. A cluster with one event costs a factor \(q_n^6\); one with at least two events costs at most \(q_n^9\). With a fixed number of events there are \(O(n^b)\) tuples with \(b\) clusters, so their total contribution with any nontrivial cluster is
\[
O\bigl((nq_n^6)^b q_n^3\bigr)=o(1).
\]
Therefore all mixed factorial moments tend to \(\lambda^{r+s}\), characterizing two independent Poisson variables. Standard tightness follows from the bounded means \(\mathbb EI_n=\mathbb EW_n=nq_n^6\).

**2. The two obstructions necessarily disconnect.** Any isolated vertex disconnects the graph for \(n>1\). Two distinct unbridged gaps cut the circle into at least two arcs, with no retained edge crossing either gap; hence \(W_n\ge2\) also forces disconnection. Thus connectivity implies \(I_n=0\) and \(W_n\le1\).

**3. All other obstructions are negligible at the critical scale.** We use the deterministic envelope decomposition in Federico, Proposition 5.4 (2024), which classifies a disconnected bounded-range cyclic graph with no isolated vertices and at most one unbridged gap into one of three exceptional patterns: two wrapping components (\(W_1\)); a nontrivial component of cyclic diameter strictly less than three (\(W_2\)); or two intertwined components (\(W_3\)). The geometrical argument is as follows. Components with disjoint cyclic envelopes generate at least two unbridged gaps; overlapping envelopes are either wrapping, intertwined, or contain an enclosed component narrower than the interaction range. This covers all cases without assuming components are intervals.

For \(W_1\), every three successive nearest-neighbor positions include a deleted nearest-neighbor edge, since two distinct components wrap around the entire circle. At least \(n/3\) such edges are absent. Markov's inequality gives \(\Pr(W_1)\le3q_n\).

For \(W_2\), a nontrivial component of diameter below three consists of a pair at cyclic distance one or two, or three consecutive vertices. These sets have respectively ten or twelve boundary edges in \(C_n^3\), all of which must be absent. Counting \(2n\) pairs and \(n\) triples yields
\[
\Pr(W_2)\le2nq_n^{10}+nq_n^{12}\le3nq_n^{10}.
\]
For \(W_3\), the local overlap-witness argument in Federico, Lemma 5.7 (2024), applies at this critical scale as well: an intertwined pair gives a monotone chain of \(k\ge3\) local witnesses, with at most \(n3^{k-1}\) possible chains and **at least \(6+(k-2)=k+4\) distinct absent edges** per chain (the six outward boundary edges and \(k-2\) interior nearest-neighbor edges). Directly summing the geometric series when \(q_n<1/3\) gives
\[
\Pr(W_3)\le n\sum_{k\ge3}3^{k-1}q_n^{k+4}
=\frac{9nq_n^7}{1-3q_n}.
\]
These bounds are meaningful precisely at the critical scaling: \(q_n\to0\), \(nq_n^7=(nq_n^6)q_n\to0\), and \(nq_n^{10}=(nq_n^6)q_n^4\to0\). Combining the deterministic trichotomy and three bounds proves the stated \(o(1)\) error for the connectivity event.

**4. Limit.** Steps 2–3 imply
\[
\Pr(G_n\text{ connected})=\Pr(I_n=0,W_n\le1)+o(1).
\]
By Step 1 the limit is \(\Pr(P_1=0)\Pr(P_2\le1)=e^{-2\lambda}(1+\lambda)\).

## Verification

The standalone script `artifacts/verify.py` executes 53,256 finite checks (cycle lengths 12, 14, 16, 15, 17, 18, 24 and 40). It verifies all six-edge local supports, the nine-edge minimum for overlapping distinct obstruction events, the ten/twelve-edge boundaries of candidate small components, exhaustive small-cycle edge-cut minima, and the unique equality of the two obstruction exponents at bandwidth three. Run `python3 artifacts/verify.py`. These calculations check finite geometric premises only; the factorial-moment and rare-witness arguments above provide the infinite proof.

## Relationship to prior work

Chakraborty, Luh and Singh (arXiv:2610.42107, posted 2026-10-30) prove a Poisson isolation law and connectivity limit in the growing-bandwidth regime and explicitly pose the small-bandwidth critical-window problem (Section 7). Their assumptions exclude fixed bandwidth three. Federico (2024, Theorem 2.1) establishes the off-critical zero-one threshold for a more general bounded-range cycle model and identifies isolated vertices and unbridged gaps as the two obstruction families. His Sections 3–5 provide the geometric trichotomy and witness-chain ideas reused and strengthened here. That paper does not state the joint independent-Poisson law or the critical equality-case connectivity limit. Wilsher, Dettmann and Ganesh (2020) concern a continuous one-dimensional soft random geometric graph, not this finite discrete cycle-power formula.

For uniform edge deletion in a cycle power of fixed bandwidth \(m\), an unbridged gap costs \(m(m+1)/2\) deleted edges while vertex isolation costs \(2m\). Equality holds uniquely at \(m=3\). The present result determines the critical distribution at that tie, rather than merely restating the known threshold exponents.

## Limitations

The theorem does not establish a full joint component-size distribution or cover arbitrary fixed bandwidths and nonuniform length-dependent edge probabilities. The finite verifier is not a proof of infinite asymptotics. The bound for intertwined components uses the published geometric witness classification; its critical-scale numerical specialization is demonstrated above. Definitive historical priority beyond the inspected primary literature remains unverified.

## References

1. Shantanav Chakraborty, Kyle Luh, Rudransh Pratap Singh, *Band Random Graphs: Connectivity, Geometry, and Transport*, arXiv:2610.42107v1 (2026-10-30). https://arxiv.org/html/2610.42107v1 (especially Section 7).
2. Lorenzo Federico, *Connecting probability for random bounded-range one-dimensional network*, Annali dell'Università di Ferrara 70 (2024), 1389–1403. https://doi.org/10.1007/s11565-024-00508-6 (especially Proposition 5.4 and Lemmas 5.5–5.7).
3. M. Wilsher, C. P. Dettmann, A. Ganesh, *Connectivity in one-dimensional soft random geometric graphs*, Physical Review E 102 (2020), 062312. Cited for related continuous-space connectivity phenomena only.
