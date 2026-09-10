# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact uniform spread of the diagonal extension PGSp4(3): fixed-point-ratio certificate versus maximal-subgroup obstruction
- **Round:** 2026-09-07-first-light-01
- **Lane:** 591
- **Disposition:** NO_RESULT
- **Domain:** Finite Group Theory
- **Method:** Aschbacher subgroup structure with fixed-point-ratio estimates and Guralnick-Kantor probabilistic generation bounds

## Problem

Determine the exact uniform spread u(G) for the named almost-simple diagonal extension G = PGSp4(3) with socle PSp4(3): either certify u(G) >= 3 via a single fixed-point-ratio sum for an explicit witness class s, or exhibit an explicit maximal-subgroup obstruction triple/quadruple pinning the exact value (candidate u=3).

## Attempted claim

u(G) = 3 for G = PGSp4(3) (diagonal almost-simple extension of PSp4(3)): there exists a fixed conjugacy class C = s^G such that every triple of nontrivial elements has a common mate in C (so u(G) >= 3 via P(x,s) sum < 1), and there exist explicit x1,x2,x3,x4 with no common mate in C (so u(G) < 4).

## Research outcome

Target u(PGSp4(3))=3 not established. Verified G=U4(2):2 from ATLAS standard generators (|G|=51840, correcting the topic 103680 typo), 25 conjugacy classes with ATLAS-matching centralizers, and 8 prime-order classes. The exact generation-proportion table needed for both the target witness/obstruction and the fallback FPR certificate proved computationally infeasible in pure Python (bounded pilot: zero pairs in ~2 min). Clean exit with NO_RESULT; no emergent finding (verified data duplicates ATLAS). Artifacts: ATLAS generator files, staged scripts, class data, exit record.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['No GAP/Magma/Sage in environment; all computation pure-Python (stdlib + numpy/sympy only).', 'Exact P(x,s)/FPR table (200 class pairs over |G|=51840) projected to hours; pilot completed zero pairs.', 'Maximal subgroups of G never identified; M(G,s) and obstruction search unstarted.', 'Verified class data replicates published ATLAS/CTblLib values — no original finding.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['No GAP/Magma/Sage in environment; all computation pure-Python (stdlib + numpy/sympy only).', 'Exact P(x,s)/FPR table (200 class pairs over |G|=51840) projected to hours; pilot completed zero pairs.', 'Maximal subgroups of G never identified; M(G,s) and obstruction search unstarted.', 'Verified class data replicates published ATLAS/CTblLib values — no original finding.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
