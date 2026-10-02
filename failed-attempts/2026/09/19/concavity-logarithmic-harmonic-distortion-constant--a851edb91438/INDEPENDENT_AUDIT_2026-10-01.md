---
audit_date: 2026-10-01
status: failed
---

# Independent scientific audit

## Final claim

For the sharp harmonic pointwise-distortion constant \(M_K\), the exact one-parameter characterization implies strict concavity, an explicit derivative, a second-order conformal expansion, a Lambert-\(W\) large-\(K\) inversion with deficit \(4/\pi-M_K\sim2/(\pi K^2\log K)\), and the corresponding sharp first-order \(L^2\) degeneration rate of the extremal boundary maps.

## Correctness — PASS

Starting from the reproduced source identities \(M=lpha(	au)\), \(K=Q(	au)=J/J'-	au\), direct differentiation gives \(Q'=-JJ''/(J')^2<0\) and \(M_K'=2	au(J')^2/J\). Differentiating this expression in \(	au\) gives a positive numerator, so division by \(Q'<0\) yields strict concavity. Independent numerical quadrature at several \(	au\) values reproduced the signs and the endpoint derivatives. The \(K	o1\) coefficients follow from \(J(1)=1\), \(J'(1)=1/2\), \(J''(1)=1/8\). The large-\(K\) statements follow by routine substitution of the standard complementary-modulus elliptic expansions and inversion of \(	au\log(4/(e	au))\) by \(W_{-1}\); the displayed boundary \(L^2\) identity follows from one elementary integral.

**Sources.** current RESULT.md at archived record; Knežević--Mateljević, arXiv:2609.19609 abstract; standard DLMF elliptic-integral asymptotics

**Residual risks.** No algebraic defect was found; the rejection below is scientific coverage/value, not correctness.

## Originality — FAIL

The source paper already determines \(M_K\), identifies its unique optimizing parameter, and the current package explicitly starts from the source's exact \(J,lpha,eta,Q\) formulas. Every advertised addition is obtained by differentiating that one-parameter formula or inserting standard elliptic-integral asymptotics and an elementary Lambert inversion. Under the required implication standard, these are direct corollaries of the published exact characterization rather than an independent uncovered theorem.

### Equivalent formulations

Equivalent parameterizations do not change the fact that the final claims are differential/asymptotic consequences of the already-determined scalar function.

### Broader coverage

Even without an older paper printing the exact \(K^2\log K\) rate, the source characterization plus standard expansions dominates the calculation under the audit's corollary rule.

### Exact database or table

Absence of an exact database hit is not novelty evidence when the result is mechanically implied by the source formula.

### Claim versus prior implication

This implication covers the mathematical content even if the source does not state these corollaries verbatim.

**Checked sources.** arXiv:2609.19609; DLMF §19.12; Wegmann 1993; published-result corpus search

**Residual risks.** The primary full text was inaccessible; however the rejection does not rely on a whole-document NOT_COVERING conclusion, only on the source's publicly stated exact determination together with the formula reproduced and used by the audited package.

## Value — FAIL

Strict concavity and endpoint rates are informative descriptions of the source constant, but here they require only differentiation, standard special-function expansions, and an elementary one-dimensional integral once the exact source characterization is known. Under the shared value bar for narrow invariants, that is a routine downstream analysis rather than a separate motivated mathematical gap.

**Sources.** Knežević--Mateljević exact characterization; DLMF standard expansions

**Residual risks.** The calculations remain useful for exposition and quantitative interpretation, but usefulness alone does not overcome the mechanically implied status.

## Limitations

- The calculations concern only the already-characterized center constant and extremal family.
- The full source preprint was not retrievable through available open-access routes; the exact source formulas were independently differentiated as reproduced in the current package, while the primary abstract confirms the exact determination and unique optimizing parameter.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
