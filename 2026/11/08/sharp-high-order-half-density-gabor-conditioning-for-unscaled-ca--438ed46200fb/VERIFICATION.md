---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Separating j even and odd gives two Parseval coefficient sums on the unit Zak torus: their windows have squared moduli |ZB_n(x,nu)|² and |ZB_n(x,nu+1/2)|², with lattice shifts contributing only unimodular factors. Hence the exact optimal bounds are the min and max of their sum; continuity removes an essential-extremum ambiguity. This gives A_2=1 and B_2^up=2 with the prescribed normalization. The Fourier aliases of a cardinal spline at reduced frequency t have magnitude s(t)^n times (|t|/|t+ell|)^n. For |t|<=3/8 the nonleading ratios are at most 3/5 and have uniformly bounded square sum, so the error amplitude relative to the unique leading alias is O((3/5)^n), also after taking squared moduli. On [1/8,3/8] the two nearest distances are nu and 1/2−nu. On the outer intervals one distance is at most 1/8, all its subleading ratios are at most 1/7, and s(1/8)>s(1/4). For L=log(s) on the central interval, L' is bounded away from zero and L'' bounded, so (s^(2n))''>0 for large n. Symmetric convexity gives the leading minimum 2s(1/4)^(2n) uniformly in x; any frequency staying a fixed positive distance away has an exponentially larger leading term. For the maximum, partition of unity gives |ZB_n|<=1 and equality at zero; the other component at any chosen frequency pair with distance at least 1/4 has amplitude bounded by a constant times s(1/4)^n, using the bounded square sum of alias ratios even at a tie. These estimates prove all prefactors and frequency localization claims. Hasannasab–Lemvig Theorem 7.1 supplies the frame property at every n>=2, not only large n.

## originality

PASS

The supported distinct finding is the sharp fixed-lattice order-growth conditioning law for the unscaled, integral-one spline, with absolute leading constants and minimizing-frequency localization. The Zak formula, spline Fourier transform, and frame existence are prior machinery, not new claims.

## value

PASS

The lattice is a canonical redundancy-two oversampling where existence alone can conceal growing ill-conditioning. The exact exponential rate and factor distinguish stability of increasingly broad standard cardinal windows from mere positivity or an unspecified asymptotic rate, and the limiting bad-frequency location identifies where conditioning is lost. This answers the motivated fixed-lattice question without conflating it with variance-normalized Gaussian approximations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
