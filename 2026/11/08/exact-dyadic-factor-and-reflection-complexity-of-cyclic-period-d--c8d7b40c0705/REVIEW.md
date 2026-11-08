# Review of exact dyadic factor and reflection complexity

## Correctness

**PASS.** For every modulus \(m\ge2\) and dyadic length \(L=2^k\), the unique multiple of \(L\) in a factor's index interval yields a complete template parameterization \((j,c)\). Every parameter occurs, using a sufficiently large power of two with prescribed valuation residue. If two centers differ by a distance with valuation below \(k-1\), a witness offset of the next valuation distinguishes the templates modulo every \(m\ge2\); centers opposite by \(L/2\) collide exactly at residue \(k-1\). Reversal closure follows by reflection in a sufficiently large power of two. The even-palindrome obstruction and orbit counting then prove the advertised formulas. Finite tests validate all collision classes for 56 parameter pairs; they do not substitute for the uniform proof.

## Originality

**PASS (best-knowledge, with residual bibliographic risk).** The relevant 2024 reflection-complexity paper calculates the classical binary period-doubling case and supplies general automatic-sequence algorithms, but its inspected Section 6.2 does not state the \(m\ge3\) exact formulas or the two-center collision classification. The 2022 generalized period-doubling palindrome article and the 2025 generalized kernel/gap-factorization article supply different structural information, not the enumerated reversal orbit classes. The 2026 group-antimorphism paper addresses a generalized group action largely for binary examples. The novelty claim is restricted to the natural \(m\ge3\) all-modulus dyadic family, with the known binary answer reported solely for consistency. Residual risk: a related older generalized-period-doubling publication may contain an equivalent complexity formula that was not indexed or accessible in full.

## Mathematical value

**PASS.** Reflection complexity is a recognized invariant distinguishing factor languages modulo reversal, and cyclic period-doubling substitutions constitute a natural two-parameter family. The exact all-scale dyadic orbit counts and complete parameter-collision classification explain the sharp factor loss and its reversal structure, moving beyond algorithms, numeric tables, and the previously worked binary case. The dyadic restriction is motivated by the constant-length substitution, not a gratuitous slice. No result is asserted for arbitrary lengths.

## Limits and closest literature

The result is not an independent scientific validation and has no claim to solve full-length complexity. Relevant literature: Allouche–Campbell–Li–Shallit–Stipulanti (arXiv:2406.09302, Section 6.2), Barro–Kaboré–Bognini (Australasian Journal of Combinatorics 83(3), 2022), Bognini–Ammar (arXiv:2511.20881), Blažek–Dvořáková–Pelantová (arXiv:2610.14637). A 2020 generalized substitution factorization paper was identifiable bibliographically, but full-statement comparison remained an accessibility risk.

Self-review: passed. Independent audit: not yet performed.
