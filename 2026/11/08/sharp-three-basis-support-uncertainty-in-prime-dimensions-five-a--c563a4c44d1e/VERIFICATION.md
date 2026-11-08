---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

## Certificate logic
For each prime \(p=5,7\), an auxiliary prime \(q\) has been chosen so \(q\equiv1\pmod p\). The listed root of exact order \(p\) gives a well-defined homomorphism from cyclotomic integers to \(\mathbb F_q\). Hence any maximal matrix minor surviving the reduction is a nonzero complex number. The integer-only checker verifies all possible subsets of \(p+1\) zero constraints from every triple of standard mutually unbiased bases. A zero complex minor would necessarily reduce to zero, so every full-rank modular instance is a valid complex full-rank instance.

## Reproduction
Compile with `c++ -O3 -std=c++17 CHECK.cpp -o check` and execute `./check`. The expected two `CHECK_OK` lines, including counts \(100100\) and \(11395440\), appear in `RESULT.md`. The certificate does not rely on any absolute paths or external datasets.

## Extent and boundaries
The exhaustive check covers all triples and all \((p+1)\)-row selections for \(p=5\) and \(p=7\). It proves no nonzero vector is orthogonal to more than \(p\) of the selected \(3p\) measurement vectors. The separate analytical witness establishes attainability. It does not prove the analogous statement for any other prime, classify all equality vectors, or supply an independent audit.
