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

# Reproducible checks

Run `python3 verify.py` using the Python standard library. The script independently constructs the proper-colouring state graph and performs breadth-first search from one representative of each orbit under leaf permutations and global palette relabellings; the orbit weights cover every ordered pair. For \(n\in\{2,3,4,5\}\), both palette sizes \(k=n+1\) and \(k=n+2\) are verified for each pair distance, polynomial coefficient, diameter, and diametral-pair coefficient. For \(n\in\{3,4,5,6\}\), a concrete \(k=n\) sharpness witness has shortest-path distance \(n+3\) rather than the \(n+2\) predicted by an invalid lower-palette extension.

Expected final line: `VERIFY_OK`. Finite BFS is not an exhaustive proof for unbounded parameters. The proof in `RESULT.md` supplies the general quantifiers, threshold construction, and complete counting argument.
