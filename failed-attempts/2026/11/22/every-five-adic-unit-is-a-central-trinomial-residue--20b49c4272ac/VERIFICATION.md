---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The base-five Frobenius factorization gives the constant term as the digit product modulo five: reduce a zero exponent sum modulo five, where its lowest exponent contribution is in [-4,4], and iterate. T_0 through T_4 are all units. Pan–Sun Theorem 1.1, equation (1.4), supplies v_5(T_(5n)-T_n)≥2+2v_5(n) for n>0; consecutive dilations of 2 therefore converge to U_2≡3 mod 25. For r≥k-1, repeatedly lifting the coefficientwise Frobenius congruence modulo five gives F(x)^(5^r b)≡F(x^(5^(r-k+1)))^(5^(k-1)b) mod 5^k. With 5^(r-k+1)>a the only exponent cancellation against F(x)^a is zero with zero, including when a=0 or b=0. Iterated separated blocks realize all positive powers of U_2. Its reduction has order four modulo five and U_2^4-1 has valuation one, so binomial lifting gives order 4·5^(k-1) for every k≥1. The last block may move arbitrarily far, proving infinite attainment and the exact closure. The frozen script was inspected, not run. Independent path /workspace/branches/5b3b05ae-bf2b-42e5-b554-d67ca95f0173/replay_record5.py verified separated products and dilations at n=52 modulo 25 and n=252 modulo 125; only the proof establishes all moduli.

## originality

FAIL

The claimed image and infinite attainment follow as a short specialization of Kohen's already published prime-power reset calculus, using the known Pan–Sun dilation congruence and the order of 3 modulo 25. This is positive prior-implication evidence, not a verdict based on search absence or journal access. Kohen does not literally state the exact five-adic image in the passages read; the earlier general result contains the necessary multiplicative reachability, as shown below. The excluded zero class is already explicitly catalogued. No distinct mathematical remainder is established in the frozen claim.

## value

FAIL

The exact image of this natural sequence is a meaningful mathematical question, and the submitted direct proof is correct. But as a distinct new finding it adds no substantive result to the prior prime-power reset method: the scalar selection uses the known dilation of T_2 and its elementary multiplicative order, and the same reachable-word computation provides infinite witnesses. No additional statistic, quantitative improvement or new structural case survives the implication. This is not a judgment against the inherent interest of the question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
