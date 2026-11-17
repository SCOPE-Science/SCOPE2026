# Global critical synchronization in a three-species Ricker competition map

## Finding
Consider the three-species Ricker map
\[
x_i(n+1)=x_i(n)\exp\!\left(2-x_i(n)-c\sum_{j\ne i}x_j(n)\right),\qquad i=1,2,3.
\]
For every fixed \(1-2/e<c<1\) and **every** initial condition \(x_i(0)>0\), all three populations converge to the same positive equilibrium:
\[
\lim_{n\to\infty}x_i(n)=s_c:=\frac{2}{1+2c},\qquad i=1,2,3.
\]
The equilibrium has one neutral flip multiplier \(-1\), so this is a global result *on* the flip boundary, not a conclusion from strict linear stability. Set
\[
\lambda_c=\frac{4c-1}{1+2c}\in(0,1).
\]
For each pair of indices \(i\ne j\), **exactly one** of the following alternatives occurs: the two populations become identical at a finite generation and remain identical forever; or their logarithmic ratio never vanishes and has the exact exponential rate
\[
\lim_{n\to\infty}\frac{1}{n}\log\left|\log\frac{x_i(n)}{x_j(n)}\right|=\log\lambda_c.
\]
There are also genuinely algebraically relaxing trajectories: for every sufficiently small nonzero \(z_0\), the diagonal initial condition \(x_i(0)=s_c e^{z_0}\) obeys
\[
\lim_{n\to\infty}n\left(\log\frac{x_i(n)}{s_c}\right)^2=\frac34,
\qquad i=1,2,3.
\]
Thus exponential synchronization coexists with a sharp inverse-square-root radial relaxation on this natural critical parameter boundary.

## Assumptions and scope
All variables are real and positive. There are exactly three species, the intrinsic Ricker growth parameter is \(2\), self-competition coefficients equal \(1\), and all six cross-competition coefficients equal a common constant \(c\) in the **open** range \(1-2/e<c<1\). The theorem includes arbitrarily unequal positive initial populations. The parameter inequality is a sufficient global-synchronization condition; its optimality is **not** claimed. The exact pairwise rate applies only to pairs which never coalesce exactly in finite time. The radial inverse-square-root law is asserted for small, nonstationary initial conditions on the invariant diagonal, not for every off-diagonal orbit.

## Proof
Put \(\alpha=1-c\), \(a=1+2c\), \(S_n=x_1(n)+x_2(n)+x_3(n)\), and \(\overline x_n=S_n/3\). Then the original map is exactly
\[
x_i(n+1)=x_i(n)\exp(2-cS_n-\alpha x_i(n)). \tag{1}
\]

**1. A uniform invariant upper bound and a positive total-population floor.** From \(x_i(n+1)\le x_i(n)\exp(2-x_i(n))\) and \(\max_{u>0}u e^{2-u}=e\), one has \(0<x_i(n)\le e\) for all \(n\ge1\). Hence \(S_n\le3e\). Since \(cS_n+\alpha x_i(n)\le S_n\), summation of (1) gives
\[
S_{n+1}\ge S_n e^{2-S_n}. \tag{2}
\]
For \(0<S_n<1\), the right side exceeds \(S_n\); for \(1\le S_n\le3e\), it is bounded below by the positive constant \(b_*:=\min_{1\le u\le3e}u e^{2-u}\). Thus induction gives a fixed positive lower bound \(S_n\ge b:=\min\{S_1,b_*\}>0\) for all \(n\ge1\).

