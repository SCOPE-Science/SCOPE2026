---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

At each regular branch the real lift is F_+(x)=2(1+b)x+a-b/2 and F_-(x)=2(1-b)x+a+3b/2; the +-- integer carries (0,1,2) yield a unique affine fixed return x=[(1+q+q²)a-q²b/2+q(3b/2-1)+3b/2-2]/(1-pq²) with p=2(1+b),q=2(1-b). Independent SymPy cancellation gives exact return residual zero, y(a_-)=1/2, z(a_+)=1, and exactly the claimed rational width and partial fractions. M=pq² decreases strictly from 8 to 0, crossing 1 once at b_c; on (b_c,b_u) x,y,z increase strictly in a and endpoint sign factors E_-,E_+,Q prove 0<x<1/2<y,z<1 with correct integer carries. Every such regular 3-cycle is primitive (the itinerary is not constant), its multiplier lies in (0,1), and it locally attracts. Primary Lemma 3.1 proves the reflection a->1/2-a mod1; Lemma 4.1 excludes all-minus nonfixed attracting cycles, giving period floor 3. Independently evaluated b_c=0.731299211487387..., b_u=0.895643923738960..., and area 2 integral width=0.0024418116003992040..., with exact rational interior checks at b=3/4,4/5,17/20,89/100. These finite checks corroborate rather than replace the all-parameter algebra. Boundary equality, global exhaustion of other charts and entire basin claims are expressly excluded.

## originality

FAIL

The full principal claim is a restatement of an existing Resultary 2026/10/26 canonical +-- eye theorem for the EXACT same PLPDM, integer carry code (0,1,2), sharp b interval and rational a endpoints. Independent symbolic subtraction gives the prior and submitted widths identical, and both texts give the same M(b), branch bounds and minimal period. Earlier family symmetry supplies the reflected twin; the only extra area notation and decimal are an elementary integral of the already published exact width and cutoff values, not an independent unknown theorem. GitHub prior Resultary source was committed 2026-11-08T20:01:35Z, before the assigned source first commit 2026-11-08T21:16:00Z. O therefore FAILS even though the original proof is correct and the 2025 primary motivating paper alone did not state this band.

## value

FAIL

Determining the smallest-period non-single-minus eye and its exact two-parameter band is mathematically motivated, but that structural classification already exists in the 2026/10/26 theorem. The only extra measure 2∫_{b_c}^{b_u}(U-L)db is immediate rational quadrature of a fully known interval width, with its numerical value reproducible by standard integration. It does not resolve a separately unknown natural invariant, supply new dynamics, an independent bifurcation threshold, a new count, or an otherwise usable obstruction; merely giving a decimal and elementary partial fractions of known formulas is not new mathematical value. Existing code and exact correctness cannot rescue the covered result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
