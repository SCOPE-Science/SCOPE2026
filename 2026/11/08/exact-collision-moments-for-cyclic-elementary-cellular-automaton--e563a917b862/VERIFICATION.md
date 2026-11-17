---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Rule 4 maps each binary ring x to indicators of isolated ones and is idempotent. For two independent inputs, collision equality at every site is a finite local constraint on paired length-three windows, producing exact 16-state de Bruijn trace M_n=tr(T^n). Independently constructed the integer 16x16 T and computed charpoly exactly u^7(u^3-u^2+2u−1)(u^6−3u^5−u^3−2u^2+2u+2). Direct independent brute force for 3≤n≤10 yields 28,106,314,948,2986,9434,29620,92876, equal to traces. Fibre of an isolated-output set factors over gaps; free segments have f_j recurrence with 1,1,2,4,7,12,..., the squared weight renewal H(z)=z²+z³Σf_j²z^j. Pointed cyclic composition yields M_n=g_n²+n[z^n]log(1/(1−H(z))). Because H has positive coefficients at relatively prime lengths 2,3, unique dominant singularity r where H(r)=1 is simple and gives leading constant one; r<λ^−2 makes zero fibre negligible. Exact finite characteristic identity and renewal proof, not finite experiment, establish all n≥3.

## originality

PASS

PASS best-of-knowledge. Jen 1989 Appendix A treats Rule 4 one-step preimage enumeration and related entropy questions, which are substantive prior work but do not explicitly compute labelled finite-ring sum over output fibres squared M_n or its coefficient-one Perron/renewal asymptotic. Koller/Hudcová 2025 uses transfer methods for entrance into attractors, a different aggregate functional, not equality of two independent one-step outputs. Relevant 1988 Jen cylindrical automata article is known only from abstract/bibliographic records and remains a priority risk, not a reason alone to fail. Related published Resultary Rule18/110/54 results concern different local rules and invariants.

## value

PASS

The exact probability that independent initial CA states coalesce to the same output is the second fibre moment (Rényi-2 conditional image entropy), a natural distinct invariant from basin maximum, image cardinality and ordinary Shannon entropy. An algebraic collision rate and exact all-n renewal formula for Rule 4 can inform studies of information loss and inverse dynamics. This is more than quoting a generic transfer-matrix technique because the precise sextic and leading constant are evaluated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
