---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the signed spectral certificate

Execute `python3 artifacts/verify.py` using standard-library Python 3. The script constructs the unweighted spider adjacency matrix for 24 triples with \(m\in\{3,4\}\), \(k\in\{3,4,5,6\}\), and \(\ell\in\{2k-1,2k,2k+1\}\). It directly computes \(p(A)\) via multiplication by the eigenvalue factors and checks: (i) every distance-\(d\) edge of the graph power has sign \((-1)^{k-d}\), (ii) every nonedge beyond distance \(k\) has a zero matrix entry within tolerance, (iii) matrix symmetry, and (iv) all explicit kernel vectors. Checked output:

```text
SPECTRAL_SUPPORT_AND_KERNEL_OK 24
VERIFY_OK
```

**Limits:** The program works in floating-point arithmetic at finite parameters; it does not constitute a proof for all integers or prove priority. The unrestricted proof is symbolic and uses eigenvector identities, walk parity, elementary symmetric functions of nonnegative roots, and the published inequality \(M(H)\le Z(H)\). Historical literature searches and comparisons are recorded in AUDIT.json; independent mathematical review was not performed.
