# Uniformly convex Fourier weights: an exact all-dimensional subconvolution threshold

## Finding
For \(d\ge2\), \(2\le q<\infty\), \(a>0\) and \(p\ge0\), put
\[
\rho(k)=\left(\sum_{j=1}^{d}|k_j|^q\right)^{1/q},\quad
w(k)=e^{-a\rho(k)}(1+\rho(k))^{-p},\qquad k\in\mathbb Z^d.
\]
The counting-measure convolution satisfies the uniform estimate \((w*w)(n)\le Cw(n)\), simultaneously for all \(n\in\mathbb Z^d\), **if and only if**
\[
p>p_c(d,q):=1+(d-1)\left(1-\frac1q\right).
\]
For \(Q_N=(w*w)(Ne_1)/w(Ne_1)\), the complete order transition is
\[
Q_N\asymp\begin{cases}N^{p_c-p},&0\le p<p_c,\\ \log N,&p=p_c.\end{cases}
\]
For \(p>p_c\), there is also an exact finite limit
\[
\lim_{N\to\infty}Q_N=2\sum_{k\in\mathbb Z^d}e^{-a(\rho(k)-k_1)}(1+\rho(k))^{-p}.
\]
In particular the critical exponent varies continuously from \((d+1)/2\) at the Euclidean norm to the cubical limiting value \(d\), quantifying the weakening of strict convexity near coordinate axes.

## Assumptions and scope
All parameters are fixed before the integer \(N\to\infty\) limit. The exponent \(q\) is finite and at least \(2\); the ambient lattice is \(\mathbb Z^d\), \(d\ge2\). The notation \(A_N\asymp B_N\) means two positive bounds with parameter-dependent constants for all sufficiently large \(N\). A Fourier Hilbert space induced by these weights is the Fourier-image of weighted coefficient \(\ell^2\); the theorem proves the exact subconvolutivity condition, without claiming that no different multiplication-algebra argument could work below it. There is no uniformity asserted as \(q\to\infty\) or \(a\downarrow0\).

