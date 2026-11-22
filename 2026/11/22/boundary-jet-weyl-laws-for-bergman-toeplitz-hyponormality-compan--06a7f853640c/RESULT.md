# Boundary-jet Weyl laws for Bergman Toeplitz hyponormality companions

## Finding

The compact correction to the selfadjoint Jacobi matrix governing hyponormality of a Bergman Toeplitz operator with an analytic shift and a smooth radial term has a sharp singular-value law controlled by the first nonvanishing boundary-jet coefficient. For a nonzero coefficient at order \(r\geq1\), the singular values have asymptotic \(s_N(K_g)\sim |c_r|B_r^rN^{-r}\), where
\[
B_r=\frac1{2\pi}\int_0^{2\pi}|2\cos\theta|^{1/r}\,d\theta
=\frac{2^{1/r}\Gamma((r+1)/(2r))}{\sqrt\pi\,\Gamma(1+1/(2r))}.
\]
Thus \(K_g\) belongs to the Schatten ideal \(\mathcal S_p\) exactly when \(p>1/r\). In particular, for the radial power symbol \(g(t)=t^{s/2}\), every \(s>0\) other than \(s=1/2\) gives
\[
s_N(K_g)\sim\frac{2s|s-1/2|}{\pi N},\qquad K_g\in\mathcal S_p\iff p>1.
\]
At the unique exceptional exponent \(s=1/2\), the leading term cancels and
\[
s_N(K_g)\sim \frac7{32}\frac{\Gamma(3/4)^2}{\pi\Gamma(5/4)^2}\,N^{-2},\qquad K_g\in\mathcal S_p\iff p>1/2.
\]
Every prescribed integer decay order \(r\ge1\) is attained by a polynomial radial symbol.

## Assumptions and scope

Use normalized area measure on the unit disk and its analytic Bergman Hilbert space \(A^2(\mathbb D)\). The monomials \(e_n=\sqrt{n+1}\,z^n\), \(n\ge0\), are orthonormal. Let \(M=T_z\), with \(T_\phi\) denoting Bergman Toeplitz compression. For a real-valued bounded absolutely continuous \(g:[0,1]\to\mathbb R\) whose derivative belongs to \(L^1(0,1)\), let \(D_g=T_{g(|z|^2)}\). Put \(\Delta=M^*M-MM^*\); it is strictly positive but has an unbounded inverse. On the finite monomial span define the symmetric normalized companion
\[
J_g=-\Delta^{-1/2}[M,D_g]\Delta^{-1/2}-\big(\Delta^{-1/2}[M,D_g]\Delta^{-1/2}\big)^*.
\]
The off-diagonal coefficients converge to \(g'(1)\) when \(g\) is continuously differentiable near \(1\), so this matrix closes to a bounded selfadjoint operator. Let \(S\) be the unilateral shift on \(\ell^2(\mathbb N_0)\) and set \(K_g=J_g-g'(1)(S+S^*)\).

For a fixed integer \(r\ge1\), assume additionally that \(g\) has \(r+2\) continuous derivatives on some neighborhood of \(1\). Set
\[
F_g(z)=\frac{1}{\sqrt{(1+z)(1+2z)}}\sum_{m=0}^{r}\frac{(-1)^m(m+1)g^{(m+1)}(1)z^m}{\prod_{j=3}^{m+2}(1+jz)}
\]
(where an empty product is \(1\)), and write \(c_k(g)=[z^k]F_g(z)\). The hypotheses of the spectral law are \(c_1=\cdots=c_{r-1}=0\) and \(c_r\neq0\), without assumptions about a possible isolated finite-dimensional spectrum of \(J_g\). The Schatten classification includes \(p\in(0,1)\) using the usual quasi-ideals. No claim is made about operators with all these jets zero or about a different radial measure.

## Proof

