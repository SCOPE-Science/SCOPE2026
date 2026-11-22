# Complete monitoring edge-geodetic sets of cycle Mycielskians

## Finding

For every integer \(n\ge5\), let \(H_n=\mu(C_n)\) be the ordinary Mycielskian of the labelled cycle \(C_n\). Write its original vertices as \(U=\{u_i:i\in\mathbb Z/n\mathbb Z\}\), its shadow vertices as \(V=\{v_i:i\in\mathbb Z/n\mathbb Z\}\), and its apex as \(w\). A subset \(S\subseteq V(H_n)\) is a monitoring edge-geodetic set if and only if

\[
 V\subseteq S\quad\text{and}\quad S\cap U\text{ is a vertex cover of }C_n.
\]

There is no restriction on whether \(w\) is selected. Hence the polynomial of **all labelled monitoring sets**, counted by number of selected vertices, is

\[
 \mathcal M_n(z)=z^n(1+z)\sum_{k=0}^{\lfloor n/2\rfloor}
 \frac{n}{n-k}\binom{n-k}{k}z^{n-k}.
\]

Inclusion-minimal monitoring sets correspond bijectively to maximal independent sets of \(C_n\), with \(w\) absent. Their size polynomial is

\[
 \mathcal F_n(z)=\sum_{k=\lceil n/3\rceil}^{\lfloor n/2\rfloor}
 \frac nk\binom{k}{n-2k}z^{2n-k}.
\]

In particular,

\[
 \operatorname{meg}(H_n)=n+\lceil n/2\rceil,
 \qquad
 \#\{\text{minimum monitoring sets}\}=\begin{cases}
 n,&n\text{ odd},\\ 2,&n\text{ even}.
 \end{cases}
\]

The inclusion-minimal sizes form the whole interval from \(\lceil3n/2\rceil\) to \(2n-\lceil n/3\rceil\). Thus the minimal-monitoring-set complex is pure exactly for \(n=5\) and \(n=7\): the two pure instances are separated by the nonpure instance \(n=6\), after which nonpurity persists.

Let \(\mathcal R_n^{\mathrm{jump}}\) (respectively \(\mathcal R_n^{\mathrm{slide}}\)) have the minimum monitoring sets as vertices, with an edge when one selected vertex can be replaced by an unselected vertex (respectively by an adjacent vertex of \(H_n\)) while preserving minimum monitoring throughout. For all \(n\ge5\),

\[
\mathcal R_n^{\mathrm{jump}}=\mathcal R_n^{\mathrm{slide}}\cong
\begin{cases}
 C_n,&n\text{ odd},\\
 2K_1,&n\text{ even}.
\end{cases}
\]

## Assumptions and scope

The graph is finite, unweighted, simple and connected. The edge set of \(H_n\), with indices modulo \(n\), consists exactly of \(u_i u_{i+1}\), \(v_i u_{i-1}\), \(v_i u_{i+1}\), and \(wv_i\) for all indices. A pair of vertices *monitors* an edge if that edge is present on **every** shortest path between the pair. Equivalently, deleting the edge strictly increases their graph distance. A monitoring set has a monitoring pair for every edge. Labels are fixed; no quotient by automorphisms is taken in either polynomial.

An inclusion-minimal monitoring set ceases to be monitoring when any selected vertex is deleted. It need not have minimum cardinality. A one-token replacement preserves cardinality and is required to produce a monitoring set immediately, with no intermediate configurations. Since all graph vertices are distinct, the exact search domain comprises \(2^{2n+1}\) subsets for each finite \(n\).

## Proof

**1. Every shadow is forced.** Fix an index \(i\) and the edge \(wv_i\). If a shortest path contains this edge and has \(v_i\) internally, the path has the two-edge segment \(w-v_i-u_{i-1}\) or \(w-v_i-u_{i+1}\). Replace this segment, respectively, by \(w-v_{i-2}-u_{i-1}\) or \(w-v_{i+2}-u_{i+1}\). Each replacement is a distinct walk of the same length; any repeated vertices in that walk would contradict the original path's shortestness. Consequently, such a path cannot be the unique required use of \(wv_i\). A pair monitoring \(wv_i\) must contain \(v_i\). Every monitoring set therefore contains all shadows.

