---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For a finite theory using raw nouns \(p_1,\ldots,p_r\), the \(2^r\) Boolean membership atoms partition every finite model. Assigning a nonnegative integer count \(z_\varepsilon\) to each atom makes every Boolean noun cardinality a \(0/1\)-linear form. Inclusion, nonempty intersection, weak cardinal comparison and strict cardinal comparison become Presburger equalities/inequalities, and existentially projecting the atom counts while retaining \(N=\sum z_\varepsilon\) gives an effective Presburger definition of the finite spectrum. Replicating every element \(m\) times preserves every atomic truth value, including strict comparisons, so spectra are dilation-closed. The displayed \(k\)-block theory really partitions the universe into \(k\) pairwise-disjoint equal blocks, yielding exactly \(\{kn:n\ge1\}\). Jiang's complete primary PDF was inspected at Section 5.1 and independently confirms the same construction for \(k=3\).

## originality

FAIL

The global Presburger/semilinearity conclusion is already subsumed by Boolean Algebra with Presburger Arithmetic (BAPA/QFBAPA), a mature logic expressly designed for Boolean set operations together with set cardinalities and Presburger arithmetic. The submitted finite-theory translation is exactly the standard Boolean-atom reduction specialized to this syllogistic syntax. Jiang's own Section 5.1 already gives the noun-level union/complement language and the exact divisibility-by-three spectrum. Generalizing that displayed three-block example to arbitrary fixed \(k\) is a direct parameter replication. Thus both the upper-envelope theorem and the showcased family are mechanically implied by established frameworks/results.

## value

FAIL

Once BAPA/QFBAPA is recognized, the semilinearity theorem is a routine application of a standard logical translation rather than a new structural result. The arbitrary-modulus family is also obtained by repeating Jiang's three equal disjoint blocks with \(k\) blocks. This is correct and clarifying, but it is exactly the kind of known-framework deduction and parameter substitution that the value standard excludes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
