"""Lane-868 bounded target-block certificate (stdlib only).

Checks, from the exact target cell (tb,rot)=(12,1), T(3,4), Hopf-2 d3=3/2:
 1. g(T(3,4))=3, Alexander degree 6, tight max tb=5, parity ok.
 2. LOSS Alexander grading A=(tb-rot+1)/2 = 6 (resp. 7 for reversed
    orientation) strictly exceeds g=3, so HFK(-S3,T(3,4)) vanishes there
    and LOSS(L)=0 for EVERY representative -> LOSS gap impossible.
 3. Single-unknot Legendrian surgery diagrams with Bennequin-realizable
    (tb,rot) attain only d3 in {1/2,-3/2,...} (exact enumeration), never 3/2.
 4. The audit's example slope triple (4/3,3/2,5/4) is not a Farey triangle
    (|3*4-2*5|=2, so 3/2 and 5/4 are not Farey-adjacent).
Replay: python3 verify_target_block.py  -> prints BLOCK_CERTIFIED iff all pass.
"""
from fractions import Fraction

def alexander_T34():
    # (t^12-1)(t-1)/((t^3-1)(t^4-1)) as integer polys, ascending coeffs.
    def mul(a, b):
        c = [0]*(len(a)+len(b)-1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                c[i+j] += x*y
        return c
    def subm(a, i, v=1):
        a = a + [0]*(i+1-len(a))
        a[i] -= v
        return a
    # numerator: (t^12-1)(t-1) = t^13 - t^12 - t + 1
    num = [1, -1] + [0]*10 + [-1, 1]  # coeffs t^0..t^13
    # denominator: (t^3-1)(t^4-1) = t^7 - t^4 - t^3 + 1
    den = [1, 0, 0, -1, -1, 0, 0, 1]
    q, r = list(num), [0]*len(num)
    # polynomial long division (monic divisor)
    dd = len(den)-1
    quot = [0]*(len(num)-dd)
    rem = list(num)
    for k in range(len(num)-dd-1, -1, -1):
        c = rem[k+dd]  # den leading coeff is 1
        quot[k] = c
        for j in range(dd+1):
            rem[k+j] -= c*den[j]
    assert all(v == 0 for v in rem), f"non-exact division, rem={rem}"
    return quot  # ascending

def genus_T(p, q):
    return (p-1)*(q-1)//2

def loss_A(tb, rot):
    assert (tb + rot) % 2 == 1, "parity: tb+rot must be odd"
    return Fraction(tb - rot + 1, 2)

def d3_single(M11, rot, qplus):
    # d3 = (c^2 - 3 sig - 2 chi)/4 + q, 1x1: c^2 = rot^2/M11, sig=sign(M11), chi=2
    c2 = Fraction(rot*rot, M11)
    sig = 1 if M11 > 0 else -1
    return (c2 - 3*sig - 4)/4 + qplus

def farey(a, b):
    # a,b as (num,den); adjacent iff |ad-bc|==1
    return abs(a[0]*b[1] - b[0]*a[1])

def main():
    ok = True
    # 1. genus / Alexander / tight max / parity
    g = genus_T(3, 4)
    D = alexander_T34()
    assert g == 3, g
    assert D == [1, -1, 0, 1, 0, -1, 1], D  # t^6-t^5+t^3-t+1
    assert len(D)-1 == 2*g
    tight_max = 3*4 - 3 - 4
    assert tight_max == 5
    assert (12 + 1) % 2 == 1
    print(f"[1] g=3, Alex={D}, deg=6=2g, tight-max-tb=5, parity(12,1) ok")
    # 2. LOSS grading vs support
    A1 = loss_A(12, 1)
    A2 = loss_A(12, -1)
    assert A1 == 6 and A2 == 7
    assert A1 > g and A2 > g
    print(f"[2] A(LOSS|12,+1)={A1}, A(LOSS|12,-1)={A2}; both > g=3 "
          f"-> HFK=0 there -> LOSS(L1)=0=LOSS(L2). LOSS GAP IMPOSSIBLE.")
    # 3. single-unknot surgery d3 enumeration (Bennequin-realizable rots)
    got = set()
    for tb in (-1, -2, -3, -4, -5):
        M = tb + 1  # contact (+1) framing; (-1) gives Stein fillable d3<1/2 anyway
        if M == 0:
            continue  # tb=-1 with (+1): smooth framing 0, not a rational homology sphere
        for rot in range(-4, 5):
            if (tb + rot) % 2 != 1:
                continue
            if abs(rot) > -tb - 1 and not (tb == -1 and rot == 0):
                # |rot| <= -tb-1 for stabilized unknots (|rot| can equal -tb-1 steps)
                # keep enumeration explicit: allow |rot| <= -tb-1, plus rot=0 at tb=-1
                if not (abs(rot) <= -tb - 1):
                    continue
            got.add(d3_single(M, rot, 1))
    assert Fraction(3, 2) not in got, got
    print(f"[3] single-unknot (+1) Bennequin-realizable d3 values: "
          f"{sorted(got)}; 3/2 absent.")
    # 4. Farey check on the audit's example triple
    s1, s2, s3 = (4, 3), (3, 2), (5, 4)
    e12, e23, e13 = farey(s1, s2), farey(s2, s3), farey(s1, s3)
    assert e12 == 1, (e12,)
    assert e23 == 2, (e23,)  # NOT adjacent -> not a Farey triangle
    print(f"[4] Farey edges 4/3-3/2:{e12}, 3/2-5/4:{e23}, 4/3-5/4:{e13}; "
          f"example triple is NOT a Farey triangle.")
    print("BLOCK_CERTIFIED: LOSS-gap half impossible by degree; "
          "surgery/Farey steps of the audit need repair beyond the lane.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
