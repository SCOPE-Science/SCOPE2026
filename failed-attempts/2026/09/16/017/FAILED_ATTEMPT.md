# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Cusped fibered genus-bound rigidity via arc-complex distance and sutured Floer decomposition
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20451
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Low-Dimensional Topology
- **Method:** Heegaard Floer and sutured-manifold decomposition analysis

## Problem

Let Sigma=Sigma_{g,1} be a compact orientable surface of genus g>=2 with one boundary component, and phi:Sigma->Sigma an orientation-preserving homeomorphism fixing boundary pointwise whose interior is pseudo-Anosov. Let M_phi be the resulting finite-volume hyperbolic 3-manifold with torus boundary. Let d_AC(phi) be translation distance in the arc-and-curve complex AC(Sigma). Let H in M_phi be a closed strongly irreducible Heegaard surface of genus h>=2, and H_std the standard genus-2g+1 splitting. Is d_AC(phi) <= -chi(H)=2h-2, hence is every H with 2h-2<d_AC(phi) a stabilization of H_std? In particular, if d_AC(phi)>4g, is g(M_phi)=2g+1 with unique minimal-genus splitting H_std up to isotopy? Decide by Heegaard Floer and sutured-manifold decomposition analysis.

## Attempted claim

Let Sigma=Sigma_{g,1} be a compact orientable surface of genus g>=2 with one boundary component, and phi:Sigma->Sigma an orientation-preserving homeomorphism fixing boundary pointwise whose interior is pseudo-Anosov. Let M_phi be the resulting finite-volume hyperbolic 3-manifold with torus boundary. Let d_AC(phi) be translation distance in the arc-and-curve complex AC(Sigma). Let H in M_phi be a closed strongly irreducible Heegaard surface of genus h>=2, and H_std the standard genus-2g+1 splitting. Is d_AC(phi) <= -chi(H)=2h-2, hence is every H with 2h-2<d_AC(phi) a stabilization of H_std? In particular, if d_AC(phi)>4g, is g(M_phi)=2g+1 with unique minimal-genus splitting H_std up to isotopy? Decide by Heegaard Floer and sutured-manifold decomposition analysis.

## Research outcome

Proved the cusped fibered genus-bound rigidity: d_AC(phi)<=2h-2 for strongly irreducible H, stabilization rigidity below the distance, and genus 2g+1 with unique minimal splitting when d_AC>4g.

## Why this attempt failed

Failed axes: correctness, originality.

correctness: TARGET proof has essential boundary-condition gap. (1) graphic adaptation is plausible, but (2) thin-position promotion fails: compressing closed H yields closed G, which cannot equal bounded fibers Sigma_{g,1}; draft claims thin levels are fiber unions and amalgamates bordered Sigma x I blocks via closed-product Waldhausen Theorem 2.2/Reidemeister-Singer without proof. Bounded-separator control via Juhasz/Ni fiber-class norm minimality does not control arbitrary weak-reduction surfaces outside fiber class. H_std with 4g<d would be a self-stabilization, needing trivial-stabilization fix. Artifact genus_counts.py checks only -chi=2h-2 arithmetic, not graphic or thin position. Essential inference unverified: proof incomplete, not just presentation. originality: Nearest prior Bachman-Schleimer 2005 'Surface bundles versus Heegaard splittings' proves identical headline for closed fiber: Theorem 6.1 d_C(phi)<=-chi(H) for strongly irreducible H, Corollary 3.2 stabilization when -chi(H)<d_C, Remark 3.3 unique minimal genus 2g+1 when d>4g, via same Rubinstein-Scharlemann graphic, pants count 2h-2, Casson-Gordon/Scharlemann-Thompson untelescoping and F x I amalgamation. Draft's bordered AC version is substantively implied by draft's own trivial steps: closed H meets fibers in closed curves so boundary is irrelevant, and curve inclusion gives d_AC<=d_C, making AC conclusion weaker and AC hypothesis d_AC>4g stronger. No new theorem, boundary or encoding escapes coverage.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; address the recorded limitation: Proof is a research-level assembly: the RS-graphic fair-position counting and Waldhausen-type product-block Heegaard uniqueness plus amalgamation steps are cited to standard theorems (Bachman-Schleimer, Hartshorn, Casson-Gordon, Scharlemann-Thompson, Waldhausen, Reidemeister-Singer) rather than reproved line-by-line; Floer input is used as a detection/minimality certificate. No explicit phi with d_AC>4g is constructed here (existence cited to standard high-power/Penner pseudo-Anosov theory), an…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
