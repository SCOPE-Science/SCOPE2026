# Scientific review: parallel-line two-gate entropy loss

## Correctness — PASS

The claim quantifies over every finite affine plane of odd order \(q\ge3\), including non-Desarguesian planes. The proof uses only affine-plane axioms: \(BB^{\mathsf T}=I+J\), the odd line size to establish injectivity of \(B^{\mathsf T}\), and equal-parity sums across parallel classes to characterize possible one- and two-line row-codewords. For any omitted set of at most two distinct incidences, it proves both necessity and sufficiency of the distinct-parallel-lines condition, and uniqueness of the single rank-deficiency direction. The graph-state cut-rank and flat-spectrum facts are taken from the foundational literature. The random-pair count follows from an exact disjoint-line enumeration. The standalone checker passed all prime-order cases \(q=3,5,7\) and a finite-field order-nine sample; this verifies sample instances and does not stand in for the all-order proof.

## Originality — PASS on examined evidence, provisional

The closest examined prior exact fault law concerns even-order **projective** planes. It begins from a deficient square point-line incidence matrix and classifies *entanglement gain* up to \(q+1\) omission matching gates. The current theorem instead concerns rectangular **affine** incidence, odd-order full-row rank, and a two-gate **loss** iff the line endpoints are parallel. Neither its two-fault equivalence nor its exact probability is implied by that projective theorem as stated. Hein–Eisert–Briegel supplies the general rank rule and one-edge bounds, not this geometric comparison. Severini discusses maximal bipartite graph-state entanglement but not the inspected affine-plane omission configuration. The odd-order projective-plane matching-law record in the comparison set also does not automatically transfer to an affine incidence matrix formed by deleting a whole line at infinity and its points. Affine incidence-code facts are classical and specifically credited. Directly equivalent specialized binary-matrix results could exist outside the searched literature; historical uniqueness is not claimed.

## Mathematical value — PASS

The natural observable is the complete point-versus-line entanglement across a geometry-based many-qubit resource. The result pinpoints the first possible size of a gate-omission set that degrades initially maximal entanglement and classifies **every** placement at that sharp size, including errors on nonincident vertices separated by arbitrary geometric position. Its exactly computable rare-event probability describes how susceptibility decreases in larger incidence networks. The all-order affine-plane conclusion does not depend on coordinatization; it is more than a small-system enumeration. These are concrete robustness and geometry consequences rather than a change of notation or an arbitrary slice of a larger known table.

## Closest sources and limitations

The principal comparison sources are Hein–Eisert–Briegel (arXiv:quant-ph/0307130), Severini (arXiv:quant-ph/0511147), and the public 2026 even-order projective-plane incidence-matching theorem. The affine-code publication of Ghinelli–de Resmini–Key was checked at abstract level only and is a residual historical search risk. The theorem is restricted to ideal graph states, exact gate omissions of size at most two, the complete point/line cut, and odd-order affine planes. The exact probability assumes uniform selection of two distinct omitted incidences.

Self-review: passed. Independent audit: not yet performed.
