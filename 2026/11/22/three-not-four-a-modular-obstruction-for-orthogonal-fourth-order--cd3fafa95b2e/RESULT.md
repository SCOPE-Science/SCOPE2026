# Three, not four: a modular obstruction for orthogonal fourth-order polyanalytic Fock evaluations

## Finding

For every Gaussian parameter \(\alpha>0\), let \(\mathcal F^2_{\alpha,4}(\mathbb C)\) be the **full** order-four polyanalytic Bargmann–Fock space. Among its nonzero normalized point-evaluation kernel vectors, the maximum number that can be pairwise orthogonal is **exactly three**. Three are realized by an equilateral triangle at any of three algebraic side lengths, but four mutually orthogonal evaluations are impossible anywhere in the plane.

Writing \(\rho_1<\rho_2<\rho_3\) for the three positive roots of
\[
P(x)=x^3-12x^2+36x-24,
\]
any three nodes at the vertices of an equilateral triangle of side \(\sqrt{\rho_j/\alpha}\) have mutually orthogonal evaluations. The obstruction to four points is uniform over all choices of the six permissible pairwise distances: an exact finite reduction modulo \(53\) excludes every planar four-point Euclidean distance matrix with squared entries among \(\rho_1,\rho_2,\rho_3\).

The phenomenon is nonmonotone in the order of the **nested full spaces**: the full order-three polyanalytic Fock space admits four mutually orthogonal evaluation kernels, whereas its larger full order-four counterpart admits only three. This compares the same kind of point evaluations in two different Hilbert-space norms, not vectors fixed under inclusion.

## Assumptions and scope

The Hilbert space consists of functions \(f\) on \(\mathbb C\) satisfying \(\bar\partial^4 f=0\) and
\[
\|f\|^2=\frac\alpha\pi\int_{\mathbb C}|f(z)|^2e^{-\alpha|z|^2}\,dA(z)<\infty.
\]
Its reproducing kernel is
\[
K_{4,\alpha}(z,w)=e^{\alpha z\overline w}L_3^{(1)}(\alpha|z-w|^2),\qquad L_3^{(1)}(x)=4-6x+2x^2-\frac{x^3}{6}.
\]
Here **full** means the direct sum of the first four true polyanalytic Fock levels; the fourth *true* level alone has a different Laguerre polynomial and is not covered by this theorem. A node configuration is a finite subset of distinct points of \(\mathbb C\). Its point-evaluation vectors are normalized by the square roots of their diagonal kernel values.

## Proof

**Kernel zeros and the lower bound.** Since \(K_{4,\alpha}(z,z)=4e^{\alpha|z|^2}\), the normalized overlap at two nodes is
\[
\langle k_w,k_z\rangle=\frac14e^{i\alpha\operatorname{Im}(z\overline w)}e^{-\alpha|z-w|^2/2}L_3^{(1)}(\alpha|z-w|^2).
\]
Its exponential factors never vanish. Thus distinct kernels are orthogonal precisely when their scaled squared Euclidean distance belongs to the root set of \(P=-6L_3^{(1)}\). Sign changes \(P(0)<0<P(1)\), \(P(3)>0>P(4)\), and \(P(7)<0<P(8)\) exhibit three distinct positive roots. Equilateral triangles with the stated sides therefore furnish three orthogonal evaluation vectors.

**Four-point planar constraint.** Suppose four nodes existed. Rescale coordinates by \(\sqrt\alpha\), label them \(z_0,z_1,z_2,z_3\), and denote their six squared distances by
\[
(a,b,c,d,e,f)=(|z_1-z_0|^2,|z_2-z_0|^2,|z_3-z_0|^2,|z_1-z_2|^2,|z_1-z_3|^2,|z_2-z_3|^2).
\]
Every entry is one of the three roots of \(P\). The matrix twice the Euclidean Gram matrix of the three anchored displacement vectors is
\[
H=\begin{pmatrix}2a&a+b-d&a+c-e\\a+b-d&2b&b+c-f\\a+c-e&b+c-f&2c\end{pmatrix}.
\]
As three vectors in \(\mathbb R^2\) are dependent, \(\det H=0\). Put \(A=a+b-d\), \(B=a+c-e\), \(C=b+c-f\). The necessary condition is
\[
Q:=8abc+2ABC-2aC^2-2bB^2-2cA^2=0.
\]

**Cyclic cubic and a finite-field image.** The monic cubic \(P\) is irreducible over \(\mathbb Q\): as a cubic it would otherwise have an integer root dividing \(24\), and direct substitution rules out all those divisors. Its discriminant is \(5184=72^2\). More concretely, if \(u\) is any root, the other two are the distinct elements
\[
T(u)=4u-\frac{u^2}{2},\qquad U(u)=\frac{u^2}{2}-5u+12,
\]
with \(T(T(u))=U(u)\), \(T(U(u))=u\), and \(P(T(u))=P(U(u))=0\). Each identity follows by polynomial division by \(P\); \(T(u)\ne u\) because \(T(u)=u\) would give \(u=0\) or \(u=6\), neither a root. Hence **all** the permitted squared distances lie in the integral localized ring \(\mathbb Z[1/2,u]\).

