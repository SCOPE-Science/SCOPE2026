# Zero invertible comparison distance for continuum many spectrally distinct Bessel families

## Finding
Fix any real \(0<r<1\) and integer \(G\geq1\). Let \(A,B\subseteq\mathbb N_0\) be infinite sets containing zero such that every integer interval \([n,n+G]\), for \(n\geq0\), meets both sets. Put \(H_A=\bigoplus_{i\in A}\ell^2\) and \(H_B=\bigoplus_{j\in B}\ell^2\), and define bounded positive operators
\[
P_A=\bigoplus_{i\in A}r^i I_{\ell^2},\qquad P_B=\bigoplus_{j\in B}r^j I_{\ell^2}.
\]
Then there exist **two independently chosen bounded invertible contractions** \(W:H_B\to H_A\) and \(V:H_A\to H_B\) with
\[
W^*P_AW=P_B,\qquad V^*P_BV=P_A,\qquad
\|W\|=\|V\|=1,\quad
\max\{\|W^{-1}\|,\|V^{-1}\|\}\leq r^{-G/2}.
\]
Define the invertible exact-pair comparison quantity (with the infimum of the empty set understood as infinity)
\[
D_{\mathrm{inv}}(P_A,P_B)=\log\inf\left\{\max\{1,\|W\|\|V\|\}:\ W,V\text{ invertible and satisfy the two displayed congruences}\right\}.
\]
Then \(D_{\mathrm{inv}}(P_A,P_B)=0\), **and the infimum is attained**, even when the two positive operators are not unitarily equivalent.

In fact, for every binary sequence \(\eta=(\eta_n)_{n\geq0}\), take
\[
A_\eta=2\mathbb N_0\cup\{2n+1:\eta_n=1\}.
\]
The corresponding operators \(P_{A_\eta}\) form a continuum-sized family of pairwise unitarily inequivalent, positive, injective, noncompact operators with nonclosed range, while every pair has invertible exact comparison distance zero. Each is the frame operator of a Bessel sequence (not a frame for the full Hilbert space), so this phenomenon occurs for Bessel-family comparisons.

## Assumptions and scope
All Hilbert spaces are complex and separable. Here \(\ell^2\) denotes an infinite-dimensional copy at **each** occupied spectral level. A set meeting every interval \([n,n+G]\) is called \(G\)-syndetic. The operators are noncompact because the eigenvalue one has infinite multiplicity, and have nonclosed range because occupied levels tend to infinity, giving arbitrarily small positive spectral values. The two comparison maps are **not** required to be mutual inverses: this is the exact-pair convention of Definition 7.2 of the motivating paper, with the additional restriction that both are invertible (Problem 11.12). The theorem does not claim distance zero under a single congruence implemented by a map and its inverse, or under unitary comparison maps.

## Proof
**Step 1 (forward incidence graph).** Define
\[
E_+=\{(i,j)\in A\times B:0\le j-i\le G\}.
\]
Every \(j\in B\) has an incident edge: if \(j<G\), choose \(i=0\); otherwise the interval \([j-G,j]\) meets \(A\). Every \(i\in A\) has an incident edge because \([i,i+G]\) meets \(B\). Each vertex has at most \(G+1\) neighbors, hence finite, and \((0,0)\in E_+\).

For each \(i\in A\), partition the infinite-dimensional Hilbert block \(\ell^2_i\) orthogonally into one infinite-dimensional summand for each edge \((i,j)\in E_+\). Do likewise in each block \(\ell^2_j\), for every \(j\in B\), using the same edges. Because every degree is finite and nonzero, such decompositions exist. Select an arbitrary unitary between the two summands indexed by each edge. Define \(W\) on the summand indexed by \((i,j)\) to be \(r^{(j-i)/2}\) times that unitary, mapping from \(H_B\) to \(H_A\). The direct sum is an onto, boundedly invertible map, since
\[
r^{G/2}\le r^{(j-i)/2}\le1.
\]
Its norm equals one because the \((0,0)\) edge has multiplier one, and its inverse norm is at most \(r^{-G/2}\). On this edge the quadratic forms agree exactly:
\[
r^i\bigl(r^{(j-i)/2}\bigr)^2=r^j.
\]
Orthogonality of the edge summands therefore proves \(W^*P_AW=P_B\), with no finite-rank or domain restriction.

**Step 2 (reverse incidence graph).** Repeat the construction on
\[
E_-=\{(i,j)\in A\times B:0\le i-j\le G\}.
\]
Every \(i\in A\) has a preceding \(j\in B\) within \(G\) (using \(0\in B\) for small \(i\)); every \(j\in B\) has a following \(i\in A\) within \(G\). The edge summands now define \(V:H_A\to H_B\), acting on \((i,j)\in E_-\) by a unitary times \(r^{(i-j)/2}\). This is boundedly invertible, \(\|V\|=1\), \(\|V^{-1}\|\le r^{-G/2}\), and
\[
r^j\bigl(r^{(i-j)/2}\bigr)^2=r^i,
\]
so \(V^*P_BV=P_A\).

