---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The measurements retain both local outcomes, not just the parity of the two Pauli outcomes. For a one-qubit Bloch vector, C_X=(1+x^2)/2 and C_Z=(1+z^2)/2; since x^2+z^2<=1, AM–GM gives C_X C_Z<=((1+1/2)/2)^2=9/16, attained by a pure vector with x^2=z^2=1/2. Product measurement distributions factor on all product density operators, so the sharp two-qubit ceiling is 81/256. An independent exact hand calculation uses the amplitude matrix A=[[3,-1],[-1,1]]: H A H=[[1,1],[1,3]] and each matrix has squared Frobenius norm 12. The normalized determinant is 2/12, and both collision probabilities are (81+3)/144=7/12. The cross-product margin is 49*256-81*144=880>0, hence the entropy sum is strictly below the entire product-state region. VERIFICATION.md and verify.py were inspected, not executed. Abdelkhalek et al. §II define entropy pairs at fixed orders and the paper says it mostly assumes dual orders; §V.D includes equal nondual orders and Conjecture V.6 does not impose duality, unlike V.8. This is a counterexample to V.6 under its unrestricted wording, not to a dual-order or Shannon version. The later Shannon theorem supports additivity of optimal linear bounds and the corresponding positive convex hull, not full entropy-pair reproduction merely by virtue of that theorem; the frozen limitations overstate that contextual coverage, without affecting the claimed collision witness.

## originality

FAIL

Verified prior coverage, not an access failure. Simnacher–Wyderka–Schwonnek–Gühne, arXiv:1901.07946 and Phys. Rev. A 99, 062339 (2019), §II, explicitly study the same four-outcome local X and Z product measurements and compare the all-state and separable entropy regions at order 2. Their Lemma 1 and Eq. (5) give psi_t proportional to (t,1,1,1) on the lower collision-entropy frontier, with Hadamard expansion in Eq. (7); Theorem 2 treats all Tsallis orders at least 2, and the authors explicitly transfer by the coordinatewise monotone Tsallis-to-Rényi map. At t=3 their state is exactly the frozen one after Z on both sites. Those local sign flips preserve Z probabilities and permute the two X outcome bits, leaving both entropies unchanged. The prior work presents the same phenomenon at the same orders, gives the very witness family, and itself discusses Conjecture V.6. The explicit decimal-free constants and concise product-only proof do not make this a new counterexample.

## value

FAIL

The computation is a clear pedagogical certificate of a worthwhile phenomenon, but as a frozen research finding it gives a parameter instance of the known lower-boundary family for the same measurements and orders. Rephrasing that instance as a product-only obstruction, with a Bloch-ball bound and rational constants, does not produce a substantive surviving research claim beyond the prior entropy-region separation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
