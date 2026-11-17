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

PASS: For C_n=binom(3n,n)/(2n+1), Legendre digit sums yield nu_3(C_n)=s_3(2n)/2-nu_3(2n+1). Writing 2n+1=3^j(2a+1) removes exactly j trailing digits 2 and proves nu_3(C_n)=s_3(2a)/2; admissible a excludes 1 modulo 3. Two-state ternary doubling with carry matrix [[1+q²,q],[q,1+q²]], initial/final (1,q), gives sum_r P_r(t)z^r=(1-tz)/(1-2(1+t)z+(1+t+t²)z²). Rational differentiation yields E=r/2−1/4+3^(−r)/4 and Var=r/6+(1−3^(−2r))/16. Distinct eigenvalues near t=1 and logarithmic characteristic-function expansion prove the Gaussian CLT. Direct independent binomial valuation histograms for r=0..6 agreed coefficientwise (r=6: 7,71,216,267,140,27,1); no inference to r>6 from tests.

## originality

PASS

PASS, best of knowledge: Resultary exact valuation series for ordinary Catalan numbers at 3 and for Fuss–Catalan at 2 do not determine the same p=3 ternary-Fuss distribution. The highly relevant 2025 Krattenthaler–Müller congruence study treats the same Fuss–Catalan family and some 3-adic residue/valuation layers but its inspected relevant section does not state this full all-depth rational histogram, exact moments or CLT. Literature cannot exclude unindexed equivalent digital-automaton work; risk preserved.

## value

PASS

PASS: Fuss–Catalan sequences are natural enumerative families, and their complete 3-adic depth-by-valuation multiplicities are an exact invariant of an entire prime-power interval, rather than a single small-case tally. The two-state rational law gives all coefficients, sharp zero/max layers, exact probabilistic moments and fluctuation scale in one formula, offering a reusable digit-arithmetic benchmark beyond previously tabulated nondivisibility. Its significance is the precise new all-depth distribution, not merely reproducibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
