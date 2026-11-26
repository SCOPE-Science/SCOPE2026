# The characteristic-two symmetric top cycle for four particles on a double-star tree

## Finding
Let \(D_{a,b}\) be the tree formed by joining two hubs with \(a\) and \(b\) pendant leaves, respectively, where \(a,b\ge 2\). Let \(B_n(D_{a,b})\) be the space of \(n\) distinct **unlabelled** particles in its geometric realization. Let \(P_a=\mathbb Z^a\) denote the integral permutation lattice on the left leaves and similarly \(P_b\) on the right.

**Theorem.** The first nonzero second homology occurs for four particles:
\[
H_2(B_n(D_{a,b});\mathbb Z)=0\quad (0\le n\le3),\qquad
H_2(B_4(D_{a,b});\mathbb Z)\cong
\bigwedge^2P_a\otimes_{\mathbb Z}\bigwedge^2P_b.
\]
The latter identification is integral and equivariant for the leaf-permutation subgroup \(S_a\times S_b\); its free rank is \(\binom a2\binom b2\). When \(a=b\), exchanging the two hubs acts on the displayed tensor product by **minus interchange of factors**.

For every field \(k\), let \(G=\operatorname{Aut}(D_{a,b})\), which is \(S_a\times S_b\) when \(a\ne b\) and \((S_a\times S_a)\rtimes C_2\) when \(a=b\). Then
\[
\dim_k H_2(B_4(D_{a,b});k)^G=
\begin{cases}
1,&\operatorname{char}k=2,\\
0,&\operatorname{char}k\ne2.
\end{cases}
\]
In particular the unique nonzero \(G\)-fixed mod-two class **does not lift to a fixed integral or rational class**.

## Assumptions and scope
All graphs are finite one-dimensional CW complexes, with no particles allowed to coincide. The two hubs are adjacent and the leaf sets are distinguished for the initial lattice description; the hub-exchanging symmetry is included when the sets have equal cardinality. No statement concerns ordered particles, higher weights, a quotient space's integral homology, or the full homology ring.

## Proof
We use the reduced Świątkowski chain model, whose homology naturally agrees with that of unordered graph configurations [ADCK, Theorem 4.5, Proposition 4.9]. It is equivariant under graph automorphisms. A leaf contributes only its empty factor. Write \(y\) for the central edge and \(x_i,z_j\) for the respective leaf-edge variables. At the left hub put \(A_i=h_i-h_y\), and at the right put \(B_j=k_j-k_y\). Let
\[
u_i=x_i-y,\qquad v_j=z_j-y,
\qquad R=\mathbb Z[y,u_1,\ldots,u_a,v_1,\ldots,v_b].
\]
Replacing \(x_i,z_j\) by \(u_i,v_j\) is an invertible integral linear change of polynomial variables. The reduced model is the length-two Koszul-type complex with generators \(1,A_i,B_j,A_iB_j\), homological degrees \(0,1,1,2\), weights \(0,1,1,2\), and differential
\[
\partial A_i=u_i,\quad \partial B_j=v_j,\quad
\partial(A_iB_j)=u_iB_j-v_jA_i.
\]
Polynomial variables have homological degree zero and weight one. There is no degree-three group, so \(H_2\) is exactly the kernel of this differential.

A degree-two chain of weight \(n\) is uniquely \(\sum_{i,j} F_{ij}A_iB_j\), where each \(F_{ij}\) is homogeneous of polynomial degree \(n-2\). The cycle equations, coefficient by coefficient, are
\[
\sum_i u_iF_{ij}=0\ (\text{each }j),\qquad
\sum_j v_jF_{ij}=0\ (\text{each }i).
\]
Separate polynomial components by degree in the \(u\)-variables and in the \(v\)-variables. The first equations force the component with \(u\)-degree zero to vanish, since distinct \(u_i\) are algebraically independent; the second equations similarly force zero \(v\)-degree components to vanish. Therefore a nonzero top cycle requires polynomial degree at least two; this proves vanishing for \(n<4\).

