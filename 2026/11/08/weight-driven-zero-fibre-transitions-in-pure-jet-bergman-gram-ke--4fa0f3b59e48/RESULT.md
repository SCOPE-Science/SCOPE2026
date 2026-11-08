# Weight-driven zero-fibre transitions in pure-jet Bergman Gram kernels

## Finding
For every real \(\beta>0\) and integer \(m\ge1\), equip the unit disk \(\mathbb D\) with the probability measure
\[
d\nu_\beta(z)=\frac{\beta}{\pi}(1-|z|^2)^{\beta-1}\,dA(z).
\]
The reproducing kernel of this weighted Bergman space is \(K_\beta(z,w)=(1-z\overline w)^{-\beta-1}\). Let \(B_{m,\beta}\) be the canonical Gram kernel of the functionals \(f\mapsto f^{(m)}(z)/m!\). Put \(t=z\overline w\). Then
\[
B_{m,\beta}(z,w)=\frac{(\beta+1)_m}{m!}\frac{Q_{m,\beta}(t)}{(1-t)^{\beta+2m+1}},\qquad
Q_{m,\beta}(t)=\sum_{j=0}^m\binom mj\binom{m+\beta}j t^j.
\]
Here \((a)_m=a(a+1)\cdots(a+m-1)\), and \(\binom{u}{j}=u(u-1)\cdots(u-j+1)/j!\). All \(m\) roots of \(Q_{m,\beta}\) are distinct, real and negative, and they move strictly toward zero as \(\beta\) increases. Exactly those roots lying in \((-1,0)\) produce attainable, pairwise distinct zero fibres \(\{(z,w)\in\mathbb D^2:z\overline w=t\}\).

