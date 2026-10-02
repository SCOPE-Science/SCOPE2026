# Independent audit — 2026-10-01

**Disposition:** failed

## Correctness

The local calculation is correct. After \(\Phi_n(X)=\Phi_{\operatorname{rad}(n)}(X^{n/\operatorname{rad}(n)})\), cancelling all Möbius factors supported on the recovered prefix leaves a product whose unique smallest remaining exponent is the next prime. Its coefficient is an \(\ell\)-adic unit, while every other term has strictly larger valuation, so \(\nu_\ell(R_j-1)=a\,\nu_\ell(x)\,p_{j+1}\). The sign congruences for odd \(\ell\) and for \(\ell=2\) at depth at least two also follow from the first nonconstant term. The archived finite check is consistent but is not used as proof.

## Originality

A separately published SCOPE record, “Higher local cyclotomic prime extraction”, was added on 2026-09-18 at 06:15 UTC, before this record’s 21:16 UTC creation. Its theorem states \(\nu_\ell(\Phi_r(y)\Phi_{P_j}(y)^{-\mu(r/P_j)}-1)=p_{j+1}\nu_\ell(y)\) for squarefree \(r\). Taking \(r=\operatorname{rad}(n)\) and \(y=x^a\) turns that residual exactly into the audited \(R_j\) via the Möbius product, and gives \(\nu_\ell(R_j-1)=a\nu_\ell(x)p_{j+1}\). Thus the central peeling theorem is already covered; the remaining sign-recovery congruence and fixed-base corollaries are elementary consequences of the first-term expansion and do not restore originality.

### Equivalent formulations

Radical reduction and the Möbius identity give literal equivalence of the local valuation formulas.

### Broader coverage

The prior theorem dominates the core claim after the standard reduction.

### Exact database or table comparison

Chronology establishes decisive prior publication within the same repository.

### Claim versus prior implication

The final audited peeling claim is mechanically implied by the earlier theorem plus classical radical reduction.

### Source inspections

- **Higher local cyclotomic prime extraction** — DECISIVE_PRIOR_COVERAGE. Material read: complete RESULT.md, METADATA.json and AUDIT.json plus Git creation timestamp. Evidence location: SCOPE 2026/09/18/higher-local-cyclotomic-prime-extraction--01e648b0fd33.

- **Cyclotomic Prime Extractors** — PRIOR_INGREDIENT. Material read: publicly indexed detailed theorem/review material for radical and least-prime extractors. Evidence location: https://arxiv.org/abs/2609.18480.

- **Cyclotomic Coincidences** — CLASSICAL_BACKGROUND. Material read: bibliographic/theorem context as classical Möbius-product background. Evidence location: https://arxiv.org/abs/1903.01962.

## Value

Once the earlier higher-local theorem is applied after radical reduction, the only surviving additions are a first-order sign congruence and immediate base \(3\), \(4\), and nonsquarefree base \(2\) corollaries. Those are mechanically implied and do not constitute an independently motivated mathematical gap under the value standard.

## Residual risks and limitations

The identities are mathematically correct, but the central residual-peeling theorem is already covered by an earlier same-day published SCOPE record after radical reduction. The surviving sign and fixed-base corollaries are routine consequences.
