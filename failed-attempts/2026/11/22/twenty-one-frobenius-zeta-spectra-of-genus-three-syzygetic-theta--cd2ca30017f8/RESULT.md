# Twenty-one Frobenius zeta spectra of genus-three syzygetic theta tetrads

## Finding
Let \(C/\mathbb F_q\) be any smooth hyperelliptic curve of genus three over an odd finite field. Denote by \(\mathcal T_C\) the reduced finite étale scheme of *syzygetic tetrads*: unordered four-element sets of distinct odd theta characteristics whose tensor product is \(K_C^{\otimes2}\). This scheme has \(315\) geometric points.

**Theorem.** The Frobenius action on \(\mathcal T_C\) is determined by the cycle partition of its eight geometric Weierstrass branch points. Among the \(22\) possible abstract partitions of eight, the resulting zeta functions number exactly \(21\). The only collision is between the partitions \((1,1,1,1,4)\) and \((2,2,4)\): both give the cycle profile \(1^7 2^{10}4^{72}\), hence
\[
Z(\mathcal T_C,T)=\frac{1}{(1-T)^7(1-T^2)^{10}(1-T^4)^{72}}.
\]
This collision remains even when the two geometrically distinguished, Frobenius-invariant subfamilies of sizes \(105\) and \(210\) are observed separately.

