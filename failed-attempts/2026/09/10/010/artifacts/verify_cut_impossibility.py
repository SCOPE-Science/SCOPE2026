"""Cut-row ICT impossibility: finite combinatorial core.
Claim C: Let (b0,b1,b2) be order-indiscernible (monotonic or constant).
Then there are NO c0,c1,c2 in any linear extension with
  b_k < c_k <= b_i for all i != k   (singleton isolation for phi1:=(y<x)).
Proof by exhaustion over order-types of (b0,b1,b2).
Since conditions are order-theoretic, c_k can be taken in an interval
determined by the b's; we check all weak order types via integer reps.

Also shows: EACH b_k would have to be the unique strict minimum, impossible for 3.
"""
import itertools

def order_type_reps():
    # representatives of all weak total orders on 3 labeled elements using values 0,1,2
    reps = set()
    for t in itertools.product([0, 1, 2], repeat=3):
        # canonicalize by rank-preserving map to keep pattern of equalities/order
        # just keep all; dedupe by comparison matrix
        reps.add(t)
    return reps

def cmp(a, b):
    return (a > b) - (a < b)

def check_triple(b):
    """Return True iff separating c's exist (search over extended line).
    c_k must satisfy b_k < c_k and c_k <= min_{i!=k} b_i.
    Feasible iff b_k < min_{i!=k} b_i for each k (take c_k between, in rationals
    extended; strictness b_k < c_k needs b_k < min others; c_k <= min others)."""
    feasible = True
    for k in range(3):
        others = [b[i] for i in range(3) if i != k]
        if not (b[k] < min(others)):
            feasible = False
    return feasible

def is_order_indiscernible(b):
    # pairs (b0,b1),(b1,b2),(b0,b2) must have same comparison for indiscernibility
    # (for length 3, indiscernibility => all adjacent pairs same sign, and transitivity restricts)
    c01, c12, c02 = cmp(b[0], b[1]), cmp(b[1], b[2]), cmp(b[0], b[2])
    return c01 == c12 and (c01 == c02 or (c01 == 0))

fails = 0
total_ind = 0
examples = []
for b in order_type_reps():
    if is_order_indiscernible(b):
        total_ind += 1
        if check_triple(b):
            print("COUNTEREXAMPLE (separation possible):", b)
            fails += 1
        else:
            # record the reason: which k fails
            reasons = [k for k in range(3)
                       if not (b[k] < min(b[i] for i in range(3) if i != k))]
            examples.append((b, reasons))
print(f"indiscernible order-types checked: {total_ind}, separable: {fails}")
assert fails == 0
# show representative monotonic cases explicitly
for b in [(0, 1, 2), (2, 1, 0), (1, 1, 1), (0, 0, 1), (1, 0, 0)]:
    print(b, "separable?", check_triple(b),
          "needs each b_k unique strict min; maxima:", [min(b[i] for i in range(3) if i != k) for k in range(3)])
print("CUT_IMPOSSIBILITY_CORE_OK: no indiscernible triple admits singleton isolation by y<x")
