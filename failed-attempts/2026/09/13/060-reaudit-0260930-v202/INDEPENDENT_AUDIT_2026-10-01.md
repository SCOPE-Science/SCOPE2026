---
record_id: SCOPE-20260913-060
audit_date: 2026-10-01
disposition: failed
---

# Independent scientific audit

## Final claim

For \(G=<a,b,c | (a b^-1 a b c^2)^6=1>\), the involutions \(x=R^3\) and \(y=aR^3a^-1\) are distinct and generate \(D_infinity\), so \(G\) is not CSA.

## Correctness — PASS

Classical one-relator torsion theory gives the root exact order six. Independent permutation arithmetic gives \(R -> (0 2)(1 3)\) and its conjugate \((0 3)(1 2)\), so the involutions are distinct. Finite subgroups of one-relator torsion groups are cyclic, so these two involutions cannot generate a finite subgroup and hence generate infinite dihedral. The CSA characterization yields non-CSA; the package abelianization is an independent check.

## Originality — FAIL

Classical class-wide theorems plus a tiny finite quotient mechanically decide the instance.

### Equivalent formulations

**Searches.** one-relator torsion distinct involutions; CSA iff no infinite dihedral

**Evidence.** The 1995 paper states the class-wide criterion.

**Reasoning.** Non-CSA reduces to the subgroup witness.
### Broader coverage

**Searches.** finite subgroups one-relator torsion cyclic

**Evidence.** Classical result applies to the whole class.

**Reasoning.** Only separation of involutions remains.
### Exact database or table

**Searches.** published exact-relator search

**Evidence.** No exact table found.

**Reasoning.** A table is immaterial because general theorems decide the instance.
### Claim versus prior implication

**Searches.** apply cyclic finite-subgroup theorem after S4 separation

**Evidence.** A finite subgroup with two distinct involutions cannot be cyclic.

**Reasoning.** Prior implication is decisive.

### Source inspections

- **CSA-groups and separated free constructions** (https://doi.org/10.1017/S0004972700014453): Trigger — Primary final implication. Material read — Abstract and full-text section with the one-relator torsion criterion; PDF inspected. Method — Full-text primary inspection. Assessment — COVERING_INGREDIENT. Evidence — It states CSA iff no infinite dihedral subgroup.
- **Classical one-relator torsion theory** (Magnus--Karrass--Solitar / Newman): Trigger — Torsion and finite-subgroup structure. Material read — Theorem-level statements checked against modern references. Method — Theorem comparison. Assessment — COVERING_INGREDIENT. Evidence — Finite subgroups are cyclic.

### Checked sources

- https://doi.org/10.1017/S0004972700014453
- classical Karrass--Magnus--Solitar/Newman results
- artifacts/verify_w3.py
- artifacts/verify_perm_rep.py
- artifacts/search_perm_rep.py
- artifacts/check_abelianization.py

### Residual risks

- No material correctness risk.

## Scientific value — FAIL

This is an isolated presentation with no demonstrated structural motivation; after the general theorems only a small quotient separation remains.

## Limitations

- No full subgroup-lattice or hyperbolicity claim.
- Rejection is originality/value, not correctness.

## Disposition

**FAILED**. Acceptance requires PASS on correctness, originality, and scientific value.
