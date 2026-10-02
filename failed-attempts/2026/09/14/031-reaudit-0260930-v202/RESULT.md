# Finite-scale Kesten-window stability on the 8x8 square

## Context

Near-critical planar percolation studies how crossing probabilities stay bounded
away from 0 and 1 inside the scaling window around p = 1/2. The admitted target
asks for a complete resolution on the finite 8x8 box: either a rigorous proof or a
rigorous disproof that the left-right crossing probability stays in [1/4, 3/4]
uniformly over |p - 1/2| <= 0.005. Qualitative Russo-Seymour-Welsh theory predicts
stability but does not instantiate exact endpoint values at this scale.

## Definitions

Bernoulli bond percolation on the vertex box V = [0,8] x [0,8] intersect Z^2 (81
vertices, E = 2*8*9 = 144 edges): each edge is open independently with
probability p; P_p denotes the product law. Cross(V) is the event that an open
path joins the left side {0} x [0,8] to the right side {8} x [0,8]. Cross(V) is an
increasing event. Write T = 200^144.

## Result

TRUE: for every p with |p - 1/2| <= 0.005,

1/4 <= P_p(Cross(V)) <= 3/4.

In fact the exact endpoint values are

P_0.495(Cross) = C(99,101)/T approx 0.5340384035,
P_0.505(Cross) = C(101,99)/T approx 0.5823560330,

and monotonicity extends these endpoint bounds to the whole window with margins
approx 0.28 below 1/4 and approx 0.17 above 3/4.

## Proof / Evidence

Monotonicity of the increasing crossing event under the standard coupling gives
P_0.495 <= P_p <= P_0.505 over [0.495, 0.505], reducing the claim to the two
rational inequalities P_0.495 >= 1/4 and P_0.505 <= 3/4.

Both endpoint probabilities were computed exactly as integer ratios by a
transfer-matrix dynamic program over frontier connectivity partitions with
left/right touch flags (output/artifacts/dp_engine.py, integer arithmetic only).
Exact certificates: 4*C(99,101) - T is a positive 332-digit integer and
3*T - 4*C(101,99) is a positive 332-digit integer, with conservation checksum
crossed + uncrossed == T holding exactly in both runs. Validation: digit-for-digit
brute-force agreement on n = 1, 2, 3 grids at multiple weights, independent
column-major edge-order reruns reproducing numerators, Monte Carlo consistency,
and the exact checker output/artifacts/verify_endpoints.py returning PASS. The
auditor independently reran small-n DP-vs-brute checks and reproduced both n=8
endpoint integers and certificates.

## Limitations

The proof is computer-assisted: the two 332-digit endpoint integers are produced
by an exact machine-executed dynamic program (minutes per run, at most 26333
live states) rather than a closed-form estimate. Trust rests on the short
self-contained integer-arithmetic code plus conservation, brute-force, and
order-independence checks.

## Reproducibility

python3 output/artifacts/dp_engine.py --n 8 --a 99 --b 101
python3 output/artifacts/dp_engine.py --n 8 --a 101 --b 99
python3 output/artifacts/verify_endpoints.py

Small-n cross-checks: add --brute for n <= 3, or --order col for the
reordering check.

## References

- Borgs, Chayes, Kesten, Spencer, finite-size scaling in percolation (scaling-window theory; no n=8 exact table).
- Nolin, Near-critical percolation in two dimensions, EJP 13 (2008) (Kesten scaling relations; no n=8 exact values).
- Standard monotone coupling / Harris inequality for increasing events.
