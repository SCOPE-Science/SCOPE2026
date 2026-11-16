# Exactly two arithmetic-gap six-node Bernstein grids preserve circle positive definiteness

## Finding
For a real parameter \(0<t<\pi/4\), form the reflection-symmetric six-node grid
\[
\boldsymbol{x}(t)=(0,t,2t,\pi-2t,\pi-t,\pi).
\]
Define the degree-five sampling operator on continuous functions \(f:[0,\pi]\to\mathbb R\) by
\[
(T_t f)(\pi u)=\sum_{j=0}^{5}\binom{5}{j}u^j(1-u)^{5-j}f(x_j(t)),\qquad 0\le u\le1.
\]
**Theorem.** The operator \(T_t\) maps *every* continuous isotropic positive-semidefinite kernel on the circle to another such kernel if and only if
\[
\boxed{t=\pi/5\quad\text{or}\quad t=\pi/6.}
\]
The first case gives the ordinary equally spaced Bernstein nodes. The second gives the distinct, nonuniform grid
\[
(0,\pi/6,\pi/3,2\pi/3,5\pi/6,\pi).
\]
There are no other real parameters in the stated interval, including irrational multiples of \(\pi\). Positive-semidefinite is meant in the weak, not strictly positive-definite, sense.

## Assumptions and scope
The circle has geodesic distance in \([0,\pi]\). A continuous real function \(f\) on that interval is of positive type if \([f(d(z_i,z_j))]_{i,j}\) is positive semidefinite for every finite circle configuration. Equivalently,
\[
f(\theta)=c_0/2+\sum_{m\ge1}c_m\cos(m\theta),\qquad c_m\ge0,\qquad\sum_m c_m<\infty.
\]
The theorem is for the specified one-parameter reflected arithmetic-gap family, not for all six-node grids. There are no normalization, sign, or differentiability restrictions beyond positive type and continuity.

## Proof
**1. Reduction and exact coefficient formula.** For every integer \(m\ge1\), write \(P_m(u)=(T_t\cos(m\cdot))(\pi u)\), \(a=\cos(mt)\), and \(b=\cos(2mt)\). Its six Bernstein data are
\[
(1,a,b,(-1)^m b,(-1)^m a,(-1)^m).
\]
Consequently \(P_m(1-u)=(-1)^mP_m(u)\). Define its cosine coefficient \(\gamma_{m,k}=2\int_0^1P_m(u)\cos(k\pi u)\,du\). For \(k=0\), direct integration of the Bernstein basis yields
\[
\gamma_{m,0}=\begin{cases}0,&m\text{ odd},\\2(1+a+b)/3,&m\text{ even}.
\end{cases}
\]
Its first, third, and fifth derivatives at zero are
\[
\begin{aligned}
p_1&=5(a-1),\\
p_3&=60\bigl(((-1)^m-3)b+3a-1\bigr),\\
p_5&=\begin{cases}0,&m\text{ even},\\240(-1+5a-10b),&m\text{ odd}.
\end{cases}
\end{aligned}
\]
Repeated integration by parts, using reflection at \(u=1\), gives for \(k\ge1\):
\[
\gamma_{m,k}=\begin{cases}
0,&k+m\text{ odd},\\
-\dfrac4{X^3}\bigl(p_1X^2-p_3X+p_5\bigr),&k+m\text{ even},
\end{cases}\quad X=(\pi k)^2.
\]
Thus positive-type preservation is exactly the requirement that these coefficients, including \(k=0\), be nonnegative for every integer \(m\ge0\). Sufficiency follows by uniform convergence of the nonnegative Fourier series; necessity follows by testing the single positive-type input \(\cos(m\theta)\).

**2. Sufficiency at the two grids.** Fix \(t=\pi/q\) with \(q\in\{5,6\}\). The sampled data depend only on \(m\bmod 2q\). For even \(m\), the zero mode is \((2/3)(1+a+b)\ge0\). The fifth derivative vanishes and \(p_1\le0\); when \(m\not\equiv0\pmod{2q}\), the exact finite inequality
\[
4\pi^2p_1-p_3<0
\]
implies \(p_1X-p_3<0\) for all even \(k\ge2\). The exceptional mode \(m\equiv0\pmod{2q}\) is constant.

For odd \(m\), write \(H_m(X)=p_1X^2-p_3X+p_5\). In every residue class \(m\bmod 2q\), the three inequalities
\[
H_m(\pi^2)<0,\qquad H_m(9\pi^2)<0,\qquad H_m'(9\pi^2)<0
\]
hold, and \(p_1<0\). Since \(H_m''=2p_1<0\), \(H_m\) is strictly decreasing on \([9\pi^2,\infty)\). This covers \(k=1\) and every odd \(k\ge3\). All opposite-parity coefficients vanish. These finitely many exact inequalities are certified with rational intervals for \(\pi^2,\sqrt3,\sqrt5\) by the included standard-library `CHECK.py`; the proof does not infer infinitely many frequencies from a numerical enumeration. Therefore all output cosine coefficients are nonnegative.