**1. Exact Jacobi entries.** Put \(\ell=n+1\) and
\[
d_n=(n+1)\int_0^1t^ng(t)\,dt,\qquad
\Delta e_n=\frac{e_n}{(n+1)(n+2)}.
\]
Direct computation of the commutator gives
\[
(J_g)_{n+1,n}=j_n=\ell\sqrt{(\ell+1)(\ell+2)}(d_{n+1}-d_n).
\]
Integration by parts, with the endpoint factor \(t^\ell(1-t)\) vanishing at both ends, yields
\[
d_{n+1}-d_n=\int_0^1t^\ell(1-t)g'(t)\,dt.
\]
For \(X_\ell\sim\operatorname{Beta}(\ell+1,2)\), it follows exactly that
\[
j_n=\frac{\ell}{\sqrt{(\ell+1)(\ell+2)}}\,\mathbb E[g'(X_\ell)].
\]
This identity also verifies that the normalized companion extends boundedly.

**2. Boundary jets.** The beta moments are
\[
\mathbb E[(1-X_\ell)^m]=\frac{(m+1)!}{\prod_{j=3}^{m+2}(\ell+j)}.
\]
Taylor-expand \(g'\) at \(1\), through order \(r\). The contribution from \([0,1-\epsilon]\) decays exponentially in \(\ell\) because \(g'\in L^1\). Uniform Taylor remainder near the endpoint gives
\[
j_n=\sum_{k=0}^rc_k(g)\ell^{-k}+O(\ell^{-r-1}).
\]
Since \(c_0=g'(1)\), if the first surviving coefficient occurs at \(r\) then
\[
(K_g)_{n,n+1}=c_r(n+1)^{-r}+O((n+1)^{-r-1}).
\]
In particular \(c_1=-\tfrac32g'(1)-2g''(1)\) and \(c_2=\tfrac{19}{8}g'(1)+9g''(1)+3g'''(1)\).

**3. Singular-value counting for a compact Jacobi tail.** We prove the required one-dimensional Weyl lemma. Let \(K\) be a real symmetric Jacobi matrix with off-diagonal \(b_n=cn^{-r}+o(n^{-r})\), where \(r>0\), \(c\ne0\). For a threshold \(u\downarrow0\), set \(L=u^{-1/r}\). Fix \(0<\epsilon<R\). Removing the first \(\lfloor\epsilon L\rfloor\) coordinates changes the singular-value counting function by at most \(O(\epsilon L)\), by the finite-rank interlacing bound. The norm of the tail past \(\lfloor RL\rfloor\) is at most \((2|c|+o(1))R^{-r}u\); choose \(R\) large enough to make this strictly smaller than \(u\). On the middle segment divide into blocks of length \(\lfloor\delta L\rfloor\); deleting cross-block bonds has rank \(O(R/\delta)\), negligible compared with \(L\). The coefficients on a block differ in norm by \(o(u)+O(\delta\epsilon^{-r-1}u)\) from the constant coefficient \(c(xL)^{-r}\) at its left endpoint. An \(h\)-site constant Jacobi block has eigenvalues \(2c(xL)^{-r}\cos(\pi j/(h+1))\) for \(j=1,\ldots,h\). Min–max singular-value inequalities, first with threshold margins \(1\pm\eta\) and then with \(\delta\downarrow0\), yield a Riemann-integral limit for the middle segment. Finally \(\epsilon\downarrow0\), \(R\uparrow\infty\), and \(\eta\downarrow0\) give
\[
\lim_{u\downarrow0}u^{1/r}\#\{k:s_k(K)>u\}
=\frac1{2\pi}\int_0^{2\pi}\int_0^\infty
\mathbf1_{\{|2c\cos\theta|x^{-r}>1\}}\,dx\,d\theta
=|c|^{1/r}B_r.
\]
Inversion of this monotone counting asymptotic yields \(s_N(K)\sim |c|B_r^rN^{-r}\). Applying it to the coefficients in step 2 proves the main statement. This is an infinite-dimensional argument; finite truncations are not used to infer the limit.

**4. Power symbols and the exceptional cancellation.** For \(g(t)=t^a\), \(a=s/2>0\), exact integration gives
\[
d_n=\frac{n+1}{n+1+a},\qquad
j_n=\frac{a\ell\sqrt{(\ell+1)(\ell+2)}}{(\ell+a)(\ell+1+a)}.
\]
Therefore \(c_1=a(\tfrac12-2a)\), which vanishes for positive \(a\) precisely at \(a=1/4\). At that value the next coefficient is \(c_2=-7/64\ne0\). The identities \(B_1=4/\pi\) and \(B_2^2=2\Gamma(3/4)^2/(\pi\Gamma(5/4)^2)\) give the two displayed constants. Finally, the coefficient \(c_r\) depends on \(g^{(r+1)}(1)\) with nonzero multiplier \((-1)^r(r+1)\), whereas the lower coefficients do not. Choosing the Taylor coefficients successively produces a polynomial \(g\) with any desired first surviving order.

## Verification

The accompanying `check_jacobi_jet.py` performs exact symbolic series checks, verifies the beta and power-moment identities on rational test cases, and checks finite Jacobi matrices numerically. Execute `python check_jacobi_jet.py` with Python, SymPy, and NumPy. The checker supports but does not replace the analytic singular-value counting proof. The gamma-factor normalization and exceptional coefficient are derived explicitly in the proof.

## Relationship to prior work

Brian Simanek, *Hyponormal Toeplitz Operators on Weighted Bergman Space* (arXiv:2001.07823v1, 22 January 2020), already reduces radial-power Toeplitz hyponormality to a Jacobi norm problem and computes its essential spectral interval. Trieu Le and Brian Simanek, *Hyponormal Toeplitz Operators on Weighted Bergman Spaces* (arXiv:2003.07330v1, 16 March 2020), obtain the general shift-plus-diagonal framework and a compact Jacobi correction for regular radial symbols. Neither inspected work states the present full singular-value coefficient, the order-by-order boundary-jet classification, or the unique trace-class resonance for power symbols.

R. V. Kozhan, *Asymptotics of the Eigenvalues of Two-Diagonal Jacobi Matrices* (Mathematical Notes 77, 2005, 283–287), studies a different rapidly varying regime (its stated theorem assumes the ratio of consecutive weights tends to zero); here the Jacobi weights are regularly varying with consecutive ratio tending to one. The block-counting lemma is proved here rather than assigned novelty to a general method. These comparisons establish a specific gap, not exhaustive historical priority.

## Limitations

The classification pertains to a normalized Jacobi *companion* and its compact remainder, not to the Toeplitz operator's own singular values or to a classification of Toeplitz hyponormality. Regularity is imposed near the circle and an integrable radial derivative elsewhere. The claim treats nonzero finite-order endpoint jets; symbols flat to every order require separate analysis. It is not an independent mathematical audit, and older unindexed treatments of regularly varying compact Jacobi matrices could overlap parts of the general spectral lemma.

## References

1. B. Simanek, *Hyponormal Toeplitz Operators on Weighted Bergman Space*, arXiv:2001.07823v1 (2020), https://arxiv.org/abs/2001.07823.
2. T. Le and B. Simanek, *Hyponormal Toeplitz Operators on Weighted Bergman Spaces*, arXiv:2003.07330v1 (2020), https://arxiv.org/abs/2003.07330.
3. R. V. Kozhan, *Asymptotics of the Eigenvalues of Two-Diagonal Jacobi Matrices*, Mathematical Notes 77 (2005), 283–287, https://www.mathnet.ru/eng/mzm2492.
