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

For the Walsh sign at S, expand ∏_(i∈S)(1−2 I_i); maps avoiding j prescribed target labels number (n−j)^n. Grouping terms by j gives exactly the multiplier for counting-measure convolution, with no factor 2^(−n) or n^(−n). Odd n has only the odd j=0 summand modulo 2. For even n≥4 and k≥1, with a=v₂(k), the j=1 term has valuation a+1. The j=0 term has n v₂(n)≥a+2. For j≥2, j·C(k,j)=k·C(k−1,j−1) implies v₂(2^j·C(k,j))≥a+j−v₂(j). For odd j≥3 this is at least a+3; for even j the even base contributes at least n extra powers of 2 or the term is zero. Thus other terms cannot cancel the leading valuation. The constant term is n^n, and n=2 gives (4,2,0); Walsh multiplicities C(n,k) give rank three and nullity one at n=2, all other orders invertible, and the asserted determinant valuations. Exact vacancy counts are the surjection counts onto the complement. The provided checker was inspected, not run: it directly enumerates small kernels, then tests all degrees in a bounded range, not an all-n proof.

## originality

FAIL

The exact numerical theorem is true, but a distinct all-order arithmetic advance is not established against the strongest checked same-day comparison. The Cayley leaf-set law at 4027fa303a3d is the empty-symbol-set Walsh spectrum of n−2 independent uniform Prüfer labels. The frozen spectrum uses n independent labels in the same occupancy transform. Term by term its j-summand is the leaf-spectrum j-summand times (n−j)² for n≥3. The inspected Cayley proof, §3, establishes that at even n≥4 each j≠1 summand is individually divisible by 2^(v₂(k)+2), not merely their sum; the j=1 factor (n−1)² is odd and preserves the unique leading valuation. This immediately transfers the complete nonconstant valuation law, and the odd-n parity argument transfers as well. Thus the target does not only resemble the earlier-style statement: the decisive published-in-index termwise estimates already yield it by multiplying each term by an integer square. The n=1 edge and n=2 singularity follow by direct evaluation at three degrees and are not covered by the leaf theorem. This is a finding of mathematical dependence of the claimed advance on available evidence, not a determination of which same-day item came first or an attribution of copying.

## value

FAIL

Vacancy recoverability is natural, but the proposed substantive advance is the all-order dyadic law, which transfers from the inspected empty-symbol spectrum estimates by a two-step increase in the number of draws. The finite n=2 singularity is true and distinct from the corresponding leaf case, but is a three-coefficient calculation and no independent scientific need for that tiny residual instance is established. No new general normalization, stability result, or other surviving advance is demonstrated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
