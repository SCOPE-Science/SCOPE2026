# Independent mathematical audit

## correctness

PASS

In the specified triangle-free cubic graph there are 12 claws and 72 unoriented nonbacktracking length-three paths, 12 of which are supported on the three vertex-disjoint squares; with the squares this gives 75 connected quadruples and 420 disconnected ones. The dual forbids the latter. On five vertices, connectivity after every deletion forces minimum degree at least two; bipartition sizes must be 2+3 and every vertex on the size-three side must meet both others, giving a forbidden K₂,₃ with overlapping squares. Thus the dual is the full 2-skeleton plus precisely the 75 tetrahedra. An independent greedy collapse in a different order removed every tetrahedron with a free triangle, leaving 145 triangles. The full 2-skeleton is simply connected, so Hurewicz and homological Whitehead classify the two-dimensional remainder as a wedge of 90 two-spheres. Duality has degree shift 9−i; the 6-skeleton of the simplex lies in X since the dual has no five-vertex face. This gives simple connectivity (indeed 5-connectivity), and Hurewicz and Whitehead give the claimed wedge of 7-spheres, not just the Betti number. All cut-complex generating facets have size eight. For the character, a setwise fixed simplex is a union of permutation cycles; its contribution to the negative augmented alternating trace is (−1)^(number of cycles), including +1 for the empty face. Enumeration by permuting the three squares and using their internal dihedral isomorphisms gave all 48 automorphisms. Cycle-union enumeration recovered all ten actual class entries (including the repeated row for two different classes), with weighted sum 144, hence invariant dimension 3.

## originality

PASS

No covering theorem found after comparing the actual statements for the closest object (Franklin total four-cut), applicable candidates for the ordinary cut construction, and computations for other twelve-vertex graphs. The group order was already known for this same graph and is not treated as new. The supported distinct content is the integral ordinary four-cut and dual homotopy type and the full rational ordinary four-cut character, including the three invariants.

## value

PASS

Computes a complete integral homotopy invariant and rational symmetry character of a standard cubic bipartite graph whose three squares rule out the girth-at-least-five shortcut. Ordinary and total four-cuts of the same graph give different outcomes; fixed classes persist for the ordinary cut complex and allow direct comparison with the total complex. The actual symmetry data, not just the Euler characteristic, are useful as a benchmark for extending ordinary cut-complex topology to graphs with squares.

The dated certificate retains the supplied scientific assessment, sources and limitations.
