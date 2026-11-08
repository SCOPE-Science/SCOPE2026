# Integral five-cube quotient lattice in dodecahedral independence homology

## Finding
Let \(D=GP(10,2)\) be the 20-vertex dodecahedral graph and let \(X=\operatorname{Ind}(D)\) be its ordinary independence complex. Let \(\Omega\) be the set of five maximum independent eight-vertex subsets of \(D\) (geometrically, the five inscribed cubes). The graph automorphism group is \(G\cong A_5\times C_2\). Its rotation subgroup \(A_5\) acts on \(\Omega\) by even permutations, while the central inversion \(z\) fixes every member of \(\Omega\). Let \(\varepsilon:G\to\{\pm1\}\) be trivial on rotations and satisfy \(\varepsilon(z)=-1\).

**Integral representation theorem.** As integral \(G\)-modules,
\[
\widetilde H_5(X;\mathbb Z)\cong
\varepsilon\otimes_{\mathbb Z}
\left(\mathbb Z[\Omega]/\mathbb Z\sum_{\omega\in\Omega}\omega\right).
\]
All other reduced integral homology groups vanish. In particular \(X\simeq\bigvee^4 S^5\), although that nonequivariant homotopy classification is prior work. The quotient above is the **permutation quotient lattice**, not the augmentation sublattice \(\ker(\mathbb Z[\Omega]\to\mathbb Z)\). They become isomorphic over \(\mathbb Q\), but the former has one-dimensional mod-five rotation coinvariants while the latter has zero-dimensional mod-five rotation coinvariants.

The complete rational character on the rotation subgroup takes values \(4,0,1,-1,-1\) on the five \(A_5\)-classes of respective orders \(1,2,3,5,5\); multiplication by \(z\) reverses every trace. The central inversion acts by exactly \(-I\) on **integral** fifth homology. Neither the rotation subgroup nor the full group fixes a nonzero fifth-homology class over \(\mathbb Q\).

## Assumptions and scope
The vertices of \(D\) are \(u_i,v_i\), where \(i\in\mathbb Z/10\mathbb Z\), with precisely the edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\), using indices modulo ten. The vertex ordering for the exact certificate is \(u_0,\ldots,u_9,v_0,\ldots,v_9\). An independent set is a subset containing no graph edge; all subsets, including the empty subset, are considered when forming the augmented chain complex. All homology uses integral coefficients except where explicitly indicated. The symmetry group acts by permuting vertices and the induced signed action on oriented simplices. The theorem is about the full **graph automorphism** action on ordinary simplicial homology, not an equivariant homotopy equivalence.

## Proof

**1. A complete integral Morse model.** An exhaustive recursion using the displayed edge definition produces precisely \(5828\) independent sets, including the empty set. By cardinality \(0,1,\ldots,8\), the counts are \(1,20,160,660,1510,1912,1240,320,5\). For each vertex in the specified order, pair still-unmatched faces \(S\) and \(S\cup\{v\}\) when both are independent and available. The matching has \(2912\) pairs on the augmented face poset and exactly four unpaired size-six faces:
\[
\{3,8,10,11,15,16\},\quad
\{4,9,11,12,16,17\},\quad
\{2,7,10,14,15,19\},\quad
\{1,6,13,14,18,19\}.
\]
The verifier exhaustively constructs all \(27640\) codimension-one Hasse covers, reverses every matched cover and proves that the resulting directed graph is acyclic. Omitting the empty face and its pair gives one critical vertex and four critical five-simplices and again an acyclic matching. Forman's discrete Morse theorem therefore gives a CW complex with one zero-cell and four five-cells, proving the claimed homotopy type and torsion-free integral homology. This is a *finite exhaustive certificate*, not an extrapolation to a graph family.

**2. Integral bases and the exact group action.** Let \(c_1,\ldots,c_4\) denote the four critical oriented five-simplices in the displayed order. For each matched lower five-face \(\tau\) paired upward to \(\sigma\), define a projection recursively using the integral signed boundary:
\[
P(\tau)=-[\tau:\sigma]^{-1}\sum_{\substack{\rho\subset\sigma\\\rho\ne\tau,\ |\rho|=|\tau|}}[\rho:\sigma]P(\rho).
\]
Set \(P(c_i)=e_i\) and \(P(\rho)=0\) for a five-face paired downward. All incidence coefficients \([\rho:\sigma]\) are \(\pm1\). Acyclicity makes the recursions terminate. The independent calculation checks \(P\partial=0\) on every size-seven face. To lift a critical five-face to an actual integral cycle, iteratively cancel its boundary coefficients along the matching, in a topological order of the corresponding gradient graph; the resulting cycles \(Z_i\) have respectively \(223,251,189,96\) nonzero oriented simplices, all coefficients \(\pm1\), and satisfy \(P(Z_i)=e_i\). Thus \(Z_1,\ldots,Z_4\) are an integral basis for homology. For each of the \(120\) automorphisms, the integral matrix on this basis is calculated as \(P\circ g\circ Z\). The verifier checks all \(14400\) multiplication identities and compares the trace of every matrix to an independent signed-simplicial Lefschetz sum.

