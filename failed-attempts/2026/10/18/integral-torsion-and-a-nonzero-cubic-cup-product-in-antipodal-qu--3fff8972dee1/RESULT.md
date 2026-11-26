# Integral torsion and a nonzero cubic cup product in antipodal quotients of two Hamming-cube Rips complexes

## Finding
Let \(Q_n=\{0,1\}^n\) have Hamming distance, and let \(K_n=\operatorname{VR}_{\le2}(Q_n)\) be the flag complex on pairs at distance at most two. Let \(a(v)=v+(1,\ldots,1)\) be bitwise complementation, and let \(Y_n=|K_n|/\langle a\rangle\) be the **geometric orbit space**, not the Rips complex of an orbit metric. For each \(n\in\{4,5\}\), put \(b_4=5\), \(b_5=25\). Then

\[
\pi_1(Y_n)\cong\mathbb Z/2\mathbb Z,\qquad
H_j(Y_n;\mathbb Z)\cong\begin{cases}
\mathbb Z&j=0,\\
\mathbb Z/2\mathbb Z&j=1,\\
\mathbb Z^{b_n}&j=3,\\
0&\text{otherwise}.
\end{cases}
\]

Moreover the **complete mod-two cohomology ring** is

\[
H^*(Y_n;\mathbb F_2)\cong
\mathbb F_2[x,y_1,\ldots,y_{b_n-1}]/
\bigl(x^4,\ x y_i,\ y_i y_j\ (1\le i,j\le b_n-1)\bigr),
\quad |x|=1,\ |y_i|=3.
\]

In particular the unique nonzero \(H^1\)-class has a **nonzero third cup power** \(x^3\ne0\). The ring is isomorphic to the ring of \(\mathbb{RP}^3\vee\bigvee^{b_n-1}S^3\), but no homotopy equivalence of spaces is asserted.

## Assumptions and scope
The scale is inclusive: all subsets whose pairwise **graph distances are at most two** are simplices. Bitwise complementation has no fixed points in the realization for \(n>2\): a simplex fixed setwise by complementation would contain an antipodal pair at Hamming distance \(n>2\). Thus the action for \(n\in\{4,5\}\) is free, and the quotient is a finite \(\Delta\)-complex obtained by identifying antipodal simplices. The statement covers exactly these two cube dimensions; no extension to larger dimensions is inferred from enumeration.

## Proof
**Step 1: fundamental group and rational homology.** The established homotopy theorem of Adamaszek and Adams gives \(K_n\simeq\bigvee^{c_n}S^3\), where \(c_4=9\) and \(c_5=49\). Consequently \(K_n\) is simply connected and the free two-sheeted covering \(|K_n|\to Y_n\) gives \(\pi_1(Y_n)\cong C_2\). A free involution has Lefschetz number zero; because reduced rational homology of \(K_n\) occurs only in degree three, its trace on \(H_3(K_n;\mathbb Q)\) is \(1\). Rational transfer identifies \(H_3(Y_n;\mathbb Q)\) with the invariant summand of dimension \((c_n+1)/2=b_n\), and gives no further positive-degree rational homology.

**Step 2: complete finite mod-two calculation.** Encode cube vertices by integers \(0\le v<2^n\), with complement \(v\mapsto v\mathbin{\mathrm{xor}}(2^n-1)\); pairs at distance at most two form edges. Enumerate every clique by recursively intersecting neighbor sets. For each simplex, order vertices by the representative \(\min(v,v\mathbin{\mathrm{xor}}(2^n-1))\) of its antipodal vertex orbit, and choose the lexicographically smaller of the simplex and its complement. No simplex contains both endpoints of an antipodal vertex pair, so this supplies consistent face orders for the quotient \(\Delta\)-complex. Form all integral signed face boundaries by deletion, with canonicalization of each face, and check all products of successive boundary matrices vanish **over the integers**. Reduce the complete matrices modulo two and perform exact bit-vector Gaussian elimination. The verified number of quotient cells by dimensions \(0,1,\ldots\), boundary ranks by dimensions \(1,2,\ldots\), and resulting Betti numbers are

\[
\begin{array}{c|c|c|c}
n & \text{quotient cells}& \text{boundary ranks over }\mathbb F_2 & \text{mod-two Betti numbers}\\ \hline
4&(8,40,80,60,8)&(7,32,47,8)&(1,1,1,5,0)\\
5&(16,120,320,320,96,16)&(15,104,215,80,16)&(1,1,1,25,0,0).
\end{array}
\]

