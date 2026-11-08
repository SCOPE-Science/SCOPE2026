# Thermal broadening preserves the strict ordering of two non-Gaussianity-optimal reset rates

## Finding

For a harmonic particle driven simultaneously by Poisson-reset Brownian active forcing and independent Gaussian thermal noise, the standardized stationary fourth and sixth cumulants are each strictly positive and have exactly one global maximizer over positive forcing-reset rates. **For every finite nonnegative thermal-to-active intensity ratio, the sixth-cumulant optimum occurs at a strictly faster reset rate than the fourth-cumulant optimum.** Both optimal reset-rate ratios grow strictly with thermal intensity, but remain in fixed finite intervals.

More precisely, define \(b=r/\mu>0\) and \(q=T/(2D)\ge0\). Let \(K_4=\operatorname{cum}_4(X)/\operatorname{Var}(X)^2\) and \(K_6=\operatorname{cum}_6(X)/\operatorname{Var}(X)^3\) for the unique stationary position. Then

\[
K_4(b,q)=\frac{6b^2(7b+3)}{(b+2)(b+3)[b+q(b+1)]^2},
\]
\[
K_6(b,q)=\frac{120b^3(205b^4+1077b^3+1694b^2+876b+180)}{(b+2)^2(b+3)^2(b+4)(b+5)[b+q(b+1)]^3}.
\]

Write \(b_4(q)\) and \(b_6(q)\) for their respective unique positive global maximizers. For every finite \(q\ge0\),

\[
0<b_4(0)<b_4(q)<5\quad(q>0),\qquad 0<b_6(0)<b_6(q)<6\quad(q>0),
\]
\[
\boxed{\ b_4(q)<b_6(q)\ }.
\]

At zero thermal intensity, \(b_4(0)=3(\sqrt{22}-1)/7=1.5816067542\ldots\), whereas \(b_6(0)=2.7251795494\ldots\). At \(q=1\) the optima are approximately \(3.3095434854\) and \(4.1086409486\). As \(q\to\infty\), they converge to \(4.3968704176\ldots\) and \(5.0521394452\ldots\), respectively. In particular the sixth-optimum shift never collapses into the fourth-optimum shift under thermal broadening.

## Assumptions and scope

Fix \(\mu,r,D>0\) and \(T\ge0\). On a two-sided stationary realization, the state evolves as

\[
dX_t=(-\mu X_t+rY_t)\,dt+\sqrt{2T}\,dW_t,\qquad
 dY_t=\sqrt{2D}\,dB_t
\]

between jumps of an independent Poisson process of intensity \(r\). At each jump \(Y\) alone is replaced by zero while \(X\) is unchanged. \(B,W\), and the Poisson process are mutually independent. The continuous equation for \(Y\) is interpreted only between resetting times. \(X\) is the stationary position and all cumulants are ordinary classical cumulants. No claim is made for zero active intensity \(D=0\), zero trap strength \(\mu=0\), or the singular excluded rate \(r=0\). The dimensionless thermal ratio is \(q=T/(2D)\); it is independent of \(r\).

A stationary solution exists by integrating the exponentially stable position kernel against the stationary resetting Brownian driver and an independent stationary Ornstein–Uhlenbeck thermal component. The reset Brownian driver is stationary with finite moments of every order because its elapsed time since the previous reset has an exponential law. Standard moment bounds for the stable convolution ensure that the position also has finite moments of every order.

## Proof

**1. Stationary moments and Gaussian convolution.** By linearity and independence, \(X=X_{\rm act}+X_{\rm th}\), where \(X_{\rm th}\) is centered Gaussian of variance \(T/\mu\), independent of \(X_{\rm act}\). All cumulants of order four or higher are therefore unchanged by adding \(X_{\rm th}\). The active variance is \(2Db/[\mu(b+1)]\), so the full variance is

\[
 V=\operatorname{Var}(X)=\frac{2D}{\mu}\left[q+\frac{b}{b+1}\right]>0.
\]

For independent reconstruction, set \(\mu=D=1\), \(r=b\), and \(T=2q\). Writing \(M_{ij}=\mathbb E[X^iY^j]\), with \(M_{00}=1\) and negative-index moments zero, stationary generator balance gives for \(i+j>0\)

