---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reduction from the integer orbit agrees with finite modular reachability because each reachable state comes from a finite word. The valuation of 4^(3^j)-1 is j+1 (cubing raises this valuation by exactly one), hence 2 has order 2*3^(k-1) modulo 3^k and generates the units. The unit seeds 10 and 2 for the first two listed triples, and the A-orbits A^j(0)=(2^j-1)a when a is nonzero, cover the claimed ternary classes except for the missing class in each of the four surjective cases. The displayed B or C in each such case maps the full projection at level k-1 onto the missing class at level k; in the two restricted cases all generators preserve the allowed classes. Splitting parity then gives the first pair directly from A and B, and the middle two shell laws from the last parity-resetting C followed solely by B. The identities are B^t(C(x))+1=2*3^t(3x+2) and B^t(C(x))=2*3^t(3x+1), respectively. They yield the special residues at t>=k; the remaining shells have exactly 3^(k-t-1) terms. In the two restricted cases the leading parity comes from A, and the opposite one from C followed by B, with mod-18 classes 9/15 and 0/6 preserved by B. For (1,6,0), words consisting only of B starting at 0 are also covered, since C(0)=0 can be inserted first. The special classes merge modulo 6 exactly as stated. Independent set saturation compared against arithmetic progression shell sets for all six triples at levels 1 through 10: 60 exact equalities, with sizes [4,5,3,5,4,3] at k=1 and [12,14,8,14,12,8] at k=2 in listed triple order. Replay: python3 -I /workspace/branches/independent-checks/record3.py; record3.log in that directory. Frozen checker inspected, not executed.

## originality

PASS

Credit the exact fixed-coordinate six-triple comparison through its distinct 2/3 and 4/9 profiles; do not claim five unrelated novel laws. A distinct same-day Resultary record already supplies the entire (0,2,3) row by specialization, and (1,0,2) follows from that exact image by affine conjugation with a finite-quotient seed argument. All six profiles form three pairs under affine residue bijections. The two other profile laws are not covered by the inspected catalog entries or literature. No priority order is inferred within the same date.

## value

PASS

The six coefficient choices are the canonical critical free affine-semigroup bases, not a slice chosen after seeing numbers. Their exact local obstructions distinguish the two additional laws 2/3 and 4/9 from the known 3/4 branch, and the residue formulas determine where the missing mass lies, including the exceptional first level. Exact orbit images are usable in further modular and density-bound investigations; rephrasing the known middle law alone would not warrant this verdict.

The dated certificate retains the supplied scientific assessment, sources and limitations.
