# Exact deficit decomposition for planar finite-field quadratic extension
## Finding
Let \(F=\mathbb F_q\) have odd order, let \(Q(x)=x^{\mathsf T}Ax\) be a nondegenerate homogeneous quadratic form on \(F^2\) with \(A\) symmetric and invertible, let \(j\in F^\times\), and put
\[
S_j=\{x\in F^2:Q(x)=j\},\qquad M=|S_j|=q-\chi(-\det A),\qquad m=M/2.
\]
Give \(S_j\) normalized counting measure and \(F^2\) counting measure. Fix a nontrivial additive character \(e:F\to\mathbb C^\times\), and define
\[
E f(\xi)=\frac1M\sum_{x\in S_j}f(x)e(\xi\cdot x).
\]
Choose one representative \(x_i\) from each antipodal pair \(\{x,-x\}\), for \(1\le i\le m\), and set
\[
u_i=|f(x_i)|^2,\quad v_i=|f(-x_i)|^2,\quad t_i=u_i+v_i,\quad r_i=\sqrt{u_iv_i},\quad z_i=f(x_i)f(-x_i),\quad T=\sum_{i=1}^m t_i.
\]
Define the fourth-moment energy
\[
W(f)=\sum_{a+b=c+d\atop a,b,c,d\in S_j}f(a)f(b)\overline{f(c)f(d)}.
\]
Then the sharp energy deficit has the exact nonnegative decomposition
\[
\begin{aligned}
\Delta(f)&=\left(3-\frac3M\right)T^2-W(f)\\
&=\frac32\left(\sum_i t_i^2-\frac{T^2}{m}\right)
+\frac12\sum_i(u_i-v_i)^2\\
&\quad+2\sum_{i<k}\left(t_it_k-4r_ir_k\right)
+4\left(\left(\sum_i r_i\right)^2-\left|\sum_i z_i\right|^2\right).
\end{aligned}
\]
Every term on the last two lines is nonnegative. Consequently
\[
\|E\|_{L^2(S_j)\to L^4(F^2)}^4=\frac{3q^2(M-1)}{M^3},
\]
and the extension deficit itself is exactly
\[
\frac{3q^2(M-1)}{M^3}\|f\|_{L^2(S_j)}^4-\|Ef\|_{L^4(F^2)}^4
=\frac{q^2}{M^4}\Delta(f).
\]
In particular, the deficit separately controls antipodal-pair mass variance and opposite-point modulus imbalance:
\[
\Delta(f)\ge \frac32\sum_i\left(t_i-\frac{T}{m}\right)^2,
\qquad
\Delta(f)\ge \frac12\sum_i(u_i-v_i)^2.
\]
Equality holds exactly for the known extremizer manifold: \(|f|\) is constant on \(S_j\) and all products \(f(x)f(-x)\) have one common argument.

## Assumptions and scope
The field has odd characteristic, \(Q\) is homogeneous and nondegenerate in two variables, and \(j\ne0\). These hypotheses imply \(0\notin S_j\), \(S_j=-S_j\), and no point of \(S_j\) equals its antipode. The formula is invariant under linear changes of variables and covers both split curves, where \(M=q-1\), and anisotropic curves, where \(M=q+1\).

The statement is an exact deficit identity, not merely an equality-case classification. The previously known sharp split and anisotropic constants are consequences and are not asserted here as the new part.

## Proof
Let
\[
B(x,y)=Q(x+y)-Q(x)-Q(y)
\]
be the polar form. Nondegeneracy of \(Q\) implies nondegeneracy of \(B\). If \(a+b=s\ne0\) with \(a,b\in S_j\), then \(Q(s-a)=Q(a)=j\) gives
\[
B(s,a)=Q(s).
\]
Thus \(a\) lies on one affine line. Its intersection with the quadratic curve has at most two points. Once one solution \(a\) is known, \(b=s-a\) is the other solution, so every nonzero pair-sum fiber consists only of \((a,b)\) and \((b,a)\), with the diagonal case contributing just \((a,a)\). For \(s=0\), every antipodal ordered pair \((x,-x)\) occurs.

