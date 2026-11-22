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

Weighted directed matrix-tree expansion gives each signed character as det L(s), with one signed outgoing arc per nonroot vertex. For odd n the number of trees n^(n-2) is odd, hence every coefficient odd; the constructed (n-1)-order unimodular skew sign matrix with row sums ±1 and root signs cancelling them has det 1. For even n the order n-1 is odd, and L(s) has all odd entries, so row subtraction forces 2^(n-2)|det L(s). The cyclic skew tournament matrix with all root weights +1 produces det(I-A)=2^(n-2), by product of (1-z^h)/(1-z) on the nontrivial odd roots (m=2h+1), while k=(n-2)/2 flipped root arcs yield det(D-J)=0 for n≥4. n=2 is nonsingular. Fourier diagonalization yields the stated Moore-Penrose norm. Independent integer determinant evaluation of both extremizers n=2..11 matched 1/2^(n-2) and even-order zero-star. Finite trials only corroborate the all-order determinant and root-product arguments.

## originality

PASS

The matrix-tree theorem and skew determinants are classical and not novel here. The new conjunction is universal exact MINIMUM NONZERO magnitude for all ordered parent-arc characters, constructive attainment in every dimension and the parity-complete inversion law; published undirected-graphic spectra and regular-matroid GCD statements do not imply it.

## value

PASS

A naturally defined counting convolution on the entire directed-tree indicator of complete bidirected graphs has a sharp quantitative recovery norm and an exact all-order singularity dichotomy; deriving the uniform sharp extremizers is more than merely restating the matrix-tree determinant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
