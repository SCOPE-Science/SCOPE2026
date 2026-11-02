# Arithmetic classification of affine-torus synchronization and compatibility fibres

## Finding
Let \(T^n=\mathbb R^n/\mathbb Z^n\) for \(n\geq0\), with \(T^0\) a point. Fix nonnegative integers \(a,b,c\), integral matrices \(A\in M_{c\times a}(\mathbb Z)\), \(B\in M_{c\times b}(\mathbb Z)\), and translations \(u,v\in T^c\). Define \(f:T^a\to T^c\) by \(f(x)=u+Ax\) and \(g:T^b\to T^c\) by \(g(y)=v+By\). Set
\[
M=[-A\ B],\qquad s=\operatorname{rank}_{\mathbb Q}M,
\]
where brackets denote horizontal concatenation. Let \(d_1\mid\cdots\mid d_s\) be the positive nonzero diagonal entries of the integral Smith normal form of \(M\). The empty product is \(1\).

The following give a complete arithmetic profile of this affine cospan:

1. Its **normalized homotopy-invariant** bivariate topological complexity is \(\mathrm{TC}_H(f,g)=s\).
2. Its **normalized strict** bivariate topological complexity is
\[
\mathrm{TC}(f,g)=\begin{cases}s,&u+A(T^a)=v+B(T^b),\\ \infty,&\text{otherwise}.\end{cases}
\]
3. The coincidence (compatibility) fibre \(\Delta_{f,g}=\{(x,y):f(x)=g(y)\}\) is empty if and only if \(v-u\notin A(T^a)+B(T^b)\). Whenever nonempty it is a disjoint union of exactly \(\prod_{i=1}^s d_i\) copies of \(T^{a+b-s}\).
4. The finite strict case can be decided by integral linear algebra and character congruences: its two image cosets coincide if and only if
\[
\operatorname{rank}_{\mathbb Q}A=\operatorname{rank}_{\mathbb Q}B=s,
\]
and every \(\ell\in\mathbb Z^c\) with \(A^{\mathsf T}\ell=0\) satisfies \(\ell\cdot(v-u)=0\) in \(\mathbb R/\mathbb Z\). It suffices to test an integral basis of this null lattice.

For **arbitrary continuous** maps \(T^a\to T^c\) and \(T^b\to T^c\), the homotopy-invariant formula in (1) still holds with their induced first-homology matrices; the strict formula (2) is restricted to the affine maps above.

## Assumptions and scope
Both bivariate invariants follow the normalized convention of García-Calcines and Vilches: value \(k\) means that \(k+1\) open planner domains suffice. In the strict invariant, a rule at \((x,y)\) supplies paths \(\alpha\) in \(T^a\), \(\beta\) in \(T^b\), with \(\alpha(0)=x\), \(\beta(1)=y\), and \(f\alpha(t)=g\beta(t)\) for every \(t\). In the homotopy-invariant version a rule is a path in the target from \(f(x)\) to \(g(y)\). All path spaces have compact-open topology. No rank, surjectivity, or nonzero-dimensional assumption is imposed.

## Proof
**Image and arithmetic preliminaries.** The images \(S_A=A(T^a)\), \(S_B=B(T^b)\), and \(W=S_A+S_B\) are connected closed Lie subgroups of \(T^c\), hence subtori; their dimensions equal respectively the rational ranks of \(A\), \(B\), and \(M\). Two connected subtori coincide precisely when their real/rational column spans coincide. Once these spans agree, the affine cosets coincide precisely when \(v-u\in S_A\). A point of \(T^c\) belongs to \(S_A\) precisely when every integer character annihilating \(S_A\) vanishes there. These characters are exactly \(\ell\in\mathbb Z^c\) with \(A^{\mathsf T}\ell=0\), proving (4), including the rank equalities and their sufficiency.

**Relaxed upper bound.** The difference map \(\delta:T^{a+b}\to T^c\), \(\delta(x,y)=g(y)-f(x)\), takes values in the coset \((v-u)+W\). A torus of dimension \(s\) has normalized Lusternik–Schnirelmann category \(s\), hence \(W\) admits \(s+1\) open sets on each of which the inclusion is nullhomotopic. An open categorical set admits a continuous selection of paths from the identity of \(W\) to each of its points (concatenate its contraction with a fixed path to the identity). Fix a path from \(0\) to \(v-u\) in \(T^c\). On preimages of these \(s+1\) sets under \(\delta-(v-u)\), concatenate this fixed path with the varying paths in \(W\), then translate by \(f(x)\) to obtain target paths from \(f(x)\) to \(g(y)\). Thus \(\mathrm{TC}_H(f,g)\le s\).

**Relaxed lower bound.** By translation in the topological group \(T^c\), a target path planner over an open set makes \(\delta\) nullhomotopic there. The map on rational degree-one cohomology induced by \(\delta\) has rank \(s\), because it is dual to \(M\). Pick \(s\) degree-one classes whose pullbacks are linearly independent. Their cup product is nonzero in the exterior algebra \(H^*(T^{a+b};\mathbb Q)\). Each factor restricts to zero on every planner domain. The relative cup-product (Lusternik–Schnirelmann) lower-bound argument therefore requires at least \(s+1\) open sets, showing \(\mathrm{TC}_H(f,g)\ge s\). This includes \(s=0\), when the difference is constant and a global planner exists. Together these prove (1).

