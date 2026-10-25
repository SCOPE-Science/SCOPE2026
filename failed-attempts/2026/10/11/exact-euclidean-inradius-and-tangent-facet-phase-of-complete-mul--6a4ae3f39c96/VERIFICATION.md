---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For connected K_{a1,...,ak} with k>=3 and n>=3, P=conv{±(e_u-e_v)} lies in full (n-1)-dimensional H; central symmetry makes 0 an incenter (not necessarily unique). A facet at <f,x>=1 has projected H-normal f-mean(f)1, so distance 1/sqrt(n sum f_i²-(sum f_i)² over n). Higashitani--Jochemko--Michałek 2018 Proposition 3.5 yields exactly type I: one nonsingleton part ±1 with both signs, outside 0; type II: 0/1 with part-constant patterns or at least two split parts. Type I squared-normal maximum per size a>=2 is a-(a mod 2)/n. Type II maximum bounded by floor(n²/4)/n, attainable whenever it can dominate the type-I maximum; if balanced labels fail for the sole nonsingleton part, then that part is >n/2 and its type-I maximum strictly dominates C_n. All singleton parts have no type I and do realize balanced type II. Equality contact families therefore follow exactly from norm maximizers. Direct independent exact-rational enumeration of all qualifying 67 unordered multipartitions for n=3..9, with source Prop 3.5 facet-type tests, reproduced predicted maxima and type-contact sets; this finite corroboration is not the universal proof. No reliance on VERIFY_OK or old PASS.

## originality

FAIL

A separate published finding from 2026-10-11 already states the identical canonical Euclidean inradius for every complete multipartite graph with >=3 parts and the same local signed-part/global balanced-cut tangent-facet phase. Its Eq. (1), polar proof and final contact statement imply this package up to the trivial all-singleton/K3 correction. The published version additionally computes graph spread, so the current package has no independently novel principal result. This is mathematical coverage; contemporaneous ordering and authorship are not inferred.

## value

FAIL

FAIL as an independent contribution, not because graph-polytope inradii or tangent phases lack mathematical interest: the earlier accessible complete-multipartite published theorem already gives the same exact canonical Euclidean inradius and tangent-facet regime, plus an equivalent graph-spread invariant. The sole boundary refinement is an elementary K3 bookkeeping correction forced by the longstanding complete-graph facet classification; it does not supply an independently motivated invariant, new mechanism, nontrivial classification, or substantive counterexample. The finite enumeration repeats known all-n identities. The result remains a useful explanation of the same known metric phenomenon but does not meet the independent-value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
