# Four sharp mode-selection regimes for sixth-moment Poisson smoothing of real two-tone Fourier signals

## Finding

Let \(1\le m<n\) be integers, let \(0<\rho\le1\), and let \(P_\rho\) denote the circle Poisson operator \(P_\rho e^{ij\theta}=\rho^{|j|}e^{ij\theta}\). On the real four-dimensional space
\[
E_{m,n}=\operatorname{span}_{\mathbb R}\{\cos(m\theta),\sin(m\theta),\cos(n\theta),\sin(n\theta)\},
\]
write \(\mathcal N_{m,n}(\rho)=\|P_\rho|_{E_{m,n}}\|_{L^2(\mathbb T)\to L^6(\mathbb T)}\), with normalized Haar measure. Put \(t=\rho^{2(n-m)}\) and \(u=\sqrt t\), and, for \(z\ge0\), define
\[
F_0(t,z)=\frac{1+9tz^2+9t^2z^4+t^3z^6}{(1+z^2)^3},
\]
\[
\begin{aligned}
F_2(t,z)&=F_0(t,z)+\frac{3tz^2}{2(1+z^2)^3},\\
F_3(t,z)&=F_0(t,z)+\frac{3uz+6u^3z^3}{(1+z^2)^3},\\
F_5(t,z)&=F_0(t,z)+\frac{3uz}{5(1+z^2)^3}.
\end{aligned}
\]
Use \(F_k\) when \(n=km\), \(k\in\{2,3,5\}\), and \(F_0\) otherwise. Then the **exact sharp norm** is
\[
\boxed{\mathcal N_{m,n}(\rho)^6=\frac52\rho^{6m}\max_{z\in[0,\infty]} F_k(t,z).}
\]
The endpoint \(z=\infty\) is understood as the continuous limit \(t^3\).

The maximizing relative amplitude \(z=|v|/|u_0|\) for \(f(\theta)=\operatorname{Re}(u_0e^{im\theta}+ve^{in\theta})\), with \(u_0\ne0\), has precisely **four** possibilities:

1. If \(n/m\notin\{2,3,5\}\): the unique maximizing amplitude is \(z=0\) exactly when \(t\le1/3\). At \(t>1/3\) a unique \(z>0\) maximizes, and its phases are arbitrary.
2. If \(n=2m\): the unique maximizing amplitude is \(z=0\) exactly when \(t\le2/7\). At \(t>2/7\) a unique positive \(z\) maximizes, and its phases satisfy \(2(\arg v-2\arg u_0)\equiv0\pmod{2\pi}\).
3. If \(n=3m\): the unique maximizing amplitude is positive at **every** \(\rho>0\), and the phases satisfy \(\arg v-3\arg u_0\equiv0\pmod{2\pi}\). As \(t\downarrow0\), \(z=\frac12\sqrt t+O(t^{3/2})\).
4. If \(n=5m\): the unique maximizing amplitude is positive at **every** \(\rho>0\), and the phases satisfy \(\arg v-5\arg u_0\equiv0\pmod{2\pi}\). As \(t\downarrow0\), \(z=\frac1{10}\sqrt t+O(t^{3/2})\).

At a pure-mode maximum the lower-frequency phase is arbitrary and the upper-frequency phase is irrelevant. In each mixed case the positive maximizing \(z\) is the **unique positive root** of
\[
(1+z^2)\,\partial_z N_k(t,z)-6zN_k(t,z)=0,
\]
where \(N_k=(1+z^2)^3F_k\); this is an explicit polynomial of degree at most five. Thus the formula specifies every sharp norm and every norming function without numerical optimization.

At the two nonpersistent thresholds, the upper-frequency *input energy fraction* \(q=z^2/(1+z^2)\) emerges continuously. More precisely, for the nonresonant and twice-frequency cases respectively,
\[
q=\frac94(t-\tfrac13)+O((t-\tfrac13)^2),\qquad
q=\frac{343}{148}(t-\tfrac27)+O((t-\tfrac27)^2).
\]
At the persistent resonances \(n=3m,5m\), the same fraction is respectively \(q=t/4+O(t^2)\) and \(q=t/100+O(t^2)\) as \(t\downarrow0\).

## Assumptions and scope

