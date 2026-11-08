# Dual sphere-wedge homotopy types in the nine-point affine plane

## Finding
Let \(P=\mathbb F_3^2\), and let \(\mathcal L\) be its twelve three-point affine lines. Define the line-free simplicial complex and its theta complex, respectively, by
\[
X=\{\sigma\subseteq P:\; L\nsubseteq\sigma\text{ for every }L\in\mathcal L\},\qquad
\Theta=\{\sigma\subseteq P:\;\sigma\cap L=\varnothing\text{ for some }L\in\mathcal L\}.
\]
Then \(\Theta\) is the combinatorial Alexander dual of \(X\), and their **integral homotopy types** are
\[
\boxed{X\simeq S^2\vee\bigvee^{11}S^3,\qquad
\Theta\simeq\bigvee^{11}S^3\vee S^4.}
\]
In particular, both spaces are simply connected, and the displayed sphere wedges hold integrally, not just after rationalization. The previously known integral homology groups of \(X\), and the homology groups of \(\Theta\) inferred from Alexander duality, are not claimed to be new.

## Assumptions and scope
Points of \(P\) are ordered lexicographically as \((0,0),(0,1),(0,2),(1,0),\ldots,(2,2)\) and indexed from zero to eight. For \((a,b)\in P\) and each of the four directions \((1,0),(0,1),(1,1),(1,2)\), the corresponding affine line is \(\{(a+td_1,b+td_2):t\in\mathbb F_3\}\). Deduplication yields twelve lines; every pair of points belongs to exactly one line, and every point to four lines. A simplicial face is a subset of the nine-point ground set, including the empty subset in enumerations. Geometric realizations and homotopy equivalences of their **nonempty-face** complexes are intended.

The theta complex is the Alexander dual in the fixed nine-element vertex set: for any \(\sigma\subseteq P\), one has \(\sigma\in\Theta\) exactly when \(P\setminus\sigma\notin X\). Thus \(\Theta\) is equivalently the simplicial complex whose facets are the six-point complements of the twelve lines. It is also the point-side component of the ordinary open-neighborhood complex of the bipartite point-line **nonincidence** graph of the affine plane, distinct from the incidence graph and its metric Rips complexes.

## Proof
All the finite steps are explicit in the standalone standard-library Python verifier `verify.py`. Represent \(\sigma\subseteq P\) by the nine-bit integer \(\sum_{j\in\sigma}2^j\). Membership in \(X\) is tested by ensuring that no line's three bits are all present; membership in \(\Theta\) by requiring that at least one line is bitwise disjoint. Enumerating all \(2^9\) masks gives \(172\) faces of \(X\) and \(340\) faces of \(\Theta\), counting the empty face. The respective ordinary face vectors, by dimensions in ascending order, are
\[
 f(X)=(9,36,72,54),\qquad f(\Theta)=(9,36,84,126,72,12).
\]
The verifier also independently enumerates \(\Theta\) as the union of all subsets of twelve six-point line complements and confirms the Alexander-duality equality of all masks.

For either complex, perform the following explicit matching on the full face set. For each vertex label \(v=0,1,\ldots,8\), in order, pair each still-unpaired \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), whenever both are still-unpaired faces; delete each pair before proceeding. The unique pair with empty lower face is \((\varnothing,\{(0,0)\})\). Omit this pair from the ordinary nonempty-face matching and retain the singleton as a critical vertex. The other pairs give an ordinary discrete vector field with \(79\) pairs for \(X\) and \(163\) pairs for \(\Theta\).

For complete, not sampled, verification of acyclicity, enumerate every covering relation \(\tau\lessdot\sigma\) of the nonempty-face posets, orient matched covers upward and all other covers downward, then run Kahn's exact topological sort. For \(X\), all \(171\) nonempty faces are sorted across \(504\) directed incidences; for \(\Theta\), all \(339\) nonempty faces are sorted across \(1260\) incidences. Therefore both matchings are acyclic. The critical ordinary cells are precisely
\[
\begin{array}{c|ccc}
 &\text{dimension }0&\text{dimension }2&\text{dimension }3\\\hline
 X&1&1&11
\end{array}
\qquad
\begin{array}{c|ccc}
 &\text{dimension }0&\text{dimension }3&\text{dimension }4\\\hline
 \Theta&1&11&1.
\end{array}
\]
All unlisted critical dimensions have zero cells. Forman's discrete Morse theorem therefore gives a CW model with these respective critical-cell counts.

To determine the nontrivial possible attaching maps, write each oriented simplicial boundary with signs \((-1)^j\) after removing the \(j\)-th vertex in ascending index order. Algebraically cancel, over \(\mathbb Z\), every matched face pair using its incidence unit \(\pm1\). At each cancellation \((a,b)\), the pivot is \([\partial b:a]=\pm1\); for any other same-dimensional column \(c\), the exact update of its remaining boundary is the integral Schur complement
\[
\partial_{\rm new}c=\partial c-\frac{[\partial c:a]}{[\partial b:a]}\,\partial b
\quad\text{after removing the eliminated rows and columns}.
\]
The verifier performs all these updates in integers and independently checks that each pivot remains a unit. For \(X\), the final signed \(1\times11\) Morse boundary from degree three to degree two is **identically zero**. For \(\Theta\), the final signed \(11\times1\) Morse boundary from degree four to degree three is **identically zero**. No fields or floating-point approximations enter this calculation.

