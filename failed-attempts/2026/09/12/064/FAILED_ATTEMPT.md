# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Gross-Zagier ratio check for 15a1 over Q(sqrt(-23))
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1212
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Gross-Zagier and Heegner-point heights
- **Method:** root number plus modular-symbols L-value and certified height interval

## Problem

Let E/Q be the elliptic curve 15a1 given by y^2+xy+y=x^3+x^2-10x-10 of conductor 15=3*5, let K=Q(sqrt(-23)) of discriminant -23, and let p=13. Preliminary gate (failure is NO_RESULT, not disproof): verify good ordinarity at 13, the splitting behaviors (3 split, 5 inert, 13 split) in K, and mod-13 irreducibility. Decided claim (single certified complex-analytic identity, no tower layers): compute the global root number w(E/K), let r=(1-w)/2, compute the Tamagawa-and-period-corrected Gross-Zagier predicted exact rational ratio R for L^{(r)}(E/K,1)/h_hat(P) where P is the explicit conductor-1 Heegner point (located by in-hour point search), and decide with rigorous interval bounds (modular-symbols L-value plus certified height computation, conductor 15*23^2=7935) whether the certified interval contains R or provably excludes it. A complete answer confirms the identity with the analytic-rank certificate, or refutes it with a documented deviation interval constituting a new obstruction with explicit witnesses.

## Attempted claim

Let E/Q be the elliptic curve 15a1 given by y^2+xy+y=x^3+x^2-10x-10 of conductor 15=3*5, let K=Q(sqrt(-23)) of discriminant -23, and let p=13. Preliminary gate (failure is NO_RESULT, not disproof): verify good ordinarity at 13, the splitting behaviors (3 split, 5 inert, 13 split) in K, and mod-13 irreducibility. Decided claim (single certified complex-analytic identity, no tower layers): compute the global root number w(E/K), let r=(1-w)/2, compute the Tamagawa-and-period-corrected Gross-Zagier predicted exact rational ratio R for L^{(r)}(E/K,1)/h_hat(P) where P is the explicit conductor-1 Heegner point (located by in-hour point search), and decide with rigorous interval bounds (modular-symbols L-value plus certified height computation, conductor 15*23^2=7935) whether the certified interval contains R or provably excludes it. A complete answer confirms the identity with the analytic-rank certificate, or refutes it with a documented deviation interval constituting a new obstruction with explicit witnesses.

## Research outcome

Proved Heegner-hypothesis obstruction for (15a1, Q(sqrt(-23))): gate passes, w=+1/r=0, and inert 5 rules out any norm-15 ideal, so no classical conductor-1 X0(15) Heegner point exists.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Essential gate arithmetic (a13=-2 ordinary, splitting 3 split/5 inert/13 split, Frob_2 discriminant 6 non-residue mod 13, c4=481, Delta=3^4*5^4) and the ideal-norm impossibility (inert 5 forces even 5-adic valuation, hence no norm-15 ideal and no conductor-1 X0(15) datum) plus root number w(E/K)=+1/r=0 were independently recomputed and are sound. However claim clause (i) as written asserts 'split I1 at 5' derived 'from c4=481 and Delta=3^4*5^4'; with v5(Delta)=4 and v5(c4)=0 the minimal model has Kodaira type split I4 at 5, not I1. The I4/I1 description of LMFDB 15.a1 (disc 405) was conflated with the stated equation (disc 50625). This is a concrete false sub-claim, so correctness FAILS as stated even though the central obstruction logic is sound and fixable by I1->I4. originality: Fused retrieval (SerpBase/Serpent/OpenAlex/Crossref/OpenAIRE, 20 results, no partial failure) finds only the general Heegner-hypothesis/Gross-Zagier literature and LMFDB data, with no prior publication of this exact triple instance. Nevertheless the finding is mechanically implied by that prior work: the classical Heegner hypothesis (every prime dividing N splits in K) directly implies no conductor-1 X0(15) datum when Kronecker(-23,5)=-1, and root-number/a_p/local-type facts are standard formulas and database entries. A timestamp plus absence of a literal-title hit does not establish priority; substantive implication by the general theorem defeats originality. Hence originality FAILS. value: ADMISSION_DEFECT: the admitted TARGET presupposed a classical conductor-1 X0(15) Heegner point for N=15 over discriminant -23, but 5 inert violates the Heegner hypothesis prerequisite that Admission should have checked via one Kronecker symbol. The emergent finding therefore exposes only a cheap admissibility/type defect (Heegner-hypothesis failure plus parity r=0 degenerating the ratio), i.e. an arbitrary-parameter fact for one ill-posed triple, not a new theorem, boundary change, benchmark, or reusable lemma. Each numeric piece is a textbook exercise or direct database lookup, and the narrow datum is mechanically implied rather than an unknown invariant a future researcher would need. Hence value FAILS under the shared STANDARD.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: No rigorous modular-symbols L-interval or certified height interval is provided, so this is not a completed TARGET containment/exclusion and not a full Gross-Zagier disproof: a generalized Heegner construction on a Shimura curve (outside the admitted classical X0(15) conductor-1 claim) is not excluded, and analytic rank 0 over K is supported by parity plus heuristic L-values but not by a certified rank proof here. The K-grid search bound (|coords|<=6) is illustrative only; the no-datum proof re…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
