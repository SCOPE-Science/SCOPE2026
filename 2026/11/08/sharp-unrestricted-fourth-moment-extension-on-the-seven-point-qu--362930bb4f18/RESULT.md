# Sharp unrestricted fourth-moment extension on the seven-point quartic graph

## Finding
Let \(F=\mathbb F_7\), \(\zeta=e^{2\pi i/7}\), and let \(f:F\to\mathbb C\) be arbitrary. Set
\[
(Tf)(u,v)=\sum_{t\in F}f(t)\zeta^{ut+vt^4},\qquad
S(f)=\sum_{t\in F}|f(t)|^2.
\]
With normalized counting measure on the 49 output frequencies and counting measure on the seven input indices, the exact sharp unrestricted fourth-moment inequality is
\[
\boxed{\frac1{49}\sum_{u,v\in F}|(Tf)(u,v)|^4\le\frac52 S(f)^2.}
\]
Write \(H=\{1,2,4\}\) and \(-H=\{3,5,6\}\). Every nonzero equality case, and no others, has the following form: choose exactly one of \(O\in\{H,-H\}\), a scalar \(c\in\mathbb C\setminus\{0\}\), and \(k\in F\); put
\[
f(0)=c,\qquad f(t)=c\zeta^{kt}\ (t\in O),\qquad f(t)=0\ (t\notin\{0\}\cup O).
\]
Thus there are exactly fourteen nonzero projective extremizers. Moreover the proof yields an exact sum of nonnegative squares and phase-alignment deficits for every complex input, not merely an upper bound.

## Assumptions and scope
The curve consists of all seven points \(C=\{(t,t^4):t\in\mathbb F_7\}\). No restriction is imposed on the support, amplitude, or phase of \(f\). The fourth output moment uses \(49^{-1}\sum_{u,v}\), and the input uses the unnormalized \(\ell^2\) norm. The zero function is a trivial equality case, excluded from the projective count. The theorem does not assert the same formula over larger fields or for other monomial exponents.

## Proof
**1. Exhaustive pair-sum structure.** Expanding the fourth moment and using additive-character orthogonality gives
\[
E(f):=\frac1{49}\sum_{u,v}|Tf(u,v)|^4
=\sum_{\substack{a+b=c+d\\a^4+b^4=c^4+d^4}}
 f(a)f(b)\overline{f(c)f(d)},
\]
with all equalities in \(F\). There are exactly six unordered-pair collisions beyond permutation, namely
\[
\{0,t\}\longleftrightarrow\{4t,4t\},\qquad t\in F^\times.
\]
Indeed fixing \(s=a+b=c+d\) and the two products \(P=ab\), \(Q=cd\), the power-sum identity \(a^4+b^4=s^4-4Ps^2+2P^2\) yields \((P-Q)(P+Q-2s^2)=0\). If \(P=Q\), the unordered pairs coincide. Otherwise \(P+Q=2s^2\) and both quadratic discriminants must be squares; direct residue substitution over the seven possible sums \(s\in F\) gives precisely the six pairs shown (including the case \(s=0\), where no nontrivial collisions occur). The reproducible exact enumerator checks the complete list of 28 unordered pairs, rather than sampling from it. Since \(4^3=1\pmod7\), these collisions form two disjoint three-cycles in \(F^\times\).

Each unordered unequal pair contributes two ordered pairs, whereas a diagonal pair contributes one. The collision identity, including permutation terms, is therefore exactly
\[
\boxed{E(f)=2S(f)^2-\sum_{t\in F}|f(t)|^4
+4\operatorname{Re}\sum_{t\in F^\times}f(0)f(t)\overline{f(4t)^2}.}\tag{1}
\]

**2. Global nonnegative deficit.** Put \(a=|f(0)|\), \(x_t=|f(t)|\), and \(B_O=\sum_{t\in O}x_t^2\) for \(O\in\{H,-H\}\). Write \(B=B_H+B_{-H}\) and \(S=a^2+B\). The exact identity
\[
\begin{aligned}
&\frac52 S^2-E(f)\\
&=2\sum_{t\ne0}x_{4t}^2(a-x_t)^2
+\frac23\sum_{O\in\{H,-H\}}\sum_{\{s,t\}\subset O}(x_s^2-x_t^2)^2\\
&\quad+\frac16(3a^2-B)^2+\frac23B_HB_{-H}\\
&\quad+4\sum_{t\ne0}\left(ax_tx_{4t}^2-\operatorname{Re}(f(0)f(t)\overline{f(4t)^2})\right)
\end{aligned}\tag{2}
\]
proves the claimed inequality since every summand is nonnegative. For completeness, expand the right side: for each three-cycle, every unordered pair \(\{s,t\}\subset O\) occurs exactly once in \(\sum_{t\in O}x_t^2x_{4t}^2\); the identity \(\sum_{\{s,t\}\subset O}(y_s-y_t)^2=3\sum_{t\in O}y_t^2-(\sum_{t\in O}y_t)^2\) then reduces the first four summands to \(\frac12S^2+a^4+\sum_{t\ne0}x_t^4-4a\sum_{t\ne0}x_t x_{4t}^2\). Adding the phase deficit and applying (1) gives (2) term by term. This is a purely algebraic identity valid for every complex \(f\).

