# A sharp antithetic coupling threshold for a three-stage two-derivative Runge–Kutta oscillator step

## Finding

**Theorem (complete binary curvature-error coupling classification).** The three-stage, fourth-order two-derivative Runge–Kutta rule TDRK3s4p2e of Gottlieb–Grant–Herrera [1, equation (5.5)] has an exact mean-square stability transition under coupled, unbiased relative errors in its two curvature evaluations. Let \(0<\epsilon\le1\), and let each relative error independently across *steps* take the marginal values \(+\epsilon\) and \(-\epsilon\) with probability \(1/2\). Within each step, permit any joint law with those marginals, and write \(p\in[0,1]\) for the probability that the two error signs agree. Define \(s=\epsilon^2\) and \(x=(h\omega)^2>0\).

For every nonzero deterministic initial vector and every iteration count \(k\ge0\), the exact expected squared Euclidean norm is
\[
\mathbb E\|u_k\|_2^2=m_{s,p}(x)^k\|u_0\|_2^2,
\quad
m_{s,p}(x)-1=\frac{x^3}{9216}\left[(1-s)^2x^2+16(3s-1)(x-4)+8sp\bigl((x-8)^2+16\bigr)\right].
\]
At **every** positive step and nonzero error amplitude, perfect antithetic coupling \(p=0\) uniquely minimizes expected squared energy among all couplings with those two symmetric marginals.

Mean-square convergence to zero at some positive step is possible **if and only if**
\[
\boxed{\frac13<s\le1,\qquad 0\le p<\frac{3s-1}{10s}.}
\]
For these parameters, convergence holds **precisely** for \(0<x<x_*(s,p)\), with a unique finite positive threshold. Set
\[
A=(1-s)^2+8sp,\quad B=16(3s-1)-128sp,\quad C=64(1-3s)+640sp.
\]
Then \(B>0\), \(C<0\), \(A\ge0\), and the threshold is defined without a removable singularity by
\[
\boxed{x_*=-\frac{2C}{B+\sqrt{B^2-4AC}}.}
\]
The single boundary step \(x=x_*\) is mean-square neutral; all larger positive steps grow exponentially in squared mean. Outside the boxed parameter regime every positive step grows exponentially in squared mean. In particular, unperturbed TDRK3s4p2e amplifies energy at every positive step except the isolated neutral step \(x=8\); independent stage-error signs (\(p=1/2\)) and perfectly shared signs (\(p=1\)) never restore mean-square stability. Yet strong enough antithetic *error coupling* creates a genuine stable interval at small steps.

For a concrete exact-rational contrast, take \(\epsilon=3/4\) and \(h\omega=1\). The antithetic and independent-sign schemes have respective one-step mean-square factors
\[
\boxed{m_{9/16,0}(1)=1-\frac{8399}{2359296}<1,
\qquad m_{9/16,1/2}(1)=1+\frac{29041}{2359296}>1.}
\]

## Assumptions and scope

