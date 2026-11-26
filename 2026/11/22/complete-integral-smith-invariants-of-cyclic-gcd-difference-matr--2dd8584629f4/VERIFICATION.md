---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Let a=p−1. Expanding a proper r-minor of aI+J by columns uses at most one J-column in any nonzero term and gives divisibility by a^(r−1). Taking rows 0,…,r−1 and columns 1,…,r and subtracting the unmatched row realizes exactly ±a^(r−1), including r=1. The full determinant is a^(p−1)(a+p), so the consecutive determinantal-divisor ratios are precisely the claimed local multiset, including {1,3} at p=2. CRT factors the numerical gcd of the difference for squarefree N, making the matrix the Kronecker product after reindexing. Both tensor products of the local Smith transformations are unimodular by tensoring their integral inverses. Thus the product entries form an integer diagonal presentation; sorting valuations separately and aligning equal positions is the structure theorem over each prime and then CRT, not a sort of the unsplit integer entries. The determinant formula also follows from the positive prime-factor determinants and the tensor determinant identity. For modulo ell, if a vanishes the local matrix is J, of rank one; otherwise a times the identity plus a rank-one perturbation has kernel at most one-dimensional, and its determinant vanishes exactly if ell divides 2p−1. This includes ell=p without any eigenspace decomposition assumption. Tensor ranks multiply. The generator number is the maximum dimension of the cokernel modulo a prime. The minimum total rank is one at ell=2 for odd N, and at most two for even N by ell=2. For even N rank one forces ell=3 by the factor at p=2, and every odd local factor then has rank one exactly for p≡1 mod 3. Otherwise ell=3 has a factor of rank at least three, and ell=2 is a minimizer. N=2 is the separate one-generator case. This proves the all-N statements directly without extrapolating numerical samples.

## originality

PASS

The supported contribution is the whole squarefree numerical-GCD circulant classification, with the sharp arithmetic generator-count dichotomy at composite even orders. Local rank-one Smith arguments, CRT, tensor operations and invariant-factor alignment are classical. The closest exact matches address the same cyclic kernel at prime-power order, with demonstrable overlap on the largest factor at prime order; the compared results do not state the full invariant alignment at general squarefree order or the global generator dichotomy. The ordinary divisor-indexed or index-pair GCD and Ramanujan determinants are different matrices.

## value

PASS

The numerical GCD difference kernel is a natural arithmetic convolution on a cyclic group. The output gives its complete finite integral cokernel uniformly, retaining mixed-prime information not supplied by a determinant or rational spectrum. In particular the exact generator count distinguishes even squarefree orders according to the residues of all their odd prime factors modulo three. This arithmetic distinction and the complete family prescription are the useful content; the local rank-one Smith calculation alone is routine.

The dated certificate retains the supplied scientific assessment, sources and limitations.
