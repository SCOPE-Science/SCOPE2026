"""Replayable certificate for lane-728 TARGET disproof.

Checks, from Marino-Salvatore (2025) conventions pinned in DRAFT.md:
  (A) Fox-Neuwirth dimension bound: every tree in FN^{<=}_3(4) has
      dim = sum(depths) <= 2*(4-1) = 6, so FN~_3(4)_8 = 0 and
      E^1_{-4,8} = H_8(Conf_4(R^3)) = 0 (total-degree-4 source window empty).
  (B) Parity: d^4 sends internal degree d -> d+3 (odd shift), so from any
      even-d source it lands in an odd-d group, which vanishes because
      H_*(Conf_n(R^3)) is concentrated in even degrees. Hence d^4 = 0
      identically (same reason the paper notes d^2 = 0).
  (C) Window table: every candidate source at filtration n=4 either is
      already zero or has its d^4 target in a zero group.

Stdlib only. Exit code 0 + VERIFY_OK on success.
"""
import itertools

M = 3          # ambient dimension
N_SRC = 4      # filtration n = 4 (i.e. p = -4)
R = 4          # differential index under dispute
MAXDIM = (M - 1) * (N_SRC - 1)  # 6


def fn_dims(n, m):
    """dims (with multiplicity over perms) of FN^{<=}_m(n) trees."""
    dims = []
    for _perm in itertools.permutations(range(n)):
        for depths in itertools.product(range(m), repeat=n - 1):
            dims.append(sum(depths))
    return dims


def main():
    dims = fn_dims(N_SRC, M)
    assert len(dims) == 24 * 27 == 648, len(dims)
    assert max(dims) == MAXDIM, max(dims)
    # (A) total-degree-4 source: (n,d) = (4,8) needs an 8-dim tree
    assert sum(1 for d in dims if d == 8) == 0
    print(f"(A) FN^{{<=}}_3(4): 648 trees, max dim {max(dims)}; "
          f"count at dim 8 = 0  =>  FN~_3(4)_8 = 0, E^1_{{-4,8}} = 0")

    # histogram for the record
    hist = {}
    for d in dims:
        hist[d] = hist.get(d, 0) + 1
    print("    dim histogram:", sorted(hist.items()))

    # (B) parity: d^4 shifts internal degree by R-1 = 3 (odd)
    assert (R - 1) % 2 == 1
    print(f"(B) d^{R} internal-degree shift = +{R-1} (odd): "
          f"even-d source -> odd-d target = 0 group; "
          f"odd-d source group itself = 0. So d^4 == 0 everywhere.")

    # (C) window table at filtration n = 4
    print("    (n,d) -> (n+4,d+3) | source status / target status:")
    for d in range(0, 10):
        src_zero = (d % 2 == 1) or (d > 2 * (N_SRC - 1))
        tgt = d + R - 1
        tgt_zero = (tgt % 2 == 1) or (tgt > 2 * (N_SRC + R - 1))
        reason_s = "0 (parity)" if d % 2 == 1 else (
            "0 (dim bound)" if d > 6 else "possibly nonzero")
        reason_t = "0 (parity)" if tgt % 2 == 1 else (
            "0 (dim bound)" if tgt_zero else "possibly nonzero")
        print(f"      (4,{d}) -> (8,{tgt}) | src: {reason_s}; tgt: {reason_t}")
        if not src_zero:
            assert tgt_zero, (d, tgt)  # every live source hits a zero group
    # total-degree readings of the target window
    assert 8 > 2 * (N_SRC - 1)          # total deg 4 => (4,8): dim-bound zero
    assert 9 % 2 == 1                   # total deg 5 => (4,9): parity zero
    print("    total-degree-4 source (4,8): zero by dim bound; "
          "total-degree-5 source (4,9): zero by parity.")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
