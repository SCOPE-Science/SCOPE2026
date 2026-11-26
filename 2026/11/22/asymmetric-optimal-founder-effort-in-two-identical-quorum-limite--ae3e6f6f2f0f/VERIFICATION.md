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

Independence gives the joint failure F(x)=f(x)f(10−x), with f(z)=(1+799(1+z)e^(−z))/800. Its logarithmic derivative is H(10−x)−H(x), H(z)=z/(1+z+e^z/799); clearing positive denominators gives sign(799−G(5−x)) for 0<x<5. For u>0 the derivative of G has the sign of 5u cosh(u)−(5+u²)sinh(u); after dividing by u³, its power series is the constant 2/3 minus strictly positive even-power terms beginning at degree four. The quotient strictly decreases to −infinity, so G has just one peak and the certified crossings in (2,3) and (4,5) are simple and unique in their intervals. The corresponding F' signs on (0,5) are +,−,+; the far crossing gives a local maximum, the near crossing gives the only interior minimum. An independently computed rational certificate confirms all the needed G comparisons and F(3)<min(F(0),F(5)), ruling out the two endpoints of the half-interval. Reflection supplies exactly the second global minimum. For varying budget, renormalize the domain by the budget to [0,1]; compactness gives a uniform strict gap outside small disjoint neighborhoods of the two minima at the base point. Nonzero curvature at the minima gives unique nearby stationary points by the implicit-function theorem; compact separation and reflection make both, and only those, global. Replay: `python /workspace/review-evidence/reproduce.py 1` uses direct Taylor enclosures for exp(n) with a geometric bound on the tail, independently of the uploaded script's exp(1) power enclosure. The decimal diagnostic gives x*=2.9374809396609965009… but does not prove uniqueness.

## originality

PASS

The supported claim is the concrete, certified off-center pair and its stability in this two-site Poisson quorum model. The strongest catalogue comparison uses exactly the same optimization, under the name two-encounter confirmation. Its sharp budget theorem covers the existence of some asymmetric regime at budget 10, but its stated witness uses different parameters. Its own public comparison explicitly identifies the pair at B=10 and p=799/800 as the earlier fixed-instance claim and distinguishes its new budget quantifiers from that example. This is evidence of a recognized follow-up, not an inference of priority from the common date and not another earlier independent proof of the current instance. Other inspected catalogue cases have materially different objectives or only optimize equal doses. Historic reliability and S-shaped utility work may provide stronger earlier coverage; no such implication was verified from available passages.

## value

PASS

This is a motivated exact counterexample to a concentration-versus-equal-split dichotomy for identical patches. Both familiar candidates strictly lose, there is precisely one off-center pair, and the pair is robust rather than a degeneracy of a tie. The parameter values realize a structural change in the useful strategy set; their numerical digits are not the value claim. The follow-up's explicit use of this fixed instance as the already-established witness gives a concrete downstream reason to retain it separately from a sharp universal budget theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
