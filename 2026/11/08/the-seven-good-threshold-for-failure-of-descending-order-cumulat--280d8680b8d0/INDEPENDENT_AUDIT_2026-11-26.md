# Independent mathematical audit

## correctness

PASS

Agent interchange fixes the first sign, and the greedy absolute discrepancy obeys d_t=|d_{t−1}−w_t| including ties. If w₁=0 every cost is zero; otherwise positive homogeneity fixes w₁=1. Each feasible choice of greedy branch signs correctly gives the absolute discrepancies, and such branches cover the entire ordered nonnegative cone, including its faces. For a competitor, the epigraph cost is equal to its actual cost at y_t=|S_t|, which is a feasible choice. Thus the dual identity F=−zᵀAx+ηw₁ with z,η≥0 proves the desired pointwise inequality. Independent exact evaluation of both linear forms on each basis vector verified all 1364 distinct branch and competitor pairs for m=2,…,6, checking the signs and full coverage. The one-good case is immediate. An independent dynamic program over current absolute discrepancy (next state d+w or |d−w|) computes optimum 18 and greedy 20 at (6,5,5,4,4,1,1). Appending zeros preserves the strict failure at longer horizons.

## originality

PASS

The objective, rule and general fixed-order optimization precede this finding. No inspected prior statement determines the universal short-horizon cutoff for arbitrary nonnegative real values in a fixed descending order. The strong reported overlaps concern other value alphabets, order models, or objectives.

## value

PASS

Least-loaded allocation is a natural baseline, and restricting arrivals to a fixed descending order is a common scheduling regime, not a choice of isolated input values. The theorem specifies exactly when myopic decisions can cease to be uniformly optimal against a planner with foreknowledge, including a small reproducible witness. The exact dual method proves a real-valued uniform result rather than an empirical threshold over integer inputs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
