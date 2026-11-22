# Integral source-rotation homology lattices and mod-three cohomology of complete-graph coloring complexes

## Finding

For an integer \(n\ge 3\), let \(X_n=\operatorname{Hom}(K_3,K_n)\) denote the regular polyhedral graph-homomorphism complex. Its cells are ordered triples \((A,B,C)\) of pairwise disjoint nonempty subsets of \(\{1,\dots,n\}\), with cell \(\Delta(A)\times\Delta(B)\times\Delta(C)\). Let \(G=C_3=\langle g\rangle\) act by cyclically permuting the **three source coordinates**, and let \(R=\mathbb Z[G]\) and \(I=\ker(\varepsilon:R\to\mathbb Z)\), with \(\mathbb Z\) a trivial \(G\)-module. Put \(d=n-3\).

**Integral source-rotation theorem.** As an integral \(R\)-lattice,
\[
\widetilde H_d(X_n;\mathbb Z)\cong
\begin{cases}
I\oplus R^{(2^n-5)/3},&n\text{ odd},\\
\mathbb Z\oplus R^{(2^n-4)/3},&n\text{ even}.
\end{cases}
\]
The decomposition is an abstract module isomorphism; no canonical choice of summand generators is asserted. In characteristic three, the generator acts with exactly one Jordan block of size two when \(n\) is odd, or exactly one block of size one when \(n\) is even; all other blocks have size three.

