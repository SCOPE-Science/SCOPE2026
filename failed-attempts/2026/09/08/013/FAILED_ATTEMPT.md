# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Rank, generator heights, and bounded integral-point census for Mordell curves y^2=x^3+k, 0<|k|<=30, with exact-rational replay
- **Round:** 2026-09-07-first-light-01
- **Lane:** 73
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Arithmetic Geometry
- **Method:** two-descent rank bounding with canonical-height saturation search and independent height-pairing replay

## Problem

For each integer k with 0<|k|<=30 (60 smooth curves E_k: y^2=x^3+k; k=0 noted singular and excluded), compute: (a) torsion subgroup with certificate, (b) analytic rank bound and 2-descent/Selmer upper bound plus explicit-point lower bound, (c) independent generators with canonical-height pairing Gram matrix and p-saturation check, (d) exhaustive integral-point enumeration for |x|<=1e6 (naive height <=1e6) with exact-arithmetic replay. Identify the highest-rank curve(s) in the slice with generator heights and the largest-naive-height integral point as extremal witnesses.

## Attempted claim

Complete 60-row table for 0<|k|<=30: torsion, analytic+descent rank (upper=lower or explicitly flagged gap), generators with canonical heights and Gram determinant, saturation check, all integral points with |x|<=1e6 verified by exact rational replay; plus named extremal witnesses: highest-rank E_k in slice with its regulator/heights, and largest-height integral point (k,x,y). One-command script replays all on-curve checks and height-matrix recomputation from the table alone.

## Research outcome

Partial theorem on Mordell curves y^2=x^3+k, 0<|k|<=30: exact Nagell-Lutz+Mazer torsion table for all 60 curves, certified rank>=1 witnesses for 29 curves, and complete exact bounded integral census for |x|<=1e6 (65 x-values), with independent exact replay passing on all curves. Rank upper bounds, heights/saturation, and integral completeness beyond 1e6 explicitly open.

## Why this attempt failed

Failed axes: originality, value.

originality: Nearest substantive prior is LMFDB per-curve database, which definitionally anticipates the claimed facts. Verified example: 36.a3 is y^2=x^3-27, rank 0, Z/2Z, integral (3,0) -- exactly the DRAFT row for k=-27. By construction LMFDB holds rank/torsion/generators/integral points for every small-k Mordell curve in the slice (27.a4 y^2=x^3+16 etc.), i.e. strictly stronger than the bounded |x|<=1e6 restriction and the rank>=1 lower bounds. No new integral point, new torsion structure, new rank record, height, regulator, or saturation result is claimed beyond what per-curve lookups plus textbook Nagell-Lutz already give. Alpoge-Bhargava-Shnidman (arXiv:2011.01186) studies 2- vs 3-descent statistics asymptotically, and PARI/GP docs provide primitives -- correctly cited as tools/statistics, not anticipated tables. The asserted delta (slice-unified table + replay script) is repackaging/presentation, not a new mathematical object or gap closure. Internal Resultary non-overlap and failed-search timestamps do not establish priority over public LMFDB data. value: Even taken as new, the partial result is not independently worth finding later. (i) Torsion for 60 tiny-k curves by Lutz enumeration is a textbook exercise. (ii) The |x|<=1e6 box is arbitrary and explicitly non-complete; Siegel-completeness (the motivated goal) is disclaimed, so the census is an unexplained bounded enumeration whose entries are subsets of already-published complete integral-point lists. (iii) Rank>=1 for 29/60 with 31 curves undetermined and no upper bounds means the target's main extremal payoff (highest-rank curve in slice) is missing by the DRAFT's own admission. No canonical heights, Gram determinants, or saturation. Box-extremals (largest-box point (24,8158,736844), richest-box k=17) are box artifacts, not theory-motivated records for BSD/Hall. Falls under textbook restatement + arbitrary parameter slice + bounded enumeration without insight.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: No rank upper bounds (no PARI/Sage: no 2-descent/Selmer, no analytic rank); curves without witness may still have rank>=1, so highest-rank curve undetermined. No canonical heights, Gram matrices, or saturation. Integral census bounded at |x|<=1e6 only; no Siegel-completeness claim. Float sqrt used only as prefilter in census with exact int64 recheck and bounded-error window; verifier uses no floats.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
