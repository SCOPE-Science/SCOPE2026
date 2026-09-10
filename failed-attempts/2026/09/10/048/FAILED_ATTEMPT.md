# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Toda-bracket decision of a contested V(1) Adams d2 at prime 3: survival witness or chart-correcting obstruction
- **Round:** 2026-09-07-first-light-01
- **Lane:** 617
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Stable Homotopy Theory
- **Method:** Adams differential tracking with Toda-bracket juggling and motivic comparison

## Problem

Decide one contested 3-primary classical Adams differential on the finite Smith-Toda complex V(1): for the E2 class x in stem 34, Adams filtration 6 (lowest unresolved d2-source in stems 32-40 per Ravenel/Shimomura V(1) Ext chart, linked by Moss to Theta=<alpha1,alpha1,beta1>-type bracket), prove either survival (permanent cycle) via a new Toda-bracket juggling argument with logged Moss-convergence check and motivic comparison, or a certified killing differential plus hidden-extension obstruction that corrects the published stem chart.

## Attempted claim

In the 3-primary classical Adams SS for V(1), let x be the pinned E2 class in (t-s,s)=(34,6) (documented May cocycle; Research logs any chart-label correction): decide d2(x). Either (A) d2(x)=0 and the linked Toda bracket Theta contains an element detected in filtration <=6 witnessing survival to E3, or (B) d2(x)=y!=0 with explicit nonzero target and certified hidden-extension obstruction; output (A) or (B) with May log, Moss crossing-differential check, and motivic-comparison map.

## Research outcome

Machine-checked May-Steerod foundation at p=3 to stem 40 (validated sphere May E1/d1/E2 window with anchors) plus a certified a0*h10 obstruction to the naive V(1)-twisted May SS and a measured infeasibility census; target d2 and fallback E3 survival NOT claimed.

## Why this attempt failed

Failed axes: correctness, value.

correctness: HEADLINE vs EVIDENCE. The emergent claim has four components; two verify, two fail. (1) May E1 core REPRODUCED: re-running inputs/artifacts/may_window.py gives 517 E1 monomials, d1^2=0 on single-generator monomials, anchors E2(1,1)=E2(1,4)=E2(2,12)=1; my independent reimplementation of the E1 enumeration (same stated conventions) confirms n_E1=517 and spot E1 counts E1(1,5)=1 ({a1}), E1(2,5)=1 ({a0*h10}), E1(6,40)=7, E1(8,41)=6. (2) H^*V(1)/Steenrod low-degree checks REPRODUCED: check_ext.py exits 0 with Poincare dims 0..9 = 1,1,0,0,1,2,1,0,1,2, matching my independent admissible-basis enumeration to degree 12. (3) CENSUS FALSE (headline component): enumerate.py claims 1,552,353 admissible monomials of degree<=41 with dim A_40=328,962, dim A_41=473,119. Its is_adm() has `return True` indented INSIDE the `while i<n:` loop (inputs/artifacts/enumerate.py line 55), so only the first factor-block is ever checked (demonstrated: the triple (P3,P1,B,P1), inadmissible at the beta-P1 triple, passes the buggy predicate). My independent full-admissibility DFS (prefix-pruned, verified against check_ext.py's correct predicate at low degrees) gives the TRUE census: 105 admissible monomials total of degree<=41, dim A_40=3, dim A_41=8. The reported figures are wrong by 4-5 orders of magnitude, and the downstream 'measured infeasibility wall / 10^5-10^6 matrices' conclusion (DRAFT 3.4, target_exit.json blocking obstacle) is therefore unsupported by the code's own output once corrected. (4) TWIST 'CERTIFICATE' IS ASSERTION, NOT COMPUTATION: twist_check.py computes nothing — it prints a hardcoded JSON string (no import of May data, no homology computation). The underlying E1 facts it cites (E1(1,5)={a1}, d1(a1)=0, E2(2,5) dim 1) are true under the script's conventions (confirmed via (1)), so the inference 'naive twist has d^2(e0)=-a0*h10*e5 with no canceling source in-window' follows, but the file itself verifies nothing and the 'obstruction' is a property of the authors' own ad hoc naive twist definition, not of V(1). (5) UNDISCLOSED BOUNDARY EFFECT: may_window.py drops products with s>8 (mul truncation). d1 raises s by 1, so all E2 dims at s=8 — including headlined E2(8,41)=6 — have outgoing differentials to s=9 silently discarded and are upper bounds, yet DRAFT claims them as exact 'full E2 page' entries with no caveat. A false headline number plus an overstated exactness claim plus an assertion-only certificate = correctness FAIL. value: EMERGENT_FINDING gets no value presumption. The admitted target (classical d2 at (34,6)) and the preset fallback (motivic d2=0 at (34,6,17)) are both explicitly NOT achieved — DRAFT states this honestly. What remains is: (i) a machine table of sphere May E2 dims to t=41 at p=3 with only 3 textbook anchors checked and no comparison against any published May/Ext chart, i.e. an unvalidated recomputation of classical data and an unexplained enumeration; (ii) the observation that the authors' own naive tensor-product tw…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Classical d2(x) at (34,6) NOT decided; motivic d2(tilde-x)=0 at (34,6,17) NOT certified (fallback success criterion not met — fallback NOT_WORTH_PURSUING per target_exit.json (bounded F1 probe spent; further fallback work would re-hit the certified wall)); no Moss-convergence, Toda-bracket, hidden-extension, or Betti-realization claim is made. May-E2 dims are sphere-level under the §1 conventions of DRAFT.md; V(1)/motivic-V(1) E2 pages need the chart-anchored k-invariant correction. Published V…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