## Proof
**1. Uniform convexity supplies the transverse penalty.** Let \(\|\cdot\|_q\) denote the norm \(\rho\). Fix a dual unit vector \(u\in\ell^{q'}\), let \(v\in\ell^q\) be its unique norming unit vector, so \(u\cdot v=1\). Write \(\delta=1-u\cdot x\) for a unit vector \(x\). Clarkson's inequality for \(q\ge2\) states
\[
\left\|\frac{x+v}{2}\right\|_q^q+\left\|\frac{x-v}{2}\right\|_q^q\le1.
\]
The first norm is at least \(1-\delta/2\); Bernoulli's elementary estimate \(1-(1-t)^q\le qt\) on \(0\le t\le1\) gives
\[
\delta\ge\frac{2^{1-q}}q\|x-v\|_q^q.
\]
Consequently for \(k\ne0\), \(r=\rho(k)\), the nonnegative norming-functional defect satisfies
\[
\rho(k)-u\cdot k\ge c_q r^{1-q}\operatorname{dist}_2(k,\mathbb R_{\ge0}v)^q.
\tag{1}
\]
Here Euclidean and \(\ell^q\) distances are compared with fixed dimension constants.

**2. Uniform conical lattice bound.** In a dyadic shell \(L\le\rho(k)<2L\), \(L\ge1\), an oriented tube of radius \(W\ge1\) around a ray contains at most \(C_d(L+W+1)(W+1)^{d-1}\) integer lattice points. To see this, cover all lattice unit cubes meeting the tube by a Euclidean cylinder of comparable length and radius and compare volumes. In (1), choose \(W_0=L^{1-1/q}\). Points whose transverse distance lies between \(2^hW_0\) and \(2^{h+1}W_0\) carry an exponential factor at most \(e^{-c2^{hq}}\). The tube-count bound and summation in \(h\ge0\) thus yield, uniformly over all dual unit vectors \(u\),
\[
\sum_{L\le\rho(k)<2L}e^{-a(\rho(k)-u\cdot k)}
\le C_{d,q,a}L^{1+(d-1)(1-1/q)}=C_{d,q,a}L^{p_c}.
\tag{2}
\]
For the outermost tubes \(W>L\), the crude \(O(L^d)\) shell count is absorbed by the exponentially small factor. Each \(W\le L\) tube has the stated bound. The finitely many points near the origin have harmless mass.

**3. Sufficiency.** For \(n\ne0\), take its norming functional \(u\), so \(\rho(n-k)\ge\rho(n)-u\cdot k\). Hence the triangle defect \(\rho(k)+\rho(n-k)-\rho(n)\) is at least \(\rho(k)-u\cdot k\). If \(p\ge1\), the triangle inequality gives
\[
\left[\frac{1+\rho(n)}{(1+\rho(k))(1+\rho(n-k))}\right]^p
\le 2^{p-1}\big((1+\rho(k))^{-p}+(1+\rho(n-k))^{-p}\big).
\]
By symmetry of convolution, \((w*w)(n)/w(n)\) is at most
\[
2^p\sum_{k\in\mathbb Z^d}e^{-a(\rho(k)-u\cdot k)}(1+\rho(k))^{-p}.
\]
Its dyadic-shell contributions are \(O(2^{j(p_c-p)})\) by (2). They sum uniformly in \(u\) for \(p>p_c\), which also implies \(p>1\). At \(n=0\), the quotient is \(\sum_k w(k)^2<\infty\). This proves sufficiency with no angular restriction on \(n\).

**4. Axial counting and necessity.** Write \(k=(m,z)\), where \(z\in\mathbb Z^{d-1}\), and define \(F(s,z)=(s^q+\|z\|_q^q)^{1/q}-s\) for \(s\ge0\). If \(0\le m\le N\), the triangle defect is \(F(m,z)+F(N-m,z)\). Standard elementary comparison of \((1+t^q)^{1/q}-1\) on \(0\le t\le1\) and \(t\ge1\) gives
\[
F(s,z)\asymp_q \min\left(\frac{\|z\|_q^q}{s^{q-1}},\|z\|_q\right)
\]
for \(s>0\), interpreting the first term as infinite at \(s=0\). In particular, with \(\alpha=(d-1)(1-1/q)\), lattice-ball comparison yields
\[
\sum_{z\in\mathbb Z^{d-1}} e^{-aF(s,z)}\le C(1+s)^\alpha.
\tag{3}
\]
For \(m\le N/2\), the polynomial quotient is at most \(2^p(1+\rho(m,z))^{-p}\le2^p(1+m)^{-p}\). Apply (3), repeat symmetrically for \(m\ge N/2\), and sum. Terms with \(m<0\) or \(m>N\) contribute \(O(1)\): the triangle defect has an additional \(2\operatorname{dist}(m,[0,N])\) and (3) bounds the transverse sum polynomially. Therefore
\[
Q_N\le C\left(1+\sum_{m=1}^{\lfloor N/2\rfloor}(1+m)^{\alpha-p}\right).
\tag{4}
\]
For \(p<p_c=1+\alpha\), restrict to \(N/3\le m\le2N/3\) and \(|z_j|\le cN^{1-1/q}\); every such summand has bounded exponential penalty and polynomial quotient bounded below by \(c'N^{-p}\). Their number is \(\gtrsim N^{1+\alpha}\), yielding \(Q_N\gtrsim N^{p_c-p}\). At \(p=p_c\), instead use \(1\le m\le N/4\) and \(|z_j|\le cm^{1-1/q}\), giving a lower bound \(c\sum_{m\le N/4}m^{\alpha-p_c}\gtrsim\log N\). Together with (4), both sharp orders follow, and the uniform subconvolution bound fails whenever \(p\le p_c\).

**5. Exact supercritical axial limit.** For \(p>p_c\), split the convolution at \(m=\lfloor N/2\rfloor\). On the half \(m\le N/2\), the pointwise summand normalized by \(w(Ne_1)\) tends for each fixed \(k\) to \(e^{-a(\rho(k)-k_1)}(1+\rho(k))^{-p}\). Since \(1+\rho(Ne_1-k)\ge1+N/2\), it is bounded by \(2^p\) times this summable limit term. Dominated convergence applies by (2). The opposite half is identical by \(k\leftrightarrow Ne_1-k\), apart from a possible midpoint layer whose contribution vanishes by the same domination. The limit is exactly twice the displayed convergent sum.

## Verification
The accompanying `CHECKER.py` recomputes finite truncated axial quotients independently from their defining convolution sum for several pairs \((d,q)\), including nonintegral critical exponents and a three-dimensional geometry. It checks finite-value positivity and the predicted growth direction; it is not an infinite proof and truncation does not certify the limiting coefficients. Each indispensable infinite claim is supported instead by steps 1–5. The nonstandard tube estimate follows from unit-cube covering, and the uniform convexity constant is explicit.

## Relationship to prior work
Das and Giannakis introduce subconvolutive Fourier weights as hypotheses ensuring multiplication algebras on compact abelian groups; their accessible article's Theorem 4 assumes the convolution bound and does not give this sharp all-dimensional \(\ell^q\) criterion. Kaleta and Ponikowski study directional convolution equivalence for almost-radial continuous densities; their abstract does not supply the discrete anisotropic decision test. Earlier special-case work establishes the planar fourth-power-norm threshold and the cubical endpoint, neither of which implies the continuum of finite \(q\) with uniform conical bounds and exact supercritical axial limits. A search did not establish an equivalent published theorem; this is a best-knowledge literature comparison, not a claim of certified historical priority.

## Limitations
No explicit sharp critical logarithmic coefficient or subcritical leading constant is asserted. All equivalence constants may depend on fixed parameters, and the results exclude \(1\le q<2\) and the exact \(q=\infty\) case. The upper proof gives existence rather than the sharp smallest global subconvolution constant. The theorem does not establish a necessity criterion for every possible Fourier multiplication algebra independently of its subconvolution definition. Some potentially related full primary sources were not accessible in complete text; independent verification of priority remains outstanding.

## References
1. S. Das and D. Giannakis, *On Harmonic Hilbert Spaces on Compact Abelian Groups*, arXiv:1912.11664 (initial submission 25 December 2019); *Journal of Fourier Analysis and Applications* 29 (2023), article 12, DOI:10.1007/s00041-023-09992-4.
2. K. Kaleta and D. Ponikowski, *On directional convolution equivalent densities*, arXiv:2109.06336 (initial submission 13 September 2021); *Electronic Journal of Probability* 27 (2022), DOI:10.1214/22-EJP790.
3. Das and Giannakis, *Correction to: On Harmonic Hilbert Spaces on Compact Abelian Groups*, DOI:10.1007/s00041-023-10043-1 (on a distinct Gelfand spectrum hypothesis, not a change to their subconvolution criterion).
