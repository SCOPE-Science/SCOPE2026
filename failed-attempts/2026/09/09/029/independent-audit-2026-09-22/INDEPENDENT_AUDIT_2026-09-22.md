# Independent audit — 2026/09/09/029

Date: 2026-09-26. Disposition: failed; complete original package archived.

## Correctness — PASS

I independently generated all 13 points of (PG(2,3)) and all (inom{13}{7}=1716) seven-point subsets. For each subset I computed its 35 determinant-zero triples over GF(3) and compared the resulting labeled matroid with the full permutation orbits of the 23 stored line families. The latter orbits contain 8,389 distinct labeled rank-three types, matching the census. Exactly four of these types occur among projective subsets: stored types 18, 19, 20, 21, with subset frequencies 936, 78, 234, 468. I separately generated all 5,616 elements of (PGL_3(3)); each type's subsets form one orbit, of the same respective sizes, and their stabilizers have orders 6, 72, 24, 12, exactly the stated matroid automorphism orders. Thus every automorphism lifts projectively and the labeled and geometric representation multiplicities equal one. This independent route checks the material finite claims without relying on the candidate's basis-frame search.

## Originality — FAIL

The candidate calls the four-way unique-representation result a new boundary and says Geelen–Whittle offer only a finiteness bound. Their full, openly available 2013 paper states on page 2 of its introduction that *all* ternary matroids are uniquely representable over GF(3), with no connectivity or seven-point restriction. Whittle's 1995 paper likewise states that fact. The candidate's central multiplicity-one theorem and degenerate maximizer are immediate instances of this prior theorem. Mayhew–Royle also catalogued all simple matroids of this size, so the 23-type count is prior census material. Explicit four matrices and a cross-indexed small slice may be convenient, but do not restore originality to the stated uniqueness finding.

## Scientific value — FAIL

The motivating uniqueness-versus-multiplicity boundary does not exist over GF(3): the general prior theorem fixes multiplicity to one for every ternary matroid. The residual four-row classification and matrices are a small catalogue extraction, without a new invariant or structural consequence established by this record. They may be useful as test data, but do not support the claimed research value.

## Primary sources

- Geelen and Whittle, *Inequivalent Representations of Matroids over Prime Fields*, Advances in Applied Mathematics 51 (2013), author-hosted full text, p. 2: https://www.math.uwaterloo.ca/~jfgeelen/Publications/prime.pdf
- Whittle, *A characterization of the matroids representable over GF(3) and the rationals* (1995), author-hosted full text: https://homepages.ecs.vuw.ac.nz/~whittle/pubs/matroids_representable_over_GF%283%29_and_rationals.pdf
- Mayhew and Royle, *Matroids with nine elements*, arXiv:math/0702316: https://arxiv.org/abs/math/0702316
- Candidate `RESULT.md` and `artifacts/full_census.json`; independent projective point, subset, permutation and (PGL_3(3)) enumeration above.
