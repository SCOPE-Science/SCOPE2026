# Exact cyclic Turán mass for the five-site support \(\{0,\pm1,\pm3\}\)

## Finding

For an integer \(N\ge7\), let \(T_N\) be the maximum counting mass \(\sum_{x\in\mathbb Z/N\mathbb Z} f(x)\) over complex positive-definite functions with \(f(0)=1\) and support contained in \(\{0,\pm1,\pm3\}\). For real-even functions write \(a=f(1)=f(-1)\), \(b=f(3)=f(-3)\).

**Even \(N\).** One has \(T_N=2\). Set
\[
c=\cos(2\pi/N),\qquad
G_N=\max_{1\le j\le N/2-1} x_j(1-x_j),\qquad x_j=\cos(2\pi j/N).
\]
Here \(G_N>0\). The full set of real-even optimizers consists of
\[
 a=\tfrac12-b,\qquad -\frac{1}{8c(1+c)}\le b\le\frac{1}{8G_N}.
\]
In particular, both \((a,b)=(1/2,0)\) and \((0,1/2)\) are optimal.

**Odd \(N\).** Set \(\delta=\pi/N\), \(C=\cos\delta\), \(r=\lfloor(N+1)/6\rfloor\), \(u=\cos(2\pi r/N)\), and \(w=C-u\). Then \(u,w>0\), and
\[
T_N=\frac{(1+C)(1-u)(1-w)}{Cuw}>2.
\]
The unique real-even optimizer has Fourier polynomial
\[
P_N(\theta)=\frac{(\cos\theta+C)(\cos\theta-u)(\cos\theta-w)}{Cuw}
=1+2a_N\cos\theta+2b_N\cos3\theta,
\]
where
\[
b_N=\frac{1}{8Cuw},\qquad a_N=\frac{3-4(C^2-Cu+u^2)}{8Cuw}.
\]
Here \(b_N>0\), and \(a_N\ge0\) with equality exactly when \(3\mid N\), in which case \(T_N=1+\sec(3\pi/N)\). Along odd moduli, \(T_N=2+9\pi^2/(2N^2)+O(N^{-3})\).

## Assumptions and scope

Positive definiteness means \(\sum_{x,y} c_x\overline{c_y}f(x-y)\ge0\) for all complex coefficient families. Equivalently the discrete Fourier coefficients are nonnegative real numbers, and \(f(-x)=\overline{f(x)}\). Taking the real part preserves feasibility, by averaging the Fourier coefficients at opposite frequencies, and preserves total mass. Thus the optimum value is also the real-even optimum. For \(N\ge7\) the five sites are distinct. The real-even feasible pairs satisfy \(1+2a x_j+2b(4x_j^3-3x_j)\ge0\) for every \(j\), and the objective is \(1+2(a+b)\). The feasible set is compact since positive definiteness gives \(|f(x)|\le f(0)=1\).

## Proof

**Even grids.** The frequency \(j=N/2\) gives \(1-2(a+b)\ge0\), and \(1+\cos\theta\) attains the resulting mass bound. On the equality line \(a+b=1/2\) the Fourier polynomial is
\[
1+2a x+2b(4x^3-3x)=(1+x)[1-8b x(1-x)].
\]
At \(x=\pm1\) feasibility is automatic. At every other grid point \(1+x>0\), so feasibility is exactly \(8b x(1-x)\le1\). The largest positive \(x_j(1-x_j)\) exists since \(0<c<1\); it is \(G_N\). The most negative value comes from the smallest sampled \(x_j>-1\), which is \(-c\), since \(x(1-x)\) increases for negative \(x\). These two inequalities are precisely the two bounds on \(b\) in the finding. The second example follows also from the nonnegative polynomial \(1+\cos3\theta\).

**Odd grids: feasibility.** Write \(x=\cos\theta\). Since \(u+w=C\), the factored cubic has zero quadratic coefficient and constant coefficient \(Cuw\). Expanding in \(x\) and \(4x^3-3x\) gives the asserted \(a_N,b_N\). To locate its roots on the grid, use the monotone half-grid \(x_j\) for \(0\le j\le(N-1)/2\), whose minimum is \(-C\). The identity \(C=\cos(\pi/3-\delta)+\cos(\pi/3+\delta)\) is useful in all three cases:

- If \(N=6m+1\), \(u=\cos(\pi/3-\delta/3)>1/2\) and \(x_{r+1}=\cos(\pi/3+5\delta/3)<\cos(\pi/3+\delta)<w<u\). The strict lower bound on \(w\) follows from \(u<\cos(\pi/3-\delta)\); the upper bound follows from \(C<1<2u\).
- If \(N=6m+3\), \(u=\cos(\pi/3-\delta)=x_r\) and \(w=\cos(\pi/3+\delta)=x_{r+1}\).
- If \(N=6m+5\), \(u=\cos(\pi/3+\delta/3)\) and \(w<\cos(\pi/3-\delta)<\cos(\pi/3-5\delta/3)=x_{r-1}\). Moreover \(w-u=\sin(\delta/3)[\sqrt3-2\sin(2\delta/3)]>0\).

