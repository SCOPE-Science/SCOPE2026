# Independent audit — SCOPE-20260909-082

Audited at: 2026-09-30T23:18:42Z

Disposition: **failed**

## Correctness

**PASS** — Fresh rank computations from the explicit eight-column binary cube reproduce the three stabilizer orbits on possible new columns with sizes 1, 8 and 7. Independent base counts and separator scans reproduce 56/84/88 bases, beta invariants 0/6/7, and the connectivity verdicts; the literal rank-5 coextension construction has the same three orbit types and no internally 4-connected member.

Sources/evidence:
- Actual package verify_cell.py and verify_coext.py at the audited source revision.
- Fresh independent GF(2) rank/base/separation computation from the explicit matrix.

Residual risks:
- The exact finite invariants are correct, but that does not establish originality or standalone scientific value.
## Originality

**FAIL** — Mayhew–Royle explicitly computed a catalogue containing all matroids with up to nine elements. Every nine-element single-element extension/coextension in this record lies inside that stronger complete prior universe. The three column orbits are also immediate from the AGL(3,2) stabilizer action on the 16 vectors. The beta and connectivity columns are mechanically computable invariants of those already-covered nine-element matroids. Under implication-based originality, absence of an identical printed three-row table does not restore novelty.

### Originality comparison details

**Equivalent formulations.** The record’s objects are specific nine-element matroids, so a complete catalogue is a stronger equivalent coverage source even if labels differ.
- Mayhew–Royle state that their catalogue contains all matroids with up to nine elements.

**Broader coverage.** A complete universe-level classification strictly dominates the three-object extension cell.
- The 2007 paper describes a complete catalogue and associated data for all matroids up to size nine.

**Exact database or table.** Known-database recomputation is specifically excluded by the value/originality bar.
- The prior work stores the classified matroids and associated data in an online database; exact naming of these three rows was not needed for coverage.

**Claim versus prior implication.** The final claim is a narrow extracted table from stronger prior coverage.
- Every object in the record has nine elements, so it is already an element of the prior complete catalogue; beta and connectivity follow by routine invariant computation.

### Source inspections
- **Matroids with nine elements** — COVERING. Material read: Full HTML/abstract and catalogue description. Evidence: The authors describe a catalogue containing all matroids with up to nine elements and associated data.

Originality residual risks:
- No access issue affects the decisive complete-catalogue coverage.
## Scientific value

**FAIL** — Once the complete nine-element catalogue and elementary stabilizer-orbit description are accounted for, the three-row table is a known-universe recomputation. The beta values and separator verdicts are reproducible and useful as checks, but they do not isolate a previously unknown motivated invariant or structural boundary.

Sources/evidence:
- Mayhew–Royle complete nine-element catalogue.
- AGL(3,2) acts with the three elementary vector orbits used by the package.

Residual risks:
- The table can remain useful pedagogically or as a regression test, but that is below the stated scientific-value threshold.

## Limitations

- Correct finite table but scientifically covered by stronger prior enumeration.