**2. Each omitted original forces both neighbors.** Consider the shadow edge \(v_{i+1}u_i\). If a shortest path uses this edge with \(v_{i+1}\) internally, the adjoining edge on the other side is \(v_{i+1}w\) or \(v_{i+1}u_{i+2}\). In the first case, reroute \(w-v_{i+1}-u_i\) as \(w-v_{i-1}-u_i\); in the second, reroute \(u_{i+2}-v_{i+1}-u_i\) as \(u_{i+2}-u_{i+1}-u_i\). Thus one endpoint of a monitoring pair must be \(v_{i+1}\).

The only other endpoints for which all shortest paths from \(v_{i+1}\) use \(v_{i+1}u_i\) are \(u_i\) and \(u_{i-1}\). Indeed, \(v_{i+1}\) is adjacent to \(w,u_i,u_{i+2}\). Every other shadow has a route of length at most two via \(w\) which avoids the edge under test. The original vertices accessible in at most two steps from \(v_{i+1}\) are exactly \(u_i,u_{i+2},u_{i-1},u_{i+1},u_{i+3}\); the route through \(u_i\) is unique only for \(u_i\) and \(u_{i-1}\). In particular, the route to \(u_{i+1}\) can go through either \(u_i\) or \(u_{i+2}\), while the route to \(u_{i+3}\) avoids \(u_i\). Every remaining original vertex \(u_j\) is at distance at most three by the alternate three-edge walk \(v_{i+1}-w-v_{j+1}-u_j\), which avoids the tested edge, so none gives a monitoring pair. The stated two monitoring pairs are valid: one is an edge; the other is the unique two-edge path \(v_{i+1}-u_i-u_{i-1}\). All claims remain valid for \(n=5\), the smallest permitted order.

It follows that a monitoring set excluding \(u_i\) must select \(u_{i-1}\), to monitor \(v_{i+1}u_i\). Applying the reversed argument to \(v_{i-1}u_i\) also forces \(u_{i+1}\). Thus the omitted original vertices form an independent set, or equivalently the selected originals form a vertex cover of \(C_n\).

**3. Sufficiency.** Assume that all shadows are selected and the originals selected form a vertex cover. Every apex edge \(wv_i\) is monitored by \(v_i,v_{i+1}\): their unique length-two path goes through \(w\), because these shadows have no common original neighbor for \(n\ge5\). For a shadow edge \(v_{i+1}u_i\), if \(u_i\) is selected, the endpoints monitor it; otherwise \(u_{i-1}\) is selected and \(v_{i+1},u_{i-1}\) monitor it along their unique two-step path. The reverse-index shadow edges follow similarly. Finally, for a rim edge \(u_i u_{i+1}\), if \(u_i\) is selected, the unique two-step path to the selected shadow \(v_{i+2}\) runs via \(u_{i+1}\). If \(u_i\) is omitted, \(u_{i+1}\) is selected, and the unique two-step path from \(u_{i+1}\) to \(v_{i-1}\) runs via \(u_i\). This monitors every edge; including or excluding the apex does not affect validity.

**4. Exact counting.** Let \(k\) be the number of unselected originals. These form an independent set of the labelled cycle, of which there are exactly \(\frac{n}{n-k}\binom{n-k}{k}\) of size \(k\), for \(0\le k\le\lfloor n/2\rfloor\). The selected shadows contribute \(n\) vertices and the apex contributes the independent factor \(1+z\), proving the first polynomial. An inclusion-minimal set must omit \(w\) and have an inclusion-minimal vertex cover, or equivalently a maximal independent omitted set. If such a maximal independent set has \(k\) vertices, its cyclic gaps are all either two or three; there are \(n-2k\) gaps of three. Rooting one of the \(k\) selected gap starts proves the count \(\frac nk\binom{k}{n-2k}\). These configurations exist precisely when \(\lceil n/3\rceil\le k\le\lfloor n/2\rfloor\), proving the second polynomial and the purity assertion. Maximum independent sets have size \(\lfloor n/2\rfloor\), giving the minimum value and counts.

