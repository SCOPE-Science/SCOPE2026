# First-resonance activation at every higher even Fourier moment

## Finding

Let \(k\ge3\) and \(m\ge1\) be integers. Let \(n\ge km\) be an integer and let
\[
 V_{m,n}=\operatorname{span}_{\mathbb C}\{1,z^m,z^n\}\subset L^2(\mathbb T),\qquad P_\rho(z^j)=\rho^jz^j,\quad0<\rho\le1.
\]
The circle carries normalized Haar measure. Write \(\mathcal M_{k;m,n}(\rho)=\max_{\|f\|_2=1,\ f\in V_{m,n}}\|P_\rho f\|_{2k}^{2k}\) and \(s=\rho^{2m}=1/k+\delta\). All statements below concern a sufficiently small positive \(\delta\), for fixed \(k,m,n\).

1. For every \(n>km\), every maximizing polynomial has its \(z^n\) coefficient **exactly zero**. Its squared \(z^m\)-coefficient magnitude is uniquely determined and equals
\[
 x_*(\delta)=\frac{2k^2}{k^2-1}\delta+O_k(\delta^2).
\]
Its optimal moment is independent of \(n\) in this range and satisfies
\[
 \mathcal M_{k;m,n}(\rho)=1+\frac{k^4}{k^2-1}\delta^2+O_k(\delta^3).
\]
2. At the first possible \(k\)-fold additive collision, \(n=km\), every maximizing polynomial has **all three coefficients nonzero**. After multiplication by a common unimodular constant and rotation of the circle, its coefficients \(a,b,c\) are uniquely determined positive real numbers, with \(a^2+b^2+c^2=1\). They satisfy
\[
 b^2=\frac{2k^2}{k^2-1}\delta+O_k(\delta^2),\qquad
 c=\frac{1}{k^k-k}\left(\frac{2k^2}{k^2-1}\right)^{k/2}\delta^{k/2}+O_k(\delta^{k/2+1}).
\]
In the original complex coefficients, the unique phase constraint at equality is
\[
 k\arg b\equiv(k-1)\arg a+\arg c\pmod{2\pi}.
\]
The resonant optimum exceeds the nonresonant optimum by the sharp asymptotic
\[
 \mathcal M_{k;m,km}(\rho)-\mathcal M_{k;m,n}(\rho)
 =C_k\delta^k+o_k(\delta^k)\quad(n>km),\qquad
 C_k=\frac{k^{1-2k}}{1-k^{1-k}}\left(\frac{2k^2}{k^2-1}\right)^k>0.
\]
The scale \(\delta^{k/2}\) of the newly activated Fourier coefficient is strictly higher order than the \(\delta^{1/2}\) scale of the first activated coefficient.

At and below \(\rho_0=k^{-1/(2m)}\), the sharp moment is \(1\), with the constant functions the only maximizers at \(\rho=\rho_0\). The theorem makes **local** assertions immediately above \(\rho_0\), not a complete phase diagram at arbitrary radii. The big-O constants may depend on the fixed integer parameters.

## Assumptions and scope

The frequency \(n\) is an integer at least \(km\); intermediate gaps \(m<n<km\) are not classified. Maximizers range over complex coefficients with the input \(L^2\)-norm one; no positivity assumption is imposed on input coefficients. The output norm is the \(2k\)-th **power** of the circle \(L^{2k}\)-norm, not the norm itself. A global phase and circle rotation are equivalences, not additional distinct maximizers.

## Proof

**1. Exact Fourier-moment identity and the first collision.** Put \(f=a+bz^m+cz^n\). The Fourier coefficients of \((P_\rho f)^k\) are the multinomial sums
\[
 \binom{k}{i,j,\ell}\,a^i(\rho^m b)^j(\rho^n c)^\ell,
 \qquad i+j+\ell=k,
\]
with output exponent \(jm+\ell n\). If \(n>km\), two different multisets \((j,\ell)\) cannot have equal output exponent: a change in \(\ell\) costs at least \(n>km\), exceeding the largest possible change in \(jm\). Orthogonality therefore gives, with \(x=|b|^2\), \(y=|c|^2\), \(a_2=1-x-y\), and \(t=\rho^{2n}\),
\[
 F_{\rm nr}(x,y;s,t)=\sum_{i+j+\ell=k}\binom{k}{i,j,\ell}^{\!2}a_2^i(sx)^j(ty)^\ell.
\]
If \(n=km\), exactly one extra collision occurs: the \(k\) lower-frequency factors and one higher-frequency factor with \(k-1\) constant factors both contribute to exponent \(km\). The moment is
\[
 F_{\rm r}(x,c;s)=F_{\rm nr}(x,c^2;s,s^k)+2ks^k(1-x-c^2)^{(k-1)/2}x^{k/2}c
\]
when coefficients are phase aligned. For arbitrary phases, the last term has an extra factor \(\cos(k\arg b-(k-1)\arg a-\arg c)\). It is strictly maximized by alignment whenever all three coefficients are nonzero. There are no other phase-dependent terms.

