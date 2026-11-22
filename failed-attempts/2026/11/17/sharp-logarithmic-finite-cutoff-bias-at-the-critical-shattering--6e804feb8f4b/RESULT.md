# Sharp logarithmic finite-cutoff bias at the critical shattering threshold

## Finding

Consider the stationary mass-one discrete coagulation–shattering model with multiplicative coagulation kernel and independent complete shattering into monomers at rate \(\lambda=4\). Let \((n_k)_{k\ge1}\) be its nonnegative stationary concentrations, uniquely specified by
\[
n_1=\frac45,\qquad n_k=\frac{1}{2(k+4)}\sum_{j=1}^{k-1}j(k-j)n_jn_{k-j}\quad(k\ge2).
\]
Set the omitted second-moment mass after a cluster-size cutoff \(N\) to be
\[
R_N=\sum_{k>N}k^2n_k.
\]
Then
\[
\boxed{\lim_{N\to\infty}(\log N)R_N=2.}
\]
Consequently, every moment of order \(p>2\) diverges, whereas all real moments of order \(p\le2\) are finite; and for \(N_\varepsilon=\min\{N\ge1:R_N\le\varepsilon\}\),
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon\log N_\varepsilon=2.}
\]
The second statement is about the cutoff of the *true infinite stationary distribution*, not the stationary solution of a separately truncated kinetic system.

## Assumptions and scope

The model is the discrete mass-one product-kernel system of Matveev [1]. A cluster of size \(k\ge2\) shatters into \(k\) monomers at a size-independent rate, and the coagulation rate between sizes \(i,j\) is \(ij\). Rates are normalized so the shattering rate is exactly \(4\). The stationary equations above define the unique positive coefficient sequence, since \(n_1\) is fixed and every later term depends on earlier terms. The model uses no source or loss of mass.

