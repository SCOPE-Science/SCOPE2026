# Cospectral order-six plane-net boundaries with different integral Néron groups

## Finding

There exist two complex plane \(3\)-nets of order \(6\), one realizing \(C_6\) and the other realizing \(S_3\), whose naturally associated marked incidence stable curves have **identical** dual-graph Laplacian characteristic polynomials and spanning-tree counts, but **nonisomorphic** geometric Néron component groups in any regular split semistable smoothing with unit node thicknesses. Their dual graphs \(\Gamma_{C_6}\) and \(\Gamma_{S_3}\) have \(54\) vertices, \(108\) edges and cycle rank \(55\). Their integral critical groups are, respectively,

\[
K(\Gamma_{C_6})\cong (\mathbb Z/3\mathbb Z)^8\oplus\mathbb Z/6\mathbb Z\oplus(\mathbb Z/12\mathbb Z)^2\oplus(\mathbb Z/36\mathbb Z)^{10}\oplus\mathbb Z/72\mathbb Z\oplus\mathbb Z/216\mathbb Z,
\]

\[
K(\Gamma_{S_3})\cong (\mathbb Z/3\mathbb Z)^6\oplus\mathbb Z/6\mathbb Z\oplus(\mathbb Z/36\mathbb Z)^{12}\oplus\mathbb Z/72\mathbb Z\oplus\mathbb Z/216\mathbb Z.
\]

Both have order \(2^{31}3^{36}\) and the same Laplacian polynomial

\[
\det(tI-L)=t(t-9)(t-6)^2(t-3)^{20}(t^2-9t+12)^{15}.
\]

The distinction is already visible modulo \(3\): the incidence matrices have ranks \(15\) and \(16\), respectively, and their reduced Laplacians have ranks \(30\) and \(32\).

## Assumptions and scope

Over \(\mathbb C\), take a plane \(3\)-net of order \(6\) whose class-labelled lines are \(\ell_{0,a},\ell_{1,b},\ell_{2,c}\), with \(a,b,c\in G\) for \(G=C_6\) or \(G=S_3\); its marked net intersections are \(p_{a,b}\), and \(p_{a,b}\in\ell_{0,a}\cap\ell_{1,b}\cap\ell_{2,ab}\). The existence of both group types as plane nets follows from [1–3]; the nonabelian example is explicitly constructed by [2, Section 6.2].

Construct a **marked incidence nodal curve**, not necessarily the strict transform of the original plane union, by taking one \(\mathbb P^1\) for each of the \(18\) labelled net lines and one \(\mathbb P^1\) for each of the \(36\) marked net points. Glue these components at pairwise distinct smooth attaching points according to the \(108\) incidences. This curve is connected, stable, and has arithmetic genus \(108-54+1=55\): every rational component has either \(6\) or \(3\) distinct branches. Extra intersections among original lines of the same class are *not* included.

For any proper regular one-parameter split semistable smoothing of this stable curve with local node equation \(uv=t\) (thickness one), take the geometric Néron component group of the Jacobian of its smooth generic fibre. The standard component-group identification [4] gives precisely \(K(\Gamma_G)\). The result is not a claim about arbitrary node thicknesses, nor about the singular plane-line divisor's generalized Jacobian.

## Proof

**1. Canonical graph and spectrum.** Order the \(18\) line vertices in three blocks of six and the \(36\) point vertices by ordered pairs \((a,b)\in G^2\). Put

\[
B_{(i,c),(a,b)}=\begin{cases}1,&(i,c)\in\{(0,a),(1,b),(2,ab)\},\\0,&\text{otherwise},\end{cases}
\qquad
L=\begin{pmatrix}6I_{18}&-B\\-B^{\mathsf T}&3I_{36}\end{pmatrix}.
\]

Only the Latin-square property is needed to calculate

\[
BB^{\mathsf T}=\begin{pmatrix}6I_6&J_6&J_6\\J_6&6I_6&J_6\\J_6&J_6&6I_6\end{pmatrix},
\]

where \(J_6\) is all ones. Its eigenvalues are \(18\) once, \(6\) fifteen times, and \(0\) twice. The remaining eighteen dimensions on the point side lie in \(\ker B\). Schur complementation therefore gives the stated degree-\(54\) characteristic polynomial, independent of the group table. By the matrix-tree theorem its nonzero eigenvalues give

\[
\tau(\Gamma_G)=\frac{9\cdot 6^2\cdot 3^{20}\cdot 12^{15}}{54}=2^{31}3^{36}.
\]

This verifies full rank \(53\) for every reduced integral Laplacian and proves that no prime other than \(2\) or \(3\) appears in its Smith invariants.

**2. Intrinsic characteristic-three obstruction.** A row relation on \(B\) over \(\mathbb F_3\) consists of functions \(f,g,h:G\to\mathbb F_3\) obeying \(f(a)+g(b)+h(ab)=0\) for all \(a,b\). Substituting either variable equal to the identity shows that, after subtracting a constant, \(h\) is an additive homomorphism \(G\to(\mathbb F_3,+)\). Conversely every such homomorphism and two independent constants yield a row relation. Therefore

\[
\operatorname{rank}_{\mathbb F_3}B=18-2-\dim_{\mathbb F_3}\operatorname{Hom}(G,\mathbb F_3).
\]

