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

# Verification evidence and limits

The proof checks the two genuinely non-formal inputs separately: integral Lefschetz hyperplane theory for the smooth complete-intersection cover, and the existence of a fixed-point-free linear involution with hyperplane bundle linearization. The second input is part of the stated hypotheses; for the referenced generalized-Fermat subfamily, existence is provided by the cited construction.

The algebraic topology calculation uses the actual multiplicative Cartan–Leray spectral sequence and group cohomology \(H^{2j}(C_2,\mathbb Z)=\mathbb Z/2\) for positive \(j\), \(H^{2j+1}(C_2,\mathbb Z)=0\). Because all second-page terms in the indicated total-degree range have even total degree, no differential can connect them. The hyperplane and character line bundles lift the associated-graded algebra generators and separate all additive extensions. The canonical identification is established by anti-invariance of the even-dimensional volume form. The exponential sequence gives \(\operatorname{Br}(X)=0\).

The standalone `checks/stable_range_table.py` is executable with plain Python and prints `E2_ADD_MULT_CHECK_OK` after checking dimensions four through eighteen. It is a sanity check of the bigraded table and monomial locations; it is **not** an infinite proof, and no external theorem is claimed to have been formally certified. No independent review has been conducted.
