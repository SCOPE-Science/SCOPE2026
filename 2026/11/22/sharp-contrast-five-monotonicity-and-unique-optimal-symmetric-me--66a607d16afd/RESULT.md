# Sharp contrast-five monotonicity and unique optimal symmetric mesh for four-knot natural cubic splines

## Finding

Let \(r>0\), and interpolate four real samples at the knots \(x_0=0\), \(x_1=1\), \(x_2=1+r\), \(x_3=2+r\) by the **natural cubic spline** \(S\): the unique piecewise cubic \(C^2\) interpolant with \(S''(x_0)=S''(x_3)=0\). For any strictly increasing samples, define the three positive **secant slopes**
\[
 a=y_1-y_0,\qquad b=\frac{y_2-y_1}{r},\qquad c=y_3-y_2,
 \qquad \kappa=\frac{\max\{a,b,c\}}{\min\{a,b,c\}}.
\]
The exact largest data-uniform monotonicity guarantee is
\[
\boxed{\ R(r)=\min\left\{r+3,\;3+\frac4r\right\}.\ }
\]
**Precisely:** for every positive triple of secant slopes with \(\kappa\le R(r)\), the corresponding natural cubic spline is nondecreasing over its entire knot interval. For every \(K>R(r)\), there is a strictly positive slope triple of contrast exactly \(K\) for which the spline decreases somewhere. Thus this is not merely a sufficient bound. Among all reflection-symmetric four-knot meshes, the unique optimum is
\[
 \boxed{\ r=2,\qquad \max_{r>0}R(r)=5.\ }
\]
For \(r\le2\), the sharp obstruction is the boundary-slope pattern \((a,b,c)=(1,K,1)\); for \(r\ge2\), it is the central-pocket pattern \((K,1,K)\). At the optimal \((1,2,1)\) mesh and \(K=5\), both have zero derivative at the indicated witness point but remain nondecreasing. For equal spacing, the sharp threshold is only \(4\).

## Assumptions and scope

There are exactly four knots; the outer spacings are equal, and simultaneous positive rescaling and translation of the abscissae have been normalized away. Natural boundary conditions mean **zero endpoint second derivatives**, not clamped zero endpoint slopes. The domain includes all knot endpoints. The contrast is a ratio of **secant slopes** and not a ratio of raw data increments (the central raw increment is \(rb\)). The result concerns unmodified linear natural spline interpolation, not nonlinear derivative limiting or other endpoint conditions. Nondecreasing permits isolated zero derivatives, and all three input slopes are strictly positive.

## Proof

**1. Curvature equations and derivative linearity.** Write \(M_i=S''(x_i)\). With \(M_0=M_3=0\), continuity of the first derivatives gives
\[
 \begin{pmatrix}2(1+r)&r\\r&2(1+r)\end{pmatrix}
 \binom{M_1}{M_2}=6\binom{b-a}{c-b}.
\]
Put \(D=(r+2)(3r+2)>0\). Solving yields
\[
 M_1=\frac{6((2+3r)b-2(1+r)a-rc)}D,\qquad
 M_2=\frac{6((2+2r)c+ra-(2+3r)b)}D.
\]
On interval \(j\) of length \(h_j\), with local coordinate \(t\in[0,h_j]\), direct differentiation of the endpoint-value/curvature representation gives
\[
 S'(x_j+t)=s_j-\frac{h_j(2M_j+M_{j+1})}{6}
 +M_jt+\frac{M_{j+1}-M_j}{2h_j}t^2,
\]
where \((s_0,s_1,s_2)=(a,b,c)\), \((h_0,h_1,h_2)=(1,r,1)\). Therefore at every fixed point
\[
 S'=p_a a+p_b b+p_c c,\qquad p_a+p_b+p_c=1,
\]
as follows also by reproduction of affine functions.

