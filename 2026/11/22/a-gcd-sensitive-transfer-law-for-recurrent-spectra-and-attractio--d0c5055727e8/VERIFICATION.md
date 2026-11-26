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

In L=lcm(a,b) steps into V_j the crossing can be j+1+kb steps back, 0<=k<L/b. Its two upstream starting indices, modulo a, are j+1+kb and j+1+s+kb because L is divisible by a. These run through exactly the claimed cosets mod g, including coincident cosets if g|s. There is one all-downstream ancestor, V_j itself. The resulting idempotent F^L is a projection; on its image the two gates are already one whenever V_(b-1)=1, hence each ring rotates and the image is exactly the recurrent set. The active residue pattern weights each upstream inactive class by w, and each adjacent active pair (r,r+s) by z; the g-residue permutation has h cycles of length m, including m=1, proving the trace power. Given K=k there are beta*k writable recurrent positions and all other initial downstream coordinates are free in a phase preimage. This gives the labeled counts and full orbit basins by disjoint union over phases of the same K. In Fix(F^t), repeat words of lengths a_t and b_t. Projecting the mod-g upstream class of any j+1 or j+1+s to mod a_t yields precisely one coset of gcd(g,a_t)=g_t; reducing j mod b_t preserves those g_t residues since g_t|b_t. This proves the repeated-word support equivalence for every t, also when a_t or b_t is one. Möbius inversion counts primitive orbits and gcd(g_t,s)=gcd(g_t,gcd(g,s)) gives the asserted invariance. Survival conditional on K has non-survival factor 2^(-beta*K); the larger eigenvalue (3+sqrt(17))/4 is below 2 for the equal lengths, while for a=n,b=n+1 survival requires an all-one upstream word and at least one downstream one. The independent python3 -B /workspace/reviews/bridge_check.py uses functional-graph peeling, orbit labeling and binary iterate composition; 94 in-scope small triples (73712 initial states) and all 65536 states in each (8,8,s), s=1,2,4, confirm phase totals 2207,2209,2401, along with fiber/basin sizes, all t through L and the survival formula. No frozen script was executed. Reproducibility caveat: the frozen check_two_bridges.py main loop lists only the trace results for 8-by-8; its defined case function could enumerate those states, but its default command does not. The separate check supplies the claimed full 8-by-8 replay. These finite checks are not an all-parameter proof.

## originality

PASS

Best-of-knowledge pass for the closed recurrence and attraction census and arithmetic separation/survival consequences, not for the two-bridge projection, rotation dynamics, the transfer-matrix trace as a technique, or Möbius inversion. The published projection has substantial overlap and indeed specifies the eventual orbit from individual initial conditions; its contribution is explicitly excluded in the frozen claim.

## value

PASS

The linked-cycle topology has an established dynamical motivation. Exact weighted counts make a quantitative distinction between offsets with identical component data, determine primitive period multiplicity and individual basin sizes, and identify a sharp change in downstream activity on moving to consecutive lengths. Replacing full-state projection enumeration by residue-sized transfer data answers a natural population question about these networks. This is a structural refinement, not a claim that eventual projection or a single 16-vertex census is new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
