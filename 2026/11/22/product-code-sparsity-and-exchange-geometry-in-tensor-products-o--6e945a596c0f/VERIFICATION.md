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

# Verification and exact limits

The mathematical proof in `RESULT.md` establishes the all-integer assertions. The two standalone checkers are finite confirmations and are not substitutes for that proof. No external or independent scholarly audit has been performed.

Run `g++ -O2 -std=c++17 exhaustive_checker.cpp -o exhaustive_checker && ./exhaustive_checker` with an ordinary C++17 compiler; it enumerates all subsets (not only minimum-sized subsets) of both \(K_{2,2}\otimes K_{2,2}\) and \(K_{2,3}\otimes K_{2,2}\). Their complete code counts are respectively \(256\) and \(576\), with factorwise counts \(16\) and \(24\), degree \(12\) and \(16\), diameter four and covering radius two. It verifies each code's total-perfect condition directly from open graph neighborhoods and obtains every exchange edge and shortest-path distance.

Run `python3 independent_check.py` with Python 3's standard library; it constructs factor-product graph vertices differently, exhaustively checks all four-element subsets in those two examples, and verifies the three-factor \(K_{2,2}\) example's \(64\) factorwise codes, all \(64\) distances from a reference factorwise code, and \(1000\) reproducible ambient samples. Its arity-three \(K_{4,4}\) construction tests all \(4096\) factorwise product codes against the injective-coordinate witness and confirms that at most two of its eight pattern selections can agree with a factorwise code, proving the six-exchange example.

Scope limits: no large-arity exhaustive search was performed, the all-arity theorem is supported by its direct proof, and the exact covering radius at \(r\ge3\) for factors with shores smaller than \(2^{r-1}\) is not claimed. The originality assessment is necessarily limited by searchable historical sources.
