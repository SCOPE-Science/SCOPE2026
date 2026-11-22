# A mixed-dimensional integral sphere wedge in the full strong Morse complex of \(C_{10}\)

## Finding
Let \(C_{10}\) be the unfilled simplicial ten-cycle and \(\mathcal{SM}(C_{10})\) its **full** strong discrete-Morse matching complex arising from injective vertex filtrations, including all faces of the resulting gradient matchings. Then
\[
\boxed{\mathcal{SM}(C_{10})\simeq S^4\vee S^5\vee S^5.}
\]
This is an integral homotopy equivalence. In particular \(\widetilde H_4\cong\mathbb Z\), \(\widetilde H_5\cong\mathbb Z^2\), and all other reduced integral homology vanishes. The homology ranks are already tabulated in the motivating literature; the new claim is the full homotopy equivalence, proved by a perfect acyclic discrete-Morse matching with a zero **signed integral** attaching matrix.

## Assumptions and scope
The underlying graph has vertex set \(\mathbb Z/10\mathbb Z\), edges \(e_i=\{i,i+1\}\) and no filled two-cell. A strong gradient for a strict filtration of its vertices pairs a vertex with its unique earlier neighboring edge precisely when that vertex has exactly one earlier graph neighbor. A vertex of the complex is one of the 20 possible vertex-edge incidences. Incidence label \(2i\) represents the pair of vertex \(i\) with \(e_{i-1}\), and label \(2i+1\) represents the pair of vertex \(i\) with \(e_i\). A simplex is a subset of one filtration-induced strong gradient. This is not the ordinary Chari–Joswig Morse matching complex and not the pure subcomplex of maximum-dimensional strong matchings. A nonempty face is represented by the sum of powers of two with exponents its incidence labels; this is an exact integer mask, not a numerical approximation.

## Proof
**1. Exact face model.** Orient every graph edge \(e_i\) either forward from \(i\) to \(i+1\) or backward. Such an orientation is induced by an injective ordering of all ten vertices if and only if it is not coherently oriented around the entire cycle: a directed cycle is the only possible directed cycle. For a nonconstant cyclic sign string \((s_0,\ldots,s_9)\in\{+,-\}^{10}\), select incidence \(2i\) when \(s_{i-1}=s_i=+\), and incidence \(2i+1\) when \(s_{i-1}=s_i=-\), with cyclic subscripts. At other vertices, there are either zero or two earlier graph neighbors and no strong matching. Taking the downward closures of all these sets therefore gives the **entire** full strong complex. There are \(2^{10}-2=1022\) acyclic edge orientations producing 1,021 distinct gradient sets and exactly 6,480 nonempty faces, with face vector
\[
(f_0,\ldots,f_7)=(20,160,660,1520,2000,1470,560,90).
\]
The 90 top-dimensional generating gradients have size eight and generate the pure subcomplex of 6,280 nonempty faces. Exactly 200 faces of the full complex are absent from the pure subcomplex: 50 in dimension three, 100 in dimension four, and 50 in dimension five. An independently generated ternary-word model gives exactly the same 6,480 face masks: adjacent nonzero \(+\) and \(-\) entries cannot be opposite, and a monochromatic word must contain two consecutive zeros. The equivalence follows by extending the forced edges to a nonconstant cyclic orientation. Both constructions are implemented from the definitions in the attached checker.

**2. A perfect acyclic face-poset matching.** Order the 20 incidence labels as follows (literal integer indices):
```
9, 7, 14, 12, 6, 2, 5, 10, 11, 15, 16, 13, 0, 4, 3, 1, 17, 19, 8, 18
```
Start with all nonempty faces unmatched. At each label \(b\), match every still-unmatched face \(\sigma\) not containing \(b\) to \(\sigma\cup\{b\}\) if both remain unmatched, then remove the pair. Sorting by integer face mask fixes the implementation unambiguously. This constructs **3,238** valid codimension-one pairs, leaving precisely four critical faces, encoded by masks
```
512             dimension 0
297032          dimension 4
328788          dimension 5
690216          dimension 5
```
A complete acyclicity check constructs all **31,840** nonempty face-poset covers. Each unmatched cover is directed downward, while each matched cover is reversed. Topological sorting visits all 6,480 vertices of this directed graph and finds no directed cycle. The verification is exhaustive, so Forman's theorem gives a CW complex with one zero-cell, one four-cell, and two five-cells, and no other cells.

