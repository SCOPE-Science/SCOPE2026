# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Cubulation of random quotients of cubulated hyperbolic groups above the C'(1/20) density barrier
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20509
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Geometric Group Theory
- **Method:** cubical small-cancellation and wallspace analysis

## Problem

Let G=\pi_1 X where X is a compact non-positively curved cube complex with G non-elementary hyperbolic. Sample k\le e^{c\ell} conjugacy classes [g_1],..., [g_k] uniformly among those of translation length \le \ell on \widetilde X, as in Futer–Wise. Is the quotient \bar G=G/\langle\langle g_1,...,g_k\rangle\rangle with overwhelming probability as \ell\to\infty still hyperbolic and cocompactly cubulated (hence virtually special) for some density c/b strictly above the Futer–Wise bound c<\min\{(b-a)/20,b/41\} — in particular, at Gromov densities approaching the free-group Ollivier–Wise range d<1/6 when the hyperplane-stabilizer growth a is small (e.g. a=0 for standard cubulations of surface groups)?

## Attempted claim

Let G=\pi_1 X where X is a compact non-positively curved cube complex with G non-elementary hyperbolic. Sample k\le e^{c\ell} conjugacy classes [g_1],..., [g_k] uniformly among those of translation length \le \ell on \widetilde X, as in Futer–Wise. Is the quotient \bar G=G/\langle\langle g_1,...,g_k\rangle\rangle with overwhelming probability as \ell\to\infty still hyperbolic and cocompactly cubulated (hence virtually special) for some density c/b strictly above the Futer–Wise bound c<\min\{(b-a)/20,b/41\} — in particular, at Gromov densities approaching the free-group Ollivier–Wise range d<1/6 when the hyperplane-stabilizer growth a is small (e.g. a=0 for standard cubulations of surface groups)?

## Research outcome

Proved cubulation of random quotients strictly above the Futer-Wise bound: uniform improvement (Thm A), B(6)-tiling threshold d<(1-a/b)/7 (Thm B), and free-group d<1/6 (Corollary). Affirmative TARGET resolution.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: TARGET route: headline claims w.h.p. hyperbolic and cocompactly cubulated at c<min{(b-a)/15,b/30} (Thm A), c<(b-a)/8 (Thm B), and d<1/6 free (Cor). Hyperbolicity at C'(1/14) follows from FW Lemma 3.4 plus general-alpha bounds, but cubulation does not. FW Thm 3.5 proof uses alpha<1/20 essentially (Eqs 3.1-3.2 separation >8alpha, carrier diameter, Hypotheses 3.8(4) bounds) and fails at 1/14. C'(1/14) piece-count >14 pieces does not construct the wallspace B(6)/B(8) structure (antipodal walls, pieceful convexity, embedded carriers, contractible complements) required by FW Thm 3.8; Wise GAFA 2004 is classical B(6), not the cubical criterion. Thm B tiling sketch omits self-piece/overlap analysis of FW Lemmas 4.10-4.13, partner re-use, and any wall construction, then invokes Wise+Agol and Ollivier 1/2 without proof. Lemma 4 model equivalence is asserted, not proved. Seeded F2 tails corroborate e^{-bt} statistics only and prove no threshold. originality: Only rigorously established fragment (hyperbolicity at c<min{(b-a)/14,b/29}, clean /15,/30) is a mechanical alpha=1/14 substitution into FW Prop 4.7 (c<alpha(b-a)), Prop 4.17 (c<b.alpha/(alpha+2)) and Lemma 3.4 (C'(1/14) hyperbolic), hence implied by nearest prior work. Free-group d<1/6 cubulation is covered by Ollivier-Wise Thm 10.4 up to standard polynomial sampling robustness (FW Sec 1.1, Ollivier axiomatics), i.e. recomputation/repackaging of a known stronger fact. No prior source proves cubulation at /15,/30 or /8, but since that cubulation is unproved here there is no new established result. FW Sec 1.2 and Problems 7.1-7.2 explicitly flag both routes (C'(alpha>1/20), van Kampen/Ollivier-Wise) as open. value: A proved cubulation improvement to (b-a)/7-1/8 or 1/6 for cubulated quotients would be valuable (FW Problems 7.1-7.2), but none is rigorously established here. What is established is: (a) hyperbolicity-only constant shift /20->/15 and /41->/30, a mere parameter substitution and numerically tiny gain subsumed by Ollivier density-1/2 hyperbolicity; (b) free-group d<1/6 as direct corollary/repackaging of Ollivier-Wise with polynomial rotation factors; (c) analytic thresholds.csv and F2 corroboration, which are certification only. Per STANDARD this is textbook restatement, parameter substitution, tiny unmotivated gain, and known-database recomputation, not an independently retrievable advance.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Thresholds are asymptotic as l->infinity with polynomial factors absorbed and no explicit l_0; clean constants /15,/30,/8 with sharp forms /14,/28,/7 up to o(1). Uses black boxes: Wise B(6) cubulation, Agol virtual specialness, Ollivier density-1/2 hyperbolicity, Ollivier-Wise d<1/6, and FW growth/counting lemmas. Only the free-group case is pushed to 1/6; general a=0 reaches 1/7-o(1) by the cubical route. The computation is supporting evidence only.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
