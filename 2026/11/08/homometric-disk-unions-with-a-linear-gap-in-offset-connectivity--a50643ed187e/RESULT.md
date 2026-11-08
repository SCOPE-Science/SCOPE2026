# Homometric disk unions with a linear gap in offset connectivity

## Finding
For every integer \(m\ge1\), there exist two noncongruent compact planar sets \(K_m,L_m\), each the union of \(6m\) pairwise disjoint closed Euclidean disks of radius \(1/4\), such that:

1. Their **complete, direction-sensitive continuous covariograms coincide**: for every translation vector \(v\in\mathbb R^2\),
   \[\operatorname{area}(K_m\cap(K_m+v))=\operatorname{area}(L_m\cap(L_m+v)).\]
   Consequently the displacement vectors of independent area-uniform point pairs have the same full law, not merely the same length distribution; the sets also have identical Fourier-intensity data.
2. For every offset radius \(11/4<r<13/4\), the Euclidean parallel body \(K_m+r\overline B_2\) is connected, whereas \(L_m+r\overline B_2\) has exactly \(m+1\) connected components. In particular, at the fixed offset radius \(r=3\), their zeroth Betti numbers differ by \(m\), which equals one-sixth of the number of disks.

Thus the complete two-point displacement law of planar sets formed from disjoint congruent disks does **not** control the connectedness of their fixed-radius parallel bodies: the discrepancy can grow linearly in geometric description size. The linear growth order is maximal up to a constant for unions of a specified number of disks, since no such offset can have more connected components than disks.

## Assumptions and scope
Let \(A=\{0,1,4,10,12,17\}\), \(B=\{0,1,8,11,13,17\}\), and \(H_m=\{22k:0\le k<m\}\). Define the center sets \(C_m=A+H_m\), \(E_m=B+H_m\), and let \(D_s=\{(x,y)\in\mathbb R^2:x^2+y^2\le s^2\}\). The two compact planar domains are
\[
 K_m=\bigcup_{c\in C_m}\bigl((c,0)+D_{1/4}\bigr),\qquad
 L_m=\bigcup_{e\in E_m}\bigl((e,0)+D_{1/4}\bigr).
\]
Here a scalar center in \(\mathbb R\) is identified with its planar representative on the horizontal axis. A parallel body is defined by Minkowski addition \(S+rD_1=\{s+ru:s\in S,\ \|u\|\le1\}\). Every finite union in the statement consists of genuine disks with pairwise disjoint interiors and smooth boundary components. The result does not concern connected source domains, nor their convex hulls.

The geometric description size is the number \(6m\) of initial components. There is no claim that the ratio \(1/6\) is the optimal universal constant for all homometric constructions.

## Proof
**1. Base autocorrelation.** For any finite set of integers \(T\), write \(\nu_T=\sum_{t\in T}\delta_t\) and \(\widetilde\nu_T=\sum_{t\in T}\delta_{-t}\). Directly listing all fifteen unordered positive differences for each six-point set gives exactly the same multiset, with one occurrence of each of
\[1,2,3,4,5,6,7,8,9,10,11,12,13,16,17.\]
Hence their signed differences have the same multiplicities: six occurrences of zero and one of each listed positive and negative difference. Equivalently,
\[\nu_A*\widetilde\nu_A=\nu_B*\widetilde\nu_B.\]
This particular six-point homometric pair is classical; its homometry is not claimed as new.

**2. Arbitrarily many disk centers.** The gap between consecutive translated blocks is \(22-17=5\), so the blocks of \(C_m\) and \(E_m\) are disjoint. Therefore their counting measures satisfy
\[\nu_{C_m}=\nu_A*\nu_{H_m},\qquad \nu_{E_m}=\nu_B*\nu_{H_m}.\]
Associativity and commutativity of convolution give
\[
 \nu_{C_m}*\widetilde\nu_{C_m}
 =(\nu_A*\widetilde\nu_A)*(\nu_{H_m}*\widetilde\nu_{H_m})
 =(\nu_B*\widetilde\nu_B)*(\nu_{H_m}*\widetilde\nu_{H_m})
 =\nu_{E_m}*\widetilde\nu_{E_m}.
\]
The minimum separation between distinct centers in either family is one. Since twice the original disk radius is \(1/2\), their interiors are pairwise disjoint and both sets have precisely \(6m\) disks and the same positive area \(6m\pi/16\).

**3. Equality of the entire continuous covariogram.** Put \(\phi=\mathbf1_{D_{1/4}}\), write \(\mu_C=\sum_{c\in C_m}\delta_{(c,0)}\), and likewise for \(E_m\). Disjoint disk interiors imply the indicator identity, almost everywhere,
\[\mathbf1_{K_m}=\mu_C*\phi,\qquad\mathbf1_{L_m}=\mu_E*\phi.\]
For an integrable real indicator \(f\), write \(\widetilde f(x)=f(-x)\). Its covariogram is \(g_f=f*\widetilde f\), since \(g_f(v)=\int f(x)f(x-v)\,dx\). Thus
\[
 g_{K_m}=(\mu_C*\widetilde\mu_C)*(\phi*\widetilde\phi)
           =(\mu_E*\widetilde\mu_E)*(\phi*\widetilde\phi)=g_{L_m}.
\]
For independent points \(X,Y\) chosen uniformly in a positive-area region \(S\), the vector \(X-Y\) has density \(g_S(v)/\operatorname{area}(S)^2\). The regions have equal area, so the complete displacement laws are identical. Fourier transforming the covariogram identity also gives equality of squared Fourier-transform magnitudes. No reconstruction claim about phase is used.

