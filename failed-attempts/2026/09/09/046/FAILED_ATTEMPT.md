# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A C2-Mahowald transfer differential on a type-2 (generalized V(1)) class in stem 34
- **Round:** 2026-09-07-first-light-01
- **Lane:** 395
- **Disposition:** NO_RESULT
- **Domain:** Stable Homotopy Theory
- **Method:** chromatic Adams-Novikov spectral-sequence analysis with C2-equivariant Mahowald-root-invariant transfer

## Problem

Use the C2-equivariant Mahowald (root-invariant) filtration together with the low-stem Adams-Novikov chart and the algebraic tmf-resolution as a cross-check to prove a new Adams-Novikov differential, or a permanent-cycle obstruction, for a height-1 telescopic class on a finite type-2 (generalized V(1)) complex in stems 30-45.

## Attempted claim

Let X be the standard 2-primary finite type-2 complex fixed in the audit plan (generalized V(1), e.g. the Beaudry-Behrens-Bhattacharya-Culver-Xu complex Z). In the 2-primary Adams-Novikov spectral sequence for X, the E2 class x in bidegree (stem 34, filtration 2) specified in the audit plan supports the nontrivial differential d3(x) = y, where y is the specified nonzero class in bidegree (stem 33, filtration 5); in particular x is not a permanent cycle and its telescope class does not survive at height 1.

## Research outcome

Target ANSS d3 (34,2)->(33,5) on 2-primary type-2 Z pursued for the full directed phase and found unclosable: (1) no cited source computes unlocalized ANSS E2 of Z at either bidegree (BE20b gives only the BP_*Z comodule + localized HFPSS; Beaudry et al. give the good/tmf picture + E(2)-local collapse; MRW-type charts are odd-primary V(1)), so the 'specified' classes x,y reduce to bare bidegrees with no cocycle names; (2) the C2-Mahowald transfer input is missing mathematics, not computation (classical invariants to stem 26 only; C_{p^n} values Burnside-only; survey-level redshift precedent; spherical-vs-Z-coefficient mismatch), and the transfer template's own tmf leg points the wrong way for y; (3) a direct normalized BP-cobar implementation failed self-consistency testing (d^2=0), root-caused to a basis bug (v2-powers need mixed slot monomials), confirming the Ext computation is machine-scale (C^5_38 lower bound ~2.1e5). Positive partial inventory secured but below any claim bar: d3 bidegree legal (audit-plan '(-1,+2)' corrected to (-1,+3)); May-Ravenel E1 enumeration gives a unique v2-torsion good candidate at (34,2) (v2^2 h_{2,1}^2, name ±1-convention-sensitive) and EMPTY at (33,5) robust to ±1 shifts with all neighboring competitor slots empty; collapse-compatibility holds automatically (loc(y)=0: localized (33,5) empty by rank-4 exterior cap, Thm 8.5.1 unthreatened). The revealed preset fallback (nonzero tmf-Hurewicz image h_tmf(x)!=0) is literally unsatisfiable: Hurewicz applies to homotopy classes while x's own E2 occupancy is unverified, and no established sub-fact was relabeled to meet its exact criterion. No emergent finding met the independent-value bar; nothing CLAIMED.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['Unlocalized ANSS E2 of Z at (stem 34, filt 2) and (stem 33, filt 5): occupancy, cocycle names, and the ANSS differential all remain OPEN; no cited paper computes these groups.', 'C2-Mahowald transfer lemma (T1)-(T3) recorded as an open template with (T1),(T2) unproved and (T3) evidence-negative for y; not a result.', 'May-Ravenel E1 enumeration uses standard Ravenel stem conventions (|h_j,0|=2(2^j-1), |h_j,1| doubled, |v2|=6); the (34,2) candidate NAME is ±1-convention-sensitive (v2^2 h21^2 vs v2^2 h30 h21 vs v2 h30^2); the (33,5)-empty verdict is robust to ±1 shifts.', 'Classical ASS occupancy at (33,5) from Beaudry Fig 8.5 left chart UNRESOLVED (rendering too dense); not used as evidence.', 'BP-cobar scale counts (C^2_36=3058, C^5_38=212564) are corrected LOWER bounds (mixed v2/t slot monomials excluded); only the infeasibility-scale conclusion is relied upon.', 'tmf-resolution E1 occupancy claims at (35,1)/(34,2) (good v2^4 e h21 cycle; h40-family parsing; evil side) are supporting sketches with open items, not lemmas; the tmf-ASS (t-n,n) vs ANSS (t-s,s) filtration distinction was maintained and no cross-SS inference was drawn from them.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['Unlocalized ANSS E2 of Z at (stem 34, filt 2) and (stem 33, filt 5): occupancy, cocycle names, and the ANSS differential all remain OPEN; no cited paper computes these groups.', 'C2-Mahowald transfer lemma (T1)-(T3) recorded as an open template with (T1),(T2) unproved and (T3) evidence-negative for y; not a result.', 'May-Ravenel E1 enumeration uses standard Ravenel stem conventions (|h_j,0|=2(2^j-1), |h_j,1| doubled, |v2|=6); the (34,2) candidate NAME is ±1-convention-sensitive (v2^2 h21^2 v…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