**2. Strict critical contractivity without an imported equality theorem.** For a finite analytic polynomial \(g(w)=\sum_{j\ge0}u_jw^j\) let \(r=k^{-1/2}\). The coefficient of \(w^J\) in \(g(rw)^k\) is a sum over \(N_{k,J}=\binom{J+k-1}{k-1}\) ordered weak compositions of \(J\). Cauchy--Schwarz gives
\[
 |[w^J]g(rw)^k|^2\le N_{k,J} k^{-J}
 \sum_{j_1+\cdots+j_k=J}\prod_{h=1}^k|u_{j_h}|^2.
\]
There are \(k^J\) ways to assign \(J\) individually labeled objects to \(k\) boxes, at least one for every occupancy composition, so \(N_{k,J}\le k^J\), strictly for \(J\ge2\). Summation over \(J\) proves \(\|g(r\cdot)\|_{2k}^{2k}\le\|g\|_2^{2k}\). If any positive-degree coefficient of \(g\) is nonzero, the summand for the ordered \(k\)-tuple consisting of that degree only has \(J\ge k\ge3\) and positive mass, making the inequality strict. Hence constants are the unique critical extremizers.

Apply this to \(g=a+bw+cw^k\). For \(n=km\), the substitution \(w=z^m\) gives precisely the critical moment. For \(n>km\), its phase-independent diagonal sum has the \(c\)-weight \(\rho^{2n}<\rho^{2km}\) at \(\rho=\rho_0\), and is at most the phase-aligned resonant sum. Consequently the only normalized critical extremizers for both families are constants. For smaller radii coefficient damping and the previous inequality imply contractivity. Compactness now forces all maximizing coefficient magnitudes to tend to \((1,0,0)\) as \(s\downarrow1/k\).

**3. The lower-mode branch.** Setting \(c=0\) in either formula gives
\[
 H_k(x,s)=\sum_{j=0}^k\binom{k}{j}^{\!2}(1-x)^{k-j}(sx)^j.
\]
Write \(s=1/k+\delta\). Direct binomial expansion at \((x,\delta)=(0,0)\) gives
\[
 H_k(x,s)=1+k^2\delta x-\frac{k^2-1}{4}x^2
 +O_k(\delta x^2+x^3).
\]
Its second \(x\)-derivative near the origin is strictly negative and its first derivative at zero is positive when \(\delta>0\). Thus a unique local positive maximizer satisfies
\[
 x_*(\delta)=\frac{2k^2}{k^2-1}\delta+O_k(\delta^2),\qquad
 H_k(x_*(\delta),s)=1+\frac{k^4}{k^2-1}\delta^2+O_k(\delta^3).
\]
The latter value is strictly greater than one. Compactness in Step 2 ensures all global maximizers lie in this neighborhood.

**4. Suppression above the first collision.** For \(n>km\), the derivative of \(F_{\rm nr}\) with respect to \(y\), at \(x=y=0\) and \(s=1/k\), is
\[
 -k+k^2k^{-n/m}<0.
\]
It remains negative throughout a sufficiently small neighborhood. Therefore every global maximizing triple there has \(y=0\). Step 3 then gives the unique magnitude profile and the claimed nonresonant optimum.

