# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A thin-but-not-quasi-alternating certificate in the 11-12 crossing window via branched-cover lattice obstruction where homology thickness fails
- **Round:** 2026-09-07-first-light-01
- **Lane:** 121
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Low-Dimensional Topology
- **Method:** branched double-cover definite-4-manifold lattice-embedding obstruction with Heegaard Floer correction terms via Turaev torsion (Greene-Watson route)

## Problem

Fix one nominated homologically thin (Khovanov-thin and HFK-thin) QA-unresolved knot Kstar with 11-12 crossings from the open-candidate list in Jablan Tables of quasi-alternating knots (arXiv:1404.4965, building on arXiv:0901.0075), where homology thickness provably gives no obstruction, and decide its QA status by a beyond-thickness certificate.

## Attempted claim

Prove that the nominated homologically thin knot Kstar (11-12 crossings, QA-unresolved in Jablan Table 2 of arXiv:1404.4965, Khovanov-thin and HFK-thin so thickness obstructions vanish) is not quasi-alternating, by certifying that its branched double cover admits no negative-definite 4-manifold filling of the type required for QA links: exhibit the Goeritz lattice of Sigma(Kstar), prove by finite lattice-embedding search that no compatible embedding exists, and confirm incompatibility with Heegaard Floer correction terms computed via Turaev torsion, with all matrices and invariants logged from committed diagram codes.

## Research outcome

Consolidated interrupted lane to a verified partial theorem: certified 6-entry Lost-table audit with 12n397 ambiguity flag, plus a sound-complete exact-integer lattice-embedding decision procedure with passing tests. Full non-QA certificate for Kstar was NOT closed and is explicitly not claimed.

## Why this attempt failed

Failed axes: originality, value.

originality: No new mathematical fact or method beyond textbook/folklore and transcription. Lemma N is standard linear algebra (rank inequality, sum-of-squares diagonal, Hadamard inequality, square determinant) and the draft itself states 'The method is standard; our contribution is only the certified packaging.' Theorem S is a correctness statement about a straightforward norm-shell + backtracking brute-force enumerator, not a new decision-theoretic result; equivalent finite enumeration is the obvious complete procedure for MM^T=P. Demo lattices (1x1 [2], A2, [[3,1],[1,3]]) are canonical textbook pattern examples with no knot linkage by the draft's own admission. Proposition A is a verbatim transcription audit of six labels/Conway strings from the committed Jablan source, i.e. database confirmation, not a classification closure. Nearest priors subsume the content: Greene 0906.2222 and Greene-Watson 1106.5559 already establish the branched-cover definite-manifold + correction-term route; Manolescu-Ozsvath 0708.3249 QA-implies-thin; Jablan 1404.4965 already tabulates the six Lost candidates as unresolved; Qazaqzeh-Chbili 1406.0279 already delimits the Q-degree obstruction. Nothing closes, extends, or restates these in a non-obvious way. value: Independently not worth finding later under STANDARD axis 3. The admitted topic required deciding QA status of one nominated thin 11-12 crossing Kstar via Goeritz lattice embedding plus d-invariant/Turaev-torsion incompatibility (or symmetric QA-tree closure plus subfamily lemma). None of that was delivered: no Goeritz matrix from any diagram/DT code, no correction terms, no embedding impossibility for any knot, no QA tree, no exclusion lemma. The remaining artifacts are (a) a six-row table transcription with an unresolved 12n397 ambiguity and (b) a small-norm brute-force enumerator demonstrated only on 1-2 dimensional pattern matrices. The draft explicitly states 'No QA status of any knot is decided here' and 'the numbers carry no knot consequences.' This is scaffolding, textbook restatement, and database repackaging, explicitly excluded as sufficient (recomputed width/table checks, implementation logs, failed-search packaging). It does not advance the recognized thin-vs-QA boundary and would not be citable as a classification fact in Floer/categorification work.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: ['No Goeritz matrix was built from any committed diagram or DT code.', 'No d-invariant / Turaev-torsion computation was performed.', 'No knot QA status (non-QA or QA tree) is decided; demo lattices are pattern-scale only with no knot linkage.', 'Unresolved source ambiguity: 12n397 listed with differing Conway strings (-2 1 0 vs -2 -1 0) in text vs Lost table.', 'Embedding search enumerates norm shells by bounded product scan: practical only for small rank and small diagonal entries; no scaling…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
