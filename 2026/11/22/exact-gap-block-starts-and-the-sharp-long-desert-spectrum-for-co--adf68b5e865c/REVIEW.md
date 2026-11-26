# Independent mathematical audit

## correctness

PASS

The original start/count formulas check out but were removed for prior coverage. For the repaired long-block theorem set u=n+1, v=2u+1. In a fixed-q layer the j-th subprogression has step u; the next lower endpoint is at most u+1 above the previous upper endpoint, and the new upper endpoint increases by u+1. Thus successive represented points in the layer are at most u+1 apart, including overlapping progressions. A gap intersecting any layer span cannot cross either represented endpoint, so every gap longer than u lies between successive spans, whose endpoints increase with q. Each nonempty uncovered interval is genuinely missing and bounded by represented endpoints. Its length is a−1−qv. With u=4K+r, 0≤r≤3, subtracting u at q=K−1 and q=K gives u(r+1)/2−K>0 and u(r−3)/2−K−1<0 respectively, including n=3. Independent Dijkstra enumeration in /workspace/branches/4cdad8b1-ae1d-4725-b6d0-ae7385fe4857/independent_enumeration.py matched the original 583156 starts and all 1800 long intervals for n=3..120; separate reachability cross-checked full blocks at n=3..28. The repaired checker /workspace/repairs/4/verify.py ran successfully (n=3..40, 200 long blocks). The frozen script was inspected, not executed; finite reproduction does not prove the uniform formula.

## originality

PASS

PASS applies only to the repaired exact spectrum above n+1. The original all-start formula and parity count fail originality: the prior exact-family isolated-gap proof already evaluates the left-neighbor bound in every Apéry cell. Dropping the right-neighbor requirement recovers the starts immediately. For w(y,z)−ta with t≥1, the prior left bound is B−1 at y=A−2,A−1 for each z=1..d−1, and is otherwise nonpositive (including z=0). Thus it gives exactly 2(d−1)(B−1) starts, the original parity count, as well as every lift in the original formula by taking y=(j_r−2) mod A and z=ell+1. This is prior-coverage evidence even though the prior theorem advertises singleton gaps. That calculation does not compare long stretches between consecutive represented points; the repaired result establishes an exact cutoff and exhaustion via coin-count layers.

## value

PASS

The repaired claim gives a sharp cutoff at the natural generator spacing b−a. It classifies every exceptionally long void, not merely a family of large examples, gives their positions and all their distinct lengths without scanning through the conductor, and distinguishes inter-layer gaps from all gaps within one coin-count span. This geometric consequence is useful apart from the removed start census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
