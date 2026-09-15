"""Bounded recovery checks for lane-20410 target triage.

(1) Pohozaev obstruction to naive H^1 standing-wave counterexample:
    -Delta Q + w Q = |Q|^{p-1} Q in H^1 => coefficients force Q = 0 when
    p >= (d+2)/(d-2) (energy-supercritical). Hence e^{it}Q is unavailable
    as a bounded non-scattering counterexample in the target regime.
(2) Borderline critical-norm divergence of the zero-energy soliton tail
    Q ~ r^{-2/(p-1)}: density exponent equals -1 identically => log divergence.
(3) Merle-Raphael-Rodnianski coverage gap: p_JL = +inf for d <= 10, so the
    closest known Type II construction does not span the target d >= 5 range.
"""
import math

print("=== (1) Pohozaev coefficients (w=1) ===")
for d in [5, 6, 7, 11, 12]:
    p_sc = (d + 2) / (d - 2)  # Sobolev critical exponent 1+4/(d-2)
    for p in [p_sc + 0.5, p_sc + 2.0]:
        c_grad = ((d - 2) * (p + 1) - 2 * d) / (2 * (p + 1))
        c_l2 = d * (p - 1) / (2 * (p + 1))
        sc = d / 2 - 2 / (p - 1)
        print(f"d={d} p={p:.4f} sc={sc:.4f} c_grad={c_grad:.4f} c_L2={c_l2:.4f} "
              f"=> {'Q=0 forced' if c_grad >= 0 and c_l2 > 0 else 'no obstruction'}")

print("=== (2) Q-tail critical-norm density exponent ===")
for d, p in [(5, 4.0), (11, 5.0), (12, 8.0)]:
    sc = d / 2 - 2 / (p - 1)
    exp = -4 / (p - 1) - 2 * sc + d - 1
    print(f"d={d} p={p} sc={sc:.4f} density_exponent={exp:.6f} (=-1 => log divergence)")

print("=== (3) Joseph-Lundgren coverage gap ===")
for d in [5, 6, 10, 11, 12, 13]:
    if d <= 10:
        print(f"d={d}: p_JL=+inf => MRR Type II construction inapplicable")
    else:
        pjl = 1 + 4 / (d - 4 - 2 * math.sqrt(d - 1))
        print(f"d={d}: p_JL={pjl:.4f} => MRR needs p>p_JL (plus Discr>4, analytic p)")