The supplied standalone verifier reconstructs the simplices and every boundary from the definition; neither precomputed face tables nor asserted ranks are imported.

**Step 3: deduction of integral homology.** Rational homology determines the free ranks. Standard transfer for a double cover satisfies \(p_*\operatorname{tr}=2\,\mathrm{id}\), and all integral homology of \(K_n\simeq\bigvee S^3\) is torsion-free. Hence the transfer sends every torsion class of \(Y_n\) to zero, so all torsion in \(H_*(Y_n;\mathbb Z)\) has exponent at most two. Write \(t_i\) for its \(\mathbb Z/2\)-rank in degree \(i\). The universal coefficient theorem yields \(\beta_i(Y_n;\mathbb F_2)=b_i+t_i+t_{i-1}\) for \(i\ge1\), with \(t_0=0\). The complete mod-two rank lists above force \(t_1=1\) and \(t_i=0\) for every \(i\ge2\). This proves all the displayed integral homology groups, including the absence of odd or higher two-primary torsion.

**Step 4: the cubic product.** Let \(x\in H^1(Y_n;\mathbb F_2)\) classify the double cover. On an oriented quotient edge, choose a lift of its ordered vertices and evaluate the difference of their last bits. This well-defined cocycle represents \(x\): changing the sheet complements both bits and leaves their difference modulo two invariant; the class is nonzero because the covering is connected and nontrivial. Using the Alexander–Whitney product on the ordered \(\Delta\)-complex, compute \(x^2\) on each oriented triangle as the product of the cocycle values on consecutive edges, and likewise \(x^3\) on each tetrahedron. Verify both products are cocycles and test membership in the complete coboundary image by exact binary elimination. In dimension two, adjoining the computed cocycle raises the respective coboundary ranks from \(32\) to \(33\) and from \(104\) to \(105\) for \(n=4,5\). In dimension three the ranks increase from \(47\) to \(48\) and from \(215\) to \(216\). Thus \(x^2\) and \(x^3\) are nonzero for both dimensions. Finally, the mod-two dimensions are one in degrees one and two, \(b_n\) in degree three, and zero in all higher degrees. Choose \(b_n-1\) complementary degree-three generators to \(x^3\). Products involving them vanish by degree, and \(x^4=0\), proving the complete ring presentation.

## Verification
Execute `python3 verify_antipodal_rips.py` using only the Python standard library. The exact expected stdout appears in `verified_output.txt`; rerun and compare. The verifier checks complete clique enumeration, quotient cell orbits, all integral boundary-square identities, complete binary boundary ranks, the covering cocycle and nontrivial square/cube using rank augmentation. It checks the exact expected data for \(n=4,5\) before printing. The original complexes contain \(392\) and \(1776\) nonempty simplices, respectively. These are exhaustive finite certificates for the stated two cube dimensions, not extrapolations from sampled parameters.

## Relationship to prior work
Adamaszek and Adams established the nonequivariant wedge-of-three-spheres homotopy theorem used in Step 1. Galetto, Montaño and Wellner (2026) determine rational hyperoctahedral representations of the original Vietoris–Rips complexes at small scales; such rational linear representations do not determine the integral homology or cup products of a geometric orbit space. Bendersky, Elia and Grbić (2026) study cohomological properties of the **original hypercube Rips complexes**, not the two antipodal orbit-space rings calculated here. The novelty claimed is the exact integral torsion and nonzero cubic quotient cup product for the two specified low-dimensional cases, rather than the known wedge theorem or its rational character consequences.

## Limitations
These calculations classify \(H_*(Y_n;\mathbb Z)\), \(\pi_1(Y_n)\) and the mod-two ring for \(n=4,5\). No homotopy equivalence with a wedge containing projective space, no full integral Postnikov invariants, no higher-dimensional classification and no independent verification are asserted. The precise finite verifications can be rerun but do not establish an all-dimensional pattern. Although accessible close primary results do not state this quotient classification, an unindexed equivalent calculation remains a literature risk.

## References
1. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040, https://arxiv.org/abs/2103.01040.
2. F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784 (first submitted June 18, 2026), https://arxiv.org/abs/2606.20784.
3. M. Bendersky, S. Elia and J. Grbić, *Cohomological properties of the Vietoris–Rips Complex of a Hypercube Graph*, arXiv:2605.00705 (first submitted May 1, 2026), https://arxiv.org/abs/2605.00705.
