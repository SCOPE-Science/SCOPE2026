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

The compatibility graph has the 128 binary words of length 7 as vertices, with an edge exactly when the two distinct deletion balls intersect in fewer than two outputs. A fresh independent reconstruction of all deletion balls verified that the 70 certificate codewords form a compatibility clique and that the supplied 70-color assignment is proper on all 7807 compatibility edges. Thus the witness gives a lower bound of 70 and the proper coloring gives a matching upper bound, proving the exact optimum and the stated redundancy.

## originality

PASS

The complete searchable Chrisnata--Kiah--Yaakobi text characterizes Type-A confusability, defines the exact graph used here and proves the asymptotic redundancy order, but does not state the length-7 optimum. The earlier Cai--Kiah--Nguyen--Yaakobi paper introduces the fixed-read reconstruction-code setting and constructions. Targeted exact-parameter searches and Resultary found no value 70 for the binary length-7 two-read single-deletion problem.

## value

FAIL

The certificate resolves one exact coding parameter correctly, but the submitted package does not give a mathematical reason that blocklength 7 is a structural boundary, first unresolved case, transition point, or representative classification cutoff. It neither classifies optimal codes nor connects the value 70 to a general finite-length phenomenon. Under the common value standard, a single computationally tractable length chosen without such motivation is an arbitrary finite slice rather than an independently valuable exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
