# Independent mathematical audit

## correctness

PASS

The OU variance at age t is v_lambda=1-(1-q)e^(-lambda t). Gaussian Jeffreys divergence per coordinate is (v_lambda-q)^2/(2q v_lambda); the coordinates add conditional on the common cycle age. The renewal-reward normalization is multiplication by r for both clocks, not averaging time-stationary ages. After rescaling age, the rate difference divided by r is h_q(r)+h_q(r/K). The scalar reward has coefficient A=(1-q)^2/(2q^2)>0 at t^2. The exponential second moment is twice the deterministic square, yielding h_q(z)=A/z^2+O(z^-3); the bounded reward controls the tail in this expansion. At small z, subtract the exponentially approached equilibrium reward under the integral. Its integrated deficit is B=(1-q)/(2q)+(q/2)log q>0 (strict positivity also follows from v increasing from q to 1 and Jeffreys divergence increasing with v on this range). The deterministic deficit is O(exp(-1/z)), so h_q(z)=-Bz+o(z). Choose a<b with signs negative and positive. At a and b the fast-mode contribution vanishes as K tends to infinity, at sqrt(K) the negative term -B/sqrt(K) dominates the positive O(1/K), and at Kb the slow-mode contribution vanishes. The four increasing frequencies have strict signs for all sufficiently large K. On r>0 the difference is real analytic (Laplace transform of a bounded reward and analytic deterministic term), so the opposite signs in each disjoint bracket force genuine sign changes, not an interval of zeros. Independent exact-rational replay: python3 /workspace/checks/gaussian_signs.py. It expands the reward as (1-u)^2/4 times a geometric series in u/2, bounds the positive expectation tail and range-reduces alternating exponential bounds. Exact comparisons verify even the four quoted decimal intervals, with approximate centers -0.025869275301, +0.003482470973, -0.009486608021, +0.002579438354. These are normalized by r. Neither a full crossing count nor a total physical dissipation law follows.

## originality

PASS

The evidenced result is the synchronized two-rate sign alternation, not the scalar conditional KL construction, renewal-reward formula, or single-mode reversal. No distinct dominating claim appeared in the compared statements.

## value

PASS

Two relaxation scales under a common reset clock suffice to invalidate a natural generalization of one-scale uniqueness. The counterexample is structural for every nontrivial fixed reset width at sufficient separation, with an explicit finite witness; it is not the mere recomputation of one numerical preference. Its relevance is to a specified conditional endpoint benchmark, not to choosing an actuator protocol for total entropy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
