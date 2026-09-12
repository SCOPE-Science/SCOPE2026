# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Focus-focus monodromy barrier to splitting in singular Poisson four-folds
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1100
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Poisson Geometry
- **Method:** vanishing-cycle symplectic-area monodromy computation in relative cohomology

## Problem

Decide whether an isolated focus-focus rank-zero point of a compact Poisson 4-manifold carries a nontrivial relative-H^2 area invariant that blocks area-preserving splitting: either prove the vanishing-cycle class is nonzero and no small Poisson deformation splits p into two elliptic points with preserved leafwise areas, or construct such an area-preserving splitting.

## Attempted claim

Let (M^4, pi0) be a compact Poisson 4-manifold with an isolated nondegenerate focus-focus rank-zero point p of Williamson type (0,0,1). Then the vanishing-cycle symplectic-area class in H^2_{pi0}(M,{p}) is nonzero, so no sufficiently small Poisson deformation splits p into two nondegenerate elliptic rank-zero points while preserving all nearby leafwise symplectic areas; any such splitting changes the Poisson moduli. An area-preserving splitting disproves the claim.

## Research outcome

Proved the positive target: focus-focus point carries nonzero area-monodromy (M!=I) blocking any small area-preserving Poisson splitting into two elliptics; certified by exact sympy script (VERIFY_OK) plus self-contained DRAFT proof.

## Why this attempt failed

Failed axes: correctness, value.

correctness: TARGET route (research_report.claim_route=TARGET): audit positive proof against admitted target. FAIL: (1) Category error: Eliasson-Vey normal form cited is for integrable systems (symplectic manifold + commuting integrals), not for zeros of a Poisson bivector; no theorem cited gives Casimir map q:U->D with T^2 fibers from pi0(p)=0 alone. (2) Fiber topology false locally: focus-focus quadratic levels q^-1(c) in R^4 are cylinders C* (S^1xR), not T^2; T^2 requires global compactification never proved from compact M + rank-2 alone; leaves could be spheres, planes, dense. (3) Step 4 persistence unjustified: rank-2 open condition + Ehresmann for a fixed submersion does not imply a varying Poisson foliation stays a T^2-bundle over the same base annulus with comparable H1 basis; area comparison presupposes the identification it needs to prove, and period lattice Lambda^t is defined by fiat from S^t. No Moser argument without integrability is given. (4) Step 5 factorisation assumes split leaf space is disc minus two elliptic values with torus fibers and Gamma=g1*g2, plus elliptic smooth-action charts for general Poisson germs; not proved, and contradicts known integrable stability without discussion. (5) H^2_{pi0}(M,{p}) class never defined as Poisson cohomology; identified with monodromy rho!=I by definition. (6) Computation does not prove log residue: script posits T_L=-L+u then differentiates it, asserts M=[[1,0],[1,1]] and Me=I by hand; numerics check -log and 2pi jump tautologically; hard steps 4-5 uncertified. Sign error: listed X1,X2 = -Hamiltonian fields for stated convention i_X w=-df (still commuting, so non-fatal but symptomatic). Proof vs evidence: local commuting/periodicity checked exactly; global barrier is unproved assembly of cited local models + assumed bundle topology. value: ADMISSION_DEFECT: topic.audit_preflight target_integrity claims the hypothesis class is nonempty and canonical, realized in coupled spin-oscillator and compact semitoric/K3-type fibrations, with well-defined vanishing-torus area. Those realizations are symplectic integrable systems (nondegenerate Poisson everywhere, focus-focus as momentum-map critical point), not compact Poisson 4-manifolds with isolated rank-zero zero of pi0 and T^2 leaf-bundle neighbourhood. No compact Poisson example with the assumed T^2-bundle, Casimir disc, or H^2_{pi} class is exhibited or cited, and DRAFT assumes rather than proves T^2 fibers, fixed annulus identification, and disc-minus-two-points topology. The H^2_{pi0}(M,{p}) invariant is never defined independently of monodromy, so no natural object + invariant pair is anchored before computation. As stated the scope is vacuous/miscategorized: a formally new barrier over a possibly empty or incoherent class, with area hypothesis supplying its own bundle identification. This is exactly vacuity/type-confusion that STANDARD and TARGET policy exclude from value even if literally true. Hence value FAILS; no bounded addition sh…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Cites (rather than re-proving) the standard Eliasson-Vey focus-focus linearization, Arnold-Mineur/Dufour-Molino smooth elliptic actions, and Ehresmann stability of the regular torus bundle over the fixed outer annulus; the new contribution is the area-locked persistence plus outer-loop factorisation barrier. Result covers only the stated minimal unfolding (one focus-focus into two elliptics) for sufficiently small deformations, and characterizes obstruction via the period-lattice/log-residue in…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
