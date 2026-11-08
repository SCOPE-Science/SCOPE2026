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

# Reproducibility and verification

Execute `python3 verify.py` in the extracted directory. Python 3 standard library suffices; no downloaded data or packages are needed.

The script regenerates the local-majority constraints directly for all \(16^3\) column triples; computes the \(400\) allowed arcs among \(256\) pair states; and finds the six cyclic components with sizes \(16,8,8,2,1,1\). It derives their characteristic polynomials from traces with Newton identities using exact integers, then verifies the universal six-residue formulas against independently computed transfer traces for \(3\le n\le40\). Finally, it brute-force enumerates every binary coloring for each size \(3\le n\le8\), checking \(M(x)=x\) and \(M^2(x)=x\) separately. The outputs agree with the theorem.

The proof in `RESULT.md` supplies the infinite-family argument: the finite transfer calculation determines the full symbolic recurrence for every size, and the majority energy argument bounds all eventual periods by two. The finite brute-force enumeration alone would not establish the theorem. No empirical convergence-time or basin-distribution claim is tested or made. Independent validation remains unperformed.
