---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Reconstructed the exact Paley-17 clique faces (17,68,68), absence of four-cliques, integer 52x52 projected triangle-boundary minor with determinant +1, and 136 affine signed chain traces (character 16,-1,0). Independent mod-two cycle-basis reconstruction gives rank_F2(iota-I)=8; the integral +/- eigensublattices each have rank eight, 2L is contained in their sum, and [v] -> [(1+iota)v] embeds the quotient in L+/2L+, forcing quotient (Z/2)^8. Full source checks/check.py, RESULT.md, REVIEW.md and VERIFICATION.md were inspected; my bounded independent check reconstructed the inputs rather than trusting saved stdout. Limit: graph P17 and this involution, no full integral G-lattice.

## originality

FAIL

The submitted "new symmetry identification" of the affine augmentation character was already proved in a 2026-10-18 full result. More decisively a 2026-11-01 full result proves that the entire degree-two integral C17 translation module is the augmentation ideal I of Z[C17]. Together with the actual geometric inversion action iota t iota^-1=t^-1 and the established rational involution trace zero, this entails the proposed mod-two eigensum obstruction, even though the earlier text does not display that final index. In I/2I=F2[t]/Phi17(t), Phi17 factors into two irreducible factors of degree eight (ord_17(2)=8); inversion sends a root to its 16th power and preserves each F256 factor. Any semilinear involution is x->u x^16 with u u^16=1; finite-field Hilbert 90 conjugates it to x->x^16. Thus each factor contributes rank four to (iota-I), total rank eight. The integral eigensum bounds in the submitted proof then force (Z/2)^8. It is a corollary of already published stronger integral module coverage and standard finite-field algebra, not a novel independent invariant.

## value

FAIL

For the final submission as a claimed new contribution, both the rational character and integral eigensum index are supplied or implied by earlier exact same-complex stronger results. The natural Paley17 invariant is mathematically meaningful and its computation correct, but restating a corollary of a complete prior integral module theorem does not constitute an original, independently valuable finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
