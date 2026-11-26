---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The count is over N_r starting positions in a prefix of length N_r+1. A carry through c trailing twos changes the ternary digit sum by 1-2c, so a 01 start requires c=0 modulo 3 and initial digit sum 0 modulo 3. Partitioning below the repunit by the highest first-different digit j (necessarily a zero), the bulk case with c<=j-2 leaves an unrestricted digit and gives 2·3^(j-c-2). When c=j-1 the lone stopping digit is 0 or 1 and exactly one choice works iff j=1 modulo 3 and r is not 0 modulo 3; when c=j there is only one candidate, admissible iff j=0 and r=1 modulo 3. The geometric bulk sum and the two boundary counts give the stated three discrepancies. Independently, exact c with c=0 modulo 3 gives density 2/3^(c+2): the stopping digit has two choices and the remaining higher digit sum modulo 3 is uniformly distributed, by the aligned three-letter blocks. Summing over c gives frequency 3/13; truncating the c sum has uniform tail density at most 3^(-K) plus one possible boundary start in a window for c>=K. Bounded factor balance would put every length-N+1 factor count within a fixed bound of N·3/13, by averaging over translates; the repunit deviations contradict this. Each aligned triple contains every letter once, so four prefix errors of magnitude at most 2/3 bound the integer difference of equal-length single-letter counts by 2. The length-two examples 00 at 44 and 11 at 8 show sharpness. A separate direct digit-sum recurrence test matched every cutoff r=1,…,12; the infinite claims follow from the carry count and frequency argument, not these finite checks.

## originality

PASS

The distinct result is the exact signed 01 discrepancy at every ternary repunit cutoff for t_(3,3), including its three residue classes. The frequency 3/13 and the implication from unbounded discrepancy to failure of factor balance are credited to prior results; sharp single-letter balance is elementary context, not the basis for an originality pass. The nearest binary discrepancy transducer, generalized ternary Parikh-vector result, and binary rational-base transition result do not supply the ternary adjacent-pair profile. Bounded evidence does not settle historical priority.

## value

PASS

The repunit cutoffs are natural repeated-digit, half-scale prefixes of this substitution word. The exact profile gives negative and positive deviations growing in magnitude on two interleaved logarithmic subsequences and a bounded deviation on the third. It quantifies a concrete separation between bounded single-letter fluctuations and unbounded adjacent-pair fluctuations that neither a limiting frequency nor a qualitative balance criterion resolves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
