---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For a geometric window, each lag |a|<=m has a nonzero ambiguity overlap at every modulation (ratio modulus four); every other lag has disjoint support. Fourier inversion therefore recovers exactly edges of the induced support graph; phase retrieval for one window is equivalent to connectivity. I independently enumerated all 16383 nonempty 14-bit support masks at bandwidth four: 560 disconnected, grouped into 42 translation orbits. For all 42x42 pairs of disconnected supports, exact elimination of the (T^c,S) Fourier restriction over F_1009 with primitive 14th root 904 had full column rank. A nonzero reduced minor proves the corresponding cyclotomic minor nonzero over C, so no nonzero signal can have both time and Fourier disconnected supports. At m=3, exact rank checks on a 3x4 seventh-root matrix and four augmented 4x4 matrices yield a nonzero-support kernel with time support {0,2,8,10} and Fourier support {0,1,2,3,7,8,9,10}; both bandwidth-three graphs disconnect. Monotonicity handles all m<=3 and 5,6. This is a finite exhaustive certificate with an all-signal analytic rank reduction, not a mere signal sample.

## originality

PASS

Best-of-knowledge originality: actual Resultary searches, relevant published statements and accessible primary text reveal no matching or stronger theorem implying this exact final claim; source-specific residual risks remain, and a search miss is never treated as novelty proof. The all-C^14 m=4 proof requires the global 42^2 exact rank certificate, and the m=3 witness supplies sharp necessity; these are not corollaries of the cited implications.

## value

PASS

The exact sharp full-space strong STFT threshold in a composite group of order fourteen is a natural obstruction/sufficiency boundary, improving the known general sufficient lag five and distinguishing full-space from already classified prime-period sectors. The 42-orbit exact minor certificate resolves a nontrivial finite dimensional Fourier-restriction question that neither a support-graph lemma nor an earlier sector theorem settles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
