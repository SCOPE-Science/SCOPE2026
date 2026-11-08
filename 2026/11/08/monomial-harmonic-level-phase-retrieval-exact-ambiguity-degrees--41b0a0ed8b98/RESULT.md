# Monomial harmonic-level phase retrieval: exact ambiguity degrees and a linear-sampling hierarchy

## Finding

Fix an integer \(n\ge2\) and nonzero real \(c\). Let
\[
\Gamma_c=\{z\in\mathbb C:\operatorname{Im}(z^n)=c\}.
\]
For two nonzero complex polynomials whose magnitudes agree on any nonempty open real-analytic arc of \(\Gamma_c\), the reduced rational quotient has **exactly** the form
\[
\frac{p(z)}{q(z)}=\xi\prod_{j=1}^{k}\frac{z^n-\alpha_j}{z^n-(\overline{\alpha_j}+2ic)},
\qquad |\xi|=1,
\]
where \(k\ge0\), \(\operatorname{Im}\alpha_j\ne c\), and the product is reduced (no numerator root coincides with any denominator root). Conversely, each such product arises from a polynomial pair with equal magnitudes on \(\Gamma_c\). A nonconstant quotient necessarily has rational-map degree \(nk\), and every positive multiple of \(n\) occurs. Thus the complete one-level data recover every polynomial of degree at most \(d\) up to one unimodular scalar if and only if \(d<n\).

Two distinct nonzero levels \(c_1\ne c_2\) **always** give phase uniqueness for *every* finite polynomial degree. In contrast, a single level has the explicit degree-\(n\) obstruction. This is a sharp one-versus-two-level transition.

For pairwise-distinct nonzero real levels \(c_1,\ldots,c_L\) and degree cutoff \(d\ge0\), the real dimension of the vector space of all complete polynomial intensity profiles on their union is
\[
D_L=(d+1)^2-\bigl(\max\{0,d-nL+1\}\bigr)^2.
\]
The number \(D_L\) is the exact minimum of point evaluations required for **real-linear reconstruction of all such intensity profiles**, not a proven minimum for nonlinear phase retrieval. Let \(D_0=0\). For any prescribed nonempty open arcs, one on each curve, there exist—and an open dense full-measure set of choices gives—an optimal arrangement taking exactly \(D_\ell-D_{\ell-1}\) points from the \(\ell\)-th arc. Complete Hermitian coefficient-matrix recovery holds precisely when \(nL>d\), so the exact least number of distinct levels for full lifting is \(\lfloor d/n\rfloor+1\). In particular, for \(d\ge2n\), two levels recover every polynomial up to phase even though they do **not** linearly identify all Hermitian coefficient matrices.

## Assumptions and scope

All polynomials have coefficients in \(\mathbb C\). The levels are real, nonzero and pairwise distinct; the zero-level union of intersecting straight lines is not part of the assertion. Each available arc is nonempty and open in the real-analytic topology of its level curve. The curves are smooth because \(z^n\ne0\) wherever its imaginary part is nonzero. Equalities on arcs are exact. The polynomial degree cutoff is an upper bound; zero polynomials are handled separately and cause no ambiguity. For a rational function, degree means the maximum of its reduced numerator and denominator degrees.

## Proof

**1. Irreducibility and continuation from an arc.** Introduce independent complex variables \(Z,W\) and
\[
F_c(Z,W)=Z^n-W^n-2ic.
\]
Choose any \(z_0\) satisfying \(z_0^n=2ic\). Since \(c\ne0\), the root \(z_0\) is simple. Viewed as a polynomial in \(W\) over the principal ideal domain \(\mathbb C[Z]\), \(-F_c\) is Eisenstein at the prime \(Z-z_0\): its constant coefficient has exactly one such factor, its intermediate coefficients vanish, and the leading coefficient is a unit. Therefore \(F_c\) is irreducible in \(\mathbb C[Z,W]\). Every real point \((z,\overline z)\) with \(z\in\Gamma_c\) lies on \(F_c=0\). An open real-analytic arc is an infinite subset of this irreducible algebraic curve. Since two coprime plane polynomials intersect in only finitely many affine points (or by restricting to a local holomorphic parameter and the identity theorem), every polynomial vanishing on such an arc is divisible by \(F_c\).

