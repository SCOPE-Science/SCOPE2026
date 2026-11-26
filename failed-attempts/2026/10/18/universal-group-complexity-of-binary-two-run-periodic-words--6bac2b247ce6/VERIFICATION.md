---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For a,b≥2, the only mixed triples are 001,100,011,110. A subgroup of S3 either joins both mixed pairs (the two singleton supports, or their complements, are in the same position-orbit) or neither; the optional constants add c to every count. For a singleton run, after relabeling, the factors are residue supports modulo m=a+b. When n<m there are n one-hot factors and the zero factor. For n=tm+r≥m there are m distinct phases, split by weight into r and m−r phases if r>0, or one class if r=0. The diagonal block permutations preserve each weight class and give any prescribed number of phase orbits in it (permute one block, fix the rest). The orbit counts add, so every intermediate target is achieved, including n=1 and r=0. The frozen replay path is `python3 verify.py` in the source record; the supplied log reports 1,662 sparse target checks and 49 long-run cases. The script and log were inspected, not executed; their finite scope is not the proof.

## originality

FAIL

A distinct published Resultary record, 3143435de6dd, gives the same two-run iff theorem, the same exact length-three spectrum and missing middle value, and explicit positive-case realizations. No part of the frozen Finding escapes that statement-level coverage. This is failure to distinguish this finding from equivalent existing catalogue coverage, not a finding that the 11/8 record predates the 10/18 record or a determination of historical priority. The earlier literature alone would not settle the comparison this way.

## value

PASS

As mathematics, the result replaces per-word finite testing with a closed structural classification of a natural infinite family. The three-position obstruction is already complete, and the attaining groups give witnesses at every positive length rather than only a decision procedure. This intrinsic value does not supply distinct content relative to the equivalent published finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
