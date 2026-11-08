# Exact monitoring edge-geodetic sets of subdivided complete graphs

## Finding

For every integer \(n\ge3\), let \(\Sigma_n\) be obtained by subdividing every edge of \(K_n\) exactly once. Its vertices are original vertices \(v_i\), \(i\in[n]\), and subdivision vertices \(w_{ij}=w_{ji}\), \(1\le i<j\le n\). Put \(N=\binom n2\). A vertex subset monitors an edge when that edge belongs to every shortest path between some pair of selected vertices. A *monitoring edge-geodetic set* (MEG-set) monitors every edge.

**Exact structural theorem.** A set \(S\subseteq V(\Sigma_n)\) is an MEG-set **if and only if it is a vertex cover** of \(\Sigma_n\). Equivalently, if \(A=\{i:v_i\in S\}\), then for each unordered pair \(\{i,j\}\not\subseteq A\), the subdivision vertex \(w_{ij}\) must belong to \(S\); subdivision vertices \(w_{ij}\) with \(i,j\in A\) are arbitrary.

Let \(P_n(z)=\sum_{S:\,S\text{ MEG}}z^{|S|}\). Then
\[
P_n(z)=\sum_{k=0}^n\binom nk z^{k+N-\binom k2}(1+z)^{\binom k2}.
\]

**Exact inclusion-minimal family.** Let \(Q_n(z)\) count inclusion-minimal MEG-sets by cardinality. Such sets are precisely
\[
S_A=\{v_i:i\in A\}\cup\{w_{ij}:\{i,j\}\not\subseteq A\},
\qquad |A|=0\ \text{or}\ 2\le |A|\le n.
\]
They are all distinct, and
\[
Q_n(z)=z^N+\sum_{k=2}^n\binom nk z^{N+k-\binom k2}.
\]
Consequently there are exactly \(2^n-n\) inclusion-minimal MEG-sets. The minimum MEG-set cardinality is \(n\) (unique when \(n\ge4\), and attained by two sets when \(n=3\)); the largest cardinality of an inclusion-minimal MEG-set is \(N+1\). The minimal-cardinality spectrum is precisely
\[
\{N\}\cup\{N+k-\binom k2:2\le k\le n\}.
\]
These spectra have arbitrarily large successive gaps as \(n\) grows. For \(n=5\), \(Q_5(z)=z^5+5z^8+11z^{10}+10z^{11}\).

## Assumptions and scope

Graphs are finite, simple, undirected, and unweighted; shortest paths use the ordinary edge-count metric. The statement concerns the one-subdivision \(\Sigma_n\), for every integer \(n\ge3\), and labelled vertex subsets. Inclusion-minimal means minimal under deleting *any* selected vertex, not merely minimum cardinality. There is no assertion for subdivisions of arbitrary base graphs or for subdivisions by other numbers of vertices.

## Proof

**1. Exhaustive geodesic classification.** For distinct original vertices \(v_i,v_j\), the unique geodesic has length two and is \(v_i,w_{ij},v_j\). For \(v_i\) and \(w_{jk}\) with \(i\in\{j,k\}\), their unique geodesic is their joining edge. If \(i\notin\{j,k\}\), there are two length-three geodesics, one passing through \(v_j\), the other through \(v_k\); they share no edge. Two distinct subdivision vertices \(w_{ij},w_{ik}\) sharing original index \(i\) have unique length-two geodesic \(w_{ij},v_i,w_{ik}\). For subdivision vertices with disjoint index pairs, the four choices of one endpoint from each pair give four length-four geodesics; no edge lies on all four, because at each terminal subdivision vertex the paths use both incident edges. These are all cases, and the displayed paths are shortest because every subdivision vertex is adjacent only to its two original endpoints, while all original-to-original paths have length at least two.

It follows that **every** vertex pair monitoring the half-edge \(v_iw_{ij}\) contains at least one of its endpoints \(v_i,w_{ij}\). More precisely, the only monitoring pairs are \(\{v_i,v_j\}\), \(\{v_i,w_{ij}\}\), and \(\{w_{ij},w_{ik}\}\) with \(k\ne i,j\). (The statement is about unordered pairs, and the last pair ranges over \(k\in[n]\setminus\{i,j\}\).)

**2. Necessity of a vertex cover.** If some half-edge \(v_iw_{ij}\) has both endpoints outside \(S\), none of its monitoring pairs can lie within \(S\), by Step 1. Hence an MEG-set meets every half-edge and is a vertex cover.

**3. Sufficiency of a vertex cover.** Suppose \(S\) covers every half-edge. If both \(v_i,v_j\) are selected, their unique geodesic monitors both halves of the subdivided edge \(ij\). Otherwise, \(w_{ij}\in S\). For a half-edge \(v_iw_{ij}\), if \(v_i\in S\), its endpoints monitor it. If \(v_i\notin S\), all subdivision vertices \(w_{ik}\), \(k\ne i\), belong to \(S\) because each edge \(v_iw_{ik}\) must be covered at the subdivision endpoint. Since \(n\ge3\), some \(k\notin\{i,j\}\) exists; the unique geodesic between \(w_{ij}\) and \(w_{ik}\) monitors \(v_iw_{ij}\). Therefore every half-edge is monitored. This establishes the equivalence and the forced-subdivision-vertex criterion.