**2. A universal negative-coefficient criterion.** Normalize the smallest positive slope to one, so all three slopes lie in \([1,K]\). For any real coefficients of sum one, the minimum of their linear combination over this cube is exactly
\[
 1-(K-1)N,\qquad N=\sum_{p_j<0}|p_j|.
\]
The minimum is attained at a corner of the cube (large slopes at negative coefficients, small slopes at positive coefficients). Thus the desired uniform contrast cutoff is exactly \(1+1/N_*\), where \(N_*\) is the largest negative-coefficient mass over all three spline intervals and all evaluation points. No finite mesh sampling enters this reduction.

**3. Outer intervals.** On the first interval set \(u=x\in[0,1]\), \(f=3u^2-1\in[-1,2]\). The exact coefficients are
\[
 (p_a,p_b,p_c)=\left(1-\frac{2(1+r)f}D,\;
 \frac{(2+3r)f}D,\;-\frac{rf}D\right).
\]
The first coefficient stays positive because \(D-4(1+r)=r(3r+4)>0\). If \(f<0\), only the \(b\)-coefficient is negative, with magnitude at most \((2+3r)/D=1/(r+2)\), attained at \(u=0\). If \(f>0\), only the \(c\)-coefficient is negative, with magnitude at most \(2r/D<1/(r+2)\). Reflection gives the same bound on the last interval. Thus their exact maximum negative mass is \(1/(r+2)\).

**4. Central interval.** On \([1,1+r]\), write \(x=1+rz\), \(0\le z\le1\). Direct substitution gives
\[
\begin{aligned}
 p_a(z)&=\frac{r[(9r+6)z^2-12(r+1)z+3r+4]}D,\\
 p_b(z)&=\frac{2[1+3rz(1-z)]}{r+2}>0,\\
 p_c(z)&=\frac{r[(9r+6)z^2-6rz-2]}D=p_a(1-z).
\end{aligned}
\]
Since \(p_b>0\), the negative mass is exactly
\[
 N(z)=\max\{0,-p_a(z),-p_c(z),-p_a(z)-p_c(z)\}.
\]
The two individual coefficient minima agree. Their common magnitude is
\[
 J(r)=\frac{r(3r^2+6r+4)}{(r+2)(3r+2)^2},
\]
found by minimizing the displayed quadratics (the vertex for \(p_a\) lies at \(z=2(r+1)/(3r+2)\in(0,1)\)). Also,
\[
 -p_a(z)-p_c(z)=\frac{r[6z(1-z)-1]}{r+2}
 \le\frac{r}{2(r+2)},
\]
with equality at \(z=1/2\), where both outer coefficients are negative and equal to \(-r/[4(r+2)]\).

For \(0<r\le2\), the inequality \(J(r)\le1/(r+2)\) follows from
\[
 (3r+2)^2-r(3r^2+6r+4)=-3r^3+3r^2+8r+4>0.
\]
For \(r\le1\) this is immediate; for \(1\le r\le2\), its right side is at least \(-3r^2+8r+4>0\). For \(r\ge2\), the bound \(J(r)\le r/[2(r+2)]\) is equivalent to \(3r^2\ge4\). Consequently, at every central point
\[
 N(z)\le\max\left\{\frac1{r+2},\frac r{2(r+2)}\right\}.
\]
The central midpoint attains the second value, and the outer endpoint attains the first. Therefore, globally,
\[
 N_* =\max\left\{\frac1{r+2},\frac r{2(r+2)}\right\},
 \qquad 1+\frac1{N_*}=\min\left\{r+3,3+\frac4r\right\}.
\]
This completes the all-real-points and all-positive-slope-triples sufficiency proof.

**5. Sharpness and unique mesh optimum.** If \(r\le2\) and \(K>r+3\), the slopes \((1,K,1)\) give
\[
 S'(0)=1-\frac{K-1}{r+2}<0.
\]
If \(r\ge2\) and \(K>3+4/r\), the slopes \((K,1,K)\) give
\[
 S'(1+r/2)=1-\frac{r(K-1)}{2(r+2)}<0.
\]
Both are genuine strictly increasing data triples, because \(K>1\). At equality the universal nonnegativity proof still applies. Finally \(r+3\) is strictly increasing and \(3+4/r\) strictly decreasing; they meet only at \(r=2\), where both equal \(5\). Thus the symmetric-mesh optimum is unique.

## Verification

