# Exact single-chord completion across the first computational boundary

## Finding
Let \(C_n\) denote the cycle with vertices labeled \(1,2,\ldots,n\) in cyclic order, and put \(T_n=n(n+1)/2\). A graph on these vertices is **sum-complete** if every integer from \(1\) through \(T_n\) is the sum of labels of some nonempty vertex subset whose induced subgraph is connected. Write \(\operatorname{mEC}(n)\) for the least number of edges added to \(C_n\) to make it sum-complete.

For **every integer** \(8\le n\le599\),
\[
\operatorname{mEC}(n)=1.
\]
More precisely, the complete table `chords.csv` provides a vertex \(b_n\) for every such \(n\), and the one-edge extension \(C_n+\{1,b_n\}\) is sum-complete. Every proposed chord is a genuine non-cycle edge. The endpoint \(599\) is the numerical threshold used in the motivating paper to connect its finite verification with its analytic proof of incompleteness.

## Assumptions and scope
Graphs are undirected simple graphs. Vertex labels remain fixed. A connected vertex subset means one whose **induced** graph is connected; the empty set is excluded. Each pair \((n,b_n)\) in `chords.csv` represents a chord from label \(1\) to label \(b_n\), with \(3\le b_n\le n-1\). The theorem is finite and covers exactly the stated range. It does not assert that one chord is sufficient for any \(n\ge600\).

## Proof
For any integer \(n\ge8\), the sums of all nonempty cyclic arcs are computed by the following exhaustive formula: for \(0\le t<n\), \(1\le\ell\le n\), define
\[
C(t,\ell)=\sum_{j=0}^{\ell-1}\bigl(1+((t+j)\bmod n)\bigr).
\]
Every nonempty connected vertex subset of the unaugmented cycle is one of these arcs, including the full vertex set.

Fix a proposed chord \(\{1,b\}\). Divide the original cycle into the internally disjoint paths
\[
P=(1,2,\ldots,b),\qquad Q=(b,b+1,\ldots,n,1).
\]
For either path, with interior vertices \(z_1,\ldots,z_m\) in the order displayed, choose any integers \(i,j\ge0\) with \(i+j\le m\); select its first \(i\) interior vertices and its last \(j\) interior vertices. Their label-sum is
\[
E_z(i,j)=\sum_{r=1}^{i}z_r+\sum_{r=m-j+1}^{m}z_r.
\]
The two portions are disjoint. Denote the finite sets of such sums by \(E_P,E_Q\). For every \(s\in E_P\), \(t\in E_Q\), the union of both selected portions and endpoints \(\{1,b\}\) has label-sum \(1+b+s+t\). Every selected vertex connects along its own path to at least one endpoint, and the chord joins the endpoints. Therefore the induced subgraph of this union is connected. Thus each integer in
\[
\mathcal U(n,b)=\{C(t,\ell):0\le t<n,1\le\ell\le n\}\cup\{1+b+s+t:s\in E_P,t\in E_Q\}
\]
is a valid connected-set sum for \(C_n+\{1,b\}\). This construction suffices; there is no assumption that it lists every connected vertex subset.

The accompanying standalone verifier reads `chords.csv`, checks the exact consecutive sequence \(n=8,\ldots,599\), constructs \(\mathcal U(n,b_n)\) by the preceding formulas using arbitrary-precision integers and bitsets, and verifies, for **every** \(n\),
\[
\{1,2,\ldots,T_n\}\subseteq \mathcal U(n,b_n).
\]
It separately checks that the unaugmented cycle's arc-sum set is strictly smaller than \(\{1,\ldots,T_n\}\) for every \(n\) in this range. This establishes \(\operatorname{mEC}(n)\le1\) and \(\operatorname{mEC}(n)\ge1\), respectively, hence equality. Every loop is finite, and the verifier performs no probabilistic search.

## Verification
The exact table has \(592\) records and no missing or repeated values of \(n\). Running `python verify.py --start 8 --stop 600` checks the entire theorem. To bound execution time, the same deterministic check was performed as the adjacent disjoint ranges \([8,301)\), \([301,451)\), \([451,526)\), \([526,565)\), and \([565,600)\); all returned `VERIFY_OK`, for a total of \(592\) checks. The verifier independently enumerates all induced connected subsets using graph traversal for the small cases \(8\le n\le14\) and confirms equality with the constructed sumset there. All checks use exact integer arithmetic. The table and verifier are embedded in the same package.

## Relationship to prior work
Marotti and Needleman's *Consecutive Cycle Sums* (first submitted October 6, 2026; primary MSC 11A67) proves that every unaugmented cycle \(C_n\) with \(n\ge8\) is incomplete. It formulates \(\operatorname{mEC}(n)\), proves an upper bound using approximately \(n/2\) added edges, gives \(\operatorname{mEC}(8)=1\), and uses finite checks up to \(599\) in its incompleteness argument. The exact one-edge statement for **all** \(8\le n\le599\) is not stated there. A separate publicly accessible construction gives \(\operatorname{mEC}(n)=O(\sqrt n)\) uniformly, but this bound does not imply the present exact equality throughout the finite window. Cambie and Groenland study connected-subgraph sums with arbitrary vertex assignments, a different optimization problem. These comparisons do not establish absolute historical priority.

## Limitations
The proof is a finite, exhaustive, reproducible classification for the specified natural cutoff, not an infinite theorem or a solution to the eventual exact-value problem. It does not claim optimality of the particular recorded chord positions, nor that every one-edge extension succeeds. A published or otherwise unindexed covering statement may exist. The full finite proof requires executing the self-contained verifier or independently reconstructing its bitset loops; a log alone is not evidence.

## References
- Jessica Marotti and Jonathan Needleman, *Consecutive Cycle Sums*, arXiv:2610.08889v1, October 6, 2026. https://arxiv.org/html/2610.08889v1
- *Sublinear edge completion for consecutive cycle sums*, publicly accessible research record (different asymptotic bound). https://www.trureturing.org/research/marotti-needleman-2026-consecutive-cycle-sums/
- Stijn Cambie and Carla Groenland, *Note on extremal problems about connected subgraph sums*, Graphs and Combinatorics 42 (2026), article 35. https://doi.org/10.1007/s00373-026-03026-8
