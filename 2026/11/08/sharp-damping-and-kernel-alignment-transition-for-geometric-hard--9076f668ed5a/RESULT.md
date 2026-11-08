# Sharp damping and kernel-alignment transition for geometric Hardy shifts

## Finding

Let \(H^2(\mathbb D)\) be the complex Hardy space, and for \(0\le\beta<1\) let \(S_\beta f(z)=z f(\beta z)\). For \(0<q\le1\), take normalized Szegő kernels \(\widehat k_a(z)=\sqrt{1-|a|^2}/(1-\overline a z)\), and define
\[
\operatorname{Ber}_q(S_\beta)=\{\langle S_\beta\widehat k_a,\widehat k_b\rangle:\ a,b\in\mathbb D,\ \langle\widehat k_a,\widehat k_b\rangle=q\},
\qquad R_q(\beta)=\sup\{|z|:z\in\operatorname{Ber}_q(S_\beta)\}.
\]
Put \(k=\sqrt{1-q^2}\). There is exactly one \(u=u(q,\beta)\in(0,1)\) satisfying
\[
1-(3-\beta)u^2+2(1-\beta)ku^3+\beta u^4=0.
\]
The full range is the **closed** disk \(\{z:|z|\le R_q(\beta)\}\), where the radius is explicitly determined by that unique quartic root:
\[
\boxed{R_q(\beta)=\frac{q u(1-u^2)}{1-\beta u^2-(1-\beta)ku}.}
\]
Up to a common rotation, every maximizing ordered kernel pair is precisely
\[
\boxed{b=u,\qquad a=\frac{u-k}{1-ku}.}
\]
In particular, the two kernel parameters are on opposite rays when
\(q<\sqrt{(1-\beta)/(2-\beta)}\), the first kernel is at the origin at equality, and the parameters lie on the same ray above this threshold.

There is also a sharp optimization *over the geometric damping itself*. At fixed \(0<q<1/\sqrt2\), the function \(\beta\mapsto R_q(\beta)\) decreases strictly up to
\[
\boxed{\beta_c(q)=\frac{1-2q^2}{1-q^2}}
\]
and increases strictly afterward. Its unique minimum is \(q\sqrt{1-q^2}\), attained at \(\beta_c(q)\). At \(q=1/\sqrt2\), the unique minimum remains \(q\sqrt{1-q^2}\) but occurs at \(\beta=0\). For \(1/\sqrt2<q\le1\), the radius increases strictly with \(\beta\), and the unique minimizing damping is \(\beta=0\). Consequently,
\[
\inf_{0\le\beta<1}R_q(\beta)=
\begin{cases}
q\sqrt{1-q^2},&0<q\le1/\sqrt2,\\
R_q(0),&1/\sqrt2<q\le1.
\end{cases}
\]

For each fixed \(0\le\beta<1\), the small-overlap expansion is
\[
\boxed{R_q(\beta)=\frac{2q}{1+\beta}-\frac{2\sqrt{(1-\beta)(3+\beta)}}{(1+\beta)^2}q^2+O_\beta(q^3)\quad(q\downarrow0).}
\]
At fixed \(0<q\le1\), the approach to the undamped boundary obeys
\[
\boxed{q-R_q(\beta)=q\sqrt{2(1-\sqrt{1-q^2})}\sqrt{1-\beta}+O_q(1-\beta)\quad(\beta\uparrow1).}
\]
The scalar radius and the qualitative fact that real-weighted shifts have disk-shaped \(q\)-Berezin ranges were previously considered; the asserted new result is the unique-root, sharp damping optimization, alignment transition, and asymptotic laws together.

## Assumptions and scope

All Hilbert spaces and inner products are complex, with the inner product linear in the first variable. The parameters satisfy \(0<q\le1\) and \(0\le\beta<1\). The operator is the unilateral weighted shift with weights \(1,\beta,\beta^2,\ldots\), equivalently \(S_\beta f(z)=zf(\beta z)\). It is bounded and compact for every \(\beta<1\), including the rank-one endpoint \(\beta=0\). For \(q=1\), the kernel constraint forces \(a=b\). The excluded undamped operator \(S_1=M_z\) has the known open \(q\)-Berezin disk of radius \(q\); our sharp formulas concern \(\beta<1\).

## Proof

