# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Explicit distortion growth for SL_3 Cayley-quotient super-expanders into uniformly convex targets
- **Round:** 2026-09-07-first-light-01
- **Lane:** 376
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Functional Analysis
- **Method:** Markov-convexity and metric-cotype distortion inequalities with nonlinear spectral-gap bootstrapping

## Problem

Quantify super-expander distortion for one deterministic Cayley-quotient tower: fix generators S of SL_3(Z) and graphs G_m=Cay(SL_3(Z/mZ),S); for fixed p>2, prove an explicit distortion-growth lower bound c_{L^p}(G_m) >= c_p (log|G_m|)^{delta_p} via Markov p-convexity and nonlinear spectral-gap bootstrapping, or certify that the bound is tight via a bounded embedding/obstruction.

## Attempted claim

Let G_m=Cay(SL_3(Z/mZ),S) for a fixed finite generating set S, N_m=|G_m|. For each fixed p>2 there exist explicit c_p>0 and delta_p>0 such that any bi-Lipschitz embedding of G_m into L^p satisfies distortion c_{L^p}(G_m) >= c_p (log N_m)^{delta_p} for all large m, proved via a Markov p-convexity / nonlinear spectral-gap inequality chain that improves the known qualitative super-expander gap to an explicit rate.

## Research outcome

Certified fallback theorem: exact L^4 distortion 2^{1/4} of C_4 plus an isometric C_4 and girth-4 certificate in the Margulis level G_5=Cay(SL_3(F_5),S) yields c_{L^4}(G_5)>=2^{1/4}>=1.1892, with a rhombus sharpness witness showing the diamond constant is best possible and tower transfer to all levels m>=2. Fully replayed by stdlib verifier (VERIFY_OK). No growth exponent claimed.

## Why this attempt failed

Failed axes: value.

value: Strongest headline c_{L^4}(G5)>=2^{1/4} (girth 4) is correct and new as a sentence but not independently worth retrieving. Reasons: (1) Textbook restatement + parameter substitution: generic principle 'any graph containing isometric C4 has c_{L^4}>=2^{1/4}' (classical) applied to obvious commuting-transvection 4-cycle (Steinberg relation). Level m0=5 and N=372000 play no role; draft's own tower remark shows identical proof for every m>=2 (flat floor, not growth), so scope is arbitrary. (2) No quantitative boundary update: target was (log N)^delta_p growth; delivered uniform constant floor true of almost any non-tree graph, with no downstream use for coarse Novikov / Lipschitz extension / sparsification beyond what generic C4 principle already gives. Draft honestly admits no growth proved and Holder L2->Lp route blocked. (3) Fallback substance missing: delivered 'sharpness' is sharpness of single-C4 method (rhombus), not certified sharpness of Markov-p-convexity constant for the family; delivered 'transferable lemma' is trivial restriction, not a nonlinear-gap/Markov-convexity lemma with certified constants. (4) Exact-invariant clause does not save: although G5 is natural and distortion motivated, the value 2^{1/4} IS mechanically implied by textbook pieces, and a future researcher needing this bound would cite the general C4 principle plus commuting pair, not retrieve this level-specific record. Girth=4 is an auxiliary unenpowered enumeration (1728-triple check) whose upper bound is the same obvious 4-cycle; certification (VERIFY_OK) alone does not rescue generic number per standard. (5) Not repairable by bounded addition: turning flat C4 floor into growth rate or genuine nonlinear-gap lemma needs certified 372k-vertex spectral gap + Mendel-Naor/Banach-(T) constants - new research direction, not prose/motivation fix. Hence intrinsic low value / arbitrary scope / missing substantive result -> REJECT.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Proves only a uniform constant floor c>=2^{1/4}, NOT the target asymptotic (log N)^{delta_p} growth rate; the nonlinear spectral-gap/Markov-convexity chain is documented as blocked (naive L2->Lp Hoelder goes the wrong way; Mendel-Naor/Banach-(T) constants plus a certified gap of the 372000-vertex graph are out of scope). The L^4 diamond inequality and rhombus extremal are classical uniform convexity (Clarkson/Enflo); originality is claimed only for the certified tower-level instance, girth cert…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
