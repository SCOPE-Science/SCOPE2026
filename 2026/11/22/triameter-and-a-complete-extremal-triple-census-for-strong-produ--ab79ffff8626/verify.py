"""Direct finite checks for the triametral-triple formulas of strong path products."""
from itertools import combinations, product
from math import comb, prod


def predicted(sizes):
    assert len(sizes) >= 2 and all(q >= 2 for q in sizes)
    a = max(sizes)
    k = sizes.count(a)
    if k >= 2:
        r = prod(q for q in sizes if q < a)
        u = a**3
        f = (u**k - 3*(u-2*a)**k + 3*(u-4*a+2)**k
             - (u-6*a+6)**k)
        assert f % 6 == 0
        return 3*(a-1), r**3 * (f//6)
    other = list(sizes)
    other.remove(a)
    b = max(other)
    j = other.count(b)
    s = prod(q for q in other if q < b)
    r = prod(other)
    return 2*(a-1)+(b-1), r*(r*r - s*s*(b*b-2)**j)


def direct(sizes):
    vertices = list(product(*(range(q) for q in sizes)))
    maximum = -1
    count = 0
    for x, y, z in combinations(vertices, 3):
        perimeter = sum(max(abs(u-v) for u, v in zip(p, q))
                        for p, q in ((x,y), (y,z), (z,x)))
        if perimeter > maximum:
            maximum = perimeter
            count = 0
        if perimeter == maximum:
            count += 1
    return maximum, count


def test():
    instances = [(2,2),(2,3),(2,3,4),(3,3,2),(3,3,3),
                 (5,3,3),(5,5,3),(2,3,3,3),(3,4,2),
                 (5,2,2,2),(4,3,3,2),(4,4,2,2)]
    checked = 0
    for sizes in instances:
        assert direct(sizes) == predicted(sizes), sizes
        checked += comb(prod(sizes), 3)
        print('EXACT', sizes, predicted(sizes))
    for q in range(2, 6):
        for d in range(2, 5):
            if q**d > 150:
                continue
            sizes = (q,)*d
            assert direct(sizes) == predicted(sizes)
            checked += comb(q**d,3)
    print('UNORDERED_TRIPLES_CHECKED', checked)
    print('VERIFY_OK')

if __name__ == '__main__':
    test()
