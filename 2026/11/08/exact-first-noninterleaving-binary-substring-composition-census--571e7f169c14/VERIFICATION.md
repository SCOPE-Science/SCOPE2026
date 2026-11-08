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

# Exact verification

Run `python3 verify.py --full` with Python 3 and a C++17-capable compiler, such as `g++`. Expected last line: `VERIFICATION_OK`. Both independent complete enumerations generate exactly 4,196,192 equivalence classes and identify the same 160 four-word groups; the source verifier computes exact composition profiles of every ambiguous word and independently applies the integer-divisor test for all interleaving decompositions. Reversal and complement checks are exact. The supplied `FOUR_CLASSES.txt` is the full explicit 160-group record. Run `python3 verify.py` to verify its downstream classification without re-enumerating the whole space.

Full replay of packaged sources: `n=23 profiles=4196192 heavy=160 hash_collision_groups=0`; size-one class count `4096`, size-two `4191936`, size-four `160`; second enumerator agrees on all three; `TWO_INDEPENDENT_FULL_CENSUSES_OK`, `COMPOSITION_AND_INTERLEAVING_OK groups=160 interleaved=152 exceptional=8 complement_orbits=4`, and `VERIFICATION_OK`.

The exhaustive finite algorithm is the proof of this finite result, not an assertion about unbounded lengths. Fixed-width fingerprints are only an index: identical true profiles necessarily have the same hash, while any unresolved bucket is split by full exact profiles. No independence, external certification, or universal all-length proof is claimed.
