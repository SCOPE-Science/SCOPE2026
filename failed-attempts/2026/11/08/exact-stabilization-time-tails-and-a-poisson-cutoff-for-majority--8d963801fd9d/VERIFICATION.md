---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For each labeled ring x, adjacent equal spins form invariant seeds and an alternating gap erodes from both ends, so T_n(x)≤t iff no alternating window of length 2t+3 remains, except the two even-ring checkerboards already periodic at t=0. Edge differences have even global XOR parity and are 2-to-1 from x. The signed automaton on 2t+2 run-length states counts precisely valid parity-zero circular difference words, giving the stated two traces plus two checkerboards. Pattern-start factorial moments have hard-core overlap and asymptotically disjoint support; n*2^-(2t+3)→lambda implies Poisson(lambda) and e^-lambda entry probability. This reasoning agrees exactly with a complete published earlier proof. Finite tests in the inspected checker are corroborative only.

## originality

FAIL

A 2026-11-02 published Resultary theorem, fully read, proves the identical first-periodic-entry law on the identical synchronous majority-of-three cycle graph: tr[M_{2t+1}(1)^n]+tr[M_{2t+1}(-1)^n]+2*1_{even n}; the submitted matrices A_m with m=2t+3 have indices 0..m-2 and exactly coincide with these M_{2t+1}. The earlier theorem also proves the identical scaling n2^-(2t+3)→lambda and e^-lambda limit, plus extra mean and concentration estimates. An additional 2026-10-25 theorem covers the same complete finite census and Poisson scaling. Thus the full claim is already known, not just an analogous method.

## value

FAIL

The mathematical facts are intrinsically relevant to cellular automaton relaxation, but the submitted finding is an exact restatement of earlier complete theorems, with no new independent invariant, stronger boundary, or nontrivial classification surviving. Reproducibility and new notation alone do not create incremental value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
