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

# Exact finite verification

The result concerns the six discrete strengths \(t=1,\ldots,6\) only. For a primitive winding \(v\) a hyperbolic-cross design geodesic is equivalent to the finite condition \(m\cdot v\ne0\) for every nonzero \(m\in H_3(t)\). Every minimal vector has, after sign changes and permutation, positive ordered coordinates \(a\le b\le c\), with \(\gcd(a,b,c)=1\). The proposed winners establish finite norm caps \(C_t\); any shorter or equal-length competitor must lie in the exhaustive integer box \(1\le a\le b\le c\le\lfloor\sqrt{C_t}\rfloor\) and also satisfy \(a^2+b^2+c^2\le C_t\).

To verify, execute `python checker.py` using Python 3 and its standard library. It generates each complete integer hyperbolic cross, enumerates every potential norm-bounded primitive competitor, and searches every cross frequency for an exact vanishing integer dot product. It asserts the unique survivors and their squared norms \((21,65,101,133,133,314)\). Primitive candidate counts are \((9,41,80,119,119,421)\), and the numbers excluded by exact integer witnesses are \((8,40,79,118,118,420)\). The proof of the search bound makes this a reproducible exhaustive finite certificate, not a random experiment or a partial numerical scan.

This finite theorem does not cover all strengths or nongeodesic designs. An earlier equivalent computational table remains a historical-priority possibility. Independent audit was not performed.
