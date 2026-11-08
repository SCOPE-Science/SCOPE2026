# Six-step boundary law for extraneous zeros of antipodal weighted-Bergman divisors

## Finding
For every fixed integer \(\beta\ge 1\), let \(\mathcal H_\beta\) be the analytic reproducing-kernel Hilbert space on the open unit disk \(\mathbb D\), with kernel \(K_\beta(z,w)=(1-z\overline w)^{-\beta}\). For \(0<r<1\), write \(M_r=\{f\in\mathcal H_\beta:f(r)=f(-r)=0\}\), and let \(F_{\beta,r}=P_{M_r}1\). It is nonzero, and its zeros, counted with multiplicity in \(\mathbb D\), have the following exact classification for every sufficiently large \(r<1\) (threshold depending on \(\beta\)):

\[
\boxed{N_\beta=4\left\lceil\frac{\beta}{6}\right\rceil-2,\qquad E_\beta=N_\beta-2=4\left(\left\lceil\frac{\beta}{6}\right\rceil-1\right).}
\]

Here \(E_\beta\) counts *extraneous* zeros not among the two prescribed simple zeros \(\pm r\). All disk zeros are simple for such \(r\). All extraneous zeros are nonreal and occur in four-element symmetry orbits under sign and complex conjugation. In particular, the first extras occur at \(\beta=7\), exactly four of them; the count rises by four at \(\beta=13,19,25,\ldots\).

Writing \(\varepsilon=1-r^2\) and \(\omega_j=e^{2\pi i j/\beta}\), the full set of \(2\beta\) complex zeros, expressed in the rescaled variable \(t=rz\), has the sharp cluster description
\[
t_{+,j}=1-\varepsilon\omega_j+O_\beta(\varepsilon^{\beta+2}),\qquad t_{-,j}=-t_{+,j},\qquad 0\le j<\beta.
\]
The positive and negative clusters each contribute exactly \(2\lceil\beta/6\rceil-1\) zeros to \(\mathbb D\).

## Assumptions and scope
The integer \(\beta\) is fixed before taking \(r\uparrow1\); no uniformity in growing \(\beta\) is asserted. At \(\beta=1\), the space is classical Hardy space. For integers \(\beta\ge2\), it is the radial weighted Bergman space with normalized area weight \((\beta-1)(1-|z|^2)^{\beta-2}dA(z)/\pi\). The assertion is about the canonical Hilbert-space projection onto the two evaluation kernels' orthogonal complement, not arbitrary inner factors or arbitrary prescribed zero configurations.

## Proof
**1. Exact extremal.** Since the two evaluation kernels are linearly independent and \(K_\beta(z,r)+K_\beta(z,-r)\) is even, its value at either \(\pm r\) is
\[
D_\beta(r)=(1-r^2)^{-\beta}+(1+r^2)^{-\beta}.
\]
Projection of \(1\) onto their span is exactly their sum divided by \(D_\beta(r)\), because the corresponding residual vanishes at both interpolation sites. Thus
\[
F_{\beta,r}(z)=1-\frac{(1-rz)^{-\beta}+(1+rz)^{-\beta}}{(1-r^2)^{-\beta}+(1+r^2)^{-\beta}}.
\]
The residual is nonzero because its value at the origin is \(1-2/D_\beta(r)>0\). It spans the canonical zero-based extremal ray, up to normalization.

**2. Exact algebraic degree and two clusters.** Set \(q=r^2=1-\varepsilon\), \(t=rz\), and \(C=\varepsilon^{-\beta}+(2-\varepsilon)^{-\beta}\). The zeros of the extremal are exactly those of the even polynomial
\[
P_{\beta,\varepsilon}(t)=C(1-t^2)^\beta-(1+t)^\beta-(1-t)^\beta,
\]
of degree \(2\beta\); \(t=\pm1\) are not roots. Multiplication by \(\varepsilon^\beta\) gives a polynomial tending coefficientwise to \((1-t^2)^\beta\). Continuity of roots, or the argument principle on two disjoint small circles centered at \(\pm1\), therefore locates precisely \(\beta\) roots (with multiplicities) in each cluster and no others for small \(\varepsilon>0\).

**3. Resolve all cluster roots.** Near \(t=1\), put \(t=1-\varepsilon v\). The zero equation is
\[
v^{-\beta}-1+\varepsilon^\beta\big[(2-\varepsilon v)^{-\beta}-(2-\varepsilon)^{-\beta}\big]=0.
\]
For \(\varepsilon=0\) the \(\beta\) simple roots are the roots of unity \(v=\omega_j\), with derivative \(-\beta\omega_j^{-\beta-1}\ne0\). The analytic implicit-function theorem provides a unique simple root \(v_j(\varepsilon)\) near each. The bracket is \(O_\beta(\varepsilon)\) uniformly near these finitely many points, so \(v_j(\varepsilon)=\omega_j+O_\beta(\varepsilon^{\beta+1})\). Consequently \(t_{+,j}=1-\varepsilon\omega_j+O_\beta(\varepsilon^{\beta+2})\). Evenness of the polynomial gives \(t_{-,j}=-t_{+,j}\). The \(j=0\) branches are exactly \(t=\pm r^2\), because both points are prescribed zeros.

