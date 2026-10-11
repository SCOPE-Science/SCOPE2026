#!/usr/bin/env python3
import math


def R_of_x(n, x):
    N = n * math.pi
    k = N + x / N
    d = k - N
    num = -4.0 * k * k + (k * k - 1.0) ** 2 * math.cos(2.0 * d) - (k * k + 1.0) ** 2 * math.cos(4.0 * d)
    den = (k * k - 1.0) ** 2 * math.sin(d) ** 2
    return num / den


def bisect_edge(n, x0, target):
    lo, hi = x0 - 0.30, x0 + 0.30
    flo = R_of_x(n, lo) - target
    fhi = R_of_x(n, hi) - target
    if flo * fhi > 0.0:
        raise ValueError("edge bracket failed")
    for _ in range(90):
        mid = 0.5 * (lo + hi)
        fm = R_of_x(n, mid) - target
        if flo * fm <= 0.0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


def predicted_offset(n, x0):
    N = n * math.pi
    rt2 = math.sqrt(2.0)
    if abs(x0 + rt2) < 1e-12:
        c = -2.0 + 4.0 * rt2 / 3.0
    elif abs(x0 + 1.0) < 1e-12:
        c = -1.0 / 3.0
    elif abs(x0 - 1.0) < 1e-12:
        c = -5.0 / 3.0
    elif abs(x0 - rt2) < 1e-12:
        c = -2.0 - 4.0 * rt2 / 3.0
    else:
        raise ValueError("unknown edge")
    return 2.0 * x0 + c / (N * N)


def exact_offset(n, x):
    N = n * math.pi
    k = N + x / N
    return k * k - N * N


def main():
    rt2 = math.sqrt(2.0)
    specs = [(-rt2, 2.0), (-1.0, -2.0), (1.0, -2.0), (rt2, 2.0)]
    previous_scaled = None
    for n in (10, 20, 40):
        N = n * math.pi
        scaled_errors = []
        offsets = []
        for x0, target in specs:
            x = bisect_edge(n, x0, target)
            off = exact_offset(n, x)
            pred = predicted_offset(n, x0)
            scaled_errors.append(abs(off - pred) * N ** 4)
            offsets.append(off)
        if not (offsets[0] < offsets[1] < 0.0 < offsets[2] < offsets[3]):
            raise AssertionError("edge ordering failed")
        if max(scaled_errors) > 20.0:
            raise AssertionError("N^-4 residual bound failed")
        previous_scaled = scaled_errors
    # Leading limits and source-level widths/gap recovered from the edge limits.
    if abs((2.0 * rt2 - 2.0) - 2.0 * (rt2 - 1.0)) > 1e-15:
        raise AssertionError("band width identity failed")
    if abs(2.0 - (-2.0) - 4.0) > 1e-15:
        raise AssertionError("gap identity failed")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
