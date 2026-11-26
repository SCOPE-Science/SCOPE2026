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

Plancherel gives the asserted operator norm at positive integer order, and y=sin²(theta/2) maps the whole circle onto [0,1] with difference amplitude 2 sqrt(y). Normalized real even symbols of degree at most two are exactly q(y)=1-a*y+b*y². For r=kappa/2>0 and h>(r+2)/r, the ratio ((r+2)h-r)/(rh-r-2) decreases strictly from infinity to (r+2)/r, whereas h^(r+1) increases unboundedly. This proves the first root prescription including uniqueness. Q(z)=1-Az+Bz² has Q(h)<0, Q'(h)>0 and B>0. Beyond its zero on (h,infinity), z^r Q(z) increases strictly from zero to infinity, so the second positive-level equation has exactly one solution. Differentiating the candidate weighted polynomial gives (r/h)y^(r-1)(zy-1)(zy-h), so the interior extrema are 1/z and h/z, and their evaluations using the root equations have signed heights +C/z^r and -C/z^r, with +C/z^r at the right endpoint and zero at the left. There are no other contacts in y. On the circle the first two interior y levels correspond to symmetric pairs of frequencies. A competitor with no larger norm must have differences of signs <=0, >=0, <=0 at the contacts. Dividing the difference by the positive y produces an affine function, so the middle value is a strict convex combination of the other two and all three must vanish. Cosine expansion recovers (5); in particular b>0 and the middle contact is negative. The constrained Fourier-nonnegative minimum exists (closed constraints, and bounded level sets from evaluation at two distinct positive y); uniqueness then implies a strict gap. Independently ran `python audit_checks/independent_replays.py 4`: 16,001-point epigraph LP and off-grid stationary point checks at orders 0.5, 1, 5, 6 and 12. At order 5 the mesh gave about 0.733730431 with off-grid ripple error about 3.2e-8 and the claimed taps to about 1e-9. The mesh is not the proof; the exact argument covers all real positive orders. Submitted code was inspected, not executed.

## originality

PASS

The convolution optimization, polynomial reduction and alternation framework have prior coverage; the same radius is included in known unrestricted integer orders 1–3. The distinct contribution supported on the evidence is the explicit all-positive-real-order, finite-order, unrestricted radius-two evaluation and its unique optimizer, notably at order five and the unrestricted fourth and sixth orders. No distinct source with full equivalent or dominating coverage was established. Priority is provisional; actual retrieval limits appear below.

## value

PASS

Five taps are the first two-free-coefficient case of the same normalized smoother problem; the fifth difference illustrates a natural previous gap. The scalar equations turn qualitative equioscillation into the actual sharp finite-order value and a unique filter, rather than just a numerical or asymptotic prediction. The negative middle contact rigorously explains why Fourier positivity raises the optimum. No utility for larger radius or nonsymmetric filters is assumed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
