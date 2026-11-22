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

Reproduction requires Python 3 and a C++17 compiler. Run `python3 verify_python.py` and then compile and run `verify_cpp.cpp` using `g++ -std=c++17 -O2 verify_cpp.cpp -o verify_cpp && ./verify_cpp` in the directory containing the files. The Python program also rewrites `witness_tree.json` deterministically; its nested query tree is checked at all 32 leaves. Code does not depend on external data files or nonstandard libraries.

The Python route generates Baer subplanes from F4 projective-frame matrices. The C++ route independently forms projective lines and generates subplanes by joining pairs of points and intersecting pairs of lines. Both exhaustively test every support of at most five points. Both compute Littlestone dimension via the exact recursion on concept subsets, and both find a depth-five tree and exclude depth six. The Python run reported 360 subplanes, face counts 1,21,210,1330,5880, no shattered size-five supports, and 1625 memoized calls; the C++ run reported the same counts and 24182 memoized cases (with reverse query order).

The structural shellability statement uses a known general matroid theorem, not a computed integral Smith normal form. The finite field is precisely F2[t]/(t*t+t+1). The results do not generalize automatically to other projective-plane orders, and independent audit remains unperformed.
