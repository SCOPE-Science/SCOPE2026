"""Step 6c (normalization check): compare theta_0 = Theta_L / Theta_{Z^72-sub}?
Verify the norm-2 coefficient bookkeeping: count norm-2 vectors of L directly:
v = x/sqrt2, x in Z^72, x mod 2 in C, <v,v>=2 <=> sum x_i^2 = 4.
Case x = (+-2,0,...): needs (0..010..0)+2e_i in C-lift: 2e_i mod 2 = 0 in C always
  -> 72 coords * 2 signs = 144 vectors. So code-theta q^1 = 144 is FORCED for ANY
self-dual C (matches our 144). Extremal T has q^1=0 because extremal lattice has
min norm 8 — but Construction-A of a Type-II [72,36,16] code is NOT extremal as
a lattice (it always has the 144 norm-2 frame vectors + weight-16 short vectors
of norm 8). So the 'mismatch' is a normalization artifact, not an obstruction:
honest conclusion = consistency trace for the unscaled lattice; the extremal
comparison must be done at the level of the even-neighbor/ shadow, not raw A2.
Record this correction explicitly; claim NO mismatch trace.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
Cq = json.load(open(os.path.join(HERE, "s6b_trace.json")))["code_theta"]
print("forced frame count 2*72 = 144; code-theta q^1 =", Cq[1])
assert Cq[1] == 144
# weight-16 words contribute norm-8 (=q^4) vectors: A16 * 2^16 / (stabilizer)?
# each weight-16 c gives 2^16 lifts with x_i in {0,+-1...}: minimal lifts are
# x_i = +-1 on supp(c), 0 else: 2^16 vectors of sum-of-squares 16 -> norm 8.
print("A16*2^16 =", 249849 * 2 ** 16, "; code-theta q^4 =", Cq[4])
print("q^4 also gets 2Z-lift contributions (e.g. (+-2^4)): so Cq[4] >= A16*2^16,",
      "holds:", Cq[4] >= 249849 * 2 ** 16)
json.dump({"frame_q1": Cq[1], "forced_frame": 144,
           "note": "raw Construction-A lattice always has 144 norm-2 frame vectors; "
                   "extremal-theta comparison at raw level is a normalization artifact, "
                   "not a code obstruction. No mismatch trace claimed."},
          open(os.path.join(HERE, "s6c_normalization.json"), "w"), indent=1)
print("wrote s6c_normalization.json")
