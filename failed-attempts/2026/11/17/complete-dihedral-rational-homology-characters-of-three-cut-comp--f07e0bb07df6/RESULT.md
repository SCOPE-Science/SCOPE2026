# Complete dihedral rational homology characters of three-cut complexes of cycle powers

## Finding

For integers \(p\ge 2\) and \(n\ge 6p-3\), let \(G=C_n^p\) be the graph with vertex set \(\mathbb Z/n\mathbb Z\), in which distinct vertices are adjacent when their circular distance is at most \(p\). Write \(K=\Delta_3(G)\) for the **ordinary** three-cut complex: its facets are complements of triples inducing disconnected subgraphs. Let \(r(i)=i+1\), \(s(i)=-i\), and let \(D_n=\langle r,s\rangle\) act by vertex permutations.

The sole nonzero reduced rational homology of \(K\) is \(H=\widetilde H_{n-4}(K;\mathbb Q)\). Its dimension, already determined in [3], is
\[
 B_{n,p}=\binom{n-2p}{2}-(2p^2+p-1).
\]
The following formulas determine the entire dihedral character \(\chi(g)=\operatorname{tr}(g\mid H)\):
\[
\boxed{\chi(r^a)=
\begin{cases}
B_{n,p},&a\equiv0\pmod n,\\
(-1)^{n/2}(1-n/2),&n\text{ even and }a\equiv n/2\pmod n,\\
(-1)^{a(n-1)},&\text{otherwise}.
\end{cases}}
\]
For every integer \(a\),
\[
\boxed{\chi(r^as)=
\begin{cases}
(-1)^{(n-1)/2}(4p-n-1)/2,& n\text{ odd},\\
(-1)^{(n-2)/2}(2p+1-n/2),&n\text{ even},\ a\text{ even},\\
(-1)^{n/2}(2p-1-n/2),&n\text{ even},\ a\text{ odd}.
\end{cases}}
\]
The rotation character is included to make the statement self-contained; its information was previously obtained in [4]. The new contribution is the **uniform reflection character for all powers**, particularly \(p\ge3\); the \(p=2\) case is already known [5]. These formulas give the isomorphism class of the rational \(D_n\)-module, since characteristic-zero representations of finite groups are determined by their characters.

The dimension of its invariant subspace is consequently
\[
\boxed{\dim_{\mathbb Q} H^{D_n}=
\begin{cases}
0,& n\equiv1\pmod4,\\
(n-4p+1)/2,&n\equiv3\pmod4,\\
\big(n-4p-1-3(-1)^{n/2}\big)/4,&n\text{ even}.
\end{cases}}
\]
In particular, the invariant subspace vanishes for **every** admissible length \(n\equiv1\pmod4\), regardless of the graph power.

## Assumptions and scope

The graph metric is irrelevant: the complex is constructed from disconnected induced triples, not from Vietoris–Rips or total-cut facets. The integer bounds are \(p\ge2\) and \(n\ge6p-3\), with no claim about the smaller interval. Coefficients in the representation theorem are rational. The underlying shellability and homology-concentration theorem is [3]. All equalities concern the natural dihedral action; no equivariant homotopy equivalence, integral decomposition, or torsion computation is asserted.

## Proof

**1. Alexander dual and its signed character.** Put \(\Gamma=K^\vee\). A set \(S\subseteq\mathbb Z/n\mathbb Z\) belongs to \(\Gamma\) precisely when it contains no disconnected induced triple. Such a triple has at most one edge; equivalently, among every three vertices of \(S\) there is at most one nonedge. Therefore
\[
 S\in\Gamma\quad\Longleftrightarrow\quad
\text{each vertex of }S\text{ has at most one nonneighbor inside }S.
\tag{1}
\]
The equivalence includes all sets of cardinality zero, one, or two. As \(\Gamma\) has a complete one-skeleton, it is connected. The shellability result [3, Theorem 1.4] and combinatorial Alexander duality show that its only nonzero reduced rational cohomology is \(\widetilde H^1(\Gamma;\mathbb Q)\), identified with \(H\) after tensoring with the sign representation of the ambient permutation action. The sign twist follows directly from the complement-of-oriented-simplex chain correspondence: a permutation of the \(n\) ambient vertices changes its orientation by its full permutation sign.

