# Sharp six-vertex onset of edge-insertion reversal for connected Henson bases

## Finding

Let \(G\) be a finite, connected, induced subgraph of the universal homogeneous triangle-free graph \(H_3\). Name the vertices of \(G\) separately. Let \(p(G)\) be the fraction of complete ordered types of two distinct points outside the named base in which the two points are adjacent. Every insertion of one missing edge that preserves triangle-freeness strictly increases \(p\) when the base has at most five vertices. Six is sharp: on \(\{0,\ldots,5\}\), with old edges \(02,04,05,12,13\), the insertion of \(03\) decreases the fraction from \(249/778\) to \(225/709\).

## Assumptions and scope

Graphs are finite, simple and undirected. The original base must be connected. The fraction counts types uniformly, not graph vertices. The six-vertex example establishes the sharp connected threshold; there is no claim to classify all six-vertex insertions.

## Proof

Write \(I(G)\) for the number of independent subsets (including the empty set) and \(D(G)\) for the number of ordered disjoint pairs of such subsets. The two new points have independent named-neighbour sets. If they are not adjacent, the sets can overlap; if they are adjacent, the sets must be disjoint. Conversely these conditions make the full finite extension triangle-free. Universality realizes the extension over the named base by homogeneity, and homogeneity also identifies any two realizations of an identical labelled diagram. Thus there are exactly \(I(G)^2\) nonadjacent and \(D(G)\) adjacent types, and comparing \(p(G)=D(G)/(I(G)^2+D(G))\) is equivalent to comparing \(D(G)/I(G)^2\).

**Connected bases through five vertices.** In a connected triangle-free graph, a missing edge is admissible exactly when its endpoints have graph distance at least three. For at most three vertices, there is no such pair. At four vertices, the only eligible connected graph is the path \(P_4\), which becomes the cycle \(C_4\). At five vertices the trees are the path \(P_5\), the star, and the tree \(T\) with arms of lengths \(1,1,2\) at its vertex of degree three. A cyclic graph either has a \(C_5\), which cannot have a chord, or has a \(C_4\); then the fifth vertex has either one neighbour on it or two opposite neighbours. Call the cycle with one pendant vertex \(Q\); the case of two opposite neighbours is \(K_{2,3}\). Listing pairs at distance at least three in these graphs gives exactly the transitions below, up to relabelling. Each row gives the representative old edges and the marked new edge. An edge \(ij\) denotes \(\{i,j\}\).

| Transition | Old edges; new edge | \(D/I^2\) before | \(D/I^2\) after |
|---|---|---:|---:|
| \(P_4\to C_4\) | \(01,12,23;03\) | \(41/64\) | \(35/49\) |
| \(P_5\to Q\) | \(01,12,23,34;03\) | \(99/169\) | \(87/144\) |
| \(P_5\to C_5\) | \(01,12,23,34;04\) | \(99/169\) | \(81/121\) |
| \(T\to Q\) | \(01,02,03,34;14\) | \(103/196\) | \(87/144\) |
| \(Q\to K_{2,3}\) | \(01,12,23,03,34;14\) | \(87/144\) | \(77/121\) |

The numerators are obtained by counting assignments of labels \(0,1,2\) to the vertices, rejecting an assignment if any listed edge has the same nonzero label at both ends. The denominators count assignments using labels \(0,1,2,3\), interpreted as the two membership bits, rejecting an assignment if the two end labels share a bit. For example the following evaluates each integer entry directly with the given edge lists (invoke with \(n=4\) for the first row and \(n=5\) for the remaining rows):

```python
from itertools import product

def counts(n, edges):
    return tuple(sum(all((x[u] & x[v]) == 0 for u, v in edges)
                     for x in product(range(k), repeat=n)) for k in (3, 4))
```

All five ratios strictly increase, by cross-multiplication.

**Six vertices.** The stated old edges form a tree. The inserted edge closes the four-cycle \(0,2,1,3,0\); in the old tree the endpoints have distance three. For a check of the counts, use states \(0,1,\ldots,r\) with the same nonzero state prohibited on any edge. For \(r=1,2\) this counts \(I,D\), respectively. If vertex \(0\) has state zero, the two leaves \(4,5\) are unrestricted, and the three-vertex path \(2,1,3\) has \((r+1)^2+r^3\) states by conditioning on its middle vertex. This contributes \((r+1)^2((r+1)^2+r^3)\) in both graphs. If vertex \(0\) has a fixed nonzero state \(c\), the two leaves have \(r^2\) assignments. In the old graph, the chain has \(r(r+1)+r^2+r(r-1)^2\) assignments, by conditioning on vertex \(1\) having state zero, state \(c\), or another nonzero state. In the new graph both chain ends must avoid \(c\), so the corresponding count is \(2r^2+(r-1)^3\). Multiply those counts by \(r^3\) for the choices at vertex \(0\) and its leaves. This gives \((I,D)=(23,249)\) before and \((22,225)\) after. The resulting decrease in \(p\) is \(1491/551602>0\).

## Relationship to prior work

The realization and type-counting step uses Henson's universal homogeneous graph construction and the finite extension criterion; it is not a new graph-type correspondence. The unrestricted five-vertex edge-insertion reversal and its two marked classes are treated in *Sharp five-point onset of adjacency-frequency reversal under a named edge in the homogeneous triangle-free graph*. Both of those five-vertex examples have disconnected original bases. Appending isolated named vertices cannot produce a connected witness. The claim here is the connected cutoff and its witness, independently of the unrestricted census.

## References

- C. W. Henson, *A family of countable homogeneous graphs*, Pacific J. Math. **38** (1971), 69–83, §2. https://doi.org/10.2140/pjm.1971.38.69
- G. Conant, *Forking and dividing in Henson graphs*, §3. https://arxiv.org/abs/1401.1570
- *Sharp five-point onset of adjacency-frequency reversal under a named edge in the homogeneous triangle-free graph*, record SCOPE-20261122-ceda5b31c1f9.
