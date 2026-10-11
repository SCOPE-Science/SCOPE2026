---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For a well-formed weighted projective space the hyperplane class is Cartier exactly at multiples divisible by every weight, so the Picard index here is \(\operatorname{lcm}(a,b)=a(a+d)/\gcd(a,d)\). The same-snapshot triangular classification gives \(0\le d\le r,1\le a\le r+d\) canonically and the strict versions terminally. Splitting off the maximal-difference boundary and using \(\operatorname{lcm}(a,b)\le ab\) proves the claimed unique maxima; at the proposed maximizers the relevant gcd is one. The inspected verifier independently checks Reid--Tai ages, the triangle conditions and the maxima for \(2\le r\le60\).

## originality

FAIL

At the exact audited repository snapshot, a previously published SCOPE result already gives the complete canonical and terminal parameter triangles for \(\mathbb P(1^r,a,b)\). Springer's primary Picard-index paper states that for a weighted projective space \(\operatorname{Pic}=\bigcap_i w_i\mathbb Z=\operatorname{lcm}(w_i)\mathbb Z\), including a higher-dimensional example. Combining those two stronger ingredients reduces the assigned theorem to maximizing \(\operatorname{lcm}(a,a+d)\) over two explicit integer triangles, and the package proof does so using only the elementary bound lcm \(\le ab\), a boundary split and gcd-one at the corner. Under the required implication-level standard this is a routine optimization of already published complete input, not an independent scientific result.

## value

PASS

The extremal Picard index is a natural geometric invariant and the exact maximizers across canonical/terminal families are mathematically useful. The record is rejected only because, at this snapshot, the result is too directly implied by an existing full parameter classification plus the standard lcm formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