**Strict obstruction and construction.** If a synchronized pair of paths exists at every input, then the common target trajectory lies in \(f(T^a)\cap g(T^b)\). Its first endpoint is \(f(x)\), for arbitrary \(x\), and its last endpoint is \(g(y)\), for arbitrary \(y\); therefore both image cosets must be contained in their intersection and must coincide. If they do not, no open cover by synchronized rules exists: \(\mathrm{TC}(f,g)=\infty\). If they coincide, call their common image \(H\); it is an affine copy of a torus of dimension \(s\). The corestrictions \(f:T^a\twoheadrightarrow H\) and \(g:T^b\twoheadrightarrow H\) are smooth surjective homomorphism translates and hence locally trivial bundles with continuous path-lifting functions. Cover \(H\) by \(s+1\) categorical opens to produce target paths *inside* \(H\) from \(f(x)\) to \(g(y)\), continuously on the corresponding \(s+1\) input domains. Lift each target path through \(f\) with initial point \(x\). Lift its time reversal through \(g\) with initial point \(y\), then reverse that lift. The resulting paths satisfy the required endpoints and identical target images. This proves \(\mathrm{TC}(f,g)\le s\). Every strict synchronized rule yields a relaxed target rule, so \(\mathrm{TC}(f,g)\ge\mathrm{TC}_H(f,g)=s\). Thus (2) holds.

**Compatibility-fibre topology.** The fibre \(\Delta_{f,g}\) is exactly \(\delta^{-1}(0)\); it is nonempty precisely when \(v-u\in W\). If nonempty, it is a translate of the kernel of the torus homomorphism represented by \(M\). Unimodular integral row and column operations turn \(M\) into Smith diagonal form with nonzero entries \(d_1,\ldots,d_s\). Its kernel is homeomorphic to
\[
T^{a+b-s}\times \prod_{i=1}^{s}(\mathbb Z/d_i\mathbb Z).
\]
It therefore has precisely \(\prod_i d_i\) torus components, proving (3).

**Continuous-map extension.** Every continuous map \(T^a\to T^c\) is homotopic to the torus homomorphism defined by its integral first-homology matrix (plus a harmless translation), since \(T^c\) is a \(K(\mathbb Z^c,1)\). The homotopy invariance of \(\mathrm{TC}_H\) from García-Calcines and Vilches, Corollary 5.7, transports (1) to general continuous maps. There is no analogous claim for strict complexity.

## Verification
For two circle covers of degrees \(2\) and \(3\), the matrix \([ -2\ \ 3]\) has rank \(1\) and Smith factor \(1\): both complexities are \(1\), and the compatibility fibre is one circle. With degrees \(2\) and \(4\), both complexities remain \(1\), but the Smith factor is \(2\) and the fibre is two circles. These are exact algebraic checks, not evidence that finite experiments prove the general theorem. For maps to a two-torus with \(A=(1,0)^\mathsf T\) and \(B=(0,1)^\mathsf T\), the images meet but are not equal: relaxed complexity is \(2\) and strict complexity is infinite. For two translated identical circle images at different heights, relaxed complexity is \(1\), strict complexity is infinite, and the compatibility fibre is empty. The proof handles all integers and arbitrary offsets without experimental induction.

## Relationship to prior work
García-Calcines and Vilches (2026, arXiv:2601.16059v1) introduce both bivariate invariants, prove a collaboration theorem for fibrations (Theorem 4.1), show homotopy invariance of the relaxed invariant (Corollary 5.7), and identify it with the category of a difference map for an H-group target (Theorem 8.9). Their five-torus Example 3.5 gives a cohomological lower bound for specific power maps; their circle example treats an individual pair. The result above uses those general foundations and standard cohomology and Smith normal form, but supplies a uniform **explicit arithmetic classification**, includes image-coset disjointness versus partial coincidence and the topology of the compatibility fibre, and computes both invariants across all integral matrices and affine translations. The work of Macías-Virgós and Mosquera-Lois (2018, arXiv:1810.12591) supplies homotopic-distance background. No novelty is asserted for the Smith theorem, the LS-category of a torus, or the general homotopy-invariance and difference-map principles themselves.

## Limitations
The assertion of strict complexity is for affine torus maps, not all continuous maps or arbitrary compact abelian groups. The component formula counts connected components of the fibre, not components of its path space, and holds only when the fibre is nonempty. The arithmetic test assumes exact torus translations; floating-point offsets require an additional representation model. The literature comparison cannot exclude equivalent formulations in uncatalogued work, and a general theorem may imply individual portions of this classification without using its explicit parameters. No independent audit has been performed.

## References
1. J. M. García-Calcines and J. A. Vilches, *Bivariate topological complexity: a framework for coordinated motion planning*, arXiv:2601.16059v1 (first public 2026-01-22), https://arxiv.org/html/2601.16059v1 .
2. E. Macías-Virgós and D. Mosquera-Lois, *Homotopic distance between maps*, arXiv:1810.12591v3, https://arxiv.org/html/1810.12591v3 .
