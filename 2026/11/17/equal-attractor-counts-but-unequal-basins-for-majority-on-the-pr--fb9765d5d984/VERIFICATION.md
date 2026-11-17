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

# Reproducible finite certificate

The archive contains the exact plain-text programs `verify_reduced_gp.py` and `verify_full_gp.cpp`, and their independent standard output transcripts `verification_reduced_output.txt` and `verification_full_output.txt`. They are free of external dependencies other than Python 3 and a C++17 compiler.

Run:

```sh
python3 verify_reduced_gp.py > reduced.out
g++ -O3 -std=c++17 -Wall -Wextra -pedantic verify_full_gp.cpp -o verify_full_gp
./verify_full_gp > full.out
cmp reduced.out verification_reduced_output.txt
cmp full.out verification_full_output.txt
```

`verify_reduced_gp.py` constructs \(U\) and \(V\) from graph adjacency, enumerates \(2^{10}\) states in each shore, checks \(124\) fixed points in each two-step map, computes the terminal projection distribution and the exact first-entry/period table for every \(2^{20}\) initial shore pair. `verify_full_gp.cpp` builds the original twenty 3-neighbor masks and independently evolves all \(2^{20}\) 20-bit states for each graph, producing the matching records without referring to the shore factorization.

The integer identity \(T^3=T^2\) on each of the four ten-bit maps can be checked directly by applying the map three times to each of \(1{,}024\) inputs. The reduced code's loop asserts that each input reaches a shore fixed state within at most twenty updates; the complete outputs and the verified four-update maximum show a much stronger bound. This finite proof requires no extrapolation. All claims are confined to these graphs and the stated update convention.

No outside source or authority has independently audited these results.
