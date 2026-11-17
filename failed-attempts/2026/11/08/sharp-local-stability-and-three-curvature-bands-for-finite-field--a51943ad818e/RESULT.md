# Sharp local stability and three curvature bands for finite-field cubic-graph Fourier extension

## Finding

Let \(F\) be a finite field of odd characteristic different from three and order \(q\ge5\). Let \(e:F\to\mathbb C\) be a nontrivial additive character and define
\[
(Eg)(x,y)=q^{-1}\sum_{t\in F}g(t)e(xt+yt^3),\qquad
S(g)=\sum_{t\in F}|g(t)|^2,\qquad
Q(g)=q^2\sum_{(x,y)\in F^2}|Eg(x,y)|^4.
\]
Write \(D=2q+1\), \(m=(q-1)/2\), and \(C_q=3-6/D\). The sharp extension deficit is \(\Delta(g)=C_qS(g)^2-Q(g)\). Define an antipodal-pair representative set \(P\subset F^\times\), with precisely one of \(t,-t\) in \(P\). Put
\[
\alpha=|g(0)|^2,\quad r_t=|g(t)|^2+|g(-t)|^2,\quad
b_t=2|g(t)g(-t)|,\quad
w_0=g(0)^2,\quad w_t=2g(t)g(-t),\quad T=\alpha+\sum_{t\in P}b_t.
\]
Then **for every** \(g:F\to\mathbb C\), the following four-term identity holds:
\[
\boxed{\begin{aligned}
\Delta(g)={}&2\left(\alpha-\frac{3S}{D}\right)^2
+\frac32\sum_{t\in P}\left(r_t-\frac{4S}{D}\right)^2\\
&+\left(T^2-\left|w_0+\sum_{t\in P}w_t\right|^2\right)
+\sum_{t\in P}(r_t-b_t)\left(S+T-\frac{r_t+b_t}{2}\right).
\end{aligned}}
\]
Each term is nonnegative. Consequently, for \(S(g)=1\), its zero set is the smooth compact torus \(\mathcal M_q\) with the parametrization
\[
 g(0)=\sqrt{3/D}\,e^{i\theta},\qquad
 g(t)=\sqrt{2/D}\,e^{i(\theta+\varphi_t)},\qquad
 g(-t)=\sqrt{2/D}\,e^{i(\theta-\varphi_t)},\quad t\in P,
\]
where all angles are arbitrary real numbers modulo \(2\pi\).

The full real second variation of \(\Delta\) along this torus has **exactly three positive curvature levels**, each of multiplicity \(m\), and an \((m+2)\)-dimensional kernel. The positive coefficients of the quadratic Taylor term (half the eigenvalues of the usual real Hessian) are
\[
\boxed{\quad \frac{24}{2q+1},\qquad 4-\frac{8}{2q+1},\qquad4.\quad}
\]
Their eigendirections are, respectively, antipodally even real amplitude variations orthogonal to the extremizer, antipodally odd real amplitude variations, and antipodally even imaginary-phase variations orthogonal to the extremizer. The kernel consists exactly of radial scaling and tangent directions of \(\mathcal M_q\).

In particular, with Euclidean distance on \(\mathbb C^F\), the **sharp local stability constant** on the unit sphere \(S(g)=1\) is
\[
\boxed{\lim_{\eta\downarrow0}\inf_{\substack{S(g)=1\\0<\mathrm{dist}(g,\mathcal M_q)<\eta}}\frac{\Delta(g)}{\mathrm{dist}(g,\mathcal M_q)^2}=\frac{24}{2q+1}.}
\]
The weakest curvature decays as \(12/q\) as the field grows, while the other two remain bounded away from zero.

## Assumptions and scope

