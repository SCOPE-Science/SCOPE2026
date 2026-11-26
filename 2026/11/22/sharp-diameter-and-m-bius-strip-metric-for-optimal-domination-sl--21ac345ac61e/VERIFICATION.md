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

The total cyclic-gap deficit from all threes is 2: either one gap 1 or two gaps 2. This precludes triple coverage and implies exactly two doubly covered sites. The closed-neighborhood operator A is injective because a kernel vector is 3-periodic and gcd(3,n)=1. Under multiplication by 3 inverse, the first gap type gives separation m-1 up to reversal, and the second gives separations j+m-1, 1<=j<=m-1. The counts agree (n(m+1)/2), so the map is onto. In both directions a transformed +1 move is the coverage change delta_(i+2)-delta_(i-1)=A(delta_(i+1)-delta_i); injectivity recovers a legal original slide. The lifted integer strip is L1-geodesic by monotone paths through a feasible coordinatewise minimum. All lifts of a target form one orbit under (a,b)->(b,a+n). A q nearest to the sum difference divided by n yields a sum residual <=floor(n/2) and gap residual <=m<=floor(n/2); other q cannot improve it (their sum residual alone is at least floor(n/2)). Standard-lift sums differ by less than 2n, so this nearest q is among the stated five. From every state one may shift the target sum by floor(n/2), adjusting its gap by one if needed for parity; all target lifts then have sum residual at least floor(n/2). Boundary pairs have exactly two legal moves and interior pairs four, including the n=4 case. This proves the exact distance, eccentricity and census, independently of any finite test. Replay: python3 /workspace/branches/independent_checks.py 1; independent bitmask enumeration and graph breadth layers at n=4,7,10,13,16 agreed for all 5,514 ordered pairs. The frozen script was inspected, not executed; its recorded larger finite run is corroboration only.

## originality

PASS

Pass the identification of the ordinary minimum-domination slide graph with this particular two-token strip and its resulting uniform eccentricity/census. Do not credit generic transport optimality, already covered in broader token systems, or the old connectivity and state count. The general distance theorem plus the new code and the extremal argument gives the numerical bound; the distinction is not that prior distances could not be used to derive it.

## value

PASS

This is a natural reconfiguration graph whose local moves and global distance were not specified by connectivity or counting. The ordinary-domination code turns an optimization over slide sequences into a constant-size exact calculation after an input scan and produces optimal paths. Equal eccentricity despite differing degrees is a useful structural consequence. The value does not depend on re-proving generic strip geodesics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
