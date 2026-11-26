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

Deleting the hub gives the direct sum of grounded arms with the original degrees retained. In the lower Krylov columns the leading terms, in order, are u,Bu,…,B^(N−1)u; hub feedback only adds earlier columns with integer coefficients. For each arm the distance support of e₁,−D e₁,… gives a unit triangular basis. In those bases the block matrix is simultaneous remainder by the monic arm characteristic polynomials, with the argument sign changed for −D. To verify the pairwise product determinant, split off a monic factor P by writing f=r+Pq: the coordinate change is unit triangular up to ordering, the P-remainder is r, and the other remainders in q are multiplied by P. Each multiplication has determinant equal to the corresponding resultant, including zero when a factor is shared. The arm recurrence gives eigenangles (2j−1)π/(2ℓ+1). A common gcd g>1 gives the common angle π/g; if the odd labels are coprime, multiplication by the other odd label permutes the odd residues up to sign modulo 2(2ℓ+1), fixing the excluded odd residue 2ℓ+1. Thus the absolute numerator and denominator cosine products agree, giving resultant modulus one. This yields the integer index classification, not just an eigenvector test. The binomial translation to I−L is integral and unit triangular; column reversal is the n-step input map, and Cayley–Hamilton precludes recovery at a longer horizon if rank fails. In the full-rank case the symmetric spectrum is simple and the modal Vandermonde gives the stated finite-horizon determinant; its time kernel is positive definite by independence of distinct exponentials. Independent edge-by-edge Krylov recurrence and elimination modulo 1009 gave residues (1,0,0,1,1) for arms (1,2,3,5,6,8), (1,2,3,5,6,7), (2,7,9), (3,5,7,11), (4,5,6,8,9), unchanged by the shift. These residues are corroboration only; the packaged exact checker was inspected, not run.

## originality

PASS

Qualitative reachability and Chebyshev resultant machinery are precedent, not contributions. The supported distinct claim is the zero-or-unit determinant and full integer column lattice for arbitrary hub-actuated unit spiders. The closest separate indexed tree census mentions this family as related known work but gives neither an independent all-arm theorem/proof nor a demonstrable earlier exact antecedent. The conclusion is not a publication-priority certification.

## value

PASS

A natural infinite family with genuine branching admits a complete exact gcd test for whether unbounded integer controls realize every integer state in n steps. A rank test cannot decide that lattice question, and the nonspider index-two example confirms that unimodularity is not automatic for unit trees. The output is useful without any claims about optimal placement, small input size or numerical conditioning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
