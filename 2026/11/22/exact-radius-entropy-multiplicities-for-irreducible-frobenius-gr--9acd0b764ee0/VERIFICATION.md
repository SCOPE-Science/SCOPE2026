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

An irreducible nontrivial action of prime order has field algebra F_(p^d), with d = ord_q(p); each nonidentity complement element is fixed-point-free on V. A normal subgroup disjoint from V centralizes V, hence is trivial; a nontrivial intersection contains V by irreducibility. Thus factor endomorphisms are trivial, automorphisms, or quotient maps with complement image. Images of different coordinate restrictions commute, forcing either one automorphic coordinate or a single common complement. The inverse of the quotient restricted to a given complement fixes the identification for counting; the zero rule is counted once. Automorphisms have d Frobenius exponents, v-1 choices of field multiplier, and v choices of image for the complement generator at each exponent. For the automorphism branch a finite iterate removes the coordinatewise automorphism. For the quotient branch time iteration after one step occurs in the complement shift; the initial observation contributes at most a bounded factor to the number of orbit names for each fixed observation window. The scalar Laurent width counts the added coordinates per time step: on a contiguous observation window at least as long as the width, the two extreme nonzero coefficients recover the newly exposed left and right coordinates by triangular elimination (omitting a side when its reach is zero). Thus the entropy is the width times log q, including the width-zero case. At positive width k the one-sided supports have 2(q-1)q^k choices when k<=R; two-sided supports have c_R(k) possible pairs of endpoints and (q-1)^2 q^(k-1) choices per pair. Unique factorization separates the positive entropy branches. The normalization at zero and the total follow from the two classes of local rule.

## originality

PASS

The distinct supported contribution is the family-wide rule classification and explicit centered-radius entropy multiplicities. The S3 classification and the general scalar entropy identity are not credited as new. Relevant general algorithms provide per-rule computation, not this family-wide closed census.

## value

PASS

This is a natural nonabelian family where the local homomorphism constraint can be solved exactly. The dichotomy identifies which entropy-generation mechanisms are possible, and the radius multiplicities count their prevalence without enumerating all finite local maps. That is information not supplied by per-rule entropy computability or by the spectrum alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
