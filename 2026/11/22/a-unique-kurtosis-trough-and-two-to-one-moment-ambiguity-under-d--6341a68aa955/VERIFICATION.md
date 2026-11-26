---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Complete Poisson resets couple all initial states at the first reset and give the exponential-age stationary law; reflection makes the even raw moments central, and the quadratic growth bound gives integrability. Independently, integrate the ordered sign correlation by passing to successive gaps and cancelling the age-density factor against the initial translation integral. With c=r+2γ, the two-gap result is m2=2a²(2c+r)/(r³c²). For four gaps, normalize the product measure to independent exponential variables of rates (c,r,c,r); put V=u3+u4. Averaging the polynomial over u1,u2 gives [2/r²+1/(cr)+(2/r+1/c)V+V²]Vu4. Using exponential factorial moments then gives m4=24a⁴(40c³+36c²r+21cr²+8r³)/(c⁵r⁶), exactly the stated expression. Their ratio minus three gives the reported K. Its derivative numerator is proportional to a strictly increasing cubic with opposite boundary signs; K−57 has numerator proportional to z(15z²+6z−16) with exactly one positive crossing. Gaussian conditional variance 2DT³/3 gives the comparison 57, and a strictly positive acceleration can match any chosen variance on either branch. The endpoint limits and monotonicity yield exactly two preimages in the claimed open interval. This is not full-law nonidentifiability. CHECKER.py and VERIFICATION.md were inspected, not executed; the exponential-moment reduction and derivative calculation above give a replay independent of execution.

## originality

PASS

The bounded pass is for the exact stationary shape, Gaussian crossing and inverse fold together, not the unreset trajectory, exponential-age renewal formula or second moment. The closest primary general formula produces Laplace moments after extraction and reset integration; it does not already supply the stationary fourth-moment shape or inverse classification. The closest indexed inverse result is for a different stochastic generator and a different observation map.

## value

PASS

The moment observables are natural for calibrating inertial transport. Even with known reset rate, the theorem pinpoints an open interval on which variance and fourth moment do not identify the switching rate or acceleration amplitude, and separates it from the Gaussian acceleration benchmark. This is a global inference obstruction, not a tabulation or a numerically detected extremum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
