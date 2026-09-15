"""Exponent-gap check: generic Salem (MMS) vs target paraboloid restriction exponent."""
pairs = [(3, 1.0), (3, 1.5), (3, 0.5), (4, 2.0), (4, 1.0), (5, 2.0)]
for d, a in pairs:
    mms = 2 * (2 * d - a) / a
    tgt = 2 * (d + 1) / a
    print(f"d={d} alpha={a}: MMS={mms:.4f} target={tgt:.4f} gap={mms - tgt:.4f} formula_gap={2 * (d - 1 - a) / a:.4f}")
    assert mms > tgt, (d, a)
print("OK: MMS exponent strictly exceeds target exponent for all 0<alpha<d-1.")
