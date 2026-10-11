# Exact Euclidean Banach–Mazur distance for two-dimensional Lorentz spaces below exponent two
## Finding
For \(1<q<2\) and \(0<\omega<1\), define the two-dimensional Lorentz sequence space \(X=d^{(2)}(\omega,q)\) by
\[
\|(x_1,x_2)\|_{\omega,q}=\bigl((x_1^*)^q+\omega(x_2^*)^q\bigr)^{1/q},
\]
where \(x_1^*\ge x_2^*\ge0\) is the nonincreasing rearrangement of \((|x_1|,|x_2|)\). Set \(t=\omega^{2/(2-q)}\). Then
\[
d_{\mathrm{BM}}(X,\ell_2^2)^2=
\begin{cases}
\displaystyle \frac{2(1+t)^{(2-q)/q}}{(1+\omega)^{2/q}},&0<\omega\le 2^{q/2}-1,\\[6pt]
\displaystyle (1+t)^{(2-q)/q},&2^{q/2}-1\le\omega<1.
\end{cases}
\]
An optimal Euclidean pullback norm is \(\|(x_1,x_2)\|_2\), up to a positive scalar factor.

## Assumptions and scope
The field is real. The parameters satisfy \(1<q<2\) and \(0<\omega<1\). No assertion is made here about the endpoint cases \(q=1\) or \(q=2\), about higher-dimensional Lorentz spaces, or about other Lorentz weight conventions.

## Proof
Write \(N=\|\cdot\|_{\omega,q}\). Any linear isomorphism from \(X\) to the Euclidean plane pulls the Euclidean norm back to a positive-definite quadratic norm \(E_Q(x)^2=x^TQx\). If
\[
aN(x)^2\le E_Q(x)^2\le bN(x)^2
\]
for all \(x\), average \(Q\) over the eight signed coordinate permutations. Because \(N\) is invariant under that group, the same two inequalities remain valid after averaging. The averaged quadratic form is a positive scalar multiple of the identity. Consequently no ellipsoid gives smaller distortion than a Euclidean circle, and it suffices to compare \(N\) with \(\|\cdot\|_2\).

By symmetry, on the Euclidean unit circle it suffices to take \(x_1\ge x_2\ge0\) and put \(s=x_2/x_1\in[0,1]\). The radial ratio is
\[
F(s)=\frac{N(x_1,x_2)}{\sqrt{x_1^2+x_2^2}}=
\frac{(1+\omega s^q)^{1/q}}{\sqrt{1+s^2}}.
\]
A direct logarithmic derivative gives
\[
\frac{F'(s)}{F(s)}=
\frac{s(\omega s^{q-2}-1)}{(1+\omega s^q)(1+s^2)}.
\]
Since \(1<q<2\), there is exactly one critical point in \((0,1)\), namely
\[
s_*=\omega^{1/(2-q)}.
\]
The function increases on \([0,s_*]\) and decreases on \([s_*,1]\), so its maximum is attained at \(s_*\). Using \(\omega s_*^q=s_*^2=t\),
\[
F(s_*)=(1+t)^{(2-q)/(2q)}.
\]
The two endpoint values are
\[
F(0)=1,
\qquad
F(1)=\frac{(1+\omega)^{1/q}}{\sqrt2}.
\]
Thus the minimum equals \(F(1)\) when \(\omega\le2^{q/2}-1\), and equals \(F(0)\) when \(\omega\ge2^{q/2}-1\). The squared Banach–Mazur distortion is \((\max F/\min F)^2\), which is exactly the displayed formula.

## Verification
The proof exhausts all linear isomorphisms through quadratic-form symmetrization and then exhausts the remaining one-dimensional radial parameter. The sign of the derivative is controlled solely by \(\omega s^{q-2}-1\), so there are no omitted interior extrema. At the phase boundary \(\omega=2^{q/2}-1\), the two branches agree because \(F(0)=F(1)\). Numerical optimization over general positive-definite quadratic forms at representative parameter values was used only as a consistency check and is not part of the proof.

## Relationship to prior work
Suzuki, Yamano, and Kato introduced and analyzed the difficult \(1<q<2\) regime for the James constant of these two-dimensional Lorentz spaces. A later survey by Saito, Mitani, and Tanaka gives the same norm explicitly and summarizes the completed James- and Schäffer-constant formulas throughout this regime. Those works motivate the parameter family but address different invariants. Searches for the Banach–Mazur distance, the Euclidean distortion, the exact phase boundary \(2^{q/2}-1\), and the radial factor \(\omega^{2/(2-q)}\) did not locate this affine-distance formula. The 2014 survey was inspected in full and contains no occurrence of “Banach-Mazur” or “distance.”

## Limitations
The originality conclusion is literature-search based, not a proof of nonexistence of prior publication. The 2006 source was inspected through its public repository metadata and available article text, while the 2014 survey was inspected as a complete public PDF. A specialized source using different notation for the same Banach–Mazur calculation could have been missed. The result concerns only the two-dimensional real space and only \(1<q<2\).

## References
1. T. Suzuki, A. Yamano, M. Kato, “The James Constant of 2-Dimensional Lorentz Sequence Spaces,” *Bulletin of the Kyushu Institute of Technology. Pure and Applied Mathematics* 53 (2006), 15–24. DOI: 10.18997/00002048; Handle: 10228/3185.
2. K.-I. Mitani, K.-S. Saito, T. Suzuki, “On the calculation of the James constant of Lorentz sequence spaces,” *Journal of Mathematical Analysis and Applications* 343 (2008), 310–314. DOI: 10.1016/j.jmaa.2007.09.040.
3. K.-S. Saito, K.-I. Mitani, R. Tanaka, “Recent development on James constant of 2-dimensional Lorentz sequence spaces,” RIMS Kôkyûroku 1906 (2014), 40–47, https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1906-05.pdf.
