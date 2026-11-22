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

# Verification instructions and scientific limits

The file `verify.cpp` is a standalone C++17 verifier. It uses only the standard library and a compiler supporting unsigned 32-bit integers and a standard population-count intrinsic. Build and run:

```sh
g++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify
./verify
```

Expected textual output is included verbatim in `verification-output.txt`. Each of the four reported finite-code cardinality-layer counts arises from enumeration of every binary mask of the stated weight. The size-16 ternary layer contains \(13{,}037{,}895\) masks and no feasible code. The size-15 layer contains \(17{,}383{,}860\) masks and exactly one feasible code, equal to the adjacent-repeat construction. The corresponding binary layers contain eight and 28 masks, respectively. The program enumerates all \(4^4\) possible received words for the 29-word four-letter code. Checks at alphabets from four through twelve additionally test the blockwise lift, but do not certify unbounded alphabets.

The mathematical proof of the infinite-alphabet extension is the blockwise-lifting argument in `RESULT.md`. The verifier's exhaustive finite cases establish the small-alphabet maxima and uniqueness, conditional on inspection of the finite code, compiler behavior, and the fixed-weight-mask successor. A separate numerical optimization reproduced the small case as a cross-check but is not substituted for the enumerative certificate. No external or independent scientific audit has been performed.
