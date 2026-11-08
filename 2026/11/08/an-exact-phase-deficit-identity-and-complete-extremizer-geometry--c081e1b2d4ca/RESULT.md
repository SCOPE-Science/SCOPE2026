# An exact phase-deficit identity and complete extremizer geometry for symmetric quadratic polynomials

## Finding
For the symmetric quadratic three-variable family
\[
P_s(z)=z_1^2+z_2^2+z_3^2-s(z_1z_2+z_2z_3+z_3z_1),\qquad s>2,
\]
there is an **exact global two-square phase-deficit identity** determining all equality configurations. This is a refinement in phase geometry and quantitative deficit of an already known sharp Schur–Agler norm-ratio computation; **the ratio itself is not a new finding**.

Choose any \((z_1,z_2,z_3)\in\mathbb T^3\). After a common unimodular rotation and a permutation, write \((z_1,z_2,z_3)=(e^{i\theta},e^{-i\theta},e^{i\phi})\) with \(0\le\theta\le\pi/2\). Set
\[
u=\cos\theta,\quad x=u^2,\quad v=\cos\phi,\quad A=4x-s-2,\quad v_*=\frac{su(A+1)}{2A},\quad H_s=\frac{(s-1)^3(s+2)}{s-2}.
\]
Then
\[
\boxed{H_s-|P_s(z)|^2=\frac{(s+2)(1-x)(s^2-4sx-s+8x-4)^2}{(s-2)(s+2-4x)}+4(s+2-4x)(v-v_*)^2.}
\]
Both terms are nonnegative for the stated range. At \(s_0=(1+\sqrt{17})/2\), and for every \(s\in[s_0,4]\), the exact supremum is
\[
\|P_s\|_{H^\infty(\mathbb D^3)}=\sqrt{H_s}.
\]
Every maximizing unimodular triple, up to permutation and common phase, is \((1,1,e^{i\alpha_s})\) or \((1,1,e^{-i\alpha_s})\), where \(\alpha_s\in[0,\pi]\) is specified uniquely by
\[
\cos\alpha_s=\frac{s(3-s)}{2(2-s)}.
\]
In particular the exact deficit identity quantitatively detects departures from the maximizing phases through two explicit nonnegative terms, uniformly throughout this parameter interval. No optimal metric-distance stability constant is claimed.

## Assumptions and scope
The polynomial is complex homogeneous of degree two; the parameter \(s\) is real and strictly larger than two. Torus reduction is valid because the polynomial is holomorphic in each variable and the maximum modulus principle reduces its supremum over the polydisk to the distinguished boundary. For phase-extremizer classification restrict \(s\) to the closed interval \([s_0,4]\). At its upper endpoint the two phases coincide, so the maximum occurs at the constant-phase triple.

## Proof
**Phase reduction.** Multiply the coordinates by a common phase to make two chosen unit-circle coordinates complex conjugate. If their smaller angular distance is at most \(\pi\), we can choose \(0\le\theta\le\pi/2\), and the third coordinate is \(e^{i\phi}\). Homogeneity preserves the modulus under common phase. The resulting quadratic is
\[
P_s(e^{i\theta},e^{-i\theta},e^{i\phi})=e^{2i\phi}-2su\,e^{i\phi}+4u^2-2-s.
\]
With \(B=-2su\) and \(A=4u^2-2-s\), direct multiplication yields
\[
|P_s|^2=(A-1)^2+B^2+4Av^2+2B(A+1)v.
\]
Since \(A<0\) for \(s>2\) and \(0\le u\le1\), completing the square gives
\[
G_s(x)-|P_s|^2=4(s+2-4x)(v-v_*)^2,
\qquad G_s(x)=(4x-s-3)^2\left(1+\frac{s^2x}{s+2-4x}\right).
\]
An algebraic factorization, valid identically for \(s>2\), gives
\[
H_s-G_s(x)=\frac{(s+2)(1-x)(s^2-4sx-s+8x-4)^2}{(s-2)(s+2-4x)}.
\]
Adding these two equalities proves the stated exact deficit. In particular \(|P_s|^2\le H_s\) for every torus triple and every real \(s>2\).

**Equality and range.** The first term vanishes only if \(x=1\) or
\[
x=x_0(s)=\frac{s^2-s-4}{4(s-2)}.
\]
The second term vanishes only if \(v=v_*\). For \(s_0\le s\le4\), the choice \(x=1\) gives
\[
v=v_*(1)=\frac{s(3-s)}{2(2-s)}\in[-1,1],
\]
so the upper bound is attained and equals the supremum squared. This configuration has the first two phases equal.

For the other algebraic equality branch, \(x=x_0(s)\in[0,1]\). Substitution gives \(A=-s/(s-2)\), and thus \(v_*=u\). Consequently \(e^{i\phi}\) is one of \(e^{i\theta},e^{-i\theta}\); at least two of the three original phases coincide. Permuting those repeated phases puts the configuration in the first equality branch. Therefore all maximizers, up to common phase and permutation, have precisely the claimed form. Conjugation supplies the two angular orientations. At the endpoints the same argument applies without modification.

## Verification
The standalone script `verify_phase.py` checks, in exact symbolic arithmetic, the square-completion, global factorization, equality-branch identity, stationary derivative for the previously known ratio, and the algebraic normalization at the known sharp parameter. It reports `SA_PHASE_IDENTITY_PASS`. This is a finite identity checker, not a proof by numerical sampling; all quantifiers in the theorem follow from the displayed algebraic equalities and sign analysis.

## Relationship to prior work
Hartz–Wang (2026), Example 6.4, gives the exact Schur–Agler norm of the full complex-parameter symmetric polynomial family; it does not formulate the global nonnegative phase-deficit identity or classify every torus maximizing triple. Grinshpan–Kaliuzhnyi-Verbovetskyi–Woerdeman (2012), Section 6 and Remark 6.2, already determine the sharp three-variable ratio and its optimizing coefficient. The numerical ratio, its radical expression and coefficient optimization are therefore **previous work**, not new assertions here. The new contribution is the complete quantitative phase-deficit identity and its all-extremizer consequences throughout a real parameter interval.

## Limitations
This is a three-variable scalar-polynomial statement and a pointwise torus phase comparison; it neither establishes a new global norm-ratio bound nor classifies commuting operator tuples attaining the Schur–Agler norm. Equality geometry is given only for the interval where the displayed upper envelope is attainable, not for arbitrary complex coefficient parameters. Independent mathematical audit and comprehensive historical priority certification are not claimed.

## References
- Michael Hartz and Yi Wang, *On the Schur–Agler Norm*, arXiv:2602.14047v1, February 15, 2026, Example 6.4; https://arxiv.org/html/2602.14047v1
- Anatolii Grinshpan, Dmitry S. Kaliuzhnyi-Verbovetskyi and Hugo J. Woerdeman, *Norm-constrained determinantal representations of multivariable polynomials*, arXiv:1208.2288v1 (2012), Section 6 and Remark 6.2; https://arxiv.org/pdf/1208.2288
