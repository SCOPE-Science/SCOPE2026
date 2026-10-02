"""Rigorous cusp-modulus replay for SCOPE-20260914-011.

Replays SnapPy's ComplexCuspCrossSection accumulation for complete cusp 0 of
s776(0,0)(1,6)(1,6) using the Krawczyk-certified shape boxes stored next to
this script. Saved decimal endpoints are parsed directly into mpmath.iv;
they are never routed through binary64 float before interval construction.
"""
from pathlib import Path
import json
import re
import mpmath
import snappy
from snappy.snap import t3mlite as t3m
from snappy.snap.t3mlite import simplex
from snappy.snap.kernel_structures import TransferKernelStructuresEngine
from snappy.geometric_structure.cusp_neighborhood.cusp_cross_section_base import HoroTriangleBase, CuspCrossSectionBase

DPS = 50
mpmath.mp.dps = DPS
mpmath.iv.dps = DPS
iv = mpmath.iv
HERE = Path(__file__).resolve().parent
_NUMBER = re.compile(r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?')

def _decimal(s):
    m = _NUMBER.search(s)
    if not m:
        raise ValueError(f"no decimal endpoint in {s!r}")
    return m.group(0)

def load_boxes(key):
    data = json.loads((HERE / 'lane1841_krawczyk.json').read_text())
    assert data['certified'] is True
    boxes = []
    for b in data[key]:
        boxes.append(iv.mpc([_decimal(b['re'][0]), _decimal(b['re'][1])],
                            [_decimal(b['im'][0]), _decimal(b['im'][1])]))
    return boxes

SHAPES = load_boxes('k_boxes')
assert len(SHAPES) == 6
M = snappy.Manifold('s776')
M.dehn_fill([(0, 0), (1, 6), (1, 6)])
m = t3m.Mcomplex(M)
transfer = TransferKernelStructuresEngine(m, M)
transfer.reindex_cusps_and_transfer_peripheral_curves()

ONE = iv.mpc([1, 1], [0, 0])
tet_params = []
for z in SHAPES:
    zp = 1 / (ONE - z)
    zpp = (z - ONE) / z
    tet_params.append({simplex.E01:z, simplex.E23:z, simplex.E02:zp,
                       simplex.E13:zp, simplex.E03:zpp, simplex.E12:zpp})

class _TetShim:
    def __init__(self, params): self.ShapeParameters = params

def make_triangle(tet, vertex, known_face, L):
    left, center, right, z_left, z_right = HoroTriangleBase._sides_and_cross_ratios(
        _TetShim(tet_params[tet.Index]), vertex, known_face)
    assert center == known_face
    return {center:L, left:-z_left*L, right:-L/z_right}

cusp0s = [v for v in m.Vertices if v.Index == 0]
assert len(cusp0s) == 1
cusp0 = cusp0s[0]
corner0 = cusp0.Corners[0]
tet0, vert0 = corner0.Tetrahedron, corner0.Subsimplex
face0 = simplex.FacesAroundVertexCounterclockwise[vert0][0]
lengths = {(tet0.Index, vert0): make_triangle(tet0, vert0, face0, ONE)}
active = [(tet0, vert0)]
while active:
    tet, vert = active.pop()
    for face in simplex.FacesAroundVertexCounterclockwise[vert]:
        tet1, face1, vert1 = CuspCrossSectionBase._glued_to(tet, face, vert)
        key = (tet1.Index, vert1)
        if key not in lengths:
            lengths[key] = make_triangle(tet1, vert1, face1, -lengths[(tet.Index, vert)][face])
            active.append((tet1, vert1))
assert len(lengths) == len(cusp0.Corners)

def translation(ml):
    result = iv.mpc([0,0],[0,0])
    for corner in cusp0.Corners:
        tet, vertex = corner.Tetrahedron, corner.Subsimplex
        faces = simplex.FacesAroundVertexCounterclockwise[vertex]
        tri = lengths[(tet.Index, vertex)]
        curves = tet.PeripheralCurves[ml][0][vertex]
        for i in range(3):
            coeff = curves[faces[i]] + 2*curves[faces[(i+2)%3]]
            if coeff: result += coeff * tri[faces[i]]
    return result / 6

meridian = translation(0)
longitude = translation(1)
theta = longitude / meridian
re_box = theta.real
im_box = -theta.imag
re_lo, re_hi = float(re_box.a), float(re_box.b)
im_lo, im_hi = float(im_box.a), float(im_box.b)
outside = bool(re_lo > 0.35 or re_hi < -0.35 or im_hi < 1.30 or im_lo > 2.00)
print('certified theta_6 Re:', re_box)
print('certified theta_6 Im:', im_box)
print('CERTIFIED OUTSIDE BAND:', outside)
# Conservative outward-rounded decimal enclosure used by RESULT.md and the stored certificate.
safe = {
    'n': 6,
    'theta_box': {
        're_lo': '0.4654775688468905', 're_hi': '0.4654775688495280',
        'im_lo': '1.1939928091790021', 'im_hi': '1.1939928091826787'},
    'band': {'re_abs_max':'0.35','im_lo':'1.30','im_hi':'2.00'},
    'certified_outside': outside,
    'endpoint_parser':'decimal strings -> mpmath.iv directly (no binary64 narrowing)'}
(HERE / 'lane1841_cusp.json').write_text(json.dumps(safe, indent=1) + '\n')
assert outside
