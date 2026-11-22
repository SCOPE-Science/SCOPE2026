# Universal second-moment isotropy upgrade by spherical-cap averaging

## Finding

Let \(\sigma\) denote normalized area measure on \(S^2\), and let \(\mathcal H_2\) be the five-dimensional complex space of pure degree-two spherical harmonics. Suppose \(\nu\) is any probability measure on \(S^2\) with isotropic second moment
\[
\int_{S^2}uu^{\mathsf T}\,d\nu(u)=\frac13 I_3.
\]
For \(0<c<1\), sample a center \(u\sim\nu\), then independently sample \(x\) uniformly from the spherical cap \(\{x\in S^2:x\cdot u\ge c\}\); let \(\mu_{\nu,c}\) be the resulting law. At the exact threshold
\[
\boxed{c_*=\sqrt{3/7}},
\]
the cap mixture preserves every quadratic-harmonic inner product, for **every** such center law:
\[
\boxed{\int_{S^2}q(x)\overline{r(x)}\,d\mu_{\nu,c_*}(x)
=\int_{S^2}q(x)\overline{r(x)}\,d\sigma(x)\quad(q,r\in\mathcal H_2).}
\]
This is the unique threshold in \((0,1)\) with the stated **universal** property. Neither a zero first moment nor any higher-moment condition on \(\nu\) is required. Individual center distributions with fourth-moment isotropy can preserve these inner products at other thresholds; uniqueness is only across *all* second-moment-isotropic distributions.

## Normalization and scope

The cap law has density \(2\mathbf1_{\{x\cdot u\ge c\}}/(1-c)\) relative to \(\sigma\), so \(\mu_{\nu,c}\) is a probability measure. The target is the Hermitian Gram form of *pure* degree-two harmonics, not all functions of degree at most two or higher-order products. The statement allows arbitrary discrete, singular or continuous probability distributions of centers; cap overlaps are counted according to the mixture, not through a binary indicator of their union. No spatial disjointness is assumed.

## Proof

For any spherical harmonic \(H_\ell\), the Funk--Hecke formula gives the normalized cap average
\[
\int H_\ell(x)\,d\kappa_{u,c}(x)=a_\ell(c)H_\ell(u),\qquad
 a_\ell(c)=\frac{1}{1-c}\int_c^1P_\ell(t)\,dt,
\]
where \(P_\ell\) is the degree-\(\ell\) Legendre polynomial normalized by \(P_\ell(1)=1\). Products \(q\overline r\) with \(q,r\in\mathcal H_2\) decompose orthogonally on \(S^2\) into harmonic degrees \(0,2,4\), and no odd degrees occur. Isotropic second moments of \(\nu\) imply \(\int H_2\,d\nu=0\) for every \(H_2\in\mathcal H_2\). Direct integration of \(P_4(t)=(35t^4-30t^2+3)/8\) gives
\[
 a_4(c)=\frac{c(1+c)(7c^2-3)}8.
\]
Thus at \(c_*\), the cap mixture eliminates both the degree-two and degree-four components of every \(q\overline r\), leaving precisely its constant spherical mean. This proves the claimed equality for arbitrary \(\nu\), complex \(q,r\), and all second-moment-isotropic center laws.

For uniqueness, use the equally weighted four centers at the vertices
\[
 (1,1,1),\ (1,-1,-1),\ (-1,1,-1),\ (-1,-1,1)
\]
divided by \(\sqrt3\). Their second moment is \(I_3/3\). For \(q(x)=x_1^2-x_2^2\), \(q(u)=0\) at all four centers, while \(\int_{S^2}q^2\,d\sigma=4/15\). The degree-two component of \(q^2\) also has center average zero, so its degree-four component has center average \(-4/15\). The cap-mixture \(q\)-norm therefore differs from the sphere norm by \(-4a_4(c)/15\). Since \(a_4(c)\) vanishes in \((0,1)\) exactly at \(\sqrt{3/7}\), no other threshold can satisfy the universal assertion.

## Mathematical significance

A center law that matches only second moments need not match fourth moments; the exact aperture cancels the missing fourth-order information *without constraining the center configuration*. The result supplies a distribution-independent positive continuous-window quadrature identity for the quadratic-harmonic Gram, distinct from tuning a particular symmetric set of caps. It does not assert that the full output measure is a degree-four spherical design: its degree-two and degree-four harmonics disappear, but odd harmonics can remain when the center distribution has nonzero odd moments.

## Relation to prior work

The Funk--Hecke multiplier identity and harmonic product decomposition are classical. Existing explicit spherical-cap concentration calculations for simplex centers already establish the tetrahedral special case \(c=\sqrt{3/7}\), including its complete two-band spectrum; an octahedral six-cap cubature result also finds this aperture in a more symmetric center law. Those tetrahedral eigenvalues, the special-case crossing, and the octahedral cubature are **prior results** and are not claimed anew. The separate statement here is the uniform quantifier over *every* isotropic second-moment center probability law, proved directly through the fourth-harmonic filter. That statement is an elementary but useful extension of the classical convolution machinery; historical priority among general spherical filtering identities remains a residual bibliographic risk.

Relevant sources: the classical Funk--Hecke formula; Simons, Dahlen and Wieczorek, *Spatiospectral concentration on a sphere* (2006, arXiv:math/0408424); *Two-band quadratic Slepian spectrum for simplex-centred cap masks and an isolated tetrahedral isotropy* (2026, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-two-band-quadratic-slepian-spectrum-for-simplex-centred-cap-mask--9f4968253e7d); *A unique fifth-degree spherical cubature radius for six octahedral cap windows* (2026, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-a-unique-fifth-degree-spherical-cubature-radius-for-six-octahedr--d07bf59bb1e6).

## Verification and limits

The proof is analytic and uses only harmonic decomposition, exact Legendre integration, and an explicit four-center witness. Exact symbolic expansion checks the multiplier and the witness's fourth-harmonic average; bounded numerical tests of particular center distributions are illustrative only, not a proof of the universal quantifier. No result is claimed for mixed harmonic bands, arbitrary cap shapes, or higher degrees. The known special tetrahedral concentration spectrum is not included as a newly discovered theorem.