The CW model for \(X\) has one zero-cell, one two-cell and eleven three-cells, with no one-cells. Its two-skeleton is \(S^2\). The attaching maps of the three-cells lie in \(\pi_2(S^2)\cong H_2(S^2;\mathbb Z)\), and their integer degrees are exactly the entries of the zero Morse boundary; hence every attaching map is nullhomotopic. Therefore \(X\simeq S^2\vee\bigvee^{11}S^3\). Similarly, the three-skeleton of the theta model is \(\bigvee^{11}S^3\). Hurewicz gives \(\pi_3(\bigvee^{11}S^3)\cong H_3(\bigvee^{11}S^3;\mathbb Z)\). The lone four-cell's zero boundary is therefore its zero homotopy attaching class, and \(\Theta\simeq\bigvee^{11}S^3\vee S^4\).

## Verification
From a directory containing `verify.py`, run `python3 verify.py`; it has no nonstandard dependencies. The committed `verification_output.txt` records the actual deterministic output, ending `ALL_CHECKS_PASS`. The code checks twelve lines, the unique line through each pair of points, two face constructions for \(\Theta\), all face counts, all matching pairs, every directed Hasse cover, exhaustive acyclicity and all integral Morse elimination pivots. Separately from integral cancellation, it computes binary boundary ranks directly from the original face sets: for \(X\), ranks in degrees one, two, three are \(8,28,43\); for \(\Theta\), ranks in degrees one through five are \(8,28,56,59,12\). These ranks corroborate the Betti vectors but do not by themselves establish the asserted homotopy equivalences.

## Relationship to prior work
The line-free complex \(X\) is precisely Alan Lew's \(X_3\), not an unnamed new combinatorial object. Figure 1.1 of Lew's 2021 thesis already gives its complete reduced integral homology: one generator in degree two, eleven in degree three, and no others. Via standard combinatorial Alexander duality, these data also determine the integral homology groups of \(\Theta\). **Neither those homology computations nor the Alexander-dual transfer is claimed as original.** The additional claim here is the two complete integral sphere-wedge *homotopy* classifications, witnessed by explicit acyclic matchings and zero integral attaching degrees. The known homology groups alone do not imply them: for example, they do not rule out nontrivial fundamental groups or nonzero higher attaching maps.

Conant and Thistlethwaite introduced the hypergraph theta complex and its Alexander-dual relationship in an arXiv paper first public on August 5, 2008. Their public abstract describes cubical hypergraphs and other examples, but complete paper text could not be inspected, leaving some coverage uncertainty. Separately, a published result about a projective-plane **nonincidence** graph concerns the thirteen-point projective plane and a different dimension-four/five wedge; a published result about affine-plane **incidence-graph metric Vietoris–Rips** complexes concerns a twenty-one-vertex metric construction. The full statements of these two other constructions were inspected, and neither implies the present two nine-point hypergraph homotopy classifications.

## Limitations
The homotopy assertions are proved only for the affine plane \(\operatorname{AG}(2,3)\); no claim is made for other finite affine planes or arbitrary Steiner triple systems. The explicit acyclic matching depends on the stated coordinate indexing; the resulting homotopy type is an invariant of the abstract affine plane. No equivariant homotopy equivalence or description of induced symmetry representations is asserted. The computational certificate is finite and complete for this ground set, not an infinite-family argument. Publication priority remains provisional because not every potentially relevant full text was accessible. There has been no independent external scientific audit.

## References
1. J. Conant and O. Thistlethwaite, *Boolean formulae, hypergraphs and combinatorial topology*, arXiv:0808.0739, first public version August 5, 2008, later *Topology and its Applications* 157 (2010), 2449–2461. https://arxiv.org/abs/0808.0739
2. A. Lew, *Studies in topological combinatorics*, doctoral thesis, Technion, August 2021, section 1.5, especially Figure 1.1 and Theorem 1.5.2, and the supporting chapter 7. https://www.math.cmu.edu/users/alanlew/files/theses/phd%20thesis.pdf
3. *Mixed-dimensional neighborhood-complex homotopy of the ternary projective nonincidence graph*, publicly available mathematical result, full `RESULT.md` consulted. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-mixed-dimensional-neighborhood-complex-homotopy-of-the-ternary-p--c6098fc06928
4. *Affine-plane incidence Rips complexes have two sphere dimensions*, publicly available mathematical result, full `RESULT.md` consulted. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-affine-plane-incidence-rips-complexes-have-two-sphere-dimensions--3087baeea0a4
