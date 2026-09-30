# Independent Audit — 2026/09/13/064

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `34e7462274e04c65b82fd405784a9964ae9072d6`
- Disposition: **FAILED**

## Correctness

**PASS** — The Tietze/HNN computation is correct. Introducing d=a b a^{-1} rewrites the relator as (d b^2 c^3)^3 and gives the stated HNN presentation. The homomorphisms from the base group to Z with coefficients (1,1,-5) and (1,-1,1) annihilate the base relator while taking b and d respectively to nonzero integers, so both associated cyclic subgroups are infinite. The a-exponent homomorphism on G2 proves the stable letter is not contained in the base, and Bass-Serre/Britton theory then makes the splitting nontrivial.

## Originality

**FAIL** — The construction is a direct instance of the classical Magnus-Moldavanskii HNN rewriting for a cyclically reduced one-relator group whose relator has exponent sum zero in a generator. McCool-Schupp explicitly present this observation: such a group is an HNN extension of a one-relator group with shorter defining relator. Here the a-exponent sum is zero and the displayed substitution d=a b a^{-1} is exactly that elementary rewriting. The integer maps certifying infinite cyclic edge groups are useful bookkeeping but do not constitute a new splitting mechanism.

## Scientific value

**FAIL** — The record resolves one deliberately chosen presentation by a single textbook Tietze move and does not compute the JSJ, prove a family theorem, or introduce a new invariant or algorithm. As a worked example it is correct, but its mathematical content is too close to the classical one-relator HNN method to support an independent research finding.

## Sources

- On one relator groups and HNN extensions (James McCool; Paul E. Schupp): https://doi.org/10.1017/S1446788700014300 — States the classical Moldavanskii observation that a cyclically reduced one-relator group with zero exponent sum in a generator is an HNN extension of a one-relator group with shorter relator.
- The JSJ-decompositions of one-relator groups with torsion (Alan D. Logan): https://arxiv.org/abs/1412.5357 — Broader JSJ background; it does not make this elementary HNN specialization original.

## Limitations

- The audit does not claim that the exact presentation is printed verbatim in McCool-Schupp.
- Failure is on originality and scientific value; the explicit splitting itself is accepted as correct.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence. Open-access/preprint sources were checked first; Oxford Download was not needed.