**4. Counting all sets.** Fix \(A\) of cardinality \(k\). Of the \(N\) subdivision vertices, exactly \(N-\binom k2\) are forced. The remaining \(\binom k2\) can be chosen freely, independently. The contribution is \(z^{k+N-\binom k2}(1+z)^{\binom k2}\). There are \(\binom nk\) possible \(A\), giving \(P_n\).

**5. Characterizing inclusion-minimal sets.** Any optional selected \(w_{ij}\) with both endpoints in \(A\) may be deleted without losing the cover property, so a minimal set has exactly its forced subdivision vertices. When \(|A|=1\), every subdivision vertex is forced, and deleting the sole selected original leaves the full subdivision shore, still an MEG-set; hence no such set is minimal. When \(A=\varnothing\), all subdivision vertices are forced and each is indispensable. For \(|A|\ge2\), every selected original \(v_i\) is indispensable: choose \(j\in A\setminus\{i\}\), so \(w_{ij}\) is omitted, and deleting \(v_i\) uncovers \(v_iw_{ij}\). Every selected subdivision vertex is forced by a nonselected endpoint, so is indispensable. This proves the complete minimal family and \(Q_n\).

**6. Cardinality extremes.** The number of minimal sets is \(1+\sum_{k=2}^{n}\binom nk=2^n-n\). Their sizes are \(N\) and \(f(k)=N+k-\binom k2\), \(2\le k\le n\). For \(k\ge2\), \(f(k)-f(k+1)=k-1\), so \(f\) strictly decreases on that integer interval. Hence the maximum is \(f(2)=N+1\), while its minimum is \(f(n)=n\). Since \(N\ge n\) for \(n\ge3\), the global minimum is \(n\); the full subdivision shore ties it exactly when \(n=3\). Finally, the gaps \(f(k)-f(k+1)=k-1\) become unbounded as \(n\) grows, proving the spectrum statement.

## Verification

The standalone `verify.py` reconstructs \(\Sigma_n\), computes all-pairs shortest-path distances by breadth-first search, removes each edge separately, and determines its monitored vertex pairs from *distance changes*, rather than using the claimed structural characterization. It exhaustively checks all \(2^{n+\binom n2}\) subsets for \(n=3,4,5\), including both polynomials and inclusion-minimality, and checks 5,000 deterministically sampled subsets at \(n=6\). The symbolic minimal-set counts and cardinality bounds are also checked for \(3\le n\le24\). Run `python3 verify.py` in this directory. The recorded execution reports `VERIFY_OK` with 38,856 directly checked subsets. Finite checks do not replace the proof for arbitrary \(n\).

## Relationship to prior work

The MEG notion and initial graph-family parameters were developed in Dev–Dey–Foucaud–Narayanan–Ramasubramony Sulochana (first public 2022). Foucaud–Marcille–Myint–Sandeep–Sen–Taruni (first public 2024), Theorem 6.3, proves that every vertex cover is an MEG-set in a connected graph of minimum degree at least two and girth at least five. The one-subdivided complete graph has minimum degree two and girth six, so **the sufficiency direction is already covered** by that general theorem. The contribution here is the converse in this specific incidence graph, the *equality of the two full set systems*, the resulting exact all-set and minimal-set polynomials, and their upper-spectrum consequences. Standard vertex-cover counting is elementary once the converse is established. The same 2024 paper studies multi-subdivision with at least two inserted vertices per original edge via bounds on minimum MEG size, not an exact set-system equivalence for a single subdivision. Other known MEG results on graph products, cycles, and structured graph classes do not directly give the stated converse. Publication priority of that converse and its enumerators remains provisional.

## Limitations

The structural equivalence is specific to full one-subdivisions of complete graphs. It does not imply MEG-set/vertex-cover equivalence for arbitrary subdivided graphs, for example longer cycles. The expressions are exact cardinality enumerators for labelled vertex sets, not orbit counts. No independent mathematical review or exhaustive publication-priority certification has been performed. The program only checks finite cases and is not an infinite proof.

## References

1. S. R. Dev, S. Dey, F. Foucaud, K. Narayanan, L. Ramasubramony Sulochana, *Monitoring edge-geodetic sets in graphs*, arXiv:2210.03774, initial submission 2022-10-07, https://arxiv.org/html/2210.03774v3 .
2. F. Foucaud, C. Marcille, Z. M. Myint, R. B. Sandeep, S. Sen, S. Taruni, *Bounds and extremal graphs for monitoring edge-geodetic sets in graphs*, arXiv:2403.09122, initial submission 2024-03-14, https://arxiv.org/html/2403.09122v2 .
3. J. Haslegrave, *Monitoring edge-geodetic sets: hardness and graph products*, arXiv:2210.08955, initial submission 2022-10-17, https://arxiv.org/abs/2210.08955 .
4. F. Foucaud, A. Pandey, K. Paul, *Characterizing optimal monitoring edge-geodetic sets for some structured graph classes*, arXiv:2503.06086, initial submission 2025-03-08, https://arxiv.org/abs/2503.06086 .
