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

# Verification and scope
The standalone Python 3 program `verify.py` has no external dependencies. Run `python3 verify.py` in the package directory. It enumerates orbits and all faces of the geometric fixed-point orbit complex independently of the theoretical three-type presentation, reconstructs reduced mod-two simplicial homology by exact bitwise elimination, and checks predicted compatibility relations. Successful execution prints `ALL_VERIFY_OK cases=6 face_sets=10321`. The preserved output is in `verify_output.txt`.

For dimensions \(n=2,3,4,5,6,7\), the observed reduced Betti numbers in dimensions two and three are respectively \((0,0),(1,0),(5,0),(17,2),(49,18),(129,98)\), and each agrees with the formula. The program tests **finite cases only**; mod-two ranks cannot establish integral torsion-freeness, simple connectivity, or an infinite family. Those are established in the proof by orbit-face identification, contractible-simplex links with explicit cycles, the integral connecting-map surjectivity, and van Kampen.

Independent mathematical audit: not performed. No machine-checked proof or external certification is claimed.