Inputs are arbitrary nonzero *real-valued* functions in \(E_{m,n}\), including all independent sine/cosine phases and the possibility of one zero coefficient. The circle has normalized Haar probability measure. There is no zero-frequency component. The operator is the ordinary Poisson Fourier multiplier, not a heat multiplier. All integer pairs \(1\le m<n\) and all \(0<\rho\le1\) are covered. For \(\rho=0\) the operator vanishes, so the equality classification changes and is excluded. Norms are positive real operator norms, not coefficient-only moments. Exact algebraic equations determine the mixed optimizers, without claiming a radicals formula for the quintic cases.

## Proof

**1. Exact sixth-moment expansion.** Represent a real input as
\[
f(\theta)=\sqrt2\big(a\cos(m\theta+\alpha)+b\cos(n\theta+\beta)\big),
\quad a,b\ge0,
\]
so that \(\|f\|_2^2=a^2+b^2\). Write \(A=\rho^ma\) and \(B=\rho^nb\). Expanding the sixth power of \(P_\rho f\) and integrating its signed Fourier characters, the universal term is
\[
\|P_\rho f\|_6^6=\frac52(A^6+B^6)+\frac{45}{2}(A^4B^2+A^2B^4)+R,
\]
with the exact extra resonance term
\[
R=\begin{cases}
\frac{15}{4}A^4B^2\cos\big(2(\beta-2\alpha)\big),&n=2m,\\
\big(\frac{15}{2}A^5B+15A^3B^3\big)\cos(\beta-3\alpha),&n=3m,\\
\frac32A^5B\cos(\beta-5\alpha),&n=5m,\\
0,&\text{otherwise}.
\end{cases}
\]
Indeed, any nontrivial signed-frequency zero-sum relation involving both frequencies in six factors has a primitive ratio \(2:1,3:1\), or \(5:1\); the \(2:1\) relation must occur twice. Ratios with primitive relation of odd length five cannot occupy an even number six of factors. The exact coefficients follow by binomial counting; the standalone checker independently enumerates the relevant zero-sum sextuples.

Each nonzero resonance term is maximized by setting its displayed cosine to \(1\), since its amplitude factor is strictly positive. With \(z=b/a\), division by \(\|f\|_2^6\) and \(\rho^{6m}\) gives precisely \(\frac52F_k(t,z)\). Zero-coefficient cases follow by continuity.

**2. Nonresonant and octave thresholds.** Set \(q=z^2/(1+z^2)\), the upper-frequency input energy fraction, so \(0\le q\le1\). For \(k=0,2\) the reduced norm factor is
\[
H_k(t,q)=(1-q)^3+t^3q^3+c_kt(1-q)^2q+9t^2(1-q)q^2,
\]
where \(c_0=9\) and \(c_2=21/2\). Expanding \(H_k=1+Aq+Bq^2+Cq^3\) gives
\[
A=c_kt-3,\quad B=3-2c_kt+9t^2,\quad C=-1+c_kt-9t^2+t^3.
\]
At \(t=3/c_k\), the linear coefficient is zero. In the generic case \((B,C)=(-2,28/27)\); in the octave case \((B,C)=(-111/49,442/343)\). Hence \(B<0\) and \(B+C<0\), so \(H_k(t,q)<1\) for every \(q>0\) at the threshold. For smaller positive \(t\), all original summands are monotone increasing in \(t\) at fixed \(q>0\), so the inequality remains strict. At larger \(t\), \(\partial_qH_k(t,0)=A>0\) while \(\partial_qH_k(t,1)=3t^2(t-3)<0\). Since this derivative is a quadratic, these opposite endpoint signs imply exactly one zero in \((0,1)\), a strict global maximizer. This proves both thresholds, uniqueness and phase classifications.

Expanding the unique critical root near the two thresholds gives \(q=-A/(2B)+O(A^2)\), yielding exactly \(9/4\) and \(343/148\) as stated.

