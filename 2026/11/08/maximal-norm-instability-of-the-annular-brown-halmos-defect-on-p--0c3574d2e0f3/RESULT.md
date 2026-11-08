# Maximal norm-instability of the annular Brown–Halmos defect on positive finite-rank operators

## Finding
For every annulus \(\mathbb A_r=\{z:r<|z|<1\}\), \(0<r<1\), put \(q=r^2\). On its standard Hardy space, let \(M=M_z\) be multiplication by the coordinate and let \(\mathfrak T_r\) be the set of Toeplitz operators with bounded boundary symbols. The quadratic Brown–Halmos defect is
\[
\mathcal L_q(T)=-M^{*2}TM^2+(1+q)M^*TM-qT.
\]
For each integer \(N\ge1\), there is an explicit positive finite-rank contraction \(D_N\), of norm one and rank \(2N-1\), for which
\[
\boxed{\operatorname{dist}(D_N,\mathfrak T_r)=\frac12,\qquad
\|\mathcal L_q(D_N)\|=\frac1N\left(q+\frac{1+q^{N+1}}{1+q^{N-1}}\right).}
\]
In particular \(N\|\mathcal L_q(D_N)\|\to1+q\), while the distance is the **maximum possible** distance of a positive contraction to \(\mathfrak T_r\), since scalar multiples of the identity are Toeplitz. Therefore there is no function \(\omega(t)\to0\) as \(t\downarrow0\) satisfying \(\operatorname{dist}(T,\mathfrak T_r)\le\omega(\|\mathcal L_q(T)\|)\) for all positive norm-one finite-rank operators \(T\). This contrasts with the exact characterization \(\ker\mathcal L_q=\mathfrak T_r\).

## Assumptions and scope
Fix an arbitrary real radius \(0<r<1\) throughout and use \(q=r^2\). The Hilbert norm is the sum of normalized \(L^2\) boundary norms on circles of radii \(1\) and \(r\); thus the functions \(e_j(z)=z^j/(1+q^j)^{1/2}\), \(j\in\mathbb Z\), form an orthonormal basis. A bounded boundary function \(\phi\) gives the Toeplitz compression \(T_\phi=P_{H^2}M_\phi|_{H^2}\). All distances and defects use the operator norm of \(B(H^2(\mathbb A_r))\).

Define \(d_j=\max\{0,1-|j-N|/N\}\) for all \(j\in\mathbb Z\), and \(D_Ne_j=d_je_j\). Then the diagonal values are zero except on \(1\le j\le2N-1\), increase linearly from zero to one at \(j=N\), then decrease to zero. In particular \(D_N\) is finite-rank positive, \(0\le D_N\le I\), \(\|D_N\|=1\), and its rank is \(2N-1\).

## Proof
**Exact defect coefficients.** Put
\[
a_j=\frac{1+q^{j+1}}{1+q^j},\qquad b_j=\frac{1+q^{j+2}}{1+q^j}.
\]
Since \(Me_j=\sqrt{a_j}\,e_{j+1}\), we have \(M^*D_NMe_j=a_jd_{j+1}e_j\) and \(M^{*2}D_NM^2e_j=b_jd_{j+2}e_j\). The exact identity \((1+q)a_j-b_j=q\) follows by clearing denominators. Writing \(\Delta_j=d_{j+1}-d_j\), the defect has diagonal coefficient
\[
\ell_j=(1+q)a_jd_{j+1}-b_jd_{j+2}-qd_j=q\Delta_j-b_j\Delta_{j+1}.
\]
Here \(\Delta_j=N^{-1}\) for \(0\le j<N\), \(\Delta_j=-N^{-1}\) for \(N\le j<2N\), and is zero otherwise. Therefore the nonzero coefficients, with empty ranges omitted, are
\[
\ell_j=\begin{cases}
-q/N,&j=-1\text{ or }j=2N-1,\\
(q-b_j)/N,&0\le j\le N-2,\\
(q+b_{N-1})/N,&j=N-1,\\
(b_j-q)/N,&N\le j\le2N-2.
\end{cases}
\]
The sequence \(b_j\) is strictly increasing, since with \(t=q^j>0\), the function \((1+q^2t)/(1+t)\) decreases strictly in \(t\) and \(q^j\) decreases with \(j\). For every \(j\ge0\), \(q<b_j<1\), and \(b_{-1}=q\). Every coefficient other than the center \(j=N-1\) therefore has modulus at most \(\max\{q,1-q\}/N<1/N\). If \(N\ge2\), then \(b_{N-1}\ge b_1=1-q+q^2\), so \(q+b_{N-1}\ge1+q^2>1\). For \(N=1\), the only other nonzero coefficients have modulus \(q\), smaller than \(q+b_0\). Thus the exact operator norm is attained at the center and is
\[
\|\mathcal L_q(D_N)\|=\frac{q+b_{N-1}}N
=\frac1N\left(q+\frac{1+q^{N+1}}{1+q^{N-1}}\right).
\]
Since \(0<q<1\), \(b_{N-1}\to1\), yielding the announced limit.

