# Scientific review

## Correctness

**PASS.** The claimed optimum is proved in both directions, for every integer base at least three and every positive iteration depth. A two-adic gap formula identifies a unique largest gap and the positions of all smaller gaps. The transfer argument places each multi-one factor across a selected canonical gap or the central left boundary, while one-marker and zero-only factors use the two central positions. Pairwise disjoint *all-occurrence supports* of \(k\) explicit factors give a lower bound for \(k\ge3\), and two disjoint supports handle the small depths. The independent standard-library exhaustive checker confirms both obligations on 23 finite instances; these checks are not used to prove the infinite claim.

## Originality

**PASS, with residual bibliographic risk.** The closest work is Cassaigne et al., *New string attractor-based complexities for infinite words* (Example 13 and Theorem 22): it analyzes the ternary word obtained by complementing the symbols of the base-three fixed point and obtains asymptotic logarithmic-order attractor profile. This does not determine the exact minimum attractor of *every* finite morphic iterate for *every* base, nor the explicit optimal position sets and lower-bound witnesses here. Restivo, Romana and Sciortino, *String Attractors and Infinite Words* (2022), develops finite-prefix attractor profiles without the exact formula. Schaeffer and Shallit's automatic-sequence results give general methods rather than this closed all-base characterization. Searches for equivalent formulations, stronger results and exact tables in the inspected primary materials and research records did not find an implication establishing the precise theorem. A currently unindexed or unpublished equivalent remains possible; a search does not establish absolute uniqueness.

## Mathematical value

**PASS.** This is an exact optimum of a natural pattern-covering invariant across an infinite family of fractal automatic words, with an optimal construction valid for every finite iterate. It upgrades the previously known qualitative logarithmic growth to a sharp, base-independent law, and the disjoint-support witness proof isolates the combinatorial mechanism determining the optimum. This is not an arbitrary finite table or a mere restatement of a generic complexity bound.

## Closest references and limits

- Restivo, Romana and Sciortino, *String Attractors and Infinite Words*, arXiv:2206.00376, first public 2022-06-01.
- Cassaigne, Gheeraert, Restivo, Romana, Sciortino and Stipulanti, *New string attractor-based complexities for infinite words*, Example 13 and Theorem 22, https://orbi.uliege.be/bitstream/2268/309672/1/String_attractors__journal_version_%20%282%29.pdf.
- Schaeffer and Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840.

Finite diagnostic verification is neither an exhaustive proof of an infinite statement nor independent external validation. The statement is about morphic iterates, not arbitrary finite prefixes or the entire infinite fixed point as a finite object.

Self-review: passed. Independent audit: not yet performed.
