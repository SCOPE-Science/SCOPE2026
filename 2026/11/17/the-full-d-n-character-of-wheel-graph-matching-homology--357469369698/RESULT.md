# The full \(D_n\) character of wheel-graph matching homology

## Finding
For each integer \(n\ge3\), let \(W_n=K_1\vee C_n\) be the wheel with one hub and \(n\) rim vertices, and let \(X_n=\mathcal M(W_n)\) be its **ordinary matching complex**. The natural rim rotation and reflection generate a dihedral group \(D_n\) acting simplicially on \(X_n\). Put \(d_n=\lfloor(n-1)/3\rfloor\). The only nonzero reduced rational homology of \(X_n\) is in degree \(d_n\); its known rank is
\[
 B_n=\begin{cases}2,&n\equiv0\pmod3,\\ n-1,&n\equiv1\pmod3,\\ n+1,&n\equiv2\pmod3.\end{cases}
\]
The contribution here is the **complete character** of this homology under \(D_n\), not this previously known rank or homotopy classification.

Define an integer six-periodic sequence by \(f_0=1\), \(f_1=0\), and \(f_j=f_{j-1}-f_{j-2}\) for \(j\ge2\); its repeating values are \((1,0,-1,-1,0,1)\). Set \(c_j=2\cos(\pi j/3)\) for every positive integer \(j\), so \(c_j\) is always an integer. Label the rim vertices \(v_i\), indexed modulo \(n\), and write \(r(v_i)=v_{i+1}\), \(s(v_i)=v_{-i}\), with both transformations fixing the hub. If \(\chi_n\) is the character of \(\widetilde H_{d_n}(X_n;\mathbb Q)\), then for \(0\le a<n\),
\[
\boxed{\chi_n(r^a)=\begin{cases}
B_n,&a=0,\\
(-1)^{d_n+1}c_{\gcd(n,a)},&1\le a<n,
\end{cases}}
\]
and **every reflection has the same trace**:
\[
\boxed{\chi_n(r^as)=\begin{cases}
0,&n\text{ odd},\\
0,&n\text{ even and }3\mid n,\\
(-1)^{n/2+1},&n\text{ even and }3\nmid n.
\end{cases}}
\]
In particular, the entire rational homology representation, not merely its Euler character or dimension, is determined. Its subspace invariant under all dihedral symmetries satisfies
\[
\boxed{\dim_{\mathbb Q}\widetilde H_{d_n}(X_n;\mathbb Q)^{D_n}=\begin{cases}
1,&n\equiv2,5,10,11\pmod{12},\\
0,&\text{otherwise}.
\end{cases}}
\]
Consequently the topological quotient \(|X_n|/D_n\) is reduced-rationally acyclic in the second case, and in the first case has one-dimensional reduced rational homology in degree \(d_n\) and none elsewhere. For \(n=3\), \(D_3\) means the specified rim-preserving group, not the larger full automorphism group of the tetrahedral wheel.

## Assumptions and scope
All graphs are finite and simple. The matching complex consists of edge sets without shared graph endpoints, including the empty face. The group acts on **oriented** simplicial chains by permuting matching edges, with the sign of the resulting permutation. Coefficients are rational for the representation and quotient claims. The previously established nonequivariant homotopy type is integral; no new integral representation decomposition is asserted. Here the wheel has exactly \(n+1\) graph vertices; this convention matters when comparing formulas in sources that use \(W_{n+1}\) for the same wheel.

## Proof
Let rim edges be \(e_i=\{v_i,v_{i+1}\}\) and hub spokes \(t_i=\{h,v_i\}\). Any matching contains at most one spoke. The subcomplex of matchings with no spokes is \(\operatorname{Ind}(C_n)\) on the \(n\) rim edges; matchings containing \(t_i\) consist of that spoke together with an independent subset of the path of \(n-2\) rim edges other than \(e_{i-1},e_i\). Thus there is an exact face-level decomposition
\[
 X_n=\operatorname{Ind}(C_n)\ \cup\ \bigcup_{i=0}^{n-1}\bigl(t_i*\operatorname{Ind}(P_{n-2})\bigr),
\]
where the cones meet only along their bases. This is an equality of complexes, not an equivariant wedge decomposition.

