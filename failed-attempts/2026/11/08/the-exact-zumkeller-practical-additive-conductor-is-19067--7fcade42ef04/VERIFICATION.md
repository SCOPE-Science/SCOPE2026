---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

A fresh independent integer-arithmetic reconstruction (not the saved verification log) enumerated all 71,608 positive even practical numbers at most 716683 using factorization, and exactly 208 odd Zumkeller numbers through 100000 using proper-divisor bitset subset sums. It verified all 99225 odd congruence classes modulo 198450 are covered by p+945u with 48 allowed u, last practical p=539968 and maximal base 716683. It checked that the finite odd bridge from 19069 to 716683 misses only 20177, which is 20176+1 with 20176 Zumkeller, and that 19067 cannot split because p=1 leaves nonabundant 19066 while every even practical p<19067 leaves z failing a necessary Zumkeller sigma condition. For n beyond 716683, modular lifting with u+210t coprime to 945 provides the infinite proof, and even n>=8 have direct finite-class representations. This validates C while recognizing the theorem is already known.

## originality

FAIL

Exact strong prior coverage is decisive. A published October 25 result for the identical positive Zumkeller-plus-positive practical sumset already proves largest exception 19067, conductor 19068, and a complete list of all 720 smaller exceptions. The assigned November 8 result asserts the same conductor and does not claim an independently motivated new invariant; its shorter alternative finite covering proof does not make the original theorem new.

## value

FAIL

Determining the exact additive conductor is a mathematically natural and previously motivating problem, but the submitted final claim merely restates the stronger already-published exact theorem. The new certificate uses a smaller finite threshold, but no independently motivated optimal proof-complexity or distinct mathematical classification is claimed; re-verification of a known table does not constitute a new valuable mathematical finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
