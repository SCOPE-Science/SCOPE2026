# A sharp concurrency dichotomy for three-line Fourier projections over finite fields

## Finding

Let \(q=p^m\) be any prime power. Let \(S\subset\mathbb F_q^2\) be the union of three distinct affine lines with pairwise distinct directions. Let \(P_S\) be the complex Fourier projection onto frequencies in \(S\). Its sharp \(\ell^\infty\)-operator norm depends **only** on whether the three lines share one point (a pencil) or have three distinct pairwise intersections (a triangle).

For a pencil the exact norm is
\[
L_{\mathrm{pen}}(q)=5-\frac{12}{q}+\frac{8}{q^2}.
\]
For a triangle, write \(\zeta_p=e^{2\pi i/p}\) and
\[
R_p=\sum_{a,b=0}^{p-1}|1+\zeta_p^a+\zeta_p^b|,\qquad
T_p=\sum_{a=0}^{p-1}|2+\zeta_p^a|,\qquad
U_p(q)=\sum_{a=0}^{p-1}|q-2-\zeta_p^a|.
\]
For \(q\ge3\), the **exact sharp** triangular norm is
\[
L_{\mathrm{tri}}(q)=\frac{(q/p)^2R_p+3(q/p)(U_p(q)-T_p)+12}{q^2}.
\]
At \(q=2\), \(L_{\mathrm{tri}}(2)=3/2\). When \(p=2\) the formula simplifies, for **all** \(q=2^m\) including \(q=2\), to
\[
L_{\mathrm{tri}}(q)=\frac92-\frac{12}{q}+\frac{12}{q^2}.
\]
The two geometric types obey the strict sharp ordering
\[
L_{\mathrm{tri}}(q)<L_{\mathrm{pen}}(q)\quad(q\ge3),
\qquad L_{\mathrm{tri}}(2)>L_{\mathrm{pen}}(2)=1.
\]
In particular, at \(q=3\) the gap is \((11-6\sqrt3)/9>0\), whereas in characteristic two it is exactly \(1/2-4/q^2\). For fixed characteristic \(p\) and \(m\to\infty\),
\[
L_{\mathrm{tri}}(p^m)\longrightarrow 3+\frac{R_p}{p^2},
\qquad L_{\mathrm{pen}}(p^m)\longrightarrow5.
\]
The three-step planar root-of-unity average \(R_p/p^2\) is not claimed as a previously unknown constant.

## Assumptions and scope

The ambient additive group is \(G=(\mathbb F_q^2,+)\). Choose any nontrivial additive character \(\psi\colon\mathbb F_q\to\mathbb C\) with \(|\psi|=1\), and the Fourier convention
\[
\widehat f(u,v)=\sum_{(x,y)\in G}f(x,y)\psi(-ux-vy),\qquad
P_S f(x,y)=q^{-2}\sum_{(u,v)\in S}\widehat f(u,v)\psi(ux+vy).
\]
Here \(\|P_S\|_{\infty\to\infty}\) is taken over **complex** functions with the ordinary counting-measure \(\ell^\infty\)-norm. There is no assumption that \(q\) is prime, that the lines pass through the origin, or that their pairwise intersections are distinct. Pairwise distinct directions are essential; parallel-line configurations are outside this theorem. The result concerns Fourier projection norms, **not** the \(\ell^\infty/\ell^r\) spectral-synthesis ratio of functions supported on \(S\), nor a principal Fourier sampling matrix.

## Proof

**Affine reduction and sharpness.** Distinct directions allow an invertible affine change of coordinates taking the first two lines to \(x=0\), \(y=0\) and the third to \(x+y=c\). Translation and invertible linear changes of coordinates only permute or phase-modulate the Fourier coefficients of an indicator, so preserve their absolute values and their sum. If \(c=0\), the lines are concurrent; otherwise scaling both coordinates reduces to \(c=1\). Thus there are precisely two geometries.

