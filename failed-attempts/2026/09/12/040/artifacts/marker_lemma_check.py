"""Bounded certificate for marker-necessity lemma + rate-tax arithmetic + Shannon-route check."""
import json, math, random
from collections import Counter
from itertools import product

def delete_one(bits, pos):
    return bits[:pos] + bits[pos+1:]

# (A) Explicit confusable pair, n=32, single fixed marker bit (last bit = 0).
data = [1]*30 + [0]
seg = data + [0]
outA = delete_one(seg, 31)  # delete the marker itself
outB = delete_one(seg, 30)  # delete adjacent data bit (also 0)
assert outA == outB and len(outA) == 31
explicit_pair_ok = True

# Toy exhaustive: 3 data bits + 1 fixed marker bit 0; count data patterns where
# marker-deletion output coincides with some data-deletion output.
colliding_datas, total_datas, examples = 0, 0, []
for d in product([0, 1], [0, 1], [0, 1]):
    total_datas += 1
    s = list(d) + [0]
    marker_out = tuple(delete_one(s, 3))
    data_outs = {tuple(delete_one(s, p)) for p in range(3)}
    if marker_out in data_outs:
        colliding_datas += 1
        if len(examples) < 3:
            examples.append({"data": list(d), "shared_output": list(marker_out)})

# (B) Exact rate-tax arithmetic.
vt_overhead = math.log2(33)          # single-deletion packing overhead per 32-bit segment
marker_bits_per_seg = 2
per_seg = 32 - marker_bits_per_seg - vt_overhead
total_info = per_seg * 32
cap_bits = 0.78 * 1024
tax_points = 64 / 1024

# (C) Recovery test: uniform-input per-segment mutual info under random
# single-deletion model (E~Bern(1/2) delete-or-not, uniform position).
random.seed(0)
T = 20000
s = 0.0
for _ in range(T):
    x = [random.randrange(2) for _ in range(32)]
    c = Counter()
    for j in range(32):
        c[tuple(delete_one(x, j))] += 1
    s += -sum((v/32)*math.log2(v/32) for v in c.values())
mean_outcome_entropy = s/T
HYgX = 1.0 + 0.5*mean_outcome_entropy
HY_heuristic = 32.5
I_example = HY_heuristic - HYgX
shannon_ceiling = (I_example*32 - 32)/1024  # minus 1-bit/segment drift entropy

results = {
  "explicit_pair_collision": explicit_pair_ok,
  "toy_colliding_datas": colliding_datas,
  "toy_total_datas": total_datas,
  "toy_examples": examples,
  "vt_overhead_bits": vt_overhead,
  "per_segment_info_bits": per_seg,
  "total_info_bits": total_info,
  "cap_bits_078": cap_bits,
  "meets_078": bool(total_info <= cap_bits),
  "marker_tax_rate_points": tax_points,
  "mean_outcome_entropy": mean_outcome_entropy,
  "HYgX": HYgX,
  "uniform_input_I_example": I_example,
  "shannon_route_ceiling_heuristic": shannon_ceiling,
  "shannon_route_sufficient": bool(shannon_ceiling <= 0.78),
}
with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1145/output/artifacts/marker_lemma_results.json", "w") as f:
    json.dump(results, f, indent=2)
print(json.dumps(results, indent=2))
