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

In F_q[[t]], writing f=t+A with leading term a t^(r+1), the linear copies of A cancel in f∘f−t and the first possible coefficient is (r+1)a² at degree 2r+1. This gives both even-depth cases, including equality 2r+1=m where the term is discarded. For odd r, a first nonzero term b t^k of f∘f−t at odd k would give a nonzero mixed coefficient (k−r−1)ab at degree r+k in the difference of the two compositions with f, contradicting commutation. At even k≥2r+2, perturbing the coefficient in degree s=k−r by u changes the degree-k obstruction by (s+r+1)au=au; all cross terms from higher coefficients or higher binomial powers occur later (2s−1>k), and later coefficients cannot change this equation. Hence exactly max(0,floor((m−1)/2)−r) coefficients are forced and all others following a are free. Summing the common shallow-odd weight and geometric unrestricted tail, with the admissible even boundary r=h for odd m=2h+1 and even h, gives both totals including the identity and covers m=3. At fixed q the remaining depths have O(1/m) relative mass, so the uniform odd-depth grid proves the weak limit. The frozen check.py and checked_output.txt were inspected as bounded supporting evidence, not executed; the arbitrary-field and arbitrary-depth conclusions are analytic.

## originality

PASS

The supported distinct result is the full characteristic-two finite-quotient depth histogram and its asymptotic law, not the previously counted depth-one stratum, a particular small quotient, or the formal torsion classification. No equivalent or dominating census was found in the compared passages.

## value

PASS

This computes a natural torsion invariant of the whole filtration, including non-lifting elements missed by the formal classification. The equal shallow-depth multiplicity and its limit are structural information, rather than more data at a few arbitrary truncations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