At weight four the coefficients must be bilinear in the two independent sets of variables, with no \(y\)-factor:
\[
F_{ij}=\sum_{k=1}^{a}\sum_{l=1}^{b}c_{ij;kl}u_kv_l.
\]
Equating the coefficients of the independent monomials \(u_i u_k v_l\) and \(u_kv_jv_l\) in the cycle equations gives \(c_{ij;kl}=-c_{kj;il}\) and \(c_{ij;kl}=-c_{il;kj}\), respectively, including zero diagonal coefficients. Thus the free integral coefficient array is alternating in the two left indices and independently alternating in the two right indices. For every \(i<k\) and \(j<l\), an explicit basis cycle is
\[
Z_{ik;jl}=(u_i A_k-u_k A_i)(v_j B_l-v_l B_j).
\]
These \(\binom a2\binom b2\) cycles are independent by their unique coefficient arrays, and every degree-two four-particle cycle is their integer combination. Identifying \(Z_{ik;jl}\) with \((e_i\wedge e_k)\otimes(f_j\wedge f_l)\) proves the integral lattice formula. Leaf permutations act by the ordinary signed exterior-square permutations. Exchanging the hubs reverses the order of the two degree-one factors and consequently introduces the Koszul sign \(-1\), proving the factor-interchange action.

The same coefficient elimination works over any field, including characteristic two, so the invariant calculation can be carried out on this explicit basis. Over characteristic two, all signs disappear and \(G\) is transitive on the basis vectors \(Z_{ik;jl}\) up to sign. The sum of all basis vectors is a nonzero, fixed class, and transitivity forces every fixed vector to be a scalar multiple. A hub swap fixes this sum as well. Over a field of characteristic different from two, for any chosen basis vector a transposition of its two left-leaf indices acts by \(-1\) on that exact coordinate, and no other coordinate maps to it; hence its coefficient in any fixed vector must be zero. This holds for every coordinate. Therefore there are no fixed vectors in other characteristics or integrally. The coefficient-elimination argument works directly in each coefficient field because the reduced complex has no chains in degree three; no universal-coefficient or torsion inference is required. This completes the proof.

## Verification
The standalone `verify.py` constructs the full degree-two boundary matrices of the reduced complex in weights two through four, for \((a,b)=(2,2),(2,3),(3,3),(3,4)\), and performs exact modular elimination in characteristics two and five. It independently constructs all adjacent-leaf-transposition matrices (and the hub swap when applicable), calculates their fixed-space dimensions, and checks the predicted ranks. Its output is supplied in `verify.out`; it ends with `VERIFY_OK`. The finite tests support but do not replace the all-parameter proof above.

## Relationship to prior work
The reduced Świątkowski model and its naturality are established in An–Drummond-Cole–Knudsen [ADCK], whose Proposition 5.22 supplies a general bivalent-vertex cutting formula and hence strongly anticipates the **nonequivariant rank** in the present family. An–Knudsen [AK] establishes general generation of second homology of planar graph configuration spaces by toric and theta classes; it does not identify the specific natural integral leaf-permutation module or the characteristic-two fixed class. Farley–Sabalka [FS] establishes fundamental discrete-Morse and graph-braid facts for trees. The asserted refinement here is the explicit natural integral module and the universal characteristic-two-versus-other-characteristics invariant-class dichotomy, not the underlying chain model or general generation by tori.

## Limitations
The homology identification is proved only at weight four (and vanishing below four). This theorem does not establish the homology of the orbit space, whose integral chains are not given by naive group coinvariants. The result is a deduction from established computational machinery; an equivalent explicit equivariant computation elsewhere could supersede its novelty, and independent verification has not been performed.

## References
- [FS] Daniel Farley and Lucas Sabalka, *Discrete Morse theory and graph braid groups*, first public arXiv submission 25 October 2004, arXiv:math/0410539; *Algebraic & Geometric Topology* 5 (2005), 1075–1109.
- [ADCK] Byung Hee An, Gabriel Drummond-Cole, and Ben Knudsen, *Subdivisional spaces and graph braid groups*, arXiv:1708.02351, §§4.2, 4.5, 5.1, 5.4; especially Theorem 4.5 and Proposition 5.22.
- [AK] Byung Hee An and Ben Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371, Theorem 1.1 and §§2–3.
