---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For every n>=2 and finite abelian H with q=|H|>=2, each labelled word has a unique least cyclic period, so f=sum_(e|r) μ(r/e)1_{U_(me)} exactly, where r=rad(n) and m=n/r. Character orthogonality on U_d ≅ H^d gives W(χ)=sum_(e|r) μ(r/e)q^(me)1_(C_(me))(χ), with C_d=U_d^perp and C_(me) nested inside C_m. Any χ∈C_m has a unique highest surviving exponent; its q^D term dominates all distinct lower powers (sum_(j<D)q^j<q^D). For sharp gap, all multipliers divisible by q^m; the union of the proper subgroups C_(mp) inside C_m has relative density at most sum_(p|r)q^(-m(p-1))<1 (the prime exponents omit 3 and sum strictly below 1), giving χ outside them with W=μ(r)q^m. |C_m|=q^(n-m) gives rank, and the trivial frequency gives largest singular value P_q(n). The Fourier stabilizer is C_m^perp=U_m and the recoverable-space condition number is P_q(n)/q^m. Independent root-of-unity transforms for H=Z3,n4; Z4,n3; Z3,n6 verified ranks 9,16,243 and gaps 9,4,3, respectively. These finite tests are checks, not the all-parameter proof.

## originality

PASS

Bounded PASS for an all-abelian-alphabet theorem, while explicitly acknowledging that the COMPLETE binary q=2 specialization is already published. The general H result is not logically entailed by an assertion restricted to binary words; however the proof generalizes easily, a substantial risk to priority and perceived novelty.

## value

PASS

Despite the close binary precursor, an exact uniform spectral-support and sharp condition-number classification for every finite abelian alphabet, including composite noncyclic group structures and every length, is a natural operator invariant researchers can use directly. Its generalized subgroup-annihilator and strict-union witness give genuine all-H statements, rather than simply renaming a q2 object. Value is modest; there is no claim the binary case is a new contribution or that this is a fundamentally new proof technique.

The dated certificate retains the supplied scientific assessment, sources and limitations.