Let \(J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\), \(\omega>0\), \(h>0\), and \(F(u)=\omega Ju\) on \(\mathbb R^2\). The exact total second derivative is \(G(u)=F'(u)F(u)=-\omega^2u\). At each time step sample signs \(S_0,S_1\in\{-1,+1\}\) with uniform marginals and \(\mathbb P(S_0=S_1)=p\). Use the *corrupted* curvature evaluations \(G_j(v)=-(1+\epsilon S_j)\omega^2v\), separately at the first and second stage; use the exact first-derivative evaluations throughout. The step is
\[
Y_1=u+\frac h2F(u)+\frac{h^2}{8}G_0(u),\quad
Y_2=u+hF(u)+\frac{h^2}{2}G_1(Y_1),\quad
u^+=u+\frac h6\bigl(F(u)+4F(Y_1)+F(Y_2)\bigr).
\]
The sign pairs are independent and identically distributed between time steps, but their two components can be dependent within each time step. The method is an idealized multiplicative-error oracle model, **not** a theorem about actual hardware rounding, stagewise stochastic-rounding algorithms, or accuracy of the resulting trajectory. The term *mean-square stable* here means \(\mathbb E\|u_k\|_2^2\to0\) for every deterministic \(u_0\); this is artificial damping relative to the energy-conserving exact oscillator, not automatically better physical fidelity.

## Proof

**Exact multiplier.** Fix one step and put \(z=h\lambda\), \(q_j=1+\epsilon S_j\), where \(\lambda\) is a scalar test eigenvalue. Direct substitution into the published three-stage update, with a corrupted second derivative \(q_j\lambda^2v\), gives the exact degree-five scalar multiplier
\[
R(z;q_0,q_1)=1+z+\frac{z^2}{2}+\frac{q_0+q_1}{12}z^3+\frac{q_1}{24}z^4+\frac{q_0q_1}{96}z^5.
\]
At \(z=i\sqrt{x}\), this is \(a+ib\), with
\[
a=1-\frac x2+\frac{q_1x^2}{24},\qquad
b=\sqrt x\left(1-\frac{(q_0+q_1)x}{12}+\frac{q_0q_1x^2}{96}\right).
\]
The corresponding real matrix is \(aI+bJ\), whose squared Euclidean norm multiplier is exactly \(a^2+b^2\) for **every** input vector. The only coupling compatible with the two uniform sign marginals has probabilities \(p/2,p/2,(1-p)/2,(1-p)/2\) on the sign pairs \((+,+),(-,-),(+,-),(-,+)\), respectively. Averaging the four explicitly stated \(a^2+b^2\) values and collecting powers of \(x\) gives the displayed formula for \(m_{s,p}(x)-1\). Stepwise independence now proves \(\mathbb E\|u_k\|_2^2=m_{s,p}(x)^k\|u_0\|_2^2\) by conditional expectation and induction, without any finite-enumeration assumption.

**Universal optimal coupling.** The exact difference from perfect antithetic coupling is
\[
m_{s,p}(x)-m_{s,0}(x)=\frac{8spx^3}{9216}\bigl((x-8)^2+16\bigr).
\]
It is strictly positive for \(s>0\), \(x>0\), \(p>0\). Thus \(p=0\) uniquely minimizes the one-step mean-square factor and, for nonzero initial data and every positive iteration count, the expected squared norm.

**Sharp phase classification.** Write the bracketed polynomial as \(Q_{s,p}(x)=Ax^2+Bx+C\) using the coefficients in the finding. For \(0<s<1/3\), the antithetic quadratic \(Q_{s,0}\) has leading coefficient \((1-s)^2>0\) and strictly negative discriminant \(256s(s+1)(3s-1)\); hence it is strictly positive on the real line. At \(s=1/3\), \(Q_{s,0}(x)=4x^2/9>0\) for \(x>0\). Increasing \(p\) increases \(Q\) strictly, so no coupling stabilizes any positive step when \(s\le1/3\).

For \(s>1/3\), put \(p_c=(3s-1)/(10s)\). At \(p=p_c\), the constant term is zero and the coefficient of \(x\) is \(\frac{16}{5}(3s-1)>0\), while \(A>0\). Consequently \(Q_{s,p_c}(x)>0\) for all \(x>0\); the same holds for \(p>p_c\). If \(0\le p<p_c\), then \(C<0\), \(B>0\) and \(A\ge0\); therefore \(Q\) is strictly increasing on \(x\ge0\), begins negative and tends to positive infinity. Its unique positive root is exactly the displayed \(x_*\); the rationalized expression also covers the only zero-leading-coefficient case \((s,p)=(1,0)\). Thus \(Q<0\) precisely below that root, vanishes only at the root, and is positive above. The sign of \(Q\) is the sign of \(m-1\), completing every case including the boundaries.

Finally, when \(s=0\) the scalar multiplier reduces to \(R(z)=1+z+z^2/2+z^3/6+z^4/24+z^5/96\), and \(m_{0,p}(x)-1=x^3(x-8)^2/9216\), giving the claimed unperturbed neutral point. The exact-rational example follows by direct substitution of \(x=1,s=9/16\) and \(p=0,1/2\).

## Verification

The standalone Python 3 standard-library program `verify.py` uses exact `fractions.Fraction` arithmetic. It reconstructs the three real-vector stages independently of the scalar polynomial, checks the complex-scalar reduction, checks the exact coupling average, and enumerates all sign histories through four steps. It also tests the rational witness and the small-step phase boundary. Running it on the packaged source produced `VERIFY_OK 1523 exact-rational assertions` (also retained in `verify_output.txt`). The finite checks are arithmetic regressions; the polynomial identities and all-parameter classification are proved above, not inferred from enumeration. Run with `python3 verify.py` alongside these files; no external modules or input datasets are required.

## Relationship to prior work

Gottlieb, Grant and Herrera [1, Section 5.2, equation (5.5)] define this exact three-stage method, derive its fourth-order consistency and second-order sensitivity to low-precision second derivatives, and display perturbed deterministic linear-stability regions. They do not provide an expectation-over-couplings formula, a comparison between all two-sign stage couplings, or a sharp noise-induced mean-square stability classification.

A published calculation [2] establishes an exact mean-square stability island for the *different two-stage* rule TDRK2s4p1e in [1, equation (5.4)] when its two curvature errors are **shared**. Its amplifier \(1+z+qz^2/2+qz^3/6+q^2z^4/24\) is not the degree-five two-error amplifier used here, and its separated-from-zero stability island does not imply the present small-step antithetic interval or the threshold \(s>1/3\). A published antithetic Heun study [3] optimizes coupling between sampled gradients of two positive quadratic components, a different degree-two multiplier; its finite-termination theorem does not cover noisy second derivatives or this fourth-order rule. Bochacik and coauthors [4] establish stability properties for randomized evaluation times in a two-stage first-derivative Runge–Kutta method, not the correlated curvature-oracle model above. These distinctions are comparisons of mathematical implications, not only titles.

## Limitations

The classification is limited to a single constant-frequency planar oscillator, this precise three-stage tableau, symmetric binary multiplicative errors on the second derivative only, and independent successive time steps. Correlation must be deliberately coupled; it does not describe generic stochastic rounding. The stabilizing relative-error amplitude exceeds \(1/\sqrt3\), much larger than ordinary floating-point roundoff. A smaller mean-square factor is **not** evidence of smaller global integration error or faithful energy dynamics: the exact physical system conserves energy. The theorem does not give a general noise-assisted stabilization prescription for nonlinear ODEs or high-dimensional noncommuting systems. Although directly relevant prior source text and published records were inspected, unindexed equivalent analyses remain a priority risk; independent audit is not claimed.

## References

[1] S. Gottlieb, Z. J. Grant and C. Herrera, *Mixed Precision and Mixed Accuracy Explicit Two-Derivative Runge–Kutta Methods*, arXiv:2602.14369v1, first publicly posted 2026-02-16, https://arxiv.org/html/2602.14369v1 .

[2] *A sharp mean-square stability island for fourth-order two-derivative Runge–Kutta under symmetric curvature perturbations*, publicly accessible 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-sharp-mean-square-stability-island-for-fourth-order-two-deriva--980ee5bd2be3 .

[3] *Antithetic stage pairing can terminate two-stage stochastic Heun in one update*, publicly accessible 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-antithetic-stage-pairing-can-terminate-two-stage-stochastic-heun--86322a4599c2 .

[4] T. Bochacik, M. Goćwin, P. M. Morkisz and P. Przybyłowicz, *Randomized Runge–Kutta method—stability and convergence under inexact information*, arXiv:2006.12131v1, first posted 2020-06-22, https://arxiv.org/html/2006.12131v1 .