**1. Complete kernel parameterization and domination.** Direct expansion of the two normalized kernels gives
\[
\langle\widehat k_a,\widehat k_b\rangle
=\frac{\sqrt{(1-|a|^2)(1-|b|^2)}}{1-\overline a b},\quad
\langle S_\beta\widehat k_a,\widehat k_b\rangle
=\frac{q(1-\overline a b)b}{1-\beta\overline a b}
\]
whenever the first expression equals positive real \(q\). Hence \(\overline a b\) is real: except when one parameter is zero, the pair lies on one line through the origin. Interchanging the two kernel parameters preserves the constraint and \(\overline a b\), but replaces the numerator factor \(|b|\) by \(|a|\). Thus a maximizing pair must have \(|b|\ge|a|\); if the inequality is strict in the opposite direction, interchange strictly increases the modulus. Rotate so that \(b=w\in[0,1)\) and \(a=r\in(-1,1)\). Solving the overlap equation yields the two branches
\[
r=\frac{w\pm k}{1\pm kw}.
\]
The plus branch has \(r>w\) when \(q<1\), so only
\[
r=\frac{w-k}{1-kw}
\]
is required for maximization; this branch is admissible for *every* \(0\le w<1\), whether or not \(|r|\le w\). Substitution gives
\[
\frac{q(1-rw)w}{1-\beta rw}
=F_{q,\beta}(w):=\frac{q w(1-w^2)}{D(w)},\qquad
D(w)=1-\beta w^2-(1-\beta)kw.
\]
The denominator is strictly positive for \(0\le w<1\), because \(D(w)=(1-w^2)\beta+(1-kw)(1-\beta)\). Every value of \(F_{q,\beta}\) is realized, and every kernel test is no larger in modulus than some such value. Common rotations give all arguments. Moreover \(F_{q,\beta}(0)=0\), \(F_{q,\beta}(w)>0\) for \(0<w<1\), and \(F_{q,\beta}(w)\to0\) as \(w\uparrow1\) for \(\beta<1\). Therefore the range is exactly the closed disk with radius \(\max F_{q,\beta}\).

**2. A unique global maximizer.** Differentiation produces
\[
F'_{q,\beta}(w)=\frac{qN(w)}{D(w)^2},\quad
N(w)=1-(3-\beta)w^2+2(1-\beta)kw^3+\beta w^4.
\]
Its derivative satisfies
\[
N'(w)=2w[-(3-\beta)+3(1-\beta)kw+2\beta w^2]<0
\quad(0<w<1),
\]
since the bracket is bounded above by \(-3(1-\beta)(1-k)<0\). Also \(N(0)=1\) and \(N(1)=-2(1-\beta)(1-k)<0\). Hence \(N\) has exactly one root \(u\) in \((0,1)\), and \(F\) strictly increases then strictly decreases there. To show that the maximizing ordered pair satisfies \(|b|>|a|\) when \(q<1\), note that the equality threshold \(|a|=|b|\) on the chosen branch is \(w=\eta=\sqrt{(1-q)/(1+q)}\), where \(k=2\eta/(1+\eta^2)\). Substitution yields
\[
N(\eta)=\frac{(1-\eta^2)^2(1+\beta\eta^2)}{1+\eta^2}>0.
\]
Thus \(u>\eta\), giving strict optimal output dominance and uniqueness of the ordered magnitudes. For \(q=1\), the constraint already gives \(a=b\). This proves the claimed complete maximizing-pair description.

**3. The alignment transition.** The exact identity
\[
N(k)=(1-k^2)[1-(2-\beta)k^2]
=q^2[(2-\beta)q^2-(1-\beta)]
\]
and the strict decrease of \(N\) imply that \(u-k\) has the sign of \((2-\beta)q^2-(1-\beta)\). The optimizing input \(a=(u-k)/(1-ku)\) therefore changes sign exactly at the claimed threshold.

