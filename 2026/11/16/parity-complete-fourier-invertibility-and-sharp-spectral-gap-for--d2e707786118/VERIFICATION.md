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

Verified signed matrix-tree cofactor equals the unnormalized Walsh coefficient, including negative edge signs. Symmetric/antisymmetric rail diagonalization gives W_a=(product a_j)/2 det(H_n(a)-2I). The standard path Laplacian eigenvalues yield W_rung=-sin(pi n/2). The ladder recurrence tau_n=4tau_(n-1)-tau_(n-2), tau_1=1,tau_2=4 gives tau_n odd iff n odd, hence every signed tree sum odd and nonzero. For even n, the length-four periodic u=(1,-1,-1,1,...) has H_n(a)u=2u for arbitrary signs on even-numbered links, producing 2^{m-1} distinct zeros. Independent exhaustive tree enumeration and integer Walsh transform for n=1..5 gives tau=1,4,15,56,209, zeros=0,6,0,200,0, and odd min=1. Finite checks corroborate but infinite proof comes from determinant/parity.

## originality

PASS

Bounded best-of-knowledge PASS for the attained global parity classification and exact least multiplier. Raff and Desjarlais-Molina cover only unsigned ladder spanning-tree counts, while weighted matrix-tree theorems give computational tools but not the signed zero-set classification. Similar wheel/K_{2,n} findings in Resultary refer to other graphs; the returned same-title Resultary entry mirrors this claim and is not evidence of independent priority. An unindexed earlier signed-ladder evaluation remains possible.

## value

PASS

Grid-strip spanning-tree indicators are canonical Boolean Fourier objects. Exact invertibility dimensions, attained least singular value and exponentially many explicit complementary null frequencies are a structural, natural infinite-family classification not implied by the unsigned tree count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
