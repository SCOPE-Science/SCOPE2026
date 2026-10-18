---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Mayr–Ruškuc §3 Foster–Pixley normal form is valid for finite simple nonabelian Malcev algebras: each output coordinate equals an automorphic source projection or constant idempotent, with every source coordinate used at least once in an embedding. Counting (c+au)^v words omitting none of u source types by inclusion–exclusion gives E_vu=Σ_{j=0}^u (-1)^{u-j} C(u,j)(c+aj)^v; exactly u!a^u domain automorphisms parameterize each image subalgebra. The division, recurrence N(v+1,u)=N(v,u-1)+(c+au)N(v,u), and EGF e^{cz}((e^{az}-1)/a)^u/u! follow algebraically and match standard r-Whitney W_{a,c}. For the A5 group example a=120,c=1, N(2,1)=122: 120 diagonal plus 2 coordinate copies; u=0 gives c^v. The inspected verify_whitney_subpowers.py exhaustively checks small descriptor multisets and example algebra; proof uses the actual structural normal form, not the script alone.

## originality

FAIL

Mayr–Ruškuc (arXiv:2404.17322, §3 pp.20–21) explicitly classify EVERY embedding φ:A^u→A^v coordinate by coordinate as one of u·|Aut A| nonconstant automorphic projections or |E| distinct constants, requiring every source coordinate occur nonconstantly at least once. This is the exact complete finite embedding classifier. Counting choices by ordinary inclusion–exclusion and dividing by u!|Aut A|^u mechanically gives the claimed W_{a,c} formula, which is itself classical r-Whitney/Dowling. The new name “full K-power substructure profile” is a direct numerical corollary of a stronger prior normal-form theorem and standard r-Whitney identity; no independent classification remains. O FAIL under implication/stronger coverage rule even though exact formula not printed by Mayr–Ruškuc.

## value

PASS

Exact K-substructure/embedding rank profile of direct powers in a natural Fraïssé class is a motivated invariant that can be useful for quantitative age and finite model counting, including non-group multiple-idempotent cases. This mathematical motivation can survive even though the count is a textbook inclusion–exclusion consequence of published structure and therefore fails the originality axis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
