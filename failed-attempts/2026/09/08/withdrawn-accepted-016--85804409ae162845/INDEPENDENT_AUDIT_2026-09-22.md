# Independent audit — 2026-09-22

**Disposition: FAILED ATTEMPT.** Recovery verification performed 2026-09-23 UTC against public `main` head `dcdc9e9b990eef6d712e3a1e18d83b7f50e21bfb`. The assigned source directory still has exact tree SHA `066ecaaeca4243ba8af0878576c3b70f16430816`, matching the assignment guard. RESULT.md blob: `2e1e17f3ddf6f2cbae11c8a459168ea3eec61415`.

## Claim reviewed
Conditioned pair-crosscorrelation minimum at N=21. The audit preserves the record's finite computations where supported, but evaluates correctness, originality, and scientific value separately.

## Correctness
PASS. The recovered audit independently recomputed the anchor autocorrelation energy, the identity X=N^2+2<C^P,C^Q>, and an exact 2^20 sign-quotient census. It reproduced min S=455, deficiency 40, 44 quotient minimizers, the next level 471 with multiplicity 684, and the five (E,X) classes. The current source directory tree is unchanged from that completed audit.

## Originality
NARROW/NOT DECISIVE. Targeted prior-art checking supports that the exact fixed-anchor histogram may be unreported, but the record is explicitly conditioned on one chosen length-21 anchor and does not establish a new general bound or construction. Packebusch–Mertens (arXiv:1512.02475) already supplies the single-sequence LABS context; Katz–Lee–Trunov (arXiv:1702.07697, arXiv:1711.02233) supplies the established crosscorrelation/Pursley–Sarwate framework.

## Scientific value
FAIL. After subtracting the established framework, the surviving contribution is a one-anchor finite enumeration with an arbitrary conditioning choice. It yields no unconditioned pair extremum, structural classification across anchors or lengths, construction, asymptotic bound, or reusable theorem. A bounded repair that merely reframes the table as a benchmark does not supply a sufficiently general scientific consequence.

## Literature checked
- Packebusch & Mertens, Low Autocorrelation Binary Sequences: https://arxiv.org/abs/1512.02475
- Katz, Lee & Trunov, Crosscorrelation of Rudin-Shapiro-Like Polynomials: https://arxiv.org/abs/1702.07697
- Katz, Lee & Trunov, Rudin-Shapiro-Like Sequences with Maximum Asymptotic Merit Factor: https://arxiv.org/abs/1711.02233

The literature comparison used open public sources; no inaccessible source was decisive for this disposition.

## Bounded repair assessment
Reframing the result as a conditioned benchmark was considered; the statement is already limited that way, so there is no correctness repair to apply. The value deficiency would require new cross-anchor/global structure rather than wording changes.

## Final disposition
The record fails the independent three-axis gate because the scientific-value axis does not pass after known framework/prior coverage is subtracted. The complete package should be preserved and archived as a failed attempt rather than represented as a validated finding. This disposition does not erase the reproducible finite computation.

## Reproducibility / provenance
Inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`; current checked head `dcdc9e9b990eef6d712e3a1e18d83b7f50e21bfb`; source tree `066ecaaeca4243ba8af0878576c3b70f16430816`. Existing historical AUDIT/REVIEW evidence is preserved. Lean verification and expert attestation are not changed by this audit.