For any finite simplicial complex \(Y\) and simplicial symmetry \(g\), define the signed fixed-face sum
\[
 F_Y(g)=\sum_{\substack{\sigma\in Y\\g\sigma=\sigma}}(-1)^{|\sigma|}\operatorname{sgn}(g|_\sigma),
\]
including the empty face (contribution \(1\)). The reduced simplicial Lefschetz number of \(g\) is exactly \(-F_Y(g)\). By Vega's established wheel matching-complex homotopy theorem [1, Theorem 5.2], reduced homology is concentrated in degree \(d_n\), with rank \(B_n\). Consequently
\[
\chi_n(g)=(-1)^{d_n+1}F_{X_n}(g).
\]
There is no assumption here that fixed simplices are pointwise fixed: their orientation signs are essential.

The independence polynomial of the path \(P_j\) at \(-1\) obeys \(f_j=f_{j-1}-f_{j-2}\), because an independent subset either avoids or contains an endpoint; the initial values are \(1,0\). For the cycle, deleting one vertex and its closed neighborhood gives
\[
 I(C_j;-1)=f_{j-1}-f_{j-3}=2\cos(\pi j/3)=c_j,\qquad j\ge3.
\]
Extend this formula to orbit quotients on one or two vertices by \(c_1=1\) (only the empty invariant set is permitted) and \(c_2=-1\) (two mutually incompatible vertex orbits). These agree with the cosine formula.

For the identity the cone decomposition counts every spoke-containing matching once, hence
\[
 F_{X_n}(1)=c_n-nf_{n-2}.
\]
This yields \(\chi_n(1)=B_n\), as an independent normalization check. For a nonidentity rotation \(r^a\), no spoke is fixed, so a rotation-invariant matching contains none. Put \(b=\gcd(n,a)\). Each nonempty orbit of rim edges has size \(n/b\); its contribution to the signed fixed-face sum, when selected, is \((-1)^{n/b}\cdot(-1)^{n/b-1}=-1\). When \(b\ge2\), the selectable orbits therefore form independent sets of a \(b\)-cycle. When \(b=1\), the unique orbit contains adjacent edges and is forbidden. In both cases \(F_{X_n}(r^a)=c_b\), giving the rotation formula.

For reflections, put \(m=\lfloor n/2\rfloor\). A fixed single rim-edge orbit contributes \(-1\) to \(F\), and so does each selected two-edge orbit, since the transposition reverses its orientation. If the two members of an orbit are adjacent, that orbit cannot be selected. The permitted orbit-graph is therefore a path. In the following cases, all contributions from fixed spokes enter with a minus sign:

* If \(n=2m+1\), there is one fixed rim edge, one forbidden adjacent rim-edge orbit, and the permitted rim-orbit graph is \(P_m\). Exactly one spoke is fixed. Its remaining \(n-2=2m-1\) rim-edge path is reversed. The fixed-orbit sum for a reversed path of odd length \(2k+1\) is \(f_{k+1}\), so this spoke contributes \(-f_m\). Thus \(F=f_m-f_m=0\).
* If \(n=2m\) and the reflection axis fixes two rim edges, the permitted rim-orbit graph is \(P_{m+1}\), and no spoke is fixed. Thus \(F=f_{m+1}\).
* If \(n=2m\) and the reflection fixes no rim edge, there are two forbidden adjacent rim-edge orbits, leaving \(P_{m-2}\). Exactly two spokes are fixed; each has a reversed path of \(n-2=2m-2\) eligible rim edges. The signed sum of a reversed path of even length \(2k\) is \(f_{k-1}\), so \(F=f_{m-2}-2f_{m-2}=-f_{m-2}=f_{m+1}\).

The two reversed-path claims follow by taking orbits under reversal: odd paths give a path on \(k+1\) selectable orbits; even paths have an adjacent forbidden central pair and leave a path on \(k-1\) selectable orbits. Each selectable orbit, of size one or two, contributes weight \(-1\) with its permutation sign. These are exact bijections for all stated path lengths (including the empty quotient when \(k=1\)). Hence all even-rim reflection types have the same character. Using the six-periodicity of \(f_j\) and the definition of \(d_n\) simplifies \((-1)^{d_n+1}f_{n/2+1}\) to \(0\) when \(3\mid n\), and to \((-1)^{n/2+1}\) otherwise.

