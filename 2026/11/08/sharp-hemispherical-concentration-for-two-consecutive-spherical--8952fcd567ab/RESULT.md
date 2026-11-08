# Sharp hemispherical concentration for two consecutive spherical-harmonic degrees

## Finding
Let \(\mathcal H_\ell\) be the complex spherical harmonics of **pure** degree \(\ell\) on \(S^2\), and let \(H=\{(x,y,z)\in S^2:z>0\}\). For each integer \(\ell\ge0\), put \(\mathcal B_\ell=\mathcal H_\ell\oplus\mathcal H_{\ell+1}\). Then the following sharp concentration inequality holds for every \(F\in\mathcal B_\ell\):
\[
\int_H|F|^2\,d\sigma\le \Lambda_\ell\int_{S^2}|F|^2\,d\sigma,\qquad
\Lambda_\ell=\frac12+\frac{(2\ell+1)\sqrt{2\ell+3}}{4(\ell+1)}\frac{\binom{2\ell}{\ell}}{4^\ell}.
\]
For \(\ell=0\), nonzero equality holds precisely on the complex line spanned by \(Y_{0,0}+Y_{1,0}\). For \(\ell\ge1\), it holds precisely on the complex two-plane spanned by \(Y_{\ell,\ell}+Y_{\ell+1,\ell}\) and \(Y_{\ell,-\ell}+Y_{\ell+1,-\ell}\), with the standard orthonormal Condon--Shortley convention. For \(\ell\ge1\) the optimizers are highest-azimuthal-order Gaussian-beam pairs, whereas for \(\ell=0\) the optimizer is the constant-plus-zonal-dipole combination.

The complete spectrum of the hemispherical concentration operator on \(\mathcal B_\ell\) is given below. Define for integers \(n\ge0\)
\[
 B_n=\frac{\binom{2n}{n}}{4^n},\quad F_n=B_n\sqrt{2n+1},\qquad G_n=B_n\sqrt{2n}\quad(n\ge1),\quad C_\ell=\frac{\sqrt{(2\ell+1)(2\ell+3)}}{4(\ell+1)}.
\]
For \(0\le m\le\ell\), define the positive numbers
\[
\gamma_{\ell m}=C_\ell\begin{cases}
F_{(\ell+m)/2}F_{(\ell-m)/2},&\ell+m\text{ even},\\
G_{(\ell+m+1)/2}G_{(\ell-m+1)/2},&\ell+m\text{ odd}.
\end{cases}
\]
The spectrum has \(1/2\pm\gamma_{\ell0}\) once each and, for each \(1\le m\le\ell\), \(1/2\pm\gamma_{\ell m}\) twice each, as well as two copies of \(1/2\). The operator therefore has exactly two half-energy eigenvalues, and no zero or unit eigenvalues. Its sharp concentration constants are strictly decreasing with degree:
\[
\Lambda_{\ell+1}-\tfrac12=(\Lambda_\ell-\tfrac12)\sqrt{1-\frac1{(2\ell+4)^2}},
\quad
\Lambda_\ell=\frac12+\frac1{\sqrt{2\pi}}\left(1+\frac1{8\ell}+O(\ell^{-2})\right)\quad(\ell\to\infty).
\]
In particular a two-adjacent-degree packet cannot concentrate asymptotically all of its energy on a hemisphere, even as the degree grows.

## Assumptions and scope
\(d\sigma\) is ordinary area measure on \(S^2\); the fraction is independent of an overall normalization of the area measure. The hemisphere boundary is immaterial. The statement concerns complex scalar spherical harmonics and the contiguous two-degree spectral window \(\{\ell,\ell+1\}\), not the low-pass space through degree \(\ell+1\), nor a more general cap. The standard complex basis \(Y_{j,m}\) is orthonormal in \(L^2(S^2,d\sigma)\). For \(m\ge0\) its colatitudinal factor is the normalized associated Legendre function \(p_{j,m}(t)=\sqrt{\frac{2j+1}{2}\frac{(j-m)!}{(j+m)!}}P_j^m(t)\) with \(t=\cos\theta\), so \(\int_{-1}^{1}|p_{j,m}|^2dt=1\).

## Proof
By azimuthal orthogonality, the concentration matrix splits into independent signed-order blocks. For each \(|m|\le\ell\), the block in the basis \((Y_{\ell,m},Y_{\ell+1,m})\) is
\[
D_{\ell,m}=\begin{pmatrix}1/2&\gamma_{\ell,|m|}\\\gamma_{\ell,|m|}&1/2\end{pmatrix}.
\]
The diagonals equal \(1/2\) because the squared modulus of each pure harmonic is antipodally even. Orders \(m=\pm(\ell+1)\) occur only in degree \(\ell+1\) and give one-dimensional blocks \((1/2)\). The off-diagonal equals \(\int_0^1p_{\ell,m}(t)p_{\ell+1,m}(t)\,dt\) (the negative-order blocks agree by conjugation).

