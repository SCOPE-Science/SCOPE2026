# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Interval-certified closed-geodesic table and planar-vs-umbilic gap for the triaxial ellipsoid (1,1.2,1.5)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 328
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Differential Geometry
- **Method:** Jacobi elliptic-integral geodesic shooting with cut-locus interval enclosure

## Problem

For the triaxial ellipsoid E0: x^2/1^2 + y^2/1.2^2 + z^2/1.5^2 = 1 with induced metric, tabulate with rigorous intervals of width <=1e-4 the lengths of the three principal planar closed geodesics (coordinate-plane sections) plus the first 6 umbilic-spawned closed geodesics ordered by length, via Jacobi elliptic-integral shooting with cut-locus enclosure, and certify the gap witness G = (shortest umbilic-spawned length) - (shortest planar length) > 0 by interval arithmetic with replayable quadrature logs. Scope variants: up to 5 nearby axis triples in [1,1.6]^3 with distinct axes to test stability of the gap.

## Attempted claim

On E0 with semi-axes (1,1.2,1.5): the three principal planar sections have rigorously enclosed lengths (intervals width <=1e-4), the six shortest umbilic-spawned closed geodesics have enclosed lengths (width <=1e-4) with closure certificates, and the interval gap G_lo = L_umb1_lo - L_planmin_hi is strictly positive (witness value to be enclosed), separating planar minimizers from umbilic families.

## Research outcome

Proved and machine-certified (stdlib-only, VERIFY_OK) that the three coordinate-plane sections of the triaxial ellipsoid (1,1.2,1.5) are closed geodesics with disjoint length enclosures of width <=1.2e-9 (x=0: 8.508500366-8.508500367; y=0: 7.932719794-7.932719796; z=0: 6.925791195-6.925791196, shortest). The umbilic table and gap witness were not achieved.

## Why this attempt failed

Failed axes: correctness, value.

correctness: Reflection lemma is sound: coordinate reflection preserves E0 and fixes each coordinate section pointwise, so fixed set is totally geodesic; the draft's a=+a/-a argument is a correct specialization. Length reduction P=4*Amax*E(m) with m=9/25, 5/9, 11/36 is exact. Series machinery is valid: b_{n+1}=b_n*(4n^2-1)/(2n+2)^2 recurrence verified algebraically, factor<1 checked exactly so b_n decreasing, tail <= b_{N+1} m^{N+1}/(1-m) valid for m in (0,1); Machin pi with Leibniz bounds valid (terms strictly decreasing checked in Fraction arithmetic, even partial sum used as upper and odd as lower, correct orientation). Replay of verify_planar.py from inputs prints VERIFY_OK with widths 1.02e-14, 1.16e-09, 1.06e-16 (all <=1e-4) and exact rational endpoints lie inside the quoted decimals [8.508500366,8.508500367], [7.932719794,7.932719796], [6.925791195,6.925791196]; disjoint ordering L(z=0)<L(y=0)<L(x=0) holds. ESSENTIAL DEFECT: the quoted separation lower bounds '>=1.006929 (y0-z0) and >=0.575781 (x0-y0)' are FALSE. Exact replay gives y_lo-z_hi=1.0069285987... and x_lo-y_hi=0.5757805709..., i.e. both claims exceed the true gaps by ~4.0e-07 and ~4.3e-07. The script only prints float(gap) with %.6f (rounding up to 1.006929/0.575781) and never certifies those decimals as lower bounds. Hence the headline intervals/ordering pass but the stated gap constants as lower bounds fail. value: Delivered headline is only the three coordinate-planar ellipse perimeters at the arbitrary triple (1,1.2,1.5), admitted by DRAFT and research_report to be the 'elementary (ellipse perimeters) part only' with the full target (six umbilic-spawned intervals + planar-vs-umbilic gap G>0) NOT achieved and no distinct short umbilic closed geodesic isolated. This is a textbook restatement plus mere parameter substitution: P=4*Amax*E(m) with rational m, evaluable by any standard library in seconds to 15 digits; ordering follows from monotonicity with huge (~0.5-1.0) separations requiring no delicate certification. The motivated invariant in the admitted program was the umbilic-spawned family and the positive gap separating planar minimizers from umbilic families for multiplicity/stability/cut-locus/spectral-rigidity use; the topic fallback itself required 3 planar + >=1 certified umbilic geodesic with residual/stability log, which is not met (zero umbilic certificates). Per the value standard, a rigorously established exact invariant of a natural object is retrievable only when motivated before computation, not mechanically implied, and reasonably needed later; here the value is mechanically implied by a standard formula, the axis triple is an arbitrary well-separated choice with no theory singling it out, and no future worker needs these three quoted numbers beyond recomputing them. Certification alone does not rescue an arbitrary object/unexplained number. Honest description of incompleteness does not erase the lack of an independently valuable exact headline. Intrinsic l…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Partial result only: the admitted full target (six umbilic-spawned closed-geodesic intervals plus a certified planar-vs-umbilic gap G>0) was NOT achieved. Float exploration showed umbilic-launched geodesics returning near the y=0 planar double cover (t≈7.9327) with nonzero transverse velocity except for the in-plane launch, and no distinct short umbilic-spawned closed geodesic was isolated or certified; no Morse/stability or cut-locus claims are made (a Jacobi-monodromy computation disagreed ac…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