**4. Boundary comparison, including tangent cases.** The actual sampling disk \(|z|<1\) is \(|t|<r\). Uniformly for each of the finitely many roots,
\[
|t_{+,j}|^2-r^2=\varepsilon\left(1-2\cos\frac{2\pi j}{\beta}\right)+\varepsilon^2+O_\beta(\varepsilon^{\beta+2}).
\]
When the cosine is above or below \(1/2\), the first-order term strictly determines membership. When it equals \(1/2\), possible only for \(6\mid\beta\), the first-order term vanishes and the **positive** second-order term dominates because \(\beta+2>2\); the boundary-tangent branches lie **outside**, not on, the sampling disk. Thus the admissible indices satisfy the strict inequality \(\cos(2\pi j/\beta)>1/2\), equivalent to \(j=0\) or \(1\le j<\beta/6\), or their negative residues. Their number per cluster is \(2\lceil\beta/6\rceil-1\). Twice this gives the asserted total, after removing the two prescribed roots. Every other interior branch is nonreal; the polynomial has real coefficients and is even, so extra zeros occur in four-element sign/conjugation orbits. All roots are simple by their separate analytic branches.

## Verification
A separate numerical checker `CHECK.py` reconstructs all \(2\beta\) branches from the exact nonlinear equation at two small separations and checks their location, normalized zero equations, and predicted counts for integers \(1\le\beta\le24\). Its output is `ANTIPODAL_KERNEL_CHECKS_PASS 2448`. The proof, not finite computation, establishes the universal statement. The checker requires Python with `mpmath` and runs as `python CHECK.py`.

## Relationship to prior work
Felder and Le [1] establish the RKHS projection/Shapiro–Shields framework, including the importance of extraneous zeros and their effect on zero-set identification. Aleman–Hedenmalm–Richter–Sundberg [2] study canonical divisors and their one-point extremals. Related work [3] addresses optimal polynomial approximants, a different projection problem. Hedenmalm and Zhu [7, Proposition 3] explicitly derive the same root-of-unity half-plane criterion for **one prescribed zero**; hence that ingredient and the first possible integer-power threshold are prior mathematics. The present result concerns the interaction of two prescribed antipodal zeros, proving the exact two-cluster decomposition, all multiplicities and the tangent-branch verdict. Cheng, Mashreghi and Ross [6] establish lower bounds and existence of extra zeros for some single-zero extremals, including weighted-Bergman examples, without determining the antipodal root locations. The precise antipodal two-point boundary clusters, the six-step integer-power count, and the distinction between tangent and interior branches are not stated in the relevant passages inspected in [1]–[3]. This is a limited scientific comparison, not a claim that all earlier literature has been exhausted. A 2026 mathematical record establishes arbitrarily many **real** extraneous zeros from some finite weighted-Bergman zero sets, which does not imply the exact two-antipodal-point, nonreal boundary count here; its full proof was not available for inspection.

## Limitations
The theorem applies only for \(r\) sufficiently close to \(1\) with fixed positive integer \(\beta\); no explicit universal radius threshold is given. It does not classify the full parameter range \(0<r<1\), noninteger exponents, nonsymmetric zero configurations, or multipliers on other RKHSs. An equivalent special-case formula may exist in older canonical-divisor studies not available in full text. Independent mathematical validation has not been performed.

## References
[1] C. Felder and T. Le, *Analogues of Finite Blaschke Products as Inner Functions*, arXiv:2105.01766v1 (May 4, 2021), revised v2 June 6, 2022, §§3, 5. https://arxiv.org/abs/2105.01766
[2] A. Aleman, H. Hedenmalm, S. Richter, C. Sundberg, *Curious properties of canonical divisors in weighted Bergman spaces*, manuscript April 1996, posted arXiv:math/0406369v1 (June 18, 2004), §3. https://arxiv.org/abs/math/0406369
[3] C. Bénéteau, D. Khavinson, C. Liaw, D. Seco, A. Sola, *Orthogonal polynomials, reproducing kernels, and zeros of optimal approximants*, arXiv:1509.04807 (2015). https://arxiv.org/abs/1509.04807
[4] T. Le, *Inner functions in weighted Hardy spaces*, arXiv:1912.05715 (2019), discussion of additional zeros for weighted kernels. https://arxiv.org/abs/1912.05715
[6] R. Cheng, J. Mashreghi, W. T. Ross, *Inner functions in reproducing kernel spaces*, arXiv:1807.06341 (2018), §§5–6. https://arxiv.org/abs/1807.06341
[7] H. Hedenmalm and K. Zhu, *On the Failure of Optimal Factorization for Certain Weighted Bergman Spaces*, Complex Variables 19 (1992), 165–176, Propositions 2–4. https://people.kth.se/~haakanh/publications/hed-zhu-cvta.pdf