\[
 (i+b\mathbf1_{j>0})M_{ij}=ibM_{i-1,j+1}+j(j-1)M_{i,j-2}+2q\,i(i-1)M_{i-2,j}.
\]

For each fixed total degree, evaluating the identities in increasing \(i\) is triangular. The resulting second, fourth and sixth moments give

\[
\frac{\operatorname{cum}_4(X)}{V^2}=K_4(b,q),\qquad
\frac{\operatorname{cum}_6(X)}{V^3}=K_6(b,q)
\]

with the stated rational expressions. Equivalently the \(q=0\) moments reproduce equations (188)–(190) of Guéneau–Majumdar–Schehr; adding the independent Gaussian changes only the second cumulant. Every displayed numerator and denominator is strictly positive for \(b>0,q\ge0\).

**2. Unique global optimizers.** Put \(w=b+q(b+1)>0\). Direct differentiation and simplification give

\[
\partial_bK_4=-\frac{6bP_4(b,q)}{(b+2)^2(b+3)^2w^3},
\qquad
\partial_bK_6=-\frac{120b^2P_6(b,q)}{(b+2)^3(b+3)^3(b+4)^2(b+5)^2w^4},
\]

where

\[
P_4=(7q+7)b^4+(6-q)b^3-(97q+27)b^2-141qb-36q
\]

and

\[
\begin{aligned}
P_6={}&(410q+410)b^9+(4871q+5076)b^8+(13097q+19862)b^7\\
&+(7926-66193q)b^6-(522631q+132670)b^5\\
&-(1433038q+330840)b^4-(1973436q+278100)b^3\\
&-(1390392q+59400)b^2-457920qb-64800q.
\end{aligned}
\]

For each \(q\ge0\), either polynomial's nonzero coefficients in descending degree have **exactly one sign change**. For \(q=0\) omit the trailing zero coefficients. Both polynomials are negative for sufficiently small positive \(b\), and positive for sufficiently large \(b\). Descartes' rule therefore gives exactly one positive zero of each, with sign changing negative to positive there. Hence both cumulants increase strictly up to the corresponding zero and decrease strictly afterward. Their limits at \(b\to\infty\) are zero; the \(q>0\) limits at \(b\downarrow0\) are also zero. For \(q=0\), the respective small-\(b\) limits are \(3\) and \(30\), each below its interior maximum. Thus each positive zero is the unique global maximizer. Evaluating \(P_4(5,q)=2(542q+2225)>0\) and \(P_6(6,q)=7776(834743q+2194554)>0\) establishes \(b_4(q)<5\) and \(b_6(q)<6\).

**3. Both maximizers increase with thermal intensity.** Factor each cumulant as

\[
K_{2m}(b,q)=K_{2m}(b,0)\left[\frac{b}{b+q(b+1)}\right]^m,\qquad m=2,3.
\]

For any fixed \(b>0\), the logarithmic derivative in \(b\) of the thermal factor is \(m q/[b(b+q(b+1))]\), strictly increasing with \(q\). For \(q_2>q_1\), the derivative of \(\log K_{2m}(b,q_2)\) is strictly positive at the unique maximizer for \(q_1\). Since the derivative has one positive zero, its zero for \(q_2\) lies strictly to the right. This proves both strict monotonicities, including comparisons with \(q=0\).

**4. Strict ordering, uniformly in temperature.** The ratio \(K_6^2/K_4^3\) is *independent of \(q\)* because the Gaussian thermal variance cancels between the normalizations. Let \(F(b)=K_6(b,0)^2/K_4(b,0)^3\). Algebra gives

\[
\frac{d}{db}\log F(b)=\frac{H(b)}{(b+2)(b+3)(b+4)(b+5)(7b+3)A(b)},
\]

where \(A(b)=205b^4+1077b^3+1694b^2+876b+180>0\), and

\[
\begin{aligned}
H(b)={}&-1435b^8-8472b^7+52694b^6+602850b^5\\
&+2114117b^4+3534090b^3+2901096b^2\\
&+1014660b+64800.
\end{aligned}
\]

For \(0<b\le5\), the inequalities \(b^8\le125b^5\) and \(b^7\le25b^5\) imply

