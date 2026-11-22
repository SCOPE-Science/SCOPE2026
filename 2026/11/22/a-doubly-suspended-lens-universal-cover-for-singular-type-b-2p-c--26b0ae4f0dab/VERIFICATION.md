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

The finite certificate `verify_b6.py` is a standalone standard-library Python script. Run `python3 verify_b6.py`. It forms the join of three twelve-gon boundaries, with diagonal rotation weights \((1,3,5)\), computes the cellular orbit basis and signed boundary operators, checks \(\partial^2=0\), and computes mod-\(2\), mod-\(3\), mod-\(5\), and mod-\(7\) boundary ranks by exact modular elimination.

The verified quotient cellular counts by degrees zero through five are \((5,41,216,468,432,144)\). For mod two the Betti vector is \((1,1,1,1,1,1)\); for mod three it is \((1,0,0,1,1,1)\); for mod five and seven it is \((1,0,0,0,0,1)\). The code prints `COXETER_B6_ORBIT_MODULAR_CHECK_OK` on success. Nonzero mod-primary cohomology in adjacent degrees reflects the universal coefficient theorem. This experiment checks only the rank-six case and does not establish integral torsion exponents or the general theorem.

For the infinite proof, verify the orthogonal spectrum \(t^{2p}+1\), the unique subgroup and fixed character, the explicit \(S^1*L\) quotient homeomorphism, free residual \(C_4\) action, and the two applications of transfer at complementary primes. The entire proof does not require an untested inductive assertion or extrapolation from finite examples. No external independent audit has occurred.
