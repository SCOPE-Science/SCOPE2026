# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Above the overlap-free ceiling: an automatic witness or tightened bound for the 7/3-power-free linear growth constant
- **Round:** 2026-09-07-first-light-01
- **Lane:** 164
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Combinatorics on Words
- **Method:** special-factor growth-constant analysis with automatic-sequence decision certificates

## Problem

Let C(7/3) = sup over all infinite binary 7/3-power-free words u of limsup p_u(n)/n. Published: C(2+) = 7/2 (twisted Thue-Morse), Thue-Morse constant 10/3, C(7/3) <= 4, and no maximum-complexity word exists (open Question 18). Decide the gap from one side within one hour: either exhibit an explicit binary 7/3-power-free automatic witness word w (morphism fixed point / DFAO from a bounded mu-perturbation search) with certified limsup p_w(n)/n > 7/2, or prove a tightened structural ceiling C(7/3) <= 4 - delta for explicit delta > 0.

## Attempted claim

An explicit infinite binary 7/3-power-free automatic word w, given by archived morphism/DFAO tables and a replayable Walnut 7/3-power-freeness certificate, whose factor complexity satisfies limsup_{n -> infinity} p_w(n)/n >= 7/2 + epsilon for an explicit stated epsilon > 0 (threshold at least 3.6), proved via its exact special-factor first-difference D(n) linear representation - thereby raising the known lower bound on the maximum linear growth constant C(7/3) strictly above the overlap-free ceiling.

## Research outcome

Bounded-slice census plus finite strict-word certificate on the 7/3-free growth-constant gap (Shallit-Shur Open Question 18): (1) exhaustive enumeration of 43,688 binary uniform morphisms (m<=8), 7,812 non-uniform morphisms (|h|<=6), and all 32+2,916 2-/3-state binary DFAOs shows every 7/3-power-free word in these families is overlap-free (0 strict; two complexity classes p(40)/40 in {3.1,3.3}); (2) exhaustive classification of shortest strict words (none of length <=8; exactly 4 at length 9, all period-4 overlaps of exponent 9/4); (3) a certified length-1500 strict 7/3-free word with exact factor counts attaining p(n)/n up to 3.44 (n=25), above the Thue-Morse constant 10/3 at 12 tabulated n. Honestly scoped: finite/slice results only; no infinite-word limsup bound on C(7/3) is claimed.

## Why this attempt failed

Failed axes: correctness, value.

correctness: Strongest combined headline claims (a) zero strict infinite words in bounded morphism/DFAO slices, (b) shortest-strict classification to L=12, (c) length-1500 strict word with exact p(n) table. (b) and finite-word parts of (c) verify: independent stdlib exhaustive scan confirms the 1500-letter file is 7/3-free (all periods, all starts) with overlap witness at (pos 0, period 4, factor 001100110); independent brute force over all 2^L words for L<=12 reproduces 0 for L<=8, exactly 4 at L=9 (001100110, 011001100, 100110011, 110011001), 4 at L=10, 8 at L=11, 4 at L=12, matching shortest_strict.json; naive set-enumeration for p(n) matches strict_p.json at all 14 sampled n (e.g. p(25)=86, p(24)=82, p(50)=168, p(100)=332, p(200)=662). However essential inference (a) is unsound as an infinite-word certificate: 7/3-freeness was tested only on capped prefixes (6000 letters for morphisms, 4000 for DFAOs) and overlap-freeness only for periods <=400 (census) / <=300 (DFAO), per DRAFT Sec 1 and Sec 3. A prefix test cannot certify an infinite fixed point / DFAO word is power-free (a power beyond the prefix or with period >400/300 would be missed; full check needs periods up to (n-1)/2 for prefixes and a Walnut/morphism-preservation proof for infinite words, explicitly absent per Sec 3). Hence 'no strict automatic word with <=3 states / within morphism bounds' is not proved. Presentation defects compound this: DRAFT Table lists p(200)=663 vs archived/naive 662; research_report.json says 'Length-1501' vs measured 1500; non-uniform census '7812 checked' disagrees with the stated bounds (|h| in 1..6 with h(0) 0-initial gives 63*126=7938). Honest scoping of finiteness does not cure the slice-completeness claim. value: Admitted headline target was limsup p_w(n)/n >=3.6 for an infinite 7/3-free automatic witness (raising C(7/3) above 7/2) or fallback (a) ceiling 4-delta for all infinite words or (b) exact infinite-word constant >10/3. None is delivered; DRAFT Sec 3 honestly concedes no witness above 7/2, no ceiling below 4, and that R3 finite ratios do not certify any infinite-word limsup. What remains is: (R1) a negative search over arbitrary state-count cutoffs (m<=8, |h|<=6, <=3 DFAO states) repackaged as a census -- arbitrary scope and a failed-search log, not the natural infinite class C(7/3); (R2) a 2^12 brute-force shortest-word list (search space 512 at L=9) with no motivated downstream use; (R3) exact p(n) of one lexicographic-DFS finite string of length 1500 -- an arbitrary object (seed+DFS tie-breaking) with unexplained numbers (e.g. p(25)/25=3.44) that cannot bound C(7/3) since finite-word ratios do not imply limsup. Per value standard, certification alone does not rescue an arbitrary object or unexplained enumeration, and a rigorously established datum must be of a motivated natural object with pre-computation motivation and plausible reuse. The DFS word and cutoff slices were the search route, not pre-motivated natural objects; the natural o…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: No witness above 7/2 and no ceiling below 4: the infinite-class supremum C(7/3) remains open. (R1) covers only bounded morphism/DFAO slices (4-state DFAOs randomly sampled, not certified). (R3) is a finite word, so its p(n)/n ratios do not certify an infinite-word limsup above 10/3 (fallback (b) not fully met). No Walnut certificate (offline); 7/3-freeness rests on archived prefixes plus replay script. Overlap scan bounded by period<=400 (census) / <=300 (DFAO).

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
