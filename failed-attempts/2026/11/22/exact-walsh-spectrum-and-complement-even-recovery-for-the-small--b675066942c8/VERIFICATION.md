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

Double counting five-set extensions gives λ_j=(132,66,30,12,4,1) for j=0,…,5. For a fixed hexad, binomial intersection moments and the impossibility of a five-point intersection with another hexad give counts (1,0,45,40,45,0,1), proving complement closure. The expansion of (1−2)^|B∩S| gives 132,−12,4 at weights 0,2,4 and −12+64h(S) at weight 6; complement-paired blocks cancel odd weights and the block size six gives Λ(Sᶜ)=Λ(S). Counting by weight and hexad membership gives (−12:924, 0:2048, 4:990, 52:132, 132:2). Unnormalized Walsh diagonalization gives the stated rank, inertia, and recoverable complement-even subspace; the restriction has condition number 33, and the pseudoinverse norm is 1/4. The average of identity and complement translation is a norm-one ℓᵖ projection (it fixes constants), and each nonzero singular value is 4 modulo 8, giving total valuation 4096. Conditioning is on the recoverable range, not on the singular full space.

## originality

FAIL

No separately published table of this exact Walsh spectrum was located. Nonetheless the reported table and recovery follow mechanically from the classical degree-five polynomial-averaging theorem on the Johnson slice for the known W12 5-design. In fact on J(12,6) put P_S(x)=∏_{i∈S}(1−2x_i). For k=|S|≤5 its hexad sum is 1/7 of the full-slice sum by Godsil's Lemma 10.12.1 and 132/924=1/7. For k=6, apply exactly the same theorem to P_S−64∏_{i∈S}x_i, of degree at most five. On the slice the removed monomial is simply the indicator of the single point S, with sum h(S) on the design and 1 on the slice. The full-slice sums are the elementary shell coefficients [z⁶](1−z)^k(1+z)^(12−k), namely 924,−84,28,−20 at k=0,2,4,6 and zero at odd k. Thus the only residual in the entire transform is the known hexad-membership indicator at k=6, yielding −20/7+64(h(S)−1/7)=−12+64h(S); weights above 6 are reflected because all blocks have even weight. There is no unanalyzed intersection parameter. Counting and spectral projection are immediate once this prior specialization is made. This is demonstrated implication, not an allegation that the exact Walsh table was printed or that the self-match has prior precedence.

## value

FAIL

The design and its spectrum are natural, and the correct table can be useful for reference, but in this narrow result the full spectrum is mechanically forced by the general polynomial-averaging identity on the known design, plus one point indicator and binomial arithmetic. The range, condition number and valuations are immediate read-offs rather than a separate recovery theorem that resolves a further mathematical gap. The record does not establish a surviving independent exact invariant or other nonroutine conclusion beyond this specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