**2. The quotient is forced through the monomial.** Define \(h^*(W)=\overline{h(\overline W)}\) for polynomials or rational functions. If nonzero polynomials \(p,q\) have equal moduli on an arc, then
\[
p(Z)p^*(W)-q(Z)q^*(W)=0\quad\text{modulo }F_c.
\]
In the function field \(K=\operatorname{Frac}(\mathbb C[Z,W]/(F_c))\), put \(R=p/q\). Both denominators are nonzero as rational functions in \(K\), hence \(R(Z)R^*(W)=1\). For each \(n\)-th root of unity \(\zeta\), the transformation \(W\mapsto\zeta W\) fixes \(Z\) and preserves \(F_c\); applying it gives \(R^*(W)=R^*(\zeta W)\). Because the injection \(\mathbb C(W)\hookrightarrow K\) is faithful, this is an identity of rational functions of \(W\). The invariant field of the rotation \(W\mapsto\zeta W\), for primitive \(\zeta\), is \(\mathbb C(W^n)\). Consequently \(R(Z)=H(Z^n)\) for a rational \(H\).

With \(U=Z^n\) and \(W^n=U-2ic\), the earlier identity becomes
\[
H(U)H^*(U-2ic)=1.
\]
At infinity this forces \(H\) to have equal numerator and denominator degrees and unimodular leading-coefficient ratio. Every finite zero \(\alpha\) is paired, with the same multiplicity, with the pole \(\overline\alpha+2ic\). A zero on the line \(\operatorname{Im}\alpha=c\) would cancel its own pole and cannot occur in a reduced quotient. Thus \(H\) has precisely the displayed product factorization. Conversely, each factor is unimodular for \(\operatorname{Im}U=c\), and multiplying by a common polynomial if desired yields polynomial representatives. Since a reduced factorization of \(H\) of degree \(k\) pulls back to a reduced rational function of degree \(nk\), the possible positive ambiguity degrees are exactly \(n,2n,3n,\ldots\). The smallest nontrivial example is \(p(z)=z^n-\alpha\), \(q(z)=z^n-(\overline\alpha+2ic)\), with \(\operatorname{Im}\alpha\ne c\). This proves the sharp degree-\(d\) one-level uniqueness criterion.

**3. A second distinct level destroys every rational ambiguity.** Suppose the same \(p,q\) have equal moduli on arcs in two levels \(c_1\ne c_2\). From the first, \(R=H(z^n)\); from each, the rational function \(H\) obeys
\[
H(U)H^*(U-2ic_j)=1,\qquad j=1,2.
\]
It follows that \(H^*\) has the nonzero period \(2i(c_1-c_2)\). A rational function with a nonzero period is constant: a pole would generate infinitely many poles, and a pole-free rational function is polynomial, whose top-degree term excludes a nonzero period unless it is constant. The constant must be unimodular. Hence \(p=\xi q\) for \(|\xi|=1\). Additional levels preserve this conclusion.

**4. Exact Hermitian restriction kernel.** Let \(\mathsf H_d\) be the real vector space of polynomials \(A(Z,W)\) with \(\deg_Z A,\deg_W A\le d\) and \(A^*(Z,W):=\overline{A(\overline W,\overline Z)}=A(Z,W)\). It has real dimension \((d+1)^2\), and the real span of \(p(Z)p^*(W)\) for \(\deg p\le d\) is all of \(\mathsf H_d\) by polarization. An element vanishes on the selected arcs if and only if it is divisible by every \(F_{c_j}\), hence by
\[
T_L(Z,W)=\prod_{j=1}^L(Z^n-W^n-2ic_j).
\]
The factors are pairwise coprime because their differences are nonzero constants. Also \(T_L^*=(-1)^LT_L\). Writing \(A=T_LB\), the multiplier must satisfy \(B^*=(-1)^LB\). Since \(T_L\), considered as a polynomial in either \(Z\) or \(W\), has degree \(nL\) and a nonzero leading coefficient, no leading-term cancellation can decrease \(\deg_Z\) or \(\deg_W\) in the product. Thus \(\deg_Z B,\deg_W B\le d-nL\). When \(d<nL\), the multiplier must vanish. Otherwise the multiplier space (Hermitian or anti-Hermitian according to parity) has real dimension \((d-nL+1)^2\). Rank–nullity gives \(D_L\) exactly. Full Hermitian lifting is equivalent to \(nL>d\).

