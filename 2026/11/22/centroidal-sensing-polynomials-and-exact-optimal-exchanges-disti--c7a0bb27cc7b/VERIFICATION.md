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

# Verification and reproducibility

The complete proof of the finite counts is provided by the two embedded standalone checkers. They require only a C++17 compiler and Python 3 standard library. Execute `c++ -O2 -std=c++17 check_cpp.cpp -o check_cpp && ./check_cpp`, then `python3 check_python.py`. Each prints `ALL CHECKS PASS` after verifying both labelled graphs.

The C++ code computes graph distances using breadth-first search and tests distinctness of the ordered partitions of detector sets induced by distance levels. The Python code instead tests the complete ternary pairwise sensor-distance comparison vector at each of the sixteen candidate locations, using distances derived directly from diameter-two adjacency, with separate implementations of graph construction and exchange adjacency. Both inspect every one of the \(2^{16}=65536\) sensor subsets for each graph, and every one-element replacement between minimum sets. The exact graph of optimal placements is traversed from every vertex to verify the claimed eccentricity distribution, not only connectedness.

Checked expected outputs: centroidal coefficient sequences for cardinalities zero through sixteen are `0,0,0,0,0,1728,6736,11152,12846,11440,8008,4368,1820,560,120,16,1` for the Shrikhande graph and `0,0,0,0,0,2112,7024,11248,12858,11440,8008,4368,1820,560,120,16,1` for the rook graph. Maximal failure-size distributions are respectively `{4:48,6:24,7:96,8:24}` and `{4:144,6:72,7:96,8:12}`. The exchange edge counts are respectively 22176 and 30624, and in both graphs every optimum has eccentricity five.

The algebraic polynomial and Bernoulli reliability factorizations were checked directly from the coefficient arrays. These certificates establish finite exactness of the specific two graph examples; they neither establish an infinite graph-family theorem nor settle historical publication priority. No independent external audit has been performed.
