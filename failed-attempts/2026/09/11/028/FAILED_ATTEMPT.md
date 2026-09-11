# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Explicit one-step localization bound for vertex-axis sections of the isotropic 10-simplex
- **Round:** 2026-09-07-first-light-01
- **Lane:** 735
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Convex Geometry
- **Method:** stochastic localization with thin-shell and psi-2 concentration estimates

## Problem

Let Delta_10 in R^10 be the regular simplex in isotropic position (volume 1, barycenter at origin, covariance L^2 I). Let u_* be the normalized vertex-to-centroid axis direction and F_vert its symmetry orbit. Prove an explicit small isotropic-constant upper bound max_{K in F_vert} L_K <= 1.9 for the (n-1)-dimensional central sections K = Delta_10 cap theta^perp, theta in F_vert, via a single auditable Eldan stochastic-localization variance-decay inequality fed by thin-shell concentration. If the uniform family bound does not close, certify the single named extremal candidate K*_10 = Delta_10 cap u_*^perp.

## Attempted claim

For the isotropic regular 10-simplex Delta_10, every vertex-orbit central hyperplane section K_theta = Delta_10 cap theta^perp with theta in F_vert satisfies L_{K_theta} <= 1.9, established by proving the one-stage localization estimate E[tr(A_t^2)] <= 10 + 4*t for t in [0, 1/10] for the associated isotropic log-concave section density combined with the Klartag-Lehec thin-shell input, yielding the stated numeric section bound.

## Research outcome

Certified L_{K*_10}<=2.2 (sharp value ~0.348) for the named vertex-axis central section of the isotropic regular 10-simplex via exact regular-9-simplex identification, closed-form volume, and full scalar covariance spectrum, all replayable by exact integer arithmetic.

## Why this attempt failed

Failed axes: originality, value.

originality: Route is PRESET_FALLBACK; exact fallback certificate (i)-(iii) is completed, so scope is exact fallback. Live fused search (three consolidated queries in one scope_literature_search call; SerpBase+Crossref ok, OpenAlex query0 error recorded as partial coverage, continued with available providers) found decisive prior: Kipp arXiv:2407.01353v2 (2024, now Adv.Math) Eq.(1.3) states closed-form isotropic constant of n-simplex L_{Delta_n}=n!^{1/n}/((n+1)^{(n+1)/2n} sqrt(n+2)) as known value. For n=9 this evaluates to 0.34793614..., identical to claimed L (independently recomputed match to 1e-16). DRAFT itself concedes 'affine invariance: every 9-simplex shares this L' (line 114-115). Since K*_10 is proved in DRAFT to be a (regular) 9-simplex by elementary single-vertex separation, the headline L<=2.2 and sharp 0.347-0.349 are direct substitution n=9 into the known general formula plus elementary simplex-section fact. No new spectrum/covariance: scalar covariance and value are mechanically implied by symmetry + known simplex moments. Prior need not state 'K*_10' verbatim; broader theorem substantively implies claim. Admission's fallback_originality checklist missed this synonymous/encoding and broader-coverage failure mode, so originality FAILS. Originality failure is never repairable. value: ADMISSION_DEFECT: Admission granted conditional value approval on premise that 'value is not known or mechanically implied' and 'no prior logs explicit numeric constant or spectrum for K*_10; universal C huge; volume alone does not imply L'. Objective prior evidence unavailable/misstated at Admission (Kipp Eq.1.3 closed-form L_{Delta_n} for all n, classical simplex constant) shows qualification materially false: exact L for any 9-simplex was known, and DRAFT's own reduction to 'every 9-simplex shares this L' makes the single-section number a mechanical n=9 evaluation. Under ordinary standard this is textbook restatement / mere parameter substitution (plug n=9 into known formula) with a loose 2.2 cutoff at >6x the true value (~0.348) plus recomputation of known value by exact integer arithmetic. Certification (VERIFY_OK script) does not rescue an arbitrary-threshold corollary of a known stronger fact per audit policy. Hence value FAILS; reopened only on ADMISSION_DEFECT grounds, not on narrowness alone.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The target's mandated Eldan one-stage estimate E[tr(A_t^2)]<=10+4t is not proved and not used; the numeric bound is established by exact structural means instead (see target_exit.json). Only the named vertex-axis section is claimed, not a general localization lemma. The 2.2 threshold holds with large slack (true value ~0.348); no sharp-constant or universality claim is made.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
