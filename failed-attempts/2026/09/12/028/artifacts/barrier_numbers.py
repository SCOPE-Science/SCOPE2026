"""Reproducible barrier arithmetic for lane-1106 target-exit request (stdlib only)."""
import math

q = 8380417
n, k, l_ = 256, 4, 4
sigma2 = 2.0
sigma = math.sqrt(sigma2)
beta = 70

def delta_bkz(b):
    return (b / (2 * math.pi * math.e) * (math.pi * b) ** (1.0 / b)) ** (1.0 / (2 * (b - 1)))

# 1. Threshold length for advantage >= 0.25 under eps=exp(-2 pi^2 s^2 l^2/q^2)
l_star = q / sigma * math.sqrt(math.log(4) / (2 * math.pi ** 2))
# alt normalization eps=exp(-pi s^2 l^2/q^2)
l_star_alt = q / sigma * math.sqrt(math.log(4) / math.pi)

# 2. Scaled full dual: dim d=2048, det=q^1024, Vol^{1/d}=sqrt(q)
d = (k + l_) * n
vol_root = math.sqrt(q)
GH = math.sqrt(d / (2 * math.pi * math.e)) * vol_root
mink = math.sqrt(d) * vol_root

# 3. BKZ-70 envelope
dl70 = delta_bkz(beta)
herm_full = (dl70 ** d) * vol_root

# 4. Optimal-subsample dual attack (N=1024 secret dims), pred(m)=delta^m q^{N/m}
N = 1024
m_opt = math.sqrt(N * math.log(q) / math.log(dl70))
pred_opt = math.exp(2 * math.sqrt(N * math.log(q) * math.log(dl70)))
need_lndelta = (math.log(l_star) / 2) ** 2 / (N * math.log(q))

out = {
    "l_star": l_star,
    "l_star_alt": l_star_alt,
    "vol_root": vol_root,
    "GH": GH,
    "minkowski": mink,
    "delta70": dl70,
    "hermite_full_dim": herm_full,
    "m_opt": m_opt,
    "pred_opt": pred_opt,
    "pred_over_star": pred_opt / l_star,
    "need_ln_delta": need_lndelta,
    "need_delta": math.exp(need_lndelta),
}
for key, val in out.items():
    print(f"{key} = {val!r}")
# Advantage at key lengths
for name, ll in [("minkowski", mink), ("q_vector", float(q)), ("pred_opt", pred_opt)]:
    adv = math.exp(-2 * math.pi ** 2 * sigma2 * ll ** 2 / q ** 2)
    print(f"adv[{name}] l={ll:.6g} -> {adv:.6g}")
