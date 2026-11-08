"""Direct tests and path-inventory dynamic programming for fan strong-majority colouring."""
from collections import Counter, defaultdict
from itertools import product


def graph_good(n, colors):
    hub, path = colors[0], colors[1:]
    neighbors = [tuple(path)]
    for i in range(n):
        nb = [hub]
        if i > 0:
            nb.append(path[i-1])
        if i < n-1:
            nb.append(path[i+1])
        neighbors.append(nb)
    for nb in neighbors:
        if max(Counter(nb).values()) > len(nb)//2:
            return False
    return True


def formula_three(n):
    assert n%2 == 0 and n>=2
    return 12 if n%4==0 else 6


def inventory(length, colors=3):
    states = {((i,), (tuple(1 if j == i else 0 for j in range(colors)))):1 for i in range(colors)}
    for k in range(1, length):
        nxt = defaultdict(int)
        for (last, tally), count in states.items():
            for x in range(colors):
                if x == last[0]:
                    continue
                t=list(tally);t[x]+=1
                nxt[((x,), tuple(t))]+=count
        states=nxt
    result=defaultdict(int)
    for (_, tally), v in states.items():
        result[tally]+=v
    return result


def count_four_odd(n):
    assert n>=3 and n%2
    m=n//2
    a,b=inventory(m),inventory(m+1)
    total=0
    for av,x in a.items():
        for bv,y in b.items():
            if all(av[i]+bv[i] <=m for i in range(3)):
                total+=x*y
    return 4*total


def construct(n):
    if n%2:
        path=tuple(1+i%3 for i in range(n));return (0,)+path
    if n%4==0:
        path=tuple((1,1,2,2)[i%4] for i in range(n))
    else:
        path=tuple((1,2,2,1)[i%4] for i in range(n))
    return (0,)+path


def main():
    for n in range(2,10):
        k=3 if n%2==0 else 4
        # Hub may be any named colour, so classify and count all assignments directly.
        total=0
        for path in product(range(k),repeat=n):
            for hub in range(k):
                if graph_good(n,(hub,)+path):
                    total+=1
        predicted=formula_three(n) if n%2==0 else count_four_odd(n)
        assert total == predicted,(n,total,predicted)
        print('GRAPH_NEIGHBOURHOOD_EXHAUSTION_OK',n,k,total)
        if n%2:
            # Lower palette is independently excluded by full neighbourhood enumeration.
            assert all(not graph_good(n, (h,)+path) for path in product(range(3),repeat=n) for h in range(3))
    for n in range(3,32,2):
        assert count_four_odd(n) > 0
        print('ODD_INVENTORY_OK',n,count_four_odd(n))
    for n in range(2,101):
        assert graph_good(n,construct(n)),n
    print('EXPLICIT_CONSTRUCTIONS_OK 2..100')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
