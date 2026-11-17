---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For K_(a,b), independent simultaneous parent samples give cross-part covariance z=qz=0, within-part x=q[1+(b-1)y]/b, y=q[1+(a-1)x]/a with q=(1-epsilon)^2. The temporal Markov kernel alternates between uniform part supports and gives R_(2l)=c^(2l-2)y; sign symmetry determines the entire pair law. At epsilon=1/2, y=(a+4b-1)/(15ab+a+b-1). Setting y=1/(3n+1) yields (5a-4n-1)b=n(a-1), satisfied identically by a_j=1+j(n-1), b_j=jn/(5j-4), n=2*lcm_j(5j-4). This ensures integrality, both parts >=2 and strictly increasing largest part a_j, including k=2. No step infers unbounded k from finite checks.

## originality

PASS

Best-of-knowledge PASS with restricted credit: the already-published pairwise nonidentifiability is excluded; the new quantified fixed-noise arbitrary finite multiplicity is established constructively and not implied by the examined Theorem 6.1(4).

## value

PASS

Graph reconstruction from local noisy dynamics is a natural inverse problem. The theorem rules out every uniform finite candidate bound even if every two-time stationary statistic is known exactly at a fixed standard rate; this is qualitatively stronger than a second example of ambiguity, without asserting full-stream indistinguishability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
