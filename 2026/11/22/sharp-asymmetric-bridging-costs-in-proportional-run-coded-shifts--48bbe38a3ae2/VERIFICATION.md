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

The two displayed bounds and their uniform leading-order consequence hold for the coded language. On the right, a terminal zero run of visible length a can be taken complete and extended by ka ones; for a terminal one run of length b, the requisite total one-run length is fixed by a fully observed preceding zero run, or one may choose a zero run of length max(a, ceil(b/k)) if the past is clipped. For an all-one word use ceil(m/k). This costs at most km. On the left, a leading zero run needs only the missing zeros prescribed by a complete first one run (or by the shortest compatible completion of an open first one run); a leading one run of length b needs at most ceil(b/k) zeros and k-1 ones. Joining the two completed junctions proves the upper bound. For t=floor((n-2)/k), the pair 0^(m-1)1 and 01^(kt)0^(n-kt-1) forces disjoint bridge contributions of at least k(m-1)-1 ones and t-1 zeros, since the first block's ones must finish and the later complete kt-run forces exactly t preceding zeros. Their concatenated contribution is admissible, including the empty-bridge case. The coefficients are unequal for k>1 and coincide at 1 for k=1; the prose 'different' is read with this qualification, not as an extra claim for k=1.

## originality

PASS

The same-language antidictionaries and the nearest ambient or coded-shift bridge/completion theorems do not cover the optimized two-independent-length theorem. The complete forbidden-list descriptions allow membership tests but do not supply either the uniform asymmetric pair completion or the combined forced-run lower witness.

## value

PASS

The worst-case shortest join is a natural refinement of the specification question in this established coded system. The theorem gives separate sharp directional costs with a length-independent error, distinguishing the effects of long outgoing and incoming words rather than merely providing an unspecified linear bound or discovering nonspecification again.

The dated certificate retains the supplied scientific assessment, sources and limitations.