**4. Exact offset topology.** Minkowski addition distributes over finite unions and \(D_{1/4}+rD_1=D_{r+1/4}\). Hence each parallel body is the union of disks of radius \(R=r+1/4\), centered on the horizontal axis at the corresponding finite center set. For such a linearly ordered disk family, the number of connected components is exactly one plus the number of consecutive center gaps strictly exceeding \(2R\). Indeed, adjacent disks overlap exactly when their center distance is at most \(2R\); if the next consecutive gap is larger, no disk to its left can meet any disk to its right.

The successive center gaps within each translated block of \(C_m\) are \(1,3,6,2,5\), and those of \(E_m\) are \(1,7,3,2,4\). Every between-block gap is \(5\). For \(11/4<r<13/4\), one has \(6<2(r+1/4)<7\). Every gap of \(C_m\) is at most \(6\), so its offset is connected. In \(E_m\) exactly one within-block gap equals \(7\), and no other gap exceeds \(6\), hence its offset has exactly \(m+1\) components. In particular the strict inequalities hold at \(r=3\), where the enlarged disk radius is \(13/4\).

The disparity \((m+1)-1=m\) is one-sixth of the \(6m\) original disks. Because a parallel body is the union of \(6m\) disks, it can have at most \(6m\) components, proving that the observed linear order cannot be improved to superlinear growth as a function of disk count. The differing consecutive-gap patterns also show the center sets, and thus the unions, are not related by a rigid motion.

## Verification
Run `python3 checker.py` from this directory. The checker independently constructs signed difference counters for the base six-point configurations; enumerates signed differences for \(m=1,\ldots,59,100,200\); compares component counts at several rational offsets; checks center separation and the relevant strict gap thresholds. Its expected success line is `HOMOMETRIC_DISK_OFFSET_LINEAR_COMPONENT_GAP_OK 61`. The universal statement follows from the preceding convolution and gap proofs, not from testing finitely many \(m\).

## Relationship to prior work
Homometric finite point sets and their relationship to covariograms and diffraction are classical. Baake and Grimm already exhibited planar homometric windows and their Fourier-covariogram relationship in a 2006 paper; Grimm and Baake discuss related inverse problems in their 2008 paper. Averkov and Langfeld's 2014 preprint gives a general direct-sum construction for homometric lattice sets (Proposition 1.1); the convolution step here is an instance of that known technique. Cho's 2010 dissertation explicitly displays the two base six-point sets and their equal distance histograms. Those facts, and nonunique reconstruction from pairwise distance data, are **not** new contributions here.

The new asserted statement is the quantitative, all-size **offset-connectivity separation** for positive-area smooth disk unions while preserving the complete direction-sensitive covariogram, with explicit stability across a nonzero offset interval. In the inspected portions of those sources, no corresponding unbounded zeroth-Betti gap for equal-covariogram parallel bodies is stated. The construction does not claim novelty of its base homometric pair, of convolution under direct sums, or of the trivial upper bound on component count.

## Limitations
The source regions are disconnected; this is essential to the stated construction. Its metric and topology are Euclidean and planar; the theorem does not assert the same disparity for connected input regions or for convex bodies. The sets share the covariogram of the **original** domains, not the covariograms of their offset domains. Connectedness is compared at an offset after dilation, not claimed to differ for the initial disjoint disk unions. The sharpness statement is an order-of-growth claim only. No exhaustive historical-priority determination is asserted; obscure constructions might imply the same phenomenon.

## References
1. M. Baake and U. Grimm, *Homometric model sets and window covariograms*, arXiv:math/0610411, first posted 2006-10-12, https://arxiv.org/abs/math/0610411.
2. U. Grimm and M. Baake, *Homometric Point Sets and Inverse Problems*, arXiv:0808.0094, first posted 2008-08-01, https://arxiv.org/abs/0808.0094.
3. G. Averkov and B. Langfeld, *Homometry and direct-sum decompositions of lattice-convex sets*, arXiv:1412.7676, first posted 2014-12-23, https://arxiv.org/abs/1412.7676.
4. M. Cho, *Approximation Algorithms for Point Pattern Matching and Searching*, Ph.D. dissertation, University of Maryland, 2010, section 2.7 and chapter 4, https://api.drum.lib.umd.edu/server/api/core/bitstreams/259f6667-0d09-4fba-babd-dc3787ae4362/content.
5. J. Rosenblatt and P. D. Seymour, *The Structure of Homometric Sets*, SIAM Journal on Algebraic Discrete Methods 3(3), 343–350 (1982), DOI 10.1137/0603035; abstract consulted, full text not inspected.
