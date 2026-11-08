# Integral arrow-reversal homology and quotients of bidirected-polygon multipath complexes

## Finding
For every integer \(m\ge5\), let \(B_m\) be the bidirected cycle on \(\mathbb Z/m\mathbb Z\), containing both arrows between adjacent vertices, and let \(X_m\) be its **multipath complex**: simplices are sets of arrows whose spanning directed subgraph is a disjoint union of directed paths and isolated vertices. Write \(\rho(i)=i+1\), \(\sigma(i)=-i\) for the vertex rotation and reflection, and let \(a\) reverse every selected arrow **without moving its endpoints**. These define commuting actions of \(a\) and the natural dihedral symmetries on \(X_m\). Set
\[
j(m)=\begin{cases}(m-1)/2,&m\equiv1\pmod4,\\(m-2)/2,&m\equiv2\pmod4,\\(m-3)/2,&m\equiv3\pmod4,\\m/2-1,&m\equiv0\pmod4.\end{cases}
\]

**Theorem (integral symmetry identities and quotient).** The geometric involution \(a:|X_m|\to|X_m|\) is fixed-point-free. On the free abelian reduced homology groups its induced action obeys the exact integral identities
\[
\boxed{a_*|_{\widetilde H_{j(m)}(X_m;\mathbb Z)}=\begin{cases}-I,&4\nmid m,\\-\rho_*^{\,2},&4\mid m,\end{cases}}
\qquad
\boxed{a_*|_{\widetilde H_{m-2}(X_m;\mathbb Z)}=(-1)^{\lfloor m/2\rfloor}\sigma_*.}
\]
The lower group has rank one unless \(4\mid m\), when its rank is three; the top group has rank two. All other reduced integral homology vanishes. Thus, over \(\mathbb Q\), arrow reversal has lower \((+1,-1)\)-eigenspace dimensions \((0,1)\) when \(4\nmid m\) and \((2,1)\) when \(4\mid m\). On top homology its eigenspace dimensions are \((1,1)\).

The quotient \(Y_m=|X_m|/\langle a\rangle\) is a genuine twofold covering quotient, and its reduced rational homology is exactly
\[
\boxed{\widetilde H_i(Y_m;\mathbb Q)\cong\begin{cases}
\mathbb Q,&i=m-2,\\
\mathbb Q^2,&4\mid m\text{ and }i=m/2-1,\\
0,&\text{otherwise}.
\end{cases}}
\]
For every \(m\ge6\), its fundamental group is \(\pi_1(Y_m)\cong C_2\).

## Assumptions and scope
All cycles are simple, with \(m\ge5\) vertices. A multipath contains no directed cycles (including two-cycles) and has indegree and outdegree at most one at each vertex. The arrow-reversal map \(a\) is a simplicial involution because reversing all arrows reverses every path; it is **not** a vertex-permutation automorphism of the underlying directed graph. The involution is central with respect to the dihedral action. The integer homology concentration and ranks quoted above are the nonequivariant theorem of Caputi, Collari and Smith, *Multipath complexes of bidirectional polygonal digraphs*, Theorem 2.10, with their parameter \(n=m-1\). The remaining topological and symmetry conclusions are established here. We do not assert an integral decomposition of the full dihedral module, or an equivariant homotopy equivalence.

## Proof
**1. The action is free on the realization.** Every directed arrow \(e:u\to v\) has a distinct reverse \(a(e):v\to u\), and no multipath simplex can contain both, since they form a directed two-cycle. If a point of the geometric realization were fixed by \(a\), its unique minimal carrier simplex would be \(a\)-invariant. Such a nonempty carrier would contain both \(e\) and \(a(e)\), a contradiction. Hence \(|X_m|^a=\varnothing\). The augmented simplicial chains have no fixed nonempty basis face under \(a\), whereas the unique augmented degree-minus-one basis element is fixed. Therefore the **reduced** Lefschetz number is \(\widetilde\Lambda(a)=-1\).

