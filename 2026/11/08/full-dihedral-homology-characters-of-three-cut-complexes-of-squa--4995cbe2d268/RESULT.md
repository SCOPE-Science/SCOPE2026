# Full dihedral homology characters of three-cut complexes of squared cycles

## Finding
For every integer \(n\ge9\), put \(W_n=C_n^2\), the square of the cycle on \(V=\mathbb Z/n\mathbb Z\): vertices are adjacent when their cyclic distance is one or two. Let \(K_n=\Delta_3(W_n)\) be the **ordinary three-cut complex**, whose facets are complements in \(V\) of triples inducing disconnected graphs. Let \(D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\) act by \(r(i)=i+1\) and \(s(i)=-i\), and set \(\mathcal H_n=\widetilde H_{n-4}(K_n;\mathbb Q)\).

The full rational dihedral character \(\chi_n\) is as follows. Define \(B_n=\binom{n-4}{2}-9=1+n(n-9)/2\). For a rotation \(r^a\), where \(0\le a<n\),
\[
\chi_n(r^a)=\begin{cases}
B_n,&a=0,\\
(-1)^{n/2}(1-n/2),&n\text{ even and }a=n/2,\\
(-1)^{n-\gcd(n,a)},&\text{all remaining }a\ne0.
\end{cases}
\]
For every reflection \(r^a s\),
\[
\boxed{\chi_n(r^a s)=\begin{cases}
(-1)^{(n-1)/2}(7-n)/2,&n\text{ odd},\\
(-1)^{(n-2)/2}(5-n/2),&n\text{ even},\ a\text{ even},\\
(-1)^{n/2}(3-n/2),&n\text{ even},\ a\text{ odd}.
\end{cases}}
\]
In the even case, the second and third lines respectively refer to reflection axes passing through two vertices and through two edges of the underlying cycle. The rotation character, the dimension \(B_n\), and homological concentration were previously established; the reflected character and hence the full \(D_n\)-module constitute the present refinement. Rational representations of a finite group are determined by their rational characters (by extension to the complex numbers and semisimplicity), so the formulas specify the complete rational representation. In particular, the dimension of the invariant space is
\[
\dim\mathcal H_n^{D_n}=\begin{cases}
\dfrac{(n-7)(1-(-1)^{(n-1)/2})}{4},&n\text{ odd},\\[3pt]
\dfrac{n-9-3(-1)^{n/2}}4,&n\text{ even}.
\end{cases}
\]
All other reduced rational homology degrees vanish by the prior shellability theorem.

## Assumptions and scope
Here the ordinary cut complex uses **disconnected** removed triples, not the *total cut complex* (which uses independent triples). The dihedral action is on the labeled underlying cycle, not on an abstract permutation of the homology basis. All signs in the character refer to oriented simplicial chains, and homology coefficients are \(\mathbb Q\). All inequalities are inclusive at \(n=9\). No result is asserted for \(n<9\). The nonequivariant theorem \(K_n\simeq\bigvee^{B_n}S^{n-4}\), for \(n\ge9\), is an input from [2] (also subsumed by [3]); it is not a new result here.

## Proof
**1. A small complementary relative complex.** Let \(\Delta\) be the full simplex on \(V\). A vertex set \(U\subseteq V\) is a face of \(K_n\) exactly when \(V\setminus U\) contains a disconnected induced triple. Consequently, a relative chain basis element \([U]\in C_*(\Delta,K_n;\mathbb Q)\) corresponds to a complement \(S=V\setminus U\) such that **every three-element subset of \(S\) induces a connected subgraph of \(W_n\)**. This condition is vacuous for \(|S|\le2\).

The complete list of complementary sets satisfying it, for all \(n\ge9\), is:
\[
\mathcal A_0=\{\varnothing\},\quad
\mathcal A_1=\binom V1,\quad
\mathcal A_2=\binom V2,\quad
|\mathcal A_3|=4n,\quad
\mathcal A_4=\{\{i,i+1,i+2,i+3\}:i\in V\},
\]
with no \(\mathcal A_q\) for \(q\ge5\).

