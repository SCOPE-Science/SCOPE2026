---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For P_j(x)=∏_{h<j}(x−h), at least floor(j/7) factors vanish modulo 7. For a divided difference with x,y in the same residue disc, the telescoping product formula retains at least floor(j/7)−1 such factors in every term. This gives uniform convergence and, modulo 7, truncation of the divided difference to j<14, where it reduces to the derivative at the disc representative. The exact finite value and derivative rows for F(a)=Σ(−1)^j P_j(a) are (1,0,1,5,2,5,6) and (1,5,4,1,5,1,3). All derivatives are units. Hence F preserves the seven-adic distance within each input disc; on each finite reduction this is an injection into the output disc, and since the two discs have equal finite cardinality it is a bijection. On nonnegative integers F(n)=(−1)^nD_n. Each class modulo 7^k occurs once in each parity during 2·7^k indices, so the signed branch values give (2,3,3,0,0,3,3) at every level. This proves the index densities and the measure 5/7 of the closure. The period divides 2·7^k; modulo 7 the divisors 1, 2 and 7 are excluded by (D₀,D₁), (D₁,D₃) and (D₀,D₇). Any higher-level period is then even and divisible by seven, and the isometry on 7ℤ₇ forces it to be divisible by 7^k by comparing F(T) with F(0). A separate exact script using dual numbers for the derivative and the signed recurrence corroborates the table, counts through k=5, and first-level surjectivity at 2, 3, 5. The universal lifting proof does not rely on extrapolation.

## originality

FAIL

A separate indexed record, Exact seven-adic fibers of the derangement numbers (ed49d5358733), states the same five supported residue classes at every level, exactly two or three indices per supported residue in a least period, and that the seven input branches are isometries. Those available statements already yield the evaluated vector, not merely a possible overlap: modulo seven the known least period has 14 indices and five supported residues, so exactly one residue has multiplicity two. Pairing indices differing by 7 negates the value modulo 7, so that unique residue is 0. Each isometric input branch maps onto its entire output residue disc and gives exactly one lift of each output in that disc at each finite level. Parity splitting transfers the base multiplicities unchanged to all lifts. The densities and Haar measure follow immediately. The remaining first-prime comparison is a direct base check using D₀=1, D₁=0, D₃=2, D₄=9, and D₈=14833 to cover all residues at 2, 3, 5; those surjectivity cases are also covered by separate indexed small-prime results. Hence this finding does not establish a distinct contribution, irrespective of relative priority between the two same-day records. This is not a claim that their body texts are identical.

## value

FAIL

Exact derangement residue fibers are a motivated arithmetic invariant, and the proof is useful exposition. As a separate finding, however, its exact seven-adic law is mechanically recoverable from the indexed branch and multiplicity result, and the only extra framing, minimality of the first excluded prime, uses immediate small-prime reductions. There is no surviving distinct unknown exact fact of independent scientific value in the submitted claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
