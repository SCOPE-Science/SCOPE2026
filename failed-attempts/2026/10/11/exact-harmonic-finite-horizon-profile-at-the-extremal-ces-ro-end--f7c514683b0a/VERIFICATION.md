---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Telescoping W^k gives norm^p=sum_{j>k}(j/(j−k))^beta |x_j|^p. For q0/p=1/beta, Minkowski on the nonnegative coordinate contributions gives upper constant max_j A_{j,N} where A_{j,N}=j sum_{k<min(N,j)}(j−k)^−1; each contribution has exact ℓ^(1/beta) norm |x_j|^p A_{j,N}^beta. For j<=N, jH_j<=NH_N; for j>=N, summands j/(j−k) decrease in j, attaining at N. e_N gives equality. Normalization N=1 and countable monotone truncation checked; separate numerical j scan N=1,2,3,4,8,15,30 merely corroborative.

## originality

FAIL

Abbar–Arnold–Coine Theorem 3.4 proof for general q>=p weighted backward shifts already obtains the fixed-horizon Jensen upper bound by a maximum over basis coordinates, with equality for a basis vector. For the specific weight omega_j=j^(−beta/p) and q=p/beta, this reduces to max_j (j/N)sum_{k<min(N,j)}1/(j−k), whose maximum is H_N at j=N. Thus the whole exact finite-horizon claim follows by elementary specialization from a strict broader published theorem/proof, irrespective of the earlier paper emphasizing global constants. The later Arnold H_j lower bound is also prior; its inaccessible full text is not the basis of failure.

## value

FAIL

The exact harmonic N-step endpoint profile is well motivated, but for this particular shift the general earlier weighted-shift fixed-horizon Jensen theorem already settles the optimization by basis vectors. The only remaining step maximizes a monotone harmonic sum at j=N and reproduces Arnold’s known H_j witness; this narrow specialization contributes no new nontrivial structural phenomenon, classification, or motivated unknown beyond the published general proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
