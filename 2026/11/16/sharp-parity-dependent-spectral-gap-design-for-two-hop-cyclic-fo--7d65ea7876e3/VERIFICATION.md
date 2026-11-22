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

Fourier diagonalization gives sigma_k^2=2(1-cos(2pi k/n))(1+b^2+2b cos(2pi k/n)). This is a concave quadratic in cosine for b>0, so minimum over all nonconstant modes lies at largest and smallest cosine, reducing the full minimax to two endpoint-frequency curves. At n=3 they coincide and the global maximizers are b=0 or1. Even n>=4: low-frequency A_n(b) increases and antipodal B_n(b)=2(1-b) decreases, yielding the unique crossing b=(sqrt(1+sin^2(pi/n))-sin(pi/n))^2. Odd n>=5: A grows, high-frequency B decreases to b=d=cos(pi/n), then grows; crossing of A and B is b=h-sqrt(h^2-1), h=1+d-c, and the latter B branch cannot beat the crossing. Concavity plus strict inequality excludes extra minimizing modes; expansions yield max gain 4pi/n and factor-two asymptotic versus one-hop gain.

## originality

PASS

Fourier symbols of directed circulant Laplacians and polynomial graph filters appear in Chen–Cheng–Sun and Emirov–Cheng–Jiang–Sun. Segarra–Marques–Ribeiro optimize filters for operator approximation, a different objective. Resultary priced antipodal shortcuts use even-cycle undirected diffusion budget and cannot imply the directed 1-/2-hop least singular maximin or odd/even explicit tie modes. Best-of-knowledge PASS with recorded risks; no failure-to-find-is-proof-of-novelty inference.

## value

PASS

The fixed-budget two-tap stable difference operator is a natural graph-signal inverse problem. Exact optimal weights, full active modes and factor-two asymptotic improvement constitute an actionable sharp design even though Fourier diagonalization itself is classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
