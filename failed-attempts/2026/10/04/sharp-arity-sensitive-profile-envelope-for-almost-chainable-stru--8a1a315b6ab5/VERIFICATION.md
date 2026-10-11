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

Kurilić's Fact 2.3 proves the stronger local statement that two \(m\)-subsets with the same intersection with the kernel induce isomorphic substructures. Since an \(m\)-subset can meet a \(k\)-point kernel in only subsets of size at most \(m\), the displayed upper bound follows. The singleton-predicate construction has kernel exactly the named points: omitting any named point lets a one-point partial order isomorphism send it to an unnamed point and violate its predicate. Every admissible kernel subset then occurs and yields a distinct induced type. The bundled verifier was read and its finite replay is consistent with this proof.

## originality

FAIL

The claimed refinement is already a direct consequence of the exact mechanism printed in Kurilić's proof, not a new structural theorem. Fact 2.3 explicitly proves that isomorphism type factors through \(K\cap F\); retaining the tautological constraint \(|K\cap F|\le m\) gives the partial-binomial count immediately. Moreover the same paper's auxiliary construction in Fact 2.1 uses a linear order with singleton unary predicates naming the finite set, essentially the submitted sharpness mechanism. Under the required implication-based originality rule, the final sharp envelope is covered as a routine extraction from the primary source even though the numerical formula is not printed there.

## value

FAIL

The exact arity-dependent number is natural, but in this package it is obtained by a one-line cardinality restriction on the source's own kernel-intersection proof, and sharpness uses the source's standard named-singleton construction. That is a routine extraction rather than a new structural lemma, classification, or motivated boundary phenomenon under the common value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
