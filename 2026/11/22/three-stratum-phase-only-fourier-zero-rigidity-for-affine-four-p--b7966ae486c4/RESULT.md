# Three-stratum phase-only Fourier-zero rigidity for affine four-point simplices

## Finding
Let \(p\ge5\) be prime, \(d\ge3\), and \(u_1,u_2,u_3\in\mathbb F_p^d\) be linearly independent. Suppose \(f:\mathbb F_p^d\to\mathbb C\) has exact support \(S=x_0+\{0,u_1,u_2,u_3\}\) and its four nonzero coefficients have equal modulus. The complete set of possible numbers of Fourier zeros is
\[
\boxed{\#\{\xi:\widehat f(\xi)=0\}\in\{0,\ p^{d-2},\ (2p-1)p^{d-3}\}.}
\]
All three values occur for every support \(S\). In particular,
\[
\boxed{|\operatorname{supp}\widehat f|\ge(p^3-2p+1)p^{d-3},}
\]
with equality exactly for two-opposite-pair phase configurations described below.

The zero set is either empty, one affine subspace of codimension two, or the union of **two distinct affine subspaces of codimension two meeting in one affine subspace of codimension three**. The three cases are characterized entirely by antipodal cosets of the four coefficient phases.

## Assumptions and scope
The finite group is the vector space \(G=\mathbb F_p^d\), with \(p\ge5\) odd prime and \(d\ge3\). The three support differences must be linearly independent; supports of affine rank two and unequal coefficient magnitudes are excluded. Use the non-unitary finite Fourier transform
\[
\widehat f(\xi)=\sum_{x\in G}f(x)\exp(-2\pi i\langle \xi,x\rangle/p).
\]
Multiplication by a nonzero scalar and support translation do not change the number or geometry of Fourier zeros. Normalize the four coefficients to \(\alpha_0,\alpha_1,\alpha_2,\alpha_3\in\mathbb T\), and write \(\mu_p\) for the group of complex \(p\)-th roots of unity.

A perfect matching \(M=(ij)(k\ell)\) on the four indices is called **feasible** if both \(\alpha_i/\alpha_j\in-\mu_p\) and \(\alpha_k/\alpha_\ell\in-\mu_p\). This condition is independent of the order of vertices in each pair. There are exactly zero, one, or two feasible matchings. The number of Fourier zeros is respectively \(0\), \(p^{d-2}\), or \((2p-1)p^{d-3}\).

## Proof
**1. Fourier reduction and exact fibers.** Put \(\omega=\exp(2\pi i/p)\). After factoring the never-vanishing character contributed by \(x_0\), the Fourier transform has the form
\[
P(t_1,t_2,t_3)=\alpha_0+\alpha_1\omega^{t_1}+\alpha_2\omega^{t_2}+\alpha_3\omega^{t_3},
\]
where \(t_j=-\langle\xi,u_j\rangle\). Linear independence of the \(u_j\) makes the map \(\xi\mapsto(t_1,t_2,t_3)\) surjective, each fiber having exactly \(p^{d-3}\) elements. Hence it suffices to count zeros on \(\mu_p^3\).

**2. Four-unit cancellation lemma.** If four complex numbers of modulus one sum to zero, they split into two pairs of opposites. To prove it, call them \(z_0,z_1,z_2,z_3\), with elementary symmetric sums \(e_j\). Their sum gives \(e_1=0\). Because their product \(e_4\) has modulus one, \(e_3=e_4\overline{e_1}=0\). Their monic root polynomial is therefore \(T^4+e_2T^2+e_4\), an even polynomial, so its roots are two opposite pairs, including multiplicities. Consequently every zero of \(P\) realizes at least one of the three perfect matchings.

**3. Each matching gives an affine line or nothing.** For \(M=(ij)(k\ell)\), the opposite-pair conditions are
\[
\alpha_i\omega^{t_i}=-\alpha_j\omega^{t_j},\qquad
\alpha_k\omega^{t_k}=-\alpha_\ell\omega^{t_\ell},\qquad t_0=0.
\]
They are solvable precisely when \(M\) is feasible. A feasible matching specifies two independent affine linear equations in \((t_1,t_2,t_3)\in\mathbb F_p^3\), since its two edges are disjoint on the four-vertex set anchored at vertex zero. It therefore contributes one affine line of exactly \(p\) zeros. Every Fourier zero belongs to at least one such line.

**4. At most two feasible matchings.** If both \((01)(23)\) and \((02)(13)\) are feasible, then \(\alpha_1/\alpha_2\in\mu_p\), because the ratios of both to \(\alpha_0\) belong to \(-\mu_p\). But feasibility of the remaining matching \((03)(12)\) requires \(\alpha_1/\alpha_2\in-\mu_p\), impossible because \(\mu_p\cap(-\mu_p)=\varnothing\) for odd \(p\). Relabeling handles all cases.

**5. Two matching lines intersect in exactly one point.** If two feasible matchings share no edge, their union is a four-cycle; the simultaneous opposite-pair equations uniquely fix every \(\alpha_j\omega^{t_j}\) relative to \(\alpha_0\), giving one character triple. In coordinates for \((01)(23)\) and \((02)(13)\), the first fixes \(t_1\), the second fixes \(t_2\), and either fixes \(t_3\); compatibility of the last equation is automatic from the two feasible coefficient-pair ratios. The lines are distinct because their directions differ. Thus their union has \(2p-1\) points. Multiplying by the \(p^{d-3}\) points per fiber proves all possible zero counts and the geometric description.

**6. All strata and sharpness.** The coefficient choices \((1,1,1,1)\), \((1,-1,i,-i)\), and \((1,1,-1,-1)\) have respectively zero, one, and two feasible matchings, for every odd prime \(p\). In the second choice, \(i\notin\mu_p\cup(-\mu_p)\). These witnesses realize exactly \(0\), \(p\), and \(2p-1\) local zeros. In the two-matching stratum, after multiplying by a common phase and individual \(p\)-th-root phases and permuting the sites, the coefficients are exactly \((1,1,-1,-1)\). The equality classification and sharp Fourier-support bound follow.

## Verification
A standalone Python 3 checker `artifacts/verify.py` evaluates the local Fourier polynomial on exact cyclotomic grids independently of the matching-line proof. Terms \(i^r\omega^s\) are accumulated as Gaussian-integer coefficient vectors modulo \(1+T+\cdots+T^{p-1}\); no floating-point cancellation threshold is used. It exhausts normalized sign-phase coefficients with arbitrary \(p\)-th-root shifts for \(p=5,7\), exhausts quarter-turn coefficient choices for \(p=5,7,11\), samples reproducible mixed phase configurations, and verifies the three explicit witnesses. Executing `python3 artifacts/verify.py` on the delivered source gives `FINITE_CYCLOTOMIC_CHECKS_PASS 5271`. The infinite families are proved by Steps 1–6; finite verification is supplementary.

## Relationship to prior work
Li's 2026 finite-parabola zero theorem studies support on a quadratic curve in \(\mathbb F_p^2\), where four sites are necessarily affinely dependent in the present three-direction sense. Its four-term bound and parabolic line-rigidity mechanism do not imply the phase-only affine-rank-three zero spectrum here. The later complete-MUB presentation is the same motivating work, not a second independent source.

A published exact Fourier-support spectrum for the ternary affine \(3\)-simplex gives all complex-coefficient possibilities for \(p=3\) only. The present theorem is stated for every prime \(p\ge5\), and its stronger phase-only classification in those characteristics is not implied by that finite ternary result. A published flat four-point finite-parabola theorem distinguishes symmetric supports, and a phase-only four-point rectangle theorem uses a rank-two Cartesian parallelogram. Their full available statements were inspected. Neither covers the affine-independent rank-three simplex. Bonami–Ghobber analyze minimum-support uncertainty in rank-two prime groups, while Delvaux–Van Barel analyze rank-deficient Fourier-matrix subblocks more broadly; neither inspected statement supplies this phase-only three-stratum classification.

## Limitations
The result requires exactly four nonzero **equal-modulus** coefficients, odd prime characteristic and affine rank three. It does not classify arbitrary coefficients, composite residue rings, or support sets of affine rank below three. The antipodal four-unit lemma is classical elementary geometry; the claimed contribution is the complete, all-prime Fourier-zero spectrum and affine-zero-set rigidity for this fixed nonplanar geometry. Unidentified older Fourier-matrix or phase-code literature may contain an equivalent matching formulation; no priority beyond the inspected sources is asserted. Independent validation has not been performed.

## References
1. Dongwei Li, *Parity-Sensitive Fourier Uncertainty and Zero-Set Rigidity on the Finite Parabola*, arXiv:2609.16030v1, first publicly posted 11 September 2026. https://arxiv.org/abs/2609.16030
2. Aline Bonami and SaifAllah Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060v2, originally posted 26 March 2010. https://arxiv.org/html/1003.5060v2
3. Steven Delvaux and Marc Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, Linear Algebra and its Applications 426 (2007), 349–367. DOI: 10.1016/j.laa.2007.05.009.
4. *Fourier-support spectrum of a ternary affine 3-simplex*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-fourier-support-spectrum-of-a-ternary-affine-3-simplex--3a5760f6b057
5. *Flat four-point finite-parabola Fourier zeros: a prime-field symmetry dichotomy*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-flat-four-point-finite-parabola-fourier-zeros-a-prime-field-symm--c2e3015b14a6
6. *Phase-only Fourier-zero spectrum of a four-point rectangle on cyclic product groups*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-phase-only-fourier-zero-spectrum-of-a-four-point-rectangle-on-cy--b51ecb1779fe
