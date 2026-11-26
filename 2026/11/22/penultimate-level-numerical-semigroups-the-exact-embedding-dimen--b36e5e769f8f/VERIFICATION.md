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

Independently establish the unrestricted theorem using the Apéry set at m. If a tuple fails, its total belongs to the Apéry set, and each partial sum does too: subtracting m from a partial sum in S would give the same possibility at the total. From zero through the total these are m strictly increasing elements, exhausting the m residue representatives. All but the first positive partial sum are decomposable, so there is only one generator other than m (at least one by cofiniteness). Write S=<m,a>, a>m and gcd(m,a)=1. If any tuple member uses a copy of m, subtraction succeeds directly. Otherwise all entries are positive multiples of a; a total containing m or more copies of a admits replacing m of them by a copies of m. The only remaining tuple is the all-a tuple, whose defective sum is the greatest of the residue-class gaps ja−m, 0≤j<m, and hence is Frobenius. This independently gives the same exact witness as the frozen zero-sum and gap-reflection route. Inspection also confirms that the supplied Kunz checker is bounded (multiplicities 3–7, coordinates 1–4, recorded 2344 cases); it was not executed and was not needed for the universal proof.

## originality

PASS

Restrict credit to the uniform penultimate-level classification paired with the exact unique ordered obstruction and its Frobenius value. Prior work defines the hierarchy, gives the endpoint and explicit m=5 examples, and supplies the zero-sum, two-generator and Apéry ingredients. The inspected sources did not give the resulting uniform equivalence with ordinary embedding dimension and unique witness. An Apéry exhaustion argument is short and natural, but the cited prior results are ingredients rather than a classification or a direct lookup of this last proper tier.

## value

PASS

The last proper level of an existing hierarchy is a natural uniform boundary, not an arbitrary finite slice. A simple invariant decides it for every multiplicity, and the theorem describes precisely which tuple fails and what gap it produces. This links hierarchy membership to an elementary generator test while explaining the entire extremal obstruction, beyond the previously exhibited examples or the all-semigroup endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
