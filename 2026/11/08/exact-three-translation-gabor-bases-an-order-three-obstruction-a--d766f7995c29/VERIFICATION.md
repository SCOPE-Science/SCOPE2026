---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Fourier inversion on the M modulation frequencies makes orthonormality equivalent to each 3x3 fiber matrix H_j having mutually orthogonal rows. Along the k-translation cycle, any consecutive three projective vectors are orthogonal, forcing projective period 3; therefore order t=N/gcd(N,k) must be divisible by three. When 3|t, d residue cycles in Z_M of length M/d each admit exactly six projective line patterns, determined by a cyclic permutation matrix and the unique order-three complex Hadamard/cyclic triple conditions; each of M free phase scalars yields q^M choices iff 3|q. Therefore count=6^d q^M, normalized count=6^d q^(M-1), and continuous solutions form exactly 6^d copies of T^M. Independent direct fiber tests covered 33 parameter cases / 94809 arrays, plus direct complex full Gram checks in inspected verifier; these do not replace cycle proof.

## originality

PASS

General finite Gabor block-decomposition and local circulant Butson order-three classifications are known, but the relevant primary literature does not directly provide the global translation-order obstruction, exact labelled q-phase count and continuous component topology for this critical {0,k,2k} translation family. Closest Resultary three-translate tight-frame result has N even and all even modulations (overcomplete), while the two-translate ONB result uses two shifts; neither implies the present count by parameter renaming.

## value

PASS

Classifying when a natural critical finite Gabor synthesis system is a basis and enumerating every flat phase mask is an exact frame-design problem. The order-three arithmetic obstruction and number/topology of admissible windows determine feasibility and design space rather than only showing examples, and are not a trivial restatement of the local Hadamard condition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
