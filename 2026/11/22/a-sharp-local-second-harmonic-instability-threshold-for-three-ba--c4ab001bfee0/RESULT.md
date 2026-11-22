# A sharp local second-harmonic instability threshold for three-band circular Poisson smoothing

## Finding

Let \(P_\rho e^{ik\theta}=\rho^{|k|}e^{ik\theta}\) be the classical circle Poisson semigroup, with \(0<\rho<1\). On the **real, mean-zero, three-band** space
\[
\mathcal H_3=\operatorname{span}_{\mathbb R}\{\cos(j\theta),\sin(j\theta):j=1,2,3\},
\]
consider the sharp restricted ratio \(\|P_\rho f\|_4^4/\|f\|_2^4\), with normalized Haar measure. Put \(s=\rho^2\). The unique maximizing family under the restriction that the second frequency vanishes is
\[
f_s(\theta)=C[\cos(\theta-\alpha)+x_s\cos(3(\theta-\alpha))],
\]
where \(C\ne0\), \(\alpha\in\mathbb R\), and \(x_s\) is the **unique positive** root of
\[
P_s(x)=3s^2(s^2-2)x^3-3sx^2+(6s^2-3)x+s=0.
\]
Exactly one sharp local stability change occurs as this restricted normer is allowed to acquire a second harmonic. It is at \(s=s_c=0.507643227655645\ldots\), the **unique** root in \((507/1000,508/1000)\) of
\[
Q(s)=112s^5-240s^4+165s^3-79s^2+57s-18.
\]
Equivalently, \(\rho_c=\sqrt{s_c}=0.712490861454127\ldots\). For \(0<s<s_c\) the restricted normer is a strict local maximizer in the entire real six-dimensional space, modulo scaling and translation. For \(s_c<s<1\) it is transversely unstable: adding a suitably phased, arbitrarily small second harmonic **strictly increases** the norm ratio. Consequently **every global normer has a nonzero second harmonic** for every \(s>s_c\). Conversely, for every \(0<s\le2/5\), **every global normer has zero second harmonic** and equals the displayed restricted family.

The claim is an exact **local** instability threshold and two rigorously proved global regimes; it does **not** assert that the global mode-onset threshold equals \(s_c\) or that no first-order global transition occurs in the intervening range.

## Assumptions and scope

All functions are real-valued, trigonometric and mean zero. Each of the three complete real harmonic eigenspaces, including independent sine/cosine phases, is allowed. The input is normalized using \(\|f\|_2\), and all integrals use \(d\theta/(2\pi)\). The smoothing parameter is \(0<\rho<1\) (the identity endpoint is used only for a sign calculation). No result is asserted for the heat semigroup, complex-valued signals, higher frequencies, or other exponents.

## Proof

**1. Exact fourth moment and phases.** Write \(f=a\cos(\theta+\alpha)+b\cos(2\theta+\beta)+c\cos(3\theta+\gamma)\), with \(a,b,c\ge0\). Orthogonality gives \(\|f\|_2^2=(a^2+b^2+c^2)/2\). Expanding the zero-sum Fourier quadruples shows that the fourth moment after applying \(P_\rho\) is bounded above by
\[
\begin{aligned}
F_\rho(a,b,c)={}&\tfrac38(A^4+B^4+C^4)+\tfrac32(A^2B^2+A^2C^2+B^2C^2)\\
&+\tfrac12 A^3C+\tfrac32 AB^2C,
\end{aligned}
\]
where \(A=\rho a\), \(B=\rho^2b\), \(C=\rho^3c\). Equality can be attained **simultaneously** in both resonant terms by setting \(\gamma=3\alpha\) and \(2\beta=\alpha+\gamma\pmod {2\pi}\). Thus maximization over the entire real six-dimensional space reduces exactly to nonnegative amplitudes. Multiplying \(F_\rho\) by four gives the fourth power of the norm ratio on the unit amplitude sphere.

