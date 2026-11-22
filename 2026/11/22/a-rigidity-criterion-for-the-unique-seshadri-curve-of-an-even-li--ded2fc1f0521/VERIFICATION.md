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

# Reproducibility and checks

The stand-alone Python 3 script `checker.py` carries out exact modular arithmetic. Execute it from the directory containing this file with `python3 checker.py`; it requires only the Python standard library. Its successful output confirms:

- All \(\binom{16}{2}=120\) pairs produce exactly \(38\) geometric projective intersections in characteristic \(7\), with incidence multiplicities \(16,12,8,2\) at multiplicities \(2,3,4,5\).
- Fourteen input lines contain seven distinct singular points, two contain six, and the external line \(M\) contains eight, all ordinary double points.
- Each of \(L_1,L_3,L_{10},L_{15}\) has exactly one ordinary double point, and these four points are distinct and lie on \(M\).
- Exhausting the \(57\) rational lines gives just one eight-secant, namely \(M\); this is supplemental to the geometric proof.

Every geometric intersection of two distinct \(\mathbb F_7\)-rational lines is \(\mathbb F_7\)-rational, so the incidence enumeration is geometrically exhaustive. The deduction concerning integral curves of arbitrary degree and the blow-up null locus is an algebraic intersection-theoretic proof and is **not** inferred from the finite computation. It uses only Bézout, the inequality \(I_P(L,C)\ge\operatorname{mult}_P C\), and intersection numbers of the plane blow-up.

The hypotheses are sufficient, not necessary. Neither semi-ampleness nor a classification of the full nef cone is verified. Independent audit has not been performed.
