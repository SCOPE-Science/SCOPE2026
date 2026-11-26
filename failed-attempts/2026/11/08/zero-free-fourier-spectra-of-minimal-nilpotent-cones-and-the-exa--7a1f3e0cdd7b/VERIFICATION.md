---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For each image line L=F_q u, the matrices in the cone with image contained in L are the maps uv^T with v^T u=0. Their exact character sum is q^(n−1) if A stabilizes L and zero otherwise, since a nonzero restricted F_q-linear functional is surjective and ψ is nontrivial. Each nonzero cone point belongs to a unique such subspace, and zero belongs to all (q^n−1)/(q−1) of them. Correcting for zero proves q^(n−1)E(A)−sum_(j=1)^(n−1) q^j, including every prime-power order and dimension n≥3. At A=0 this agrees with the stated cardinality. Unitary Fourier diagonalization in counting ℓ² gives the absolute multipliers as singular values, with the largest attained at zero and all nonzero by the mod-q² residue. Write B=sum_(j=1)^(n−2)q^j; the multiplier is q^(n−1)(E−1)−B. For q≥3 the closest integer is E=1 (one Jordan block already realizes it). For q=2, E=2 realizes 2 using blocks of sizes n−1 and 1 with distinct eigenvalues; when n=3, E=1 also gives modulus 2, with no claim of uniqueness. In size three the irreducible cubic, quadratic-plus-linear and six split Jordan types exhaust the matrices. The potentially subtle same-eigenvalue (2,1) type has commuting matrices [[a,b,c],[0,a,0],[0,d,e]], with determinant a²e, yielding the stated unit-centralizer order q³(q−1)²; other centralizers are products of field units, units of a truncated polynomial ring, GL₂ and/or scalar units as appropriate. Multiplying each orbit size by its eigenvalue/polynomial choices gives the table; combine equal absolute values when reading singular multiplicities. `python3 /workspace/independent_checks.py 3` directly summed residues on the cone at all q^9 frequencies for q=2,3, confirming the signed tables. The supplied checker was inspected, not run.

## originality

FAIL

The central eigenline formula is mechanically implied by the published rank-one bilinear-forms spectrum via a single scalar-shift average. The nonvanishing and sharp norm follow by integer spacing and immediate Jordan witnesses. The size-three table regroups standard similarity types and orbit sizes under the same formula. I found no evidence that an earlier source literally printed the final seven rows in this notation; the rejection rests on affirmative prior implication, not on Letellier access or an empty search.

## value

FAIL

The cone and spectral invariant are natural, and the self-contained derivation can be useful exposition. As an exact new mathematical contribution, however, the frozen finding evaluates a one-step character restriction of a known spectrum, takes its elementary spaced-integer minimum, and recodes known class counts for n=3. No further structural statement or independently substantive surviving invariant was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
