# Shape-blind marked-base extension spectra of the homogeneous 4-branching \(D\)-set

## Finding
Let \((M,D)\) be the countable dense proper homogeneous 4-branching \(D\)-set. Let \(A\subset M\) be a finite set of \(n\geq3\) *pointwise named* elements. Its finite induced \(D\)-structure has a unique reduced unrooted leaf tree \(T_A\), with its \(n\) leaves labelled by \(A\) and all inner vertices of degree 3 or 4. Put \(q=q(A)\), the number of degree-four inner vertices.

For integers \(r,k\geq0\), let \(c_{n,q,r}(k)\) count the complete types over \(A\) of ordered injective \(r\)-tuples of points outside \(A\) whose finite reduced hull has exactly \(q+k\) quadrivalent inner vertices. Then \(c_{n,q,0}(0)=1\), all other initial values are zero, and
\[
c_{n,q,r+1}(k)=\bigl(2(n+r)-q-k-3\bigr)c_{n,q,r}(k)
+\bigl(n+r-2q-2k\bigr)c_{n,q,r}(k-1).
\]
In applying this formula an absent or infeasible previous state contributes zero. Every coefficient is determined by \(n,q,r,k\); **no other information about the shape of \(T_A\) is required.** The bivariate extension enumerator \(P_{n,q,r}(z)=\sum_k c_{n,q,r}(k)z^k\) equivalently satisfies
\[
P_{n,q,r+1}(z)=(2n-q-3+2r+(n-2-2q+r)z)P_{n,q,r}(z)
-(z+2z^2)P'_{n,q,r}(z),\qquad P_{n,q,0}(z)=1.
\]
Define \(F_{n,q}(r)=P_{n,q,r}(1)\). For fixed \(n\), two unlabelled base trees have the same complete sequence \((F_{n,q}(r):r\geq0)\) if and only if they have the same \(q\), since
\[
F_{n,q}(1)=3n-3q-5.
\]
Nonisomorphic unlabelled bases with identical complete injective tuple-type spectra first occur with six leaves. At \(n=6\), there are exactly two unlabelled shapes for \(q=0\), two for \(q=1\), and one for \(q=2\). Thus there are exactly two minimal two-element collision classes. The first four entries of each six-point profile, starting with arity zero, are:

| \(q\) | \(F_{6,q}(0)\) | \(F_{6,q}(1)\) | \(F_{6,q}(2)\) | \(F_{6,q}(3)\) |
|---:|---:|---:|---:|---:|
| 0 | 1 | 13 | 196 | 3397 |
| 1 | 1 | 10 | 124 | 1846 |
| 2 | 1 | 7 | 70 | 889 |

## Assumptions and scope
The 4-branching \(D\)-set is the countable homogeneous structure whose finite reduced hulls are unrooted leaf-labelled trees with all inner degrees in \(\{3,4\}\). The finite \(D\)-relation is reconstructed from path separation of two pairs of leaves. Homogeneity and the finite extension property identify complete nonalgebraic tuple types over individually fixed \(A\) with isomorphism classes of finite labelled extension trees fixing each old and each ordered new leaf. No extra metric, planar structure or arbitrary resolutions of a degree-four vertex are included. All newly added coordinates are pairwise distinct and distinct from all elements of \(A\). The theorem applies for \(n\ge3\) and \(0\le q\le\lfloor(n-2)/2\rfloor\).

## Proof
**1. The count of one-leaf extension sites.** Let \(n\) be the number of leaves, \(t\) the number of degree-three inner vertices, \(q\) the degree-four inner vertices, and \(E\) the number of edges. The tree identities \(n+3t+4q=2E\) and \(E=n+t+q-1\) give
\[
t=n-2-2q,\qquad E=2n-q-3.
\]
A reduced extension by one new labelled leaf can be created in exactly two ways: subdivide any old edge and attach the leaf at the new trivalent vertex (\(E\) choices, with no change in \(q\)), or attach the leaf directly to a trivalent vertex, which becomes degree four (\(t\) choices, increasing \(q\) by one). Attaching to a degree-four vertex would violate the degree bound. Each construction gives a distinct reduced extension tree fixing the labels. Conversely, removing the distinguished new leaf from any valid extension and suppressing a degree-two vertex if one arises recovers the old tree uniquely, together with its particular edge or trivalent-vertex insertion site. Consequently the alternatives are exhaustive and disjoint.

**2. Simultaneous extension recurrence.** Take an ordered \(r\)-tuple of new leaves and add the next one. A state with \(q+k\) quadrivalent vertices has \(n+r\) leaves, hence \(2(n+r)-q-k-3\) edges and \(n+r-2-2(q+k)\) trivalent vertices. The final state \(k\) therefore arises from the previous \(k\) by one of the former edge insertions or from the previous \(k-1\) by one of the latter vertex attachments. The displayed recurrence follows. The proof is inductive for every \(r\); finite computer checks are not used as an induction substitute. Multiplication of the recurrence by \(z^k\) and summation gives the stated differential recurrence.

