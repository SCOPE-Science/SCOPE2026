# Independent mathematical audit

## correctness

PASS

Over the algebraic closure the nontrivial characters of the odd abelian kernel form distinct inversion pairs. On each pair the two idempotents and the swapping involution give matrix units, and Frobenius transits the factors in orbits of length d_i. The center of each descended simple block is F_(q^d_i), and its Brauer group is trivial; the fixed trivial-character block is k[epsilon]/(epsilon^2). In M_2(K), a nonzero square-zero matrix has equal image and kernel, a line. Two such matrices with distinct lines have nonzero cross-products with distinct images; hence they cannot commute. In characteristic two the square of a sum forces commutation, so each projection of a square-zero k-space lies in one K-line even when k=F_2. Taking the full product proves maximality, and each agreeing coordinate contributes d_i to the intersection in addition to the common dual-number line. The trace-zero matrix equation reduces to a^2+bc=0, an irreducible cone (primitive and linear in b over the fraction field of K[a,c]); its derivatives vanish on the cone only at the vertex. Products over the algebraic closure give the stated reduced dimension and codimension-two singular components, not a reducedness claim about the original equations. A rank-one matrix acts separately on the two columns, and a nonzero dual number multiple of epsilon has regular rank one, so ranks add and yield the polynomial and the q^m count. Empty products give the claimed m=1 case. An independently written direct group-basis check (python3 /workspace/check_dihedral_incidence.py) exhausts F_2[(C_3 x C_3) rtimes C_2]; maximal cliques under square-zero pair sums recover 81 spaces of dimension 5, with unordered distinct intersection-dimension counts 1:648, 2:1296, 3:972, 4:324 and the predicted rank coefficients. This tests genuine multi-block incidence beyond the recorded single-orbit checks, not arbitrary groups or the geometry. Frozen code was inspected, not run.

## originality

PASS

Pass for the joint arithmetic arrangement, labeled incidence, reduced geometry and regular-rank refinement, not the single-block line lemma, character decomposition as such or known special-case point counts. An earlier rank-one nilpotent clique statement supplies the local constraint if the indexed statement holds as summarized; it does not give the same-object grouped incidence and rank calculation. Evidence is bounded by access to the identified sources.

## value

PASS

The invariant is motivated by a scalar count that is identical for all kernels of the same order. The exact maximal rational spaces and their intersection multiplicities retain splitting-field information that this count loses, with a useful independent regular-rank invariant and a separation between rational incidence and geometric irreducibility. The usefulness is in the explicit complete group-algebra package, not the isolated known matrix lemma or a new interpretation of the unit count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