For \(n\ge5\), let \(Y_n=|X_n|/C_3\). Its fundamental group is \(C_3\). Set
\[
\beta_n=\frac{2^n-3-2(-1)^d}{3},\qquad
k_n=\begin{cases}(2^n-5)/3,&n\text{ odd},\\(2^n-4)/3,&n\text{ even}.
\end{cases}
\]
Then its complete integral homology is
\[
H_i(Y_n;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z/3\mathbb Z,&0<i<d\text{ and }i\text{ odd},\\
\mathbb Z^{\beta_n},&i=d,\\
0,&\text{otherwise}.
\end{cases}
\]

Write \(a\) and \(b\) for the standard generators of \(H^*(BC_3;\mathbb F_3)=\Lambda(a)\otimes\mathbb F_3[b]\), with \(|a|=1\), \(|b|=2\), and \(b=\beta_{\mathrm{Bock}}(a)\). The mod-three cup-product ring has the form
\[
H^*(Y_n;\mathbb F_3)\cong
\bigl(\Lambda(a)\otimes\mathbb F_3[b]\bigr)_{\le d}\ \oplus\ V_d,
\quad \dim_{\mathbb F_3}V_d=k_n,
\]
where the subscript means quotient by every homogeneous term of degree greater than \(d\). The extra vector space \(V_d\) is concentrated in degree \(d\); positive-degree elements annihilate it, and products within it vanish. Consequently, the mod-three cup-length is exactly \(\lceil d/2\rceil\). This specifies the ordinary orbit space, not a fixed-point space or a homotopy quotient of a nonfree action.

## Assumptions and scope

All graphs are finite simple complete graphs. Every source-coordinate set is nonempty, and distinct coordinates carry disjoint target-label sets. The acting group is the order-three subgroup of source permutations, not a cyclic subgroup of target-color permutations. The integral lattice statement applies for all \(n\ge3\), including reduced degree-zero homology for \(n=3\). The quotient homotopy, integral homology and cohomology claims apply only for \(n\ge5\). No unstable higher-homotopy groups of the quotient are classified.

## Proof

**1. Classical connectivity and cell Euler characteristic.** The Babson–Kozlov wedge theorem, in its complete-graph case, gives
\[
X_n\simeq\bigvee^{2^n-3}S^{n-3}.
\]
The sphere count follows also from its cell enumeration: \(\operatorname{Hom}(K_3,K_n)\) has one \((s-3)\)-cell per ordered three-block partition of any selected \(s\)-subset of the \(n\) target labels. Thus the nonreduced Euler characteristic is \(1+(-1)^d(2^n-3)\). In particular, for \(n\ge5\), \(X_n\) is simply connected and \((d-1)\)-connected.

**2. Freeness of source rotation.** Cyclic permutation sends \((A,B,C)\) to \((B,C,A)\). A cell (and its relative interior) cannot be stabilized by a nonidentity rotation: this would force \(A=B=C\), contradicting disjointness and nonemptiness. Since relative interiors partition the geometric complex, the action is free. The cellular chain groups \(C_j(X_n;\mathbb Z)\) are consequently finite-rank free \(R\)-modules, including the augmentation in degree zero.

**3. Integral module.** As the reduced integral homology of \(X_n\) vanishes except in degree \(d\), its augmented cellular chain complex furnishes an exact sequence of \(R\)-modules
\[
0\to M_n\to C_d\to C_{d-1}\to\cdots\to C_0\to\mathbb Z\to0,
\quad M_n=\widetilde H_d(X_n;\mathbb Z).
\]
By generalized Schanuel's lemma, \(M_n\) is stably isomorphic to the \((d+1)\)-st syzygy of the trivial \(R\)-module. The standard two-periodic free resolution of \(\mathbb Z\) has alternating differentials \(g-1\) and \(N=1+g+g^2\), hence its odd syzygies are \(I\) and its even syzygies are \(\mathbb Z\). Thus \(M_n\) is stably \(I\) for even \(d\) and stably \(\mathbb Z\) for odd \(d\).

For clarity, the necessary integral-representation fact is that every finitely generated \(\mathbb Z\)-free \(R\)-module is a direct sum of copies of \(\mathbb Z\), \(I\), and \(R\). It follows from the pullback description \(R\subset\mathbb Z\oplus\mathbb Z[\zeta_3]\), glued over \(\mathbb F_3\), because \(\mathbb Z[\zeta_3]\) is Euclidean and the gluing matrices reduce to identity-and-zero blocks. Equivalently, these are the three integral indecomposable \(C_3\)-lattices (see the references). Modulo three, \(g\) has respectively a size-one, size-two or size-three unipotent Jordan block on these modules. Schanuel stable isomorphism, reduced modulo three, fixes the sizes one and two: exactly one size-two block and no size-one block for even \(d\), and the reverse for odd \(d\). The rank \(\operatorname{rank}_{\mathbb Z}M_n=2^n-3\) then forces the displayed number of regular size-three blocks. Because the three integral module types exhaust the possibilities, this also proves the integral decomposition, not merely its mod-three reduction or rational character.

**4. Quotient fundamental group and homology.** For \(n\ge5\) the free covering \(X_n\to Y_n\) is universal, giving \(\pi_1(Y_n)=C_3\). The classifying map \(c:Y_n\to BC_3\) has \((d-1)\)-connected homotopy fiber \(X_n\). Its homology Serre spectral sequence therefore identifies \(H_i(Y_n;\mathbb Z)\) with \(H_i(BC_3;\mathbb Z)\) for \(i<d\): these groups are \(\mathbb Z/3\) in positive odd degrees and zero in positive even degrees. As \(Y_n\) is a \(d\)-dimensional CW complex, \(H_d(Y_n;\mathbb Z)\) is a free subgroup of its top cellular chains. No lower homology group has positive rational rank. Finally the free threefold cellular action gives
\[
\chi(Y_n)=\frac{1+(-1)^d(2^n-3)}{3}=1+(-1)^d\beta_n,
\]
which determines the displayed top rank and excludes all higher homology.

**5. Mod-three cohomology and cup-length.** The cohomological Serre spectral sequence of the same classifying map shows that \(c^*\) is an isomorphism in degrees below \(d\) and an injection in degree \(d\). In particular, the complete truncated polynomial-exterior algebra of \(BC_3\) survives with its products. The universal coefficient theorem and the integral homology calculation give
\[
\dim_{\mathbb F_3}H^d(Y_n;\mathbb F_3)=\begin{cases}\beta_n+1,&d\text{ even},\\\beta_n,&d\text{ odd},\end{cases}
\]
so the complement to the one-dimensional image of \(H^d(BC_3;\mathbb F_3)\) has dimension exactly \(k_n\). By dimensional reasons every positive-degree product involving this complement vanishes. The largest product of positive-degree classes is \(b^{d/2}\) when \(d\) is even, and \(ab^{(d-1)/2}\) when \(d\) is odd. Both are nonzero by injectivity of \(c^*\), giving cup-length \(\lceil d/2\rceil\); no longer product can have degree at most \(d\).

## Verification

Two standalone standard-library Python programs accompany this result. `verification/quotient_orbit_chain.py` independently enumerates the oriented ordinary quotient cells and computes modulo-three cellular boundary ranks for \(3\le n\le7\), including the small disconnected and graph cases. `verification/cyclic_lattice_jordan.py` constructs full labeled top-dimensional cellular boundaries and the chain-level cyclic rotation over \(\mathbb F_3\). For \(n=5,6,7\) it finds the predicted Jordan block counts \((0,1,9)\), \((1,0,20)\), and \((0,1,41)\), in block-size order one, two, three. These finite checks are independent tests of combinatorial signs and small instances, **not** proofs for all \(n\), nor independent human validation. The proof for arbitrary \(n\) is the topological and integral-representation argument above.

## Relationship to prior work

Babson and Kozlov's original complete-graph Hom theorem determines the nonequivariant sphere wedge. Earlier descriptions of the full two-sided rational symmetry character determine rational traces but not the displayed integral decomposition or its mod-three Jordan structure. Closely related calculations for **target-color** cyclic quotients act on different coordinates and do not determine the **source-coordinate** quotient here. The present contribution is the uniform integral rotation lattice and the complete modular cup-product algebra of its ordinary quotient. The underlying general tools—periodic resolutions, Schanuel's lemma, and group cohomology—are standard; no novelty is asserted for them.

## Limitations

The module isomorphisms are not accompanied by canonical geometric integral cycle bases. The quotient is not classified up to homotopy equivalence, except for its fundamental group and stated cohomological invariants. Full texts of several closely related indexed later records were unavailable; an equivalent unindexed or unpublished statement cannot be ruled out. The small-parameter programs do not certify the infinite-family theorem.

## References

- E. Babson and D. N. Kozlov, *Complexes of graph homomorphisms*, first public preprint 2003-10-05, arXiv:math/0310056, https://arxiv.org/abs/math/0310056.
- D. N. Kozlov, *Combinatorial Algebraic Topology*, Springer 2008, §§19.2.1, Theorem 19.10 and Proposition 19.11, https://webhomes.maths.ed.ac.uk/~v1ranick/papers/kozlov.pdf.
- C. W. Curtis and I. Reiner, *Methods of Representation Theory*, Vol. I, Wiley 1981, §34B (integral cyclic-group lattices).
- K. S. Brown, *Cohomology of Groups*, Springer 1982, periodic resolutions and group cohomology.
- J. D. P. Evans, *Group algebras of metacyclic type*, doctoral thesis, UCL 2018, §§2.8 and 5.2 (three integral \(C_3\) lattice types), https://discovery.ucl.ac.uk/id/eprint/10043870/1/Thesis.pdf.