The ambient space \(F^2\) carries counting measure, the graph \(\{(t,t^3):t\in F\}\) carries normalized counting measure, and \(F\) has characteristic neither two nor three. This normalization makes \(\|Eg\|_{\ell^4(F^2)}^4=q^{-2}Q(g)\) and \(\|g\|_{L^2(C)}^4=q^{-2}S(g)^2\). All complex functions \(g\) are allowed. The distance in the local statement is the ordinary coefficient \(\ell^2\) distance and no quotient-by-phase convention is imposed: the entire extremizer torus is used.

## Proof

**Collision identity.** Additive-character orthogonality expresses \(Q(g)\) as the sum of \(g(a)g(b)\overline{g(c)g(d)}\) over ordered quadruples satisfying \(a+b=c+d\) and \(a^3+b^3=c^3+d^3\). For their common sum \(s\ne0\), the identity \(a^3+b^3=s^3-3abs\) forces \(ab=cd\), hence the unordered pairs agree. For \(s=0\), every pair \((t,-t)\) collides with every other such pair. Writing \(B=w_0+\sum_{t\in P}w_t=\sum_{t\in F}g(t)g(-t)\), direct counting gives
\[
Q(g)=2S^2-\sum_t|g(t)|^4-2\sum_t|g(t)|^2|g(-t)|^2+|g(0)|^4+|B|^2.
\]
Substitution of \(\alpha,r_t,b_t\) simplifies this exactly to
\[
Q(g)=2S^2-2\alpha^2-\sum_{t\in P}r_t^2-\frac12\sum_{t\in P}b_t^2+|B|^2.
\]

**Exact global deficit.** Weighted completion of squares gives
\[
2\alpha^2+\tfrac32\sum_t r_t^2-\tfrac6D S^2
=2(\alpha-3S/D)^2+\tfrac32\sum_t(r_t-4S/D)^2,
\]
using \(S=\alpha+\sum_t r_t\) and \(D=4m+3\). Moreover, since \(S-T=\sum_t(r_t-b_t)\),
\[
S^2-|B|^2-\tfrac12\sum_t(r_t^2-b_t^2)
=(T^2-|B|^2)+\sum_t(r_t-b_t)\left(S+T-\tfrac12(r_t+b_t)\right).
\]
Adding gives the boxed identity. The first two summands are squares, the third is nonnegative by the triangle inequality, and the fourth is nonnegative because \(r_t\ge b_t\), \(S\ge r_t\), and \(T\ge b_t\). For nonzero \(g\), the fourth vanishes precisely when the paired absolute values agree, the first two force their specified positive values, and the third forces each nonzero product \(g(t)g(-t)\) to align with \(g(0)^2\). This proves the torus description.

**Complete second variation.** Fix its positive real point \(h\), with \(h(0)=\sqrt{3/D}\) and \(h(t)=\sqrt{2/D}\) for \(t\ne0\); \(\|h\|_2=1\). In the real coefficient space, set
\[
H_e=\{u:u(t)=u(-t)\},\qquad H_o=\{u:u(t)=-u(-t)\},
\]
where \(H_o\) also has \(u(0)=0\). These are orthogonal subspaces of dimensions \(m+1\) and \(m\). For \(z=u+iv\), let \(u_e,u_o,v_e,v_o\) denote even and odd projections and let \(P_\perp\) be projection in \(H_e\) perpendicular to \(h\). Expanding the previous exact polynomial formula around \(h\) yields
\[
\boxed{\Delta(h+z)=\frac{24}{D}\|P_\perp u_e\|_2^2+
\left(4-\frac8D\right)\|u_o\|_2^2+4\|P_\perp v_e\|_2^2+O_q(\|z\|_2^3).}
\]
For reproducibility, one can expand \(S(h+z)\) to quadratic order, \(B(h+z)\) to quadratic order, and \(2|g(0)|^4+\sum_{t\in P}(|g(t)|^4+|g(-t)|^4+4|g(t)g(-t)|^2)\) to quadratic order in \(u,v\). The linear terms cancel. Their quadratic sum, before imposing a norm constraint, is exactly the displayed expression. In particular the phase-odd variations and global phase give zero; the radial real variation gives zero by homogeneity. The positive quadratic coefficients and multiplicities are therefore as stated. Every other extremizer is obtained from \(h\) by a diagonal unitary symmetry preserving \(\Delta\), so its Hessian is unitarily congruent to the one at \(h\).