**3. Complete profile equivalence.** Because the initial state and transition coefficients depend only on \(n,q\), every \(c_{n,q,r}(k)\), and thus the full type-count profile \(F_{n,q}(r)\), is independent of topology inside the fixed \((n,q)\) stratum. Conversely, putting \(r=1\) gives \(F_{n,q}(1)=E+t=3n-3q-5\); for a fixed \(n\) this determines \(q\) uniquely. This establishes both directions of the equivalence.

**4. Sharp first collision.** The unlabelled reduced trees on 3, 4 and 5 leaves have, respectively, the following cardinalities grouped by \(q\): at \(n=3\), \(\{0:1\}\); at \(n=4\), \(\{0:1,1:1\}\); and at \(n=5\), \(\{0:1,1:1\}\). These can be proved directly by the number of inner vertices and the allowed path skeletons. At six leaves the possible inner-vertex degree counts are \((t,q)=(4,0),(2,1),(0,2)\). For \((4,0)\), the inner-vertex skeleton is a four-vertex tree of maximum degree three, hence exactly a path or a three-armed star. For \((2,1)\), the inner skeleton consists of three vertices in a path; the unique degree-four vertex is either at the middle or at an endpoint, yielding two nonisomorphic shapes. For \((0,2)\), the two degree-four vertices are necessarily adjacent, giving a single shape. These degree/adjacency descriptions certify nonisomorphism and completeness without relying on enumeration. As each given \(q\) determines one complete type profile and different \(q\) are distinguished already by one-point counts, six is the sharp first size, with exactly two collision pairs.

## Verification
The included executable `verify.py` constructs each finite labelled reduced tree by its edge-subdivision and trivalent-vertex attachment sites, identifies labelled isomorphism types by complete edge-split signatures, and checks all trees through seven leaves against the tree count \(1,4,25,220,2485\). It canonically determines unlabelled shapes through six leaves by exhaustive permutations of internal vertices, confirms the two collision pairs and the unique \(q=2\) shape, and independently builds all two-step extensions of representatives of every six-leaf shape. Those outcomes agree with the coefficient recurrence. The run returned `ALL_SHAPE_AND_EXTENSION_CHECKS_OK`. The finite checks reinforce, but do not replace, the proof for unrestricted \(r\).

## Relationship to prior work
Adeleke and Neumann's work supplies the original structural framework for homogeneous \(D\)-relations; Assari, Hosseinzadeh and Macpherson describe the homogeneous 4-branching \(D\)-set and its associated set-homogeneous hypergraph, including a distinct six-point failure of set-homogeneity of the reduct. That failure is **not** the same claim as this equality of all pointwise-marked extension spectra. An existing published published-finding corpus finding, *Exact tuple-orbit profile of the homogeneous 4-branching D-set*, enumerates parameter-free injective tuple orbits by a rooted tree generating function; it does not calculate fixed-base extension profiles or their collision fibres. Grindstaff and Owen give a general combinatorial-geometric characterization of extensions of phylogenetic tree spaces, principally with edge metrics; their result contains tree-extension mechanisms but does not state the degree-four-constrained shape-blind count recurrence or the sharp minimal profile collision. The theorem here identifies the precise model-theoretic marked-base orbit-spectrum invariance and sharp loss of reconstruction, not novelty of standard elementary tree attachment operations.

## Limitations
The conclusion compares numerical complete type-count sequences, not the complete labelled isomorphism type of the base or the full relational structures of the stabilizer actions. The classification of collision classes is exhaustive only at the smallest nontrivial size of six leaves; higher-leaf collision multiplicities are not enumerated. An equivalent historical statement in tree-extension or permutation-group language might exist. The foundational 1998 memoir's full text was not accessible during this review; this source was checked at the table-of-contents and bibliographic level. The initiating-source publication date follows the identifiable 1998 record, but conflicting catalogue day precision remains. No independent mathematical audit has been performed.

## References
1. S. A. Adeleke and P. M. Neumann, *Relations Related to Betweenness: Their Structure and Automorphisms*, Memoirs of the American Mathematical Society **131** (623), 1998; DOI `10.1090/memo/0623`.
2. A. Assari, N. Hosseinzadeh, D. Macpherson, *Set-homogeneous hypergraphs*, Journal of the London Mathematical Society **108** (2023), 1852–1885; DOI `10.1112/jlms.12796`; preprint `arXiv:2202.09613`, first posted 2022-02-19, especially Section 2.1 and Proposition 4.2.3.
3. G. Grindstaff and M. Owen, *Geometric comparison of phylogenetic trees with different leaf sets*, `arXiv:1807.04235` (2018), especially Sections 2–3 and Theorem 3.12.
4. Estrada and Goodrick, *Model Theory of Homogeneous D-sets*, `arXiv:2502.09881` (2025), finite-tree representations and extension constructions.
5. *Exact tuple-orbit profile of the homogeneous 4-branching D-set*, published-finding corpus research record `2026/10/4/95b0894cb649` (2026), compared for parameter-free versus marked-base claims.
