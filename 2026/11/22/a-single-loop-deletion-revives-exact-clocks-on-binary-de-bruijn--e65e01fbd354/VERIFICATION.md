---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The disjoint extension sums give im(A^t) exactly the functions of a suffix of length m−t for 0≤t≤m. Applying A to a constant multiplies by two, so A is nilpotent with sharp index m+1. The linearly independent suffix indicators v_j=A^je satisfy Bv_j=v_{j+1}+v_0 for j<m and Bv_m=v_0; their cyclic span W has characteristic and minimal polynomial h_m=1+z+…+z^(m+1). As a separate check, the rank-one determinant lemma and eᵀA^je=1 for 0≤j≤m give full characteristic polynomial z^(N−m−1)h_m. The cyclic vector has exact period m+2: h_m divides z^(m+2)+1 but divides no shorter binomial, by degree and the internal coefficients at d=m+1. The quotient by W induces the nilpotent A. The intersection W∩im(A^t) consists exactly of the indicators indexed j≥t: if a nonzero earlier coefficient has least index j, comparing the all-zero word with one differing in position j+1 gives distinct values despite identical final m−t bits. Since im(B^t) contains W and has the same image modulo W as A^t, its rank is 2^(m−t)+t up to m and m+1 thereafter. This proves the last strict decrease at m−1 for m≥2; m=1 is wholly recurrent. In the Fitting decomposition the nilpotent kernel has dimension N−r_t, and it independently supplies the entry shells while the cyclic W supplies periods. On W, the polynomial gcd counts fixed vectors, including repeated factors; explicitly for d|m+2 its degree is d if v₂(d)<v₂(m+2), otherwise d−1. Möbius inversion and division by primitive period give the stated joint and orbit counts. VERIFICATION.md and both supplied scripts were inspected, not executed; the state script checks entry shells and return after m+2 steps, not every primitive-period count. Those counts follow from the cyclic-module proof.

## originality

PASS

The supported distinct claim is the exact effect of the specified loop deletion: the recurrent cyclic module together with the entire rank profile and the temporal/entry census in characteristic two. Standard rank-one perturbation, Fitting decomposition and Möbius inversion are ingredients and not independent novelty claims. Inspected sources treat the unedited graph, a different word graph, or general spectral perturbation, not the full deletion result. This is a bounded best-of-knowledge assessment, not a priority certification.

## value

PASS

The constant-word loop is canonical and its deletion supplies an exact sensitivity result: from total extinction it creates a recurrent clock of growing length and changes the full transient-depth profile. The quotient calculation yields exact joint counts for all field sizes and word lengths, including cases where repeated roots matter and where exponential state enumeration is impractical. This is more informative than the routine rank-one characteristic-polynomial calculation alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