For any vertex permutation \(g\) preserving \(G\), the augmented Hopf-trace formula consequently gives
\[
 \operatorname{tr}(g\mid H)
 =\operatorname{sgn}(g)
 \sum_{\substack{S\in\Gamma\\gS=S}}
 (-1)^{|S|}\operatorname{sgn}(g\mid S).
\tag{2}
\]
The empty face occurs in the sum and contributes \(+1\). Equation (2) is an exact signed-face formula, not a finite-size approximation.

**2. Nonidentity rotations.** For \(g=r^a\) of order \(d\ge3\), any nonempty invariant face contains an entire rotation orbit with \(d\) regularly spaced vertices. Write \(n=ds\). Each orbit vertex has at least \(d-1-2\lfloor p/s\rfloor\) nonneighbors within that orbit. This number is at least two. Indeed: for \(d=3,4\), \(s>p\); for \(d=5,6\), \(s\ge p\); for \(d\ge7\), use \(p/s\le d/6+1/(2s)\) to get \(d-1-2\lfloor p/s\rfloor\ge 2d/3-2>2\). These inequalities use only \(n\ge6p-3\) and \(p\ge2\). By (1) there is no nonempty invariant face, so the inner sum in (2) is \(1\).

For a half-turn, necessarily \(n=2m\), each orbit is an antipodal nonedge pair. Two such orbits cannot appear together in a face: the distance \(m>2p\) prevents one vertex from being adjacent to both members of another antipodal pair, while its own antipode already consumes its one permitted nonneighbor. Thus the invariant faces are the empty face and the \(m\) antipodal pairs, with inner signed sum \(1-m\). The sign of \(r^a\) is \((-1)^{a(n-1)}\), and the sign of the half-turn is \((-1)^m\). The identity trace is the previously proved Betti number \(B_{n,p}\). This proves the rotation formula.

**3. The reflection orbit lemma.** Each reflection partitions the vertices into \(f\) fixed singletons and \(q=(n-f)/2\) exchanged pairs. There are three possibilities: one fixed vertex and one opposite edge axis when \(n\) is odd; two opposite fixed vertices when \(n\) is even and \(a\) is even; and two edge axes when \(n\) is even and \(a\) is odd.

Call an exchanged pair an *orbit pair*. Two distinct orbit pairs form a face of \(\Gamma\) together if and only if they are based near the **same** reflection axis, with their positive offsets \(u<v\) satisfying
\[
 u+v\le p\quad\text{(vertex axis)},\qquad
 u+v+1\le p\quad\text{(edge axis)}.
\tag{3}
\]
Here offsets are respectively positive integers \(1,2,\ldots\) or nonnegative integers \(0,1,\ldots\), according to whether the axis passes through a vertex or an edge midpoint. To check (3), order the two pairs along one fundamental semicircle. Their two same-side distances are \(v-u\); their two cross-side distances equal the smaller of the distances obtained by summing the offsets at the first or opposite reflection axis. If the cross-side distance exceeds \(p\), then each vertex already has a nonneighbor in the other pair, forcing both pair-internal edges and both same-side edges to be present. The pair-internal conditions put each pair within \(p/2\) of an axis; the same-side condition forces both near the **same** axis, because the axes are separated by \(n/2\ge3p-3/2\). Their cross-side distance would then be at most \(p\), a contradiction. Conversely, either inequality in (3) makes all four cross-orbit edges present; each vertex can then have at most one missing edge, namely to its own reflection partner. This proves (3) and also shows that sets with two or more orbit pairs lie entirely near a single axis. Such sets are faces precisely when their two largest offsets obey (3).

A face involving an axis-fixed vertex and one orbit pair exists exactly when that pair is among the \(p\) closest pairs on its vertex-axis side. In a face with two or more orbit pairs near a vertex axis, the fixed axis vertex can always be toggled: all its orbit-pair vertices lie within graph distance \(p\), and toggling preserves (1). When two fixed vertices exist, no face can contain both together with an orbit pair, as their separation is greater than \(2p\).

**4. Weighted count for the axes.** In the inner sum of (2), an invariant face consisting of \(j\) orbit pairs and \(e\) fixed singletons contributes \((-1)^{j+e}\): there are \(2j+e\) vertices and the restricted permutation has sign \((-1)^j\). The empty face, the subsets of fixed vertices, and the \(q\) lone orbit pairs contribute
\[
 1-f+\binom f2-q.
\tag{4}
\]
For each vertex axis, the \(p\) faces consisting of the center vertex and one of its \(p\) nearest orbit pairs add \(+p\). Every face using at least two orbit pairs near that axis cancels with the face obtained by toggling the fixed center vertex.

