# The five-column clique-fiber Rips complex is a wedge of \(m-1\) two-spheres

## Finding
For every integer \(m\ge3\), give the Cartesian product graph \(G_m=K_m\square C_5\) its shortest-path metric. The inclusive scale-two Vietoris--Rips complex \(X_m=\operatorname{VR}(G_m;2)\) has integral homotopy type
\[
X_m\simeq\bigvee^{m-1}S^2.
\]
In particular, \(X_m\) is simply connected, \(\widetilde H_2(X_m;\mathbb Z)\cong\mathbb Z^{m-1}\), and all its other reduced integral homology vanishes. The cover used in the proof identifies five-triangle Möbius bands as the intersections of row simplices with a common circle-like core. This is a theorem for every \(m\ge3\), not an extrapolation from enumerated instances.

## Assumptions and scope
The vertex set is \(V=\mathbb Z/5\mathbb Z\times\{1,\ldots,m\}\); each vertex is denoted \((i,a)\), with column \(i\) and row \(a\). The exact graph distance is
\[
d((i,a),(j,b))=\min\{(i-j)\bmod5,(j-i)\bmod5\}+\mathbf1_{a\ne b}.
\]
A nonempty subset of \(V\) is a simplex of \(X_m\) precisely when every pair has distance at most two. All complexes, intersections, and collapses are simplicial. The five columns form a genuinely cyclic graph, rather than a path. There is no statement for graph-metric scale other than two or for a different cycle length.

## Proof
**Step 1: classify every face.** Let \(V_i=\{(i,a):1\le a\le m\}\). Define the *adjacent-column core* \(B\) to consist of all faces supported in one column or in two cyclically adjacent columns. Equivalently,
\[
B=\bigcup_{i\in\mathbb Z/5}\Delta(V_i\cup V_{i+1}).
\]
For each \(i\) and \(a\), set
\[
e_{i,a}=\{(i,a),(i+2,a)\},\qquad F_{i,a}=\Delta(e_{i,a}\cup V_{i+1}),
\]
and put \(U=B\cup\bigcup_{i,a} F_{i,a}\). For each row \(a\), put \(R_a=\Delta(\{(i,a):i\in\mathbb Z/5\})\). All these displayed sets are Rips simplices (or unions of such). We claim
\[
X_m=U\cup\bigcup_{a=1}^m R_a.\tag{1}
\]
Indeed, any pair of cyclically adjacent columns permits arbitrary rows, whereas two columns at distance two force their selected vertices to have the *same* row. The distance-two column pairs form the five edges \(\{i,i+2\}\) of the pentagram. On any chosen set of at least three columns that is not a consecutive triple \(\{i,i+1,i+2\}\), these pentagram edges connect the chosen column set. Hence every face using those columns must be row-monochromatic and lies in some \(R_a\). For a consecutive triple, only the end columns form a distance-two pair, so their vertices have equal row \(a\), and any vertices from the middle column are allowed. This is exactly \(F_{i,a}\). Faces supported on one or two columns lie in \(B\), or are distance-two pairs \(e_{i,a}\) in their corresponding \(F_{i,a}\). Thus (1) lists *every* simplex. A face with more than one vertex in an end column cannot contain a distance-two partner, so it was already covered by the same argument.

**Step 2: the core collapses to a circle.** The only faces in \(F_{i,a}\setminus B\) are those containing \(e_{i,a}\); every such face lies in a unique \(F_{i,a}\), because a distinct distance-two column pair would give a row-monochromatic nonconsecutive triple not lying in any \(F_{i,a}\). Choose \(p_i=(i+1,1)\in V_{i+1}\). For every \(S\subseteq V_{i+1}\setminus\{p_i\}\), pair the face \(e_{i,a}\cup S\) with \(e_{i,a}\cup S\cup\{p_i\}\), in descending order of \(|S|\). The lower member has exactly its paired upper member as an immediate coface when removed; no other \(F\)-block contains the long edge. Thus these are elementary free-face collapses and \(U\searrow B\). Next, for any chosen row \(a\), every vertex \((i,b)\), \(b\ne a\), is dominated in \(B\) by \((i,a)\): any face of \(B\) containing the former still belongs to \(B\) after adjoining the latter. Removing the dominated vertices leaves the five-edge cycle \(C_a=\{(i,a),(i+1,a)\}\) with its vertices and no triangles. Therefore \(B\searrow C_a\cong S^1\). This also proves each inclusion \(C_a\hookrightarrow U\) is a homotopy equivalence, inducing a generator of \(\pi_1(U)\cong\mathbb Z\).

