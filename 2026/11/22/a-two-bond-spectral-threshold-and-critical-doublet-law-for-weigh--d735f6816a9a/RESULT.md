# Weak binding at two separated enhanced Jacobi bonds

## Finding

For each integer \(m\ge2\), let \(J_m\) be the Jacobi operator on \(\ell^2(\mathbb Z)\) with zero diagonal, hopping \(a_m/2\) across the bonds at indices \(0,m\), and hopping \(1/2\) elsewhere. Write \(a_m^2=1+\gamma_m/m\) with \(\gamma_m>0\). Write \(\lambda_{+,m}>1\) for the larger positive outlier and \(\lambda_{-,m}>1\) for the smaller one when present. The finite binding threshold for the smaller outlier is \(\gamma_{c,m}=2m/(m-1)\); the second state exists just when \(\gamma_m>\gamma_{c,m}\).

If \(\gamma_m\to\gamma>0\), the upper gap has the limit
\[
m^2(\lambda_{+,m}-1)\ \longrightarrow\ \frac{\kappa_+^2}{2},\qquad 2\kappa_+=\gamma(1+e^{-\kappa_+}),\quad \kappa_+>0.
\]
If \(\gamma>2\) the lower outlier exists eventually and \(m^2(\lambda_{-,m}-1)\to\kappa_-^2/2\), where \(\kappa_->0\) solves \(2\kappa_-=\gamma(1-e^{-\kappa_-})\). The positive solutions are unique on their respective domains. If \(0<\gamma<2\) the smaller outlier does not exist eventually; for fixed \(\gamma_m\equiv2\) it does not exist at any \(m\). For \(\gamma\downarrow2\), \(\kappa_-\sim\gamma-2\).

At the moving lattice threshold the following sharper statement holds: for **every** sequence with \(\Delta_m=\gamma_m-\gamma_{c,m}>0\) tending to zero,
\[
\frac{m^2(\lambda_{-,m}-1)}{\Delta_m^2}\longrightarrow\frac12 .
\]
In particular, for \(\gamma_m=2+s/m\) with fixed real \(s\), the smaller outlier is absent for large \(m\) if \(s\le2\), but exists eventually if \(s>2\) and then \(m^4(\lambda_{-,m}-1)\to(s-2)^2/2\). The quartic scale detects the threshold displacement that the fixed-coupling continuum gap does not resolve.

## Proof

**Finite-distance input.** In the convention of [Exact two-bond numerical-range bifurcation and tunneling for bilateral shifts](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-exact-two-bond-numerical-range-bifurcation-and-tunneling-for-bil--ab2134afdf83), take \(c=a_m\), \(d=m-1\). Its two channels are \(\lambda=(z+z^{-1})/2\) with \(0<z<1\), where \(a_m^2z^2\pm(a_m^2-1)z^{m+1}=1\), and its finite binding criterion is \((m-1)(a_m^2-1)>2\). In particular the plus root always exists, and each nontrivial root is unique in its channel. These exact finite-distance facts, including the finite threshold, are inputs and not new claims here.

**Fixed limiting coupling.** Write \(z=e^{-\kappa/m}\). The equations become
\[
m(1-e^{-2\kappa/m})=\gamma_m\big(e^{-2\kappa/m}\pm e^{-(m+1)\kappa/m}\big).
\]
The left-minus-right functions converge uniformly on bounded \(\kappa\)-intervals to \(2\kappa-\gamma(1\pm e^{-\kappa})\). The plus limit is strictly increasing, is negative at zero and tends to infinity. The minus limit is strictly convex, vanishes at zero, has derivative \(2-\gamma\) there and tends to infinity. Thus it has one strictly positive, sign-changing root for \(\gamma>2\), and none for \(\gamma\le2\). Bracket each strictly positive limiting root using two strictly positive arguments of opposite sign arbitrarily close to it; the finite functions have those signs eventually. Uniqueness of the finite roots gives convergence. Since \(\lambda=\cosh(\kappa/m)\), the gap formulas follow. The finite criterion handles absence, including fixed \(\gamma_m=2\). For the limiting lower branch, \(\gamma=2\kappa_-/(1-e^{-\kappa_-})\) increases strictly from 2, and expansion at zero gives \(\gamma=2+\kappa_-+O(\kappa_-^2)\).

**Detuning from the exact threshold.** Set \(t_m=-\log z_{-,m}>0\), \(x_m=(m-1)t_m\). The minus equation, after division by \(z^2\), is equivalent to the following exact product:
\[
\frac{\gamma_m}{\gamma_{c,m}}
=\frac{e^{2x_m/(m-1)}-1}{2x_m/(m-1)}\frac{x_m}{1-e^{-x_m}}.
\]
The first factor is at least one and the second is strictly increasing from one to infinity. Thus \(\Delta_m\to0^+\) forces \(x_m\to0\). Uniformly in \(m\ge2\) the right-hand side is \(1+(1/2+1/(m-1))x_m+O(x_m^2)\) at zero. Consequently \(\Delta_m/x_m\to1\) and \(mt_m/\Delta_m\to1\). Using \(\lambda_{-,m}=\cosh(t_m)\) proves the ratio claim, even for detuning much smaller than any inverse power of \(m\). For \(\gamma_m=2+s/m\), one has \(m\Delta_m=s-2m/(m-1)\). Its strict positivity is eventually equivalent to \(s>2\), and in that case the ratio claim gives the stated quartic law.

## Scope and relation to prior work

The limiting equations are those of the even and odd bound states of the unit-separated continuum double-delta problem \(-d^2/dx^2-\gamma(\delta_0+\delta_1)\) at energy \(-\kappa^2\). In that problem the free resolvent restricted to the two points has entries \(e^{-\kappa|i-j|}/(2\kappa)\) for \(i,j\in\{0,1\}\), and its parity eigenvalues give the two equations; the negative-eigenvalue count agrees with Theorem 3.8 of Goloschapova and Oridoroga, [On the Negative Spectrum of One-Dimensional Schrödinger Operators with Point Interactions](https://arxiv.org/abs/0903.1180). The result here is about convergence and threshold detuning **of the lattice outliers**, not a new continuum spectrum or an operator-norm convergence theorem. The finite-distance root classification and fixed-enhancement tunneling law are already stated in the finite-distance input above. The detuned quartic law here concerns two separated hopping defects on the free full line, not a block of enhanced hopping on the half line or a parity-dependent defect on a periodic half line.