\[
H(b)\ge (602850-1435\cdot125-8472\cdot25)b^5
+52694b^6+2114117b^4+\cdots+64800>0.
\]

At \(b=b_4(q)<5\), differentiation of \(\log F=2\log K_6-3\log K_4\) thus yields \(2\partial_b\log K_6=\partial_b\log F>0\). The unique maximum of \(K_6\) must therefore occur strictly to the right: \(b_6(q)>b_4(q)\).

**5. Large-temperature limits.** Dividing each derivative polynomial by \(q\) and letting \(q\to\infty\), strict monotonicity and the uniform bounds in Step 2 identify the finite limits as the unique positive zeros of

\[
7b^4-b^3-97b^2-141b-36=0
\]

and

\[
\begin{aligned}
410b^9+4871b^8+13097b^7-66193b^6-522631b^5\\
-1433038b^4-1973436b^3-1390392b^2-457920b-64800=0.
\end{aligned}
\]

Both have exactly one positive zero by the same coefficient-sign argument; their numerical values were stated above. This completes the proof.

## Verification

Run `python verify.py` with Python 3 and SymPy installed. The program independently reconstructs the stationary generator moment recurrence through degree six, checks both standardized cumulant formulas and derivative factorizations, verifies the thermal cancellation and ordering polynomial, asserts coefficient sign patterns and endpoint signs, and computes independent numerical positive roots at several exact rational thermal intensities. Exact symbolic identities are proof checks; the root samples illustrate, rather than establish, the global theorems.

## Relationship to prior work

Guéneau, Majumdar and Schehr (arXiv:2306.09453, first public 2023-06-15) introduce the **same Brownian force-reset model without independent thermal diffusion**, its Kesten representation, and the complete second/fourth/sixth stationary moments. Those moments are foundational inputs already known; this finding does not claim them as new. The contribution is the thermal-broadened, two-observable *global optimization theorem*: unique fourth- and sixth-cumulant maxima for all thermal ratios, strict temperature monotonicity of both rates, their uniform strict ordering, and an algebraic temperature-invariant comparison mechanism. These statements are not explicitly present in the inspected full original text, although they are derivable from its moment formulas plus independent Gaussian convolution and new sign arguments.

Di Bello et al. (arXiv:2309.13424, first public 2023-09-23) consider a different active force composed of **instantaneous compound-Poisson kicks** on a thermally diffusing trapped particle; the noise is not a Brownian force restarted at Poisson epochs. Their kurtosis analysis is an important conceptual comparison, not a formula covering the result here. Olsen (Phys. Rev. E 108, 044120, 2023) examines **resets of the particle position** to random positions, not resets solely of a Brownian active force. The prior generality of Gaussian convolution and the existence of the original moment formulas mean the originality claim is solely for the joint optimization and ordering theorem, not for the model, convolution principle, or moment recurrence.

## Limitations

Only the dimensionless stationary one-dimensional overdamped model above is treated; no statement is made for inertial dynamics, non-Poisson reset clocks, correlated thermal and active noises, or cumulant orders above six. Standardized fourth and sixth cumulants have different statistical meanings and are not directly interchangeable measures of tail risk. Numerical optimizer values are approximate, whereas uniqueness and ordering are exact. Because earlier work already provides all unbroadened low-order moments and Gaussian broadening is elementary, publication priority for the combined optimization statement could require further expert literature review. This is a self-contained mathematical analysis, not an independent external validation.

## References

1. M. Guéneau, S. N. Majumdar and G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, arXiv:2306.09453 (first public 2023-06-15), https://arxiv.org/abs/2306.09453. In particular Sec. 4.2 and Appendix E, equations (188)–(190).
2. C. Di Bello, R. Majumdar, R. Marathe, R. Metzler and E. Roldán, *Brownian particle in a Poisson-shot-noise active bath: exact statistics, effective temperature, and inference*, arXiv:2309.13424 (first public 2023-09-23), https://arxiv.org/abs/2309.13424.
3. K. S. Olsen, *Steady-state moments under resetting to a distribution*, Physical Review E 108, 044120 (2023), https://doi.org/10.1103/PhysRevE.108.044120.
