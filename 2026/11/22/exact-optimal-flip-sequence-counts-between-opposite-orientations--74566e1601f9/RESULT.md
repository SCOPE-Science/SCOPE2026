# Exact optimal flip-sequence counts between opposite orientations of \(K_{2,n}\)

## Finding
Let \(K_{2,n}\) have named hubs \(a,b\), named right vertices \(v_1,\ldots,v_n\), and \(n\ge1\). A state is an acyclic orientation of all \(2n\) graph edges, and one move reverses one graph edge provided the new state is acyclic. Set \(O_-\) to orient every edge from its right vertex to the corresponding hub, and \(O_+\) to orient every edge from its hub to the corresponding right vertex.

The shortest flip distance from \(O_-\) to \(O_+\) is \(2n\). Its number \(g_n\) of **different shortest flip sequences**, with all edges and right vertices distinguished, has the exact *formal* exponential generating function
\[
\sum_{n\ge0}\frac{g_n}{n!}z^n=\frac{S(z)}{2-S(z)},\qquad
S(z)=\sum_{n\ge0}(2n-1)!!z^n,
\]
where \((-1)!!=1\). In particular \(g_0=1\), and if \(s_n=(2n-1)!!\), then \(f_n=g_n/n!\) obeys
\[
f_0=1,\qquad f_n=2s_n+\sum_{k=1}^{n-1}s_k f_{n-k}\quad(n\ge1).
\]
The recurrence uses \(O(n^2)\) arithmetic operations to obtain \(g_n\), without traversing the exponentially large orientation graph. The first counts for \(n=1,\ldots,8\) are
\[
2,\ 16,\ 264,\ 7392,\ 319200,\ 19990080,\ 1731764160,\ 199511262720.
\]
Moreover,
\[
g_n\sim 2\,\frac{(2n)!}{2^n},\qquad
\frac{g_n}{(2n)!}\sim2^{1-n}.
\]
The latter quotient is the probability that a uniformly sampled ordering of the \(2n\) distinct original edges gives an acyclic orientation after each reversal.

## Assumptions and scope
Vertices and edges are individually labelled; paths are distinct if their ordered sequences of reversed edges differ. Each move reverses exactly one edge; intermediate orientations must be acyclic. There are no further restrictions such as preservation of a source or sink. \(n=0\) appears only as a generating-function convention, not as a new assertion about graph connectivity. The series \(S\) is a formal power series in \(\mathbb Q[[z]]\); it has zero analytic radius of convergence, so no analytic convergence of the displayed expression is asserted.

## Proof
**Step 1 (complete orientation criterion).** For each right vertex write its two-edge orientation as \((x_i,y_i)\), with \(x_i=1\) when \(a\to v_i\), \(y_i=1\) when \(b\to v_i\), and zero for the reverse orientation. The patterns \(00\) and \(11\) do not make a directed hub-to-hub path. Pattern \(10\) makes \(a\to v_i\to b\); pattern \(01\) makes \(b\to v_i\to a\). All simple cycles in \(K_{2,n}\) have length four (any such cycle uses both hubs and two distinct right vertices), so a directed cycle occurs **if and only if** at least one right vertex has pattern \(10\) and a distinct right vertex has pattern \(01\). This criterion describes all states and all allowable moves.

**Step 2 (geodesic characterization).** \(O_-\) has all bits zero, whereas \(O_+\) has all bits one. Every one-edge move changes one bit, so at least \(2n\) moves are needed. First flip the \(a\)-edge at all right vertices (yielding only patterns \(10\)), then flip all \(b\)-edges. Every intermediate state is acyclic, so the bound is attained. Every \(2n\)-move path must flip each edge **exactly once**, with no backtracking. We therefore count permutations of the \(2n\) distinct edge flips satisfying the criterion in Step 1 at every prefix.

**Step 3 (unique busy-period factorization).** During such an edge ordering, call right vertex \(i\) *open* after its first edge flip and before its second. Its open state is either \(10\) or \(01\), depending on which edge was flipped first; call this its type. A valid prefix never has two open vertices of opposite types. Cut the edge ordering at **all** times when there are no open right vertices. The resulting maximal nonempty blocks are *busy periods*: they use disjoint nonempty sets of right-vertex labels, and they have no intermediate time with no open vertex. Every busy period uses a single type, because its nonempty open set cannot switch types without becoming empty. Conversely, an ordered sequence of single-type busy periods on disjoint label sets yields a valid edge ordering. This factorization is canonical and bijective.

**Step 4 (counting a single type).** Fix one type and a chosen set of \(m\) labelled right vertices. There are exactly \((2m)!/2^m\) edge-event orders compatible with that type: for each label the prescribed first flip must precede its second, and the \(m\) two-event precedence constraints are disjoint. Thus the exponential generating function for *possibly decomposable* one-type sequences is
\[
S(z)=\sum_{m\ge0}\frac{(2m)!}{2^m m!}z^m
=\sum_{m\ge0}(2m-1)!!z^m.
\]
Let \(C(z)\) enumerate nonempty indecomposable busy periods for one fixed type. Unique decomposition of one-type sequences gives \(S(z)=1+C(z)+C(z)^2+\cdots=1/(1-C(z))\). Hence \(C(z)=1-1/S(z)\).