**Step 3 (optimal distance and distinctness).** The definition has the universal lower bound \(D_{\mathrm{inv}}\ge0\). The maps from Steps 1–2 attain \(\|W\|\|V\|=1\), establishing equality. Each \(A_\eta\) contains all even indices, so every interval of three consecutive integers meets it (choose \(G=2\)). Distinct binary sequences give different sets of positive eigenvalues \(\{r^i:i\in A_\eta\}\). A unitary intertwiner preserves eigenvalues, hence \(P_{A_\eta}\) and \(P_{A_\theta}\) cannot be unitarily equivalent when \(\eta\ne\theta\). There are \(2^{\aleph_0}\) choices. Finally, on \(H_{A_\eta}\), the sequence \(f_{i,m}=r^{i/2}e_{i,m}\), with \(m\ge0\) and standard basis \(e_{i,m}\), has Bessel bound one and frame operator \(P_{A_\eta}\); the infimum of frame bounds is zero.

## Verification
The attached standalone Python script `verify_syndetic_edges.py` uses exact rational arithmetic with \(r=1/4\) to check directed edge coverage and all edgewise congruence identities over multiple finite prefixes and binary patterns. It returns `SYNDETIC_EXACT_EDGE_IDENTITY_OK 13920` on successful execution. The full infinite-dimensional construction follows the proof above: infinite block multiplicity, not finite enumeration, is essential. No numerical test establishes infinite cardinality, nonclosed range, or novelty.

For a particularly transparent example, take \(A=2\mathbb N_0\) and \(B=\{0\}\cup\{2n+1:n\ge0\}\). A convenient covering subgraph of \(E_+\) retains only the edges \((2n,2n+1)\), \(n\ge0\), and \((0,0)\); split the \(A_0\) block into two infinite summands. A covering subgraph of \(E_-\) retains only \((2n,2n-1)\), \(n\ge1\), and \((0,0)\). Applying the same edge-block method on these subgraphs yields two invertible exact maps whose only nonzero scalar coefficients are \(1\) and \(\sqrt r\). The two operators have different eigenvalue sets.

## Relationship to prior work
El Idrissi, *Coarse comparison of Bessel families*, arXiv:2610.39002v1 (first public 28 October 2026), classifies invertible **inequality** comparisons by bounded displacement of dyadic spectral multiplicities (Theorem 6.5) and defines the exact-pair quantity for arbitrary bounded maps (Definition 7.2). Problem 11.12 asks for analogous quantities on restricted operator classes, including invertible maps. Neither the inequality classification nor the unrestricted exact-pair distance specifies that two invertible exact maps can simultaneously have norm exactly one for distinct spectral supports. The present theorem gives an explicit, attained zero-value stratum of that proposed restricted quantity; it does not compute the quantity for all pairs.

Balan's earlier frame-distance work and the classical Douglas factorization theorem provide broad comparison context, but their accessible records do not state the current two-sided norm-one invertible construction. Priority remains subject to fuller historical review. A separate earlier study of dense-range comparison for a specific pair of positive operators does not cover the present invertible maps: those earlier operators are explicitly not invertibly equivalent.

## Limitations
The proof assumes infinite multiplicity at each occupied spectral level, and syndetic occupancy; it does not extend automatically to finite multiplicities, lacunary supports, arbitrary spectral measures, or unitary exact comparison. It proves only a sharp zero-distance phenomenon on a natural family, not a complete formula or a classification of the restricted quantity. Zero distance does not imply unitary equivalence here. The full text of all earlier frame-distance papers has not been independently examined; potential earlier equivalent formulations remain a publication-priority risk. Independent mathematical audit has not been performed.

## References
1. N. El Idrissi, *Coarse comparison of Bessel families*, arXiv:2610.39002v1, submitted 28 October 2026, https://arxiv.org/html/2610.39002v1 (Theorem 6.5, Definition 7.2, Problem 11.12).
2. R. Balan, *Equivalence relations and distances between Hilbert frames*, Proc. Amer. Math. Soc. 127 (1999), https://doi.org/10.1090/S0002-9939-99-04826-1 (published abstract consulted).
3. R. G. Douglas, *On majorization, factorization, and range inclusion of operators on Hilbert space*, Proc. Amer. Math. Soc. 17 (1966), 413–415, https://doi.org/10.1090/S0002-9939-1966-0203464-1 (published abstract consulted).
