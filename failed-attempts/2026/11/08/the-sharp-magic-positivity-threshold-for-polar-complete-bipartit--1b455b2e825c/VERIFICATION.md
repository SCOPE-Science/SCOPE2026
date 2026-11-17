---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Graph-potential normalization fixes the two small-part endpoints and counts common intervals, giving L_q(t)=(2t+1)^q+2 sum_(s=1)^(2t) s^q. Bernoulli–Faulhaber expansion and triangular basis conversion give exact a_i(q). Direct independent rational interpolation confirms q1..8 positivity, including q8 minimum 2/15, q9 a5=-144/5 and q9..14 negative witnesses. For q>=15, Bernoulli signs and |B_(j+2)|/|B_j|>3 (even j>=14) give negative coefficient a1 (q=0 mod4), a2 (q=1,2 mod4), or a3 (q=3 mod4). This is a valid all-q proof, not an extrapolated test.

## originality

FAIL

FAIL decisively: published October 25, 2026 SCOPE theorem for exactly the SAME polar of symmetric edge polytopes of K_(2,m), in the same root lattice, gives the identical count L=(2t+1)^m+2 sum_(s<=2t)s^m, the identical magic-positivity iff 1<=m<=8 for ALL m, AND a stronger ordinary Ehrhart-positivity cutoff at 19. Its explicit exact formula for every magic coefficient also dominates the presented low-index Bernoulli specialization. Finite q<=11 table was already Konoike. Different proof of already proved sharp cutoff does not establish a new claim.

## value

FAIL

FAIL as unchanged original: the exact same all-parameter cutoff, lattice counts and magic coefficients are a known completed classification. Additional low-index witnesses provide an alternative certificate and routine specializations of a prior universal coefficient formula; no independently motivated new invariant or geometric structure is established here that survives the stronger prior theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
