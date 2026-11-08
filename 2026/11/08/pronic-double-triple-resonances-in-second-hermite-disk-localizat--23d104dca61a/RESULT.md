# Pronic double triple resonances in second-Hermite disk localization

## Finding

For a centered disk of phase-space area \(R>0\), let \(T_R\) denote short-time Fourier localization with the normalized **second Hermite** window. Its eigenvalues \(\lambda_n(R)\), indexed by normalized Hermite signals \(h_n\), obey the exact adjacent-gap identity
\[
\lambda_n(R)-\lambda_{n+1}(R)
 =\frac{e^{-R}R^{n-1}}{2(n+1)!}
  P_n(R)P_{n+1}(R),\qquad
 P_n(R)=R^2-2nR+n(n-1).
\]
Every equality between consecutive indexed eigenvalues is part of the triple \(\lambda_{m-1}=\lambda_m=\lambda_{m+1}\), occurring at the positive radii \(R=m\pm\sqrt m\) with integer \(m\ge1\). The lower root is positive precisely when \(m\ge2\); for \(m=1\) only \(R=2\) is admitted.

At a fixed positive area there are either zero, one or two such **triple centers**. The two-center case occurs **exactly** at the pronic areas
\[
R=k(k+1),\qquad k=1,2,3,\ldots,
\]
where the two disjoint consecutive triple plateaus are
\[
\{h_{k^2-1},h_{k^2},h_{k^2+1}\},
\qquad
\{h_{(k+1)^2-1},h_{(k+1)^2},h_{(k+1)^2+1}\}.
\]
No four *consecutively indexed* modes share an eigenvalue. The triple crossings are transverse: at any positive root \(R_*\) of \(P_m\),
\[
\lambda_m'(R_*)=0,\qquad
\lambda_{m-1}'(R_*)>0,\qquad
\lambda_{m+1}'(R_*)=\frac{m}{m+1}\lambda_{m-1}'(R_*)>0.
\]
Thus, as \(R\) increases through \(R_*\), the central mode changes locally from being more concentrated than each neighbor to being less concentrated than each neighbor. At \(R=2\) the two plateau centers are \(m=1\) and \(m=4\); at \(R=6\) they are \(m=4\) and \(m=9\).

## Assumptions and scope

Write \(h_0(t)=2^{1/4}e^{-\pi t^2}\), and let \(\{h_n:n\ge0\}\) be the corresponding unit-norm Hermite basis of \(L^2(\mathbb R)\). Use the short-time Fourier transform
\[
V_gf(x,\xi)=\int_{\mathbb R}f(t)\overline{g(t-x)}e^{-2\pi i\xi t}\,dt
\]
and the disk \(D_R=\{(x,\xi)\in\mathbb R^2:\pi(x^2+\xi^2)\le R\}\), whose Euclidean area is \(R\). Define \(T_R=V_{h_2}^{*}\mathbf1_{D_R}V_{h_2}\). The parameter \(R\) is a **positive real number**, and indices \(m,n,k\) are integers with the ranges stated above. All equalities are equalities of indexed eigenvalues, not claims about their position in nonincreasing spectral order.

## Proof

**Radial diagonalization.** Rotational covariance of the Hermite short-time Fourier transform makes \(T_R\) diagonal in \(\{h_n\}\), as in Abreu–Gröchenig–Romero, Proposition 4.1 and Lemma 4.2. Their normalized complex-Hermite formula, specialized to the order-two window, gives for every integer \(n\ge0\)
\[
\lambda_n(R)=\frac1{2n!}\int_0^R
  e^{-t}t^{n-2}P_n(t)^2\,dt,\qquad
P_n(t)=t^2-2nt+n(n-1).
\tag{1}
\]
For \(n=0,1\), the apparent negative powers cancel, leaving the continuous densities \(e^{-t}t^2/2\) and \(e^{-t}t(t-2)^2/2\), respectively. For \(n\ge2\), equation (1) follows from \(L_2^{n-2}(t)=P_n(t)/2\) and the generalized Laguerre normalization. Thus no singular integration at zero is involved.

