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

# Reproducibility and limits

From the directory containing these files, compile and run:

```sh
c++ -std=c++17 -O2 verify.cpp -o verify
./verify
python3 verify_independent.py
```

The first program constructs actual strictly upper-triangular \(4\times4\) matrices and multiplies them as matrices, independently of the abstract fiber count, over fields of orders \(2\), \(3\), and \(4\). The order-four field is represented using the polynomial relation \(z^2+z+1=0\). The following was observed:

```text
q=2 pairs=4096 zero=1024 pure=768 generic=384 verified
q=3 pairs=531441 zero=41553 pure=34992 generic=17496 verified
q=4 pairs=16777216 zero=557056 pure=491520 generic=245760 verified
VERIFY_OK
```

The separate program enumerates first-layer projected fibers and performs finite-field Gaussian elimination on adjoint matrices over prime fields of orders \(2\), \(3\), and \(5\). It checks the independent zero-fiber rank sum and the global pair normalization. Its observed rank distributions were:

```text
rank spectrum q= 2 {0: 2, 1: 6, 2: 32, 3: 24}
rank spectrum q= 3 {0: 3, 1: 24, 2: 270, 3: 432}
rank spectrum q= 5 {0: 5, 1: 120, 2: 3500, 3: 12000}
VERIFY_OK
```

The exact formula for all prime powers is established by the proof in `RESULT.md` using only linear equations over fields. The programs are finite corroboration, not universal verification or independent expert certification. No assumption about untested larger matrix sizes is made.
