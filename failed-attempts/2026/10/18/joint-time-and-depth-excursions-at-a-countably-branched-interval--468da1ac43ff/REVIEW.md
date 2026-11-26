# Independent mathematical audit

## correctness

PASS

The branch from V_i maps affinely onto (0,λ^(i−2)], so uniform conditional measure on a target cell persists after every specified itinerary. The cell increment is R−1 with P(R=r)=(1−λ)λ^r on r≥0. Put a=z(1−λ), c=aλ. Subtract λ times each next-state equation from the previous one to obtain f_i−λf_(i+1)=af_(i−1) below the top, and (1−c)f_(m−1)=af_(m−2) at the top. Starting there and working backwards to f_4=1 gives exactly H_m=aP_(m−6)/P_(m−5). Positivity follows from P_j=(r_+^(j+2)−r_-^(j+2))/(r_+−r_-), with r±=(1±√(1−4c))/2 and positive repeated-root limit. At m=6 this is the geometric one-state formula; z=0 gives zero. The skip-free first-hit sequences have total increment −1, so the cyclic lemma on weak compositions gives the Catalan coefficient and the square-root PGF. At z=1, the roots are λ and 1−λ (or repeated at 1/2), and 1−H_m(1) is exactly the stated height tail with exponent m−3. A finite strip is left almost surely by the positive-probability all-down run, so treating nonreturns as infinite height does not alter this computation. The unrestricted PGF at one gives the stated missing mass. For the duration scaling at λ=1/2±ε, Stirling gives prefactor 1/(2√π) and exponential factor (1−4ε²)^(n−1); the bound by a constant times n^(−3/2)e^(−4nε²) justifies the tail integral. The supercritical mass adds 4 after division by ε. q=1∓4ε+O(ε²) gives the two stated depth limits. The result is confined to the auxiliary map, with no transfer by semiconjugacy.

## originality

FAIL

The principal finite-ceiling joint transform is an exact recoding of the classical side-specific gambler's ruin duration transform. The geometric run representation gives an exact match of both observables and yields the stated continuant ratio by substitution. This is not merely overlap in the unbounded Catalan marginal or use of a similar recurrence. The known interval-map transition matrix already supplies the stopped chain; the separate crossover laws follow from its classical marginals. The decision rests on demonstrated equivalent coverage, not on the unavailable indexed excursion record.

## value

FAIL

Duration and maximum cell depth are well motivated, but the Bernoulli run representation turns the joint law into the classical finite-barrier ruin statistic with a deterministic clock change on returns. The given formula and separate near-critical limits add no independently unresolved invariant after this identification. The record deliberately claims no extension to original bimodal-map return times or a new joint critical limit beyond the finite transform and its marginal consequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
