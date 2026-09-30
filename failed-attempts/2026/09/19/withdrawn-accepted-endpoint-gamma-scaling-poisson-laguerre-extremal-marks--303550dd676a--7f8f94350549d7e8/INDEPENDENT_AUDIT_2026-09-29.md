# Independent Audit — 2026/09/19/endpoint-gamma-scaling-poisson-laguerre-extremal-marks--303550dd676a

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `054f07d6d95985f64c6ba927a94c11d1736ff334`
- Disposition: **FAILED**

## Correctness

**PASS** — The mathematics is essentially the same correct endpoint-tilting argument as in the preceding record: the scale a_{d,rho}=d(v_d gamma)^(2/d)L^(1-2/d), the Gamma(kappa,rate 2A) tilted deficit law, the product refinement with the Gumbel score, and the d=3 -kappa log a_rho centering all check. The same independent power-endpoint numerical integration confirms the Gamma Laplace transform. The +log(gamma) correction is likewise algebraically consistent with the quoted exact d=3 centering.

## Originality

**FAIL** — This record is materially duplicated by the earlier public SCOPE record `endpoint-gamma-localization-poisson-laguerre-inradii--28a16606f392`. The earlier record was committed at 2026-09-19 13:04:44 +08:00; this record's first public commit is 2026-09-20 02:04:18 +08:00, roughly thirteen hours later. Both state the same d>=3 regularly varying endpoint hypothesis, the same scale d(v_d gamma)^(2/d)(log rho^d)^((d-2)/d), the same Gamma(shape endpoint exponent, rate 2A) limiting mark deficit, the same product Poisson/Gumbel refinement and maximum-cell independence, the same d=3 -endpoint_exponent/3 log log centering, and the same missing +log(gamma) correction to the two v1 examples. Notation beta versus kappa and added exposition do not create a new theorem. Because the covering result was already publicly recorded before this record, originality fails independently of external-literature novelty.

## Scientific value

**FAIL** — As a standalone exposition the record is mathematically useful, but it contributes no independent scientific content beyond the earlier SCOPE record already containing the same theorem, correction, and asymptotic interpretation. The later presentation does not add a stronger hypothesis range, sharper rate, new limiting object, or distinct application sufficient to justify a second validated finding. Under the audit contract, exact or near-exact internal duplication is insufficient scientific value for a separate research record.

## Sources

- Point process convergence of large inradii of Poisson-Laguerre tessellations (Matthias Schulte; Martina Švarc Petráková): https://arxiv.org/abs/2609.20750 — External source underlying both SCOPE records.
- Earlier SCOPE commit: Add endpoint-Gamma localization for Poisson-Laguerre inradii (SCOPE-Science/SCOPE2026): https://github.com/SCOPE-Science/SCOPE2026/commit/f746180269f5a24fa4f0f66509533b3fb76baa69 — Earlier public commit at 2026-09-19 13:04:44 +08:00 containing the same substantive result.
- Later SCOPE commit: Add endpoint Gamma scaling for Poisson-Laguerre extremal marks (SCOPE-Science/SCOPE2026): https://github.com/SCOPE-Science/SCOPE2026/commit/329d2cf88c8d7eb7f119f75b483a13b092467795 — First public commit of this record at 2026-09-20 02:04:18 +08:00.

## Limitations

- The failure is for originality and independent scientific value, not mathematical correctness.
- The comparison is internal repository precedence and substantive theorem overlap; it does not depend on proving that no external author independently found the endpoint-Gamma law.
- Relocation should preserve the complete package as a failed attempt because the derivation remains useful evidence of a duplicated line of work.

## Independent checks

```json
{
  "duplicate_precedence": {
    "earlier_commit": "f746180269f5a24fa4f0f66509533b3fb76baa69",
    "earlier_time": "2026-09-19T05:04:44Z",
    "later_commit": "329d2cf88c8d7eb7f119f75b483a13b092467795",
    "later_time": "2026-09-19T18:04:18Z"
  },
  "substantive_overlap": [
    "same d>=3 bounded regularly varying endpoint hypothesis",
    "same d(v_d gamma)^(2/d)(log rho^d)^((d-2)/d) scale",
    "same Gamma(endpoint exponent, rate 2A) deficit law",
    "same product marked-Poisson/Gumbel refinement and maximum-cell independence",
    "same d=3 logarithmic centering correction",
    "same missing +log(gamma) v1 example correction"
  ],
  "failed_destination_verified_absent": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. The dated independent-audit pair was verified absent before staging this change set, and `VERIFICATION.md` was read at blob `31a3bb079c3be0cdcbee536377edadb1613bf629`. GitHub was used only as read-only evidence; no repository write was performed. Open-access/preprint sources were checked first. No decisive comparison required Oxford Download in this run.
