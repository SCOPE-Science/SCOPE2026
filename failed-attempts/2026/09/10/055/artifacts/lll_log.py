"""Route B: quantitative symmetric-LLL log for 3-coloring the degree-5 cell.
Stdlib only. Writes lll_log.json."""
import json
import math

# Random uniform 3-coloring; bad event per edge E_e = "e monochromatic".
p = 1.0 / 3.0
# Each edge shares a vertex with at most 2*(5-1) = 8 other edges.
d = 8
criterion = math.e * p * (d + 1)
# Colours needed for naive uniform-k LLL to pass: e*(1/k)*(d+1) <= 1
k_needed = math.e * (d + 1)

# Asymmetric sanity: non-uniform (q,q,1-2q) edge-bad prob q^2+q^2+(1-2q)^2,
# minimized at q=1/3 -> 1/3. So no distribution helps the symmetric criterion.
best = min(q * q + q * q + (1 - 2 * q) ** 2 for q in (i / 100 for i in range(1, 50)))

out = {
    'p_edge_bad': p,
    'dependency_degree': d,
    'symmetric_LLL_value_e_p_dplus1': criterion,
    'passes': criterion <= 1.0,
    'uniform_colours_needed_for_LLL': k_needed,
    'best_nonuniform_edge_bad_prob': best,
    'conclusion': ('symmetric LLL FAILS for 3 colours at degree 5 '
                   '(8.15 >> 1); uniform LLL would need >=25 colours'),
}
with open('lll_log.json', 'w') as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