**Exact distance to all Toeplitz operators.** For any bounded symbol \(\phi\), let \(\alpha\) and \(\beta\) denote its angular mean on the outer and inner boundary circles, respectively. Directly from boundary compression,
\[
 t_j:=\langle T_\phi e_j,e_j\rangle=\frac{\alpha+q^j\beta}{1+q^j}.
\]
Fix \(\delta=\|D_N-T_\phi\|\). Because \(d_j\to0\) at both ends, and \(t_j\to\alpha\) as \(j\to+\infty\), \(t_j\to\beta\) as \(j\to-\infty\), one has \(|\alpha|\le\delta\) and \(|\beta|\le\delta\). At \(j=N\), the same formula is a convex combination of \(\alpha\) and \(\beta\), so \(|t_N|\le\delta\). But \(d_N=1\) gives \(|1-t_N|\le\delta\); therefore \(1\le |t_N|+|1-t_N|\le2\delta\). This holds for every Toeplitz symbol, hence the distance is at least \(1/2\). Conversely, \(I/2=T_{1/2}\in\mathfrak T_r\) and the spectrum of \(D_N\) is contained in \([0,1]\) with both endpoints present, so \(\|D_N-I/2\|=1/2\). This proves equality and sharpness.

**Failure of uniform norm stability.** If such a modulus \(\omega\) existed, the explicit defect expression would tend to zero as \(N\to\infty\), while the exact distance would remain \(1/2\), a contradiction. No claim is made that \(D_N\) lies far from *compact perturbations* of Toeplitz operators: each \(D_N\) itself is compact.

## Verification
The self-contained `verification.py` uses only exact rational arithmetic. It evaluates the weighted-shift identities and every diagonal coefficient in the finite support for several rational annulus parameters and integers \(N\) from one through thirty; it separately confirms the exact maximum coefficient and the interpolation identities for Toeplitz diagonals. Run it using `python3 verification.py`; successful output ends with `ANNULAR_TOEPLITZ_TENT_EXACT_OK`. These finite checks corroborate computations but are not a proof for all radii and all \(N\); those universal statements follow from the algebraic argument above.

## Relationship to prior work
Jain and Sarkar, *Characterizations of Toeplitz operators on the annulus* (arXiv:2610.40118v1, October 29, 2026), Theorem 2.2, prove the exact nullspace characterization \(\mathcal L_q(T)=0\iff T\in\mathfrak T_r\). Their Sections 3–4 separately characterize compact and compactly perturbed Toeplitz operators. The present finding concerns the operator-norm quantitative conditioning of their defining equation, and measures distance only to exact Toeplitz operators. It neither reproves the characterization nor challenges the compact-perturbation result. Classical Brown–Halmos theory on the unit disk motivates the comparison but does not itself contain the annular radii and this exact defect formula.

## Limitations
The theorem concerns scalar Hardy spaces over a circular annulus, the operator norm, and a specific family of finite-rank positive diagonal contractions. It does not classify all approximate solutions or give a positive stability bound on a restricted class. The factor \(1/2\) is maximal for norm-one positive contractions but would not extend unchanged to arbitrary non-self-adjoint unit-ball operators. The witness is compact, so the result does not show instability of Toeplitz membership modulo compacts. Publication priority beyond the literature specifically compared has not been independently certified; results under other approximate-Toeplitz or nonclosed-range formulations could overlap.

## References
1. Shubham Jain and Jaydeb Sarkar, *Characterizations of Toeplitz operators on the annulus*, arXiv:2610.40118v1 (first public October 29, 2026), especially Theorem 2.2 and Sections 3–4. https://arxiv.org/abs/2610.40118
2. A. Brown and P. R. Halmos, *Algebraic properties of Toeplitz operators*, Journal für die reine und angewandte Mathematik 213 (1963/64), 89–102, as referenced by Jain and Sarkar.
3. D. Sarason, *The \(H^p\) spaces of an annulus*, Memoirs of the American Mathematical Society 56 (1965), as referenced by Jain and Sarkar.
