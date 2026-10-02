---
record_id: SCOPE-20260913-059
audit_date: 2026-10-01
disposition: failed
---

# Independent scientific audit

## Final claim

For free standard semicircular variables \(s_1,s_2\), the Brown measure of \(p_1=s_1(s_1+s_2)\) has no atom at zero and \(Delta(p_1)=sqrt(2)/e\).

## Correctness — PASS

The standard semicircle logarithmic integral is \(-1/2\); scaling gives \(log(sqrt(2))-1/2\). Fuglede--Kadison multiplicativity yields \(Delta(p_1)=sqrt(2)/e>0\). Brown's logarithmic-potential identity excludes positive mass at zero. Independent numerical values match.

## Originality — FAIL

This is a direct specialization of classical determinant multiplicativity, Brown logarithmic potential, and an elementary semicircle integral.

### Equivalent formulations

**Searches.** Brown measure zero atom finite logarithmic potential

**Evidence.** Finite potential at zero excludes a positive atom.

**Reasoning.** Immediate consequence.
### Broader coverage

**Searches.** Fuglede Kadison multiplicativity; Brown potential identity

**Evidence.** Both are general classical theorems.

**Reasoning.** They are much broader than this polynomial.
### Exact database or table

**Searches.** published Brown measure s1 squared plus s1 s2; sqrt(2)/e

**Evidence.** No table needed; value is mechanically derived.

**Reasoning.** Missing tabulation is irrelevant.
### Claim versus prior implication

**Searches.** factor p1 and multiply determinants

**Evidence.** Factors have standard semicircle laws of variances one and two.

**Reasoning.** General theorems imply the claim.

### Source inspections

- **Determinant theory in finite factors** (https://doi.org/10.2307/1969645): Trigger — Primary multiplicativity source. Material read — Full-text proof of determinant multiplicativity. Method — Full-text primary inspection. Assessment — COVERING_INGREDIENT. Evidence — Key step is classical.
- **Invariant Subspaces for Operators in a General II_1-factor** (https://arxiv.org/abs/math/0611256): Trigger — Brown-measure framework. Material read — Abstract and determinant/Brown setup. Method — Primary inspection. Assessment — COVERING_INGREDIENT. Evidence — General machinery.

### Checked sources

- https://doi.org/10.2307/1969645
- https://arxiv.org/abs/math/0611256
- artifacts/fk_atom_check.py

### Residual risks

- No material risk.

## Scientific value — FAIL

The atom check is routine and leaves the harder support-gap radius open.

## Limitations

- No support-gap claim.
- Rejection is originality/value, not correctness.

## Disposition

**FAILED**. Acceptance requires PASS on correctness, originality, and scientific value.
