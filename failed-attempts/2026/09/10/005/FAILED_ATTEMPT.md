# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Disjoint-arc partial-data Calderon uniqueness on the unit disk via paired two-weight CGOs and disjoint chord-transform injectivity
- **Round:** 2026-09-07-first-light-01
- **Lane:** 501
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Inverse Problems
- **Method:** complex-geometrical-optics construction with Carleman estimates and attenuated geodesic ray-transform comparison

## Problem

Let D={|x|<1}, Gamma_D={e^{itheta}:|theta|<pi/4}, Gamma_N={e^{itheta}:|theta-pi|<pi/4} (closures positively separated). For real q in C^{1,alpha}(D) let Lambda^{D->N}_q map Dirichlet data f supported in Gamma_D to Neumann data (d_n u)|_{Gamma_N} of (Delta+q)u=0. Does Lambda^{D->N}_{q1}=Lambda^{D->N}_{q2} imply q1=q2 via paired two-Morse-weight CGOs vanishing on the respective complements plus injectivity of the disjoint attenuated chord transform over chords joining Gamma_D to Gamma_N, and if not, what explicit single-measurement triple (f*,q1,q2) with matching Neumann data on Gamma_N witnesses the obstruction?

## Attempted claim

Let D, Gamma_D, Gamma_N be the fixed disjoint quarter-arcs above. For all real q1,q2 in C^{1,alpha}(D), if the disjoint maps agree (Lambda^{D->N}_{q1}=Lambda^{D->N}_{q2}) then q1=q2 in D, established by (i) paired Morse-weight CGOs u^D_h, u^N_h vanishing on dD\Gamma_D and dD\Gamma_N respectively and (ii) injectivity of the resulting disjoint attenuated chord transform I^{D->N}_a on chords with one endpoint in Gamma_D and the other in Gamma_N.

## Research outcome

Target disjoint uniqueness not proved. Instead consolidated a verified emergent structural no-go for its two-weight phase mechanism: proved parity obstruction (O2) for rotation-symmetric pairs, polynomial Fourier-reality lemma (O1), Cayley singular-weight escape, plus certified geometry/chord-cone and sign tables; replay EMERGENT_VERIFY_ALL_OK.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Re-ran inputs/artifacts/emergent_verify.py -> EMERGENT_VERIFY_ALL_OK; numerics for V1-V6 replay. Independent algebra confirms: O1 polynomial reality lemma is correct (P(z)-conj(P)(1/z) Laurent argument: z^N*H(z) polynomial vanishing on arc => identically zero, so c_{n>=1}=0; bound <=2N and 4 zeros for z^2/2 correct). O2(a) identity dn(psi_-)(+-i)=0 for real-coeff symmetric pair is correct (odd-only sum => zR'(z) purely imaginary at +-i). O2(b) antipodal equality dn(psi_+)(w)=dn(psi_+)(-w) is correct (even-only sum). BUT Theorem O2 headline inference '(b) hence cannot satisfy two-sided sign pattern (negative on both Gamma_D,Gamma_N, positive on both overlap gaps)' is FALSE. Counterexample within the admitted class: Phi_D(z)=-z^2/2 (real coeffs), Phi_N(z)=Phi_D(-z)=-z^2/2. Then psi_+=Re(-z^2), dn_+=Re(-2z^2). On Gamma_D (|theta|<pi/4): cos2theta>0 => dn<0 (e.g. -2 at 0). On Gamma_N (|theta-pi|<pi/4): same => dn<0 (-2 at pi). On gap interiors (pi/4,3pi/4) and (-3pi/4,-pi/4): cos2theta<0 => dn>0 (+2 at +-i). So antipodal equality is COMPATIBLE with the stated pattern; it does not preclude it. The true parity obstruction is for the odd difference weight (antipodally opposite, zero at +-i prevents strict positivity on gaps), not for the even sum weight. Hence 'no rotation-symmetric real pair can supply simultaneous two-sided Carleman control' is unproved; no Carleman estimate is proved linking psi_+/psi_- to control (DRAFT Sec.6 admits none). Proposition E overstates necessity: Cayley Phi=i(1+z)/(1-z) correctly verified real on circle minus pole with min|Phi'|>=0.5, but exhibit of one singular example does not prove 'achievable ONLY with a boundary pole'; general-holomorphic necessity is explicitly conjectured, not proved. Verifiers check identities, not the control-preclusion claim. Essential inference therefore fails. originality: EMERGENT_FINDING genuineness passes: logs show it arose from target audit step 2 diagnostics (single-weight success, sum/difference failure, parity/DFT checks), not a pre-planned substitute. But ordinary originality standard fails. O1 (no nonconstant polynomial real on positive-length arc) is a textbook exercise: finite Laurent polynomial H(z)=P(z)-overline{P}(1/z) vanishing on arc => identically zero; standard F.&M. Riesz / identity-theorem / Schwarz-reflection corollary (cf. Rudin RCA Ch.17). O2 equalities/zeros are one-line odd/even parity algebra, mechanically implied by the ansatz Phi_N(z)=Phi_D(-z) with real c_n, not a substantive gap. Cayley witness is the classical Cayley/Mobius map. Geometry (separation sqrt(2), K_D union/overlap 1/2, chord cone within pi/4 of horizontal, threshold 1/sqrt(2)) is elementary disk trigonometry. Admission triage (GT 0908.1417 single colocated weight; Daude-Kamran-Nicoleau 1510.06559/1701.09056 anisotropic disjoint; IUY 0809.3037 overlapping coverage; fractional 1609.09248 nonlocal) correctly shows no prior states this exact paired obstruction, but absence of the composite…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: ['O1 proved for polynomials only; general holomorphic H^p extension is a conjecture.', 'O2 covers rotation-symmetric real-coefficient pairs, not all asymmetric pairs.', 'No Carleman estimate, CGO existence, chord-transform injectivity, potential uniqueness, or f* obstruction witness is claimed.', 'Prior comparisons rest on admission triage, not new full-text survey.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
