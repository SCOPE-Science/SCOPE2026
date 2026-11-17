---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: The independent recipient-side Bernoulli dynamics on K_{a,2} has state transition increments Bin(a-i,j/2), Bin(2-j,i/a). The exact triangular first-step recurrence H_i and geometric waiting phase yield both starting-side expectations. I independently implemented the recurrence with fractions.Fraction for every integer a=2..11, finding equality 3 at a=2 and strict T_B<T_A for each a=3..11. The bound T_A>=a^2/(2a-1)+1 versus T_B<=ceil(log_2 a)+3 separates at 12<=a<=16 and all a>=17 (via r>=5 dyadic bound). The coupling T_A<=a^2/(2a-1)+T_B plus lower bound yields T_A-T_B=a/2+O(log a). A finite rational test cannot prove the unbounded inequality; the stated analytic bounds do.

## originality

PASS

PASS, best of knowledge: Geneson–Hicks–Lichtenberg–Moon–Robles 2026, Section 3.6, proposes the very starting-side comparison as Conjecture 3.12 and proves only an optimal-seed upper bound and finite small table. A separate November 8 paper establishes the small-origin limiting law and large-origin mean asymptotic, hence eventually strict preference, but NOT strict preference at every finite a>=3. The current exact rational+analytic finite/all-large bridge supplies that missing all-a result. Same-day relative priority is not asserted.

## value

PASS

PASS: this proves the full natural width-two slice of an explicitly posed source-location conjecture and an unbounded asymptotic expected-time advantage. The process is recipient-side RZF, not sender-side PZF, so no conflation with opposite-rule conjectures; the exact small-size checks bridge a genuine gap between eventual asymptotic ranking and all finite a.

The dated certificate retains the supplied scientific assessment, sources and limitations.
