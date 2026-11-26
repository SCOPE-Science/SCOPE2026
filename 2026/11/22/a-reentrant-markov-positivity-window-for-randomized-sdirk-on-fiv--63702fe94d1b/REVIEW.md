# Independent mathematical audit

## correctness

PASS

I solved the stages with a common x and checked the full row update symbolically (`python3 /workspace/checks/sdirk_birth.py`, SymPy 1.14). With U=(I−hxB)^−1 the two stage operators are U and (I+h(1−2x)UB)U. The completed update is I+h(U+stage2)B/2; every entry matches, row sums are one, and the two relevant discriminants and −1/16 coefficient agree. The transient block has shift distance at most three and only its diagonal r_0 and the four-jump absorbing corner a_4 can be negative. For 0<h<1/3 the numerator 3−4x+hx(4x−1) strictly decreases in x and crosses exactly once between 3/4 and 1; from h=1/3 on it is nonnegative everywhere since at h=1/3 the sign is that of (x−1)(4x−9). The diagonal is nonnegative for h≤2. For h>2 its numerator is negative at x=1/2 and its larger root determines the successful upper interval, which collapses at 1+sqrt(3) to the singleton x=1 and is empty above it. This singleton is correctly assigned probability zero, although the short open-interval phrasing about nonemptiness in Proof Step 4 should be read with its following endpoint clarification. Uniform interval lengths give both nonconstant branches; at h=0 the update is the identity. Row lumping or the same transient calculation for n≤4 eliminates a_4, giving minimality in the stated family. The h^4 corner expansion is uniform on the parameter interval and integrating its leading coefficient gives −1/16, so expectation cannot restore stochasticity for all sufficiently small positive h. I inspected but did not run the frozen checker; exact stage algebra plus sign analysis, not binning, establishes the continuous law.

## originality

PASS

Qualified for the low-step absorbing-chain obstruction, its sharp probability and mean coefficient, and the complete noninterval safe set assembled with the already-covered high-step law. Neither the randomized method itself nor the high-step scalar sign criterion is credited as new.

## value

PASS

Stochasticity of a numerical transition matrix is a natural preservation property not guaranteed by scalar norm stability. With just five absorbing-birth states, almost half the draws fail at arbitrarily small positive steps, the ensemble mean also fails, yet a finite interval recovers stochasticity for every draw. The minimal dimension and complete probability law make this a usable test of positivity claims for stiff solvers. The scope is one step, this generator family and this parameter law, not nonlinear positivity or arbitrary Markov matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
