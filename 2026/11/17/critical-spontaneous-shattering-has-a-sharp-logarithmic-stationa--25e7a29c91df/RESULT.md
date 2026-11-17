# Critical spontaneous shattering has a sharp logarithmic stationary second-moment tail

## Finding
For the discrete Smoluchowski equation with multiplicative coagulation \(K(i,j)=ij\), mass normalized to one, and spontaneous size-independent shattering of every nonmonomer cluster into monomers at rate \(\lambda=4\), there is a unique mass-one nonnegative stationary concentration sequence \((n_k)_{k\ge1}\). It has \(\sum_{k\ge1} k^2 n_k=2\) and the exact critical tail law
\[
\boxed{\lim_{N\to\infty}(\log N)\sum_{k>N} k^2 n_k=2.}
\]
Equivalently, the absolute error of the stationary second moment computed by cutting its sum after size \(N\) is asymptotic to \(2/\log N\). The stationary recurrence and the critical value \(\lambda=4\) are already known; the new assertion is the rigorous sharp logarithmic tail, including the constant and the mass-one construction from the recurrence.

## Assumptions and scope
For integer \(k\ge2\), the stationary form of the mass-one equation is
\[
0=\frac12\sum_{i=1}^{k-1}i(k-i)n_i n_{k-i}-(k+4)n_k,
\]
while the monomer equation is \(0=4-5n_1\). Here \(n_k\ge0\) are number concentrations, and \(\sum_{k\ge1}kn_k=1\). We construct and classify the mass-one stationary sequence; no assertion is made about time-dependent solutions or convergence of the kinetic flow. In particular, this is the stationary *infinite-size* system, not a finite-dimensional truncated closure.

## Proof
**1. Formal recurrence and generating ODE.** Fix \(a_1=4/5\) and define, for \(k\ge2\),
\[
a_k=\frac{k}{2(k+4)}\sum_{i=1}^{k-1}a_i a_{k-i},\qquad n_k=\frac{a_k}{k}.
\]
All coefficients are positive. Their generating series \(q(z)=\sum_{k\ge1}a_k z^k\) has positive convergence radius: for example \(a_k\le\frac12\sum_{i=1}^{k-1}a_i a_{k-i}\), allowing a Catalan majorant with positive radius. Comparing coefficients gives
\[
z(1-q)q'=4(z-q),\qquad q(0)=0,\quad q'(0)=4/5.\tag{1}
\]

**2. Existence with total mass one.** As long as the series exists on the positive real axis below \(1\), one has the strict barriers
\[
z^2<q(z)<z.\tag{2}
\]
Indeed, \(q(z)<z\) initially. At a hypothetical first contact with \(q=z\) at \(z<1\), (1) gives \(q'=0\), contrary to a first crossing from below. For the lower barrier \(q>z^2\), initially \(q(z)=\tfrac45z+O(z^2)>z^2\); at a first contact \(q=z^2\), (1) gives \(q'=4/(1+z)>2z\) for \(0<z<1\), contrary to a first crossing from above. If the radius \(R\) were smaller than \(1\), (2) would give \(q(R-)\le R<1\), and the right-hand side of the first-order ODE would be analytic at \((R,q(R-))\). Analytic continuation would extend \(q\) beyond the positive real \(R\), contradicting Pringsheim's theorem for a positive-coefficient power series. Therefore \(R\ge1\), and (2) implies \(q(1-)=1\). By monotone convergence \(\sum_{k\ge1}kn_k=1\). The recurrence gives uniqueness among nonnegative mass-one stationary sequences.

