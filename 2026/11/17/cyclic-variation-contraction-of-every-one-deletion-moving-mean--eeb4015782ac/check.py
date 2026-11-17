"""Exact and randomized tests for cyclic one-deletion order-statistic averaging.
Only Python standard library is required.
"""
from fractions import Fraction
from itertools import permutations
from random import Random


def filter_one_deletion(x, w, rank):
    n = len(x)
    assert 2 <= w <= n and 1 <= rank <= w
    output = []
    for i in range(n):
        window = [x[(i + j) % n] for j in range(w)]
        output.append((sum(window) - sorted(window)[rank - 1]) / (w - 1))
    return output


def variation(x):
    return sum(abs(x[(i + 1) % len(x)] - x[i]) for i in range(len(x)))


def linearized(x, w, rank):
    n = len(x)
    order = []
    for i in range(n):
        z = sorted(((i + j) % n for j in range(w)), key=lambda j: x[j])
        order.append([j for k, j in enumerate(z) if k != rank - 1])
    return order


def lin_apply(order, h):
    return [Fraction(sum(h[k] for k in indices), len(indices)) for indices in order]


def exhaustive():
    checks = 0
    for w, ns in [(3, range(3, 8)), (4, range(4, 7)), (5, range(5, 7))]:
        for n in ns:
            for ranks in permutations(range(n)):
                for rank in range(1, w + 1):
                    order = linearized(ranks, w, rank)
                    for start in range(n):
                        for length in range(1, n):
                            h = [0] * n
                            for j in range(length):
                                h[(start + j) % n] = 1
                            out = lin_apply(order, h)
                            assert variation(out) <= variation(h), (n, w, rank, ranks, h)
                            checks += 1
    print('EXHAUSTIVE_CHAMBERS_AND_ARCS_PASS', checks)


def exact_sharp():
    # Two distinct rational pairs with ratio exactly one on the short cycles.
    for baseline, delta in [([0,1,3,2],[0,1,1,0]),([0,1,2,3,4],[0,0,1,0,0])]:
        y = list(map(Fraction, baseline))
        x = [a + Fraction(h,10) for a, h in zip(y, delta)]
        fx = filter_one_deletion(x, 3, 2)
        fy = filter_one_deletion(y, 3, 2)
        assert variation([a-b for a,b in zip(fx, fy)]) == variation([a-b for a,b in zip(x,y)])
    for n in range(6, 41):
        x = [Fraction(1 if 3 <= i <= 5 else 0) for i in range(n)]
        y = [Fraction(0) for _ in range(n)]
        assert variation(filter_one_deletion(x, 3, 2)) == variation(x) == 2
    for w in range(2, 15):
        for n in [2*w, 2*w+1, 3*w]:
            x = [Fraction(int(i < w)) for i in range(n)]
            for rank in range(1, w+1):
                assert variation(filter_one_deletion(x, w, rank)) == variation(x) == 2
    for w in range(2, 15):
        x = list(map(Fraction,range(w)))
        for rank in range(1,w+1):
            assert variation(filter_one_deletion(x,w,rank)) == 0
    print('SHARP_THREE_POINT_AND_GENERAL_LARGE_CYCLES_PASS')


def stochastic_flow():
    rng=Random(28423)
    tests=0
    for _ in range(500):
        n=rng.randint(3,25)
        w=rng.randint(2,n)
        rank=rng.randint(1,w)
        x=rng.sample(range(1000),n)
        # Work on a lifted cycle; define the selected index set for each window.
        def selected(i):
            indices=list(range(i,i+w))
            indices.sort(key=lambda j:x[j%n])
            indices.pop(rank-1)
            return sorted(indices)
        support={i:selected(i) for i in range(-w,n+w+1)}
        for i in range(n):
            a,b=support[i],support[i+1]
            assert all(u<=v for u,v in zip(a,b))
            # Positive interlacing cumulative coefficients for every edge.
            for j in range(i,i+w):
                q=Fraction(sum(k<=j for k in a)-sum(k<=j for k in b),w-1)
                assert q>=0
        for j in range(n):
            total=Fraction(0)
            for i in range(j-w+1,j+1):
                a,b=support[i],support[i+1]
                total+=Fraction(sum(k<=j for k in a)-sum(k<=j for k in b),w-1)
            assert total==1
        tests+=1
    print('POSITIVE_COLUMN_STOCHASTIC_GRADIENT_FACTOR_PASS',tests)


def random_real_pairs():
    rng=Random(24)
    for k in range(3000):
        n=rng.randint(3,30);w=rng.randint(2,n);rank=rng.randint(1,w)
        a=[Fraction(rng.randint(-7,7),3) for _ in range(n)]
        b=[Fraction(rng.randint(-7,7),2) for _ in range(n)]
        h=[v-u for u,v in zip(a,b)]
        z=[v-u for u,v in zip(filter_one_deletion(a,w,rank),filter_one_deletion(b,w,rank))]
        assert variation(z)<=variation(h),(n,w,rank,a,b)
    print('EXACT_RATIONAL_RANDOM_TWO_INPUT_CHECKS_PASS',3000)


if __name__=='__main__':
    exhaustive()
    exact_sharp()
    stochastic_flow()
    random_real_pairs()
    print('ALL_ONE_DELETION_VARIATION_CHECKS_PASS')
