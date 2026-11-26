# Independent mathematical audit

## correctness

PASS

At each strict turn in a walk on the full two-sided second-power line, the neighboring vertices are either equal or at label distance one. Delete the loop or take the direct edge; within [a,2a] this never raises cost and strictly decreases the number of edges. A turn-free walk between distinct endpoints is monotone, and there are finitely many monotone candidates. The sharpness example with only {0,2} and {1,2} of weight a gives a path costing 2a between 0 and 1, whereas the sole monotone path costs b>2a. A minimum also exists in this example, since any path at cost ≤2a has at most two edges. Monotonicity gives the two-predecessor recursion, with both newly used incoming edges independent of the past. Subtracting D_(n−1) gives the four-state increment Markov chain. It is irreducible for 0<p<1 and state 1 has a holding probability 1−p. The ergodic theorem and bounded increments yield the a.s. and L² drift limits. For g=f−μ and h−Ph=g, M_n=Σ_(j=2)^n[h(X_j)−Ph(X_(j−1))] differs from Σ_(j=1)^n g(X_j) by the bounded term h(X_1)−Ph(X_n). Its conditional variance per step is P(h²)−(Ph)² evaluated at X_(j−1), so the ergodic theorem, boundedness and the martingale CLT give the asserted Gaussian limit with variance π(h²)−π((Ph)²)=2π(gh)−π(g²). Expectations of the bracket give Var(M_n)/n→σ², and the bounded boundary term changes this by o(1), even from the initial law of the first edge. Independent exact algebra replay: `python3 /workspace/branches/5ce4285f-24ec-4e0e-ba33-2dca88c314a2/independent_symbolic_check.py` (SymPy), PASS for transition, stationarity, drift, Poisson equation, variance, fair values and H(1−r) identity. Grouping 9r²−3r³ and 22r⁴−7r⁵ gives strict positivity on 0≤r≤1. The uploaded script was read, not run; the bounded algebra check does not itself prove the probability theorems or general geometry. At degenerate probabilities the passage time is the constant edge weight times ceil(n/2). No uniform stochastic claim near the endpoints or monotonicity of every minimizing path at ratio 2 is established.

## originality

PASS

Pass the explicit exact drift and fluctuation variance for the binary law on this graph and the sharp deterministic monotone-minimizer criterion. General regeneration LLN/CLT, the factor-two support distinction, and Markov-chain variance methodology are prior and not credited. The best-matching primary theory represents the same limiting constants implicitly; it does not evaluate them as these rational functions. The backward-step observable and open backtracking questions inspected there do not give the deterministic existence-and-sharpness statement. The strongest indexed exact hit is the assigned record itself, not separate coverage.

## value

PASS

The simplest full two-step line already permits backtracking and is a natural test of spread-out first-passage geometry. The sharp boundary explains exactly when the deterministic path minimization can be replaced universally by a forward recursion, and the resulting constants quantify drift and fluctuation size across the whole nondegenerate binary family rather than one chosen probability. These provide explicit comparisons for models where general theory gives only implicit constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