Reduce this ring modulo the prime \(53\), sending \(u\mapsto29\). The reduction is well defined because \(P(29)\equiv0\pmod{53}\) and \(2\) is invertible. The complete root set reduces to
\[
\{29,T(29),U(29)\}=\{29,40,49\}\pmod{53}.
\]
Therefore an actual identity \(Q=0\) over the real algebraic number field would force \(Q=0\) modulo \(53\) for one of the \(3^6=729\) assignments of these residues to \((a,b,c,d,e,f)\).

**Exhaustive exact obstruction.** Direct evaluation of the displayed integer polynomial \(Q\) modulo \(53\) for every ordered six-tuple in \(\{29,40,49\}^6\) yields **no zero**. The result is entirely reproducible using the standard-library `CHECK.py` supplied with this statement. It checks the two algebraic transforms by rational-polynomial remainders, checks the three residues directly, and enumerates all \(729\) tuples. Independently, on each tuple it constructs the full five-by-five Cayley–Menger matrix and compares its determinant with \(Q\), avoiding dependence on one determinant expansion. Exactly \(36\) nonzero residue values occur; the counts in the four bins \(1\ldots13\), \(14\ldots26\), \(27\ldots39\), \(40\ldots52\) are \(233,211,215,70\), respectively, totaling \(729\). The zero residue count is exactly zero. This finite computation is exhaustive over the **entire** algebraic possibility space that the preceding proof reduces to, not a sample of geometric configurations.

The necessary four-point equation is impossible, so there is no four-node orthogonal configuration. Every larger orthogonal configuration would contain four nodes and is also impossible. The equilateral construction makes the maximum exactly three.

## Verification

Execute `python3 CHECK.py` in the same directory. The script uses only Python's standard library and performs exact arithmetic (rational polynomial reduction and integer determinants). Expected outputs include `Gram / Cayley-Menger determinant crosscheck: 729/729`, `nonzero mod 53: 729/729`, and `zero residues: 0`. The proof independently establishes why the finite modular check controls all real configurations; numerical approximations to roots are unnecessary. For orientation, the three squared separations are approximately \(0.9358222275\), \(3.3054072893\), and \(7.7587704831\).

## Relationship to prior work

Lee-Guzmán, Maximenko, Ramos-Vazquez, and Sánchez-Nungaray [1, Proposition 3.3 and §4] provide the full polyanalytic kernel and distinguish full from true levels. Fulsche and Hagger [2, §3, especially equations (3.1)–(3.3)] give the same exact Laguerre kernels and study their operator structure. Neither inspected kernel treatment asserts the four-point impossibility at full order four. A published four-node classification for **full order three** [3] is the closest exact orthogonal-design counterpart; it uses the *two* roots of a different quadratic Laguerre polynomial and proves the opposite four-node existence at that order. It does not imply the new arithmetic obstruction for the cubic. The standard three-distance-set literature permits broad finite configurations; the obstruction here depends on the special cyclic cubic and its finite-field image rather than a general three-distance-set cardinality theorem.

## Limitations

The theorem concerns exact pairwise orthogonality of point evaluations for a single specified *full* polyanalytic order, not near-orthogonality, noisy interpolation, optimal Gram conditioning, derivatives, higher complex dimensions, or true single-Landau-level spaces. The modular argument is tailored to the particular cubic \(P\); it is not an all-order bound. Although an exhaustive finite arithmetic certificate proves the stated obstruction once the analytic kernel identity is accepted, prior-publication priority remains a best-knowledge assessment and has not undergone an independent literature audit. Some earlier general polyanalytic kernel literature may contain alternate equivalent formulations not identified in the checks.

## References

[1] E. Lee-Guzmán, E. A. Maximenko, G. Ramos-Vazquez, and A. Sánchez-Nungaray, *Horizontal Fourier transform of the polyanalytic Fock kernel*, arXiv:2309.03410v1 (first publicly posted 2023-09-07), Proposition 3.3 and §4. https://arxiv.org/abs/2309.03410

[2] R. Fulsche and R. Hagger, *Quantum Harmonic Analysis for Polyanalytic Fock Spaces*, J. Fourier Anal. Appl. (2024), §3, DOI:10.1007/s00041-024-10124-9. https://link.springer.com/article/10.1007/s00041-024-10124-9

[3] *Aperture versus jitter in four-point orthogonal polyanalytic Fock designs* (2026), complete order-three orthogonal node classification, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-aperture-versus-jitter-in-four-point-orthogonal-polyanalytic-foc--bd3d947544b1

[4] NIST DLMF, §18.2(vi), positivity and simplicity of generalized Laguerre roots (background); https://dlmf.nist.gov/18.2