**3. The signed integral attaching differential.** Use the increasing incidence-label order to orient every simplex. For each matched lower-dimensional four-face \(\sigma\) with paired five-face \(\tau\), signed elementary cancellation eliminates \(\sigma\) using the relation
\[
[\sigma]=-[\sigma:\tau]^{-1}\sum_{\substack{\rho\subset\tau,\ \dim\rho=4\\\rho\ne\sigma}}[\rho:\tau][\rho],
\]
where each bracketed incidence is \(+1\) or \(-1\). Four-faces paired downward to three-faces project to zero; the unique critical four-face projects to its own generator. The acyclic matching makes this recursive integer projection terminate. Applying it to the oriented boundaries of the two critical five-simplices yields, **over the integers**, the exact Morse boundary matrix
\[
\partial^{\mathrm M}_5=\begin{pmatrix}0&0\end{pmatrix}.
\]
This is recomputed by `verify_strong_c10.py` using signed simplicial incidence coefficients, not inferred from mod-two homology or a rank-only experiment. All other positive-dimensional Morse boundaries have zero target groups, hence vanish.

**4. Homotopy conclusion.** The resulting CW four-skeleton is \(S^4\), with a unique basepoint, and the two five-cells are attached along maps \(S^4\to S^4\). Since \(\pi_4(S^4)\cong\mathbb Z\) is classified by degree, each attaching map has degree exactly its signed cellular incidence coefficient. The matrix above is zero, so both attaching maps are nullhomotopic. Attaching them gives precisely \(S^4\vee S^5\vee S^5\), proving the boxed integral homotopy statement.

## Verification
Run `python3 verify_strong_c10.py` with Python 3 and its standard library. The program independently generates the full complex (a) from all 1,022 nonuniform edge orientations, and (b) from all \(3^{10}\) ternary sign words, and asserts exact set equality. It checks the entire listed coordinate-toggle matching, every Hasse incidence, global directed acyclicity, all four critical masks, and the two entries of the signed **integer** Morse differential. In an independent calculation from the original full simplicial chain groups, it reduces all boundary matrices over \(\mathbb F_2\), obtaining reduced ranks one in degree four and two in degree five. `VERIFY_EXPECTED.txt` stores its complete deterministic successful stdout. The standalone program has no external input, packages or network dependencies.

Finite exhaustive computation establishes this specific finite homotopy type because it inspects *every* simplex and every face-poset incidence and, together with Forman's theorem and the degree classification, constitutes a complete proof. It is not claimed to establish any infinite-family behavior.

## Relationship to prior work
Knudson and Owens-White [1] introduce \(\mathcal{SM}\), classify the **pure** strong cycle complexes, and list **homology** of the **full** complexes through 21 vertices. In their Introduction and Section 8, they explicitly distinguish homology from homotopy for the full cycle construction. Their Table 1 already displays the free homology ranks of the ten-cycle using a sphere-wedge shorthand, which **does not assert or imply a full homotopy equivalence**. Our four-critical-cell acyclic certificate and signed zero integral differential resolve this stronger topological question for the ten-cycle.

At ten vertices, the same original paper proves that the **pure** strong subcomplex has homotopy type \(S^2\vee S^5\vee S^5\), whereas the 200 extra full-complex faces change the small sphere to \(S^4\) while preserving the two top-dimensional sphere classes. That change is verified by independently computing the pure subcomplex and its mod-two Betti ranks, and the pure homotopy type is credited to the published theorem. The earlier published all-length classification [2] likewise determines integral **homology** of full strong cycle complexes, not their attaching maps or homotopy types. The exact full homotopy equivalence for the nine-cycle [3] concerns one lower cycle length, where the critical cells are exclusively four-dimensional, and does not imply this mixed-dimensional result. Ordinary Morse matching complexes and the pure strong subcomplex are different constructions, so their wedge formulas do not cover the claim.

## Limitations
The result concerns only the full strong matching complex of the unfilled ten-cycle. It does not classify the full complex at every cycle length, determine symmetry representations or higher operations for larger lengths, or provide a simplicial collapse directly onto a wedge. The result is proved by exact combinatorial enumeration and a mathematical discrete-Morse argument; independent mathematical audit has not been performed. The priority comparison cannot exclude unpublished or unindexed equivalent results.

## References
[1] Kevin P. Knudson and Abigail Owens-White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1, first publicly available 2026-09-06, Definition 4.2, Introduction, Section 8, and Table 1, https://arxiv.org/abs/2609.06844 ; lawful full-text mirror https://borowiecki.dev/pdf/2609.06844 .

[2] *Uniform integral homology of full strong Morse matching complexes of cycles*, public research record, 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-uniform-integral-homology-of-full-strong-morse-matching-complexe--43f58158c288 .

[3] *Integral homotopy type of the full strong Morse matching complex of the nine-cycle*, public research record, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-integral-homotopy-type-of-the-full-strong-morse-matching-complex--e87f9e9fd5ee .
