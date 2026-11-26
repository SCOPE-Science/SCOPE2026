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

The fiber formulas are correct. The frozen overcount discussion did not explicitly retain the last scalar whose choices compensate imposing the one product equation. The repaired proof fixes all image-vector representatives, writes the last factor as u_k γb and shows that γ is uniquely determined by the nonzero pairings. Each adjacent pair of distinct image lines gives precisely q^(n−2)(q−1) choices for its row functional; there is no remaining quotient by rescaling, even at k=2. The image lines consequently form walks on the loopless complete graph, with end line in ker b. The projection onto constants and its complement gives the two eigenvalues P−1 and −1, and b(a)=trace Z tests whether the start is an allowed end. Every rank-one prefix has t(P−1) surviving extensions, and averaging over the two trace classes of relative sizes H/P and 1−H/P gives the exact total variation. The repair also shows exact-length positivity by length-two walks between any pair and induction, rather than extending an unspecified walk with a possibly changed endpoint. At length one in the graph there is exactly the stated obstruction. Independent bounded enumeration started from all raw matrices using minors to identify rank one and ordinary matrix squaring to select factors. It matched every fiber and the exact TV for (n,q)=(2,2),(2,3),(3,2), k=2 through 5. The supplied code and transcript, including F4 tests, were inspected, not executed; the all-field proof does not rely on either computation.

## originality

PASS

The supported new portion is the general all-length prescribed-product law beyond two factors for the full minimal nonzero nilpotent similarity orbit, and the exact alternating trace discrepancy and conditional mixing law. The two-factor census and qualitative rank-one factorability are not credited as discoveries. The repaired normalization and positivity argument do not change those claims.

## value

PASS

This is an all-length count for the minimal nilpotent class over every finite field, not just another existence proof or a numerical census. Beyond the sharp reachability boundary, it quantifies the exact alternating bias between target strata and the full conditional mixing rate. The projective-walk reduction explains both phenomena and makes the formulas directly usable without enumerating matrix words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
