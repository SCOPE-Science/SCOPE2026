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

Run the commands below after extracting the complete package. The execution consists of two independent exhaustive calculations and a cross-check against the packaged integer histograms.

```sh
g++ -O2 -std=c++17 src/forward_census.cpp -o forward
g++ -O2 -std=c++17 src/reverse_census.cpp -o reverse
./forward > forward.json
./reverse > reverse.txt
python3 src/check_outputs.py forward.json reverse.txt data/joint_histogram.csv data/word_histogram.csv
```

The forward program enumerates all base-eight transition tuples, filters rank six and rotation representatives, then counts shortest reset words by breadth-first shortest-path accumulation. The reverse program independently builds reversed letter-labelled edges on the 255 nonempty subsets and counts shortest paths from eight singleton goals to the full set. The last program checks the full joint table, both marginals and the sharp extremizer. All arithmetic is integral. The result concerns a fixed finite eight-state family only; the full histogram and verifiers, not a sample of witness words or external logs, constitute the computational certificate. An external independent audit is not included.