For \(m\ge2\), define the **weight-transition polynomial**
\[
T_m(\beta)=\sum_{j=0}^m(-1)^j\binom mj\binom{m+\beta}j.
\]
It has exactly \(\lfloor m/2\rfloor\) distinct simple **positive** real roots \(0<\beta_{m,1}<\cdots<\beta_{m,\lfloor m/2\rfloor}\). The exact number of attained scalar zero fibres is
\[
\boxed{\ Z_m(\beta)=\left\lceil\frac m2\right\rceil+\#\{j:\beta_{m,j}<\beta\}.\ }
\]
Equality at a threshold does **not** count the newly entering fibre: at that parameter its scalar root is \(t=-1\), which is inaccessible to two points of the open disk. For \(m=1\), \(Z_1(\beta)=1\) for every \(\beta>0\). For example,
\[
\beta_{2,1}=\frac{1+\sqrt {17}}2,\qquad
\beta_{3,1}=\frac{3+\sqrt {73}}2.
\]
Thus raising the weight eventually brings *all* \(m\) scalar zeros into the bidisk, through exactly \(\lfloor m/2\rfloor\) distinct phase transitions.

These transitions have a **sharp universal large-order boundary**. For \(m\ge2\) write \(\beta_m^*=\beta_{m,\lfloor m/2\rfloor}\), the final transition. Then
\[
\boxed{\ \lim_{m\to\infty}\frac{\beta_m^*}{m}=2+2\sqrt2.\ }
\]
Equivalently, for each fixed \(c>0\), the smallest zero of \(P_m^{(0,cm)}\) tends to
\[
\boxed{\ h(c)=\frac{c^2-4c-4}{(c+2)^2}.\ }
\]
For every fixed \(\varepsilon>0\), sufficiently large \(m\) have all \(m\) zero fibres accessible when \(\beta\ge(2+2\sqrt2+\varepsilon)m\), whereas at least one scalar zero remains inaccessible when \(0<\beta\le(2+2\sqrt2-\varepsilon)m\), provided the latter right-hand side is positive.

At fixed \(m\), the high-weight locations have a second, universal limit. If \(\ell_{m,1},\ldots,\ell_{m,m}\) are the positive simple zeros of the ordinary Laguerre polynomial \(L_m\), the scalar roots can be labelled so that
\[
t_{m,j}(\beta)=-\frac{\ell_{m,j}}\beta+O_m(\beta^{-2})\qquad(\beta\to\infty).
\]

## Assumptions and scope
The measure normalization is part of the theorem. The derivatives are ordinary complex derivatives, normalized by \(m!\); the corresponding Gram kernel is \((m!)^{-2}\partial_z^m\partial_{\overline w}^m K_\beta(z,w)\). The weighted norm is induced by \(d\nu_\beta\), and \(\beta>0\) is arbitrary real, not necessarily integer. All zero counts concern distinct scalar products \(z\overline w\), not the uncountable cardinality of the full two-variable zero set. A scalar \(t\) is attained exactly when \(|t|<1\). At \(m=0\) the kernel is the classical weighted kernel, which is zero-free. The large-order limit concerns \(m\to\infty\) with the ratio \(\beta/m\) fixed and positive; the Laguerre limit instead fixes \(m\) and lets \(\beta\to\infty\).

## Proof
**Step 1: exact normalization and hypergeometric reduction.** The monomials have squared norms \(\|z^k\|^2=k!/(\beta+1)_k\), by the beta integral. Thus
\[
K_\beta(z,w)=\sum_{k\ge0}\frac{(\beta+1)_k}{k!}(z\overline w)^k=(1-z\overline w)^{-\beta-1}.
\]
Differentiating the convergent series \(m\) times in each variable gives
\[
B_{m,\beta}(z,w)=\frac{(\beta+1)_m}{m!}
{}_2F_1(\beta+m+1,m+1;1;t).
\]
Euler's hypergeometric transformation with these arguments converts the right side into \((1-t)^{-\beta-2m-1}{}_2F_1(-m,-m-\beta;1;t)\). The terminating series equals \(Q_{m,\beta}(t)\), proving the displayed kernel formula with no omitted normalization.

**Step 2: Jacobi correspondence and accessible roots.** Let \(J_m^{(\beta)}(x)=P_m^{(0,\beta)}(x)\), with the standard Jacobi normalization. Pfaff's finite transformation gives
\[
Q_{m,\beta}(t)=(1-t)^m J_m^{(\beta)}\!\left(\frac{1+t}{1-t}\right).
\]
The Jacobi polynomial is orthogonal on \((-1,1)\) for the strictly positive weight \((1+x)^\beta\), so it has \(m\) distinct roots in that interval. The inverse Cayley map \(t=(x-1)/(x+1)\) takes these to \((-\infty,0)\), preserving simplicity. It takes \(x>0\) to \(-1<t<0\) and \(x=0\) to \(t=-1\). Every \(t\in(-1,0)\) is realized by \(z=\sqrt{-t}\), \(w=-\sqrt{-t}\). Therefore the number of zero fibres equals the number of strictly positive Jacobi roots.

**Step 3: strict motion of every zero as the weight changes.** Here is a direct proof, so the parameter-monotonicity claim does not rely on finite experiments. Normalize \(J_m^{(\beta)}\) to a monic polynomial \(p(x,\beta)\), with ordered simple roots \(x_1(\beta)<\cdots<x_m(\beta)\). At a fixed parameter put \(q_i(x)=p(x,\beta)/(x-x_i)\). The polynomials \(q_i\) are pairwise orthogonal for the measure \(w_\beta(x)dx=(1+x)^\beta dx\), since for \(i\ne j\), \(q_iq_j=p(q_i-q_j)/(x_i-x_j)\) and \(\deg(q_i-q_j)\le m-2\). Differentiating \(\int p q_i w_\beta=0\), taking \(q_i\) fixed at the differentiation parameter, and using monicity gives \(\partial_\beta p=-\sum_j x_j'(\beta)q_j\). Orthogonality then yields
\[
x_i'(\beta)=\frac{\displaystyle\int_{-1}^1(x-x_i)q_i(x)^2\bigl[\log(1+x)-\log(1+x_i)\bigr](1+x)^\beta dx}{\displaystyle\int_{-1}^1q_i(x)^2(1+x)^\beta dx}>0.
\]
The numerator is strictly positive, because both factors in square brackets and \(x-x_i\) have the same sign for \(x\ne x_i\). Hence every Jacobi root moves strictly right, and every scalar zero \(t=(x-1)/(x+1)\) moves strictly toward zero.

**Step 4: exactly all transitions, with no hidden boundary cases.** At \(\beta=0\), \(J_m^{(0)}\) is the Legendre polynomial, whose roots are symmetric: \(m/2\) positive when \(m\) is even, and \((m-1)/2\) positive plus the single root zero when \(m\) is odd. The strict derivative above shows that for \(\beta>0\) sufficiently small there are exactly \(\lceil m/2\rceil\) positive roots. The finite Jacobi binomial expansion implies
\[
\beta^{-m}P_m^{(0,\beta)}(x)\longrightarrow \frac{(x-1)^m}{2^m m!}
\]
coefficientwise as \(\beta\to\infty\). Hence every root eventually lies in \((0,1)\). Each remaining negative root crosses zero exactly once by strict monotonicity; roots never coincide. Since \(2^mP_m^{(0,\beta)}(0)=Q_{m,\beta}(-1)=T_m(\beta)\), there are precisely \(\lfloor m/2\rfloor\) positive transition roots of \(T_m\). Each is simple as a root *in the parameter*, because the crossing derivative \(x_i'(\beta)\) and \(\partial_xP_m^{(0,\beta)}(0)\) are both nonzero there. The asserted exact count, including equality cases, follows.

**Step 5: sharp final-transition scale.** The Jacobi polynomial \(P_m^{(0,\beta)}\) is the characteristic polynomial, up to a positive multiplier, of the symmetric tridiagonal \(m\times m\) Jacobi matrix with rows indexed by \(j=0,\ldots,m-1\), diagonal entries and adjacent off-diagonals
\[
d_j=\frac{\beta^2}{(2j+\beta)(2j+\beta+2)},\quad
a_j=\frac{2j(j+\beta)}{(2j+\beta)\sqrt{(2j+\beta)^2-1}}\quad(1\le j\le m-1).
\]
Set \(a_0=a_m=0\). These are the standard orthonormal Jacobi three-term recurrence coefficients (also verified independently in `CHECK.py`). Fix \(c>0\) and take \(\beta=cm\). Uniformly for \(s=j/m\in[0,1]\),
\[
d_j\to d(s)=\frac{c^2}{(2s+c)^2},\qquad a_j\to a(s)=\frac{2s(s+c)}{(2s+c)^2},
\]
with the appropriate zero off-diagonals at the matrix endpoints. Gershgorin's lower bound gives
\[
\liminf_{m\to\infty}\lambda_{\min}\ge \min_{0\le s\le1}\bigl[d(s)-2a(s)\bigr]
=\frac{c^2-4c-4}{(c+2)^2}=h(c).
\]
The equality uses the strict decrease of \(d(s)-2a(s)=1-8s(s+c)/(c+2s)^2\) in \(s\) when \(c>0\). For the reverse inequality, restrict a Rayleigh vector to the last \(L_m\) coordinates, where \(L_m\to\infty\) and \(L_m/m\to0\), and choose the alternating sine vector for the constant tridiagonal matrix with entries \(d(1)\) and \(a(1)\). Its Rayleigh quotient is \(d(1)-2a(1)\cos(\pi/(L_m+1))+o(1)\), giving \(\limsup\lambda_{\min}\le h(c)\). This proves the displayed limiting smallest Jacobi root.

The function \(h(c)\) changes sign exactly once for \(c>0\), at \(c_*=2+2\sqrt2\). The smallest Jacobi root is strictly increasing in \(\beta\) for each fixed \(m\), and its unique zero at \(\beta_m^*\) is the last transition. For every \(0<c_-<c_*<c_+\), the limiting signs imply \(c_-m<\beta_m^*<c_+m\) for all sufficiently large \(m\). Letting \(c_-\uparrow c_*\) and \(c_+\downarrow c_*\) establishes \(\beta_m^*/m\to c_*\). Monotonicity extends the same conclusion to the uniform inequalities in the statement.

**Step 6: fixed-order high-weight localization.** The hypergeometric formula \(P_m^{(0,\beta)}(1-2u/\beta)={}_2F_1(-m,m+\beta+1;1;u/\beta)\) converges coefficientwise to \({}_1F_1(-m;1;u)=L_m(u)\). All Laguerre roots are simple and positive, so finite-polynomial perturbation gives \(u=\ell_{m,j}+O_m(\beta^{-1})\). Substitution into the inverse Cayley map gives \(t=-\ell_{m,j}/\beta+O_m(\beta^{-2})\), as asserted.

## Verification
Run `python CHECK.py` with the versions specified in `requirements.txt`. The standalone script checks the exact terminating hypergeometric/Jacobi identity for \(0\le m\le10\) at multiple rational weights, compares independently differentiated kernels for \(1\le m\le6\), evaluates all threshold counts for \(2\le m\le13\), cross-checks the tridiagonal Jacobi spectrum against an independent root routine, and probes the two asymptotic regimes. It completed with `CHECK_OK 383 assertions`. These finite validations are sanity checks; the all-order transition count, high-order constant and fixed-order scaling are proved analytically above.

## Relationship to prior work
Gehlawat, Jain and Sarkar (first public submission August 13, 2026, arXiv:2608.13193) introduce the canonical Gram kernel for general differential evaluations and study explicit upper-half-plane examples. The previously published note *Exact zero fibres of pure-jet Bergman Gram kernels on the disk* (published-finding corpus, October 11, 2026, identifier `98259fe7e47b`) treats the **unweighted** case \(\beta=1\), finding \(\lceil m/2\rceil\) attainable fibres. This is the \(\beta=1\) special case of the present formula, not a new subclaim. Classical Jacobi theory supplies orthogonality, the recurrence and the Jacobi-to-Laguerre limit; its general varying-parameter extreme-zero theory also provides context for the large-order boundary. The present contribution is the complete **weight-dependent kernel-zero phase diagram**, including the precise finite algebraic transitions, treatment of boundary exclusions, and their sharp weight-to-jet-order interpretation. No claim of inventing Jacobi theory or the general derivative representation is made.

## Limitations
This result concerns pure equal-order derivative functionals on the radial power-weighted disk. It does not classify mixed-jet sequences, general radial weights, or all zeros of multivariable ball kernels. For fixed \(m\), the transition roots are characterized as zeros of explicit degree-\(m\) polynomials; no uniform radicals expression is asserted. The large-order result is leading order, not an Airy-type correction. The polynomial facts have classical precedents, so the main originality question is the completeness of their application to weighted Bergman jet zero fibres.

## References
1. Sahil Gehlawat, Aakanksha Jain and Amar Deep Sarkar, *A Canonical Positive Definite Kernel Associated with the ξ-Bergman Kernel*, arXiv:2608.13193v1 (August 13, 2026), especially §§2–4. https://arxiv.org/html/2608.13193
2. *Exact zero fibres of pure-jet Bergman Gram kernels on the disk*, published-finding corpus published mathematical note (October 11, 2026), identifier `98259fe7e47b`.
3. NIST Digital Library of Mathematical Functions, §§18.5, 18.9, 18.16, Jacobi polynomial representation, recurrence and zero theory. https://dlmf.nist.gov/18
4. D. K. Dimitrov and F. R. Rafaeli, *Monotonicity of zeros of Jacobi polynomials*, Journal of Approximation Theory 149 (2007), 15–29; strict monotonicity is reproved here for this one-parameter family.
5. D. S. Moak, E. B. Saff and R. S. Varga, *On the zeros of Jacobi polynomials with varying parameters*, Transactions of the AMS 249 (1979), 159–162; classical background on extreme-zero asymptotics.
