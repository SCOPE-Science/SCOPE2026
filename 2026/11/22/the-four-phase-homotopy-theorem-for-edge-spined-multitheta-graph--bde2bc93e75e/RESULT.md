# The four-phase homotopy theorem for edge-spined multitheta graphs

## Finding

Take two vertices \(u,v\), add the edge \(uv\), and add \(m\ge3\) internally disjoint paths between them, of lengths \(\ell_1,\ldots,\ell_m\ge2\). No other graph edges are present. Write \(G=G(\ell_1,\ldots,\ell_m)\), let \(R=\sum_{i=1}^m\lfloor\ell_i/3\rfloor\), and set \(E=\{\ell_i\bmod3:1\le i\le m\}\).

The ordinary independence complex (with faces the independent vertex sets) has the following **integral homotopy** classification:

\[
\operatorname{Ind}(G)\simeq
\begin{cases}
\mathrm{pt}, & \{0,2\}\subseteq E,\\
S^{R-1}, & 0\in E,\ 2\notin E,\\
S^R, & E=\{1\},\\
S^R\vee S^R, & 0\notin E,\ 2\in E.
\end{cases}
\]

Thus arbitrarily many parallel routes never produce more than two sphere summands, and mixing lengths congruent to zero and two modulo three forces contractibility. Spheres and wedges are meant up to homotopy, not PL homeomorphism.

## Assumptions and scope

The graph is finite, simple, and undirected. Path lengths count **edges**. All path interiors are disjoint from one another and from both poles; the direct pole edge is present. Every \(\ell_i\) is an integer at least two, and \(m\) is arbitrary but at least three. The classification concerns the standard vertex independence complex, not a matching or multipath complex.

Let \(P_t\) denote the path on \(t\) vertices. In joins, the independence complex of \(P_0\) is the formal join unit \(\{\varnothing\}\), conventionally of sphere dimension \(-1\). When this is the only factor, its realization is empty; the zero-dimensional exceptional case is explicitly treated below.

## Proof

**1. Exact two-cone decomposition.** Deleting both poles leaves the disjoint union of paths \(P_{\ell_i-1}\). Put

\[
X=\bigast_{i=1}^m\operatorname{Ind}(P_{\ell_i-1}).
\]

The independent sets containing \(u\), respectively \(v\), cannot contain the other pole and cannot contain the first, respectively last, internal vertex on any arm. Their remaining choices give two subcomplexes \(Y_u,Y_v\subseteq X\), each abstractly isomorphic to

\[
Y=\bigast_{i=1}^m\operatorname{Ind}(P_{\ell_i-2}).
\]

Since the poles are adjacent, no independent set contains both. Hence, with each cone attached along its actual inclusion in \(X\),

\[
\operatorname{Ind}(G)=X\cup(u*Y_u)\cup(v*Y_v).
\]

This is a double homotopy-cofiber description, not merely an Euler characteristic identity.

**2. The path factors.** For every \(a\ge0\), the standard path-independence recurrence gives

\[
\operatorname{Ind}(P_{3a})\simeq S^{a-1},\qquad
\operatorname{Ind}(P_{3a+1})\simeq\mathrm{pt},\qquad
\operatorname{Ind}(P_{3a+2})\simeq S^a,
\]

with \(P_0\) interpreted as the formal join unit. Consequently \(X\) is contractible exactly when some arm length is congruent to two modulo three; otherwise \(X\simeq S^{R-1}\). Likewise \(Y_u\) and \(Y_v\) are contractible exactly when some arm length is congruent to zero modulo three; if not, each has sphere type \(S^{R-1}\) (possibly formal dimension \(-1\)).

**3. The sole nontrivial attaching-map test.** Suppose every length has residue one: write \(\ell_i=3a_i+1\), so \(a_i\ge1\). In the \(i\)-th arm, either inclusion of a shortened path independence complex is

\[
\operatorname{Ind}(P_{3a_i-1})\longrightarrow
\operatorname{Ind}(P_{3a_i}).
\]

It is a homotopy equivalence: adding the endpoint gives a mapping cone whose attaching subcomplex is \(\operatorname{Ind}(P_{3a_i-2})\), contractible because \(3a_i-2\equiv1\pmod3\). Joining these equivalences gives \(Y_u\xrightarrow{\simeq}X\), and likewise \(Y_v\xrightarrow{\simeq}X\). The first cone makes the space contractible; the second leaves \(\Sigma Y_v\simeq S^R\).

**4. Remaining residue regimes.** If some length has residue zero, \(Y_u,Y_v\) are contractible. Attaching their cones leaves the homotopy type of \(X\), namely \(S^{R-1}\) if no length has residue two and a point otherwise. If no length has residue zero but some length has residue two, then \(X\) is contractible and each \(Y\simeq S^{R-1}\). Both inclusion maps are nullhomotopic through \(X\), and successive cone attachments give \(\Sigma Y_u\vee\Sigma Y_v\simeq S^R\vee S^R\).

If every length equals two, both \(Y_u\) and \(Y_v\) have no geometric vertices. Then the complex is a simplex on the internal vertices together with two isolated pole vertices: three connected components, homotopy equivalent to \(S^0\vee S^0\). This is precisely the stated formula at \(R=0\), so the formal empty-path convention causes no exception. These four cases exhaust all residue sets, completing the homotopy proof over the integers.

## Verification

The self-contained `verify.py` constructs every independent face and computes augmented simplicial boundary ranks over \(\mathbb F_2\) by exact bitwise column elimination. It checks 70 finite graphs against the theorem, including all nondecreasing length tuples for two arms from two through eight edges, three arms from two through five edges, and four arms from two through four edges, plus seven four- through six-arm stress cases. The smaller two-arm computations are regression checks, not claims of new coverage.

Run `python3 verify.py`. Its exact recorded output is in `verification_output.txt`. The finite calculations check necessary homological consequences; the proof above, not finite extrapolation, establishes the uniform integral homotopy claim.

## Relationship to prior work

Kozlov's path and cycle formulas provide the factors used in the argument. The 2023 work of Daundkar, Panja and Prasad treats **vertex** wedges of paths and cycles, not multiple routes sharing both endpoints and a pole edge. Przytycki and Silvero (2024), Example 3.8, analyze three-path theta graphs and their subdivisions; that includes the two-extra-arm specialization but not the stated arbitrary number of additional arms. Adamaszek's cofibre sequences are a general tool, but do not supply the four-phase multitheta classification.

The new content is the exact classification uniformly in an unbounded number of arms with arbitrary mixed length residues, including the constant bound of two on the number of sphere summands. It is not a claim that the underlying cone decomposition or the path formulas are new.

## Limitations

The result assumes a direct pole edge and otherwise internally disjoint paths; graphs with extra chords, arbitrary inter-arm edges or no pole edge are not classified. No equivariant action, simple-homotopy refinement, or topological-manifold claim is asserted. Searches of primary articles and indexed results reduce but do not eliminate the possibility of an unindexed equivalent published theorem.

## References

- N. Daundkar, S. Panja and S. Prasad, *Independence complexes of wedge of graphs* (first arXiv version 15 March 2023), https://arxiv.org/abs/2303.08798.
- J. H. Przytycki and M. Silvero, *Khovanov homology, wedges of spheres and complexity*, published 2 May 2024, Example 3.8, https://doi.org/10.1007/s13398-024-01594-z.
- M. Adamaszek, *Splittings of independence complexes and the powers of cycles* (arXiv version 2011; revised 2012), https://arxiv.org/abs/1106.6250.
