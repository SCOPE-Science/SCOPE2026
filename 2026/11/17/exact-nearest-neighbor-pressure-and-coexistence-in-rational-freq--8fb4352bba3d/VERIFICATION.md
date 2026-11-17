---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible mathematical checks

Run `python3 verify_pressure.py` using Python 3 and the standard library. The program enumerates generator transition counts for \(88\) integer cases, checks \(42\) sample combinations of real edge rewards and integer frequency parameters, compares six finite truncated renewal roots per example, and verifies the freezing root equations for eleven integer parameters. Expected success marker: `VERIFY_OK cases=42 finite_roof_roots=6 per_case critical_roots=11 exact_word_checks=88`.

The infinite-parameter assertions are **not** inferred from sampling: they follow from the precise marker-return coding, Kac's theorem, Abramov's formula, the inequality \(h_{\mathrm{ret}}\le H(p)\), and the KL identity \(D(p\Vert q)=-H(p)-s+L\mathbb E M\ge0\). Equality requires iid geometric return lengths and identifies the unique non-atomic ergodic candidate. The imported coded-support premise is Theorem C of Reyes (arXiv:2611.10995v1). General older frameworks supply context, not an independent audit or certification.
