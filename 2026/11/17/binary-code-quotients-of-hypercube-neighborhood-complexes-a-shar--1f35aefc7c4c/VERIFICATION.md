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

The embedded `artifacts/verify.py` independently constructs the parity component and its anchored two-dimensional triangulation for four nontrivial codes, identifies **cell orbits** rather than merely projected vertex sets, and computes exact binary boundary ranks. It checks the formula for the vertex, edge and triangle orbit counts and reproduces the mod-two homology predicted by the integer theorem and universal coefficient short exact sequence. The verifier uses only Python's standard library. Exact output is in `artifacts/verification_output.txt`.

The four checked parameters are \((d,r)=(4,1),(5,1),(6,2),(7,3)\). Their observed mod-two Betti triples are \((1,1,4),(1,1,16),(1,2,29),(1,3,46)\), respectively. These differ intentionally from the **ranks of integral second homology**, which are \(3,15,27,43\): the extra mod-two classes come from first integral homology's two-torsion. The universal proof is the code-freeness criterion, explicit equivariant collapse, covering-space fundamental-group identification and Euler characteristic; finite matrices alone do not prove its universal quantifiers.

No independent audit has been performed. The claim does not assert that the quotient is a wedge of spheres or that finite tests establish the general statement.
