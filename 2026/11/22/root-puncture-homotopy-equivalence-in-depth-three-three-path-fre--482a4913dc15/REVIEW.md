# Independent mathematical audit

## correctness

PASS

The faces are induced disjoint unions of singletons and edges. On a star, collapsing the leaf simplex in the realization to a point leaves two vertices and q parallel edges, giving q-1 circles up to homotopy. With no r or a_i the common subcomplex U is the join of the M star complexes; the join/smash equivalence gives B spheres of dimension 2M-1 and hence free integral homology of rank B in that degree. In D, for a branch Q_i, any face containing a_i and b_ij can contain no other b_ih and no leaf under b_ij. Toggling a chosen leaf from a different b-subbranch pairs these faces. In decreasing size order every lower face has its paired upper face as the sole remaining proper coface; such a leaf exists since s_i>=2. Once these pairs are removed, the faces containing just a_i and leaves are removed by toggling any leaf, leaving U_i. For an elementary pair in one join factor, performing its joined pairs in decreasing size of the other-factor face ensures the same free-face condition. Thus D collapses to U. In L a face can have at most one a_i since it must admit r; if a_i is present it cannot contain any b_ij, but its own branch's leaves can be toggled freely, with the other branches unrestricted in U_h. This gives the claimed relative collapse L to U. The two inclusions from U are homotopy equivalences, so their factorization through the actual inclusion L into D proves that map is a homotopy equivalence; K is its mapping cone and is contractible. The regular case has M=b^2 and the asserted product B. CHECK.py and EXPECTED.txt were inspected, not executed; python3 CHECK.py in the source package replays two finite collapse checks and mod-two Betti number computations. Neither finite homology nor the sample count is used to infer contractibility or the integral statement.

## originality

PASS

The sphere type of D follows by joining known height-two branch types. Contractibility of K, even for the irregular family, follows independently from the earlier simplicial-vertex recurrence by induction; it should not carry the originality claim. The supported distinct content is the explicit elementary collapses of both the actual embedded root link and deletion onto the specific same star subcomplex, and thereby control of the actual L-to-D map. The inspected recursions give homotopy types, not this shared relative simplicial collapse statement.

## value

PASS

An explicit common collapse compares the root link with the deletion as they are embedded, not just as two abstract spaces with equal Betti numbers. It gives direct integral control of the map involved in adding the cone at the root, and an elementary relative certificate uniform in the branching parameters. This is useful even though absolute contractibility and the deletion wedge can be recovered through earlier theorems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