**3. Exhaustive equality cases.** Suppose \(f\ne0\) and equality holds in (2). Its product term forces \(B_HB_{-H}=0\), so at most one nonzero orbit is populated. The squared-difference term forces equal nonzero magnitudes on that orbit, say \(x\); the scalar term forces \(3a^2=3x^2\), so \(a=x>0\). The first squared term is then zero automatically. The phase terms vanish precisely when
\[
 f(0)f(t)\overline{f(4t)^2}\in[0,\infty),\qquad t\in O.
\]
Dividing by the common nonzero scalar \(c=f(0)\), set \(f(t)/c=e^{i\beta_t}\). The three constraints say \(\beta_t\equiv2\beta_{4t}\pmod{2\pi}\). As \(4^3\equiv1\), they imply \(7\beta_t\equiv0\pmod{2\pi}\) and force exactly the seven choices \(f(t)/c=\zeta^{kt}\), \(k\in F\). Conversely every displayed input satisfies every equality constraint, with \(S=4|c|^2\) and \(E=40|c|^4\). Distinct orbits and distinct \(k\) have distinct projective classes. This proves sharpness and completeness.

## Verification
The standalone reproducible `artifacts/verify.py` enumerates all 49 ordered input pairs and their sum fibers, reconstructs all six nontrivial unordered collisions, and checks (1) on 1000 Gaussian-integer inputs. It checks the exact rational specialization of (2) on 1000 independent nonnegative rational magnitude vectors and directly evaluates each of the fourteen projective equality families. It additionally checks two exact indicator witnesses with \(E=40\) and \(S=4\). Successful replay reports `QUARTIC_SEVEN_SHARP_PASS exact_integer_and_rational_tests=1000 projective_extremizers=14 pair_fibers=22`. These finite calculations corroborate; the universal complex-coefficient inequality follows from the displayed algebraic identity and phase argument.

## Relationship to prior work
Mockenhaupt and Tao (2002) establish the finite-field Fourier restriction viewpoint and orthogonality mechanism. Existing published calculations for this *same quartic graph* determine its total additive energy and optimize the fourth moment on the multiplicatively invariant **two-dimensional coefficient subspace**, respectively; neither gives the unrestricted seven-variable norm or all its extremizers. A published general theorem for abelian difference sets already determines the sharp constant \(5/2\) on each four-point \((7,4,2)\) difference-set subcurve \(\{0\}\cup H\) and \(\{0\}\cup(-H)\). **That one-arm constant is prior work**, not claimed as new. The new point is global domination across their seven-point union, with strict mixed-arm loss quantified by \(\frac23B_HB_{-H}\), and the complete full-curve projective equality classification. A published linked-midpoint four-character theorem concerns cyclic character orders at least nine and therefore does not supply this order-seven union inequality.

## Limitations
The result is a natural, exact, finite-field boundary case rather than an all-field quartic extension theorem. It uses a very specific collision structure at field order seven. General results on unions of additive difference sets or hidden small-order cyclotomic convolution inequalities could conceivably imply the theorem; the literature comparison is bounded rather than an exhaustive priority guarantee. The numerical portion of the checker is not a substitute for the symbolic all-coefficient sum-of-squares proof.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234v1, first publicly submitted 2002-04-18, https://arxiv.org/abs/math/0204234.
2. *Exact additive energy of the finite-field quartic graph*, published 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-additive-energy-of-the-finite-field-quartic-graph--235f10989b3f.
3. *An arithmetic phase transition in the invariant quartic-curve Fourier norm*, published 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-arithmetic-phase-transition-in-the-invariant-quartic-curve-fo--ba1c8156001a.
4. *Sharp fourth-moment extension and exact deficit for finite abelian difference sets*, published 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-extension-and-exact-deficit-for-finite-abeli--f000b50fe5d9.
5. *Sharp fourth moments for linked-midpoint four-character spectra*, published 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moments-for-linked-midpoint-four-character-spectra--0b57c5d24021.
