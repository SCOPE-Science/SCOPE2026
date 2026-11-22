# Frobenius coinvariants of the integral Schläfli double-six relation lattice

## Finding
Let \(k=\mathbb F_q\) have characteristic at least five. Let \(S/k\) be a smooth cubic surface obtained by blowing up a Frobenius-stable reduced set of six geometric points in \(\mathbb P^2_k\) in general position (no three collinear and not all on a conic). Write \(\mathcal L\) for its 27 geometric lines and \(\mathcal D\) for its 36 unordered Schläfli double-sixes. Set \(F=\mathbb Z^{\mathcal L}\), and define the saturated anticanonical-relation lattice and the double-six incidence lattice by
\[
K=\ker\bigl(F\longrightarrow \operatorname{Pic}(S_{\bar k})/\mathbb Z[-K_S]\bigr),\qquad
L=\sum_{D\in\mathcal D}\mathbb Z\sum_{\ell\in D}e_\ell,\qquad Q=K/L.
\]
Both \(K\) and \(L\) are Frobenius-stable. Label the six blown-up points by \(1,\ldots,6\), and let \(\sigma\in S_6\) describe Frobenius. Put \(o_2(\sigma)\) equal to the number of its orbits on the fifteen unordered two-element subsets of these six labels. Then the **integral Frobenius coinvariants** have the uniform isomorphism type
\[
\boxed{Q/(\sigma-1)Q\ \cong\ \mathbb Z/4\mathbb Z\ \oplus\ (\mathbb Z/2\mathbb Z)^{o_2(\sigma)-1}.}
\]
More structurally, there is an explicit \(S_6\)-equivariant isomorphism of mod-two modules
\[
\boxed{Q/2Q\ \cong\ \mathbb F_2^{\binom{[6]}2},}
\]
where the right side is the permutation module on unordered pairs, together with an invariant surjection \(Q\twoheadrightarrow\mathbb Z/4\mathbb Z\). These two pieces of information yield the coinvariant formula without separate Smith calculations for each permutation.

For the eleven Frobenius cycle partitions, \(o_2(\sigma)\) and the number of order-two factors are respectively:

| Cycle partition of six | \(o_2(\sigma)\) | Number of order-two factors |
|---|---:|---:|
| \((6)\), \((5,1)\) | 3 | 2 |
| \((4,2)\), \((4,1,1)\), \((3,3)\), \((3,2,1)\) | 5 | 4 |
| \((3,1,1,1)\) | 7 | 6 |
| \((2,2,2)\), \((2,2,1,1)\) | 9 | 8 |
| \((2,1,1,1,1)\) | 11 | 10 |
| \((1,1,1,1,1,1)\) | 15 | 14 |

## Assumptions and scope
Use the geometric Picard basis \(H,E_1,\ldots,E_6\), where \(H^2=1\), \(E_i^2=-1\), and all other pairwise products vanish. The 27 lines have classes \(E_i\), \(L_{ij}=H-E_i-E_j\) (for \(i<j\)), and \(C_i=2H-\sum_{j\ne i}E_j\). The anticanonical divisor is \(-K_S=3H-\sum_iE_i\). Frobenius permutes all indices in these expressions through \(\sigma\); this assumes the six-point blow-up is defined over \(k\). The quotient \(Q\) is a finite formal incidence-lattice quotient, not torsion of \(\operatorname{Pic}(S)\), not an arithmetic Brauer group, and not the component group of a Néron model. Coinvariants are for the cyclic Frobenius action on this finite group.

