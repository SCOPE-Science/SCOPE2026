# Self-review

## Correctness — PASS

The exact weak-order count \(T=1+2S+(S^2-Q)/2\) is an established finite-base identity. Conditioning iid block sizes of law \(\rho^k/k!\) on a renewal hit at the integer \(n\) reproduces the uniform labelled ordered-partition distribution. The reward moments are \(\mathbb EK=2\rho\), \(\mathbb EB=2\), \(\mathbb EY^2=2/\rho\), giving the standardized Gaussian variance coefficient \(1/\rho^2\). A direct dominant-pole residue proof establishes the conditional lattice limit without a positive moment generating function; fixed-order formal derivatives supply the fourth moment and \(Q\) estimates needed for \(\operatorname{Var}(T_n)\sim n^3/\rho^4\). The standalone checker independently matches 127 direct type diagrams and exact integer moment recurrences through 200. Finite checks corroborate the analytic proof, not replace it.

## Originality — PASS (provisional historical priority)

The closest indexed full text, *Quadratic average one-point type growth over random finite weak orders* (2026), determines the mean and states explicitly that it establishes no concentration, variance or limiting law. Its exact formula and mean are prerequisites, not new claims here. Dolinka and Mašulović give the general ideal/filter description, Elder et al. give the related ordinal-sum interval-closed-set enumeration, and Patch–Nazarathy–Taimre address generic renewal-reward asymptotics with different hypotheses. The current claim concerns a conditional lattice-renewal Gaussian limit and sharp \(n^3\) variance constant for a concrete model-theoretic type count. Equivalent earlier renewal specializations remain a priority risk.

## Mathematical value — PASS

The earlier exact average provides no typical-case spread or probability law. The new theorem quantifies fluctuations, proves concentration around the quadratic law, and identifies a nonzero sharp variance constant. It also isolates a probabilistic subtlety: the exponential block reward has no positive exponential moments, so generic analytic quasi-power arguments are not automatically valid. This is a motivated extension of the random-structure type-count problem, not a renamed expectation calculation.

## Scientific limits

The result is for uniformly labelled weak orders, individually named generic-poset types, and large \(n\); it asserts neither concentration speed nor a result for all finite posets. No independent audit or complete historical priority determination has been performed.

Self-review: passed. Independent audit: not yet performed.