For triples, a connected induced graph has a vertex joined to the other two. Each vertex has four neighbors, so center-counting gives \(6n\); only triangles are counted three times, and \(W_n\) has precisely the \(n\) triangles \(\{i,i+1,i+2\}\). Thus \(|\mathcal A_3|=6n-2n=4n\). For four vertices in cyclic order, write the four positive cyclic gaps. At least one gap is \(\ge3\), since four gaps at most two would sum to at most eight. Across such a gap the endpoint vertices are nonadjacent (the complementary arc has at least three steps too). Because every triple must induce a connected graph, **each vertex has at most one nonneighbor among the four vertices**. The two endpoints must therefore each be adjacent to both other vertices. The remaining three gaps must each be one, so the four-set is a consecutive block. Conversely every consecutive four-block meets the condition. Any five-set meeting the condition would have all its four-subsets consecutive blocks. Choose a contained four-block \(\{i,i+1,i+2,i+3\}\) and a fifth vertex \(x\). Then \(\{i,i+2,i+3,x\}\) must also be a consecutive four-block. But for \(n\ge9\), the three vertices \(i,i+2,i+3\) belong together to exactly one consecutive four-block, namely \(\{i,i+1,i+2,i+3\}\). This forces \(x=i+1\), which contradicts distinctness. Hence no five-set occurs, and larger sets are excluded by heredity.

**2. The relative Hopf-trace identity.** Let \(g\in D_n\) be a permutation of \(V\). Because \(\Delta\) is contractible and [2] shows that the reduced homology of \(K_n\) is concentrated in dimension \(n-4\), the relative homology of \((\Delta,K_n)\) is concentrated in degree \(n-3\), with \(H_{n-3}(\Delta,K_n;\mathbb Q)\cong\mathcal H_n\) naturally under \(g\). Each relative oriented simplex is the complement of \(S\in\mathcal A_q\) and lies in degree \(n-q-1\). If \(g(S)=S\), the coefficient of that simplex in its image is \(\operatorname{sgn}(g|_{V\setminus S})=\operatorname{sgn}(g)\operatorname{sgn}(g|_S)\). Writing
\[
T_q(g)=\sum_{S\in\mathcal A_q,\ gS=S}\operatorname{sgn}(g|_S),
\]
where \(T_0(g)=1\), Hopf's trace formula gives the **exact character identity**
\[
\chi_n(g)=\operatorname{sgn}(g)\bigl(T_0(g)-T_1(g)+T_2(g)-T_3(g)+T_4(g)\bigr).
\tag{*}
\]
The relative trace identity is valid in characteristic zero; it is not just a numerical Euler-characteristic approximation.

**3. Reflections.** Write \(g(i)=a-i\pmod n\) and let \(f\) be the number of its fixed vertices. Then \(f=1\) for odd \(n\), while \(f=2\) when \(n\) is even and \(a\) is even, and \(f=0\) when \(n\) is even and \(a\) is odd. The permutation comprises \((n-f)/2\) transpositions and thus has sign \((-1)^{(n-f)/2}\). Its fixed oriented singletons contribute \(T_1=f\), and its invariant unordered pairs are the \(\binom f2\) fixed pairs (sign \(+1\)) and \((n-f)/2\) exchanged pairs (sign \(-1\)), giving
\[
T_2=\binom f2-(n-f)/2.
\]
An invariant connected triple must consist of one fixed vertex and one exchanged pair. For each fixed vertex, the two exchanged pairs at cyclic offsets one and two give exactly the connected triples; no pair farther away can connect that vertex. This yields \(T_3=-2\) for odd \(n\), \(T_3=-4\) for even vertex-axis reflections, and \(T_3=0\) for even edge-axis reflections. The sign is negative because the reflection interchanges two elements of every such triple.

A consecutive four-block is fixed by a reflection precisely when its midpoint edge is fixed. The reflection reverses the four vertices, producing two transpositions and sign \(+1\). There is exactly one such block for odd \(n\), none for even vertex-axis reflections, and two for even edge-axis reflections. Hence \(T_4\) is respectively \(1,0,2\). Substitution in (*) produces the three displayed reflection character formulas, including the signs from the global vertex permutation.

