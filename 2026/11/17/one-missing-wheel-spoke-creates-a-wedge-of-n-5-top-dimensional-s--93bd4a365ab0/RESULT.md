# One missing wheel spoke creates a wedge of \(n-5\) top-dimensional spheres in the ordinary three-cut complex

## Finding
For every integer \(n\ge5\), let \(W_{n+1}=C_n*K_1\) have rim vertices \(0,1,\ldots,n-1\), indexed cyclically, and hub \(h\). Remove only the spoke \(\{h,0\}\), obtaining \(G_n\). For any finite graph \(G\), define its **ordinary three-cut complex** \(\Delta_3(G)\) to have facets \(V(G)\setminus T\) over all three-element sets \(T\) for which the induced graph \(G[T]\) is disconnected.

Then, with a zero-fold wedge interpreted as a point,
\[
|\Delta_3(G_n)|\simeq \bigvee^{n-5}S^{n-3}.
\]
In particular, the complex is contractible when \(n=5\), and for every \(n\ge6\) its only nonzero reduced integral homology is
\[
\widetilde H_{n-3}(\Delta_3(G_n);\mathbb Z)\cong\mathbb Z^{n-5}.
\]
For comparison, the same ordinary three-cut complex of the intact wheel, or of that wheel after deleting one *rim edge* rather than a spoke, is contractible. Thus a single missing hub spoke produces nontrivial top homotopy while a single missing rim edge does not.

## Assumptions and scope
All graphs are finite and simple. The rim is an unfilled cycle with no chords, \(n\ge5\), and the hub is adjacent to every rim vertex except \(0\). The convention here is that \(W_{n+1}\) has \(n\) rim vertices and one hub (the notation \(W_n\) is also used elsewhere for squared cycles, and does not denote the graph here). This is the *ordinary* cut complex, not the total cut complex. The assertion is integral and concerns the full homotopy type, not only ranks over a field.

## Proof
Put \(R=\{0,\dots,n-1\}\), \(Y=R\setminus\{0\}\), \(U=\{1,n-1\}\), and \(Z=\{2,\dots,n-2\}\). Write \(m=|Z|=n-3\), so \(m\ge2\). Partition the facets of \(\Delta_3(G_n)\) according to whether the corresponding disconnected triple contains the hub.

**The hub-free triples give a cone.** A triple inside \(R\) sees exactly the original rim cycle. Hence its complementary facet contains \(h\). Their generated subcomplex is
\[
A=\{h\}*\Delta_3(C_n),
\]
which is contractible (and nonempty).

**The hub-containing triples give a ball.** Since \(h\) is adjacent to every vertex of \(Y\), a triple \(\{h,a,b\}\) can be disconnected only if one of \(a,b\) is \(0\). The third vertex must be a nonneighbor of \(0\) on the cycle: precisely \(z\in Z\). Thus the complementary facets are \(Y\setminus\{z\}\) for \(z\in Z\). They generate
\[
B=\Delta(U)*\partial\Delta(Z),
\]
where \(\Delta(U)\) is the full edge on \(U\) and \(\partial\Delta(Z)\) the boundary of the simplex on \(Z\). In particular \(B\) is a contractible triangulated \(m\)-ball with exactly \(m\) top-dimensional simplices. We have \(\Delta_3(G_n)=A\cup B\).

**The intersection has two exceptional codimension-one faces.** The intersection \(I=A\cap B\) contains every face of \(B\) with at most \(n-4=m-1\) vertices. Indeed, for such a face \(F\subseteq Y\), the set \(R\setminus F\) contains at least four vertices. Any four vertices of a cycle of length at least five contain a three-set inducing a disconnected graph: the induced graph on four vertices is a proper subgraph of a cycle and hence a forest of paths; if connected it is a four-vertex path, whose two endpoints and one interior vertex give a disconnected triple, and if disconnected an appropriate three-set is immediately disconnected. Therefore \(F\) is a face of \(A\).

A face of \(B\) of size \(n-3=m\) is of the form \(Y\setminus\{x,y\}\), with at least one of \(x,y\) in \(Z\). It belongs to \(A\) precisely when \(\{0,x,y\}\) is disconnected on the rim. The only connected such triples are \(\{0,1,2\}\) and \(\{0,n-2,n-1\}\). Consequently
\[
I=B^{(m-1)}\setminus\{F_+,F_-\},\qquad
F_+=Y\setminus\{1,2\},\quad F_-=Y\setminus\{n-2,n-1\},
\]
where the notation means omitting only these two maximal \((m-1)\)-simplices, retaining all their proper subfaces. No \(m\)-face belongs to \(A\).

