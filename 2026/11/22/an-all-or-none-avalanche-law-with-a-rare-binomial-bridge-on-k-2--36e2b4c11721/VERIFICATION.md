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

Put m=n−1 and fix the positions of k occupied nonsink leaves. Burning adds one grain to each hub. Some hub must start at n−1; it can release exactly the k occupied leaves before the other hub fires, and the latter can fire iff its initial height is at least n−1−k. Completing the burn yields the original stable configuration. This gives 2k+1 ordered hub states and total n·2^(n−1). With a hub drive the counts per leaf assignment are k zero events, one boundary event of size 1+k, and k full events of size n+1. In the zero-event sentence of Proof §2, the other hub height b is fixed at n−1 and it is a that has k possible values; the state count used is correct. For a driven leaf initially empty the avalanche is zero. When it is occupied, its initial firing activates at least one hub, and for exactly two ordered hub states the other stays one grain short after the remaining occupied leaves fire. These give size 2 plus the number of other occupied leaves. In every other recurrent state with that leaf occupied, both hubs fire once, all other leaves once, and the driven leaf twice. This legal schedule stabilizes: no hub receives more than n grains over the schedule, and every leaf ends below threshold; the abelian property then identifies the odometer. The two boundary hub states are distinct even at n=2, since k≥1 in this case. Summing gives both boxed polynomials, mass (n−1)/(2n) at each extreme and bridge mass 1/n with the stated binomial laws. With maximum M=n+1 or n+2 and bridge binomial degree d=n−1 or n−2, the exact variance is (1−1/n)M²/4+d/(4n); this gives the scaling, and the bridge mean and extreme-pair mean both equal M/2. Shipped verify.py was inspected, not executed. Its finite integer histograms and formula checks are ancillary to the all-n counting argument.

## originality

PASS

The supported distinct claim is the pair of complete fixed-source spectra, specifically the conditional binomial bridges and the nonadjacent leaf spectrum with its repeated toppling. The known hub maximal coefficient, hub mean, one-toppling bound and general recurrence machinery do not count as new. The priority assessment is bounded to the inspected comparisons.

## value

PASS

For a canonical graph family the fixed-drive laws resolve the full stationary size distribution rather than only a mean or a full-support event. The pair shows that almost all additions are zero or system-size, with an exactly quantified binomial intermediate class, and makes the repeat-toppling distinction visible for the leaf source. This is a motivated exact comparison of source classes on an unbounded graph family; it is not a claim of scale-free criticality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