**4. Rotations and invariants.** For a nonidentity rotation of order at least three, no nonempty admissible complement \(S\in\mathcal A_1\cup\cdots\cup\mathcal A_4\) is invariant: a rotation orbit of length at least three either has more than four vertices or itself contains a disconnected triple. The rotation half-turn, when it exists, fixes exactly \(n/2\) antipodal pairs among the admissible complements; each contributes \(-1\) to \(T_2\), and no other nonempty set is invariant. Therefore (*) gives the stated rotation traces (recovering [4] independently), and the identity trace is \(B_n\) by [2]. Finally, apply the averaging projector \((2n)^{-1}\sum_{g\in D_n}g\) and sum these rotation and reflection traces. For odd \(n\), the rotations sum to \(B_n+n-1\). For even \(n\), the signs of the \(n\) rotations sum to zero (the sign character maps \(r\) to \(-1\)); replacing the half-turn sign by its actual trace therefore gives a rotation-trace sum of \(B_n-1-(n/2)(-1)^{n/2}\). Combining the \(n\) reflection traces yields precisely the two invariant-dimension expressions above.

## Verification
Run `python3 verify.py` using Python 3's standard library from a directory containing this document and `verify.py`. The program enumerates **all admissible triples and quadruples** and checks absence of admissible five-sets for \(9\le n\le14\); it constructs the full dihedral permutations and verifies the signed relative-chain formula against the displayed character for **every group element** at \(9\le n\le22\) (434 actions); and it independently constructs the full ordinary three-cut complex at \(9\le n\le12\), checks its oriented Lefschetz character on all elements, and calculates all mod-two boundary ranks. Its recorded output in `verifier_output.txt` ends in `VERIFY_OK`. These are finite corroborations; the complete infinite-family proof is the argument in the preceding section.

## Relationship to prior work
Bayer et al. [1] introduced and investigated ordinary cut complexes, including symmetry questions for unpowered cycles. Chauhan, Shukla and Vinayak [2] proved shellability and the sphere multiplicity for the squared-cycle family. Chauhan and Shukla [3, Theorem 1.4] extended those nonequivariant results to higher cycle powers. The published cyclic-representation classification [4] already implies the **entire rotation part** of this theorem; the rotation formulas are cited context, not claimed as independently new. The title and mathematical statement of [4] were checked in full, and it explicitly leaves dihedral reflection characters open. Existing dihedral results for ordinary cut complexes of unpowered cycles [1,5], or for unrelated graph complexes, do not imply the two reflection-axis formulas here. The present contribution is exactly the dihedral extension, its explicit reflection signs and the resulting full rational representation and fixed-space dimensions.

## Limitations
The coefficients are rational and the vertex labels are those of the squared cycle. The result does not give integral-lattice representations, a dihedrally equivariant wedge decomposition, or statements for \(n<9\). The literature search is not a formal proof of novelty; equivalent unindexed or differently named work remains a risk. The finite verifier supports but does not replace the uniform proof.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, M. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675v1, first submitted 2023-04-26. https://arxiv.org/abs/2304.13675
2. P. Chauhan, S. Shukla and K. Vinayak, *Shellability of 3-Cut Complexes of Squared Cycle Graphs*, arXiv:2406.01979v1, first submitted 2024-06-04. https://arxiv.org/abs/2406.01979
3. P. Chauhan and S. Shukla, *Shellability of 3-cut complexes of powers of cycle graphs*, arXiv:2603.23155v1, first submitted 2026-03-24, Theorem 1.4. https://arxiv.org/abs/2603.23155
4. *Rational cyclic homology representations of three-cut complexes of cycle powers*, published mathematical research record, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-rational-cyclic-homology-representations-of-three-cut-complexes--dc0f17aad16d
5. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (2024), Section 6.2. https://arxiv.org/abs/2407.08158