**Step 3: each row meets the core in a Möbius band, not a disk.** For every \(a\), the intersection \(M_a=R_a\cap U\) has exactly five vertices, all ten edges, and the five consecutive-column triangles
\[
t_{i,a}=\{(i,a),(i+1,a),(i+2,a)\},\qquad i\in\mathbb Z/5.
\]
It has no tetrahedra. The five length-two diagonals \(e_{i,a}\) are free edges, each contained in exactly \(t_{i,a}\) in \(M_a\). Collapse each \((e_{i,a},t_{i,a})\) pair to obtain \(M_a\searrow C_a\). This is the standard five-triangle Möbius strip, with boundary given by the five length-two diagonals. In particular \(M_a\simeq S^1\), and the inclusion \(M_a\hookrightarrow U\) is a homotopy equivalence: the triangle and diagonal collapses identify the ordinary five-cycle \(C_a\) as a common deformation retract up to homotopy.

**Step 4: the homotopy pushouts.** Distinct row simplices \(R_a\) are disjoint from one another, and their entire intersections with \(U\) are the \(M_a\). All inclusions are CW cofibrations. Attaching the first contractible row simplex \(R_1\) to \(U\) along the homotopy equivalence \(M_1\to U\) produces a contractible complex \(Z_1=U\cup R_1\). For each remaining \(a\), attach the contractible \(R_a\) along \(M_a\simeq S^1\) to \(Z_{a-1}\). Since \(Z_{a-1}\) is simply connected (initially contractible and thereafter a wedge of two-spheres), the attaching map \(M_a\to Z_{a-1}\) is nullhomotopic. The homotopy pushout consequently gives \(Z_a\simeq Z_{a-1}\vee\Sigma M_a\simeq Z_{a-1}\vee S^2\). Induction over \(a=2,\ldots,m\) proves \(X_m\simeq\bigvee^{m-1}S^2\), including integral homology.

## Verification
The standalone program `verify.py` constructs the complete scale-two Rips face sets for \(m=3,4,5\) directly from the distance formula. Independently, it constructs \(B,U,F_{i,a},R_a,M_a\), checks the full cover equality, replays *every* claimed elementary collapse from \(U\) to \(B\) with explicit coface checks, verifies the five-triangle-to-five-cycle collapses for each row, and reduces all boundary matrices over \(\mathbb F_2\). The verified face totals are \(433,1564,5815\), with second mod-two Betti ranks \(2,3,4\), and all other reduced mod-two ranks zero. The output file `verification_output.txt` records the actual execution. Only the explicit Steps 1--4, not this finite replay, prove the uniform theorem.

## Relationship to prior work
Adams, Adetowubo, Barriga-Acosta, Feng and Sterling [1] study Rips complexes of square torus grids and identify several exceptional scale regimes. Their studied square-cycle factors are not the complete-graph factor \(K_m\) paired with the *five*-cycle here. The published result [2] treats the same clique-fiber graphs \(K_m\square C_n\) at scale \(r\) for \(n\ge3r\): for \(r=2\), it gives \(\bigvee^{2m-1}S^2\) at \(n=6\) and \(S^1\) for \(n\ge7\). It does *not* cover \(n=5\). The circular-ladder classification [3] treats \(K_2\square C_5\simeq S^2\), which is the \(m=2\) case of the formula; the result here starts at \(m=3\), provides an unbounded new family, and explains the boundary using Möbius-band intersections. Searches for graph-product, equivariant, augmented-cycle, and clique-fiber aliases did not identify a stronger result covering these parameters. A priori, an unindexed general Rips decomposition could still imply the result.

## Limitations
The theorem concerns *inclusive graph-shortest-path* scale two and precisely five cyclic columns. It does not settle lengths four, or higher scales, and makes no equivariant assertion. The small-case binary computations do not establish integral homotopy types without the supplied topological proof. No independent audit has been performed.

## References
[1] H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng and J. Sterling, *Vietoris--Rips complexes of torus grids*, arXiv:2502.07134 (first submitted 2025-02-10), https://arxiv.org/html/2502.07134v2. Examined Introduction, scope and homotopy results.

[2] *A sharp one-circle-to-sphere-wedge transition for clique-fiber cyclic Rips complexes*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-one-circle-to-sphere-wedge-transition-for-clique-fiber-c--e28e5da49d34. Inspected complete RESULT.md, especially hypotheses and proof of the \(n\ge3r\) range.

[3] *Scale-two Rips homotopy types of finite circular ladders*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-scale-two-rips-homotopy-types-of-finite-circular-ladders--ccd7a360a668. Compared the five-column \(m=2\) assertion; full primary manuscript not independently examined.
