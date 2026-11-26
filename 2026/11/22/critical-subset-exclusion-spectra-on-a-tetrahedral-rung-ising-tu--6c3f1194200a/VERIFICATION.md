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

Re-derived the Hamiltonian in units J: a column contributes 6-8r+2r², the next interface contributes 4-2r_i-2r_{i+1}+4t_i and the field contributes -(h/J)(4-2r_i). This gives the stated global identity without double-counting C_3. At h/J=3 the shifted energy is a sum of integer-nonnegative terms 2(r-1)(r-2) and 4t, so the equality constraints are necessary and sufficient and are attained by proper singleton colorings. Singletons contribute M=2, pairs zero. A trace counts closed indexed column words once, with the arriving-column weight counting each singleton once. The two-dimensional constant block and the three equivalent zero-sum direction blocks follow from BB^T=2I+11^T and complement acting as minus on the zero-sum image. On ker B the complement is +1: the minus space for the three complementary-pair swaps has dimension three and is already exhausted by the zero-sum image. Thus the polynomial and power-sum degeneracy hold, also at weights with coinciding eigenvalues. The odd minimum sector can be counted directly: zero singletons would force an impossible odd alternating complement sequence and one singleton would touch complementary pairs and have no allowed leg. With two adjacent singleton columns the intervening odd-length pair run has six initial choices and the singleton legs are distinct members of its complementary two-set, giving 12 possibilities. Nonadjacent singleton columns separate an odd and even pair run: the odd run gives six initial choices and two ordered distinct possible singleton legs; the even run has exactly two compatible initial pairs, giving 24 possibilities. Summing over the n adjacent and binom(n,2)-n other position pairs gives 12n(n-2). Pure singleton states give 3^n+3(-1)^n; for even n the zero sector has six alternating words. At h=3J the finite spectral gap to the other eigenvalues at y=1 gives asymptotically rho(e^t)^n for the polynomial near t=0, with a uniform exponentially small relative error there. The first two log derivatives are μ=1/2+sqrt(7)/14 and ν=3sqrt(7)/49, yielding the characteristic-function CLT and uniform ground-state magnetization mean. Independently built the ten-state matrix and checked the factor and derivatives symbolically: python3 /workspace/branches/replay_3_5/expansion_checks.py, matching .log. At h=5J the integer-nonnegative terms are 2r(r-1) and 4t. The five-state matrix splits into three eigenvalues -1 and the constant/empty block with trace 4 and determinant -1. Interpolation of the two energy identities gives exactly their equality-set intersection on 3J<h<5J; increasing h beyond 5J selects the unique state of maximal M in the critical set, the all-positive state. At h=0 the even-cycle states attaining both local exchange bounds are exactly the six alternating balanced columns; interpolation with the h=3J bound excludes all others for 0≤h<3J and even n. For odd cycles the immediate-left crossing is only a fixed-n assertion, justified by the finite gap above the critical ground energy. The archived bounded checker was inspected, not executed; the all-size results are analytic. The CLT is for the uniform labelled ground states at exactly 3J, and no full odd low-field or finite-temperature diagram is inferred.

## originality

PASS

Qualified for the weighted four-leg critical spectrum, exact odd-sector count and model-specific fluctuations. The subset-exclusion construction has a close earlier three-leg analogue, and hard-core counting at saturation and transfer-matrix CLTs are standard methods, not independent novelty here. The comparisons did not establish exact prior coverage of the four-leg weighted result.

## value

PASS

The two natural longitudinal-field boundaries of a frustrated clique-rung antiferromagnet have different critical ensembles. At coexistence, the ten-state spectrum controls both extensive ground-state multiplicity and the magnetization distribution; the odd-cycle obstruction gives a different extreme sector from the even cycle. The explicit fluctuation variance and endpoint entropy provide comparison quantities at fixed exchange and physically specified fields. The value is in the combined energy, parity and fluctuation classification for the natural K_4 tube, not the elementary fact that transfer matrices or the hard-core representation exist.

The dated certificate retains the supplied scientific assessment, sources and limitations.
