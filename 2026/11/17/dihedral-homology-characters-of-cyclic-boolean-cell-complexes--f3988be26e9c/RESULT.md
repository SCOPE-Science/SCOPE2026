# Dihedral homology characters of cyclic Boolean cell complexes

## Finding
For each integer \(n\ge 3\), let \(C_n\) be the simple cycle on \(\mathbb Z/n\mathbb Z\), and let \(B_n=\Delta(C_n)\) be its Boolean cell complex (injective vertex words modulo interchanges of consecutive letters that are nonadjacent in \(C_n\)). Its geometric realization has the homotopy type of a wedge of \(L_n-2\) spheres of dimension \(n-1\), where \(L_0=2\), \(L_1=1\), and \(L_{j+2}=L_{j+1}+L_j\). This nonequivariant sphere classification and multiplicity are established in earlier work, not claimed here.

**Theorem (complete dihedral character).** Write \(D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\), acting on vertex labels by \(r(i)=i+1\) and \(s(i)=-i\). Let \(\chi_n\) be the character of the induced representation on \(\widetilde H_{n-1}(B_n;\mathbb Q)\). Define the integer sequence \(P_0=1\), \(P_1=0\), \(P_{j+2}=-P_{j+1}+P_j\). Then for every \(0\le k<n\), with \(d=\gcd(n,k)\),
\[
\chi_n(r^k)=(-1)^{n+d}(L_d-2).
\]
For every \(0\le a<n\),
\[
\chi_n(r^a s)=
\begin{cases}
-P_{(n-1)/2},&n\text{ odd};\\
P_{n/2+1},&n\text{ even and }a\text{ even};\\
P_{n/2-2},&n\text{ even and }a\text{ odd}.
\end{cases}
\]
These are the character values on all \(2n\) group elements, not merely their dimensions or Euler characteristics. In particular, the dimension of the full-dihedral invariant rational top homology, equivalently the \((n-1)\)-st rational Betti number of the geometric quotient, is
\[
 b_{n-1}(|B_n|/D_n;\mathbb Q)
 =\frac1{2n}\left(\sum_{k=0}^{n-1}(-1)^{n+\gcd(n,k)}(L_{\gcd(n,k)}-2)
 +\sum_{a=0}^{n-1}\chi_n(r^as)\right).
\]
No other positive-degree rational homology of the quotient occurs. The quotient assertion concerns rational coefficients; no claim is made about its integral torsion or fundamental group.

For \(n=3,4,5,6,7,8\), the full-dihedral invariant ranks are respectively \(0,1,0,2,2,3\). Thus already the smallest cycle cases distinguish the reflection-axis classes when \(n\) is even.

## Assumptions and scope
A cell of \(B_n\) is a commutation class \([w]\) of an injective word \(w\) on a nonempty subset \(S\subseteq\mathbb Z/n\mathbb Z\). It has dimension \(|S|-1\). Its characteristic map is a simplex with vertices indexed by \(S\); distinct cells may have the same vertices. The empty word is included only in the augmented chain complex. Diagram automorphisms act by relabeling letters, hence by cellular homeomorphisms. Each oriented cell uses its vertex labels in increasing numerical order, independently of the representative word. The resulting signed action on a cell supported on \(S\) has coefficient \(\operatorname{sgn}(g|S)\).

The theorem is for simple cycles with \(n\ge3\), all their dihedral elements and rational coefficients on the resulting representations; the underlying CW complexes have torsion-free integral homology by the previously established wedge-of-spheres theorem.

## Proof
**1. Word classes and orientations.** For any support \(S\), a word orders the endpoints of every edge of the induced graph \(C_n[S]\). Direct each such edge from the earlier to the later letter. The resulting orientation is acyclic. Conversely, each acyclic orientation has a topological ordering; two such orderings differ by adjacent swaps of incomparable letters, necessarily nonadjacent in the graph. Thus the cells supported on \(S\) are precisely the acyclic orientations of \(C_n[S]\). This bijection is equivariant under graph automorphisms and respects deleting a vertex.

**2. Cellular Lefschetz expression.** Let \(A_g(S)\) be the number of \(g\)-invariant acyclic orientations of the induced graph on a \(g\)-stable subset \(S\), with \(A_g(\varnothing)=1\). The signed cellular trace in degree \(|S|-1\) is \(\operatorname{sgn}(g|S)A_g(S)\). The established homotopy classification concentrates reduced rational homology in degree \(n-1\). The augmented Lefschetz identity therefore gives
\[
\chi_n(g)=(-1)^n\sum_{\substack{S\subseteq\mathbb Z/n\mathbb Z\\gS=S}}
 (-1)^{|S|}\operatorname{sgn}(g|S)A_g(S).\tag{1}
\]
The empty subset contributes \(1\) inside this sum. The sign in (1) is essential: fixed cells alone, without orientations, do not give the character.

**3. Rotations.** For \(g=r^k\), let \(d=\gcd(n,k)\). A stable vertex subset is a periodic repetition of a binary length-\(d\) pattern \(T\). Every selected vertex orbit has length \(n/d\). Consequently
\[
 (-1)^{|S|}\operatorname{sgn}(g|S)=(-1)^{|T|},
\]
since one selected orbit contributes the sign \((-1)^{n/d-1}\) and \((-1)^{n/d}\) from its size.