**Two elementary collapses.** Each \(F_\pm\) is a free codimension-one face of \(B\): \(F_+\) lies only in \(Y\setminus\{2\}\), and \(F_-\) only in \(Y\setminus\{n-2\}\). These containing \(m\)-simplices are distinct for \(n\ge5\). Collapse both pairs, obtaining a contractible complex \(B'\) with precisely \(m-2\) surviving \(m\)-simplices. Its \((m-1)\)-skeleton is exactly \(I\).

For \(m=2\), no top simplex survives; hence \(I=B'\) is contractible. If \(m\ge3\), the pair \((B',I)\) has exactly \(m-2\) relative \(m\)-cells and no other relative cells. Since \(B'\) is contractible, its long exact homology sequence gives
\[
\widetilde H_j(I;\mathbb Z)=
\begin{cases}\mathbb Z^{m-2},&j=m-1,\\0,&j\ne m-1.\end{cases}
\]
Furthermore \(B'\) is obtained from \(I\) by attaching only \(m\)-cells, which does not change homotopy groups below degree \(m-1\). Thus \(I\) is \((m-2)\)-connected. Since it is an \((m-1)\)-dimensional CW complex, Hurewicz and the homological Whitehead theorem imply \(I\simeq\bigvee^{m-2}S^{m-1}\) for \(m\ge3\). The same formula, with the zero-fold wedge interpreted as contractible, holds for \(m=2\).

Finally, both \(A\) and \(B\) are contractible simplicial subcomplexes, and their inclusions from \(I\) are cofibrations. Their union is the homotopy pushout and is homotopy equivalent to the suspension of \(I\). Therefore
\[
|\Delta_3(G_n)|\simeq\Sigma |I|\simeq\bigvee^{m-2}S^m
=\bigvee^{n-5}S^{n-3}.
\]
For an intact wheel, every disconnected triple avoids its dominating hub, so its three-cut complex is a cone. Removing a rim edge does not affect domination by the hub and gives the same cone conclusion. This proves the comparison as well.

## Verification
The standalone finite checker `check_wheel_cut.py` reconstructs the induced connectivity of every triple, enumerates all faces of the cut complexes, tests the asserted ball/intersection description and the two free codimension-one faces, and computes reduced homology over \(\mathbb F_2\) for \(5\le n\le12\). All eight tests passed, with reduced Betti profiles empty at \(n=5\), and a single class of rank \(n-5\) in degree \(n-3\) thereafter. The intact-wheel and rim-edge-deletion acyclicity checks also passed in those eight cases. These finite checks corroborate but do not replace the unrestricted integral proof above. Run `python check_wheel_cut.py` using Python 3's standard library.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced cut complexes and treated graph joins, cycles and other families. Their graph-join theorem accounts for the intact wheel as a cone; it does not supply the one-spoke-deleted result. Chauhan and Shukla's 2026 work proves shellability and sphere counts for three-cut complexes of sufficiently large *powers of cycles*; the present graph has a near-dominating hub and is not a cycle power. Shen, Song, Yu, Zhou and Zhuang analyze realizability, uniqueness and recognition of cut complexes, not the exact homotopy type here. The result also differs from total cut complexes and ordinary matching complexes of wheels. The comparison supports a potentially new fault-sensitive homotopy classification but does not establish priority against unindexed work.

## Limitations
Only ordinary three-cut complexes of wheels with exactly one deleted spoke are classified. No classification for two or more missing spokes, other cut parameters, shellability, equivariant representations, or arbitrary near-dominating graphs is claimed. The finite program verifies only the indicated range and mod-two ranks; the integral and homotopy conclusions are derived from the explicit cellular proof. No independent review is asserted.

## References
- Pratiksha Chauhan and Samir Shukla, *Shellability of 3-cut complexes of powers of cycle graphs*, arXiv:2603.23155v1 (first public 2026-03-24), https://arxiv.org/abs/2603.23155.
- Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Rowan Rowlands, Sheila Sundaram and Lei Xue, *Topology of cut complexes of graphs*, arXiv:2304.13675 (2023; revised 2024), https://arxiv.org/abs/2304.13675.
- Yufeng Shen, Zhiyu Song, Fenglin Yu, Wuhan Zhou and Jingqi Zhuang, *Realizations and Uniqueness of Cut Complexes of Graphs*, arXiv:2512.12933 (2025), https://arxiv.org/abs/2512.12933.
