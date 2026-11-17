---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Verified for 3-state threshold-one GHM on free path: the height gradient d(0,1)=1,d(1,0)=-1 and local excitation indicators give h_{t+1}(v)=max_{u in N[v]}h_t(u). By diameter D=n-1 the height has stabilized and no new excitation occurs after update D; states 1 and 2 vanish within two more steps, giving T<=n+1. New excitation at update D-1 can occur only at one endpoint, exactly when that endpoint is a strict maximum of initial height over all other vertices; both events disjoint. Reverse-state-word walks with strictly positive prefix heights satisfy stated 3-letter kernel equations; cancellation at the unique small formal root yields S(z)=(sqrt((1+z)/(1-3z))-1)/(2z) and EGF ordinary A(z)=sqrt((1+z)/(1-3z)). Algebraic singularity at 1/3 gives probability constant 2/(3 sqrt(3 pi n)); n=1 treated separately. Independently replayed full original-state transitions for n=1..9 and recovered 1,2,4,10,26,70,192,534,1500; examined independent transfer and max-plus source files, which are finite corroboration only.

## originality

PASS

The height/max-plus dynamics and square-root formal sequence are acknowledged prior work, but the precise identification of the *naturally longest possible free-boundary path extinction shell* with that sequence, its exact all-n coefficient and sharp random-initialization probability are absent from three highly relevant fully read primary analyses. Distinctive exact finite-path enumerator remains best-knowledge novel, not just a known table with no dynamical interpretation.

## value

PASS

Exactly counting the configurations that attain the natural largest transient in an established three-state cellular automaton is a mathematically motivated complete extremal classification, with an exact n^-1/2 rare-event law. The answer is not arbitrary because maximal first-zero time is intrinsic to the model. Although the same integers were known in other enumerative forms, identifying the precise dynamical class is substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