Run `python3 verify_natural4_monotone.py` in the same directory. The standard-library verifier independently assembles the natural spline curvatures for rational knot ratios and secant-slope triples, checks the middle-interval coefficient identities, tests 5,050 exact-rational derivative evaluations across contrast-corner data and checks strictly negative witnesses just above every sharp cutoff. These checks passed. The exact inequalities in the proof establish the theorem for **every** real \(r>0\), continuous evaluation point and positive slope triple; the finite tests merely guard the algebra and implementation.

## Relationship to prior work

The classical Fritsch–Carlson characterization supplies necessary and sufficient conditions for an individual cubic Hermite segment to be monotone. It does **not** state the all-data four-knot natural-spline contrast radius or optimize the knot ratio. Aràndiga, Baeza and Yáñez (first public version 2021-02-23) analyze monotone cubic reconstruction and nonlinear derivative corrections; their sufficient conditions concern a different construction and do not establish this unchanged-natural-spline exact minimax. Baeza and Yáñez (public online 2022-06-22) prove that changing only endpoint first derivatives cannot always restore global monotonicity; that impossibility without any bounded secant contrast is consistent with the bounded-contrast threshold proved here. Beatson and Chacko (report dated 1990-11-30) compare spline boundary conditions, norms and approximation errors, not this uniform-in-data monotonicity radius.

The published **symmetric natural four-knot variation-optimality** result (public record `a68c76ffcd7c`) minimizes the unrestricted total-variation operator gain, with optimum \(r\approx1.42882553\); this is a different quantifier/objective from guaranteeing *zero derivative-sign changes* for slope-contrast-bounded increasing data, whose optimum is \(r=2\). The published equispaced natural four-knot variation constant (record `287732549e93`) likewise does not imply a positive-derivative contrast threshold. A separate four-knot **clamped-zero-first-derivative** contrast-four result has different endpoint conditions and different admissible data parameterization; it does not cover this natural-endpoint theorem. Exact-title, aliases, parameter, operator-norm and stronger-implication searches yielded no equivalent quantitative theorem in the inspected sources.

## Limitations

This is an exact finite-knot structural result: there is no statement for five or more knots, arbitrary asymmetric spacings, other endpoint conditions, or monotone data with unbounded secant contrast. It provides a sufficient-and-sharp **uniform guarantee**, not the necessary-and-sufficient condition for monotonicity of any particular data triple. It does not determine an approximation-error optimum or assert that \((1,2,1)\) optimizes total variation. Although the listed comparisons did not find exact coverage, unindexed historical equivalent formulae remain a priority risk; no independent review has occurred.

## References

- F. N. Fritsch and R. E. Carlson, *Monotone Piecewise Cubic Interpolation*, SIAM J. Numer. Anal. **17** (1980), 238–246. https://doi.org/10.1137/0717021
- F. Aràndiga, A. Baeza and D. F. Yáñez, *Monotone cubic spline interpolation for functions with a strong gradient*, first arXiv posting 2021-02-23. https://arxiv.org/abs/2102.11564
- A. Baeza and D. F. Yáñez, *A note on some bounds between cubic spline interpolants depending on the boundary conditions: Application to a monotonicity property*, Applied Numerical Mathematics **181** (2022), 320–325 (online 2022-06-22). https://doi.org/10.1016/j.apnum.2022.06.012 ; full author copy https://arxiv.org/abs/2402.01324
- R. K. Beatson and E. Chacko, *Which Cubic Spline Should One Use?*, University of Canterbury report 59 (1990-11-30), later SIAM J. Sci. Stat. Comput. **13** (1992), 1009–1024. https://ir.canterbury.ac.nz/server/api/core/bitstreams/76c796a1-5524-4a10-8394-a0e93ecc05e5/content
- Published natural four-knot variation-minimax finding (2026), record `a68c76ffcd7c`, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-unique-variation-optimal-symmetric-four-knot-natural-cubic-inter--a68c76ffcd7c
- Published natural four-knot equispaced-variation finding (2026), record `287732549e93`, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-total-variation-amplification-of-the-first-coupled-natural--287732549e93
