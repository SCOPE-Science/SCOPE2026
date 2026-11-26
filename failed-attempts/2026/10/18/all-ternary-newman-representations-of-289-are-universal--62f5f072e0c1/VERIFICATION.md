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

The base-three equality makes c_i equal to 3^{-i} times the difference of the truncated 289Q and P evaluations: integrality follows by reduction modulo 3^i. From the digit range the carry is inductively in [0,144], starts at 96 after the common constant digit, and reaches 0 with zero padding. An independent exact construction used all four digit pairs at every possible carry, intersected forward reachability from 96 with backward reachability from 0, and propagated five-digit input histories without taking the supplied tables as inputs. It reproduced 32 reachable carries (20 live, 12 traps), checked all 26 live edges for consistent shifted histories and exact convolution, and confirmed the zero history at carry 0 and the nontrivial example 80920=289*280. Because every finite valid representation gives such a live walk, the convolution certificate applies at arbitrary degree, not just to the bounded-walk examples. Replay: python3 /workspace/reproductions/newman289.py. The uploaded checker was inspected, not executed.

## originality

FAIL

An inspected distinct public record gives the identical all-representations polynomial identity, example and live/trap carry certificate. There is no scientifically distinct remainder between the two claims. This is a decision on demonstrated duplicate coverage in the available corpus, not a claim that the later-dated entry historically anticipated the frozen result or evidence of who discovered it first. The 2023 article genuinely leaves the local cell open.

## value

PASS

As a mathematical result, the all-degree fixed quotient settles the sole open local-representation entry in a motivating published finite table. It explains why locally admissible anomalous carry transitions cannot finish a representation. The value is not that 289 is another computable small number, nor does it erase the separate originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
