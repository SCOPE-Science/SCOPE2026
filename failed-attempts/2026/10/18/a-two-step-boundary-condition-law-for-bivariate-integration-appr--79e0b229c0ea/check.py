"""Finite consistency checks for two-factor anchored and pinned integration spectra.
Run with: python check.py
All integer lattice calculations use exact integer arithmetic.
"""
import heapq
import math

GAMMA = 0.5772156649015328606065120900824


def shift_count(s, root):
    """Count positive numbers s, s+2, ... not exceeding root (s=1 or 2)."""
    return max(0, (root - s) // 2 + 1)


def count_hyperbola(s, t, threshold):
    """Ordered products (2i+s)(2j+t) <= integer threshold."""
    root = math.isqrt(threshold)
    m = shift_count(s, root)
    n = shift_count(t, root)
    left = sum(shift_count(t, threshold // (2 * i + s)) for i in range(m))
    right = sum(shift_count(s, threshold // (2 * j + t)) for j in range(n))
    return left + right - m * n


def count_direct(s, t, threshold):
    return sum(shift_count(t, threshold // u)
               for u in range(s, threshold // t + 1, 2))


def kth_product(s, t, rank):
    """Exact rank-th ascending ordered product (2i+s)(2j+t), including ties."""
    h = [((2 * i + s) * t, i, 0) for i in range(rank)]
    heapq.heapify(h)
    value = 0
    for _ in range(rank):
        value, i, j = heapq.heappop(h)
        j += 1
        heapq.heappush(h, ((2 * i + s) * (2 * j + t), i, j))
    return value


def b_value(pinned):
    return 2 * GAMMA + (4 - 2 * pinned) * math.log(2) - 1


def real_w_from_log(log_argument):
    """Solve w+log(w)=log_argument for w>0 (principal Lambert W)."""
    w = max(0.1, log_argument - math.log(max(1.0, log_argument)))
    for _ in range(32):
        step = (w + math.log(w) - log_argument) / (1.0 + 1.0 / w)
        w -= step
        if abs(step) < 1e-14 * max(1.0, w):
            break
    assert w > 0
    return w


def run():
    checks = 0
    # Independent row-by-row enumeration versus the hyperbola decomposition.
    for s, t in ((1, 1), (1, 2), (2, 1), (2, 2)):
        for threshold in range(1, 1602, 13):
            assert count_direct(s, t, threshold) == count_hyperbola(s, t, threshold)
            checks += 1
        for rank in (1, 2, 3, 4, 5, 9, 17, 50, 100, 200, 500, 1000):
            threshold = kth_product(s, t, rank)
            assert count_hyperbola(s, t, threshold) >= rank
            assert count_hyperbola(s, t, threshold - 1) < rank
            checks += 2
    # The exact count has an O(sqrt X) remainder with the calculated constant.
    for s, t in ((1, 1), (1, 2), (2, 2)):
        pinned = (s == 2) + (t == 2)
        b = b_value(pinned)
        for X in (500, 1000, 5000, 10000, 30000, 100000, 250000):
            count = count_hyperbola(s, t, 4 * X)
            main = X * (math.log(X) + b)
            assert abs(count - main) < 6 * math.sqrt(X)
            checks += 1
        for rank in (1000, 3000, 10000, 30000):
            product = kth_product(s, t, rank)
            # Singular number is 4/(pi^2 * product): pi^2 * rank * s_k=4*rank/product.
            exact_scaled = 4 * rank / product
            target = real_w_from_log(math.log(rank) + b)
            assert abs(exact_scaled - target) < 0.12
            checks += 1
    assert abs(b_value(0) - b_value(1) - 2 * math.log(2)) < 1e-13
    assert abs(b_value(1) - b_value(2) - 2 * math.log(2)) < 1e-13
    checks += 2
    for rank in (10000, 30000, 50000):
        p0 = kth_product(1, 1, rank)
        p1 = kth_product(1, 2, rank)
        p2 = kth_product(2, 2, rank)
        assert p0 <= p1 <= p2
        checks += 1
        # Finite-rank boundary corrections approach 2 log 2 from below.
        for diff in ((4 * rank / p0 - 4 * rank / p1),
                     (4 * rank / p1 - 4 * rank / p2)):
            assert 0 < diff < 2 * math.log(2) + 0.1
            checks += 1
    print(f"PASS: {checks} finite consistency assertions")
    print("one-step limit: 2 log(2) =", 2 * math.log(2))
    print("two-step limit: 4 log(2) =", 4 * math.log(2))
    for rank in (1000, 10000, 50000):
        vals = []
        for s, t in ((1, 1), (1, 2), (2, 2)):
            vals.append(4 * rank / kth_product(s, t, rank))
        print(f"rank={rank} scaled singular values: {vals}, consecutive differences: {[vals[0]-vals[1], vals[1]-vals[2]]}")

if __name__ == '__main__':
    run()
