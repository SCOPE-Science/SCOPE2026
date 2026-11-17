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

Strong Wang–Wang factor-free convention, not the weaker cross-fix-free notion. All codewords share first 0 and last 1 up to complement. I independently enumerated the entire finite feasible length range (lengths 2..12, because any total <=16 with three distinct words and minimum length two has maximum <=12) and tested self-border, cross-prefix/suffix, and factor exclusion. Exactly two oriented triples exist at total <=16: (00011,01011,010011) and (00101,00111,001101), each total 16; complementation gives four, and reversal/complement map the two. This establishes the global lower bound and equality classification by exhaustion of a rigorously bounded search domain, not partial length experiments.

## originality

PASS

The earlier fixed-max-length census already reports T_6=16 at maximum cardinality three, so that restricted optimum receives no novelty credit. It does NOT classify all optimal codebooks and does not rule out a hypothetical shorter sum using a codeword longer than six; the reviewed all-length proof eliminates every such length profile and gives precisely four equality cases and one symmetry orbit. Wang–Wang's 2024 general length bounds do not give this sharp three-message classification. Best-of-knowledge acceptance is limited to the exhaustive all-length equality classification, not the previously tabulated T_6 value.

## value

PASS

For three equiprobable binary messages, synchronization-safe code construction is a natural exact shortest-mean-length question. The first nontrivial cardinality-three instance has a sharp all-length optimum and complete four-element equality orbit, improving a 6-bit uniform code and explaining the role of mixed lengths; exhaustive finite optimization is substantive beyond merely replaying the older T_6 table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
