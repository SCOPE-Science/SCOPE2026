# A quadratic rare-growth boundary for Gaussian partial pivoting in dimension two

## Finding
Let \(A\) be a real \(2\times2\) matrix with four independent entries drawn from the same continuous even density \(f\). Perform Gaussian elimination with partial row pivoting in exact arithmetic. Define the *generated-entry growth factor* \(\rho\) as the largest absolute entry appearing in the input or in the upper-triangular factor, divided by the largest absolute input entry. Put \(g(s)=2f(s)\) for \(s\ge0\).

For every \(1<t<2\), the exact upper-tail law is
\[
\Pr\{\rho>t\}=\int_0^\infty\!\int_0^a\!\int_0^\infty\!\int_0^\infty
 g(a)g(c)g(B)g(D)\,\mathbf{1}\!\left\{D+\frac ca B>t\max\{a,B,D\}\right\}\,dD\,dB\,dc\,da.
\]
If \(f\) is bounded by \(C e^{-c|s|}\) for some positive constants \(C,c\), then as \(\varepsilon\downarrow0\),
\[
\boxed{\Pr\{\rho>2-\varepsilon\}=K_f\varepsilon^2+o(\varepsilon^2),\qquad
 K_f=\int_0^\infty m\,g(m)^2\!\left(\int_0^m a\,g(a)^2\,da\right)dm>0.}
\]
For standard normal entries this becomes
\[
\boxed{\Pr\{\rho>2-\varepsilon\}=\frac{\varepsilon^2}{2\pi^2}+o(\varepsilon^2).}
\]
For symmetric unit-scale Laplace entries the same exponent has the distinct coefficient \(K_f=1/32\).

In the standard normal case there is also an exact two-variable upper-tail formula valid for every \(1<t<2\): write \(h=\sin\theta+q\cos\theta\). Then
\[
\boxed{
\Pr\{\rho>t\}=\frac4{\pi^2}\int_0^{\pi/2}\!\int_0^1
\mathbf{1}\{h>t\max(\sin\theta,\cos\theta)\}
\frac{h^2}{t^2+(1+q^2)h^2}\,dq\,d\theta.}
\]
By construction \(1\le\rho<2\) almost surely. The formula for \(t>1\) also applies if growth is defined using only the final upper-triangular factor; for \(t\le1\) those two normalizations need not agree.

## Assumptions and scope
The four input entries are independent and identically distributed, real, with a continuous even probability density. The exact integral law for \(t>1\) needs no tail assumption. The sharp near-maximum law assumes \(0\le g(s)\le C e^{-cs}\) for all \(s\ge0\), with \(C,c>0\); normal and Laplace densities satisfy this hypothesis. All statements are for \(2\times2\) matrices and exact-arithmetic partial **row** pivoting; they assert neither finite-precision backward-error probabilities nor a dimension-uniform bound. Ties and zero pivots have probability zero.

## Proof
**1. One-step reduction and sign cancellation.** After pivoting the first column, let \(a>c\ge0\) be the ordered absolute first-column entries, and let \(B,D>0\) be the corresponding absolute second-column entries (pivot row first). Put \(q=c/a\). The upper-right entry has magnitude \(B\), the first pivot has magnitude \(a\), and the Schur complement equals the signed difference between two terms of magnitudes \(D\) and \(qB\). Since all entry signs are independent and symmetric, the adverse signs occur with conditional probability \(1/2\), giving Schur magnitude \(D+qB\). In the other sign configuration the Schur magnitude is at most \(\max(B,D)\), so growth cannot exceed one. There are two possible first-column orderings, each with the same density; their factor two cancels the adverse-sign probability one half. The initial maximum is \(M=\max(a,B,D)\). This establishes the asserted fourfold integral for any \(t>1\), with no omitted orientation factor. Furthermore \(|u_{22}|\le D+qB\le 2M\), with strict equality almost surely.

**2. Exact Gaussian integration.** Substitute \(c=qa\) with \(0<q<1\), and \(B=r\cos\theta\), \(D=r\sin\theta\) with \(r>0\), \(0<\theta<\pi/2\). The Jacobian is \(ar\). For \(g(s)=\sqrt{2/\pi}\,e^{-s^2/2}\), the event becomes
\[
 h>t\max(\sin\theta,\cos\theta),\qquad 0<a<rh/t.
\]
Integrating the \(a\)-variable gives
\[
\int_0^{rh/t}a\,g(a)g(qa)\,da=
\frac{2}{\pi(1+q^2)}\left[1-e^{-(1+q^2)r^2h^2/(2t^2)}\right].
\]
The remaining Rayleigh integral of \(r e^{-r^2/2}\) equals \(\beta/(1+\beta)\) after subtracting its damped version, where \(\beta=(1+q^2)h^2/t^2\). Combining the densities yields the displayed two-variable formula, including its coefficient \(4/\pi^2\).