**5. Sharp layerwise finite interpolation.** For \(L=0\), define \(D_0=0\). Suppose the first \(\ell-1\) layers have been sampled with a kernel equal to the polynomials vanishing on those curves. Its restriction to the \(\ell\)-th arc has dimension \(D_\ell-D_{\ell-1}\). The restricted functions are real analytic and linearly independent on that arc, so their evaluation functionals span the dual: otherwise a nonzero function would vanish everywhere on the arc. Therefore one can choose exactly \(D_\ell-D_{\ell-1}\) distinct points on the arc with independent evaluations on this new subspace. The corresponding determinant is nonzero at one configuration and real analytic in the node parameters, so its nonzero locus is open, dense, and full measure. Induction yields an optimal total of \(D_L\) point evaluations with the specified allocation. Conversely, fewer than \(D_L\) real point evaluations cannot inject the entire \(D_L\)-dimensional profile space. This is a *linear profile* lower bound, not a general nonlinear phase-retrieval lower bound.

## Verification

The accompanying standalone `check_harmonic_levels.py` uses exact rational arithmetic and symbolic polynomial identities. Running `python check_harmonic_levels.py` prints `HARMONIC_LEVEL_PROFILE_CHECK_PASS exact_ranks=12 reflection_identities=5`. Its twelve rank checks concern the hyperbolic case \(n=2\), degrees \(1\) through \(4\), and the first one, two and three distinct nonzero levels. The five reflection checks include the exact general conjugate-root identity and the explicit ambiguity identity for \(n=2,3,4,5\). These tests corroborate the theorem but do not substitute for the irreducibility, rational-invariant, or dimension proofs above. No external tool or source data is needed for the checker beyond SymPy.

## Relationship to prior work

Wellershoff's paper on magnitude equality for finite-order entire functions on pairs of straight lines (arXiv:2202.03733, first public February 8, 2022) and Liehr's arithmetic-progression rigidity work (arXiv:2308.05722, first public August 10, 2023) explain reflection and translation phenomena for straight-line sampling. Their results concern analytic functions on lines, not the algebraic curve \(\operatorname{Im}(z^n)=c\) in the original signal variable. Chalendar and Partington (arXiv:2403.16255, first public March 24, 2024) analyze phase retrieval from circles and lines. The present statement additionally determines the entire rational-quotient classification on monomial harmonic-level curves, its divisibility spectrum, the exact lifting deficiency, and the layer-by-layer minimal *linear* profile sample allocation. Established circle, line, polynomial-graph and two-ray results are neither contradicted nor restated as new conclusions. No claim of independent bibliographic completeness is made.

## Limitations

The analysis requires monomial levels with a nonzero right-hand side; it does not classify general real algebraic curves or arbitrary polynomial pullbacks of lines. The generic finite designs specify exact counts and genericity, not universally well-conditioned points, a practical polynomial-time reconstruction algorithm, or the minimal number of nonlinear phase-retrieval samples. Independent validation and a complete historical-priority search remain open.

## References

- Matthias Wellershoff, *Phase retrieval of entire functions and its implications for Gabor phase retrieval*, arXiv:2202.03733v1 (2022-02-08), https://arxiv.org/abs/2202.03733.
- Lukas Liehr, *Arithmetic progressions and holomorphic phase retrieval*, arXiv:2308.05722v1 (2023-08-10), https://arxiv.org/abs/2308.05722.
- Isabelle Chalendar and Jonathan R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255v1 (2024-03-24), https://arxiv.org/abs/2403.16255.
