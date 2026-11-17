---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

On K_(n,n,n+1), first two part degrees 2n+1 are odd and hence become homogeneous after one update; third part with degree 2n may retain its bit pattern only on a+b=n. If a+b !=n, first updated triple is homogeneous and reaches consensus or one of 001<->110 at update two. If a+b=n, opposite first two uniform bits with min(a,b)<c<=max(a,b) generate the extra primitive two-cycle family, otherwise consensus. Binomial-weighted disjoint cases yield B_n as the displayed S_n(a,b) double sum; already-periodic core=2^(n+2)-2; all states periodic by time2. Exact small-n counts independently checked B_n=6,22,252,1526,14296,98092 for n=1..6. For m_n>n with m_n/n->lambda >=1, three centered binomial sums obey multivariate CLT, tie probability O(n^-1/2), and Gaussian sign correlation gives Phi(lambda)=1/4+(asin(lambda/(1+lambda))-2asin(1/sqrt(2*(1+lambda))))/(2pi). Phi(1)=1/6, Phi(infty)=1/2; at exact m=n, balanced basin O(n^-1/2)->0. Distinction between limiting m/n=1 from above and exact m=n is essential.

## originality

PASS

Best-of-knowledge distinct exact result after comparing named equivalent, broader and database formulations; known subclaims explicitly credited, with residual priority risks.

## value

PASS

The exact basin census, a positive 1/6 oscillation-basin limit after one extra vertex, and a Gaussian interpolation curve show a genuine singular structural sensitivity of majority attractors, beyond previously known periodic-core counts and the balanced-graph square-root rarity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
