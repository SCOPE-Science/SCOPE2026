"""Lane 409 — rigorous analytic certificate for single-ray large-amplitude domination.

Exact setting of check_large_amplitude.py (g=1/2, two-color single-mode ray).
Divide by V=(2pi)^3; all coefficients exact rationals except K2/V = g*sqrt(3)/2.
Bound sqrt(3) in [1.7320508075688772-1e-12, +1e-12] via math (rigorous enough as
explicit decimal enclosure checked by squaring: 1.7320508075688772^2 < 3 < 1.7320508075688774^2).

Prove: H(a)/V = (5/128)a^6 - (5/32)a^4 - P*(sqrt3/4)*a^3 + (1/2-P)*a^2 with P=2
  => h(a) = (5/128)a^6 - (5/32)a^4 - (sqrt3/2)a^3 - (3/2)a^2 > 0 for all a >= 4,
  and h'(a) > 0 there (so H increasing, domination persists to infinity).
Writes results11.json.
"""
import json, math, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results11.json")
res = {}

# rigorous sqrt3 enclosure
s_lo, s_hi = 1.7320508075688772, 1.7320508075688774
assert s_lo**2 < 3 < s_hi**2, (s_lo**2, s_hi**2)
res["sqrt3_enclosure"] = [s_lo, s_hi]
res["sqrt3_enclosure_pass"] = True

# h(a) = c6 a^6 + c4 a^4 + c3 a^3 + c2 a^2, c3 negative with sqrt3 factor
c6 = 5.0 / 128.0
c4 = -5.0 / 32.0
c2 = -1.5
# worst case (smallest h) uses largest sqrt3 for the negative cubic term
c3_hi = -(s_hi / 2.0)  # most negative
c3_lo = -(s_lo / 2.0)
res["coeffs"] = {"c6": c6, "c4": c4, "c3_worst": c3_hi, "c2": c2}

def h(a, c3):
    return c6 * a**6 + c4 * a**4 + c3 * a**3 + c2 * a**2

def hp(a, c3):
    return 6 * c6 * a**5 + 4 * c4 * a**3 + 3 * c3 * a**2 + 2 * c2 * a

def hpp(a):
    # h''(a) = 30 c6 a^4 + 12 c4 a^2 + 6 c3 a + 2 c2; worst case c3 most negative
    return 30 * c6 * a**4 + 12 * c4 * a**2 + 6 * c3_hi * a + 2 * c2

a0 = 4.0
res["h_at_4_worst"] = h(a0, c3_hi)
res["hp_at_4_worst"] = hp(a0, c3_hi)
res["hpp_at_4_worst"] = hpp(a0)
# h''(a) increasing for a>=4? h'''(a)=120 c6 a^3 + 24 c4 a + 6 c3;
# check h'''(4) with worst c3 > 0 then h'' increasing afterwards since h''''>0.
hppp4 = 120 * c6 * 64 + 24 * c4 * 4 + 6 * c3_hi
res["hppp_at_4_worst"] = hppp4
# h''''(a) = 360 c6 a^2 + 24 c4 = a^2*360*5/128 - 120/32 = 14.0625 a^2 - 3.75 > 0 for a>=1
res["h4_pos_for_a_ge_1"] = bool(360 * c6 * 1 - 3.75 > 0)
res["chain"] = ("h''''>0 on [1,inf) => h''' increasing; h'''(4)>0 => h''' >0 on [4,inf) "
    "=> h'' increasing; h''(4)>0 => h''>0 => h' increasing; h'(4)>0 => h' >0 "
    "=> h increasing; h(4)>0 => h>0 on [4,inf). Each numeric inequality uses the "
    "worst-case (most negative) sqrt3 upper bound, so rigorous.")
res["all_pass"] = bool(res["h_at_4_worst"] > 0 and res["hp_at_4_worst"] > 0
    and res["hpp_at_4_worst"] > 0 and hppp4 > 0)
res["values"] = {"h4": res["h_at_4_worst"], "hp4": res["hp_at_4_worst"],
    "hpp4": res["hpp_at_4_worst"], "hppp4": hppp4}
res["conclusion"] = ("RIGOROUS single-ray lemma: along the two-color single-mode ray at g=1/2, "
    "with constant-proxy rough-field size P=2, D(a)-|T(a)| >= V*h(a) > 0 for all a>=4 "
    "and increasing. Dissipation strictly dominates rough drift + energy at large amplitude. "
    "Degree-count (F~a^2, D~a^6, T~a^3) is homogeneous hence general-profile mechanism evidence.")

with open(OUT, "w") as f:
    json.dump(res, f, indent=2)
print(json.dumps(res, indent=2))
