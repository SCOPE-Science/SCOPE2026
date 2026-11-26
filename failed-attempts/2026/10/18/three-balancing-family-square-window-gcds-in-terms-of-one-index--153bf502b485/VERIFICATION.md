---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The three formulas hold for all positive k. The Pell companion identities reduce each window sum to (B_k C_{2n+j} ± k)/m, with the specified shift j and m=16 or 2. Subtracting the first numerator leaves B_k times companion differences. Their common divisor comes from the first two adjacent differences because the step-two recurrence has unimodular transition; parity gives gcd(16,560)=16 and gcd(96,3264)=96. At primes ≥5 the remaining gcd has exactly the part of gcd(k,B_k). At 2, C_even≡1 and C_odd≡3 mod 16, B_odd≡k mod 16, and doubling gives B_k≡3k modulo 2^(v2(k)+4) for even k. Inserting these gives even-k valuations v2(k)-1,v2(k),v2(k), and zero for odd k. At 3 the recurrence makes B_odd a unit and C_odd divisible by 3. For even k, doubling from an odd index first supplies a factor 3, and each tripling of an even index contributes at least one more via 4C_j^2-1. Thus v3(B_k)>v3(k) for even k. The only extra 3 is in the c formula at k≡3 mod 6, where H(k) is prime to 3. This also gives the asserted divisibility by k. The broken-down proof covers k=1 and the infinite range of offsets. The frozen verifier was read, not run; its nominal counter of 7,620 is not a literal count of assert executions and is irrelevant to the proof.

## originality

FAIL

The formula-level coverage is established: three distinct earlier-dated Resultary entries together give exactly the same formulas across all k, including every claimed exceptional factor. Their union covers the frozen finding, not merely its special cases or the ratios conjectured in the 2023 literature. Combining the already stated parity cases under H(k) does not add a mathematical conclusion requiring a new comparison. This verdict identifies substantive coverage; it does not determine public posting priority or independent authorship.

## value

PASS

An all-k exact calculation for three named square-window problems is mathematically motivated by Question 30. Reducing each infinite gcd to a common index divisor explains and sharpens the observed exceptional factors, without purporting to solve the fourth family or evaluate H(k) in simpler terms. This is an assessment of the mathematical content, independent of its duplicate coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