**5. Optimal relocation.** At minimum cardinality the shadows are fixed, the apex is absent, and an optimum is encoded by a maximum independent set of the cycle. If \(n\) is even there are exactly two alternating independent sets. They cannot be related by one replacement for \(n\ge6\), yielding \(2K_1\). If \(n=2k+1\), the \(n\) maximum independent sets are
\[
 I_r=\{r,r+2,\ldots,r+2(k-1)\}\pmod n,
 \qquad r\in\mathbb Z/n\mathbb Z.
\]
A permissible one-replacement move joins precisely \(I_r\) to \(I_{r\pm2}\): the exchanged original vertices are consecutive in the underlying cycle. This is also an edge-slide. Since two is coprime to odd \(n\), the exchange graph is one cycle of length \(n\). This completes the proof.

## Verification

The standalone `verify.py` constructs the cycle Mycielskian directly and, for each edge, recomputes all graph distances after its deletion. It checks the monitoring predicate against the structural criterion for **every vertex subset** at \(n=5,6,7,8,9\), including all coefficient counts, every inclusion-minimal set, and all one-token jumps and slides. This checks \(2^{11}+2^{13}+2^{15}+2^{17}+2^{19}=698{,}368\) vertex subsets. For \(10\le n\le15\), it additionally checks the precise two-pair certificate of each representative shadow edge, using independently computed shortest-path distances. The executable returns `VERIFY_OK` when all checks pass. The proof above, not the finite enumeration, establishes the assertions for every \(n\ge5\).

For illustration, at \(n=5\), \(\mathcal M_5(z)=5z^8+10z^9+6z^{10}+z^{11}\) and \(\mathcal F_5(z)=5z^8\). At \(n=6\), the inclusion-minimal polynomial is \(2z^9+3z^{10}\); at \(n=7\) it returns to the single size \(7z^{11}\).

Run with an ordinary Python 3 interpreter: `python3 verify.py`. No third-party packages are required.

## Relationship to prior work

The 2022 introduction of monitoring edge-geodetic sets by Dev, Dey, Foucaud, Narayanan and Ramasubramony Sulochana gives foundational definitions and studies trees, cycles, unicyclic graphs, complete multipartite graphs, grids, hypercubes and corona products; the present complete enumeration concerns their Mycielski transforms, which contain additional vertices and four-cycles. Haslegrave's 2022 preprint (published 2023) establishes bounds for Cartesian and strong products, not this graph operation. Foucaud and coauthors' 2024 preprint (published 2025) proves, among other results, that a vertex cover of a graph of girth at least five is monitoring edge-geodetic; that sufficient condition does not apply to \(\mu(C_n)\), which has four-cycles, nor does it force the shadow set or give the present equivalence and enumerations. Bianchi and coauthors study locating and locating-total domination under the Mycielski construction, including cycle inputs, but those are different neighbor-signature requirements and do not imply this edge-failure monitoring claim.

The value here is a complete infinite-family description of fault-detecting sensor configurations and a precise identification with the independent-set complex of a cycle. It also determines the nonpure inclusion-minimal cardinality spectrum and the parity-sensitive optimal reconfiguration geometry.

## Limitations

The theorem is restricted to ordinary Mycielskians of simple cycles of order at least five. No statement is made for arbitrary base graphs, weighted networks, simultaneous edge failures, or sensor replacement via intermediate nonmonitoring configurations. The checker verifies finite instances, not the universal claim. Literature comparison does not establish exhaustive global publication priority; independent mathematical validation has not been performed.

## References

1. S. R. Dev, S. Dey, F. Foucaud, N. Krishna and L. R. Sulochana, *Monitoring edge-geodetic sets in graphs*, first posted 2022-10-07, arXiv:2210.03774, https://arxiv.org/abs/2210.03774.
2. J. Haslegrave, *Monitoring edge-geodetic sets: hardness and graph products*, first posted 2022-10-17, arXiv:2210.08955, https://arxiv.org/abs/2210.08955.
3. F. Foucaud, C. Marcille, Z. M. Myint, R. B. Sandeep, S. Sen and S. Taruni, *Bounds and extremal graphs for monitoring edge-geodetic sets in graphs*, first posted 2024-03-14, arXiv:2403.09122, https://arxiv.org/abs/2403.09122.
4. S. M. Bianchi, D. Chakraborty, Y. Lucarini and A. K. Wagler, *Location-Domination Type Problems Under the Mycielski Construction*, first posted 2023-11-23, arXiv:2311.13979, https://arxiv.org/abs/2311.13979.
