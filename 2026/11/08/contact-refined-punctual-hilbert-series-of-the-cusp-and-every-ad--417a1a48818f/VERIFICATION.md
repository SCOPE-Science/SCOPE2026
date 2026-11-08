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

# Verification

The exact claim and proof are in `RESULT.md`; the standalone reproduction script is `verify.py`, executable with `python3 verify.py` using only Python's standard library. Its output ends in `CERTIFICATE_OK`.

It independently enumerates the \(\mathbb F_2\)- and \(\mathbb F_3\)-rational ideals of colength one through four in truncated versions of \(k[[t^2,t^3]]\). All subspaces of prescribed codimension are enumerated in reduced row-echelon form, and closure under multiplication by \(t^2\) and \(t^3\) is checked by exact finite-field linear algebra. Contact is computed by adjoining the image of multiplication by \(t^2\). The verified counts, for field size \(q\), are: colength one contact-one \(1\); colength two contacts one and two \((q,1)\); colength three contacts one and two \((q,1)\); colength four contact-two \(q+1\).

A separate enumeration of all multiplication-stable subspaces of \(\mathbb F_2[x,y]/(x,y)^3\) gives the length-one, -two and -three plane counts \((1,3,7)\). These agree with the first terms of the \(u=1\) rational expression, as required because \(x(y^2-x^3)\in(x,y)^3\). The script checks 21 additional numerical specializations of the full generating-series formula through colength twelve for coefficient nonnegativity and boundary consistency.

All statements at arbitrary colength and over arbitrary fields are established by the explicit cusp ideal classification and the published fat-branch modification theorem, not by the finite computations. The finite checks do not establish independent verification of the literature's general theorem or historical originality. No independent mathematical audit has been performed.
