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
# Verification

Run `python3 verify_direct.py` and `python3 verify_hypergraph.py` in the directory with `ORBIT_REPRESENTATIVES.tsv` using standard-library Python 3. Both programs exhaust six cyclic-rotation classes of four choices each, with \(4^6=4096\) potential maximal dictionaries. The first tests all 108 crossed-window triples in each candidate, checks 2872 successes, 32 strong non-overlapping successes, and partitions all successes into 73 symmetry classes with orbit sizes \(8,16,24,48\) in the declared multiplicities. It compares the generated complete 73-row canonical list byte for byte with the provided table.

The second constructs a forbidden-subset hypergraph independently from the word permutations, counts 2872 independent selections, and evaluates all 48 relabeling/reversal fixed-point counts for a total of 3504. It thereby separately checks Burnside's orbit count \(3504/48=73\). It deliberately does not use the direct crossed-window validity function. These finite checks are exhaustive for the specified 24-word universe, but they do not cover other alphabets, longer codewords or different composition vectors. No independent external audit is claimed.