Here \(0<\delta\le\pi/7\), so in each case \(u,w>0\), and no sampled cosine is strictly between the two positive roots. The factored cubic is therefore nonnegative on the sampled grid.

**Odd grids: optimality and uniqueness.** Let \(v=4u^3-3u\) and \(D=\cos(3\delta)\). The bound \(0<u<\sqrt3/2\) follows from \(2\pi r/N\ge\pi/3-\delta>\pi/6\), so \(v<0\); also \(0<D<C\). The active Fourier inequalities have coefficient pairs \((u,v)\) and \((-C,-D)\). Put
\[
L=-\frac{C-D}{Cv-Du},\qquad K=-\frac{u-v}{Cv-Du}.
\]
Both weights are strictly positive. They satisfy \(Lu-KC=Lv-KD=-1\), so their weighted combination gives \(0\le L+K-2(a+b)\) for every feasible pair. The factored polynomial is zero at both contacts, hence attains equality. Conversely every maximizer must be zero at both contacts, which uniquely determines \((a,b)\) since \(Cv-Du\ne0\). At \(x=1\) the factored polynomial equals the mass in the finding.

**Strict inequality, vanishing coefficient, and asymptotics.** The polynomial \(1+\cos\theta\) is strictly positive at every odd grid frequency, so increasing its first cosine coefficient by a sufficiently small positive amount improves the mass beyond 2. Also
\[
\frac{a_N}{b_N}=3\sin^2\delta-4(u-C/2)^2.
\]
The angle for \(u\) lies within \([\pi/3-\delta,\pi/3+\delta]\), where \(|u-C/2|\le(\sqrt3/2)\sin\delta\) with equality only at the endpoints. These contacts at the ends of the angle interval arise exactly when \(3\mid N\). Then the zero at the smallest sampled cosine \(-C\) gives \(P_N=1+\cos(3\theta)/D\). Finally, \(u=1/2+O(\delta)\), \(C=1-\delta^2/2+O(\delta^4)\), and \(uw=u(C-u)=1/4+O(\delta^2)\). Expanding \(T_N=(1+C)C^{-1}[1+(1-C)/(uw)]\) proves the stated asymptotic.

## Verification

The proof gives an exact certificate for every modulus: in the even case the Nyquist inequality and its factored equality line, and in the odd case the three root brackets and positive combination of two active inequalities. The accompanying `check.py` is a finite floating-point corroboration for the mass and odd contact formula, with a separate enumeration of two-row LP intersections through \(N=101\). It is not a test of the full even equality interval, whose necessity and sufficiency are established by the displayed factorization.

## Relationship to prior work and limitations

Kolountzakis and Révész’s infinite-group five-site example gives mass \(2\) for \(\{0,\pm1,\pm(2k+1)\}\) in \(\mathbb Z\); it does not give the positive odd-grid defect. Fu, Li, Wang and Wang treat a continuous union of three intervals and discrete approximations on \(\mathbb Z\), not this cyclic quotient with fixed five-site support. The finite-grid Turán result with support \(\{0,\pm1,\pm4\}\) has different Fourier constraints and a modulus-five phenomenon. The finite-grid Carathéodory–Fejér result on \(\{0,\pm1,\pm3\}\) maximizes the first coefficient rather than the sum here. By averaging a Lovász theta matrix over cyclic translations, the mass can also be expressed as theta of the graph joining distinct vertices whose differences are outside \(\{\pm1,\pm3\}\); that general reformulation alone does not yield the grid contacts or the real-even optimizer formulas. No global priority is asserted. Only this support, these modulus ranges, and the real-even equality cases are classified; complex optimizer faces are not classified.

## References

- M. N. Kolountzakis and Sz. Gy. Révész, *Turán’s extremal problem for positive definite functions on groups*, [arXiv:math/0312218](https://arxiv.org/abs/math/0312218), §3.3, Example 3.
- M. N. Kolountzakis and Sz. Gy. Révész, *On pointwise estimates of positive definite functions with given support*, [arXiv:math/0302193](https://arxiv.org/abs/math/0302193).
- X.-Y. Fu, Y.-K. Li, W.-J. Wang, and X. Wang, *Turán problem on the union of three intervals of equal length*, [arXiv:2608.15643](https://arxiv.org/abs/2608.15643).
- *Pentagonal locking and residue-sensitive finite Turán defects for a five-point cyclic support*, [Resultary b2ce368d6213](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-pentagonal-locking-and-residue-sensitive-finite-tur-n-defects-fo--b2ce368d6213/RESULT.md).
- *Exact discrete Carathéodory–Fejér constant for the isolated third harmonic*, [Resultary e309f8e59103](https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-exact-discrete-carath-odory-fej-r-constant-for-the-isolated-thir--e309f8e59103/RESULT.md).
