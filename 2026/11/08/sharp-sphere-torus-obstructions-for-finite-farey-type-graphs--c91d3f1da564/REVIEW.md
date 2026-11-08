# Scientific review

## Correctness

**PASS.** The key link lemma follows immediately from the exact two-triangle incidence: each open neighborhood is a disjoint union of cycles. A closed neighborhood with \(k\) or fewer vertices, or a \(k\)-vertex link without triangular components, supplies the obstruction; a triangular link component supplies a four-vertex clique obstruction. This proves the universal minimum-degree inequality. The two Euler edge bounds then give sphere and torus impossibility. Exact icosahedral adjacency forces a unique minimum planar witness, while the quotient triangular lattice avoids chordless cycles of length four and five by a disk Euler argument. The complete small-witness checker returned `ALL_FAREY_BOUNDARY_CHECKS_OK`.

## Originality

**PASS, subject to stated historical-priority risks.** The motivating March 2026 paper gives a planar nonexistence result only at \(\psi_6\), not the sharp \(\psi_4/\psi_5\) boundary or the toroidal \(\psi_5/\psi_6\) boundary with witnesses. The 2025 axiomatization also leaves those finite thresholds open. A previous argument establishes a weaker generic minimum-degree/genus barrier for larger axiom depths, so quadratic genus growth alone is not claimed new. Classical uniqueness of the icosahedron and the Euler formula are credited. The relevant manuscripts and the planar uniqueness paper were inspected at their hypotheses and conclusions. A broader earlier result may still affect priority.

## Mathematical value

**PASS.** The two exact low-genus thresholds address a natural boundary in finite approximations to an infinite graph theory. The optimal twelve-vertex sphere realization and an explicit infinite family of toroidal realizations give both sides of the obstruction, and the two-regular link lemma turns a local logical condition into a uniform degree restriction. The result is more than a generic genus inequality or a small numerical improvement.

## Closest literature and limits

Lockhart, *Pseudofiniteness of the Farey Graph* (arXiv:2603.23900), proves the prior \(\psi_6\) planar barrier and constructs finite high-genus approximants. Mohammadi Khangheshlaghi–Tent (arXiv:2503.02121) establish the axioms. Liang–Wei (2021) record the classical icosahedron neighborhood uniqueness. No claim is made about the exact higher-genus minimum, the smallest toroidal witness, or independent certification of historical priority. The checker confirms finite witnesses but is not a proof of arbitrary-depth assertions.

Self-review: passed. Independent audit: not yet performed.
