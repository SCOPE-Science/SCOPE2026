# All maximum cuts of rectangular strong path grids

## Finding

For integers \(2\le a\le b\), let \(K_{a,b}=P_a\boxtimes P_b\), the simple graph on \([a]\times[b]\) in which two distinct sites are adjacent precisely when both coordinates differ by at most one. A cut is an unordered bipartition of this labelled vertex set, identified under global exchange of its two sides. Then the complete number \(M(a,b)\) of maximum cuts is
\[
M(a,b)=\begin{cases}3,&a=b=2,\\2,&a=b\ge3,\\1,&2\le a<b.\end{cases}
\]
More explicitly, for \(a<b\) the unique maximizing cut, up to side exchange, assigns the same color to all sites in a column and alternates colors along the longer coordinate. For \(a=b\ge3\), the only maximizers are this column-striping and its row-striping transpose. For \(a=b=2\), the graph is \(K_4\), so there are three balanced \(2+2\) cuts.

The known optimum cut size is
\[
\operatorname{MaxCut}(K_{a,b})=(b-1)(3a-2).
\]
The new assertion is the complete classification and enumeration of *all* maximizing cuts, not this scalar value.

## Assumptions and scope

All graphs are finite, undirected and unweighted. Vertices are the fixed grid sites, not graph-isomorphism classes; the only identification is simultaneous swapping of the two cut sides. Both factors have at least two vertices. For a coloring \(c:V(K_{a,b})\to\{0,1\}\), an *uncut edge* joins equal colors. Set \(U(c)\) to their number. Maximizing the cut is equivalent to minimizing \(U(c)\). A *row stripe* colors each complete row constantly and alternates between rows; a *column stripe* is its transpose. Here rows are indexed by the first, shorter coordinate.

## Proof

**Known optimum and its exact scope.** Theorem 5.10 of Diester, Kühn, Rapp, Schneider and Ueckerdt, arXiv:2611.13917v1 (2026-11-10), states that for connected bipartite \(G\) with \(v\) vertices and \(e\) edges, the fewest uncut edges of \(G\boxtimes P_\ell\) is \(\min\{e\ell,v(\ell-1)\}\). Applying it to \(G=P_a\) and \(\ell=b\) gives
\[
\gamma(a,b):=\min_c U(c)=\min\{(a-1)b,a(b-1)\}=(a-1)b
\]
for \(a\le b\). As \(K_{a,b}\) has \(a(b-1)+b(a-1)+2(a-1)(b-1)\) edges, subtraction gives the displayed maximum-cut size. We now prove the new equality-case classification.

**One-line extension lemma.** Consider two consecutive horizontal rows, colored by vectors \(x=(x_1,\ldots,x_L)\) and \(y=(y_1,\ldots,y_L)\), where \(L\ge2\). The *increment* \(B(x,y)\) in uncut edges upon appending row \(y\) to a pre-existing row \(x\) consists of the horizontal edges within \(y\), plus all vertical and diagonal edges between \(x\) and \(y\):
\[
B(x,y)=\sum_{i=1}^{L}\mathbf1_{x_i=y_i}
+\sum_{i=1}^{L-1}\left(\mathbf1_{y_i=y_{i+1}}+\mathbf1_{x_i=y_{i+1}}+\mathbf1_{x_{i+1}=y_i}\right).
\]
For each \(1\le i<L\), the three edges on \(\{x_i,y_i,y_{i+1}\}\) form a triangle. These triangles are edge-disjoint, so \(B(x,y)\ge L-1\). Equality forces every remaining edge, namely \(x_Ly_L\) and \(x_{i+1}y_i\) for \(i<L\), to be cut, and every displayed triangle to have exactly one uncut edge. Since \(x_L\) must differ from both \(y_L\) and \(y_{L-1}\), the latter two colors agree. The last triangle must have its horizontal \(y_{L-1}y_L\) edge as its only uncut edge, forcing \(x_{L-1}=x_L\). Repeating backwards proves that \(x\) is constant, \(y\) is constant, and they have opposite colors. Conversely these two constant opposite rows give equality. We have proved
\[
B(x,y)=L-1\quad\Longleftrightarrow\quad x,y\text{ are opposite constant vectors.}
\]

If \(x\) alternates, define \(t_i=\mathbf1_{x_i=y_i}\). As \(x_{i+1}\ne x_i\), direct substitution gives the further exact identity
\[
B(x,y)=L+\sum_{i=2}^{L-1}(1-t_i)+\sum_{i=1}^{L-1}\mathbf1_{t_i\ne t_{i+1}}.
\]
For \(L\ge3\), equality \(B=L\) holds only for \(t_i=1\) for all \(i\), that is, \(y=x\). For \(L=2\), equality holds exactly for \(y=x\) and \(y=1-x\). In particular, for alternating \(x\), \(B\ge L\).