## Proof
**1. A uniform integral presentation.** There are 36 opposite pairs of roots \(r\in(-K_S)^\perp\) with \(r^2=-2\), represented by
\[
E_i-E_j\quad(i<j),\qquad H-E_i-E_j-E_h\quad(i<j<h),\qquad 2H-\sum_iE_i.
\]
A double-six corresponding to \(\{r,-r\}\) consists exactly of the twelve line classes \(\ell\) satisfying \(\ell\cdot r\ne0\). Its line sum represents \(4(-K_S)\), so \(L\subseteq K\). To see completeness, write \(r=aH-\sum b_iE_i\). From \(\sum b_i=3a\), \(\sum b_i^2=a^2+2\), and Cauchy–Schwarz, one obtains \(|a|\le2\); the possible integer tuples give precisely the 72 roots listed with both signs.

Order the line classes as \(E_1,\ldots,E_6\), then the fifteen \(L_{ij}\) lexicographically, then \(C_1,\ldots,C_6\). The images of \(E_1,\ldots,E_5,L_{12}\) in \(\operatorname{Pic}(S)/\mathbb Z[-K_S]\) are an integral basis. Use the remaining 21 line coefficients as coordinates on \(K\), correcting the six omitted pivot coordinates to kill the Picard class. The double-six vectors then form a \(21\)-by-\(36\) integer matrix \(B\). Exact elimination modulo four gives diagonal-type counts \(1^6,2^{14},0^1\). A specified square \(21\)-column minor, with the double-six columns sorted lexicographically by their support sets, has determinant \(-65536\); its zero-based indices are
\[
(1,3,5,6,9,10,13,14,16,17,18,19,20,22,23,26,27,29,30,33,35).
\]
Therefore the full integral Smith form is \(1^6,2^{14},4\): the mod-four calculation forces the order to be at least \(2^{16}\), while the exact minor bounds it by \(2^{16}\). Consequently \(Q\cong(\mathbb Z/2)^{14}\oplus\mathbb Z/4\). This re-establishes, rather than assumes, the previously published geometric integral presentation.

**2. The fifteen-pair module.** Write a formal line combination \(x\in F\) with coefficients \(x_{E_i},x_{C_i},x_{L_{ij}}\). For each pair \(\{i,j\}\), define
\[
\Phi(x)_{\{i,j\}}=x_{L_{ij}}+\sum_{h\notin\{i,j\}}x_{E_h}\pmod2.
\]
The formula commutes with every permutation of the six indices. It annihilates the double-six vectors modulo two. This follows by checking the three representative root families in step 1: for \(2H-\sum E_i\), every pair receives four exceptional-line contributions; for \(E_i-E_j\), the two involved exceptional lines compensate exactly for the eight \(L_{ih},L_{jh}\); for \(H-E_i-E_j-E_h\), the selected exceptional triple compensates the six pair-lines lying wholly inside that triple or its complement. Thus \(\Phi\) induces \(Q/2Q\to\mathbb F_2^{15}\). In the integral kernel basis of step 1, the images of the 15 basis elements associated with \(E_6\) and the fourteen \(L_{ij}\ne L_{12}\) form a \(15\)-by-\(15\) matrix of rank 15 modulo two (the attached verifier reconstructs and row-reduces this explicit matrix). Since \(\dim_{\mathbb F_2}Q/2Q=15\), the induced map is an \(S_6\)-equivariant isomorphism.

**3. Frobenius and the unique order-four summand.** Taking coinvariants and reducing modulo two commute. The coinvariants of a permutation module have one basis element per permutation orbit; hence \(\dim_{\mathbb F_2}(Q_\sigma/2Q_\sigma)=o_2(\sigma)\). The coordinate sum \(d(x)=\sum_{\ell}x_\ell\pmod4\) on \(K\) kills each twelve-line double-six and is permutation-invariant. It surjects onto \(\mathbb Z/4\): for example, the kernel-basis vector associated with \(E_6\) has odd coordinate sum. Thus every \(Q_\sigma\) surjects onto \(\mathbb Z/4\). As \(Q\) has precisely one cyclic order-four factor and exponent four, every quotient \(Q_\sigma\) also has at most one such factor. There is therefore exactly one; its remaining \(o_2(\sigma)-1\) nonunit invariant factors must all equal two. This proves the boxed formula.

