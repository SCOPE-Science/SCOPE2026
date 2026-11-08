---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For homogeneous positive activity x, acyclic right-column patterns in K_{3,b} give Z=(1+3x)^(b-2)H_b, marked-edge polynomials A_b,B_R,B_L,B_D and Rayleigh differences Delta_R=x^4(b-1)P_R, Delta_D=x^4 P_D, Delta_L=Delta_D+x^4(1+3x)^2 H_b. Every coefficient in P_R and P_D is nonnegative for b>=2 and x>0 with positive constant terms, hence strict covariance negativity in every edge-pair orbit. Independently symbolically expanded all three exact polynomial identities with Sympy (zero remainders). Correctness PASS: a valid new proof is not the same thing as a new scientific claim.

## originality

FAIL

FAIL: An earlier publicly released 2026-10-24 full primary paper (manuscript dated 2026-10-23) by Scott Schubr, Degree laws and edge correlations for random forests, Theorem 1.2 (v1 PDF), proves the identical strict inequality for every complete bipartite K_{m,n}, m,n>=2 and every shared positive edge fugacity, with the same unrooted forest probability proportional to x^{|F|}, including isolated vertices. The audited result K_{3,b}, b>=2, is its immediate specialization m=3,n=b. This is conclusive stronger coverage, regardless of the different polynomial certificates and absence from initial citations.

## value

FAIL

FAIL for the single final claimed result: the central all-b, all-x strict edge-covariance statement is a known special case of an earlier broader theorem and hence does not close an unknown mathematical gap. The explicit K3b polynomial factors are a correct alternative calculation that could be independently useful, but they are not separately established here as an original motivated invariant that rescues the already-covered main claim; no repaired narrower claim/files supplied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
