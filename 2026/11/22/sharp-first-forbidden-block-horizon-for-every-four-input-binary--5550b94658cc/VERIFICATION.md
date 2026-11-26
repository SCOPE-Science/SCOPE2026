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

For a four-consecutive-input binary rule, the length-three input suffix is the complete state for extending a free input block. Start from all eight suffixes; following an output word by taking every matching appended-bit edge gives exactly its possible terminal suffixes. The empty subset is therefore equivalent to absence, and breadth-first search gives the least length. If no empty subset is reachable, every finite word occurs. For any specified bilateral output, the closed nonempty constraints for growing windows then have a common preimage by compactness. An independently written exhaustive implementation (replay: python3 /workspace/branches/6ff72d77-5aa8-42e3-832c-8993681940cb/independent_census.py; full-run.log in the same directory) reproduced all histogram bins from all 65,536 tables, including 0 at 15 and 582 at infinity. The maximal finite length was 18, attained by 5482, 22184, 43351 and 60053. Each has zero missing words at length 17 and eight at 18; both stated witnesses were independently checked for both rules to which each was assigned. Fullness at length 17 implies fullness at shorter lengths. The uploaded scripts were inspected, not executed; the independent check requires neither periodic boundaries nor extrapolation from a rule sample.

## originality

PASS

On the inspected evidence, the new result is the exact distribution of minimal absent lengths, including the sharp finite cutoff and its equality cases. The automaton method and the number 582 of surjective rules are not credited as new.

## value

PASS

A uniform minimal-obstruction cutoff gives the exact block length sufficient to test surjectivity for every four-input binary rule and shows why a length-17 test is insufficient. Four inputs are the next full binary family beyond three-input elementary rules; the census supplies a reproducible baseline with sharp witnesses and a missing interior length, not merely a rerun of the known Boolean surjectivity census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
