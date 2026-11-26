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

For n≥3, the claimed maximum and equality cases follow by run compositions. A balanced profile sums the two endpoint orientations, giving N/t times the binomial product in (1); an unbalanced profile has one forced orientation and product (2). At fixed t the centered loop split maximizes the product, strictly up to exchange for t≥2. For the unbalanced optimum, take a mode t≤r/2 and compare to the feasible balanced profile with t'=t+1 and (q',r')=(q+1,r). The comparison is strict except for the length-five equality in this intermediate bound, where the balanced global maximum is still larger. The centered balanced mode follows from the sign of AB−(A+B+3)k−2, with the single adjacent tie at n≡2 mod 4. Stirling at the centers up to bounded shifts gives the stated constant. At n=1 there is one empty spectrum and two words; at n=2 each spectrum is a singleton. Here the balanced-maximizer sentence is read in the n≥3 paragraph, not as saying the two transitions agree in all four singleton profiles at n=2. Independent literal enumeration of all 262,142 words of lengths 1–17 agrees with the maxima and n≥7 profiles; the frozen program was inspected, not executed.

## originality

FAIL

The separate Resultary record 5122acc1b9bd already gives the same all-length extremum for n≥3, the same equality classification (including small-rank loop splits), and the same sharp asymptotic. This is demonstrated equivalent coverage, not an inference from a similar name or an inaccessible source. The added values at n=1,2 are immediate from the definition and do not supply a distinct substantive result.

## value

FAIL

The maximum reconstruction ambiguity is a natural invariant and the unrestricted sharp theorem is worthwhile in isolation. As a submitted contribution, its entirety beyond the empty and single-pair cases and the extracted small table is already established. The same run-count, central-product, consecutive-ratio and Stirling strategy is present in the prior proof; no materially useful new theorem or method survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