**4. Optimize the damping.** The unique root depends smoothly on \(\beta\) by \(N'(u)<0\). The envelope derivative is
\[
\frac{\partial R_q}{\partial\beta}
=\frac{q u^2(1-u^2)(u-k)}{D(u)^2}.
\]
Its sign is exactly that of \((2-\beta)q^2-(1-\beta)\). For \(0<q<1/\sqrt2\), this affine expression in \(\beta\) crosses zero exactly once inside \((0,1)\), at \(\beta_c(q)=(1-2q^2)/(1-q^2)\). At this crossing \(u=k\), hence \(R_q(\beta_c)=F(k)=qk\). For larger \(q\), the derivative is positive for \(\beta>0\); the endpoint \(q=1/\sqrt2\) has its minimum at \(\beta=0\). These are all the cases.

**5. Boundary asymptotics.** For fixed \(\beta<1\), the exact factorization at \(k=1\) is
\[
N(w)\big|_{k=1}=(1-w)^2(\beta w^2+2w+1).
\]
With \(k=1-q^2/2+O(q^4)\), set \(w=1-cq\). Dividing \(N\) by \(q^2\) gives \((3+\beta)c^2-(1-\beta)+O(q)\). At its positive simple root, the implicit-function theorem yields
\[
u=1-\sqrt{\frac{1-\beta}{3+\beta}}\,q+O_\beta(q^2).
\]
Substituting into \(F_{q,\beta}(u)\) and expanding the rational expression gives the stated two-term formula for \(R_q(\beta)\). For fixed \(q>0\), write \(\varepsilon=1-\beta\). The quartic near \(w=1\) gives
\[
u=1-\sqrt{\frac{1-k}{2}}\sqrt\varepsilon+O_q(\varepsilon).
\]
The identity \(F_{q,1-\varepsilon}(w)=q w(1-w^2)/[(1-w^2)+\varepsilon w(w-k)]\) then yields the asserted square-root boundary law. All error estimates concern fixed indicated secondary parameters and follow from smooth algebraic expansions at simple rescaled roots.

## Verification

The standalone `check.py` uses only Python 3 standard-library arithmetic. It verifies symbolic polynomial identities with an exact multivariate rational-polynomial representation, checks the Szegő overlap and radius identities on rational parameter families, and exercises root localization, sign transitions, damping thresholds, and both asymptotic regimes. Run with `python3 check.py` from the directory containing this document. Its tests are finite consistency checks, not a proof by sampling. The infinite-domain uniqueness, order, and asymptotics are justified in the proof above.

## Relationship to prior work

Bhattacharya and Patra, *\(q\)-Berezin Range of Operators in Hardy Space* (arXiv:2601.02334, first submitted January 5, 2026), prove disk geometry for real-weighted Hardy shifts, specialize to the geometric weights \(\beta^n\), and express the radius as a maximum over two functions in Corollary 3.19 and Remark 3.20. Those starting formulas are prior work. The distinct assertions here are an exact one-root characterization, uniqueness and location of norming pairs, the sharp minimization over \(\beta\), and the two boundary expansions. Mahapatra et al., *\(q\)-Berezin sectorial operators with applications to \(q\)-Berezin number inequalities and \(q\)-Berezin ranges* (arXiv:2608.21723, first submitted August 22, 2026), study related operator inequalities and shifts on Bergman space rather than the present sharp Hardy geometric-shift damping problem. The sharp damping comparison does not follow merely from the known circular shape of the range.

## Limitations

No statement is made for complex geometric damping, for \(q=0\) (the Hardy normalized kernels have nonzero overlap), or for arbitrary weight sequences. The result at \(\beta=1\) is only used as a boundary comparison; its open disk is known. Originality is a best-knowledge literature comparison, not an independent publication-priority certification. The asymptotic error constants can depend on the fixed secondary parameter and are not claimed uniform up to the other singular endpoint. The exact mathematical claims have received self-review only; no independent mathematical audit has been performed.

## References

1. D. Bhattacharya and A. Patra, *\(q\)-Berezin Range of Operators in Hardy Space*, arXiv:2601.02334v1 (January 5, 2026), https://arxiv.org/abs/2601.02334; relevant full text v2: https://arxiv.org/html/2601.02334v2, especially Theorem 3.18, Corollary 3.19, Remark 3.20.
2. S. Mahapatra, S. Halder, R. Birbonshi, A. Patra, K. Paul, *\(q\)-Berezin sectorial operators with applications to \(q\)-Berezin number inequalities and \(q\)-Berezin ranges*, arXiv:2608.21723v1 (August 22, 2026), https://arxiv.org/abs/2608.21723, especially Section 3.
