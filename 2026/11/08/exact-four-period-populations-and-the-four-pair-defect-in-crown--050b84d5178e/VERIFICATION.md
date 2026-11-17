---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For synchronous 3-state GH on Cr_n=K_{n,n}-M_n, every nonconstant four-periodic full state activates every vertex exactly once per four times (an always-rest vertex next to periodic excitation would activate). Assign phase p(v); local update is equivalent to excluding adjacent phase p+2 and requiring adjacent phase p-1. Cross-shore opposite-phase supports must be singleton matched pairs; coexistence forces four distinct matched indices and n=4, yielding exactly 4!=24 exceptional assignments. Otherwise each shore uses both phases of one parity, opposite shore both of other; writing s=2^n-2, r=s-2n, robust assignments count r, singleton-phase shore assignments 2n, no pair of both shores singleton compatible, yielding 2sr. Thus P4(n)=2(2^n-2)(2^n-2-2n)+24*1_{n=4} for every n>=3. Independently enumerated complete 3^(2n) microscopic dynamics for n=3,4,5 (0,192,1200). Source finite phase checker also inspected; infinite result follows from phase classification.

## originality

PASS

The 2016 general GHM graph cycle-integral theorem describes eventual dynamics but does not yield the exact initially primitive-four state count for the crown family. Published November 2 crown dynamics theorem classifies allowable periods, maxima of entry times, and exceptional 6/10 period basins via clipped matched-type signatures; its full RESULT.md inspected and no explicit P4(n) population formula or 24-state phase defect appears. Its machinery might support deriving the count with additional counting work, but this is not a direct stated numerical corollary.

## value

PASS

The crown graph is a natural all-size minimally defective complete bipartite family; exact four-period population and isolated four-pair phase exception quantify effects of deleting a full matching and complement period classification with an exact labeled state count. The n=4 anomaly and all-n formula are natural structural information, not an arbitrary finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