For fixed \(m\ge0\), both associated Legendre factors solve
\[
-\frac{d}{dt}\big((1-t^2)p'(t)\big)+\frac{m^2}{1-t^2}p(t)=j(j+1)p(t).
\]
Integration of the two Lagrange identities on \([0,1]\), and the vanishing of \(1-t^2\) at \(t=1\), give
\[
2(\ell+1)\int_0^1p_{\ell,m}p_{\ell+1,m}\,dt=
\big[p_{\ell,m}p'_{\ell+1,m}-p'_{\ell,m}p_{\ell+1,m}\big]_{t=0}.
\]
Associated Legendre parity makes exactly one product in the bracket vanish. The identities \(P_j^m(0)=0\) for odd \(j+m\), \(|P_j^m(0)|=(j+m-1)!!/(j-m)!!\) for even \(j+m\), together with the derivative recurrence at zero, reduce the bracket to the displayed binomial products. In detail, put \(B_n=\binom{2n}{n}/4^n\) and \(C_\ell=\sqrt{(2\ell+1)(2\ell+3)}/[4(\ell+1)]\). If \(\ell+m=2r\) and \(\ell-m=2s\), the normalized overlap equals \(C_\ell B_rB_s\sqrt{(2r+1)(2s+1)}\). If \(\ell+m+1=2r\) and \(\ell-m+1=2s\), it equals \(C_\ell B_rB_s\sqrt{(2r)(2s)}\). Both are strictly positive, proving the spectral formulas and eigenspaces.

It remains to determine the **largest** off-diagonal among all orders, not merely the block spectra. Define \(F_n=B_n\sqrt{2n+1}\) for \(n\ge0\). Its consecutive ratios satisfy
\[
\frac{F_{n+1}}{F_n}=\sqrt{1-\frac1{(2n+2)^2}}.
\]
These ratios increase strictly, and \(F_0=1\), so log-convexity implies \(F_rF_s\le F_{r+s}\), with strict inequality when both \(r,s>0\). Thus all the even-parity order overlaps are at most \(C_\ell F_\ell\), attaining that value only at \(m=\ell\).

For the opposite parity, the elementary Wallis bound \(B_n<1/\sqrt{\pi n}\) gives \(G_n=B_n\sqrt{2n}<\sqrt{2/\pi}\) for all \(n\ge1\). The ratio formula and Wallis asymptotic show \(F_\ell>\sqrt{2/\pi}\) for every finite \(\ell\), and \(2/\pi<\sqrt{2/\pi}\). Consequently every odd-parity product satisfies \(G_rG_s<2/\pi<F_\ell\). Hence \(\gamma_{\ell m}<\gamma_{\ell\ell}\) whenever \(m<\ell\), establishing the sharp constant and all equality conditions (including the one-dimensional \(\ell=0\) case).

Finally \(\gamma_{\ell\ell}=C_\ell F_\ell\), which is the stated binomial expression. Direct cancellation of consecutive central binomial coefficients yields \(\gamma_{\ell+1,\ell+1}/\gamma_{\ell\ell}=\sqrt{1-(2\ell+4)^{-2}}\). Stirling's expansion \(B_\ell=(\pi\ell)^{-1/2}(1-1/(8\ell)+O(\ell^{-2}))\) gives the asymptotic in the finding.

## Verification
The independent finite checker `check_slepian.py` compares the derived closed overlap formulas against associated-Legendre quadrature in all \(496\) order blocks through degree \(30\), checks strict top-order maximality, the entire spectrum's multiplicity and trace, and three larger-degree asymptotic cases. It reports `ADJACENT_HEMISPHERE_SLEPIAN_PASS checked_pairs=499 max_quadrature_error=1.93e-14 asymptotic_cases=3`. These checks corroborate the formulas but are not a proof of the all-degree result; the latter is the exact Legendre/Wallis argument above. Run with `python check_slepian.py` (Python 3, NumPy, SciPy).

## Relationship to prior work
Spherical Slepian theory establishes the cap concentration matrix, its azimuthal block decomposition, and numerical eigenvalue methods (Simons, Dahlen and Wieczorek; Simons and Dahlen). The present result applies that operator to a **two-consecutive-degree band** and determines every eigenvalue in elementary factorial form, the sharp global optimizer across all azimuthal orders, and the non-unit high-frequency limit. The referenced literature does not state these exact conclusions. Jaming and Speckbacher's 2020 concentration bounds concern low-pass finite spherical-harmonic expansions on general homogeneous spaces and do not imply these sharp values for an adjacent-degree shell. A published parity/Cauchy decomposition for arbitrary degree masks determines which eigenvalues equal \(1/2\), but expressly leaves their positive spectral gaps unspecified; it therefore does not give the present sharp constant or rigidity. Direct searches found no equivalent closed highest-order-maximizer theorem, but absence from searches does not prove global historical novelty.

## Limitations
The result is confined to scalar harmonics on \(S^2\), one hemisphere, and precisely two adjacent pure degrees. It does not give optimal concentration for other angular caps, nonadjacent bands or bands of width three or more. The full spectrum is algebraically exact, but independent peer review and priority confirmation have not been performed. General spherical Slepian matrix formulas make this case computationally accessible, so an unlocated specialized derivation remains a historical-priority risk.

## References
1. P. Jaming and M. Speckbacher, *Concentration estimates for finite expansions of spherical harmonics on two-point homogeneous spaces via the large sieve principle*, arXiv:2004.02474, first public 6 April 2020; especially Theorem 4.4.
2. F. J. Simons, F. A. Dahlen and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424 (first public 31 August 2004); SIAM Review 48 (2006), 504–536.
3. F. J. Simons and F. A. Dahlen, *Spherical Slepian functions and the polar gap in geodesy*, Geophysical Journal International 166 (2006), 1039–1061; especially equation (50) and Section 4.
4. P. J. Roddy and J. D. McEwen, *Slepian Scale-Discretised Wavelets on the Sphere*, arXiv:2106.02023 (first public 3 June 2021), IEEE Transactions on Signal Processing 70 (2022), 6142–6153.
5. *Exact half-energy multiplicities for hemispherical spherical Slepian concentration with arbitrary degree masks*, publicly available mathematical research record, 2026, research-record identifier `0284b88cef7a`.
