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

Parity forces the left quotient D to be in G. If the group coordinates of the bracketings are P and Q, the quotient is P Q^-1 for even parity and Q^-1 P for odd parity, by the four multiplication rules. Expanding gives the displayed commutators in sectors 001, 010, 100, 011, 101 and 110; each fixes a free third variable and changes the other two bijectively to a commutator pair. For example, 101 uses u=c^-1 a and [u^-1,b]. In 111 the resulting commutator can be written [b^-1 c,b^-1 a] by conjugating both arguments, so fixing b again gives a bijective parametrization. Thus the seven sector counts are n C_G(g) and 000 contributes n^3 only at identity. Normalization by 8n^3 and the classical Frobenius formula give the character expression, which is unchanged under g -> g^-1. Sector 001 realizes every commutator, and the subgroup they generate inside G is precisely the associative subloop [G,G]. The symbolic proof applies also in the trivial and abelian cases; the supplied examples are not needed for generality.

## originality

FAIL

A distinct indexed Resultary record gives the same exact all-target law for every finite group and the same equality of the seven individual nonzero-parity sector fibers. Its associator convention is not pointwise identical in every sector, but the explicit tables give independent bijective coordinates to the same group commutator in each sector, so the convention change yields no distinct fiber statement. This is demonstrated mathematical overlap, not an inference about priority from the shared date.

## value

FAIL

The full nonidentity distribution is a natural invariant and is richer than the classical association probability, but the assigned formulation adds no useful new statistic or case to the demonstrated exact coverage. Changing the quotient convention leaves the entire stated law unchanged, and the support and character reformulations require no further structural result. There is no distinct pointwise comparison or convention-dependent phenomenon in the submitted conclusion to carry value as a narrower repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
