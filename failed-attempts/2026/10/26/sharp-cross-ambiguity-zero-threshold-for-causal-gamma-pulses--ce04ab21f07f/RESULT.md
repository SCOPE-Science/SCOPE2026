# Sharp cross-ambiguity zero threshold for causal gamma pulses

## Finding

For each integer \(m\ge0\), define \(f_m(t)=t^m e^{-t}\mathbf1_{(0,\infty)}(t)\) and \(f_0(t)=e^{-t}\mathbf1_{(0,\infty)}(t)\). The **cross**-ambiguity function of this ordered pair has no zeros anywhere in real delay–frequency space for \(m=0,1,2,3,4\), but has at least one conjugate-frequency pair of positive-delay zeros for every \(m\ge5\). The threshold \(5\) is exact. Every positive-delay zero is a transverse, orientation-preserving simple zero.

More precisely, let \(E_m(z)=\sum_{k=0}^{m}z^k/k!\). The complete positive-delay zero set corresponds bijectively to its roots in \(\operatorname{Re}z>0\) through
\[
T=\frac{\operatorname{Re}z}{2},\qquad \omega=\frac{2\operatorname{Im}z}{\operatorname{Re}z}.
\]
The theorem does not assert a closed formula for the number of such roots for each \(m\ge5\).

## Assumptions and scope

All pulse functions are real and in \(L^2(\mathbb R)\). Delay \(T\) and angular frequency \(\omega\) are real. We use the centered, unsquared, complex cross-ambiguity convention
\[
A_m(T,\omega)=\int_{\mathbb R}f_m(u+T/2)f_0(u-T/2)e^{-i\omega u}\,du.
\]
The two functions appear in the displayed order, which matters: the statement concerns their **cross** transform, not either self-ambiguity transform.

## Proof

Put \(q=2+i\omega\). Since \(\operatorname{Re}q=2\), it is never zero. The common support is \(u\ge T/2\) when \(T\ge0\) and \(u\ge-T/2\) when \(T<0\). Shifting the lower integration endpoint and using the exact incomplete-gamma identity yields
\[
A_m(T,\omega)=\frac{m!}{q^{m+1}}\begin{cases}
e^{-T-i\omega T/2}E_m(qT),&T\ge0,\\
e^{T+i\omega T/2},&T<0.
\end{cases}
\]
The two branches agree at \(T=0\), where \(E_m(0)=1\), so neither \(T\le0\) branch has any zeros. For \(T>0\), set \(z=qT=2T+i\omega T\). Every point of the open right half-plane has exactly one such representation with \(T>0\), \(\omega\in\mathbb R\). Hence the precise zero-bijection follows.

The zeros of \(E_m\) are simple. Indeed \(E_m'=E_{m-1}\) for \(m\ge1\), while \(E_m-E_{m-1}=z^m/m!\). A common zero would have to be \(z=0\), contradicting \(E_m(0)=1\). The map \((T,\omega)\mapsto (\operatorname{Re}z,\operatorname{Im}z)=(2T,T\omega)\) has Jacobian determinant \(2T>0\). Multiplying a complex-valued local map by the nonzero smooth prefactor in the display preserves the sign of its real Jacobian at a zero. Thus each zero has strictly positive real Jacobian and is isolated and transverse.

It remains to determine on which side of the imaginary axis zeros of \(E_m\) lie. For \(m\ge1\), use the monic real polynomial \(P_m(z)=m!E_m(z)\), whose leading coefficients are \(1,m,m(m-1),m(m-1)(m-2),\ldots\). The Hurwitz principal minors for \(m=1,2,3,4\), in their natural order, are respectively
\[
(1),\quad(2,4),\quad(3,12,72),\quad(4,24,192,4608).
\]
All are positive, hence every root of each \(P_m\), \(1\le m\le4\), has strictly negative real part by the Routh–Hurwitz criterion. The case \(m=0\) is constant and root-free.

For \(m=5\), the same minors are \((5,40,0,-38400,-4608000)\), so the fourth principal minor is negative. For every integer \(m\ge6\), the third principal minor is
\[
\Delta_3(P_m)=-2m^2(m-1)(m-2)(m-5)<0.
\]
This identity follows by substituting the five leading coefficients of \(P_m\) into the \(3\times3\) Hurwitz determinant and factoring. If all roots of such a polynomial had nonpositive real part, then for each \(\varepsilon>0\) the shifted polynomial \(P_m(z+\varepsilon)\) would have strictly left-half-plane roots. All its Hurwitz principal minors would be positive. Sending \(\varepsilon\downarrow0\) would force all principal minors of \(P_m\) to be nonnegative, contradicting the indicated negative minor. Thus at least one root lies in \(\operatorname{Re}z>0\). Because \(E_m(x)>0\) for real \(x\ge0\) and its coefficients are real, any such root is nonreal and is accompanied by its complex conjugate. This proves at least two positive-delay cross-ambiguity zeros for every \(m\ge5\) and completes the classification of the threshold.

## Verification

The standalone `checker.py` (Python, SymPy and mpmath) computes the above Hurwitz minors exactly for the five base degrees, checks the closed general third-minor formula symbolically, verifies squarefreeness in representative degrees, and evaluates a positive-delay witness for \(m=5\). At high precision it finds one polynomial root near \(0.239806393753408+3.128335025970710i\), corresponding to \(T\approx0.119903196876704\) and \(\omega\approx26.09050556998547\). It independently compares direct integral quadrature against the exact transform formula for representative degrees and both delay signs. Recorded outputs are in `checker_output.txt`; the general argument is the proof above, not an extrapolation from these checks.

## Relationship to prior work

Bayer and Gröchenig (2014, arXiv:1407.4321) analyze mixed-window short-time Fourier transforms in localization-operator theory, including the distinction between nowhere-vanishing and almost-everywhere nonvanishing assumptions. Gröchenig, Jaming and Malinnikova (2018, arXiv:1811.03937), especially their Section 4, establish the zero-free **self**-ambiguity transform of \(t^m e^{-t}\mathbf1_{t>0}\) for every integer \(m\ge0\), by different Bessel-polynomial arguments. Their cross-window examples and their self-window theorem do not state the present uniform order-five cross-zero transition for \((f_m,f_0)\). The polynomial-root reduction itself uses classical truncated exponentials and the classical Routh–Hurwitz criterion; no originality for those ingredients is asserted.

## Limitations

This result classifies the existence and basic local geometry of cross zeros, not the exact total number of zeros for each large \(m\), nor the full zero-free classification for other pairs of gamma orders. Ordinary partial-exponential root literature might imply the right-half-plane assertion without time-frequency terminology; this priority risk is explicitly retained. Isolated zeros do **not** contradict an almost-everywhere nonvanishing criterion, and no loss of Hilbert–Schmidt density for localization operators is claimed. No independent mathematical audit has been performed.

## References

1. D. Bayer and K. Gröchenig, *Time-Frequency Localization Operators and a Berezin Transform*, arXiv:1407.4321, first public preprint July 16, 2014. https://arxiv.org/abs/1407.4321
2. K. Gröchenig, P. Jaming and E. Malinnikova, *Zeros of the Wigner Distribution and the Short-Time Fourier Transform*, arXiv:1811.03937, 2018. https://arxiv.org/abs/1811.03937
3. Classical Routh–Hurwitz polynomial stability criterion and truncated exponential polynomials; used only as standard mathematical tools.
