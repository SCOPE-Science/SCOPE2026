---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

FAIL

The headline four-block formula is correct on independent rederivation, but its required exact breakpoint certificate as frozen does not solve the claimed linear systems. In verify.py:37–48, u,v,w are the rows of M; the scalar triple products replace rows and thus solve M^T X = rhs, not M X = rhs. For y=1/2, x+y=1, 3x+y+3a=5/2, the true isolated concurrence is (x,y,a)=(1/2,1/2,1/6); the code instead obtains (13/6,-2,5/6) and discards the triple. The 31 listed rows also repeat y=0 and y=1. Independent exact enumeration by intersecting the first two nonparallel lines in the (x,y) plane as functions of a and substituting in the third found 27 qualifying triples among 29 distinct lines, all at a=1/6, not the recorded twelve. Independent exact vertical-strip integration returned 1/3, 2/9, -1/9, -5/18, -1/3 at the five interpolation nodes. Away from the sole isolated breakpoint, all feasible vertices are affine and each area at most quadratic, confirming the formula. Pair independence is Haar pushforward by a full-rank integral map; the half-period y-shift kills odd moments; Walsh inversion gives the word law. The first piece has its sole zero at 1/(4√3), the second never vanishes, and a polynomial Bowen covering bound proves zero entropy, excluding Bernoulli because the factor is nontrivial. The failure is in the original required certificate, not a counterexample to the probability law.

## originality

FAIL

The exact evaluated law and uniform phases have distinct, verified indexed coverage, including a stronger progression result. This is a finding of current coverage, not an assertion that either later-dated catalogue entry had priority over the frozen record. The 2004 paper separately supplies a general Fourier representation and already covers the object and low-order context; no explicit earlier evaluation is established by this review. No scientifically distinct remainder of the submitted central claim warrants a repair.

## value

PASS

In isolation the evaluated law answers a natural first potentially nontrivial finite-window question for a standard zero-entropy sign process: all smaller distinct-time marginals are uniform, yet the fourth block is usually not, and isolated irrational phases restore its uniformity. This assessment of mathematical utility is not credit for a separate contribution where indexed coverage already exists.

The dated certificate retains the supplied scientific assessment, sources and limitations.
