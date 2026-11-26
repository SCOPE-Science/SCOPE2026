---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Final assessment is of the repaired statement. The original unrestricted even-unimodal extension was not well-defined: the centered Cauchy is even unimodal, but C_f(0) and L_f both diverge; in particular their scaled subtraction is undefined. The repair requires E|X|<∞ for the extension and updates both the result and the scientific scope statement in the accompanying self-review. This condition is automatic in the original log-concave class. For finite first absolute moment, decompose crossing length into distances to the cut to obtain C=2[(1-F)a+Fb], with a=E(t-X)_+, b=E(X-t)_+. Absolute continuity and b-a=mu-t give C'=2f(t)(mu-t); the positive interior density in the stated class yields the unique centered maximum. Opposite-sign pairs give its value E|X|=I1. Integrating indicators of thresholds between the two endpoints gives L=2I1-I2, I2=∫g². The half-line survival inherits log-concavity by the monotone hazard, so g²≥g(2t); the defect integral follows and can vanish only when -log g is linear by convexity and equality under doubling. Bounded support cannot satisfy equality in its upper half. For the upper side, H(da)=-2a df(a) is a probability law by integration by parts for the monotone profile, allowing atoms in the mixing law and interpreting the density a.e. Finite E|X| implies EA=2E|X|, so subtraction is legitimate. Given a≥b, E|aU-bU'|=a/2+b²/(6a); subtracting (a+b)/3 gives exactly (a-b)²/(6a). Independence forces a deterministic radius at zero defect. The polynomial family gives the advertised continuous range strictly between the endpoints and the uniform endpoint. Separate direct integrations of length over the two endpoint coordinates verified p=0,1,2 and an unequal-radius identity (`python3 -B /workspace/review_replay.py`, check 4). No uploaded checker was executed.

## originality

PASS

Reassessed after specifying the finite-moment scope. Pass for exact sharp range with extremizer classification and the two named defects, not for the weighted-cut model, location of the best cut on symmetric laws in covered settings, the MAD–Gini relation, or the scale mixture representation. Both the ordinary signed Gini/MAD alias and the Gini index of the absolute-value law were checked. The available comparisons do not cover the two rigidity defects and the class-wide classification together; historical priority of individual bounds is not certified.

## value

PASS

Even after crediting the classical dispersion reduction and centered optimality, the exact attainable interval and scale-rigidity defects are a meaningful answer for a natural restricted class of length-weighted cuts. The defects quantify precisely how departures from exponential survival and from a single uniform scale affect the two endpoint inequalities. The explicit continuous family separates class-wide attainability from a table of isolated distribution values. Finiteness is automatic for the motivated log-concave class and is merely made explicit for the optional unimodal extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
