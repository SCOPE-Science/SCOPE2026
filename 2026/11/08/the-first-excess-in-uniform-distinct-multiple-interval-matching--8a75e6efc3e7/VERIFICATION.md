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

# Reproduction
Compile from the supplied source using `g++ -O3 -std=c++17 -Wall -Wextra verify.cpp -o verify` and run `./verify --dual`.

The verifier constructs the exact eligible-offset masks for every modulus and every possible start residue. It tests every start \(0\le m<L_n\) for \(2\le n\le16\) at length \(2n-2\), and every start for \(n=17\) at both lengths 32 and 33. A successful augmenting-path matching is validated as a set of distinct eligible offsets. Every failed matching is checked by independent exhaustive Hall-subset enumeration, not inferred from an unsuccessful heuristic. With `--dual`, a separate nonrecursive breadth-first alternating-path matcher checks every small-\(n\) instance, each \(n=17\) start divisible by 997 and each \(n=17\) matching failure.

Expected terminal assertion: `VERIFY_OK all_start_classes=26368160 exceptional_32=32 first_exception=485749 ordered_exceptions_checksum=11468177711038706587 dual_augmenting_paths=yes`. The count \(26{,}368{,}160\) includes both tested lengths at \(n=17\). The checksum is a deterministic FNV-style checksum over ordered exceptional starts, not a cryptographic substitute for enumeration.

Limits: the verifier proves a finite classification because period reduction is mathematically exact. It is not a proof for \(n\ge18\), and no independent mathematical audit is claimed. Standard 64-bit integers suffice: the largest period is 12,252,240, and the largest right-position bit is 33.