For a proper pattern, the invariant orientations are determined by the choices on the edge-orbits whose two endpoint orbits are selected. For the full pattern all \(d\) edge orbits can be oriented independently except for the two coherent directed cycles, which are forbidden. This remains valid for \(d=1,2\), interpreting the quotient as a cyclic list of \(d\) edge positions rather than a simple quotient graph. Introduce
\[
 T=\begin{pmatrix}1&-1\\1&-2\end{pmatrix}.
\]
A two-state cyclic transfer-matrix expansion, whose state is whether an orbit is selected and whose selected edge weight is \(2\), yields the alternating sum \(\operatorname{tr}(T^d)-2(-1)^d\). Since the characteristic polynomial of \(T\) is \(t^2+t-1\), its eigenvalues are \((-1\pm\sqrt5)/2\); hence \(\operatorname{tr}(T^d)=(-1)^d L_d\). Substituting into (1) gives \(\chi_n(r^k)=(-1)^{n+d}(L_d-2)\), including the identity rotation.

**4. Reflections.** Write \(g=r^as\), so \(g(i)=a-i\). Each stable subset is a union of vertex orbits. A selected fixed vertex contributes \(-1\) to \((-1)^{|S|}\operatorname{sgn}(g|S)\), and a selected transposed vertex pair also contributes \(-1\). A reflected edge whose endpoints are exchanged is incompatible with an invariant orientation, so a vertex orbit containing its endpoints is forced absent. All remaining selected edge orbits contribute a factor \(2\); there is no cyclic-orientation correction because a reflection reverses either globally coherent directed cycle, so neither is invariant.

When \(n=2m+1\), the folded quotient is a path on \(m+1\) vertex orbits, with the final orbit forbidden by the single inverted edge. The resulting signed partition function is that of a path on \(m\) vertices. The outer sign \((-1)^n=-1\) in (1) makes the trace \(-P_m\).

When \(n=2m\) and \(a\) is even, two opposite vertices are fixed and no edge is inverted; the folded quotient is a path on \(m+1\) vertex orbits, giving \(P_{m+1}\). When \(a\) is odd, there are no fixed vertices, but two opposite edges are inverted: the end vertex orbits must be absent, leaving a path on \(m-2\) vertex orbits, giving \(P_{m-2}\).

To identify the path partition function, let its final vertex be either absent or present. If \(u_j,v_j\) denote the signed sums with these respective states after \(j\) vertices, then \((u_0,v_0)=(1,0)\) and
\[
 (u_{j+1},v_{j+1})=(u_j+v_j,-u_j-2v_j).
\]
Therefore \(P_j=u_j+v_j\) satisfies \(P_0=1\), \(P_1=0\), \(P_{j+2}=-P_{j+1}+P_j\). These three cases yield the reflection formula without assuming any finite computation.

**5. Quotients.** For a finite cellular action, transfer and rational exactness of invariants identify \(H_*(|B_n|/D_n;\mathbb Q)\) with \(H_*(|B_n|;\mathbb Q)^{D_n}\). Averaging the character over the group gives the displayed invariant rank. By the original homotopy classification there are no other positive-degree ambient rational homology groups, so none occur in the quotient.

## Verification
Run `python3 verify_boolean_cycles.py` with standard-library Python. It constructs every nonempty cell directly from injective words and their induced edge orientations, builds signed cellular boundary maps, verifies \(\partial^2=0\), checks chain equivariance for generating rotations and both kinds of reflection, and independently computes the complete signed cellular character for all \(2n\) dihedral elements for each \(3\le n\le8\). In orders \(3\le n\le7\), it also computes the top boundary rank modulo two distinct odd primes, obtaining the expected top-homology rank \(L_n-2\). The final line is `BOOLEAN_CYCLE_DIHEDRAL_INTEGRAL_CELL_CHECK_PASS`. The infinite parameter range follows from the proof, not the finite checks.

## Relationship to prior work
Jonsson and Welker (2007) introduced and studied complexes of injective words and their commutation classes, including the present cellular construction; their focus is shellability and Cohen–Macaulay properties. Ragnarsson and Tenner (2008) established the wedge-of-spheres homotopy classification for Boolean complexes of all finite simple graphs, including affine type \(\widetilde A\) and its known Lucas multiplicity. Ragnarsson and Tenner (2010) constructed homology bases for Boolean complexes, principally over \(\mathbb F_2\). None of these results, in the portions and complete theorem statements inspected, specifies this entire integral-cell-induced rational dihedral character with its two distinct even-cycle reflection traces. The nonequivariant dimension is explicitly not claimed as new.

An analogous-looking representation theory for the different Coxeter-like complexes of Babson and Reiner concerns a group action on a distinct complex, not diagram relabeling of these commutation-class cells. No equivalence is asserted or implied solely from a similarity of terminology.

## Limitations
The theorem is confined to cycle Boolean complexes and rational representations. It does not determine the integral \(\mathbb Z[D_n]\)-module, integral quotient homology, or fundamental group. Equivalence to an unindexed historical formulation remains a possible novelty risk; database searches cannot prove uniqueness. Computations for \(n\le8\) are finite corroboration, not proof of the universal formulas. The results have not undergone independent mathematical validation.

## References
1. J. Jonsson and V. Welker, *Complexes of Injective Words and Their Commutation Classes*, arXiv:0712.2143, first submitted 2007-12-13. https://arxiv.org/abs/0712.2143
2. K. Ragnarsson and B. E. Tenner, *Homotopy Type of the Boolean Complex of a Coxeter System*, arXiv:0806.0906, first submitted 2008-06-05. https://arxiv.org/abs/0806.0906
3. K. Ragnarsson and B. E. Tenner, *Homology of the Boolean Complex*, arXiv:1005.4411, first submitted 2010-05-24. https://arxiv.org/abs/1005.4411
4. E. Babson and V. Reiner, *Coxeter-like Complexes*, Discrete Mathematics and Theoretical Computer Science 6 (2004), DOI 10.46298/dmtcs.312. https://dmtcs.episciences.org/articles/312
