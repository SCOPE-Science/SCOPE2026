# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A power-operation plus trace-protected gamma-family permanent cycle on V(1) at p=7
- **Round:** 2026-09-07-first-light-01
- **Lane:** 378
- **Disposition:** NO_RESULT
- **Domain:** Stable Homotopy Theory
- **Method:** Adams-Novikov differential analysis with BP power operations and trace-method K-theory comparison

## Problem

Decide one Adams-Novikov bidegree on a height-2 Smith-Toda complex at a prime >=5 by overlapping a BP power-operation constraint with a trace-method vanishing line: either force a new permanent cycle extending the collapse range for one Toda-bracket (gamma) family, or isolate the exact power-operation relation that kills it.

## Attempted claim

At prime p=7, in the Adams-Novikov spectral sequence for the Smith-Toda complex V(1), the E_2 class x_2 in bidegree (s=2, t=1370) representing the second gamma-family element survives all differentials d_r for r>=3 (hence is a permanent cycle), extending the known collapse range for the gamma family on V(1) at p=7 from t=1 to t=2; the witness is an explicit check that each candidate d_r target vanishes either by a stated BP power-operation relation or by the imported V(1)-homotopy TC(BP<1>) vanishing line.

## Research outcome

Target permanent-cycle claim at (p=7,V(1),s=2,t=1370) is non-viable as stated: the source E2 group is provably zero by standard 12-sparsity (chain-level census: 0 monomials), so no nonzero x_2 exists to protect; the r-in-[3,9] audit window is vacuous with first threats at r=11,23,... outside it; both witness inputs (BP operation relation, TC vanishing line) are unstated and not derived. Exact admitted fallback also unsatisfiable: branch (i) needs a nonzero class to kill; branch (ii) conjunctively requires a transferable BP power-operation vanishing lemma, which was not derived (only grading sparsity). No CLAIMED result; obstruction dossier preserved in WORKLOG/verify.py.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['E2^{2,1370}(V(1))=0 proved by standard ANSS sparsity (q=12 does not divide t=1370) plus from-scratch cobar monomial census (0 monomials at T=1370 vs 26846 at T=1368 and 27892 at T=1380 controls); robust across 8 stem/cell-shift re-readings (residues 2,3,4,5,6; 0 absent).', "All d_r targets r in [3,9] land in sparsely-zero bidegrees (vacuous window); first possibly-nontrivial threats at r=11 mod 12 (r=11,23,...) lie outside the audit window; 'all r>=3' additionally needs infinitely many pages (finite head 14-118 depending on unstated vanishing line; plan covers 0).", 'Both named witness inputs unstated in-topic and not derivable in-session: no explicit BP power-operation relation; no TC(BP<1>) vanishing-line equation. Cited TC literature gives v2-periodicity (non-vanishing) in this stem range, opposite direction to a vanishing import.', 'Honest Bockstein correction logged: v2-Bockstein lift of [v3^2] lands at (s,t)=(1,1272) stem 1271 (degree shift -|v2|=-96), not near (2,1370); no gamma_t locus (t=1,2,3) matches the stated bidegree. Reaching it would change the admitted claim and is prohibited.', 'Fallback branch (ii) collapse half holds only vacuously (E_r=0 throughout window); power-operation-lemma half absent. Per instructions, a vacuous half-result plus relabeled sparsity is not submitted as the admitted fallback.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['E2^{2,1370}(V(1))=0 proved by standard ANSS sparsity (q=12 does not divide t=1370) plus from-scratch cobar monomial census (0 monomials at T=1370 vs 26846 at T=1368 and 27892 at T=1380 controls); robust across 8 stem/cell-shift re-readings (residues 2,3,4,5,6; 0 absent).', "All d_r targets r in [3,9] land in sparsely-zero bidegrees (vacuous window); first possibly-nontrivial threats at r=11 mod 12 (r=11,23,...) lie outside the audit window; 'all r>=3' additionally needs infinitely many pages…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
