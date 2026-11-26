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

The equation is A²=0 and AB+BA=0, with the entry-equation scheme as base, not its reduced orbit closure. Rank r forces Jordan type (2^r,1^s), s=n−2r. With a decomposition into image, s-dimensional middle space, and complement to the kernel, A is the identity block from the last summand to the first. Writing those indices as I,H,J, the independent constraints on B are B_JI=B_JH=B_HI=0 and B_JJ+B_II=0. They give 2r²+2rs=2r(n−r) constraints even in characteristic two. The group centralizer is open in the linear commutant, of dimension 2r²+2rs+s², hence the orbit has dimension 2r(n−r) and is geometrically irreducible. The linear maps in B have constant rank on that orbit, giving a kernel vector bundle and an irreducible total space of dimension n². All closures are distinct (rank cannot increase on specialization); equal dimension precludes proper containment. Since they cover the geometric reduced support, they are exactly its components. Choosing image, containing kernel, and the quotient-to-image isomorphism gives the two Gaussian coefficients and GL_r; multiplying by the kernel size gives the exact summand including r=0. The independent replay directly tested pairs for (q,n)=(2,2),(3,2),(2,3), with rank counts (16,12),(81,72),(512,672), and used elimination of the explicit anticommutator at (2,4), obtaining (65536,107520,53760). Replay and results: /workspace/branches/da23c851-285d-4493-9bb8-b95b76882176/independent_replay.py and independent_replay_results.txt in the same directory. Frozen verify.py was inspected, not run. The replay is bounded and does not independently test the recorded extension-field cases; the proof covers them.

## originality

FAIL

The strongest distinct indexed power-zero theorem uses the same entry-equation scheme and supplies the rank of the defining differential and the exact labelled dual-number count for arbitrary exponent, characteristic and Jordan type. Its exponent-two specialization gives every frozen arithmetic summand and mechanically gives the full geometric conclusion: constant rank on each irreducible orbit, sum of base and fiber dimensions n², and distinct equal-dimensional closures. Several additional records explicitly reproduce or refine the arithmetic marginal; one reproduces the n=3 geometric example. These are existing equivalent or stronger mathematical coverage at review time, not evidence of who published or discovered the result first. The earlier reduced nilpotent-jet literature is not the reason for failure.

## value

PASS

Giving all irreducible components of a natural first-order matrix representation locus is substantively useful: every rank stratum contributes, despite the one-component ordinary representation variety, and the same stratification yields an exact characteristic-uniform point count. This is a meaningful structural question and not merely a small table, though the separate originality check finds existing mathematical coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