**2. Global contraction of all population ratios.** For \(i\ne j\), write \(w_{ij,n}=\log(x_i(n)/x_j(n))\), and define the logarithmic mean
\[
L(u,v)=\begin{cases}(u-v)/(\log u-\log v),&u\ne v,\\u,&u=v.\end{cases}
\]
It obeys \(\min\{u,v\}\le L(u,v)\le\max\{u,v\}\). Equation (1) gives the **exact** identity
\[
w_{ij,n+1}=\bigl[1-\alpha L(x_i(n),x_j(n))\bigr]w_{ij,n}. \tag{3}
\]
Because \(\alpha e<2\) and \(0<L(x_i,x_j)\le e\) for \(n\ge1\), every multiplier in (3) has modulus strictly below \(1\). Let \(D_n=\max_{i,j}|w_{ij,n}|\). Then \(D_{n+1}\le D_n\) for \(n\ge1\). Hence \(x_i(n)\ge S_n/(3e^{D_1})\ge m:=b/(3e^{D_1})>0\). Consequently \(m\le L\le e\) and
\[
D_{n+1}\le qD_n,\quad q=\max\{|1-\alpha m|,|1-\alpha e|\}<1. \tag{4}
\]
This supplies global exponential synchronization in logarithmic coordinates and, in particular, \(x_i(n)-\overline x_n=O(q^n)\).

**3. The common scalar dynamics is a vanishing perturbation of the critical Ricker map.** Define \(t_n=aS_n/3\), so \(t_n\in[ab/3,ae]\). Summing (1), and factoring out the common exponent, yields the exact recurrence
\[
t_{n+1}=g(t_n)B_n,\quad g(t)=t e^{2-t},\quad
B_n=\sum_{i=1}^3\frac{x_i(n)}{S_n}e^{-\alpha(x_i(n)-\overline x_n)}. \tag{5}
\]
Expanding the exponential uniformly on the bounded positive interval, and using \(\sum_i(x_i-\overline x_n)=0\), gives
\[
\sum_i x_i(x_i-\overline x_n)=\sum_i(x_i-\overline x_n)^2,
\quad B_n=1+O(q^{2n}). \tag{6}
\]
The scalar map \(g(t)=te^{2-t}\) has its unique positive fixed point \(2\), which attracts every positive scalar trajectory. For completeness, it has no nontrivial positive two-cycle: if \(g(u)=v\) and \(g(v)=u\), then \(u+v=4\); writing \(u=2-d,v=2+d\), the other cycle equation would require \(\log((2+d)/(2-d))=d\), impossible for \(0<d<2\) since its left derivative is \(4/(4-d^2)>1\). The standard one-dimensional no-two-cycle convergence principle, or the scalar Ricker theorem recorded in [1], then gives convergence to \(2\). The fixed point is locally attracting because its two-step map is \(z\mapsto z-4z^3/3+O(z^4)\) in logarithmic coordinate \(z=\log(t/2)\), established explicitly in step 5.

We also justify the vanishing-forcing passage in (5): on the fixed compact interval containing all \(t_n\), scalar iterates of \(g\) approach \(2\) **uniformly** after a sufficiently large fixed number of steps (compactness and local asymptotic stability). Over any fixed number of steps, the discrepancy between (5) and the scalar iterates tends uniformly to zero as \(n\to\infty\), by (6), compactness and uniform continuity. Therefore \(t_n\to2\), so \(S_n\to6/a\), and (4) gives \(x_i(n)\to2/a=s_c\).

**4. Exact transverse logarithmic exponent.** With \(x_i,x_j\to s_c\), continuity of the logarithmic mean yields
\[
1-\alpha L(x_i(n),x_j(n))\longrightarrow
1-\frac{2(1-c)}{1+2c}=\lambda_c>0. \tag{7}
\]
If any factor in (3) is zero, the corresponding populations coalesce immediately, and equality is invariant by (1). Otherwise every factor is nonzero. Taking logarithms of absolute values of (3), summing and dividing by \(n\), Cesàro convergence gives the stated limit \(\log\lambda_c\), independently of the initial values.