**4. Pair-orbit counts.** For a cycle partition \(\lambda=(\lambda_1,\ldots,\lambda_c)\), the orbits on pairs within one cycle number \(\lfloor\lambda_i/2\rfloor\), and those joining two different cycles number \(\gcd(\lambda_i,\lambda_j)\). Hence
\[
o_2(\sigma)=\sum_i\left\lfloor\frac{\lambda_i}{2}\right\rfloor+\sum_{i<j}\gcd(\lambda_i,\lambda_j).
\]
This formula gives the eleven values displayed above and every extension-field variant by replacing \(\sigma\) with its power.

## Verification
The attached `verify_double_six_coinvariants.py` is self-contained Python 3 standard-library code. Run `python3 verify_double_six_coinvariants.py`. It builds all 27 line classes and all 36 root-pair double-sixes; checks the Picard-kernel presentation, the exact determinant-65536 minor, the complete mod-four diagonal, the rank-15 pair-module map, its vanishing on all 36 incidence columns, equivariance for adjacent transpositions, and the invariant degree-four map. For all eleven conjugacy types it independently constructs \([B\mid\sigma-I]\) and checks the stated invariant-factor pattern over \(\mathbb Z/4\), ending with `DOUBLE_SIX_FROBENIUS_COINVARIANTS_VERIFIED_OK`. Mod-four data are sufficient here because the exact determinant proof establishes that \(Q\) has exponent four. An independent full integer Smith-form calculation on the same presentations agrees with every row.

## Relationship to prior work
Dolgachev–Kapranov (1993) and Buckley–Košir (2006) give the classical double-six and six-point blow-up geometry. Elsenhans–Jahnel (2010) describe Galois-invariant double-sixes and the permutation action on the classical lines; they do not study the present finite integral relation quotient. The previously published *Order-four integral reconstruction obstruction for Schläfli double-sixes* determines the **underlying abelian group** \(Q\), but explicitly leaves Galois modules untreated. The published *Integral Frobenius coinvariants of the Segre cubic node–plane incidence* treats a different ten-by-fifteen incidence cokernel, not the 27-line/36-double-six relation lattice. A Fermat-cubic census of sixer markings addresses finite marking sets, not this module. None of these inspected results implies the displayed **fifteen-pair equivariant module isomorphism** without new work, nor states the coinvariant formula for this lattice.

## Limitations
The result is limited to cubic surfaces with a Frobenius-stable six-point blow-up marking; it is not a classification of all \(W(E_6)\)-Galois types or all smooth cubic surfaces. It does not identify the formal quotient with geometric torsion in a Picard or Brauer group. The literature comparisons are substantive but cannot rule out an unindexed equivalent integral representation-theoretic calculation. The arithmetic formula classifies the types that occur; it does not claim each type is realizable over every finite field.

## References
1. I. Dolgachev and M. Kapranov, *Schur quadrics, cubic surfaces and rank 2 vector bundles over the projective plane*, arXiv:alg-geom/9304005v1 (first posted 1993-04-13), §0. https://arxiv.org/abs/alg-geom/9304005
2. A. Buckley and T. Košir, *Determinantal representations of smooth cubic surfaces*, arXiv:math/0606098v1 (2006-06-05), §2. https://arxiv.org/abs/math/0606098
3. A.-S. Elsenhans and J. Jahnel, *Cubic surfaces with a Galois invariant double-six*, Central European Journal of Mathematics 8 (2010), 646–661, especially §§1,3,7. https://doi.org/10.2478/s11533-010-0036-1
4. *The order-four integral reconstruction obstruction for Schläfli double-sixes*, mathematical research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-order-four-integral-reconstruction-obstruction-for-schl-fli--0aac314408f8
5. *Integral Frobenius coinvariants of the Segre cubic node–plane incidence*, mathematical research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-integral-frobenius-coinvariants-of-the-segre-cubic-node-plane-in--be1de342035c
