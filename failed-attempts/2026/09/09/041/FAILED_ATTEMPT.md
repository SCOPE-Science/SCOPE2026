# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Lee collapse pages and a torsion-to-collapse certificate across the 10_124-10_131 window
- **Round:** 2026-09-07-first-light-01
- **Lane:** 361
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Knot Theory
- **Method:** Lee spectral-sequence collapse-page certification with Turner differential ranks and torsion-to-collapse analysis via Bar-Natan cobordism checks

## Problem

For the committed window W={10_124,...,10_131}, determine from scratch the exact Lee spectral-sequence collapse page E_r per knot, the Turner/Lee E2 differential ranks and surviving E-infinity bigradings, and the integral Khovanov torsion pattern per bidegree; prove and verify a torsion-to-collapse lemma stating explicit torsion/bidegree conditions under which E2=E-infinity holds on W, with one independent Bar-Natan cobordism-map replay check and full rank logs.

## Attempted claim

From committed PD codes of each K in W={10_124,...,10_131}, the independently built Khovanov-Lee-Bar-Natan data yield the exact Lee collapse page E_r(K), the E2 Turner differential ranks, the surviving E-infinity bigradings, and the integral torsion pattern; and a stated torsion-to-collapse lemma (explicit hypotheses) holds verified across W, e.g. specified Z2-only torsion concentration forces E2-collapse, with all ranks, differentials, and one cobordism replay check archived.

## Research outcome

Certified single-knot Khovanov-Lee profile for 10_124 (fallback scope): exact Kh bigradings, SNF-certified Z2 torsion hosts, validated Lee complex with dim-2 homology, and E2 differential ranks, with replay logs; collapse page withheld due to a documented, honestly disclosed E3-vs-Lee tension.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: DRAFT.md self-reports a global inconsistency that is fatal under standard Khovanov-Lee theory: E2 survivors after the four Phi-induced ranks (1,1,0,1) on total Kh dim 10 leave E3 of dim 4 at (0,7),(0,9),(4,15),(5,19) with 'no further nonzero bigrading-compatible higher differential', while the same pipeline reports ungraded Lee homology dim 2. Over Q, Lee homology of any knot has dim 2 (Lee), so E_inf must have dim 2. E3=4 with no further differential contradicts Lee=2; hence at least one of the three computed inputs (rational Kh bigradings, Phi-induced E2 ranks, Lee nullity) deviates from the standard theory, as DRAFT sec.4 honestly states. Because the three inputs come from the same code pipeline (kh_stepG/kh_stepH/kh_stepI/kh_stepJ), the error cannot be localized from the logs: every check applied (d^2=0 on 20155 compositions, Euler/chi, trefoil control, global dPhi+Phid=0 mod 1e9+7 on 122866 entries, two-prime rank agreement, spot SNF) passed yet the joint output is mathematically impossible. Evidence is experimental, not proof: all 60 Kh block ranks outside 6 SNF-checked blocks rest on agreement mod two primes (1000000007, 998244353), not exact arithmetic; odd torsion outside two SNF blocks explicitly not excluded; three of four E2 ranks rest on mod-prime quotient computations (only the (4,15)->(5,19) zero is exact over Z); Lee nullity rests on mod-prime ranks; dPhi+Phid checked only mod prime. No collapse page, no E-inf bigradings, and no torsion-to-collapse lemma are claimed. Mirror/orientation ambiguity is flagged in research_report.json (s=+8 computed vs s=-8 admission/KnotAtlas). Therefore no headline claim is proved; the only certified fragments are partial SNF facts conditional on an otherwise-contradicted pipeline. originality: The parts of the profile that appear correct are already tabled on KnotAtlas 10_124, contradicting DRAFT's gap statement. KnotAtlas 10_124 displays the full bigraded Khovanov table (t^r q^j coefficients with chi column), with nonzero entries at exactly the 10 bigradings DRAFT lists: (0,7),(0,9),(2,11),(3,15),(4,13),(4,15),(5,17),(5,19),(6,17),(7,21), plus Jones -q^10+q^6+q^4, PD X4251..., DT, signature 8, s=-8, and the integral table (Data:10_124/Integral_Khovanov_Homology) showing Z summands and Z2 torsion at r=3 and r=7, i.e. the same Z2 pattern DRAFT re-hosts at (2,13)/(6,19) via UCT excess at (2,13),(3,13),(6,19),(7,19). DRAFT's claim that 'KnotAtlas tabulates ... only as ungraded or chi-level data' and 'records no integral SNF torsion locations per bidegree' is factually false on live fetch. Hence rational Kh dims and Z2-host existence/location are not new and not mechanically separated from the prior table. The only in-principle-new data (Phi-induced E2 ranks 1,1,0,1, Lee-nullity replay logs) cannot be credited as a new exact invariant because correctness FAIL shows the joint computation is inconsistent (E3=4 vs Lee=2), so no reliable new value is established. Rasmussen (math/0402131), Bar-…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: ['Only 10_124 carried past Jones level (10_128 Jones-matched; 6 PDs need phase resolution)', 'Kh ranks outside SNF-checked blocks rest on two-prime agreement; odd torsion outside SNF blocks not excluded', 'E2 ranks (except the exact (4,15) zero) rest on mod-prime quotient computations', 'Collapse page, E-inf bigradings, torsion-to-collapse lemma NOT established (E3=4 vs Lee=2 tension disclosed in DRAFT/WORKLOG)', 's=+8 vs admission-text s=-8 mirror ambiguity flagged; s not a finding']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