For a set \(S\), the projection convolution kernel is
\[
K_S(u,v)=q^{-2}\sum_{(x,y)\in S}\psi(ux+vy).
\]
Its sharp complex \(\ell^\infty\)-operator norm is exactly \(\sum_{u,v}|K_S(u,v)|\): the triangle inequality gives the upper bound, and choosing the input at each point to be the conjugate phase of the appropriate translated kernel attains it. Character signs do not affect this absolute sum.

**Pencil.** Inclusion–exclusion for the three concurrent lines gives
\[
q^2K_{\mathrm{pen}}(u,v)=q(\mathbf1_{u=0}+\mathbf1_{v=0}+\mathbf1_{u=v})-2.
\]
There is one coefficient \(3q-2\), exactly \(3(q-1)\) coefficients \(q-2\), and \((q-1)(q-2)\) coefficients \(-2\). Summing absolute values, including \(q=2\), gives \(L_{\mathrm{pen}}(q)=5-12/q+8/q^2\).

**Triangle.** The pairwise intersections are \((0,0),(0,1),(1,0)\). Inclusion–exclusion therefore yields
\[
q^2K_{\mathrm{tri}}(u,v)
=q\bigl(\mathbf1_{u=0}+\mathbf1_{v=0}+\psi(v)\mathbf1_{u=v}\bigr)
-\bigl(1+\psi(u)+\psi(v)\bigr).
\]
At \((u,v)=(0,0)\) its magnitude is \(3q-3\). The three punctured axes \(u=0\), \(v=0\), \(u=v\) each contribute
\(A_q=\sum_{a\ne0}|q-2-\psi(a)|\). The remaining points contribute
\(B_q=\sum_{u,v\ne0,\,u\ne v}|1+\psi(u)+\psi(v)|\). Hence
\[
q^2L_{\mathrm{tri}}=3q-3+3A_q+B_q.
\]
For \(q\ge3\), additive-character orthogonality gives each \(p\)-th root of unity exactly \(q/p\) occurrences, with one of the root-one occurrences omitted from \(A_q\). Therefore
\[
A_q=(q/p)U_p(q)-(q-3).
\]
For \(B_q\), sum over the full two-dimensional frequency plane, and remove the three coincident axes. The full sum equals \((q/p)^2R_p\), while each axis has sum \((q/p)T_p\) and the axes all meet at the common point of value \(3\), counted three times. Thus
\[
B_q=(q/p)^2R_p-3(q/p)T_p+6.
\]
Substitution proves the displayed triangular formula. At \(q=2\), the four Fourier kernel numerator magnitudes are \(3,1,1,1\), yielding \(3/2\). For \(p=2\) the root-of-unity sums are \(R_2=6\), \(T_2=4\), and \(U_2(q)=2q-4\) when \(q\ge4\); simplifying and checking \(q=2\) separately gives the asserted characteristic-two expression.

**Strict ordering.** For \(q\ge3\), the character sums \(\sum_{a\ne0}\psi(a)=-1\) give
\[
\sum_{a\ne0}|q-2-\psi(a)|^2=(q-1)(q-2)^2+3q-5.
\]
Cauchy–Schwarz, followed by \((q-1)(q-3)+4>0\), yields
\[
A_q\le(q-1)(q-2)+2.
\]
On the full frequency square, \(\sum_{u,v}|1+\psi(u)+\psi(v)|^2=3q^2\). Each of the three axes has squared sum \(5q\); correcting for the common intersection of squared magnitude \(9\) gives
\[
\sum_{u,v\ne0,\,u\ne v}|1+\psi(u)+\psi(v)|^2=3(q-2)(q-3).
\]
There are \((q-1)(q-2)\) points off the axes. Consequently, for \(q\ge4\),
\[
B_q\le(q-2)\sqrt{3(q-1)(q-3)}<\sqrt3(q-2)^2.
\]
Subtracting the two sharp norm formulas yields
\[
q^2(L_{\mathrm{pen}}-L_{\mathrm{tri}})=5q^2-15q+11-3A_q-B_q
>(2-\sqrt3)q^2+(4\sqrt3-6)q-(1+4\sqrt3).
\]
The last polynomial has value \(7-4\sqrt3>0\) at \(q=4\), and positive derivative for \(q\ge4\), hence proves the gap throughout that range. At \(q=3\), direct evaluation gives \(q^2L_{\mathrm{tri}}=6+6\sqrt3\) versus \(q^2L_{\mathrm{pen}}=17\), with gap \((11-6\sqrt3)/9>0\). At \(q=2\), the checked values give the opposite strict inequality. All inequalities compare the **already sharp** operator norms rather than estimates on unknown optima.