**Exact difference.** The elementary polynomial identity
\[
(n+1)P_n^2-tP_{n+1}^2
=(n-1-t)P_nP_{n+1}
+t\bigl(P_n'P_{n+1}+P_nP_{n+1}'\bigr)
\tag{2}
\]
holds identically in \(n,t\). Differentiating
\[
Q_n(R)=\frac{e^{-R}R^{n-1}}{2(n+1)!}P_n(R)P_{n+1}(R)
\]
and applying (2) gives \(Q_n'(R)=\lambda_n'(R)-\lambda_{n+1}'(R)\) for every \(R>0\), including \(n=0\). Both sides of the proposed identity tend to zero as \(R\downarrow0\), because \(P_0(R)=R^2\), \(P_1(R)=R(R-2)\), and for higher indices the factor \(R^{n-1}\) vanishes. Integration establishes the displayed adjacent-gap identity for all indices and all positive areas.

**All crossing areas.** Every prefactor in the difference identity is nonzero for \(R>0\). Consequently \(\lambda_n=\lambda_{n+1}\) if and only if \(P_n(R)P_{n+1}(R)=0\). Since \(P_0(R)=R^2>0\), every adjacent equality arises from a root of some \(P_m\) with \(m\ge1\). That root simultaneously sets to zero the differences at indices \(m-1\) and \(m\), forcing the consecutive triple. The positive roots of \(P_m\) are exactly \(m\pm\sqrt m\), with the noted exception that \(m-\sqrt m=0\) when \(m=1\).

**Classification of simultaneous centers.** For fixed \(R\), regard \(P_m(R)\) as a polynomial in the integer \(m\):
\[
P_m(R)=m^2-(2R+1)m+R^2.
\tag{3}
\]
It has at most two distinct integer roots. If it has two, say \(u<v\), Vieta's relations give \(u+v=2R+1\) and \(uv=R^2\). Hence \(2R\) and \(R^2\) are integers. The first says \(R\) is integral or half-integral; the second excludes the nonintegral half-integer case. Thus \(R\) is a positive integer. The discriminant of (3) equals \(4R+1=(v-u)^2\), an odd square, so for some integer \(k\ge1\), \(R=k(k+1)\). Substitution into (3) yields \(u=k^2\), \(v=(k+1)^2\). Conversely, those two integers are roots when \(R=k(k+1)\). Their separation \(2k+1\ge3\) makes the corresponding three-index plateaus disjoint and rules out a run of four consecutive equal eigenvalues. With one root there is precisely one consecutive triple, and with no root no adjacent pair is equal.

**Transverse three-way crossing.** At a root \(R_*\) of \(P_m\), equation (1) gives \(\lambda_m'(R_*)=0\). Neither \(P_{m-1}\) nor \(P_{m+1}\) vanishes there (the preceding root classification forbids two centers a distance one apart), so their derivatives in (1) are strictly positive. The relations \(P_{m-1}(R_*)=2(R_*-m+1)\), \(P_{m+1}(R_*)=2(m-R_*)\), and \((R_*-m)^2=m\) imply \(R_*^2=m(R_*-m+1)^2\). Substituting in their derivative formulas yields \(\lambda_{m+1}'(R_*)/\lambda_{m-1}'(R_*)=m/(m+1)\). A first-order Taylor expansion around \(R_*\) proves the claimed local reversal relative to each neighboring mode.

## Verification

The accompanying `checker.py` exactly verifies identity (2) as a polynomial in the two symbolic variables and verifies the divisibility underlying the universal slope ratio. It independently compares the adjacent-gap formula against numerical quadrature for multiple indices and radii, verifies consecutive triples at the first four pronic areas, and performs finite exact-integer checks of the two-root pattern. The packaged replay returned `SECOND_HERMITE_RESONANCE_CHECKS_PASS 1180`. These finite checks corroborate the proof; the all-index and all-area conclusions are the exact algebra and arguments above, not extrapolations from computation.

## Relationship to prior work

Abreu, Gröchenig, and Romero give the general radial Hermite-window diagonalization and eigenvalue-integral formula; their Remark 4.3 explicitly notes a **first-Hermite** eigenvalue crossing. Equation (1) is a specialization of that established formula, not a new eigenvalue expression. Maximenko and Tellería-Romero obtain general radial polyanalytic Toeplitz eigenvalue formulas and structural operator results. The claimed contribution here is the all-area adjacent-gap factorization together with complete **second-Hermite** consecutive resonance classification, simultaneous pronic double triples, and the transverse slope-ratio law. These are not asserted in the specifically inspected sections of those works. This priority assessment is provisional: general Laguerre identities or other sources could implicitly cover the same theorem.

## Limitations

The classification concerns the normalized second Hermite window and **disk** localization, not arbitrary windows or domains. It concerns equality of eigenvalues at **consecutive Hermite labels**. Nonconsecutive accidental eigenvalue equalities are not excluded; in particular, the theorem does not assert the total geometric multiplicity of any spectral value is exactly three, nor does it identify the rank of a globally sorted spectral cutoff. The local reversal is only with respect to the immediately adjacent labels and sufficiently small changes of area. No independent external audit has been performed.

## References

1. L. D. Abreu, K. Gröchenig, J. L. Romero, *Harmonic analysis in phase space and finite Weyl–Heisenberg ensembles*, arXiv:1704.03042, first posted 2017-04-10; Section 4, Proposition 4.1, Lemma 4.2, Remark 4.3, and Section 5. https://arxiv.org/abs/1704.03042
2. E. A. Maximenko, A. M. Tellería-Romero, *Radial operators on polyanalytic Bargmann–Segal–Fock spaces*, arXiv:1905.00978, first posted 2019-05-02; Section 6, Proposition 6.3 and equation (43). https://arxiv.org/abs/1905.00978
