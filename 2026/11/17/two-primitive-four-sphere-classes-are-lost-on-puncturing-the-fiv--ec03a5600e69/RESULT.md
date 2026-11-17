# Two primitive four-sphere classes are lost on puncturing the five-by-five torus Rips complex

## Finding
Let \(T=\mathbb Z_5\times\mathbb Z_5\) with \(d_1((x,y),(u,v))=\min(|x-u|,5-|x-u|)+\min(|y-v|,5-|y-v|)\), using cyclic coordinate differences. Let \(X=\operatorname{VR}_{\le3}(T)\), and let \(Y_p\) denote the full induced subcomplex after removing any one point \(p\) (the metric is *not recomputed* after removing \(p\)). Then
\[
Y_p\simeq\bigvee^7S^4,\qquad \operatorname{lk}_{X}(p)\simeq\bigvee^2S^3,\qquad X\simeq\bigvee^9S^4.
\]
The map \(\widetilde H_4(Y_p;\mathbb Z)\to\widetilde H_4(X;\mathbb Z)\) is injective with a primitive rank-seven image and rank-two free quotient. In suitable wedge coordinates its inclusion is the standard inclusion \(\bigvee^7 S^4\hookrightarrow\bigvee^9S^4\). Its quotient (homotopy cofiber) is \(X/Y_p\simeq\bigvee^2S^4\).

## Assumptions and scope
All complexes are finite abstract simplicial complexes including the empty face in the augmented face poset. Rips faces have *inclusive* pairwise diameter at most three, with the *original* cyclic Manhattan metric. The result holds for every one-point deletion because the torus translations act transitively. The link contains the faces disjoint from \(p\) that can be adjoined to \(p\).

## Proof
**Metric reduction.** The only pairs of distinct torus points at distance greater than three have coordinate distances \((2,2)\). Form the graph \(H\) with such forbidden pairs as edges. Then \(X=\operatorname{Ind}(H)\), \(Y_p=\operatorname{Ind}(H-p)\) and \(\operatorname{lk}_X(p)=\operatorname{Ind}(H-N_H[p])\). The coordinate transform \((x,y)\mapsto(x+y,x-y)\) is invertible modulo five, and takes each forbidden edge into a unit-coordinate step. Hence \(H\cong C_5\square C_5\).

**Finite complete acyclic matchings.** The enclosed `verification.py` enumerates every independent vertex set of \(H\) (including the empty set) and applies a deterministic matching: in the fixed coordinate order induced by the transform, at each pivot \(v\), pair every still-unmatched face \(S\) without \(v\) to the still-unmatched face \(S\cup\{v\}\), whenever it exists. It constructs the *entire* augmented Hasse diagram and reverses matched arrows, then checks acyclicity by a complete topological sort. The output reports \(25{,}531\), \(19{,}849\), and \(5{,}682\) augmented faces for the full complex, its deletion, and the link, respectively. The unmatched faces are exactly nine in dimension four, seven in dimension four, and two in dimension three, respectively. The empty face is matched in all cases.

By the elementary finite discrete-Morse theorem (including the reduced/augmented variant), these acyclic matchings produce CW models with one base point and precisely the indicated same-dimensional top cells. With no lower positive-dimensional cells, the attaching maps are trivial; the three spaces have the displayed integral sphere-wedge homotopy types. No inference from numerical homology alone is used.

**Inclusion and primitive quotient.** There is the simplicial cofibration \(\operatorname{lk}_X(p)\to Y_p\to X\) obtained from \(X=Y_p\cup (p*\operatorname{lk}_X(p))\). The relative homology is \(H_4(X,Y_p;\mathbb Z)\cong\widetilde H_3(\operatorname{lk}_X(p);\mathbb Z)\cong\mathbb Z^2\), with all other positive relative groups zero. Since \(\widetilde H_3(Y_p)=0\), the long exact sequence yields the short exact sequence \(0\to\mathbb Z^7\to\mathbb Z^9\to\mathbb Z^2\to0\). Its quotient is free, hence the image is primitive. Maps between wedges of four-spheres are determined on degree-four homology by integer matrices; Smith reduction of this primitive injection gives the stated standard-inclusion homotopy coordinates. Finally, \(X/Y_p\cong(p*\operatorname{lk}_X(p))/\operatorname{lk}_X(p)\simeq\Sigma\operatorname{lk}_X(p)\simeq\bigvee^2S^4\).

## Verification
Run `python3 verification.py` using only Python 3 standard libraries. The actual embedded run output is `verification_output.txt`. It reports three complete acyclic Hasse graphs with, respectively, \(142{,}050\), \(108{,}568\), and \(27{,}800\) oriented covers. Every vertex is visited in each topological sort, so this is a finite proof certificate, not a probabilistic test. An independently formulated identity between cyclic distances and forbidden graph edges is checked on all ordered point pairs.

## Relationship to prior work
Adams, Adetowubo, Barriga-Acosta, Feng and Sterling (2025), Section 7 and Theorem 7.1, already prove the **unpunctured** homotopy type \(X\simeq\bigvee^9S^4\). A subsequent published record on \(\operatorname{Ind}(C_5\square C_5)\) likewise supplies the unpunctured nine-sphere type, which the present proof rechecks only as a needed premise. Neither identified statement determines the punctured space, the link, or the primitive inclusion. This work addresses robustness of a torus Rips invariant under removal of a single metric sample, not a new derivation of the previously known full-space homotopy type.

## Limitations
This treats a single vertex omission from the five-by-five torus at *inclusive* scale three. It does not describe two-point deletions, an intrinsically re-metrized punctured graph, equivariant automorphism representations, or other torus sizes. Novelty is relative to the sources and records actually accessible, not a guarantee against unindexed results; an identified relevant published record was accessible only in summary form.

## References
1. H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng, J. Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134v2 (first public 2025-02-10), Sections 5, 7, 8, https://arxiv.org/html/2502.07134v2.
2. *Nine integral four-spheres in the fully periodic five-by-five hard-square complex*, published record, 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-nine-integral-four-spheres-in-the-fully-periodic-five-by-five-ha--374b6b4d37f7 (summary inspected; full text inaccessible).
3. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145.