**3. A zero-mode arithmetic obstruction.** For even \(m=2h\), put \(v=\cos(2ht)\). Then
\[
1+a+b=1+v+\cos(4ht)=v+2v^2,
\]
which is negative if and only if \(-1/2<v<0\). If \(t/\pi\) is irrational, the even-mode phases are dense in the circle and such an \(h\) exists. Otherwise write \(t=r\pi/p\) in lowest terms. The phases \(2ht\bmod 2\pi\) run through *all* \(p\)-th roots of unity. For every \(p\ge13\), their spacing \(2\pi/p\) is less than the length \(\pi/6\) of the open arc \((\pi/2,2\pi/3)\), so a forbidden root occurs. The denominators \(p=7,10,11\) also contain a forbidden root, at indices \(h=2,3,3\), respectively. Among \(p\le12\), the only possible denominators after this zero-mode test are \(5,6,8,9,12\). Reduced fractions with \(0<r/p<1/4\) thus leave precisely
\[
 t\in\{\pi/5,\pi/6,\pi/8,\pi/9,2\pi/9,\pi/12\}.
\]

**4. The higher-mode obstruction.** For the input \(m=1\) and output \(k=3\), put \(a=\cos t\) and \(X=9\pi^2\). Since \(b=2a^2-1\), the numerator in step 1 becomes
\[
H_1(X)=(480X-4800)a^2+(5X^2-180X+1200)a-5X^2-180X+2160.
\]
For \(0<t\le\pi/8\), one has \(a\ge\cos(\pi/8)>923/1000\). In the rigorously enclosing interval \(9.869<\pi^2<9.870\), both coefficients controlling the derivative in \(a\) are positive, and direct rational arithmetic at \(a=923/1000\) gives \(H_1(9\pi^2)>1706\). Hence \(\gamma_{1,3}<0\). This excludes \(\pi/8,\pi/9,\pi/12\).

Finally, at \(t=2\pi/9\) and \(m=9\), the Bernstein data are \((1,1,1,-1,-1,-1)\), so \(p_1=0\), \(p_3=-120\), \(p_5=-1440\). At \(k=3\),
\[
H_9(9\pi^2)=120(9\pi^2)-1440>0,
\]
again giving a negative cosine coefficient. Only \(t=\pi/5\) and \(t=\pi/6\) survive, and step 2 proves both work. \(\square\)

## Verification
Run `python3 CHECK.py` with Python 3 and its standard library. It reconstructs the derivative formulas' finite sign tests for every residue \(m\bmod 2q\), \(q=5,6\), using exact rational interval arithmetic. Its certified intervals for \(\pi\) use Machin's arctangent identity and the alternating-series remainder; those for \(\sqrt3\) and \(\sqrt5\) are checked by squaring. It also certifies the small-parameter third-mode obstruction, the \(2\pi/9\) witness, and the strict seven-root zero-mode inequality. The checker does not substitute finite sampling for the global proof: the periodic reduction, degree-five integration-by-parts identity, root-spacing argument, and monotonicity in \(k\) are analytical.

## Relationship to prior work
Otten, Nguyen and Watts (2026) establish positive-type preservation for ordinary equally spaced Bernstein grids at every degree, which supplies the known \(t=\pi/5\) case. Their theorem does not cover the nonuniform \(\pi/6\) grid or exclude all other real center-gap parameters. Earlier low-degree variable-node classifications for degrees two and three concern different operators, and an existing degree-four grid classification does not imply the present degree-five result. The novelty assessed here is the complete continuum classification for this six-node arithmetic-gap deformation and the unexpected second survivor, not the general coefficient test or the uniform-grid result.

## Limitations
This result does not classify unrestricted nonsymmetric six-node samples, other Bernstein degrees, strictly positive-definite outputs, or optimal approximation errors. The proof uses a small finite exact-arithmetic sign certificate for the two surviving grids; the explicit mathematical reductions justify its coverage. Although the closest literature has been checked by statement and implication, priority against all older approximation-theory formulations remains provisional.

## References
1. M. Otten, N. Nguyen and T. W. Watts, *Preservation of Positive-Definiteness by Bernstein Operators on the Circle*, first posted 2026-08-05, arXiv:2608.04836, https://arxiv.org/abs/2608.04836 . Full publicly accessible preprint text inspected through the author's licensed open reproduction at https://www.researchgate.net/publication/411739385_Preservation_of_Positive-Definiteness_by_Bernstein_Operators_on_the_Circle .
2. *Quadratic rigidity and cubic node freedom for positive-definite Bernstein interpolation on the circle*, public mathematical research record dated 2026-11-02, identifier b87f6c90a4aa. Its reported scope is degree two and degree three.
3. Classical Bochner–Schoenberg characterization of positive-type cosine series on the circle, as presented in reference 1, Section 1.
