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

# Reproduction

Compile `verify.cpp` with a C++17 compiler and execute it to regenerate the complete sorted list; compare to `upwords_order5.txt`. Run `verify.py` with the list and regenerated file to independently inspect compatibility multiplicities and reversal/complement closure. Example:

```sh
g++ -O2 -std=c++17 -Wall -Wextra verify.cpp -o verify
./verify > enumerated.txt
python3 verify.py upwords_order5.txt enumerated.txt
```

The actual replay visited 31,600,915 recursive nodes, independently regenerated all 1,328 literal words, and returned `EXHAUSTIVE_OK nodes=31600915 total=1328 by_length=26:8,27:32,28:32,29:136,30:352,33:768,`. Direct five-bit target expansion for every listed word and the four transforms of every word passed in Python: `VERIFY_OK words=1328 orbits=332`. These checks certify an exact finite computational exhaustion, not an unbounded theorem about all word orders. The enumerator's exhaustiveness and safe pruning are proved in `RESULT.md`; a log without these arguments would not be enough.