For \(G=C_6\), the last dimension is \(1\); for \(G=S_3\), it is \(0\), because its abelianization is \(C_2\). Hence the ranks are \(15\) and \(16\). Modulo \(3\), every diagonal degree vanishes and \(L\) is a bipartite off-diagonal matrix; its rank is twice that of \(B\), giving \(30\) and \(32\). The reduced Laplacian has the same modular rank, since any one point column can be removed without changing the incidence rank (confirmed also by explicit row reduction in the supplied verifier). Thus the groups differ even though all rational spectral invariants coincide.

**3. Exact integral invariants.** Delete vertex \(0\) or vertex \(53\) from \(L\); these give two independent \(53\)-square reduced Laplacians. The supplied standalone program `CHECK.py` reconstructs both group tables and both graphs from definitions, then computes the complete Smith exponents at \(2\) and \(3\) using elementary invertible row and column operations over \(\mathbb Z/p^e\mathbb Z\), with exponents \(e=36\) at \(2\) and \(e=40\) at \(3\). Pivot choice minimizes valuation on the active block; every other entry is divisible by that power and can be cleared using the inverse of the pivot's unit part. This is a valid prime-local Smith reduction, not numeric rank estimation. All computed exponents are less than the respective modulus exponents.

The multiplicities of exponents \(0,1,2,3\) are:

| Group | At \(2\) | At \(3\) |
|---|---|---|
| \(C_6\) | \((38,1,12,2)\) | \((30,11,11,1)\) |
| \(S_3\) | \((38,1,12,2)\) | \((32,7,13,1)\) |

Both roots yield these same tuples. The total prime valuations are \(31\) and \(36\), agreeing with the independently proved spanning-tree count; therefore all invariant factors have been recovered. Sorting each prime-exponent list and multiplying corresponding powers produces the displayed divisor-ordered invariant factors. This completely proves the integral decomposition.

**4. Curve interpretation.** Since every vertex has at least three distinct attaching branches, the glued union of rational components is stable; its dual graph is exactly \(\Gamma_G\). Standard deformation theory of stable curves supplies one-parameter smoothings with simple local equations \(uv=t\). For a proper regular semistable model with this special fibre, the geometric Néron component group is the cokernel of any reduced intersection/Laplacian matrix [4]. Therefore the two displayed nonisomorphic groups are genuine component groups of genus-\(55\) algebraic-curve degenerations.

## Verification

`CHECK.py` uses only the Python standard library. Running `python CHECK.py` must end with `NET6_CYCLIC_DIHEDRAL_NERON_GROUPS_OK`. It rebuilds the \(18\times36\) incidence matrices, checks every entry of the predicted Gram matrices, reconstructs the \(54\times54\) Laplacians, computes independent modular ranks, and executes two prime-local Smith reductions on two different choices of deleted vertex for each group. Exact exponent lists and all divisor-ordered invariant factors are asserted; the product of the factors is tested against \(2^{31}3^{36}\). No floating-point arithmetic or external computer-algebra package is used.

## Relationship to prior work

Yuzvinsky [1] constructs cyclic plane nets and studies their plane geometry. Pereira–Yuzvinsky [2, Section 6.2] explicitly constructs dihedral group nets as general plane sections of reflection hyperplane pencils. Korchmáros–Nagy–Pace [3, Theorem 1.1 and Section 4.4] contextualizes both classes. Busonero–Melo–Stoppino [4, Sections 1–2] relates stable-curve dual graphs, their complexity groups, and Néron components, concentrating on cardinality rather than this pair's integral Smith forms. These results supply the geometric inputs but do not state the present cospectral/nonisomorphic component-group comparison. The distinction also does not follow from the known order-four net incidence-curve group coincidence or from graph critical groups of other configurations. A search in mathematical research records and the relevant primary literature found no equivalent statement, but does not establish exhaustive historical priority.

## Limitations

The theorem concerns **the stable marked-incidence curves**, not all singular points or the complete resolution graph of the original \(18\)-line arrangements. It classifies just the two specified group tables, not all Latin squares of order \(6\). Néron identification assumes a proper regular split unit-thickness semistable smoothing. The primary literature supports the realizability and general Néron correspondence; the numerical integral classifications are independently recomputed in the embedded program, not independently audited by an external mathematician. Older unpublished or differently indexed combinatorial calculations could subsume the originality claim.

## References

1. S. Yuzvinsky, *Realization of finite Abelian groups by nets in \(\mathbb P^2\)*, arXiv:math/0305242, originally public 2003-05-16. https://arxiv.org/abs/math/0305242
2. J. V. Pereira and S. Yuzvinsky, *Completely reducible hypersurfaces in a pencil*, arXiv:math/0701312, originally public 2007-01-10, Section 6.2. https://arxiv.org/abs/math/0701312
3. G. Korchmáros, G. P. Nagy, and N. Pace, *\(3\)-nets realizing a group in a projective plane*, arXiv:1104.4439, originally public 2011-04-22. https://arxiv.org/abs/1104.4439
4. S. Busonero, M. Melo, and L. Stoppino, *On the complexity group of stable curves*, arXiv:0808.1529, originally public 2008-08-11. https://arxiv.org/abs/0808.1529
