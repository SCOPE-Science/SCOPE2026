# Antipodal two-point punctures erase all seven-dimensional five-cube Rips homology

## Finding
Let \(Q_5=\{0,1\}^5\) have its original Hamming metric, and write \(X=\operatorname{VR}_{\le3}(Q_5)\). For each antipodal pair \(\{p,\overline p\}\), with \(d_H(p,\overline p)=5\), let \(Z_p=X[Q_5\setminus\{p,\overline p\}]\) be the induced one-scale Rips subcomplex. Then
\[
\boxed{Z_p\simeq S^4.}
\]
Furthermore the induced inclusion \(Z_p\hookrightarrow X\) is an isomorphism on \(H_4(-;\mathbb Z)\) and zero on \(H_7(-;\mathbb Z)\). The previously known full-complex homotopy type is \(X\simeq S^4\vee\bigvee^{10}S^7\). Thus removal of two antipodal landmarks preserves the fourth-dimensional sphere but eliminates all ten seventh-dimensional homology generators. In the natural two-step deletion chain, each of the two vertex losses removes precisely five primitive seventh-homology generators.

## Assumptions and scope
The Rips convention is inclusive: a subset is a face exactly when all pairwise Hamming distances are at most three. Puncturing means removing vertices but retaining all original pairwise Hamming distances between the survivors. Antipodal is exactly distance five in the binary five-cube. The result is a fixed finite integral homotopy computation, not a dimension-uniform formula.

## Proof
**1. Complete acyclic matching for the antipodal puncture.** Encode five-bit words as integers \(0,\ldots,31\). The antipodal representative pair is \(\{0,31\}\). A face is a subset containing no pair of words whose Hamming distance is four or five. The included standalone verifier enumerates **every** such face in the full complex, one-site puncture, antipodal two-site puncture, and vertex link. For each complex it applies a fixed pivot permutation, matching currently unmatched faces \(\sigma\) and \(\sigma\cup\{v\}\) whenever both exist and are unmatched. It then builds every cover of the entire face poset, reverses the orientation of matched covers, and checks acyclicity by an exhaustive topological sort.

For the antipodal two-site complex, it finds exactly **53,403 augmented faces**, **26,701 matched pairs**, **304,150 directed Hasse covers**, and **one unmatched dimension-four face**; the empty face is matched, and no other critical face remains. The acyclicity test passes. Reduced discrete Morse theory thus yields one basepoint and one four-cell, proving \(Z_0\simeq S^4\), not merely equality of rational Betti numbers. Bitwise translation by any five-bit vector is an isometry, and carries any antipodal pair to \(\{0,31\}\), proving the statement for all 16 such pairs.

**2. Exact inclusion and two independent homology losses.** The complete matching also returns one four-cell and ten seven-cells for \(X\), one four-cell and five seven-cells for \(Y=X[Q_5\setminus\{0\}]\), and five six-cells for \(L=\operatorname{lk}_{X}(31)\). These latter critical counts agree with, and can be compared to, the published integral full-complex theorem and its vertex-filtration lemmas. The link matching has no critical faces besides five dimension-six faces, so \(L\simeq\bigvee^5 S^6\). Crucially, since \(d_H(0,31)=5>3\), the vertex \(0\) cannot lie in \(L\), and the link of \(31\) in \(Y\) is **exactly** the same simplicial complex \(L\).

For any vertex deletion \(B=A\setminus\{v\}\), the star decomposition identifies the homotopy cofiber of \(B\hookrightarrow A\) with \(\Sigma\operatorname{lk}_{A}(v)\). Applied to \(Z_0\subset Y\) and \(Y\subset X\), both cofibers are \(\Sigma L\simeq\bigvee^5 S^7\), because the links are isomorphic by the antipodal distance argument. Their reduced integral relative homology is zero outside degree seven. Therefore the long exact sequences show that both inclusions induce **isomorphisms on \(H_4\)**. They also give the short exact sequences
\[
0\to H_7(Y;\mathbb Z)\to H_7(X;\mathbb Z)\to\mathbb Z^5\to0,
\qquad
0\to H_7(Z_0;\mathbb Z)\to H_7(Y;\mathbb Z)\to\mathbb Z^5\to0.
\]
Here \(H_7(Z_0;\mathbb Z)=0\), \(H_7(Y;\mathbb Z)\cong\mathbb Z^5\), and \(H_7(X;\mathbb Z)\cong\mathbb Z^{10}\). Each quotient is free, making the injections primitive and split over the integers, and the second sequence identifies all five surviving seventh-homology classes after the first removal as those killed by the second. This proves the stated total loss and survival of the fourth sphere.

## Verification
Run `python3 verify.py` with Python 3.10 or newer. The verifier uses only the Python standard library, and is bundled alongside its captured successful output. Its exact finite certificate checks all augmented simplices and all Hasse covers; for the antipodal puncture the critical-cell vector is a single dimension-four cell, while the other three checks support the two cofiber maps. The one-puncture and full-complex wedge types were known from prior research and are credited, not claimed as new.

## Relationship to prior work
Feng's 2023 radius-three hypercube theorem established the full wedge \(S^4\vee\bigvee^{10}S^7\). Its vertex-order induction also determines the single-vertex deletion and the relevant final-vertex link, so **neither the single-deletion type nor the link type is claimed as original here**. The new object is the simultaneous removal of both antipodal vertices, which does not form an initial segment of that vertex order; the resulting collapse to a lone fourth sphere and the comparison of two successive primitive losses are not supplied by those earlier statements. The June 18, 2026 preprint studies homology representations of the full cube under group actions rather than antipodal vertex deletion. Related published research on fixed-point sets of cube symmetries, radius-two punctures, or nonhypercube one-site punctures treats different objects. Semantic database queries and primary-paper comparisons found no result implying this specific two-puncture homotopy classification, subject to residual priority risk.

## Limitations
This is one exact 30-point metric subspace at radius three, transported to 16 equivalent antipodal pairs. Arbitrary two-site distances, multiple deletions, other cube dimensions and the full persistence filtration are not classified. Verification is exhaustive finite, not a dimension-general theorem. An independent mathematical audit has not been performed.

## References
1. Ziqin Feng, *Homotopy types of Vietoris–Rips complexes of Hypercube Graphs*, arXiv:2305.07084 (public May 11, 2023), especially Theorem 23, Theorem 24 and the vertex-link construction. https://arxiv.org/abs/2305.07084
2. *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784 (public June 18, 2026). https://arxiv.org/abs/2606.20784
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, for acyclic matching and CW reduction.
