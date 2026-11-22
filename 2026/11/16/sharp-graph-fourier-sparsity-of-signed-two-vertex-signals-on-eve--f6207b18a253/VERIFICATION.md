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

The combinatorial path Laplacian has simple real cosine eigenvectors phi_0=n^-1/2 and phi_k(j)=sqrt(2/n)cos(pi*k*(j+1/2)/n). For every u<v, factoring phi_k(u) +/- phi_k(v) gives a product of cosine or sine functions at indices A=u+v+1 and B=v-u, exactly one odd. Converting each factor zero to c*k = n or 0 (mod 2n), counting zero indices k=0,...,n-1 by gcd, and distinguishing even n=2^t q (odd q) from odd n (least prime p), proves sharp support (n-q+1)/2 or (n-n/p)/2 and the reflected-pair/sign/optimizer enumeration. For n a power of two, q=1 ties both signs; for n=2 and n=3 boundaries give integer counts. Inspected actual RESULT.md, check_exact.py and check_dct.py at frozen Git blobs; verified algebraic examples P6/P9/P16 and checked bound/equality logic. Script enumerates n=2..80 exactly and DCT 2..22 with high precision, but the universal conclusion rests on modular proof, not finite logs.

## originality

PASS

Checked potential equivalence with arithmetic controllability of path nodes and graph uncertainty; those statements are for independent channels or general inequalities, not fixed signed equal-magnitude two-site Fourier support and exact all-location minima. Resultary returned the identical record and distinct graph/cycle results, not an independent stronger coverage; no claim of assured historical priority.

## value

PASS

The fully optimized, all-size two-site graph-Fourier uncertainty equality case has a natural graph-signal-processing motivation: it identifies sparse signed sensor/forcing geometries and exactly when reflected pairs and parity/gcd produce maximal spectral annihilation. Distinguishing sum versus difference for each path length and counting all optimal locations adds a structural classification beyond the familiar DCT formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