The derivative from (1) satisfies \(0<q'(z)=4(z-q)/(z(1-q))<4/z\) for \(0<z<1\). Because the coefficients of \(q'\) are nonnegative, \(q'(1-)=M\) exists and is finite. Letting \(z\uparrow1\) in (1), using \(q(z)=1-M(1-z)+o(1-z)\), yields \(M^2=4(M-1)\), hence \(M=2\). Consequently \(\sum k^2n_k=2\). The nonnegative coefficients and these finite moments make the stationary coagulation sums and mass-one monomer balance legitimate.

**3. Critical singularity.** Put \(x=1-z\), \(y(x)=1-q(1-x)\), \(u(x)=y(x)/x\), and \(v(x)=2-u(x)\). Convexity of \(q\), its value \(q(1)=1\), and endpoint slope \(q'(1-)=2\) give \(u<2\) for \(x>0\); the upper barrier \(q<z\) gives \(u>1\). Also \(u\to2\) and \(v\downarrow0\) as \(x\downarrow0\). In these variables (1) becomes exactly
\[
(1-x)u(u+xu')=4(u-1),\qquad
xv'=\frac{v^2-xu^2}{(1-x)u}.\tag{3}
\]
Writing \(t=\log(1/x)\) and \(w(t)=1/v(e^{-t})\), equation (3) is
\[
\frac{dw}{dt}=\frac{1-e^{-t}u^2w^2}{(1-e^{-t})u}.\tag{4}
\]
For all sufficiently large \(t\), \(1<u<2\) and the right side is at most \(2\), so \(w(t)=O(t)\). Thus the correction \(e^{-t}u^2w^2\to0\). Since \(u\to2\), (4) now implies \(w'(t)\to1/2\), and integration yields \(w(t)\sim t/2\), or
\[
v(x)\sim\frac{2}{\log(1/x)}.\tag{5}
\]
Finally \(q'(1-x)=y'(x)=u+dv/dt\), where (3) gives \(dv/dt=O(t^{-2})\). Hence
\[
2-q'(1-x)\sim\frac{2}{\log(1/x)}.\tag{6}
\]

**4. A monotone Tauberian step.** Set \(b_k=k^2n_k\). The nonnegative sequence has \(\sum b_k=2\), and \(q'(z)=\sum_{k\ge1}b_k z^{k-1}\). Define the nonincreasing tail \(H(T)=\sum_{k-1>T}b_k\). For \(s>0\), direct integration of each positive term proves
\[
2-q'(e^{-s})=s\int_0^\infty e^{-sT}H(T)\,dT.\tag{7}
\]
Equation (6) makes the left side asymptotic to \(2/\log(1/s)\). Karamata's Laplace Tauberian theorem gives \(\int_0^T H(t)dt\sim2T/\log T\). Since \(H\) is nonincreasing, the monotone-density theorem yields \(H(T)\sim2/\log T\). Replacing the \(k-1\) threshold by the integer threshold \(k>N\) (a unit shift) does not change the asymptotic, proving the boxed limit.

## Verification
The accompanying standard-library program `check_stationary.py` computes 18 exact rational recurrence coefficients, checks all 18 exact coefficients of (1), and tests 6,000 floating-point recurrence coefficients. It prints `VERIFY_OK exact_series_coefficients=18 finite_prefix=6000` and increasing values of \((2-\sum_{k\le N}k^2n_k)\log N\) for the three cutoffs \(N=100,1000,6000\). These are consistency checks; the proof of the infinite limit relies on the barriers, ODE asymptotics and Tauberian arguments, not a finite experiment. Execute `python3 check_stationary.py` from the extracted files' directory.

## Relationship to prior work
Matveev, *Suppression of gel formation by spontaneous fragmentation*, arXiv:2611.09537v1 (6 November 2026), derives the critical rate \(4\), steady-state monomer value \(4/5\), generating equation and coefficient recurrence (his (8), (12)), and discusses finite numerical cutoffs. All those identities are treated here as prior work and rederived only to validate the hypothesis of the asymptotic. That paper does not state the \(2/\log N\) second-moment tail or its proof. Matveev's earlier aggregation–fragmentation review and other coagulation/shattering work concern related but different kernels or fragmentation schemes. The present claim is a sharp infinite-size *moment truncation* law, not a new gelation threshold.

## Limitations
The limit concerns the unique mass-one stationary sequence of the *infinite* product-kernel model at precisely \(\lambda=4\); it is not a uniform estimate for arbitrary finite \(N\), not a statement about \(\lambda>4\), and not a rate of dynamical convergence in time. Its use of classical Pringsheim and monotone Tauberian theorems is explicit. Some adjacent journal literature was not available in full text; historical priority is not independently established. No independent scientific audit has been performed.

## References
1. S. Matveev, *Suppression of gel formation by spontaneous fragmentation*, arXiv:2611.09537v1 (first public posting 2026-11-06), https://arxiv.org/abs/2611.09537. Especially §§2–3 and eqs. (8), (12).
2. S. A. Matveev et al., *Generating functions and efficient numerical simulation of aggregation-fragmentation kinetics*, arXiv:2606.10785 (2026), https://arxiv.org/abs/2606.10785. Related kernels and fragmentation models.
3. N. H. Bingham, C. M. Goldie, J. L. Teugels, *Regular Variation*, Cambridge University Press (1987): Laplace Tauberian theorem and monotone density theorem.
4. B. T. Fagan, N. J. MacKay, A. J. Wood, *Robustness of steady state and stochastic cyclicity in generalized coalescence-fragmentation models*, European Physical Journal B 97 (2024), 21. Related stochastic and numerical models, full text not inspected.
