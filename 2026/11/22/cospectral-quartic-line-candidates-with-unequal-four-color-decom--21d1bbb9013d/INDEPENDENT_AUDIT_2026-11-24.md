# Independent mathematical audit

## correctness

PASS

Convention 2.12 and Theorem 3.20/Remark 3.21 of Degtyarev–Rams confirm four mutually disjoint (-1)-vertices whose four neighborhoods partition the (-2)-rook graph into independent transversals. The Latin-square labels encode exactly such a partition. To check exhaustiveness independently, reduce the first row and column of the neighborhood Latin square to (0,1,2,3) by index and symbol permutations. The four reduced squares are the Klein table and the three simultaneous relabelings of the cyclic table. Thus the known two embeddable abstract types must be these (the color counts distinguish them). Independently reconstructed 64 edges per graph, both exact characteristic polynomials and the coloring counts (replay: python /workspace/branches/independent_replay.py 4 with SymPy). For the spectra, the symbol column space splits into the grid constant direction and three rook eigenvectors of eigenvalue -2; B^T B=4I supplies the couplings. Its orthogonal complement leaves six modes each at 2 and -2. Subtracting the two prescribed self-intersection diagonals yields the weighted blocks and inertia (1,10,9). For the count, normalize the first rook row by the unique palette permutation putting it in order (0,1,2,3); enumerate all 24 remaining Latin grids with that top row by exhausting three permutation rows, and multiply the four numbers of permissible colors for the independent extra vertices. The resulting normalized counts are 225 and 357, so the labeled counts are 5400 and 8568. Neither the matrices nor this enumeration establish separate geometric realizability of the candidates.

## originality

PASS

The two abstract types and their permitted incidence structure are prior; the shared adjacency/weighted polynomials together with the exact differing natural four-partition counts are supported as the distinct result on the checked evidence.

## value

PASS

The objects are the two pre-existing maximal twenty-line candidates, and four is the smallest possible number of disjoint families because a rook row already forms a 4-clique. The two exact numbers of minimal disjoint-line decompositions separate those candidates even with both ordinary and weighted intersection spectra fixed. This is a useful exact invariant at the level at which both abstract types are known, without asserting existence of both surfaces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