**5. Forced resonant activation and sharp scales.** At \(n=km\), with \(x>0\), the right derivative of the aligned moment with respect to \(c\) at \(c=0\) is \(2ks^k(1-x)^{(k-1)/2}x^{k/2}>0\). Thus no global maximizer with \(x>0\) can have \(c=0\); Step 3 rules out \(x=0\), and compactness rules out \(a=0\) near onset. Phase alignment is forced. The second derivative with respect to \(c\) at \(b=c=0,s=1/k\) is \(-2k(1-k^{1-k})<0\). By the implicit-function theorem, there is a unique local maximizing branch \(c=c(b,s)>0\), and direct differentiation yields
\[
 c(b,s)=\frac{s^k}{1-ks^k}b^k\bigl(1+O_k(b^2)\bigr)
\]
near \(b=0,s=1/k\). Substitution into \(F_{\rm r}\) adds to \(H_k(b^2,s)\) the positive term
\[
 \frac{ks^{2k}}{1-ks^k}b^{2k}+O_k(b^{2k+2}),
\]
uniformly for \(s\) near \(1/k\). Since \(k\ge3\), this begins at order \(x^k\) and leaves the negative quadratic coefficient in Step 3 intact. Differentiating the resulting one-variable objective shows its second derivative is negative for sufficiently small \(x\), so it has one positive maximizer with \(b^2=x_*(\delta)+O_k(\delta^2)\). Inserting the leading \(b\) scale into the displayed \(c\)-branch gives the asserted \(\delta^{k/2}\) coefficient.

Finally, optimizing the added \(x^k\) term shifts the maximizing \(x\) only by \(O_k(\delta^{k-1})\), whose effect on the unperturbed optimum is \(O_k(\delta^{2k-2})=o_k(\delta^k)\) for \(k\ge3\). Evaluating the term at the unperturbed \(x_*(\delta)\) proves the displayed positive constant \(C_k\) and concludes the theorem.

## Verification

The standalone `checker.py` rederives the exact moment by two independent finite convolution calculations using rational arithmetic, checks multinomial collision structure for multiple integer moment orders and both frequency regimes, and checks the exact rational coefficients of the local normal form and resonant gain. The scientific proof is the symbolic/analytic argument above; finite execution does not establish all-integer quantifiers. No external proof assistant or independent auditor was used.

## Relationship to prior work

Weissler's sharp analytic Poisson hypercontractivity establishes the contractivity threshold \(\rho^{2m}=1/k\), but does not classify the optimizing spectral support just beyond it. Bayart, Brevig, Haimi, Ortega-Cerdà and Perfekt (2017) present Weissler's result in the broader Bergman/Hardy context. Brevig, Ortega-Cerdà, Seip and Zhao (2017) study related Hardy contractive inequalities. Carando, Defant, Marceca, Schoolmann and Sevilla-Peris (2024) study the additive structure of general Dirichlet-frequency systems and bounds for translated Hardy norms; their results do not assert the finite three-mode critical amplitude law. The exact undamped sharp eighth moment of \(\{0,1,4\}\) concerns \(\rho=1\) rather than the near-critical dilation problem. The new point is a uniform all-order \(k\ge3\) spectral activation dichotomy with a sharp \(\delta^{k/2}\) amplitude and \(\delta^k\) advantage, not simply hypercontractivity itself.

## Limitations

Only the immediate supercritical neighborhood is classified; its width need not be uniform in all integer parameters. The region \(m<n<km\), arbitrary spectra with more than three modes, and noninteger target moments are not covered. The result is an analytic theorem with computational consistency checks, not an independently validated priority claim. Historical priority of any equivalent unindexed resonance-bifurcation statement remains a residual risk.

## References

- F. B. Weissler, *Logarithmic Sobolev inequalities and hypercontractive estimates on the circle*, Journal of Functional Analysis **37** (1980), 218--234, DOI `10.1016/0022-1236(80)90042-7`.
- F. Bayart, O. F. Brevig, A. Haimi, J. Ortega-Cerdà and K.-M. Perfekt, *Contractive inequalities for Bergman spaces and multiplicative Hankel forms*, arXiv:`1701.06897` (first public version 2017-01-24), https://arxiv.org/abs/1701.06897.
- O. F. Brevig, J. Ortega-Cerdà, K. Seip and J. Zhao, *Contractive inequalities for Hardy spaces*, arXiv:`1706.00738` (2017-06-02), https://arxiv.org/abs/1706.00738.
- D. Carando, A. Defant, F. Marceca, I. Schoolmann and P. Sevilla-Peris, *Hypercontractivity and strips of convergence in Hardy spaces of general Dirichlet series*, arXiv:`2401.09996` (2024-01-18), https://arxiv.org/html/2401.09996v1.