**2. Top integral cycles and the reflection identity.** Label the clockwise arrows \(f_i:i\to i+1\) and counterclockwise arrows \(b_i:i+1\to i\), with indices modulo \(m\). Every \((m-2)\)-simplex is a Hamiltonian directed path, obtained by omitting one arrow from the full clockwise or full counterclockwise directed cycle. In particular, the only top simplices are the \(2m\) paths of these two kinds. Define
\[
z_+=\partial[f_0,f_1,\ldots,f_{m-1}],\qquad z_-=\partial[b_0,b_1,\ldots,b_{m-1}],
\]
where the brackets denote *formal* simplices in the ambient simplex, so their boundaries lie in \(X_m\). In each orientation family, the top boundary kernel is generated primitively by this alternating boundary; the clockwise and counterclockwise supports are disjoint, including in their boundaries. Thus \(z_+,z_-\) form a \(\mathbb Z\)-basis of \(\widetilde H_{m-2}\). The maps act by
\[
\rho_*(z_\pm)=(-1)^{m-1}z_\pm,\quad a_*(z_+)=z_-,\quad a_*(z_-)=z_+.
\]
For \(\sigma(i)=-i\), the arrow index map is \(f_i\mapsto b_{-i-1}\); the involution \(i\mapsto-i-1\) has \(\lfloor m/2\rfloor\) transpositions. Therefore \(\sigma_*(z_\pm)=(-1)^{\lfloor m/2\rfloor}z_\mp\). The asserted integral top identity follows, and \(\operatorname{tr}(a_*|\widetilde H_{m-2})=0\).

**3. The complete rotation character on lower rational homology, obtained independently.** For \(k\in\mathbb Z\), set \(d=\gcd(m,k)\), with \(d=m\) at \(k=0\). A face invariant under \(\rho^k\) is described by a cyclic word of length \(d\) in \(\{0,+,-\}\): zero means an absent unoriented edge; the two signs encode the allowed arrow orientation. Adjacent occupied positions must have the same sign, and the two nonzero constant words are excluded because they lift to directed full cycles. The contribution of an occupied position to the signed Lefschetz orbit sum is \(-1\). The three-state weighted transfer matrix is
\[
M=\begin{pmatrix}1&-1&-1\\1&-1&0\\1&0&-1\end{pmatrix},
\]
with characteristic polynomial \((u+1)(u^2+1)\). Its trace is \(\operatorname{tr}(M^d)=(-1)^d+2\cos(\pi d/2)\). Subtracting the two prohibited constant words gives the orbit sum
\[
S_d=\operatorname{tr}(M^d)-2(-1)^d=2\cos(\pi d/2)-(-1)^d.
\]
The augmented-chain sign for a selected arrow orbit is \(-1\); consequently \(\widetilde\Lambda(\rho^k)=-S_d=(-1)^d-2\cos(\pi d/2)\), i.e. \(3\) for \(d\equiv2\pmod4\), and \(-1\) otherwise. Top homology contributes \(2(-1)^d\) to this alternating Lefschetz number by Step 2. In the unique remaining degree \(j(m)\), the lower trace is therefore
\[
\operatorname{tr}(\rho_*^k|\widetilde H_{j(m)}(X_m;\mathbb Q))=\begin{cases}
1,&4\nmid m,\\
3,&4\mid m\text{ and }4\mid k,\\
-1,&4\mid m\text{ and }4\nmid k.
\end{cases}
\]
Because rational representations of finite cyclic groups are semisimple and determined by characters, the lower module is the trivial line when \(4\nmid m\), and when \(4\mid m\) it is the direct sum of the rotation-sign line \(\mathbb Q_-\) (where \(\rho=-1\)) and the two-dimensional cyclotomic plane \(\mathbb Q(i)\) (where \(\rho\) is multiplication by \(i\)). This independently establishes the exact rotation spectrum needed below; it is consistent with the earlier dihedral character classification cited under prior work.

