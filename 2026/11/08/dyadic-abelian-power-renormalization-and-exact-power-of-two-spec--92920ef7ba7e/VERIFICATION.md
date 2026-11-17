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

PASS: The recurrence x_m(2j)=0 and x_m(2j+1)=x_m(j)+1 mod m gives x_m(j)=v2(j+1) mod m. Induction gives sigma_m^k(a)=U_{m,k}(a+k), a common length-2^k−1 prefix with only the last letter variable. An arbitrarily offset d·2^k window has d copies of U and d terminal letters, proving exact Parikh pushforward with floor(i/2^k), hence identical Abelian-power occurrence sets under dyadic expansion for all d,h. Unit-period valuation parity class gives squares, cubes, no h≥4 for m≥2, and geometric valuation distribution yields square/cube starting densities. Independent 24,000 misaligned Parikh checks plus bounded Abelian tests confirmed formula; no infinite conclusion from tests.

## originality

PASS

PASS for surviving all-m and arbitrary-base-d theorem; explicit prior-credit exception: a published same-day result for the binary period-doubling word, 2026/11/8/SCOPE-dyadic-period-abelian-power-rigidity-and-exact-occurrence-freque--b15742f4181c, already gives m=2 dyadic squares/cubes with densities 1/3 and 1/6 and absence of fourth powers. This m=2 special case is NOT original. The assigned result also proves exact misaligned Parikh renormalization for every m≥2 and d≥1, all-position occurrence-set lifting and all alphabet-m frequency distributions; the binary result does not imply them. No inspected primary statement covers that broader content.

## value

PASS

PASS: For a natural nonuniform m-letter substitution, the period-dilation identity reduces Abelian repetition-position questions at arbitrary periods to odd periods, while an exact all-m exponent cutoff and occurrence densities classify each dyadic scale. This structural all-moduli renormalization and frequency pushforward remain independently useful despite the known m=2 pure-dyadic corollary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