For each edge axis, faces with at least two orbit pairs have offsets \(0\le a_1<\cdots<a_j\), \(j\ge2\), with \(a_{j-1}+a_j+1\le p\). Their signed contribution is
\[
 \sum_{\substack{0\le b<c\\b+c+1\le p}}
 \sum_{T\subseteq\{0,\ldots,b-1\}}(-1)^{|T|+2}
 =\sum_{c=1}^{p-1}1=p-1.
\tag{5}
\]
The inner subset sum vanishes for \(b>0\), so only \(b=0\) remains. Combining (4)–(5), the inner sum in (2) is
\[
 \begin{cases}
 2p-1-(n-1)/2,& n\text{ odd},\\
 2p-(n-2)/2,&n\text{ even},\ a\text{ even},\\
 1+2(p-1)-n/2,&n\text{ even},\ a\text{ odd}.
 \end{cases}
\]
The corresponding ambient permutation signs are \((-1)^{(n-1)/2}\), \((-1)^{(n-2)/2}\), and \((-1)^{n/2}\). This proves all three reflection formulas for every permitted \(p,n\).

**5. Invariants.** For a rational representation of the finite group \(D_n\), the dimension of invariants is the average of the character over its \(2n\) elements. Substitute the rotation and reflection formulas. When \(n=2m+1\), the sum of character values reduces to zero if \(m\) is even, and to \(2n(m-2p+1)\) if \(m\) is odd. When \(n=2m\), it reduces to \(n(2m-4p-1-3(-1)^m)/2\). Division by \(2n\) gives the stated dimensions.

## Verification

The standalone Python file `verify.py` implements two independent finite checks. Its first method enumerates permutation-invariant faces of \(\Gamma\) by orbit selection and tests condition (1), independent of the axis-counting proof. Its second method constructs the cut complex directly as the downward closure of complements of disconnected triples, then computes signed simplicial Lefschetz traces **without** using Alexander duality. The recorded execution in `verification_output.txt` checked 30 parameter pairs, 165 dual orbit traces, 122 direct cut-complex group traces, and 30 Burnside averages, all passing. These tests corroborate the general theorem; its infinite quantifiers are established by the preceding combinatorial argument, not by enumeration.

Reproduce with `python3 verify.py` from the directory containing the standalone file. No third-party Python packages or network access are needed.

## Relationship to prior work

The definition and earlier equivariant methods for cut complexes come from Bayer and collaborators [1], first public on 2023-04-26. Their subsequent paper [6, Theorem 6.6] determines the dihedral action for unpowered cycles (the graph power \(p=1\)), but not the powers covered here. The homology and shellability of squared-cycle three-cut complexes were established in [2]. The general \(p\ge2\) homotopy concentration and Betti formula were proved in [3], whose 2026 preprint has primary MSC2020 classification \(57M15\). A published study [4] already gives the **rotation** character for all admissible powers, and a separate study [5] gives the **full dihedral** character when \(p=2\). These results are not re-claimed. The genuinely new part is the closed all-power reflection calculation, which converts [4] into a complete dihedral classification for every \(p\ge3\). Literature and indexed-result searches did not reveal an implication from any inspected prior theorem to these all-power reflection values.

## Limitations

This result is about rational homology representations, not integral dihedral modules, integral quotient homology, higher cut parameters, or smaller graph lengths. The proof relies on [3] for the vanishing of other homology groups. The finite verification is not a substitute for that external theorem or the symbolic orbit argument. No independent external audit has been performed. An equivalent derivation outside the inspected literature remains possible.

## References

[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first submitted 2023-04-26, https://arxiv.org/abs/2304.13675.

[2] P. Chauhan, S. Shukla, K. Vinayak, *Shellability of 3-Cut Complexes of Squared Cycle Graphs*, arXiv:2406.01979, first submitted 2024-06-04, https://arxiv.org/abs/2406.01979.

[3] P. Chauhan, S. Shukla, *Shellability of 3-Cut Complexes of Powers of Cycle Graphs*, arXiv:2603.23155, first submitted 2026-03-24, Theorem 1.4, https://arxiv.org/abs/2603.23155.

[4] *Rational cyclic homology representations of three-cut complexes of cycle powers*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-rational-cyclic-homology-representations-of-three-cut-complexes--dc0f17aad16d.

[5] *Full dihedral homology characters of three-cut complexes of squared cycles*, preceding mathematical calculation for the special case \(p=2\).

[6] M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first submitted 2024-07-11, Theorem 6.6, https://arxiv.org/abs/2407.08158.
