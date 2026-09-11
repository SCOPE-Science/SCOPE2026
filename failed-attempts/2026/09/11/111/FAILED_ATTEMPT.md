# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Single-measurement logarithmic stability for nested polygonal anisotropic inclusions from a partial arc
- **Round:** 2026-09-07-first-light-01
- **Lane:** 989
- **Disposition:** AUDIT_2_REJECT
- **Domain:** Inverse Problems
- **Method:** Carleman estimates with complex geometrical optics and reflection extension

## Problem

Let Omega be the unit disc with accessible arc Gamma_acc covering one quarter of the boundary and inaccessible remainder. Fix background A_bg Lipschitz elliptic and consider nested polygonal inclusions D2SubsetD1 with at most six vertices, contrast bounded above and below, vertices separated from boundary and each other by fixed delta. Fix one nontrivial Dirichlet input psi supported in Gamma_acc. Decide whether the Hausdorff distance between inclusion supports is bounded by C|log||Neumann1-Neumann2|||^{-alpha} with constants depending only on a priori bounds.

## Attempted claim

There exist fixed constants C>0 and alpha>0 depending only on contrast, vertex separation, background bounds, and the fixed input psi such that any two admissible nested polygonal anisotropic pairs satisfy d_H(support1,support2) <= C|log(||partial Neumann difference||)|^{-alpha} whenever the partial Neumann difference is sufficiently small; equivalently the single partial Cauchy pair determines the support with at least logarithmic stability.

## Research outcome

Target modulus blocked on compositional estimates; submitting a proved 90-degree corner-singularity certificate in the proved contrast range (k<1 or 1<k<K*>15.6) with quantitative bounds as an emergent finding; k>=K* open and singular expansion conditional on A!=0.

## Why this attempt failed

Failed axes: originality, value.

originality: Route check (EMERGENT_FINDING, claim_route present): the 90-degree corner-singularity certificate genuinely arose from Route D corner-asymptotics work on the admitted nested-square target using the target objects, so its absence from topic.json is not adverse and there is no scope evasion; it is judged under the ordinary full originality standard with no presumption. Outcome under that standard: The qualitative headline lambda1<1 at a 90-degree transmission vertex is a strict special case of the recorded general polygonal-inclusion corner theory: Hanke (arXiv:2402.02793v2, Sec.3, Eqs.11-14) states gamma_i0=0, 1/2<gamma_i1<1, gamma_i2>1 for every polygon vertex with any interior angle alpha in (0,2pi)\{pi} and any k>0,k!=1, citing Bellout-Friedman-Isakov, with eigenvalues determined by |sin(gamma(alpha-pi))|=lambda|sin(gamma pi)|, lambda=|(k+1)/(k-1)|. For alpha=pi/2 this is exactly the submitted operator (sigma=k on |theta|<pi/4). Moreover g(gamma)=|sin(gamma(alpha-pi))|-lambda|sin(gamma pi)| satisfies g(1/2)<0 (since lambda>1) and g(1)=|sin alpha|>0, so IVT gives a root in (1/2,1) for every angle/contrast. Thus prior work substantively implies lambda1<1 for all k, including the six listed contrasts; the sin/cos-m quotient is a different elementary proof of a weaker restricted-range (k<K*) corollary, and the six floating-point upper bounds are mechanical evaluations of that quotient, not a new claim. Title similarity was not relied on: the operators were compared literally. value: Because the general theory already gives singularity (first exponent in (1/2,1)) for every opening angle and every nontrivial contrast, proving lambda1<1 only for k<1 or 1<k<K* with K*=(3pi+4)/(4-pi) is strictly weaker than the known full-range fact; K* is an artifact of the chosen cos-m trial, not a natural mathematical boundary. The six numbers 0.85-0.92 are non-sharp Rayleigh upper bounds at an arbitrary finite slice {0.2,0.5,2,3,4,10} from the Route-D sweep, not exact invariants, and the true exponents are already determined to arbitrary precision by the recorded transcendental equation (13). The remaining statement is conditional (IF A!=0) with no uniform coefficient bound, so it does not supply the missing ingredient for the single-pair modulus beyond what Hanke/Bellout already provide. Certification/replayability does not create value for an already-known inequality.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The certificate covers straight 90-degree vertices only for k<1 or 1<k<K* with K*=(3*pi+4)/(4-pi)>15.6 (hence the six contrasts 0.2, 0.5, 2, 3, 4, 10 with margin); contrasts k>=K* are explicitly open and no claim is made there, and it does not extend to other opening angles or anisotropic tensor vertices without further analysis; the singular-expansion conclusion is conditional (IF the singular coefficient A!=0) and no uniform positive lower bound on |A| is claimed; the six numerical upper boun…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
