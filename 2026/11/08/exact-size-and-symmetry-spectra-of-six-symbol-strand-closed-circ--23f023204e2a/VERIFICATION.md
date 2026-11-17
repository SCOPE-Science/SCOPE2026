---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Dinucleotide circular ambiguity is a directed closed walk; hence circular code iff its arc digraph is acyclic. Arc-reversing fixed-point-free complement gives symmetric source/sink elimination and an invariant topological order. The nine complement-orbits of unordered pairs each allow 3 states; all 3^9=19683 assignments can be exhaustively checked, with 48 complement-preserving relabelings. Independent complete brute-force acyclicity enumeration reproduced all coefficients F and all 48-group orbit coefficients G, totals 8383 labeled and 220 orbits, with 48 maximal labeled codes. Distinguishes complete finite search from an infinite classification; no inference for larger alphabets.

## originality

PASS

The Michel–Pirillo four-letter circular-code census and Pellegrini–Pirillo all-alphabet maximum tournament construction do not determine the full size-refined F(z) and 48-symmetry quotient G(z) for a six-symbol fixed-point-free complement. General graph-theoretic acyclicity criterion is used, not claimed new. No complete six-letter 8383/220 census found in searched published records; historical unindexed enumeration remains possible.

## value

PASS

The first complementary alphabet with three paired symbols supplies a natural exact finite census of all circular dinucleotide codes, not merely maxima. Complete cardinality coefficients, symmetry orbits and 220 constructive representatives form a reusable coding-theory benchmark without claims about biology or higher alphabets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