**5. A critical algebraic trajectory.** On the invariant diagonal \(x_1=x_2=x_3=s_c e^z\), the exact scalar recurrence is
\[
z_{n+1}=f(z_n):=z_n+2-2e^{z_n}.
\]
Ordinary Taylor expansion gives
\[
f(z)=-z-z^2-\tfrac13z^3+O(z^4),\qquad
f(f(z))=z-\tfrac43z^3+O(z^4). \tag{8}
\]
For sufficiently small \(z_0\ne0\), the even subsequence \(u_k=z_{2k}\) keeps its sign, decreases in magnitude to zero, and satisfies
\[
u_{k+1}=u_k-\tfrac43u_k^3+O(u_k^4),\qquad
\frac1{u_{k+1}^2}-\frac1{u_k^2}\longrightarrow\frac83.
\]
By Cesàro/Stolz, \(ku_k^2\to3/8\). Because \(f(z)/z\to-1\), the odd subsequence has the same squared leading magnitude, and in the original generation clock \(nz_n^2\to3/4\). This completes the theorem.

## Verification
The accompanying `verify.py` checks the cubic coefficient in (8) symbolically, the linearized eigenvalues, the algebraic and transverse rates numerically, and selected positive initial conditions in the specified parameter interval. It is supplemental to the proof, not a substitute for the uniform bounds or infinite asymptotic arguments. Run `python verify.py` using Python 3 with `sympy` and `mpmath` available. All artifacts refer to the exact equations displayed above.

## Relationship to prior work
Luís and Rodrigues [1, Section 5] analyze local fixed-point stability in the three-dimensional Ricker competition model and [1, Section 6] formulate a global-attraction conjecture for locally stable nontrivial equilibria. The present result treats a **fully specified symmetric three-species slice on its neutral flip boundary**, and supplies global attraction together with different radial and transverse rates. The 2019 three-dimensional global result of Gyllenberg, Jiang, and Niu [2, Theorem 2.3] requires a Ricker intensity inequality \(\nu_i<1/(1+2c)\) on this symmetric specialization; here \(\nu_i=2\), so that published theorem cannot imply the stated boundary case. Ackleh and Salceanu [3] study exclusion and robust coexistence rather than the critical rate. A later survey [4] continues to emphasize incomplete global-attraction theory. Related two-species critical Ricker results [5,6] exhibit a similar anisotropy in dimension two but do not determine the three-species global theorem. The range \(c>1-2/e\) is the sufficient condition obtained by the global logarithmic-mean contraction; a larger true stability range has not been ruled out.

## Limitations
No assertion is made about parameters \(c\le1-2/e\), about asymmetric interaction matrices, or about initial data on the boundary of the positive octant. This result does not prove that all off-diagonal trajectories have the inverse-square-root radial asymptotic; only the stated diagonal family is covered. The sufficient inequality is not claimed optimal. The one-dimensional no-two-cycle convergence principle is a standard result; its use is explicitly identified. Relevance and priority are based on the cited publicly accessible primary literature and indexed comparison; an unindexed equivalent or more general theorem remains a residual novelty risk. No independent audit has been performed.

## References
[1] R. Luís and E. Rodrigues, “Local Stability in 3D Discrete Dynamical Systems: Application to a Ricker Competition Model,” *Discrete Dynamics in Nature and Society* (2017), Article 6186354. First published 6 July 2017. https://doi.org/10.1155/2017/6186354

[2] M. Gyllenberg, J. Jiang, and L. Niu, “A note on global stability of three-dimensional Ricker models” (2019), Theorem 2.3. https://scispace.com/pdf/a-note-on-global-stability-of-three-dimensional-ricker-4cttqcfljw.pdf

[3] A. S. Ackleh and P. L. Salceanu, “Competitive exclusion and coexistence in an n-species Ricker model” (2015). https://doi.org/10.1080/17513758.2015.1020576

[4] R. Luís, “Open Problems and Conjectures in the Evolutionary Periodic Ricker Competition Model,” *Axioms* **13** (2024), 246. https://doi.org/10.3390/axioms13040246

[5] “Global critical relaxation and a logarithmic clock in symmetric Ricker competition” (2026), indexed mathematical research record. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-global-critical-relaxation-and-a-logarithmic-clock-in-symmetric--196d57cbc210

[6] “Asymmetric critical synchronization and logarithmic relaxation in planar Ricker competition” (2026), indexed mathematical research record. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-asymmetric-critical-synchronization-and-logarithmic-relaxation-i--fbde7aa617eb