**3. The canonical five-cube lattice.** The five independent size-eight sets are exactly \(\Omega\); every automorphism permutes them. Direct finite group computation identifies the derived subgroup of order \(60\) with the rotations \(A_5\), and the unique nontrivial central element \(z\) with antipodal inversion. The full matrices establish \(z_*=-I\) over \(\mathbb Z\), and show that \(z\) fixes each of the five octets.

Choose the first octet in increasing bit-mask order. Its rotational stabilizer has order \(12\), and the sublattice it fixes in homology is generated by the primitive class \(Z_4\). The orbit of this class indexed by the five octets has the following columns in the basis \(Z_1,\ldots,Z_4\):
\[
B=\begin{pmatrix}
0&0&1&0&-1\\
0&0&0&1&-1\\
0&1&-1&0&0\\
1&-1&0&0&0
\end{pmatrix}.
\]
The columns sum to zero, while the determinant of its first four columns is \(-1\). Hence the orbit homomorphism \(\mathbb Z[\Omega]\to\widetilde H_5(X;\mathbb Z)\) is surjective with **exact** kernel the constant line \(\mathbb Z\sum_\Omega\omega\). It intertwines the rotation action by construction; the sign twist makes the central involution equivariant as well. This proves the integral module isomorphism, including its normalization and primitivity.

**4. Why the integral distinction matters.** Let \(Q=\mathbb Z[\Omega]/\mathbb Z\sum\omega\) and \(A=\ker(\mathbb Z[\Omega]\xrightarrow{\sum}\mathbb Z)\). Both rationalizations are the four-dimensional standard representation restricted from \(S_5\) to \(A_5\), but over \(\mathbb F_5\) the rotational coinvariants have dimensions \(\dim(Q\otimes\mathbb F_5)_{A_5}=1\) and \(\dim(A\otimes\mathbb F_5)_{A_5}=0\). These numbers are obtained from the four-by-four integral permutation matrices and exact modular Gaussian elimination in the verifier. Therefore the two integral modules are not isomorphic; rational character information alone could not establish the theorem.

## Verification
Run `python3 verify_dodecahedral_lattice.py` with Python 3, NetworkX 3.x and SymPy 1.x. The script independently constructs all faces and all graph automorphisms, exhaustively verifies the full acyclic matching, generates explicit integral cycles and projections, checks the group action, tests all signed Lefschetz traces, computes the index-one five-orbit lattice map, and compares mod-five coinvariants. Its recorded output is in `verification_output.txt`. All calculations are over integers or exact finite fields; no randomization or floating-point tolerance is used.

## Relationship to prior work
Barmak's 2010 investigation of star clusters develops independence-complex homotopy methods and proves suspension statements for triangle-free graphs. Berghoff's 2020 work provides homological spectral-sequence methods for independence complexes, with examples concerning other graph families. A previously published computation for \(GP(10,2)\) establishes the nonequivariant wedge of four five-spheres and even uses a corresponding acyclic matching. None of these supplied statements identifies the full **integral** automorphism module with the quotient of the five-cube permutation lattice. In particular, a bare wedge decomposition gives only an abstract rank-four group and does not determine its integral action. Existing results for dodecahedral Rips and neighborhood complexes concern different simplicial complexes; their homology modules cannot be substituted for that of \(\operatorname{Ind}(D)\). The classical compound of five cubes gives the natural five-set but does not by itself supply any homology action.

## Limitations
The certificate is exhaustive and exact for this one 20-vertex graph; the general assertion is not extended to other generalized Petersen graphs. The proof does not establish an equivariant wedge decomposition, an equivariant homotopy type, or preferred geometric representatives for all five cube-indexed classes independent of orientation choices. Publication priority may still be affected by unindexed literature or equivalent constructions not found in the inspected sources. No independent mathematical audit has been performed.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first public 2010-07-02, https://arxiv.org/abs/1007.0418.
2. M. Berghoff, *On the homology of independence complexes*, arXiv:2008.06267, first public 2020-08-14, https://arxiv.org/abs/2008.06267.
3. *The dodecahedral independence complex is a wedge of four 5-spheres*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-dodecahedral-independence-complex-is-a-wedge-of-four-5-spher--ba0161fd495f (nonequivariant statement).
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
5. H. S. M. Coxeter, *Regular Polytopes*, third edition (1973), Section on regular compounds (five inscribed cubes).