**Constant-boundary lemma.** On any \(r\times L\) strong grid with \(r\ge1\), \(L\ge2\), if one end row is monochromatic, there are at least \(r(L-1)\) uncut edges, with equality *only* for row stripes. Indeed, the monochromatic end row already has \(L-1\) uncut horizontal edges; appending each successive row costs at least \(L-1\), with equality exactly when the two consecutive rows are opposite monochromatic rows, by the preceding lemma.

**Induction on the shorter side.** We simultaneously prove the claimed complete classification for all \(2\le a\le b\). For \(a=2=b\), \(K_{2,2}\cong K_4\), with exactly three maximum cuts. For \(2=a<b\), start from the square and append columns; each appended column costs at least one uncut edge. The known optimum is \(b\), while the square minimum is two, so equality must hold at every append. The first append forces the two most recent columns to be opposite monochromatic columns. Of the three \(K_4\) optimal cuts, exactly one has a monochromatic final column. Thus only column stripes can extend optimally, and the same conclusion propagates to all larger \(b\).

Now suppose the classifications for all shorter sides less than \(a\) have been established, where \(a\ge3\). First consider the square \(a\times a\), whose optimum uncut count is \(a(a-1)\). Delete its last row. The resulting \((a-1)\times a\) rectangle has optimum \(a(a-2)\), by the known size formula, and *unique* optimizer given by column stripes, by the induction hypothesis. Let \(u\) be the prefix uncut count and \(B\) the appended-row increment. We have
\[
u\ge a(a-2),\qquad B\ge a-1,\qquad u+B=a(a-1).
\]
If \(B=a-1\), the extension lemma forces the final two rows to be opposite monochromatic rows. The constant-boundary lemma applied to the prefix gives \(u\ge(a-1)^2\). Equality is forced by the displayed total, and the prefix and full square must be row stripes. Otherwise \(B\ge a\); the same displayed inequalities force \(B=a\) and \(u=a(a-2)\), so the prefix is the unique column stripe. Its last row alternates. The alternating-row identity, with \(L=a\ge3\), forces the new row to equal it, yielding column stripes. Thus precisely the two orthogonal stripe cuts optimize every square of side at least three.

Finally, take \(b>a\). Delete its last column. Its optimum uncut count is \((a-1)(b-1)\), while the full optimum is \((a-1)b\). The extension cost is at least \(a-1\), so equality is necessary for every optimal full coloring; the two rightmost columns are then opposite monochromatic columns. At \(b=a+1\), only the column-stripe optimizer of the square has a monochromatic last column; therefore only its column-stripe continuation can optimize. Repeating this argument inductively in \(b\) proves uniqueness for every nonsquare rectangle. This completes the proof for all \(a,b\ge2\). \(\square\)

## Verification

Run `python3 verification/check_king_cuts.py` using the Python 3 standard library. It independently constructs every edge from the strong-product adjacency rule. An exhaustive anchored spin enumeration tests the claim for eleven grids with up to sixteen vertices. A second, independent column-state transfer matrix counts all optimal unordered cuts and their cut sizes for 69 rectangles with shorter side between two and seven and longer side at most fifteen. Both exact integer methods reported `VERIFY_OK`. These finite calculations corroborate, but do not replace, the unrestricted proof above.

## Relationship to prior work

The exact maximum-cut value, and the existence of an alternating optimal bipartition, follow from Diester et al., Theorem 5.10 and Corollary 5.11. **Neither the value nor existence is claimed as new.** The additional classification is an equality-case theorem: it proves all other optimal cuts absent and finds a sharp three/two/one-count transition when rectangular aspect ratio changes. The earlier theorem's lower-bound certificate does not state, tabulate, or directly enumerate all optimizing cuts. The direct combinatorial edge-counting argument here provides those missing equality conditions.

Related finite-grid antiferromagnetic Ising models interpret maximum cuts as ground states. This language does not change the exact mathematical claim or its comparison to the cited graph-theoretic result. Searches under the equivalent terms 'ground state degeneracy', 'king grid', and 'strong product path' did not locate a covering all-order formula; historical priority is nevertheless not independently certified.

## Limitations

Only ordinary unweighted complete rectangular strong products of two paths are covered, with free (nonperiodic) boundaries. No claim is made for induced subgraphs, cyclic products, higher-dimensional strong grids, weighted energies, or the number of near-optimal cuts. The prior optimum-size formula is taken from the cited published theorem rather than independently reproved here. The classification has undergone self-review and exact finite corroboration, but not independent mathematical audit; older literature using equivalent Ising terminology may exist.

## References

1. Jan Diester, Kolja Kühn, Manuel Rapp, Samuel Schneider, Torsten Ueckerdt, *Feedback Vertex Set, Max Cut, and Edge Coloring on the Strong Product of a Graph and a Path*, arXiv:2611.13917v1, first public 2026-11-10, especially Theorem 5.10, proof, and Corollary 5.11. https://arxiv.org/abs/2611.13917
2. Standard antiferromagnetic Ising / maximum-cut correspondence; contextual comparison only, not relied upon for the proof.