**2. Restricted maximizer and a transverse coordinate.** Normalize \(a^2+b^2+c^2=1\). For \(b=0\) put \(x=c/a\). The fourth moment is
\[
A_s(x)=\frac{s^2}{8}\frac{3+4sx+12s^2x^2+3s^4x^4}{(1+x^2)^2}.
\]
Its derivative has numerator \(4P_s(x)\), with the positive denominator \((1+x^2)^3\). The coefficients of \(P_s\), in descending order, have exactly one sign change for every \(0<s<1\). By Descartes' rule, \(P_s(0)=s>0\) and its negative leading coefficient, there is precisely one simple positive root \(x_s\); the objective increases before and decreases after that root. Neither pure first nor pure third frequency is a restricted global maximizer.

Let \(v=b^2\in[0,1]\) and keep the ratio \(c/a=x\). The exact phase-aligned fourth moment is
\[
F_s(v,x)=(1-v)^2A_s(x)+v(1-v)H_s(x)+v^2D_s,
\]
where
\[
H_s(x)=\frac{3s^3}{2}\frac{1+sx+s^2x^2}{1+x^2},\qquad D_s=\frac38s^4.
\]
Hence the coefficient of \(v\) at the restricted normer is
\[
H_s(x_s)-2A_s(x_s)=\frac{s^2}{4(1+x_s^2)^2}R_s(x_s),
\]
with
\[
R_s(x)=6s(1+sx+s^2x^2)(1+x^2)-(3+4sx+12s^2x^2+3s^4x^4).
\]
For all possible phases of the entering second harmonic this is the **largest** quadratic coefficient. If negative, strict local maximality follows also in the transverse phase directions; the first/third relative phase has strictly negative curvature, and the unique restricted radial maximizer has negative radial curvature. If positive, the phase-aligned perturbation strictly improves the quotient.

**3. Exact uniqueness and sign of the instability threshold.** A direct polynomial resultant gives the identity
\[
\operatorname{Res}_x(P_s,R_s)=54s^6Q(s)E(s),\quad E(s)=9(s^4-4s^2+1)^2+16s^2>0.
\]
An exact Sturm count for \(Q\) has variations \(4\) at \(0\), \(2\) at \(1\), and isolates precisely two roots in \((0,1)\): \((507/1000,508/1000)\) and \((794/1000,795/1000)\). To distinguish positive from negative stationary branches without a numerical inference, compute the degree-one subresultant of \(R_s,P_s\), divided by \(27s^6\), as \(U(s)x+V(s)\), where
\[
\begin{aligned}
U(s)={}&72s^{10}-126s^9-489s^8+936s^7+721s^6-1838s^5\\
&+587s^4+64s^3+49s^2+24s-36,\\
V(s)={}&48s^9-60s^8-327s^7+420s^6+565s^5-738s^4\\
&-119s^3+100s^2+141s-54.
\end{aligned}
\]
Exact Sturm counts certify that neither \(U\) nor \(V\) vanishes in either isolating interval. On the lower interval, \(U<0<V\), so any common root is \(-V/U>0\); on the upper, \(U<0\) and \(V<0\), so any common root is negative. The cubic \(P_s\) has exactly one positive root at every \(s\); therefore \(R_s(x_s)\) can vanish only at the lower isolated root \(s_c\), and does vanish there. Indeed, the resultant vanishes, the degree-one subresultant fixes a positive common root, and all higher subresultants together with \(U\ne0\) preclude a spurious degeneracy. Finally \(R_0(x)=-3\), while \(R_1(x)=3x^4+6x^3+2x+3>0\) for \(x>0\). By continuity, \(R_s(x_s)\) is strictly negative below \(s_c\) and strictly positive above it. The Sturm and subresultant certificates are reproduced exactly by the bundled checker.

