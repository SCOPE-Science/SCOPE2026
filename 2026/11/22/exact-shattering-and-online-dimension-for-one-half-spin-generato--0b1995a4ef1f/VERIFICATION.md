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

# Verification and scope

The proof in `RESULT.md` establishes the classification for every prime power and all ranks at least two. Its nonstandard step is the avoidance argument for one prescribed half-spin generator family: the single-point incidence probability in each quotient is \(1/(q^{r-1}+1)\), and fewer than \(r\) points must be avoided. The unique same-family extension of a codimension-one singular subspace is essential to the online upper bound.

Three independently structured enumerators provide finite boundary checks. Run in a working directory containing the files:

```sh
python3 code/verify_binary.py
g++ -O2 -std=c++17 code/verify_binary.cpp -o check_binary
./check_binary
python3 code/verify_ternary.py
```

Expected binary generator family sizes in ranks \(2,3,4\) are \(3,15,135\), and the rank-three binary face counts are \(1,35,315,0\). The independent C++ binary generator enumeration confirms the rank-four top-face count \(56700\). The ternary implementation confirms 16 projective singular points and four same-family generators at rank two, and 130 singular points, 40 same-family generators, and 3120 shattered pairs at rank three.

These finite checks do not substitute for the proof of the unrestricted field/rank theorem. In rank four the programs exhaustively count independent totally singular triples but test only a representative sample of their Boolean traces. Any independent reproduction of the universal claim must verify the quotient-incidence argument and parity-of-generator-systems property, not infer universality from the test runs.