**3. Quadratic near-maximum cone.** Set \(\varepsilon=2-t\). Choose \(m=\max(B,D)\), write \(\min(B,D)=m(1-v)\), and put \(c=a(1-u)\), with \(u,v\in[0,1)\). The change from \((c,B,D)\) to \((u,v,m)\) has Jacobian \(am\) in each of the two possible choices of the larger second-column entry. If \(a\le m\), the event for \(B=m\) is exactly \(u+v<\varepsilon\); the event for \(D=m\) is exactly \(u+v-uv<\varepsilon\). Both scaled domains \((u/\varepsilon,v/\varepsilon)\) converge in measure to the unit triangle \(\{(x,y)\ge0:x+y<1\}\) of area \(1/2\). Their densities converge pointwise to \(am\,g(a)^2g(m)^2\). The exponential upper bound gives an integrable envelope and permits dominated convergence. Adding the two triangle areas gives the coefficient
\[
 \int_{0<a<m<\infty}am\,g(a)^2g(m)^2\,da\,dm=K_f.
\]
If \(a>m\), the event forces \(a/m<2/(2-\varepsilon)\), \(u<\varepsilon\), and \(v<2\varepsilon\) when \(\varepsilon<1/2\). This additional thin \(a\)-interval makes that contribution \(O(\varepsilon^3)\) under the exponential envelope. Thus no boundary mass is missing and the full event has the claimed \(K_f\varepsilon^2+o(\varepsilon^2)\) asymptotic.

**4. Constants.** In the Gaussian case \(g(s)^2=(2/\pi)e^{-s^2}\), so
\[
K_f=\frac4{\pi^2}\int_0^\infty m e^{-m^2}\left(\frac{1-e^{-m^2}}2\right)dm
=\frac1{2\pi^2}.
\]
For the unit-scale Laplace law \(g(s)=e^{-s}\), direct integration of \(\int_0^\infty m e^{-2m}\int_0^m a e^{-2a}\,da\,dm\) gives \(1/32\). Positivity of \(K_f\) follows from continuity and the existence of an interval on which the nonzero density is strictly positive.

## Verification
Run the independently executable standard-library script `python VERIFY.py` in the same directory as this document. It performs exact-rational pivoted-elimination comparisons with the direct growth calculation, independently evaluates the Gaussian angular integral by deterministic midpoint quadrature, compares with seeded Gaussian simulations, and checks the two exact coefficients. A successful run ends in `VERIFY_OK`. Those finite checks establish neither the asymptotic probability nor the general-density theorem; the proof above establishes these statements.

## Relationship to prior work
The first-public October 3, 2026 note of Trefethen studies the entry \(u_{nn}\) and large-dimension rare growth, explicitly separating the corner-entry question from full growth. The October 6 work of Spielman and Yu supplies general-dimension inverse-quasipolynomial lower estimates, whereas Urschel's October 5 paper provides high-probability bounds on the large-dimensional scale. Neither statement implies a full probability law at fixed dimension two near its extremal growth value. Huang and Tikhomirov establish polynomial high-probability growth bounds, not this sharp coefficient. Peca-Medlin and Trogdon have an exact distribution for a *different, structured random-butterfly ensemble*, not independent Gaussian entries. The 1990 empirical work of Trefethen and Schreiber reports averages and numerical studies up to large dimensions and cites Macleod’s random-matrix statistics. The 2007 rare-growth simulations of Driscoll and Maki principally concern much larger dimensions; the full article was not inspected. A historically relevant 1988 unpublished report by A. J. Macleod entitled *The distribution of the growth factor in Gaussian elimination with partial pivoting* was not located, so priority remains uncertain. The present result is a low-dimensional exact benchmark, not a resolution of asymptotic large-dimension tail problems.

## Limitations
This is a finite-dimensional law for \(2\times2\) exact Gaussian elimination with independent symmetric entries, plus a general-density endpoint extension. The asymptotic is in the *distance from the dimension-two maximal growth*, not in matrix dimension. No transfer to larger matrices, correlated ensembles, non-symmetric entry laws, floating-point error, or smoothed perturbation models is claimed. Searches of accessible sources cannot certify historical uniqueness; the inaccessible Macleod report and the full Driscoll–Maki article remain priority risks. Independent mathematical validation has not been performed.

## References
- L. N. Trefethen, *Instability of Gaussian elimination is exponentially rare (proof of partial result)*, arXiv:2610.04761v1, October 3, 2026, https://arxiv.org/html/2610.04761v1.
- D. A. Spielman and X. Yu, *Large Growth Happens: Gaussian Elimination with Partial Pivoting on Random Matrices*, arXiv:2610.08701v1, October 6, 2026, https://arxiv.org/html/2610.08701v1.
- J. Urschel, *On the Growth Factor of Random Matrices*, arXiv:2610.06785v1, October 5, 2026, https://arxiv.org/abs/2610.06785.
- H. Huang and K. Tikhomirov, *Average-case analysis of the Gaussian elimination with partial pivoting*, Probability Theory and Related Fields 189 (2024), 501–567; https://arxiv.org/abs/2206.01726.
- J. Peca-Medlin and T. Trogdon, *Growth factors of random butterfly matrices and the stability of avoiding pivoting*, SIAM J. Matrix Anal. Appl. 44 (2023), 945–970; https://arxiv.org/abs/2203.15921.
- L. N. Trefethen and R. S. Schreiber, *Average-case stability of Gaussian elimination*, SIAM J. Matrix Anal. Appl. 11 (1990), 335–360; https://people.maths.ox.ac.uk/~trefethen/publication/PDF/1990_44.pdf.
- T. A. Driscoll and K. L. Maki, *Searching for Rare Growth Factors Using Multicanonical Monte Carlo Methods*, SIAM Review 49 (2007), 673–692; https://doi.org/10.1137/050637662.
- A. J. Macleod, *Some statistics on Gaussian elimination with partial pivoting*, ACM SIGNUM Newsletter 24 (1989), 10–14; and the cited unpublished 1988 report *The distribution of the growth factor in Gaussian elimination with partial pivoting* (material not retrieved).