Writing \(P=\sum_i z_i\), pair-sum orthogonality therefore gives the exact identity
\[
W(f)=2T^2-\sum_i(u_i^2+v_i^2)-4\sum_i u_iv_i+4|P|^2
=2T^2-\sum_i t_i^2-2\sum_i r_i^2+4|P|^2.
\]
Now put \(R=\sum_i r_i\). Add and subtract the three successive sharp upper bounds used in the elementary optimization: phase alignment \(|P|\le R\), opposite-point balance \(r_i\le t_i/2\), and equal pair masses \(\sum_i t_i^2\ge T^2/m\). Direct algebra yields
\[
\begin{aligned}
\left(3-\frac3M\right)T^2-W(f)
&=4(R^2-|P|^2)\\
&\quad+\left[\frac12\sum_i(u_i-v_i)^2+2\sum_{i<k}(t_it_k-4r_ir_k)\right]\\
&\quad+\frac32\left(\sum_i t_i^2-\frac{T^2}{m}\right).
\end{aligned}
\]
The middle bracket is nonnegative because \(t_i\ge2r_i\), while the first term is nonnegative by the triangle inequality and the last by Cauchy--Schwarz. This proves the decomposition.

Equality in all terms forces all \(t_i\) equal, \(u_i=v_i\), and equality in the triangle inequality for \(\sum_i z_i\). Hence \(|f|\) is constant and the nonzero \(z_i\) have a common argument. Conversely those conditions make every deficit term vanish.

Finally additive-character orthogonality gives
\[
\|Ef\|_4^4=\frac{q^2}{M^4}W(f),\qquad
\|f\|_2^4=\frac{T^2}{M^2},
\]
which converts the energy identity to the stated extension identity.

## Verification
The accompanying `verify.py` checks split and anisotropic representative conics over ten odd prime fields from \(3\) through \(31\). For each conic it verifies the cardinality, the complete pair-sum fiber structure, the exact fourth-moment identity for deterministic nonconstant Gaussian-integer weights, and the four-term deficit decomposition using exact rational arithmetic.

The successful replay output is:

`VERIFY_OK primes=10 conics=20 pair_fibers=3384 energy_checks=20`

These finite checks corroborate the algebra. They do not prove the prime-power theorem; that follows from the field-independent argument above.

## Relationship to prior work
Iosevich and Koh introduced the same nondegenerate quadratic surfaces and proved the sharp exponent range in dimension two, including \(R^*(2\to4)\lesssim1\), by controlling sums of two points on the curve. Their result is an order-of-magnitude extension estimate, not an exact norm or deficit identity. Koh and Shen later characterized when general planar algebraic curves have the sharp \(L^2\to L^4\) exponent range, again at the boundedness level.

The 2024 sharp finite-field extension work of González-Riquelme and Oliveira e Silva treats the parabola at \(L^2\to L^6\), and higher-dimensional paraboloids, hyperbolic paraboloids, and cones at \(L^2\to L^4\); it does not state the planar quadratic-curve deficit above. The 2026 quadratic-surface result of Ronda concerns surfaces in \(F^3\), not curves in \(F^2\).

Separate exact split-hyperbola and anisotropic norm-one-torus norm/equality statements were already present in the comparison corpus. The contribution here is the exact nonnegative deficit decomposition and its quantitative stability consequences, which are strictly stronger than knowing the sharp constant and equality set.

## Limitations
The decomposition is specific to nonzero levels of nondegenerate homogeneous binary quadratic forms in odd characteristic. It does not address zero-radius cones, characteristic two, higher-dimensional quadratic surfaces, or arbitrary planar curves. The displayed lower bounds control two concrete amplitude defects but are not claimed to be an optimal metric-distance stability theorem for the full extremizer manifold. A residual originality risk remains that the same algebraic decomposition appears in older restriction or additive-energy literature under different terminology.

## References
1. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1, first public 2008-04-28.
2. D. Koh and C.-Y. Shen, *Sharp extension theorems and Falconer distance problems for algebraic curves in two dimensional vector spaces over finite fields*, arXiv:1003.4240v1, first public 2010-03-22.
3. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1, first public 2024-05-26.
4. P. Ronda, *Sharp \(L^2\to L^4\) extension inequality for quadratic surfaces in finite fields*, arXiv:2609.13023v1, first public 2026-09-11.