Finally, the multiplicity of the trivial \(D_n\)-representation is the character average. For rotations set \(S(n)=\sum_{a=0}^{n-1}c_{\gcd(n,a)}=\sum_{b\mid n}\varphi(n/b)c_b\). The arithmetic function \(c_b\) is multiplicative: on prime powers it equals \(-1\) for powers of \(2\), \(-2\) for powers of \(3\), and \(1\) for powers of any other prime. Consequently the divisor sum is multiplicative and satisfies
\[
 S(n)=\begin{cases}n,&\gcd(n,6)=1,\\0,&\gcd(n,6)>1.\end{cases}
\]
Indeed on powers of \(2\) and \(3\) the term \(\varphi(p^k)\) cancels the contributions of all smaller powers, while at other prime powers the sum of totients is \(p^k\). Substituting the identity contribution \(B_n\) and the nonidentity rotation contributions gives cyclic invariant dimensions \(0,0,1,0,1,2\) in residue classes \(n=0,1,2,3,4,5\pmod6\). All reflections have common trace \(\eta_n\) given above. The full dihedral invariant dimension is \((u_n+\eta_n)/2\), which is precisely the mod-twelve formula. Over \(\mathbb Q\), finite-group averaging (or transfer after barycentric subdivision) identifies homology of the orbit space with the invariant homology, giving the quotient statement.

## Verification
The attached dependency-free Python verifier `verify_wheel.py` builds the wheel edges directly and enumerates every matching. For \(3\le n\le16\) it independently computes the signed action on every fixed oriented face for all \(2n\) dihedral elements; 42,933 faces over these cases and 266 element calculations were checked against the formula. It separately checks the signed independent-set and path-reversal formulas for lengths \(1\) through \(18\), computes reduced simplicial mod-two homology by exact boundary ranks for \(3\le n\le11\), and tests both cyclic and dihedral invariant formulas for \(3\le n\le300\). The executed output is embedded as `verification_output.txt` and ends in `VERIFY_OK`. These finite checks are corroboration; the arguments above prove all parameter values.

## Relationship to prior work
Vega [1] already proves the full **nonequivariant homotopy type** of wheel matching complexes, including the one-degree homology concentration and sphere multiplicities used here. Kozlov's independence-complex computation for cycles, as cited in [1, Proposition 5.1], supplies an established input. Neither statement gives the action of reflections on oriented matching chains or its mod-twelve invariant criterion. The fully inspected published result [2] gives the complete dihedral character of **cycle** matching complexes (including its three reflection-orbit path cases), accounting for the rim-only contribution, but it does not address the additional fixed-spoke contributions of a **wheel**. Its quotient congruence classes are \(1,11\pmod{12}\), rather than the wheel classes \(2,5,10,11\pmod{12}\). The fully inspected published result [3] treats the **discrete-Morse complex** of wheels, whose vertices are directed vertex-edge incidences rather than graph edges, not the ordinary matching complex. Direct searches for wheel ordinary-matching dihedral characters, alternative parametrizations and exact quotient invariants did not identify an equivalently strong published statement; this is evidence-based originality assessment, not a proof of uniqueness.

## Limitations
The theorem concerns the natural rim dihedral group. The full automorphism group is larger only in the smallest tetrahedral case, where no full-group statement is made. No integral equivariant lattice structure, Steenrod operations or equivariant homotopy decomposition is asserted. The included verifier checks finite samples only. A matching-result in inaccessible or unindexed literature could supersede the originality assessment. The full relevant scientific statements and proofs of [2] and [3] were inspected and distinguish their objects. An equivalent wheel matching character in other unindexed or inaccessible work remains possible.

## References
[1] J. Vega, *2-Matching Complexes*, arXiv:1909.10406, first publicly submitted 2019-09-23; revised 2021-01-28. In particular, Theorem 5.2 and its proof in the open HTML version: https://arxiv.org/html/1909.10406v2 .

[2] *Dihedral homology characters and quotient congruences for cycle matching complexes*, public research result, identifier `2026/10/11/SCOPE-dihedral-homology-characters-and-quotient-congruences-for-cycle--6d9fbe47cba0`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-dihedral-homology-characters-and-quotient-congruences-for-cycle--6d9fbe47cba0 .

[3] *Dihedral top homology of wheel discrete-Morse complexes*, public research result, identifier `2026/10/11/SCOPE-dihedral-top-homology-of-wheel-discrete-morse-complexes--07726f70cc8e`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-dihedral-top-homology-of-wheel-discrete-morse-complexes--07726f70cc8e .