**Step 5 (both types).** Each busy period independently admits either of the two types; its EGF is \(2C(z)\). Ordered sequences of these periods, with labels distributed among the blocks, have EGF
\[
F(z)=\frac{1}{1-2C(z)}=\frac{S(z)}{2-S(z)}.
\]
Here multiplication of EGFs counts the disjoint distributions of *labelled* right vertices among ordered periods, so the coefficient of \(z^n\) is indeed \(g_n/n!\). From \((2-S)F=S\), with \(S=1+\sum_{n\ge1}s_nz^n\), coefficient comparison gives \(f_n=s_n+\sum_{k=1}^ns_k f_{n-k}=2s_n+\sum_{k=1}^{n-1}s_k f_{n-k}\), as claimed.

**Step 6 (asymptotic estimate).** Define
\[
T_n=\sum_{k=1}^{n-1}\frac{s_k s_{n-k}}{s_n}
=\sum_{k=1}^{n-1}\frac{\binom nk}{\binom{2n}{2k}}.
\]
Vandermonde's identity gives \(\binom{2n}{2k}\ge\binom nk^2\), and therefore
\[
0\le T_n\le\sum_{k=1}^{n-1}\frac1{\binom nk}=O(n^{-1}).
\]
Indeed for \(n\ge7\), the last sum is bounded by \(2/n+2(n-3)/(n(n-1))\), which is below \(1/2\). The six smaller cases show \(T_n\le1/2\) for \(2\le n\le6\) as well. Inducting in the recurrence, \(f_1=2s_1\) and
\[
f_n\le2s_n+4\sum_{k=1}^{n-1}s_ks_{n-k}=s_n(2+4T_n)\le4s_n.
\]
The recurrence also yields \(f_n\ge2s_n\). Combining the bound \(f_{n-k}\le4s_{n-k}\) with \(T_n\to0\) sharpens this to \(f_n/s_n\to2\). Since \(n!s_n=(2n)!/2^n\), the stated asymptotic follows. This completes the all-size proof.

## Verification
The standalone standard-library program `check_geodesics.py` independently computes coefficients by the formal recurrence; enumerates acyclicity-preserving **monotone** edge-flip sequences by dynamic programming for \(1\le n\le8\); and performs **unrestricted**, undirected breadth-first searches, counting all shortest paths while allowing flips in both directions, for \(1\le n\le7\). These three counts agree in every tested case. The program also checks the full orientation counts \(2\cdot3^n-2^n\) and legal-edge counts \(4n3^{n-1}\) through \(n=8\). `check_output.txt` records the deterministic results. Finite checks corroborate, but do not replace, the proof for arbitrary \(n\).

## Relationship to prior work
General acyclic-orientation flip graph theory, including the fact that a minimal flip distance equals the number of differing edge directions, is established in the literature on graphical zonotopes and acyclic reorientation posets; the distance \(2n\) is **background**, not claimed as novel. Pilaud describes these posets and their lattice properties; Cardinal and collaborators explicitly study flip graphs and generation; Cardinal and Steiner study optimization of shortest flip paths on generalized permutohedra. Cameron, Glass, Rekvényi and Schumacher count acyclic orientations of complete bipartite graphs by poly-Bernoulli numbers, an invariant distinct from the number of shortest sequences between two prescribed orientations. Published complete-bipartite graphical-zonotope work computes local degrees, not this source-target geodesic multiplicity, and published online-shattering work for \(K_{2,n}\) uses the same orientation language but computes VC/Littlestone dimensions rather than flip sequences. The proposed contribution is the two-type canonical busy-period decomposition, its exact sequence enumerator, the quadratic-time recurrence and the asymptotic proportion.

## Limitations
The result is specific to antipodal hubward-to-leafward orientations of \(K_{2,n}\), not all orientation pairs nor general complete bipartite graphs. It counts labelled edge-sequences, not paths modulo automorphism. The generating identity is formal, not convergent analytic. The all-size proof is supported by deterministic computations, but independent scholarly audit has not occurred. Historical novelty was checked against relevant literature and published exact graph results, but an earlier unindexed or equivalently phrased enumeration remains a residual priority risk.

## References
1. V. Pilaud, *Acyclic reorientation lattices and their lattice quotients*, arXiv:2111.12387 (first public version, 24 November 2021), https://arxiv.org/abs/2111.12387 .
2. J. Cardinal, H. P. Hoang, A. Merino, O. Mička, T. Mütze, *Combinatorial generation via permutation languages. V. Acyclic orientations*, arXiv:2212.03915 (7 December 2022), https://arxiv.org/abs/2212.03915 .
3. J. Cardinal and R. Steiner, *Shortest paths on polymatroids and hypergraphic polytopes*, arXiv:2311.00779 (1 November 2023), https://arxiv.org/abs/2311.00779 .
4. P. J. Cameron, C. A. Glass, K. Rekvényi and R. U. Schumacher, *Acyclic orientations and poly-Bernoulli numbers*, arXiv:1412.3685 (first version 2014), https://arxiv.org/abs/1412.3685 .
