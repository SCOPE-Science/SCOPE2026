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

The witness data `parameters_q7.txt` comprise \(16\) consecutive triples of vectors on \(\mathbb F_7^2\), each vector having \(49\) entries. All entries lie in \(\{1,\ldots,28\}\) and are interpreted in \(\mathbb F_{29}\). The C++17 code reconstructs derivatives using the explicit twisted-convolution coefficient formula; it is not a precomputed rank table. The reduction uses \(\zeta_7\mapsto7\), which has order exactly seven in \(\mathbb F_{29}\).

Exact commands from the directory holding the included files:

```sh
g++ -O3 -std=c++17 verify_q7.cpp -o verify_q7
./verify_q7 parameters_q7.txt
python3 check_derivatives.py parameters_q7.txt
```

Observed exact output:

```text
type=(0,0) rank=2320 expected=2320
type=(0,1) rank=2320 expected=2320
type=(1,1) rank=2320 expected=2320
type=(1,2) rank=2320 expected=2320
ALL_FOUR_JACOBIAN_RANK_CERTIFICATES_OK
INDEPENDENT_DERIVATIVE_FORMULAS_OK 240
```

There are \(49^2=2401\) target coordinates. For each of the \(16\) summands the verifier selects \(3\cdot49-2=145\) derivative columns, and proves their total \(2320\) columns independent for each type orbit. Full rank over \(\mathbb F_{29}\) implies a nonzero \(2320\times2320\) minor over the cyclotomic integer ring and hence over \(\mathbb C\). The differential upper bound and the four type orbits finish the proof. The second independent checker compares finite differences of the original coefficient sums to their separately coded derivative formulas for \(240\) sample positions. It is a formula check, not a replacement for the full-rank computation.

The remaining limitations are mathematical: no conclusion about the expected filling at \(r=17\), all larger primes, or independent external validation.