**4. Consequence for global normers.** For \(s>s_c\), no second-frequency-free vector can be a global normer, because the only normers of that restricted plane are the \(f_s\) family and each has an improving transverse perturbation. Since the coefficient unit sphere is compact, global normers exist; all must have a nonzero second-frequency coefficient.

For the independent small-radius global regime, write \(a_0^2+c_0^2=1\) and \(x=c_0/a_0\). We have \(A_s(x)\le A_s^*=A_s(x_s)\), \(A_s^*\ge3s^2/8\), and \(D_s\le A_s^*\). The quadratic form in \(H_s\) has matrix \(\begin{pmatrix}1&s/2\\s/2&s^2\end{pmatrix}\), whose largest eigenvalue is at most its trace \(1+s^2\). Therefore
\[
\frac{H_s(x)}{2A_s^*}\le2s(1+s^2)\le\frac{116}{125}<1\qquad(0<s\le2/5).
\]
Insert these inequalities into the exact expression for \(F_s(v,x)\):
\[
F_s(v,x)\le (1-v)^2A_s^*+2v(1-v)A_s^*+v^2A_s^*=A_s^*,
\]
strictly when \(v>0\). The remaining \(v=0\) maximum is unique up to real scale and rotation by the preceding steps. This proves the claimed global regime.

## Verification

The standalone `checker.py` uses SymPy with exact rational arithmetic. Run `python3 checker.py` with SymPy installed. It recomputes the Fourier quadruple expansion, derivative, resultant, positive-factor square identity, exact Sturm root counts, subresultant-sign isolation, and small-radius inequality. Its finite numerical spot checks are diagnostic and are not used to establish the infinite-family claims. The exact symbolic and analytic argument above supplies those conclusions.

## Relationship to prior work

General Poisson-semigroup hypercontractivity on the circle is classical, and Frank–Ivanisvili (2021) discusses the circle case alongside the spherical fractional semigroup. Neither establishes the sharp support stability for the mean-zero first three real Fourier bands. The existing exact **two-frequency** Poisson norm theorem already supplies the restricted \(\{1,3\}\) optimizer and is credited; its setting excludes frequency \(2\), so it cannot decide the transverse instability. The existing exact **unsmoothed three-frequency** fourth-moment theorem supplies the endpoint optimizer at \(\rho=1\) and is credited; it does not decide the parameter-dependent local threshold. The additional sharp polynomial threshold and global nonvanishing statement concern the weighted full triad, not a special-case restatement of either existing result.

## Limitations

This is a local stability classification of the unique two-frequency normer, not a complete full-three-band norm formula. In particular, global uniqueness and exact global onset in \(2/5<s\le s_c\) are not proved. The algebraic local threshold is not asserted to be the unique global phase transition. The theorem is specific to real-valued mean-zero trigonometric functions with frequencies one through three, and the fourth moment. A search of indexed mathematics and accessible relevant works cannot exclude an unpublished or unindexed equivalent result. No independent audit has been performed.

## References

1. R. L. Frank and P. Ivanisvili, *Hypercontractivity of the semigroup of the fractional Laplacian on the n-sphere*, arXiv:2101.06209v1, first public 2021-01-15; https://arxiv.org/abs/2101.06209. Full HTML, Introduction, Theorem 1.1 and Section 2 examined.
2. F. B. Weissler, *Logarithmic Sobolev inequalities and hypercontractive estimates on the circle*, J. Functional Analysis 37 (1980), 218–234, DOI:10.1016/0022-1236(80)90042-7. Background on the unrestricted semigroup; not inspected in full.
3. *Resonant persistence and sharp mode selection for two-frequency circular Poisson smoothing*, public mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-resonant-persistence-and-sharp-mode-selection-for-two-frequency--ebfd25bec609. RESULT.md materially compared.
4. *Sharp fourth moments of the three consecutive centered real Fourier harmonics*, public mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-fourth-moments-of-the-three-consecutive-centered-real-four--76ef99312c58. RESULT.md materially compared.
