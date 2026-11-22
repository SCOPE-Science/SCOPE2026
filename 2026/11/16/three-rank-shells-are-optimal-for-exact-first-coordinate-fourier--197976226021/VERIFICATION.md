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

Under left/right GL_n-invariance, the Fourier transform of the matrix law is constant on frequency-rank 1 and 2 classes, and differences of distinct coordinate frequencies have exactly those ranks (including same coordinate with distinct scalar). Let Z=q^{nullity M}, N=q^n. For independent input vectors, kernel-incidence counts imply p1=(E Z-1)/(N-1) and p0=E[(Z-1)(Z-q)]/[(N-1)(N-q)]. Rank-one Fourier zero requires p1=1/N, and rank-two orbit averaging additionally requires p0=1/N^2. These give E Z=2-1/N and Var Z=(q-1)(1-1/N)^2. Any two-support law on powers of q must include 1 (mean between 1 and q); variance then forces its other support b*=q+1-q/N strictly between q and q^2, impossible. Vandermonde moment matching on 1,q,q² gives positive w0,w1,w2 as quoted; q^2 is valid even n=2. Independently enumerated all 16 binary 2x2 matrices: rank counts 1,9,6 for ranks 0,1,2, weights 1/16,9/16,3/8 in that order and exact rank-one and rank-two character expectations both zero. No small finite-field enumeration is used as proof for all prime powers.

## originality

PASS

Best-of-knowledge PASS after separate formulation/implication comparisons, published-result search, and bounded primary-literature inspection; not a certification of absolute historical priority. Checked the implication direction: ambient transform theory => possibility of computing multipliers; not => positivity/minimal-shell theorem as stated. Best of knowledge, with inaccessible full text explicitly noted.

## value

PASS

A natural orbit-sparsity optimization for a rank-metric harmonic sampling frame; the sharp minimum number of GL_n×GL_n rank strata and positive explicit three-shell design are distinct from k-good matrix minimum *individual point-support* results. Exact orthonormality of 1+n²(q-1) modes has concrete structured-sampling significance without pretending to be a full Fourier basis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
