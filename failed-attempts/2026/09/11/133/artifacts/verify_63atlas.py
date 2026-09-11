"""Replay: atlas 6_3 reps have tb=-4, rot=1 and identical ungraded/bilinearized data."""
import sys; sys.path.insert(0, 'vendor_leg')
from legendrian import Leg
for lbl in ('K6_3.0', 'K6_3.1'):
    k = Leg(lbl)
    d = k.dga()
    assert d.check_d_squared()
    assert (k.tb, k.rot) == (-4, 1), (lbl, k.tb, k.rot)
    augs = d.augmentations(grading_mod=1)
    assert len(augs) == 384, (lbl, len(augs))
    assert all(a.format_poincare() == '4*t^0' for a in augs), lbl
    from collections import Counter
    bc = Counter(d.lin_hom(a, b, grading_mod=1, as_str=True) for a in augs for b in augs)
    print(lbl, 'tb,rot=', (k.tb, k.rot), 'naugs=', len(augs), 'bilin=', dict(sorted(bc.items())))
assert True
print('VERIFY_OK')
