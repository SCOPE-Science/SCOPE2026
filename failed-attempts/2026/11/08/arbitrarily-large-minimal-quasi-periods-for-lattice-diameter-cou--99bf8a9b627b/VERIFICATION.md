---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

At the pinned RESULT.md the parallelogram parametrization (s,t) in [0,k]^2 gives horizontal width k(q+2-1/q). For nonhorizontal primitive lattice directions a vertical displacement at least m bounds m<=k(q+1), and equality is excluded by the primitive-direction integrality at the unique extreme vertices. On integer heights k<=y<=qk, H(y)=k(q+2)-a-1_{j>0}-1_{j<r} for k=qa+r and y=bq+j. Counting exactly the qualifying residues yields the displayed piecewise N_q(k), and pairwise distinct residue slopes force every eventual period to be divisible by q. Independently enumerated every integer-point pair for q=2..7, k=1..4: all 24 cases agree on gcd-length diameter, segment count and horizontal orientation. The all-q proof is symbolic, not inferred from these finite tests.

## originality

FAIL

The full earlier October 25 published theorem is the identical family P_m with identical lattice diameter, qualifying lines, complete all-dilation count, least quasiperiod m and leading-slope ratio m. Setting m=q and n=k, its r>0 formula (q-r+1)(k-a) is algebraically identical to (q-1)k+1-(r-1)(k-a-1) from the submitted theorem. The binary-input-versus-period-table observation follows mechanically from the earlier theorem plus vertex coordinates O(q). Consequently both the central and claimed extras are covered.

## value

FAIL

A sharp unbounded quasi-period spectrum is mathematically motivated, but this exact family, counts, and slope ratio were already established in the earlier October 25 full theorem. The additional explicit-tabulation lower bound is a straightforward input-size restatement of that same preexisting spectrum, not a separate valuable new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