**Sharp local distance constant.** The parametrization of \(\mathcal M_q\) is a smooth, compact embedded \((m+1)\)-torus in the sphere. Its real tangent at \(h\) is \(i(\mathbb Rh\oplus H_o)\). The normal tangent to the sphere decomposes into \((H_e\cap h^\perp)\oplus H_o\oplus i(H_e\cap h^\perp)\). For fixed \(q\), the uniform quadratic Taylor expansion in tubular coordinates and the strictly ordered positive levels (since \(D\ge11\)) imply the lower local ratio \(24/D\). Choosing a nonzero \(u\in H_e\cap h^\perp\), normalizing \(h+\varepsilon u\) to unit norm and sending \(\varepsilon\to0\) attains this limiting ratio. This proves sharpness.

## Verification

The standalone script `artifacts/verify.py` checks the collision formula, global deficit identity, exact Hessian quadratic form and spectral multiplicities for several prime fields. It compares the algebraic expression against independently assembled collision fibers and checks the predicted least-curvature limit. Run `python3 artifacts/verify.py` in an environment with SymPy. The script uses deterministic test data and includes its own normalization and assertions. A finite verifier does not establish the all-field theorem; the collision argument and identities above do.

## Relationship to prior work

González-Riquelme and Oliveira e Silva (arXiv:2405.16647v1, first public 2024-05-26) develop sharp finite-field extension inequalities, concentrating on the parabola at the sixth moment and quadratic surfaces at the fourth moment. They do not derive the cubic-graph local stability spectrum. Mockenhaupt and Tao (arXiv:math/0204234v1) provide the extension normalization and general convolution bounds, not the present curvature classification. Hughes and Wooley (arXiv:1911.12262v1) consider the same formal curve over truncated integers, predominantly at tenth moments, with the same zero-sum algebra but a different operator and objective.

A public earlier note titled “Exact sharp finite-field cubic-graph \(L^2\) to \(L^4\) extension norm and extremizers” (published-finding corpus, 2026-10-04; identifier `2db777d1e47b`) determines \(C_q\) and all equality cases. The present result **takes that sharp norm as known context**, and adds an exact nonnegative global deficit identity, the complete three-band second variation with all kernel dimensions, and a sharp quantitative local stability coefficient. The inspected prior result contains no such second-variation or local-stability theorem. Thus the same sharp constant is not claimed as new.

## Limitations

The sharp stability conclusion is local, not an explicit global lower bound proportional to distance squared. Constants in the higher-order remainder may depend on \(q\); no uniform-in-field-size tubular neighborhood is asserted. Characteristic two and three are excluded. This is an all-finite-field analytic theorem proved algebraically; direct verification covers only selected prime fields. Historical novelty remains provisional because a more general unpublished perturbative stability theorem could imply the displayed spectrum.

## References

1. C. González-Riquelme and D. Oliveira e Silva, “Sharp extension inequalities on finite fields,” arXiv:2405.16647v1 (2024-05-26), https://arxiv.org/abs/2405.16647.
2. G. Mockenhaupt and T. Tao, “Restriction and Kakeya phenomena for finite fields,” arXiv:math/0204234v1 (2002-04-18), https://arxiv.org/abs/math/0204234.
3. K. Hughes and T. D. Wooley, “Discrete restriction for \((x,x^3)\) and related topics,” arXiv:1911.12262v1 (2019-11-27), https://arxiv.org/abs/1911.12262.
4. “Exact sharp finite-field cubic-graph \(L^2\) to \(L^4\) extension norm and extremizers,” published-finding corpus, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-sharp-finite-field-cubic-graph-l-2-to-l-4-extension-norm-a--2db777d1e47b.
