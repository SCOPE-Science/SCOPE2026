# The sharp tangential Hilbert–Schmidt boundary and angular energy law for affine Bergman composition differences

## Finding
On the normalized weighted analytic Bergman space \(A^2_\alpha(\mathbb D)\), fix \(\alpha>-1\), \(0<c<1\), \(2<\gamma<3\), \(\beta\ge0\), and \(0<|\varepsilon|\le(1-c)/32\). Define
\[
\begin{aligned}
\varphi(z)&=1-c(1-z),\\
\psi(z)&=\varphi(z)+\varepsilon[c(1-z)]^\gamma,\\
(Df)(z)&=z(1-z)^\beta\bigl(f(\psi(z))-f(\varphi(z))\bigr).
\end{aligned}
\]
All powers use the holomorphic right-half-plane branch. Set \(s=\beta+\gamma\), \(\kappa=1-c\) and
\[
\mathscr A=\frac{2|\varepsilon|^2c^{2\gamma-\alpha-4}}{\pi\kappa^3}.
\]
Writing \(k_w(\zeta)=(1-\overline w\zeta)^{-\alpha-2}\), define the *truncated squared Hilbert–Schmidt energy*
\[
E(r)=\int_{\mathbb D\cap\{|1-z|>r\}}
|z|^2|1-z|^{2\beta}\|k_{\psi(z)}-k_{\varphi(z)}\|^2\,dA_\alpha(z),\quad 0<r<2.
\]
Then the boundary energy density has the exact asymptotic
\[
\boxed{-E'(r)\sim\mathscr A\,r^{2s-6}\quad(r\downarrow0).}
\]
Consequently the operator has the complete, sharp Hilbert–Schmidt boundary
\[
\boxed{D\in\mathcal S_2\quad\Longleftrightarrow\quad\beta+\gamma>\tfrac52.}
\]
For \(s<5/2\), \(E(r)\sim\mathscr A r^{2s-5}/(5-2s)\); for \(s=5/2\), \(E(r)\sim\mathscr A\log(1/r)\); and for \(s>5/2\), \(E(r)\to\|D\|_{\mathcal S_2}^2\). If \(2<\gamma<5/2\) is held fixed, the squared norm has the sharp critical pole
\[
\boxed{\lim_{\beta\downarrow 5/2-\gamma}(\beta+\gamma-\tfrac52)\|D\|_{\mathcal S_2}^2
=\frac{|\varepsilon|^2c^{2\gamma-\alpha-4}}{\pi\kappa^3}.}
\]
There is also a precise angular concentration law: condition the local Hilbert–Schmidt energy on a shrinking circle \(|1-z|=r\), and set \(v=(1-|z|^2)/r^2\). Its normalized distribution tends weakly to
\[
\boxed{\frac{\kappa^3}{B(\alpha+1,3)}\,
\frac{v^\alpha}{(v+\kappa)^{\alpha+4}}\,dv,\qquad v>0.}
\]
Both boundary arcs carry one half of the limiting energy. Here \(B\) is Euler's beta function.

## Assumptions and scope
The unit disk \(\mathbb D\) is given normalized measure \(dA_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha\,dx\,dy/\pi\). The functions \((1-z)^\beta\) and \([c(1-z)]^\gamma\) are single-valued on \(\mathbb D\) because \(\operatorname{Re}(1-z)>0\). Complex \(\varepsilon\ne0\) is allowed. The defining energy integral can take value \(+\infty\) away from the Hilbert–Schmidt range, while each individual kernel norm is finite; the derivative of \(E\) is meant for every fixed \(r>0\). The parameters \(c,\alpha,\gamma,\varepsilon\) are fixed in the critical-pole limit. The regime \(\gamma=2\), where the perturbation is no longer small relative to the tangential boundary gap, is excluded.

## Proof
**1. Symbol and kernel preparation.** Put \(w=1-z\), \(r=|w|\), \(\rho=1-|z|^2\) and \(\kappa=1-c\). Direct expansion yields the exact identity
\[
1-|\varphi(z)|^2=c\rho+c\kappa r^2.
\]
Since \(r<2\), \(c<1\) and \(\gamma>2\), the perturbation \(\delta(z)=\varepsilon(cw)^\gamma\) satisfies \(|\delta|\le2|\varepsilon|c^2r^2\). Hence
\[
1-|\psi|^2\ge 1-|\varphi|^2-2|\delta|-|\delta|^2
\ge c\rho+\bigl(c\kappa-4|\varepsilon|c^2-16|\varepsilon|^2c^4\bigr)r^2>0.
\]
The last coefficient is positive under the stated bound on \(\varepsilon\). Thus both maps are disk self-maps and both composition operators are bounded; multiplication by the bounded holomorphic function \(z(1-z)^\beta\) is bounded. Summing squared images of an arbitrary orthonormal basis under \(D\) gives the exact kernel-energy representation
\[
\sum_{n\ge0}\|De_n\|^2=\int_{\mathbb D}|z|^2|w|^{2\beta}
\|k_{\psi(z)}-k_{\varphi(z)}\|^2\,dA_\alpha(z).
\]
**2. Uniform kernel expansion.** Let \(p=\alpha+2\), and \(R=1-|\varphi(z)|^2\). The evaluation kernel is \(k_a(\zeta)=(1-\overline a\zeta)^{-p}\), and its parameter derivative satisfies the exact identity
\[
\|\partial_{\overline a}k_a\|^2
=p(1-|a|^2)^{-p-1}+p(p+1)|a|^2(1-|a|^2)^{-p-2}.
\]
Moreover, \(|\delta|/R\le C r^{\gamma-2}\to0\) uniformly across the shrinking disk cap, since \(R\ge c\kappa r^2\). The Hilbert-space Taylor expansion and standard differentiated-kernel bounds, applied along the segment joining \(\varphi\) to \(\psi\), give a *uniform relative* remainder \(O(r^{\gamma-2})\). Since \(\varphi(z)\to1\),
\[
\|k_{\psi(z)}-k_{\varphi(z)}\|^2
=p(p+1)|\varepsilon|^2c^{2\gamma-\alpha-4}
\frac{r^{2\gamma}}{(\rho+\kappa r^2)^{\alpha+4}}\bigl(1+o(1)\bigr)
\]
uniformly for all \(z\in\mathbb D\) with \(|1-z|=r\) as \(r\downarrow0\). This includes the highly tangential approaches where \(\rho\ll r\).

**3. Exact angular change of variables.** For \(w=re^{i\theta}\), the disk cap is \(\cos\theta>r/2\), and \(\rho=2r\cos\theta-r^2\). Put \(v=\rho/r^2\), so \(\cos\theta=r(v+1)/2\), and \(0<v<2/r-1\). Adding the two conjugate arcs produces the exact Jacobian
\[
\sum_{\text{two arcs}}|d\theta|=
\frac{r\,dv}{\sqrt{1-r^2(v+1)^2/4}}.
\]
After inserting the asymptotic kernel norm and \(dA_\alpha=(\alpha+1)\rho^\alpha r\,dr\,d\theta/\pi\), we obtain
\[
-E'(r)=\frac{(\alpha+1)p(p+1)|\varepsilon|^2c^{2\gamma-\alpha-4}}\pi
r^{2s-6}\left(\int_0^{2/r-1}
\frac{v^\alpha(1-r^2v)}{(v+\kappa)^{\alpha+4}\sqrt{1-r^2(v+1)^2/4}}\,dv\right)(1+o(1)).
\]
The \(o(1)\) is uniform. The integral converges as \(r\downarrow0\) to
\[
\int_0^\infty\frac{v^\alpha}{(v+\kappa)^{\alpha+4}}\,dv
=\kappa^{-3}B(\alpha+1,3)
=\frac2{(\alpha+1)(\alpha+2)(\alpha+3)\kappa^3}.
\]
For rigor, convergence holds by dominated convergence on fixed \(0<v<M\), the integrable \(O(v^{-4})\) bound for the range \(M<v<1/r\), and a total \(O(r^3)\) bound for the upper endpoint \(1/r<v<2/r-1\), including its square-root Jacobian singularity. Inserting this beta integral cancels every \(\alpha\)-dependent prefactor and yields \(\mathscr A\). This proves the local density and, by normalizing the integrand, the weak beta-prime distribution; each symmetric arc contributes one half.

**4. Integrating and the pole.** Away from \(z=1\) the kernel integral is finite; thus all divergences come from \(\int_r^{r_0}t^{2s-6}dt\). Its integral gives the stated power and logarithm, and convergence exactly when \(2s-6>-1\), namely \(s>5/2\). In a compact interval of \(\beta\) around \(5/2-\gamma\), the radial asymptotic has a common integrable relative-error bound \(O(r^{\eta})\) for some \(\eta>0\), following the uniform kernel expansion and the angular integral estimates. Writing \(u=s-5/2>0\), the leading local integral equals \(\mathscr A r_0^{2u}/(2u)\), while all remainders contribute \(O(1)\) uniformly as \(u\downarrow0\). Multiplying by \(u\) proves the displayed pole. No finite quadrature is used to infer an infinite-dimensional assertion.

## Verification
A standalone finite checker, `verification/check.py`, verifies the exact quadratic boundary-gap identity and beta identities symbolically, and tests the dimensionless local-density quotient by independently evaluating the exact Bergman kernel difference at four parameter tuples and two shrinking radii each. It completes 13 finite assertions. These calculations corroborate constants but do not certify the all-parameter analytic proof. All formulas above are stated under their explicit parameter and branch conditions.

## Relationship to prior work
Lo and Loh (2020, Example 3.5) exhibited a closely related Hardy-space boundary-contact difference and a sufficient Hilbert–Schmidt regime \(\gamma>5/2\); the threshold value was therefore **not** introduced here. Lo and Loh (2022, Example 3.8) studied the same affine/fractional-contact pair with the multiplier \(z\) on weighted Bergman spaces, obtaining a restricted sufficient interval rather than the sharp all-parameter necessity, critical residue or tangent-angle law above. Choe, Hosokawa and Koo (2010/2011, Theorem 3.6) established a general weighted Bergman Hilbert–Schmidt integral criterion; their criterion provides foundational coverage but does not evaluate the singular tangential integral and exact leading constants here. The new contribution is the explicit uniform local asymptotic, full \(\beta+\gamma\) phase boundary, exact pole and universal angular energy distribution for this natural contact family.

## Limitations
The result is about the Hilbert–Schmidt class, not the full Schatten scale or compactness of every non-Hilbert–Schmidt case. It requires \(2<\gamma<3\), \(\beta\ge0\) and the indicated small nonzero perturbation. The beta-prime law measures *local squared kernel energy*, not a probability distribution of operator singular vectors. This same-model analytical review is not independent external validation. Although the inspected literature provides no exact covering theorem for the present combined asymptotic, historical-priority uncertainty remains, particularly for specialized contact asymptotics derived from general integral criteria.

## References
- C.-O. Lo and A. W.-K. Loh, *Hilbert-Schmidtness of weighted composition operators and their differences on Hardy spaces*, Opuscula Math. 40 (2020), 495–507. First public online 9 July 2020. https://doi.org/10.7494/OpMath.2020.40.4.495
- C.-O. Lo and A. W.-K. Loh, *Compact and Hilbert–Schmidt weighted composition operators on weighted Bergman spaces*, J. Aust. Math. Soc. 113 (2022), 208–225. First public online 22 March 2022. https://doi.org/10.1017/S1446788722000039
- B. R. Choe, T. Hosokawa and H. Koo, *Hilbert–Schmidt differences of composition operators on the Bergman space*, Math. Z. 269 (2011), 751–775. First public online 3 August 2010. https://doi.org/10.1007/s00209-010-0757-7
- S. Acharyya and Z. Wu, *Compact and Hilbert–Schmidt differences of weighted composition operators*, 2017, accessible manuscript: https://www.academia.edu/107395310/Compact_and_Hilbert_Schmidt_Differences_of_Weighted_Composition_Operators
