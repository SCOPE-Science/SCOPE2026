---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The cyclic Hamming-composition spectra for lengths k<=4 invert to seven run statistics (a,r,p,q,v0,v1,e). Counts T_{k,j} in assigned RESULT.md recover those by triangular equations even for n<4 with wrap. The V_r(m,u) cases correctly count feasible numbers of length-two runs; remaining run lengths can absorb arbitrary nonnegative excess. The singleton incidences form a 2r-cycle bipartition with p and q selected; induced edges attain sharp L and H bounds and integer intermediate values via adjacent transpositions changing incidence by at most one, with r=1 double-incidence separately. Thus summing V0*V1*(H-L+1) gives all distinct arrays without requiring counting rotational source necklaces. Independently exhaustively enumerated cyclic binary words for n<=12 against finite-sum values; first separation of <=3 and <=4 occurs n=8. Finite enumeration corroborates but does not establish the all-n theorem.

## originality

PASS

Earlier cyclic binary trigram composition-spectrum results are strictly weaker observations. Ordered 4-gram profiles count richer data than composition-only windows, and length-four run<=2 restrictions do not cover arbitrary binary rings. Published linear composition reconstruction and restricted-read codes are not an all-n exact codebook capacity for cyclic composition windows of lengths 1..4.

## value

PASS

Exact maximal zero-error codebook cardinality for a natural cyclic composition-only observation is a motivated information-theoretic invariant; interval realization of singleton-run incidences gives a useful structural constructive result. The n=8 first strict improvement gives a sharp finite boundary; not a mere restatement of known full 4-gram profiles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
