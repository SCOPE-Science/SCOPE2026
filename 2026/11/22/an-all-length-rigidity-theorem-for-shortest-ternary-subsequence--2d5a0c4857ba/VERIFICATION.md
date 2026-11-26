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

Deleting one of two adjacent equal letters of a cover preserves coverage: for a host position used at either copy in an embedding, keep that position as the single copy in the shorter embedding. A run-free cover can use at most one host position per run, and the used position within a run can be chosen arbitrarily, so contraction preserves the entire shortest-cover set. Unary hosts are immediate; binary alternating hosts have the unique cover of length two when the endpoints differ and of length three when they agree. Transitivity makes a shortest cover s-primitive, and Charalampopoulos et al., SPIRE 2022 Fact 1 bounds its ternary length by 8. Its first symbol is the normalized host's first symbol, leaving exactly 255 run-free candidates. For each fixed candidate, the maximum feasible index for a newly read host position leaves the shortest possible suffix to match later. The older suffix obligations are nested, and their greedy one-letter updates preserve length dominance (an obligation can shrink by at most one). Thus keeping the longest residual suffix and the longest feasible prefix is exact. The product starts after 01, stores the last letter, explores both permitted successors of every reachable state, and tests the entire length-minimal accepted set against the regex state. The supplied C++ sources and outputs were inspected, not executed. The separately written Python implementation was run to closure and its transitions and full log checked: 84,725 states, 169,450 edges, 255 candidates, maximum shortest length eight, and 12 accepting regex states with exactly the two stated minima; every other state has exactly one. Replay: python3 /workspace/branches/a0b8078f-2ef0-44c3-bb90-a6fb6231da87/independent_finite_check.py (output full_run.log in that directory). This certifies all normalized run-free lengths, not a sample; the certificate is computer-assisted, not formalized. In the exception family the delimiter and block changes determine a,b,c uniquely, and normalization by first appearance gives six distinct relabelings. The run-free series u^11/(1−u²)^3 with u=z/(1−z), times six, gives the stated generating function, first coefficients, and leading singularity constant 3/64.

## originality

PASS

The first ambiguity and its six length-eleven words are already covered. The all-length exception language, exact two-cover rigidity and enumeration of arbitrary positive run expansions are distinct in the inspected material. The foundational candidate-length bound and the notions of primitives and covers are credited, not original claims here.

## value

PASS

A natural question about uniqueness of minimum subsequence covers is answered at every host length for a fixed alphabet. The exact language, exclusion of three-way ambiguity, and closed counting series give structural and enumerative information not supplied by a few more lengths of brute force.

The dated certificate retains the supplied scientific assessment, sources and limitations.
