---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For N=2m+1, the central covariance sum is C_m=3−2^(1−m); the atmospheric variance numerator of the boxcar uses the lag counts N−k and equals S_N=3N−4+2^(2−N). The independent target-noise term cancels, and the comparison noise adds η/N to normalized risk. Thus R_m=1+(η−B_m)/N, with B_m=3+4/N−4·2^(−m)−2·4^(−m)/N. With y=2^(−m), the numerator of B_{m+1}−B_m over N(N+2) is D_m=−8+2yN(N+2)+y²(3N+8)/2. Independent rational arithmetic gives D_0 through D_6 as 7/2,73/8,327/32,1021/128,2275/512,1961/2048,−15569/8192. For all m≥6 both positive terms have next/current ratios below one: (N+4)/(2N) and (3N+14)/(4(3N+8)). Therefore the maximum is uniquely B_6=86399/26624 over the entire unbounded family, establishing the strict regions and the sole finite tie at equality. At η=13/4 the 11-, 13-, and 15-frame excess risks over omission are 65/61952,129/346112,1793/1843200, respectively, so the middle window is a strict neighboring minimum but loses to omission. These are variance comparisons in the specified second-order model, without any assumption of Gaussianity or an AR(1) recursion. The result says neither that 13 frames are optimal at arbitrary subcritical η nor that finite unit gain can be replaced by optimized gain. RESULT.md lines 23–46 reconstructed; verify.py and VERIFICATION.md inspected, not executed.

## originality

PASS

Temporal comparison-star binning and selecting its width are prior work, and the per-window covariance algebra is classical. The supported distinct claim is the exact unbounded odd-window optimum of the benefit threshold for the unit-gain half-life covariance model, including its local-but-not-global example. Hartley–Wilson's unavailable full text limits the priority assessment, not the mathematical verdict.

## value

PASS

A one-frame correlation half-life makes a natural idealized benchmark for the reference-inclusion decision in a previously motivated workflow. The exact global threshold and the strict local minimum rejected by omission distinguish all-window design from choosing a good neighboring bin. The result is a useful benchmark for the stated unit-gain rule, not a telescope-independent recommendation or model calibration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