**4. Integral reversal identity.** The homology-rank theorem and Step 2, together with \(\widetilde\Lambda(a)=-1\), give
\[
(-1)^{j(m)}\operatorname{tr}(a_*|\widetilde H_{j(m)}(X_m;\mathbb Q))=-1.
\]
The integer \(j(m)\) is even when \(4\nmid m\) and odd when \(4\mid m\). In the rank-one case this forces \(a_*=-I\). When \(4\mid m\), the rational lower module is \(\mathbb Q_-\oplus\mathbb Q(i)\) by Step 3. Since \(a\) commutes with \(\rho\), it preserves these two inequivalent rational cyclic summands. On the first summand it acts by \(\pm1\); on the second, it is multiplication by an element of \(\mathbb Q(i)\) whose square is one, hence again by \(\pm1\). Its trace is \(+1\), so it must act by \(-1\) on \(\mathbb Q_-\) and by \(+1\) on \(\mathbb Q(i)\), exactly the action of \(-\rho^2\). All the integral homology groups here are free abelian by the cited theorem. Equality of integer endomorphisms after tensoring with \(\mathbb Q\) therefore gives equality over \(\mathbb Z\). This proves both integral identities and all claimed eigenspace ranks.

**5. Quotient and fundamental group.** By Step 1, the quotient map \(|X_m|\to Y_m\) is a free twofold covering of finite polyhedra. Transfer over \(\mathbb Q\) identifies \(H_*(Y_m;\mathbb Q)\) with the \(+1\) eigenspaces of \(a_*\) on \(H_*(X_m;\mathbb Q)\). Step 4 gives the lower eigenspace ranks; Step 2 gives one top invariant generator. No other reduced homology groups occur. For \(m\ge6\), the connectivity theorem of Caputi–Collari–Smith (Theorem 2.8 with \(n=m-1\)) makes \(|X_m|\) simply connected; it is then the universal cover of \(Y_m\), with deck group \(C_2\). Hence \(\pi_1(Y_m)\cong C_2\).

## Verification
The accompanying standalone `verify.py` enumerates multipath faces directly as directed edge subsets and checks indegree, outdegree, and directed cycles; it does **not** assume the three-state word model in its face generator. For \(5\le m\le10\), it verifies no nonempty \(a\)-stable simplex and independently computes signed augmented-chain Lefschetz numbers for all rotations and all rotation–reversal compositions. The predicted rational characters match all \(90\) computations across \(11,418\) generated simplices. For \(5\le m\le8\), an independent quotient-chain complex computes ranks of reduced homology over the two odd primes \(1009\) and \(1013\); these match the predicted rational Betti numbers. The source-backed integral ranks, transfer argument, and algebraic proof above establish all \(m\); finite characteristic computations alone are not a proof of a characteristic-zero or integral theorem. Run `python verify.py` from a directory containing only this standalone script; see `verify_output.txt` for the recorded output.

## Relationship to prior work
Caputi, Collari and Smith establish the nonequivariant integral homology and connectivity of \(X_m\), not the orientation-reversal quotient or the integral equality between reversal and rotation on homology. A separate published dihedral rational-character calculation determines the action of vertex rotations and reflections, but does **not** include the independent arrow-reversal involution, the integral operator identities, the free twofold quotient, or its fundamental group. The rotation character is rederived above, rather than counted as a new result. The new claim is the **graded integral identification of the independent arrow-reversal action** and the resulting all-length quotient topology; it is not the previous Betti-rank or dihedral-character classification.

## Limitations
The claims concern the bidirected simple cycle with at least five vertices and its **global** reversal of all arrows. They do not determine the full integral \(\mathbb Z[D_m\times C_2]\)-module isomorphism class, higher integral torsion in the quotient, geometric fixed-point types of mixed vertex–reversal symmetries, or equivariant homotopy equivalences. The rational quotient Betti formula does not assert an integral homology classification. Equivalent unindexed literature remains possible.

## References
1. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, first public 2026-01-09, especially Theorems 2.8 and 2.10, https://arxiv.org/abs/2601.05670 .
2. *Dihedral rational homology of bidirectional-polygon multipath complexes*, published mathematical record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-dihedral-rational-homology-of-bidirectional-polygon-multipath-co--627013477864 .
3. L. Caputi, C. Collari, S. Di Trani, *Combinatorial and topological aspects of path posets, and multipath cohomology*, Journal of Algebraic Combinatorics 57 (2023), https://doi.org/10.1007/s10801-022-01180-9 .
