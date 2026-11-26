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

This verdict is for the complete replacement RESULT.md in /workspace/repairs/1, not the frozen wording. The frozen leading statement is false if read literally: for F=5, m=3, the word is 00 and u^2 counts the gaps 4 and 5, but 4 is the only gap strictly between 3 and 5. The repair marks (m,F], gives the u^{-1} alternative for the strict convention, and leaves the correct total genus formula unchanged. Below the conductor any pair of positive elements sums to more than F, and the initial gap block before m has length at least two. Thus perfectness is exactly the word restriction with a terminal zero-run of length >=2, including the ordinary term separately. The run decomposition gives A(z,u), with g=F-t-1+#zeros. At u=1 the cubic has negative real derivative everywhere and a simple root r in (0,1); conjugate reciprocal roots have modulus sqrt(r)<1. The continued dominant pole is simple and isolated near u=1, yielding exponentially controlled coefficients and the stated log-pole derivatives rho and v>0. Conditional on a fixed offset j the word length is h-j and its centered CLT has limiting variance v/2 in sqrt(F) units; the parity and fixed-j centering changes are bounded. The geometric bound also covers the ordinary case J=h+1, making the fixed-j mixture converge to the product. The repaired proof explicitly sums the complex coefficient error and uses analytic derivative bounds to obtain O(1) cumulant errors. Independent exact subset/addition/isolated-gap checks reproduced the full (m,g) table for F=3..18 (298 qualifying semigroups); three finite coefficient calculations agreed through word length 18. Independent differentiation and numeric checking give alpha=0.7942522056686771 and beta=0.1405488061714853; exact moments were checked through F=1001. Replay: /workspace/branches/65ad5f66-87b2-4149-8958-5b7abbb8635e/independent_semigroup_check.py and its .out companion. The supplied script was inspected, not executed; the infinite theorem rests on the proof, not the finite checks.

## originality

PASS

This verdict is only for the repaired main claim: the conditioned genus CLT with explicit constants and its asymptotic independence of the multiplicity offset. There is affirmative prior coverage of the original total count, sharp amplitude and error in equivalent word coordinates; the geometric marginal follows immediately, and the marked finite enumeration follows from known fixed-Hamming-weight run counts. These are now attributed supporting identities, not independent novelty claims. The precise joint normal/geometric limit was not supplied by the inspected antecedents. Best-of-knowledge qualification applies only to that surviving claim.

## value

PASS

The surviving contribution concerns the typical joint behavior of two intrinsic semigroup invariants under a natural exact gap restriction. It separates the tight multiplicity scale from the sqrt(F) genus scale, obtains their asymptotic independence across both parities, and gives explicit leading genus moments that differ from the unrestricted law. The conditioned joint statement, not the classical word count or its relabeling, is the mathematical value and supplies a benchmark for other strata of perfect semigroups. It neither describes smaller multiplicities nor claims to settle the unrestricted perfect population.

The dated certificate retains the supplied scientific assessment, sources and limitations.
