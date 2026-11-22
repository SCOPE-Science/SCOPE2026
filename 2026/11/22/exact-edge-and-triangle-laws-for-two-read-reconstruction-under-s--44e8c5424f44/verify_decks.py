"""Direct deletion-deck verifier for binary words avoiding the contiguous pattern 001."""
from itertools import product

EDGE_COUNTS = [0, 0, 1, 4, 11, 26, 56, 114, 223, 424, 789, 1444, 2608]
TRI_COUNTS = [0, 0, 0, 0, 1, 5, 16, 42, 98, 212, 435, 859, 1648]

def direct(n):
    words = [''.join(p) for p in product('01', repeat=n) if '001' not in ''.join(p)]
    decks = [set(w[:i]+w[i+1:] for i in range(n)) for w in words]
    adjacent = [set() for _ in words]
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if len(decks[i] & decks[j]) >= 2:
                adjacent[i].add(j)
                adjacent[j].add(i)
    edges = sum(map(len, adjacent))//2
    triangles = sum(len(adjacent[i] & adjacent[j]) for i in range(len(words)) for j in adjacent[i] if i<j)//3
    return len(words), edges, triangles

def main():
    for n in range(1, 13):
        vertices, edges, triangles=direct(n)
        assert edges == EDGE_COUNTS[n], (n, edges, EDGE_COUNTS[n])
        assert triangles == TRI_COUNTS[n], (n, triangles, TRI_COUNTS[n])
        print(n, vertices, edges, triangles)
    print('VERIFY_DECKS_OK')

if __name__ == '__main__': main()
