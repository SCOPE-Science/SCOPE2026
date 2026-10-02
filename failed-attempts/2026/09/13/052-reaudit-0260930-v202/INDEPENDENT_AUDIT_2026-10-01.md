---
record_id: SCOPE-20260913-052
audit_date: 2026-10-01
disposition: failed
---

# Independent scientific audit

## Final claim

For \(F_s(E_1,E_2)=P_s(E_1)+P_s(E_2)\) on two disjoint unit-volume chambers in \(R^3\), \((1-s)m_s\) tends to the two-ball perimeter limit and therefore cannot converge at any polynomial rate to either standard-double-bubble perimeter convention.

## Correctness — PASS

Sharp fractional isoperimetry gives \(P_s(E_i)>=P_s(B)\), and two disjoint ball translates attain equality, so \(m_s=2P_s(B)\) for every \(s\). The standard local limit gives the asymptotic. Independent arithmetic gives \(T=9.6719517241\), \(S_0=10.1549129756\), \(C_0=9.1394216781\), with gaps \(0.48296\) and \(0.53253\).

## Originality — FAIL

The theorem is mechanically implied by sharp fractional isoperimetry plus the standard local limit because the objective decouples.

### Equivalent formulations

**Searches.** fractional perimeter balls fixed volume; decoupled chamber sum

**Evidence.** The primary source states ball minimality.

**Reasoning.** The problem is exactly two copies of a known minimization.
### Broader coverage

**Searches.** fractional perimeter local limit

**Evidence.** The same source records the local limit.

**Reasoning.** General theory is broader.
### Exact database or table

**Searches.** published-finding search for fractional two-chamber sum

**Evidence.** No table is needed because analytic coverage is decisive.

**Reasoning.** No duplicate table does not restore originality.
### Claim versus prior implication

**Searches.** compare m_s with one-body isoperimetry

**Evidence.** \(m_s=2P_s(B)\) exactly.

**Reasoning.** The prior implication is stronger.

### Source inspections

- **A quantitative isoperimetric inequality for fractional perimeters** (https://cvgmt.sns.it/media/doc/paper/1499/FuMiMo-final.pdf): Trigger — Same functional. Material read — Introduction through Theorem 1.1, including local limit and ball minimality. Method — Full-text primary-source inspection. Assessment — COVERING. Evidence — General ingredients decide the instance.

### Checked sources

- https://cvgmt.sns.it/media/doc/paper/1499/FuMiMo-final.pdf
- https://arxiv.org/abs/1012.0051
- artifacts/verify_gaps.py

### Residual risks

- No material risk.

## Scientific value — FAIL

This is a cheap functional-mismatch check for an uncoupled objective and adds no new minimizer structure, rate, or boundary phenomenon.

## Limitations

- Correctness passes; rejection is originality/value.
- No claim about a coupled fractional cluster energy.

## Disposition

**FAILED**. Acceptance requires PASS on correctness, originality, and scientific value.