**Large-field consequence.** Fix \(p\). The elementary asymptotic \(U_p(q)=p(q-2)+O_p(q^{-1})\) gives the displayed fixed-characteristic limit as \(q=p^m\to\infty\). The mean \(R_p/p^2\) is at most \(\sqrt3\) by a second-moment Cauchy–Schwarz inequality, so this limit remains strictly below five. As \(p\to\infty\), its value approaches the classical continuous two-angle average \((2\pi)^{-2}\int_0^{2\pi}\int_0^{2\pi}|1+e^{it}+e^{is}|\,dt\,ds\) by Riemann sums; this observation does not assert novelty of that standard integral.

## Verification

Run `python3 checker.py` using only the Python standard library. The checker directly enumerates Fourier coefficients for the canonical line configurations over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7,\mathbb F_8,\mathbb F_9,\mathbb F_{11},\mathbb F_{25}\). It independently evaluates the root-of-unity formula, and checks **every** choice of three distinct directions and every line offset in the finite planes of orders \(2,3,4,5\): respectively \(8,108,640,2500\) arrangements. The finite checker is supplementary; the arbitrary-field theorem follows from the displayed orthogonality identities and inequalities, not finite enumeration.

## Relationship to prior work

Iosevich, Li, and Yu (2026) develop Fourier-ratio spectral synthesis on finite groups, introduce the Fourier algebra indicator norm, and obtain exact synthesis constants on affine-transitive supports such as paraboloids. Their full source does not state this three-line projection-norm classification or its strict concurrency comparison. Sanders (2020) gives a general coset-decomposition theorem controlled by the Fourier algebra norm, not a formula for this finite line arrangement. Existing indexed three-line Fourier **sampling-matrix** results concern rank and arithmetic resonance of principal submatrices; their operator is not the full-group convolution projection studied here. A related published surface calculation also contains the known three-step planar-walk average, not the present affine-line incidence classification.

The contributions claimed here are the complete **two-orbit sharp projection-norm classification**, its exact characteristic-dependent expressions, and the strict geometric ordering with the binary exception. The existing algebra norm definition, orthogonality and three-step-walk integral are background rather than new results.

## Limitations

The theorem excludes line arrangements with parallel directions. It concerns complex \(\ell^\infty\)-projection norms, not principal Fourier matrices, reconstruction condition numbers, or optimized \(\ell^r\) spectral-synthesis ratios. It makes no general claim on higher-dimensional hyperplane arrangements. Searches cannot exclude an older equivalent result under an unrelated terminology; one closely titled indexed three-line sampling result was only available through its summary when its linked full text could not be fetched. Independent mathematical review has not been performed.

## References

1. A. Iosevich, Z. Li, and K. Yu, *Spectral synthesis with the complexity parameter in \(\mathbb Z_N^d\)*, arXiv:2609.25404, initial public version 21 September 2026. https://arxiv.org/abs/2609.25404
2. T. Sanders, *Bounds in Cohen's Idempotent Theorem*, Journal of Fourier Analysis and Applications 26, Article 25 (2020). https://doi.org/10.1007/s00041-020-09732-y
3. J. M. Fraser and F. Rakhmonov, *Exceptional projections in finite fields: Fourier analytic bounds and incidence geometry*, Mathematische Zeitschrift 312, Article 111 (2026). https://doi.org/10.1007/s00209-026-04008-5. This discusses geometric projections and incidence estimates, not the Fourier-multiplier norm here.
