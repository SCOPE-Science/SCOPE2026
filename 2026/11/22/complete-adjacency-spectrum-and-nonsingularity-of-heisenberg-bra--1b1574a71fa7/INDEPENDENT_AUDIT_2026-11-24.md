# Independent mathematical audit

## correctness

PASS

The Brandt multiplication makes distinct cells completely joined only when both index products vanish, and makes each off-diagonal cell K_m. On a diagonal cell the Heisenberg commutator is ab'-a'b, so all z central labels are included, joined to t disjoint cliques of s labels determined by projective direction. This works over all finite fields, including characteristic two. The within-cell difference and clique-contrast eigenspaces give the -1 and s-1 factors. For the remaining off-diagonal array u, the eligible cell sum with the self cell allowed is total(u)-row_j(u)-col_i(u)+u_ji at index (i,j); the missing self vertex contributes the separate -1. Substitution gives Q on constant modes and R on the symmetric standard mode, with the antisymmetric standard scalar m(n-1)-1. The row/column restrictions on u=r_i+c_j for zero-sum r,c have coordinate matrix [[n-1,-1],[-1,n-1]], invertible for n>=3. The remaining zero-row/column off-diagonal spaces split into symmetric and alternating arrays, of the claimed dimensions, on which the action is m-transpose minus identity. In particular the symmetric residual space is zero at n=3. These account for all n²m coordinates. For a determinant cross-check set N=ts, C=N-(s-1) and h=n-2, so zC+N=q^4. The leading two-by-two determinant of Q is C-nq^4; expansion gives det Q=(m-1)(C-nq^4)+md(C-2q^4)<0. Likewise det R=(m-1)C+mh(2q^4-C)>0. The other roots are nonzero for q>=2. Nonsingularity is of the ordinary adjacency matrix, for every characteristic of the underlying finite field; no arbitrary modular spectral decomposition is asserted. The independent replay checked the symbolic determinant identities and directly multiplied semigroup elements for n=3,q=2, giving exact adjacency determinant 93513959325 and the predicted numerical spectrum on 72 vertices. This finite run corroborates but does not prove the general factorization. Uploaded code and saved output were inspected, not run.

## originality

PASS

Credit the general Brandt construction, the matrix-unit base incidence and the group centralizer decomposition separately. The supported distinct claim is the full mixed-sector polynomial and universal real nonsingularity for nonabelian UT3 Brandt graphs. The closest inspected semigroup and group results use either different relation matrices, trivial group labels or the local group graph alone; no inspected result establishes the combined spectrum and sign conclusion.

## value

PASS

UT3 has the natural first nonabelian unitriangular geometry: commuting labels correspond to projective directions. The spectrum tests how that geometry interacts with exact matrix-unit incidence, rather than repeating a local-group computation. The mixed sectors and uniform determinant signs explain why the real singularity of the aperiodic graph for n>=4 disappears in this group extension. An exact spectrum and categorical nonsingularity for this size-and-field family are useful benchmarks for comparisons with other Brandt extensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
