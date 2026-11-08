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

# Mathematical verification

The proof derives the 27-line equations, their same-partition and cross-partition intersections, the Frobenius orbits, and the total rational-point counts. It is valid for every prime power of characteristic different from three, with the characteristic-two concurrency treated separately.

The self-contained `verify_point_spectrum.py` enumerates normalized rational projective points for \(q\in\{2,4,5,7,8,11,13,16,19,31\}\) and independently tests the number of geometric lines through each. It uses polynomial-basis finite-field multiplication in characteristic two and modular arithmetic over prime fields. All ten enumerations return exactly the four-stratum formulas, including the five line-covered fields among the test cases.

The independent `verify_line_geometry.py` constructs each of the 27 lines in \(\mathbb F_7\) and \(\mathbb F_4\). It verifies 135 meeting pairs, 18 triple and 81 double points in \(\mathbb F_7\), 45 triple points and no double points in \(\mathbb F_4\), and six explicitly displayed pairwise skew lines in both characteristics.

The scripts are exact finite checks of test cases, **not** an exhaustive search over all finite fields. The universal theorem is established by the symbolic geometry and Frobenius arguments in `RESULT.md`. The existence of the classical 27 lines and the blow-up/contraction description of split smooth cubic surfaces are established algebraic-geometric inputs. No third-party paper or external dataset is included in these verification files.
