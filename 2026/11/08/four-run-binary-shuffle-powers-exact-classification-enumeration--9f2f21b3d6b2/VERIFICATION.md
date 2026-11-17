---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Reconstructed the two-run/four-run root dichotomy from first/last symbols and four source runs. Four-run identical roots force q-divisibility of every run; two-run roots 0^A1^B need k complete early copies with ceil(b/B)<=k<=floor(a/A), and the constructive allocation realizes them. Inclusion-exclusion over qA-1 by qB-1 run compositions gives the floor-sum formula; fixed-q Riemann floors yield density (q^3-q^2+q+1)/(2q^3), whose derivative (q-3)(q+1)/(2q^4) proves unique integer minimum at q=3. Independent explicit interleaving-state search for 34 small cases and arithmetic count checks for 448 cells agreed.

## originality

PASS

The 2025 four-run shuffle-square classification is only q=2. The submitted q>=3 exact threshold and full composition-density law do not follow by mere substitution into a two-copy theorem. No equivalent q>=3 four-run result was identified in the targeted Resultary searches; this is a best-of-knowledge decision, not proof of global priority.

## value

PASS

Classifies a natural bounded-run family in arbitrary equal-copy shuffle powers, gives a nontrivial exact composition enumeration and a sharp limiting density phase change q=3; neither a renaming nor routine one-line q=2 substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
