# Independent Audit — Torsion-lift criterion and Henselian classification for commutative generalized quasi t-fine rings

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `c7cc5481aa328dcfc80ba6c998864b884bcb041a`  
**Audited current source tree:** `c7cc5481aa328dcfc80ba6c998864b884bcb041a`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** failed

The current `main` record path is unchanged from the dispatcher's source-check commit, so the audited tree is the assigned source tree. GitHub was used read-only. The dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASSED

PASS. In a commutative ring, quasinilpotents equal the Jacobson radical, so generalized quasi t-fineness forces every element outside J to be a unit and makes the ring local; reduction modulo J then shows that every nonzero residue class has a torsion-unit lift, and conversely such lifts give the required decomposition. A field with torsion multiplicative group is algebraic over a finite prime field, hence locally finite. In a Henselian local ring with locally finite residue field, every nonzero residue element has finite order n prime to the residue characteristic and is a simple root of X^n-1, so Hensel lifting gives a torsion-unit representative. The classification Z_(p) iff p=2 or 3 follows because its only rational roots of unity are ±1, while Z_p is Henselian for every p.

## Originality — FAILED

FAIL. The assigned record is substantively duplicated by the earlier same-day SCOPE record `2026/09/19/henselian-residue-criterion-generalized-quasi-t-fine-rings--80fd65831087`, published at 2026-09-19T02:22:08Z, whereas the assigned record's metadata gives 2026-09-19T17:31:51Z. The earlier record already proves the torsion-lifting criterion, the commutative Henselian iff locally-finite-residue classification, the exact Z_(p) versus Z_p boundary, and in fact a stronger all-size mixed-characteristic matrix obstruction. The assigned package therefore does not constitute an original archive finding.

## Scientific value — FAILED

FAIL AS A DISTINCT ARCHIVE CONTRIBUTION. The mathematics is clean and useful, but essentially all substantive claims are already present in the earlier SCOPE record, which additionally treats arbitrary local rings in the torsion-lifting step and proves a stronger matrix obstruction. Maintaining this later subset as a separate validated finding adds duplication rather than scientific coverage.

## Independent checks

- Reproved the commutative torsion-lifting criterion and the Henselian lifting argument independently.
- Rechecked the Z_(p) and Z_p classification directly from roots of unity and Hensel lifting.
- Fetched and compared the earlier SCOPE record `henselian-residue-criterion-generalized-quasi-t-fine-rings--80fd65831087` in full; its theorem statements and proofs subsume the assigned record's main results.
- Verified the earlier record's metadata timestamp is 2026-09-19T02:22:08Z and the assigned record's is 2026-09-19T17:31:51Z, establishing internal archive priority.
- Compared with the motivating arXiv source, whose public abstract introduces generalized quasi t-fine rings but does not itself state the Henselian classification.
- Verified no files under the assigned record changed between the dispatcher source-check commit and current main, and verified both dated independent-audit files and FAILED_ATTEMPT.md are absent.

## Limitations

- The failure is solely an originality/scientific-value judgment; the audited commutative statements are mathematically correct.
- No claim is made that the motivating arXiv authors had previously published the Henselian criterion; the decisive prior art here is the earlier SCOPE archive record.
- Relocation preserves the complete original package for provenance.

## Evidence and references

- https://arxiv.org/abs/2609.19882
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/henselian-residue-criterion-generalized-quasi-t-fine-rings--80fd65831087
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/torsion-lifts-commutative-quasi-t-fine-rings--101da94a3acc

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