The physical stationary solution has
\[
\sum_{k\ge1}k n_k=1,\qquad \sum_{k\ge1}k^2n_k=2.
\]
For completeness, these boundary identities also follow from the supercritical stationary solutions [1]: as \(\lambda\downarrow4\), their coefficientwise recurrence converges, their second moments tend to \(2\), and Fatou's lemma bounds the limiting second moment by \(2\). Uniform second-moment bounds ensure preservation of total mass \(1\), because the tail of the first moment past \(K\) is at most \(2/K\). Writing \(A(z)=\sum_{k\ge1}k n_k z^k\), the stationary equation implies \(z(1-A(z))A'(z)=4(z-A(z))\) for \(0<z<1\). Letting \(z\uparrow1\) and writing \(m=A'(1)\le2\), one gets \(m^2=4(m-1)\), hence \(m=2\). These steps verify the finite-moment premise at the endpoint instead of inferring it from a finite truncation.

## Proof

**1. Exact generating equation.** Define \(G(z)=\sum_{k\ge1}n_kz^k\) and \(A(z)=zG'(z)\) for \(0\le z<1\). Summing the stationary recurrences gives
\[
\frac12 A(z)^2-A(z)-4G(z)+4z=0.
\]
Differentiation at interior points and \(G'(z)=A(z)/z\) give
\[
z(1-A(z))A'(z)=4(z-A(z)). \tag{1}
\]
Because \(n_k>0\) for every positive integer \(k\), \(A'(z)\) is strictly increasing in \(z\); its limit at \(1\) equals \(2\).

**2. The marginal singularity.** For \(w=1-z\) define
\[
B(w)=1-A(1-w),\qquad h(w)=2-\frac{B(w)}w.
\]
The mean value identity \(B(w)/w=w^{-1}\int_{1-w}^1 A'(s)\,ds\) implies \(0<h(w)<2\) and \(h(w)\to0\) as \(w\downarrow0\). Since \(A'(1)=2\), the signs and all limits are justified.

Equation (1), using \(B_w=A'(1-w)\), reads \((1-w)B B_w=4(B-w)\). Substitution of \(B=w(2-h)\) gives the **exact** scalar equation
\[
w h_w=\frac{h^2}{(1-w)(2-h)}-\frac{w(2-h)}{1-w}. \tag{2}
\]
Write \(L=\log(1/w)\), \(w=e^{-L}\), and \(u(L)=1/h(e^{-L})\). Then (2) yields
\[
\frac{du}{dL}=\frac{1}{(1-w)(2-h)}-\frac{w(2-h)}{(1-w)h^2}. \tag{3}
\]
For all sufficiently large \(L\), the first term is at most \(1\); the second is nonnegative. Therefore \(u(L)\le L+C\) for a finite constant \(C\). It follows that \(h\ge (L+C)^{-1}\), so \(w/h^2\le e^{-L}(L+C)^2\to0\). The first term of (3) tends to \(1/2\), while the second tends to zero. Thus \(u'(L)\to1/2\), and integration gives \(u(L)/L\to1/2\), equivalently
\[
h(w)\sim\frac{2}{\log(1/w)}. \tag{4}
\]
Further, (2) implies \(w h_w=O(h^2)+O(w)=o(h)\). Consequently
\[
q(w):=2-A'(1-w)=h(w)+w h_w(w)\sim\frac{2}{\log(1/w)}. \tag{5}
\]
There is no appeal here to a pointwise coefficient asymptotic or to an unproved Tauberian hypothesis.

**3. Tauberian sandwich for positive coefficients.** Put \(\mu_k=k^2n_k>0\), so \(\sum_k\mu_k=2\). By direct summation,
\[
q(w)=\sum_{k\ge1}\mu_k\big[1-(1-w)^{k-1}\big]. \tag{6}
\]
Fix a large integer \(N\) and write \(\ell=\log N\). Choose \(w_-=1/(N\ell^2)\) and \(w_+=\ell^2/N\). The elementary inequality \(1-(1-w)^{k-1}\le(k-1)w\), valid for \(k\le N\), yields
\[
q(w_-)\le R_N+\frac{2}{\ell^2}. \tag{7}
\]
For \(k>N\), \(1-(1-w_+)^{k-1}\ge1-e^{-\ell^2}\); consequently
\[
q(w_+)\ge (1-e^{-\ell^2})R_N. \tag{8}
\]
Both \(\log(1/w_\pm)/\log N\to1\). Combining (5), (7) and (8) therefore proves \((\log N)R_N\to2\).

**4. Moment and cutoff consequences.** Finiteness of the second moment implies finite moments of every order \(p\le2\). If a moment of order \(p>2\) were finite, then \(R_N\le N^{-(p-2)}\sum_k k^p n_k\), contrary to the logarithmic asymptotic. For the minimal cutoff \(N_\varepsilon\), monotonicity of \(R_N\) and its two-sided sharp asymptotic imply \(\varepsilon\log N_\varepsilon\to2\); this follows also by comparing with integer parts of \(\exp((2\pm\delta)/\varepsilon)\) for each fixed \(\delta>0\).

## Verification

The full inference is analytic. The accompanying standalone `check.py` independently evaluates the stationary recurrence, tests the generating-function identity at several interior arguments, and displays positive, very slowly vanishing finite-cutoff second-moment tails. Finite numerical tests corroborate the algebra but neither establish the limit nor imply a pointwise asymptotic for \(n_k\).

## Relationship to prior work

Matveev [1, Sections 1–3] derives the stationary recurrence, the mass conservation regime \(\lambda\ge4\), and the exact second moment at criticality. The new result is the sharp **cluster-size-cutoff second-moment tail** \(R_N\sim2/\log N\) and its moment/cutoff consequences. The previously established moment formula \(M_2=2\) alone does not determine this convergence rate. Fagan, MacKay and Wood [2] study generalized stochastic coalescence-fragmentation and finite-cluster effects, not this exact infinite critical recurrence. Tran and Van [3] study a **continuous-mass binary fragmentation kernel** \(b(s,t)=1\), which is not the discrete complete-monomer shattering law. The comparison does not claim that similarly phrased logarithmic tails in other models are new.

## Limitations

No pointwise formula such as \(n_k\sim C/[k^3(\log k)^2]\) is proved; a tail sum does not by itself force a pointwise equivalent without added regularity. The theorem does not establish transient-in-time convergence, finite-system cutoff dynamics, results below the critical shattering rate, or universal behavior for other fragmentation laws. The comparison with available literature leaves the usual risk of an unindexed earlier equivalent.

## References

[1] S. Matveev, *Suppression of gel formation by spontaneous fragmentation*, arXiv:2611.09537v1 (first posted 2026-11-06), https://arxiv.org/html/2611.09537v1 .

[2] B. T. Fagan, N. J. MacKay, and A. J. Wood, *Robustness of steady state and stochastic cyclicity in generalized coalescence-fragmentation models*, European Physical Journal B 97, 21 (2024); preprint arXiv:2310.04226, https://arxiv.org/abs/2310.04226 .

[3] H. V. Tran and T.-S. Van, *Local mass-conserving solution for a critical coagulation-fragmentation equation*, arXiv:2202.03394v3, https://arxiv.org/html/2202.03394v3 .
