# Sharp alternating-step BDF3 parasitic damping without any ratio ceiling

## Finding

For every fixed ratio \(r>0\), apply the variable-step, third-order backward differentiation formula (BDF3), defined by differentiation of the cubic interpolant at the newest time node, on the infinite alternating positive-step pattern \(h,rh,h,rh,\ldots\), where \(h>0\). On the homogeneous test equation \(y'=0\), write \(\delta_n=y_n-y_{n-1}\) and \(v_n=(\delta_n,\delta_{n-1})^{\mathsf T}\). If \(P_r\) is the two-update matrix for these difference variables, put \(q=r+r^{-1}\). Then

\[
\operatorname{tr}P_r=\frac{-q^2+q+7}{5q^2+30q+41},\qquad
\det P_r=\frac{q+2}{5q^2+30q+41}.
\]

Let \(\varrho(r)=\rho(P_r)\) be the largest modulus of either Floquet multiplier. The following are **sharp and complete**:

1. For every finite positive ratio, \(\varrho(r)<1/5\), and \(\sup_{r>0}\varrho(r)=1/5\), approached only as \(r\to0\) or \(r\to\infty\). Thus *every fixed alternating ratio, however large, is zero-stable* for the homogeneous BDF3 recursion, with decaying parasitic differences.
2. There is a unique \(q_*>2\) satisfying

   \[
   q_*^4-22q_*^3-173q_*^2-390q_*-279=0.
   \]

   The global minimum of \(\varrho\) occurs **only** for the reciprocal ratio pair

   \[
   r_*=\frac{q_*+\sqrt{q_*^2-4}}2,\qquad r_*^{-1},
   \]

   and equals

   \[
   \min_{r>0}\varrho(r)=\sqrt{\frac{q_*+2}{5q_*^2+30q_*+41}}
   =0.0783782974843467\ldots.
   \]

   Numerically, \(q_*=28.5500009388038\ldots\) and \(r_*=28.5149315928808\ldots\). The minimum is the collision of the two negative real Floquet multipliers. For comparison, at uniform steps \(r=1\), the two-step parasitic spectral radius is \(2/11=0.181818\ldots\).

These results concern the **two-step Floquet spectral radius**, not a one-step amplification factor, a norm bound uniform over varying ratios, or the stability function on nonzero test equations.

## Assumptions and scope

Take any real or complex scalar starting triplet \((y_0,y_1,y_2)\); after this, use the unique variable-step BDF3 recurrence from the cubic interpolation formula at each node \(t_n\). The positive step lengths alternate between \(h\) and \(rh\) for all \(n\ge1\); shifting the phase exchanges \(r\) with its reciprocal and does not change the two-step spectrum. The ratio \(r\) is fixed as the number of time steps increases. No upper bound is imposed on this fixed \(r\), but constants controlling the values \(y_n\) are not claimed uniform as \(r\to0\) or \(r\to\infty\).

For a standard finite-horizon convergence interpretation, take fixed \(r\), let the maximum step tend to zero, and use an order-three-consistent starter and a sufficiently smooth right-hand side. The result supplies the homogeneous zero-stability component of the usual convergence argument; it does not claim arbitrary variable-grid stability.

## Proof

**1. Exact interpolation and difference transfer.** At a node whose current-to-previous step ratio is \(r\), rescale the current step to length one. Because the pattern alternates, the four cubic-interpolation nodes relative to the current node are

\[
0,\quad -1,\quad -1-r^{-1},\quad -2-r^{-1}.
\]

The coefficients of the derivative of the cubic interpolant, in newest-to-oldest order, are

\[
\begin{aligned}
w_0&=\frac{5r^2+5r+1}{(r+1)(2r+1)}, & w_1&=-2r-1,\\
w_2&=\frac{r(2r+1)}{r+1}, &w_3&=-\frac{r}{2r+1}.
\end{aligned}
\]

Their sum is zero. The equation \(w_0y_n+w_1y_{n-1}+w_2y_{n-2}+w_3y_{n-3}=0\) therefore gives

\[
\delta_n=a(r)\delta_{n-1}+b(r)\delta_{n-2},\qquad
 a(r)=\frac{r^2(4r+3)}{5r^2+5r+1},\quad
 b(r)=-\frac{r(r+1)}{5r^2+5r+1}.
\]

Let \(M(r)=\left(\begin{smallmatrix}a(r)&b(r)\\1&0\end{smallmatrix}\right)\). Two successive updates are \(P_r=M(r^{-1})M(r)\); reversing the order gives the similar matrix \(M(r)P_rM(r)^{-1}\), since \(b(r)\ne0\). Direct multiplication, followed by cancellation of \(r^2\), yields

\[
\operatorname{tr}P_r=\frac{-q^2+q+7}{D(q)},\qquad
\det P_r=\frac{q+2}{D(q)},\qquad D(q)=5q^2+30q+41,
\]

where \(q=r+r^{-1}\ge2\). In particular, the dimensionless two-step spectrum is independent of the overall step scale.

**2. Uniform sharp upper spectral bound.** The two multipliers are the roots of \(\lambda^2-t\lambda+d=0\), with \(t=(-q^2+q+7)/D(q)\) and \(d=(q+2)/D(q)\). For the rescaled roots \(z=5\lambda\), the real quadratic is \(z^2-5tz+25d\). The elementary degree-two strict Schur/Jury criterion is

\[
1-25d>0,\qquad 1-5t+25d>0,\qquad 1+5t+25d>0.
\]

These quantities have the explicitly positive numerators

\[
\frac{5q^2+5q-9}{D(q)},\qquad
\frac{10q^2+50q+56}{D(q)},\qquad
\frac{60q+126}{D(q)},
\]

for every \(q\ge2\). Hence both multipliers satisfy \(|\lambda|<1/5\). As \(q\to\infty\), \(t\to-1/5\) and \(d\to0\), so one multiplier approaches \(-1/5\) and the other approaches zero. This proves the sharp supremum. The difference vectors decay geometrically for each fixed ratio, and summing \(\delta_n\) proves that the values \(y_n\) remain bounded and converge.

**3. Exact global minimizer.** The unnormalized discriminant is

\[
\Delta(q)D(q)^2=(-q^2+q+7)^2-4(q+2)D(q)
=q^4-22q^3-173q^2-390q-279=:F(q).
\]

The coefficient signs of \(F\) have exactly one change, so Descartes' rule of signs gives at most one positive root. Since \(F(2)<0\) and \(F(q)\to+\infty\), the unique root \(q_*>2\) exists. For \(2\le q<q_*\), the Floquet roots are conjugate, so their common modulus is \(\sqrt{d(q)}\). Direct differentiation gives

\[
d'(q)=-\frac{5q^2+20q+19}{D(q)^2}<0,
\]

so the radius strictly decreases to \(q_*\). For \(q>q_*\), the roots are real; their trace is negative, and the larger modulus equals

\[
\varrho(q)=\frac{-t(q)+\sqrt{t(q)^2-4d(q)}}2.
\]

Here \(t(q)<0\) and

\[
t'(q)=-\frac{35q^2+152q+169}{D(q)^2}<0,\qquad d'(q)<0.
\]

Thus both \(-t\) and the positive square-root discriminant increase strictly with \(q\), proving the spectral radius increases strictly for \(q>q_*\). Consequently \(q_*\) is the unique minimizing shape parameter. The equation \(r+r^{-1}=q_*\) has exactly the two stated positive reciprocal solutions. The displayed minimum and numerical values follow by substitution.

## Verification

The standard-library script `verify_bdf3.py` independently reconstructs cubic derivative weights by exact rational Vandermonde elimination at eleven ratios, checks the transfer-matrix traces and determinants and the three strict Schur inequalities at those ratios, and isolates the quartic root by high-precision decimal bisection. It reports 163 separate exact identity/inequality and interval assertions. The analytic proof above supplies the universal quantifiers; finite checks and printed decimals do not prove them. A recorded script output is included as `verification_output.txt`.

## Relationship to prior work

Li and Liao (arXiv:2201.00527v1, equations (1.1)–(1.5), Theorem 3.1, and Remarks 1–4) develop variable-step BDF2/BDF3 stability and give a **sufficient** bound around \(2.553\) on adjacent BDF3 ratios for their perturbed stability framework. They explicitly note this bound is far from necessary and analyze the general variable-ratio transfer matrices, but do not state or imply this reciprocal-period-two Floquet formula, the absence of a ratio ceiling on that restricted grid family, or the globally optimal alternating ratio.

Chen, Yu, Zhang and Zhang (arXiv:2112.13613, particularly equations (1.4)–(1.5) and Theorem 4.2) prove energy stability for a variable-step BDF3 discretization of the Allen–Cahn equation under a different restrictive ratio bound. Their positive-definiteness and PDE-energy estimates do not give the present unrestricted periodic-grid zero-stability law. Söderlind, Fekete and Faragó (2018, DOI 10.1007/s10543-018-0716-y, Sections 2–4) treat **smoothly deformed grids** with adjacent ratios tending to one under refinement, an assumption violated by any fixed nonunit alternating ratio. Earlier literature by Grigorieff–Paes-Leme (1984) and Guglielmi–Zennaro (2001) covers BDF3 zero-stability and joint spectral-radius bounds; their full original texts were not verified for an exact periodic special case. These are residual novelty risks, not proof of absence of overlap.

## Limitations

Zero-stability is not absolute stability on \(y'=\lambda y\) for \(\lambda\ne0\); no property of stiff or nonlinear equations follows automatically. Floquet spectral contraction is not a uniform bound on the norms of individual update matrices or transient amplification as \(r\) becomes arbitrarily extreme. Arbitrary sequences of changing ratios are not covered. The convergence consequence for sufficiently smooth problems requires the usual consistency and starter hypotheses. Uninspected historical specialist results could contain an equivalent special case; an independent literature audit has not been performed.

## References

- Z. Li and H.-L. Liao, *Stability of variable-step BDF2 and BDF3 methods*, first publicly available 3 January 2022, arXiv:2201.00527v1, https://arxiv.org/abs/2201.00527.
- M. Chen, F. Yu, Q. Zhang and Z. Zhang, *Variable step-size BDF3 method for Allen-Cahn equation*, arXiv:2112.13613, https://arxiv.org/abs/2112.13613.
- G. Söderlind, I. Fekete and I. Faragó, *On the zero-stability of multistep methods on smooth nonuniform grids*, BIT Numerical Mathematics (2018), DOI:10.1007/s10543-018-0716-y, https://real.mtak.hu/85237/1/B111_BIT.pdf.
- R. D. Grigorieff and P. J. Paes-Leme, *On the zero-stability of the 3-step BDF-formula on nonuniform grids*, BIT 24 (1984), 85–91, DOI:10.1007/BF01934518.
- N. Guglielmi and M. Zennaro, *On the zero-stability of variable stepsize multistep methods: the spectral radius approach*, Numerische Mathematik 88 (2001), 445–458, https://hdl.handle.net/11368/1703201.
