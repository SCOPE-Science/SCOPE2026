---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The rooted Euler-tour correspondence is exhaustive: the length-five words are the 32 distinct edges, and the single occurrence of 00000 fixes the rotation. A transition pairing is accepted exactly when it is one 32-edge cycle. An independent rooted traversal and bit-rotation/Hamming-distance computation reproduced all 2,048 classes, all 47 energy rows and six peak columns in the frozen CSV, including 87 occupied joint cells, minima 192 on 12 classes and maxima 1952 on four, the three and one size-four extremal orbits, the exact mean 2813/4 and variance 1336631/16, and the peak marginals. The peak-8 rows give the 224–992 range. The autocorrelation is a multiple of four by balance. The paired nonmiddle lags contribute multiples of 32; at lag 16 the support-intersection count is even because positions are paired by adding 16. Thus the divisibility also follows directly. The Fourier identity has the stated factor 1/32 and zero-lag subtraction 1024 with the unscaled forward transform shown in the record.

## originality

FAIL

Resultary 132a86d69a57, displayed date 2026-10-18, provides the full per-cycle autocorrelation and symmetry-orbit data for the exact same 2,048 rotation classes, normalization, and reversal/complement action. Its CSV directly provides R1 through R16, orbit_representative and orbit_size. The entire frozen cross-tabulation and all extremal symmetry counts follow by applying a fixed sum of squares and maximum to each row and grouping. The earlier source need not have printed those aggregated numbers for its stronger exact data to cover them. The journal papers provide partial corroboration but are not the decisive overlap.

## value

FAIL

The energy objective and complete classification are well motivated, but the claimed exact outputs are routine aggregations of the earlier complete profiles and orbit labels. The divisibility observation follows from balance and lag pairing and does not leave a substantive independent result. A convenient derived table and an independent recount are useful corroboration, not a surviving new exact invariant under the stated standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
