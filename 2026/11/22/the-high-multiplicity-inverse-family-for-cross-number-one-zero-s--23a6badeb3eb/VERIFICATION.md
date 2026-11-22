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

# Reproducible verification

The self-contained `check.py` requires only Python 3 and the standard library. Execute `python3 check.py` in the same directory. The script constructs the exact family for the odd primes \(3,5,7,11,13\), counts its two- and three-supported members, and independently performs a dynamic-programming search for a zero-sum subsequence of cross number one in every generated sequence. In addition, for \(3,5,7\) it enumerates the complete set of unordered sequences at the sharp length and verifies equality with the displayed family.

Observed results:

```
p=3; construction=4; support2=4; support3=0; full enumeration=4; all checks PASS
p=5; construction=48; support2=24; support3=24; full enumeration=48; all checks PASS
p=7; construction=180; support2=60; support3=120; full enumeration=180; all checks PASS
p=11; construction=900; support2=180; support3=720; full enumeration=not attempted; all checks PASS
p=13; construction=1584; support2=264; support3=1320; full enumeration=not attempted; all checks PASS
```

In the dynamic program a weight is \(\gcd(x,2p)\). A state is an integer weight between \(0\) and \(2p\) together with a residue class for the term sum. A cross-number-one zero sum is detected exactly when the state (weight \(2p\), residue zero) is reached. The program does not use the theorem's reduction to \(C_p\) to decide whether a constructed sequence is valid. All finite enumerations are bounded checks; the universal statement for arbitrary odd primes relies on the written proof.
