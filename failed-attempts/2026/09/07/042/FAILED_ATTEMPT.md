# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A checkable Bessel-bridge envelope for Legendre polynomials in the endpoint first lobe at moderate degree
- **Round:** 2026-09-07-first-light-01
- **Lane:** 81
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Approximation Theory
- **Method:** Sturm comparison and three-term recurrence inequalities with Hilb Bessel-bridge explicit remainder

## Problem

For Legendre polynomials P_n(x), x=cos(theta), 5<=n<=50, with N=n+1/2 and j01=2.4048255577 (first zero of J0), sharpen the textbook Bernstein envelope inside the endpoint first lobe 0<theta<=j01/N by proving an explicit Hilb/Bessel-bridge majorant that tracks the true J0-shaped descent, with all constants explicit and verifiable by three-term-recurrence computation plus a Sturm-comparison remainder estimate.

## Attempted claim

For 5<=n<=50, N=n+1/2, x=cos(theta) with 0<theta<=j01/N (first lobe), |P_n(x)| <= sqrt(theta/sin(theta)) * G(N*theta) + 0.025*theta^2 with G(z)=min(1, 1-z^2/8+0.004, sqrt(2/(pi*z))*(1-z^2/40)), j01=2.4048255577. On lobe interior (|P_n|>0.05) this cuts mean overestimation slack from ~1.71 (textbook min(1,sqrt(2/(pi*n*sin(theta))))) to ~1.49, median ~1.10 to ~1.06, P90 ~3.1 to ~2.6, max ~10.5 to ~6.7, with zero violations on a 2000-point/lobe verification grid (auditor-reproducible).

## Research outcome

Proved elementary J0 majorant G on [0,j01] (cap lemma + polynomial certificate for decay branch); conditional Hilb-bridge envelope for Legendre first lobe at 5<=n<=50 verified by reproducible recurrence grid with zero violations and ~13%/17%/38% mean/P90/max slack cuts vs textbook Bernstein; fallback 0.767 first-lobe constant certified. Remainder constant measured with headroom; full Sonin-ODE derivation left as explicit roadmap.

## Why this attempt failed

Failed axes: correctness, value.

correctness: Theorem A (G>=J0 on [0,j01]) is proved: Lemma 3.1 pairing argument verified (t<=j01^2/4<1.446<(2m)^2, so every pair -t^{2m-1}/((2m-1)!)^2+t^{2m}/((2m)!)^2<=0, hence J0<=1-z^2/4<=1-z^2/8; j01^2=5.783<8 confirmed); Lemma 3.2(i) alternating-series upper bound valid on [0.69,1.99] (t<=0.9901<1, ratios t/(k+1)^2<1 from k>=3, independently confirmed min p-J0>0); Lemma 3.2(ii) polynomial certificate numerically sound (independently recomputed r_min=0.02711 on 651-mesh and dense grid, max|r'|~0.78<claimed 12, b-binding interval [0.6985,1.9880] contained in [0.69,1.99] with zero outside, so coverage holds) modulo the acknowledged floating-point-not-interval mesh evaluation. BUT the headline target claim |Pn(cos theta)|<=S(theta)G(N theta)+0.025 theta^2 on the continuum first lobe for 5<=n<=50 is NOT proved: it is Corollary B conditional on Hypothesis H |R_n|<=0.025 theta^2, which is only measured on a grid with an explicit endpoint exclusion (t>=2.5e-4*tmax) plus an ODE/Sonin proof sketch the draft itself labels 'roadmap, not proof' and 'measured (+ODE-sketch), not proved line-by-line'. The between-grid Lipschitz guard by the draft's own numbers does not close the endpoint layer (mesh crossing 6.8e-7 >> endpoint min margin 9.0e-10; draft section 5.5 concedes this), and endpoint closure instead invokes the analytic floor 0.004-0.025 theta^2 which assumes H, making continuum promotion circular on the unproved hypothesis. Grid reproduction confirms the numbers (min E-|Pn|=9.04e-10 at z~6e-05, max|R|/theta^2=0.02132<=0.025, pooled slacks 1.4907/1.0588/2.6024/6.9434 vs textbook 1.7150/1.1047/3.1432/11.1738) but a 9e-10 grid minimum is evidence, not a continuum proof. The fallback 'certified' constant m_n^(1)<=0.767 is likewise a grid maximum (measured 0.76690), i.e. a lower bound on the true maximum promoted to an upper bound without a dedicated continuum guard. Hence proof vs experimental evidence: only G>=J0 and the conditional implication (H=>envelope, by triangle inequality) are proved; the unconditional envelope and constant are conjectures with numerical support. value: Even if H were proved, the result is not independently worth finding later: scope is a finite window (46 integers 5<=n<=50, first lobe only, no large-n/interior/Jacobi claim); gains are modest and partly tiny (pooled mean 1.7150->1.4907 ~13%, median 1.1047->1.0588 ~4%, P90 ~17%, max ~38%; fallback constant sqrt(2/pi)=0.7979->0.767 ~3.9% on the first lobe) of the kind the value bar rejects as epsilon improvements; the proved fragment in isolation (elementary J0 cap 1-z^2/8 and truncated-decay polynomial certificate) is a textbook-level Bessel exercise, not a Legendre advance; the reusable assets are finite grid tables (slack_table.csv, M_n/m_n^(1) maxima) without continuum certificates, i.e. unexplained enumerations with fitted fudge constants (0.004, 1/40, 0.025) rather than a general theorem. Conditional status further destroys certificate reusability for quadrature/spectra…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Hilb 0.025t^2 remainder measured+sketched (Sonin/Sturm ODE roadmap), not proved line-by-line -- Corollary B is conditional; b>=J0 polynomial certificate uses explicit-Lipschitz mesh argument, not interval arithmetic; scope limited to n=5..50 first lobe; n+1/2 shift and Bernstein sharpness are classical, not claimed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