**3. Persistent third- and fifth-harmonic resonances.** Put \(u=\sqrt t\in(0,1]\). For the third harmonic, differentiation of \(F_3=N_3/(1+z^2)^3\) gives the numerator
\[
\begin{aligned}
P_3(z)={}&(6u^6-18u^4)z^5-18u^3z^4
 +(36u^4-36u^2)z^3\\
&+(18u^3-15u)z^2+(18u^2-6)z+3u.
\end{aligned}
\]
The coefficients in descending powers have exactly one sign change for \(0<u\le1\): the leading three are nonpositive, the quadratic coefficient can be positive only when \(u^2>5/6\), when the linear coefficient is already positive, and the constant is positive. Thus Descartes' rule gives at most one positive root. Since \(P_3(0)=3u>0\) and the leading coefficient is negative, exactly one exists, and \(F_3\) increases then decreases through it. It is the unique global maximizer and strictly improves on both pure modes.

For the fifth harmonic the corresponding numerator is
\[
P_5(z)=(6u^6-18u^4)z^5+(36u^4-36u^2)z^3-3uz^2
+(18u^2-6)z+3u/5.
\]
Its descending coefficients also have exactly one sign change (including zero coefficients). Its positive constant and negative leading coefficient likewise give precisely one positive root, a strict global maximizer. The phase alignments follow from Step 1.

The small-\(u\) equations \(P_3(z)=3u-6z+O(u^3)\) and \(P_5(z)=3u/5-6z+O(u^3)\) at \(z=O(u)\) give, by the implicit-function theorem, \(z=u/2+O(u^3)\) and \(z=u/10+O(u^3)\). The stated energy-fraction laws follow by squaring.

## Verification

Run `python3 artifacts/verify.py` using the Python standard library. Its 19,653 checks include exhaustive exact signed-character sixth-moment enumeration for \(1\le m<25\), \(m<n<75\), exact rational tests of both threshold factorizations and stationary endpoint signs, independent arbitrary-phase coefficient convolutions, and direct comparisons of the reduced maximization formulas against sixth moments computed by Parseval of the cubed signal. Exact universal frequency classification, polynomial sign arguments, and asymptotic steps are provided above; finite testing alone would not prove them.

## Relationship to prior work

The published *Sixth-moment resonance trichotomy and strict lower-norm cancellation for real two-tone Fourier planes* gives the unsmoothed sixth-moment resonance expansion and sharp \(\rho=1\) extrema; it is a premise for comparison, not a novelty claim here. The published *Resonant persistence and sharp mode selection for two-frequency circular Poisson smoothing* settles the different \(L^2\to L^4\) problem (with only the \(1:3\) resonance). The present claim determines the exact Poisson-smoothed **sixth** norm for every radius, including new octave and nonresonant mixing thresholds, all positive-radius optimizer uniqueness, and persistent fifth-harmonic mixing not present at fourth moment. Global Poisson hypercontractivity theory, including Frank–Ivanisvili (2021), studies the unrestricted operator and does not itself imply these restricted sharp norming functions or thresholds.

## Limitations

This concerns the full real sine/cosine planes only, not complex-valued unrestricted Laurent-polynomial input spaces, more than two frequency magnitudes, general \(L^p\) exponents, or other semigroups. Some exact moment identities and the unsmoothed endpoints were known already and are not independently claimed. The algebraic optimizer equations can be solved numerically but are not expressed by radicals. The full text of certain older or broader historical sources was unavailable; an unindexed equivalent sixth-moment semigroup treatment remains a priority risk. Independent scientific validation has not been performed.

## References

1. R. L. Frank and P. Ivanisvili, *Hypercontractivity of the semigroup of the fractional Laplacian on the n-sphere*, arXiv:2101.06209v1, first public 2021-01-15, https://arxiv.org/abs/2101.06209; Journal of Functional Analysis 281 (2021), 109145.
2. P. Ivanisvili, A. Lindenberger, P. F. X. Müller, and M. Schmuckenschläger, *Hypercontractivity on the unit circle for ultraspherical measures: linear case*, arXiv:2004.05567v1, 2020-04-12, https://arxiv.org/abs/2004.05567.
3. *Sixth-moment resonance trichotomy and strict lower-norm cancellation for real two-tone Fourier planes*, public mathematical result (full `RESULT.md` compared), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sixth-moment-resonance-trichotomy-and-strict-lower-norm-cancella--6e8aaec258be.
4. *Resonant persistence and sharp mode selection for two-frequency circular Poisson smoothing*, public mathematical result (full `RESULT.md` compared), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-resonant-persistence-and-sharp-mode-selection-for-two-frequency--ebfd25bec609.
