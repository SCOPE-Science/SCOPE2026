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

# Reproducibility and scope of verification

Run `python verify.py` from the directory containing this file. The checker uses exact rational fractions and the Python standard library only. It computes outbreak threshold probabilities in two structurally independent ways: (i) the analytic closed path formula and (ii) exhaustive enumeration of retained/closed edges, weighting all open components by their vertex sizes to account for uniform seeding. It independently verifies the mean via sums of squared cluster sizes. For each \(3\le n\le11\), every \(2\le k<n\), every \(2\le h\le n\), all ordered positive compositions of \(n\) into \(k\) parts, and three exact values of \(p\), it checks the proposed global minimum and its equality class. It also checks that balanced and concentrated component lengths are mean extremizers. For \(3\le n\le8\), smaller exact cases are checked against enumeration of every remaining open-bond state. It checks six-vertex signs at rational transmission probabilities on both sides of the crossover and at equality.

A successful execution prints:

`PASS: partition extremizers, mean, and tails for 990 parameter cases`

`PASS: independently enumerated 2964 fixed-size outbreak probabilities`

`PASS: six-vertex three-case phase transition at p=3/4`

All-size mathematical justification is in RESULT.md. Finite verification is not a substitute for the proof and does not demonstrate historical novelty. No independent external audit has been performed.
