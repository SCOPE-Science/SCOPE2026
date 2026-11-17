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

For four-symbol DNA words with exactly two C/G letters, reverse-complement closure and no fixed strands, 96 possible balanced words have 8 fixed and 44 nontrivial two-strand orbits; four orbits self-conflict under the closed 0/one-adjacent-swap balls. The remaining 40 orbits form a 100-edge graph with connected component sizes 4,6,6,12,12. Independent reconstruction of each swap ball and exhaustive independent-set enumeration gives component (size,alpha,opt-count) (4,1,4), twice (6,2,3), twice (12,3,12). Thus maximum is 2*(1+2+2+3+3)=22 codewords and labeled equality count 4*3*3*12*12=5184. An alternative multiset graph recursion corroborates unrestricted 25. Every finite choice is checked, so this finite enumeration is exhaustive rather than extrapolated.

## originality

PASS

PASS best-of-knowledge for sharp 22-codeword capacity and complete 5184 labeled equality census under the precise adjacent-transposition, Watson–Crick closure, GC-balance constraints; related Hamming/deletion code counts not identified as covering.

## value

PASS

This precisely characterizes both capacity and all optimal labeled codebooks of a motivated finite joint DNA composition/strand-pairing/adjacent-transposition model; the complete equality case and channel contrast are independently useful invariants, beyond a routine general distance-code substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