If \(N_n=\#\mathcal T_C(\mathbb F_{q^n})\), the vector \((N_1,N_2,N_3,N_4,N_5)\) determines the entire zeta function of \(\mathcal T_C\). The cutoff five is sharp: the partitions \((1,7)\) and \((3,5)\) have \(N_1=N_2=N_3=N_4=0\) but have \(N_5=0\) and \(15\), respectively. Both kinds of examples exist over every odd finite field. The result reconstructs the tetrad zeta function, **not always the branch partition**.

## Assumptions and scope
The ground field \(\mathbb F_q\) has odd characteristic, so \(J_C[2]\) and the odd-theta and tetrad schemes are étale. Let \(B\) denote the reduced eight-point Weierstrass branch scheme of the hyperelliptic double cover \(C\to\mathbb P^1\). We count geometric theta-characteristic isomorphism classes and Frobenius-stable *sets* of four such classes; stability does not require each member to descend.

The \(22\) cases are the conjugacy classes of permutations of eight objects. Not every class is necessarily realizable over a given small \(\mathbb F_q\), because \(\mathbb P^1(\mathbb F_q)\) may have too few points for a given number of rational branches. The two specific collisions and the sharpness examples below are realized as claimed. The zeta function is the finite-scheme generating series \(\exp(\sum_{n\ge1}N_n T^n/n)\).

## Proof
**1. Odd theta characteristics and the symplectic model.** Write \(B(\overline{\mathbb F}_q)=\{W_1,\dots,W_8\}\). The \(28\) odd theta characteristics are represented uniquely by \(\mathcal O_C(W_i+W_j)\), indexed by the two-element subsets of \(B\). The Jacobian's geometric two-torsion is the six-dimensional symplectic vector space
\[
J_C[2](\overline{\mathbb F}_q)\cong\{S\subseteq B:|S|\text{ even}\}/(S\sim B\setminus S),
\]
with addition given by symmetric difference and Weil pairing \((-1)^{|S\cap T|}\). Difference of odd theta characteristics indexed by edges \(e,f\) is the class of \(e\mathbin\triangle f\). This description is Frobenius equivariant, since the geometric Weierstrass points form a Galois-stable set.

A syzygetic tetrad corresponds to a four-element affine plane in the torsor of odd theta characteristics. Equivalently, for four distinct two-subsets \(e_1,e_2,e_3,e_4\), its defining tensor-product relation is
\[
e_1\mathbin\triangle e_2\mathbin\triangle e_3\mathbin\triangle e_4\in\{\varnothing,B\}.
\]
The second possibility uses the identity that the full ramification divisor has class \(K_C^{\otimes2}\), whereas the first is immediate from the degree-two hyperelliptic pencil. Equivalently, these are precisely the odd affine planes whose difference space is a two-dimensional totally isotropic subspace of \(J_C[2]\).

**2. The two graphical kinds are exhaustive.** Regard each two-subset as an edge of the complete graph on the eight branch labels. Four distinct edges with empty symmetric difference form a simple four-cycle: every vertex must have even degree, and four edges permit only that simple cycle. Four edges with full symmetric difference form a perfect matching: each of the eight vertices must have odd degree, so it occurs once. Thus the two kinds have cardinalities
\[
3\binom84=210,\qquad (8-1)!!=105,
\]
respectively, giving \(315\) total. Both are preserved by every permutation of the branch labels. The equal total is also checked independently by counting isotropic planes: \(63\) nonzero vectors each have \(30\) linearly independent orthogonal nonzero partners; division by the six ordered bases of a two-plane gives \(63\cdot30/6=315\).

**3. Exact finite classification.** For each partition \(\lambda\vdash8\), let \(\sigma_\lambda\) be the product of disjoint cycles of the specified lengths. Apply \(\sigma_\lambda\) to the \(315\) edge quadruples above and traverse the resulting permutation cycles. Their lengths and multiplicities are listed, without sampling, in `tetrad_frobenius_22.csv`, along with the independent profiles of the two kinds and the first five fixed-point counts. This is an exhaustive proof because every Frobenius permutation of eight geometric branch points is conjugate to exactly one of the \(22\) representatives, and conjugate permutations act with identical cycles on the tetrad set.

The standalone Python 3 checker `verify_tetrads.py` enumerates all \(\binom{28}{4}\) possible four-edge sets and selects precisely those satisfying the symmetric-difference test. Independently it enumerates the \(315\) totally isotropic two-planes of \(J_C[2]\) in the even-subset model, constructs the unique bijection from tetrads to planes, and proves equivariance for each of the \(22\) permutations. It directly checks the fixed points of every permutation power up to its order, not merely the orbit totals. Comparing all computed profiles yields exactly one collision, stated above; the same collision persists on both subfamilies, with respective profiles \(1^3 2^3 4^{24}\) and \(1^4 2^7 4^{48}\).

**4. Sharp recovery and witnesses.** The \(22\)-row table has \(21\) distinct full profiles. The five-count prefixes also have \(21\) distinct values, so a five-count prefix specifies exactly one zeta function. The four-count prefixes have only \(18\) different values, and in particular the two types \((1,7)\), \((3,5)\) yield no fixed tetrads over extensions of degrees at most four. The former has tetrad profile \(7^{45}\), the latter \(5^3 15^{20}\), proving the sharp separation at degree five. For any odd \(q\), irreducible polynomials of every positive degree exist over \(\mathbb F_q\); products of distinct monic irreducibles of degrees \(1,7\), or of degrees \(3,5\), therefore give smooth genus-three hyperelliptic curves realizing these two cases.

To realize the **permanent** ambiguity in characteristic three, let
\[
\begin{aligned}
C_1 &: y^2=x(x-1)(x+1)(x^4+x+2),\\
C_2 &: y^2=(x^2+1)(x^2+x+2)(x^4+x+2)
\end{aligned}
\qquad\text{over }\mathbb F_3.
\]
The quartic \(x^4+x+2\) and both displayed quadratics are irreducible over \(\mathbb F_3\). The former model has polynomial degree seven, with the rational ramification point at infinity, giving partition \((1,1,1,1,4)\); the latter gives \((2,2,4)\). The standalone checker verifies the irreducibility by exhaustive monic trial division. Their tetrad zeta functions coincide even though their rational odd-theta counts are six and two.

## Verification
Run `python3 verify_tetrads.py` in the directory containing the two named artifacts; it regenerates `tetrad_frobenius_22.csv` and terminates with

`315_TETRADS_105_MATCHINGS_210_FOUR_CYCLES_22_PARTITIONS_21_SPECTRA_VERIFIED`

`FIVE_EXTENSION_RECOVERY_SHARP_ONE_COLLISION_VERIFIED`

The script uses only the Python standard library; all arithmetic is finite and integral. It verifies all \(315\) tetrads, all \(315\) isotropic planes, the equivariant correspondence, every cyclic power needed for fixed-point counts, all \(22\) cycle partitions, the single collision and five-count sharpness, and the explicit characteristic-three irreducibility conditions. The CSV is the complete certificate of the enumeration, not a sample of curve equations.

## Relationship to prior work
The underlying \(315\) syzygetic tetrads, their graph interpretations as \(210\) quadrilaterals and \(105\) matchings, and their \(S_8\) action were already described by Olof Bergvall in *Cohomology of arrangements and moduli spaces* (2016, Section 3.6). The general finite étale/theta-geometric viewpoint and the isotropic-plane identification also occur in Bergvall, *Arithmetic and topology of classical structures associated to plane quartics* (first arXiv version 24 June 2021; journal 2023, Section 3.6). These geometric facts are **not** claimed as new. Bergvall's 2022 paper concerns Frobenius classes of degree-two del Pezzo surfaces, not a \(22\)-case arithmetic classification of syzygetic tetrad schemes of hyperelliptic genus-three curves.

The additional arithmetic statement here is the exact \(21\)-zeta-function spectrum, its unique permanent ambiguity even after separating the two natural kinds, and the optimal five-extension reconstruction bound. These are not the same as the orbit counts of the \(28\) odd or \(36\) even theta-characteristic schemes, whose actions occur on different finite sets.

## Limitations
This theorem concerns geometric finite étale theta schemes and Frobenius permutation actions. It does not produce explicit isogenies, reconstruct the curve or its Jacobian, recover the branch-point coordinates, or distinguish the two colliding branch partitions. It also does not classify which of all \(22\) types occurs over each fixed small field. The claimed originality is the stated complete arithmetic table and sharp inference bound, not the classical \(315\)-tetrad construction; an unindexed equivalent group-theoretic cycle table remains a literature-priority risk. No independent external mathematical audit is asserted.

## References
- O. Bergvall, *Cohomology of arrangements and moduli spaces*, Stockholm University, 2016, Section 3.6, https://www.diva-portal.org/smash/get/diva2:1426010/FULLTEXT01.pdf.
- O. Bergvall, *Arithmetic and topology of classical structures associated to plane quartics*, arXiv:2106.13072, version 1 dated 2021-06-24, https://arxiv.org/abs/2106.13072. Journal version: *European Journal of Mathematics* 9 (2023), article 117, https://doi.org/10.1007/s40879-023-00711-3.
- O. Bergvall, *Frobenius actions on Del Pezzo surfaces of degree 2*, arXiv:2211.12855, version 1 dated 2022-11-23, https://arxiv.org/abs/2211.12855.
- The complete arithmetic data and self-contained checker supplied alongside this result: `tetrad_frobenius_22.csv` and `verify_tetrads.py`.
