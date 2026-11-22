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

# Reproducibility record

The independent Python and C++ programs in `verify_python.py` and `verify_cpp.cpp` were run from complete standalone files and both yielded exactly the records in `CERTIFICATE.txt`. The main graph is encoded by an explicitly stated twelve-element LCF offset sequence. Python computes shortest paths using twelve breadth-first searches; C++ instead uses Floyd–Warshall. Both enumerate all 4,096 vertex masks, test 66 distance-distinguishing constraints at every redundancy level, construct one-replacement jump and slide transitions, and independently compute all connected-component radii and diameters from all-source shortest paths.

Commands:

```sh
python3 verify_python.py > python.out
c++ -O2 -std=c++17 verify_cpp.cpp -o verify_cpp
./verify_cpp > cpp.out
cmp python.out cpp.out
cmp python.out CERTIFICATE.txt
```

A successful comparison gives a finite, replayable exhaustiveness check; it does not constitute independent professional validation or historical priority proof. The result has no external data, network dependency, random seed, or missing file dependency. All claims concern this one finite graph and this exact move definition.
