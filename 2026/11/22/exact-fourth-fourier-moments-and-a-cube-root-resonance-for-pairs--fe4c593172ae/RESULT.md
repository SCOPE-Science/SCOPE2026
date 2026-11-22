# Exact fourth Fourier moments and a cube-root resonance for pairs of finite-field parabolas

## Finding
Let \(q\) be any odd prime power, let \(\mathbb F_q\) be its field, and let
\[
P_c=\{(x,cx^2):x\in\mathbb F_q\},\qquad
S_\lambda=P_1\cup P_\lambda,
\quad\lambda\in\mathbb F_q\setminus\{0,1\}.
\]
The branches meet only at the origin, so \(|S_\lambda|=2q-1\). Write \(\chi\) for the quadratic character with \(\chi(0)=0\) and put
\[
B_q=22q^2-54q+33.
\]
The exact additive energy, equivalently the sharp fourth Fourier moment of the support indicator, is
\[
\boxed{E(S_\lambda)=B_q-4(q-1)\left[\chi(2\lambda-1)+\chi(\lambda(2-\lambda))-\mathbf1_{\{\lambda=-1\}}\right].}
\tag{1}
\]
For the unitary Fourier transform \(\widehat f(\xi)=q^{-1}\sum_{z\in\mathbb F_q^2}f(z)\psi(-\langle z,\xi\rangle)\), formula (1) is exactly
\[
\boxed{\sum_{\xi\in\mathbb F_q^2}|\widehat{\mathbf1_{S_\lambda}}(\xi)|^4=q^{-2}E(S_\lambda).}
\]
The two-branch *multiplicity* function \(f_\lambda=\mathbf1_{P_1}+\mathbf1_{P_\lambda}\), which counts the common origin twice, has the striking parameter-independent identity
\[
\boxed{\sum_{\xi}|\widehat{f_\lambda}(\xi)|^4=22-6/q.}
\tag{2}
\]
Hence all parameter dependence in the energy of the *set* arises solely from correcting the double-counted intersection.

The complete sharp lower and upper envelopes across all admissible parameters are as follows. In the table, extrema are expressed in the natural units \((E(S_\lambda)-B_q)/(4(q-1))\).

| Field order | Minimum | Maximum |
| --- | ---: | ---: |
| \(3\) | \(1\) | \(1\) |
| \(5\) | \(1\) | \(3\) |
| \(7\) | \(-1\) | \(1\) |
| \(9\) | \(0\) | \(2\) |
| \(11\) | \(-1\) | \(3\) |
| \(13\) | \(-1\) | \(2\) |
| Every odd prime power \(q\ge17\) | \(-2\) | \(3\) if \(q\equiv2\pmod3\), otherwise \(2\) |

For every \(q\ge17\), the minimizers are exactly the non-opposite ratios satisfying
\[\chi(2\lambda-1)=\chi(\lambda(2-\lambda))=1.\]
If \(q\equiv2\pmod3\), the *unique* maximizer is \(\lambda=-1\), at the exceptional energy \(B_q+12(q-1)\). If \(q\equiv0\) or \(1\pmod3\), the maximizers are exactly the non-opposite ratios satisfying both characters equal \(-1\), with energy \(B_q+8(q-1)\). Thus \(17\) is the first odd field order at which the displayed large-field lower envelope is attained, and it remains attained for all larger odd prime powers.

There is also an exact arithmetic census of all possible energy levels. Suppose the characteristic is at least five. Set
\[
T_q=\sum_{t\in\mathbb F_q}\chi((2t-1)t(2-t)),\quad
R_q=1+\chi(-1)+\chi(3),\quad
U=\mathbb F_q\setminus\{0,1,1/2,2\}.
\]
For each \(\sigma,\tau\in\{\pm1\}\), the number of \(\lambda\in U\) with \(\chi(2\lambda-1)=\sigma\) and \(\chi(\lambda(2-\lambda))=\tau\) is exactly
\[
\boxed{N_{\sigma,\tau}=\frac{q-4-(\sigma+\tau)R_q+\sigma\tau(T_q-1)}4.}
\tag{3}
\]
The two allowed ratios \(\lambda=1/2,2\) have respectively character pairs \((0,\chi(3))\), \((\chi(3),0)\), and \(\lambda=-1\) receives the extra intersection correction in (1). The cubic in \(T_q\) is squarefree, so the Hasse bound gives \(|T_q|\le2\sqrt q\). Thus (3), with the three explicit exceptional ratios, is an exact full energy-level histogram for every such field, using a single elliptic trace.

In characteristic three, put \(e=\chi(-1)\) and \(U=\mathbb F_q\setminus\{0,1,-1\}\). Both characters vanish at the admissible exceptional ratio \(\lambda=-1\), and the sign-pair counts over \(U\) are instead
\[
\boxed{N_{\sigma,\tau}=\frac{q-3-(1+e)(\sigma+\tau+\sigma\tau)}4.}
\tag{4}
\]
Equations (1), (3) and (4) give every energy and its number of attaining ratios, not just the envelopes.

## Assumptions and scope
All statements concern odd prime-power fields, not just prime fields. Addition is componentwise on \(\mathbb F_q^2\); the Fourier transform uses a fixed nontrivial additive character \(\psi\) and the unitary normalization \(q^{-1}\). The ordered additive energy is
\[
E(S)=\#\{(s_1,s_2,s_3,s_4)\in S^4:s_1+s_2=s_3+s_4\}=\sum_{z\in\mathbb F_q^2}(\mathbf1_S*\mathbf1_S)(z)^2.
\]
All coefficients in the exact identities are integers. The character \(\chi\) takes the values \(0,1,-1\). The ratio \(\lambda\) is the ordered-branch curvature ratio; swapping the branches sends \(\lambda\) to \(\lambda^{-1}\), which exchanges the two character terms in (1) and preserves the energy. The finite small-field exceptions are essential; neither the asymptotic extremal formula nor the non-exceptional sign classification is asserted for them.

## Proof
**1. Two-parabola convolution and orthogonality.** For nonzero \(a,b\), let \(C_{a,b}=\mathbf1_{P_a}*\mathbf1_{P_b}\). Solving \(x+y=s\) and \(ax^2+by^2=t\) gives
\[
C_{a,b}(s,t)=1+\chi((a+b)t-ab s^2)\quad(a+b\ne0).
\tag{5}
\]
If \(a+b=0\), direct elimination yields \(C_{a,-a}(s,t)=1\) when \(s\ne0\); for \(s=0\), it is \(q\) at \(t=0\) and zero elsewhere. Thus write \(C_{a,b}=1+h_{a,b}\) in both cases, where each \(h_{a,b}\) has zero sum and squared \(\ell^2\)-norm \(q(q-1)\). For \(a+b=0\), explicitly \(h_{a,-a}(s,t)=\mathbf1_{\{s=0\}}(q\mathbf1_{\{t=0\}}-1)\).

Fix \(a\ne b\), both nonzero. The three functions \(h_{a,a}\), \(h_{b,b}\), and \(h_{a,b}\) are pairwise orthogonal. When \(a+b\ne0\), their quadratic-character arguments have distinct roots in \(t\) for each \(s\ne0\): respectively \(as^2/2\), \(bs^2/2\), and \(ab s^2/(a+b)\). The standard two-root character identity is
\[
\sum_{t\in\mathbb F_q}\chi((t-u)(t-v))=\begin{cases}q-1,&u=v,\\-1,&u\ne v.\end{cases}
\]
It follows directly by counting solutions of \(w^2=(t-u)(t-v)\) (for \(u\ne v\), the invertible change \((2t-u-v,2w)\) gives a hyperbola with \(q-1\) solutions). For each pair, \(s=0\) contributes \((q-1)\) times a fixed character of a nonzero scalar, while the \(q-1\) remaining values contribute its negative, so the total inner product vanishes. When \(a+b=0\), the support of \(h_{a,-a}\) is \(s=0\), where its inner products with \(\chi(2at)\) and \(\chi(2bt)\) vanish by character cancellation; the other pair remains orthogonal by the same two-root identity.

For \(f=\mathbf1_{P_a}+\mathbf1_{P_b}\), therefore,
\[
f*f=C_{a,a}+C_{b,b}+2C_{a,b}=4+h_{a,a}+h_{b,b}+2h_{a,b},
\]
whence, exactly,
\[
\sum_z(f*f)(z)^2=16q^2+(1+1+4)q(q-1)=22q^2-6q.
\tag{6}
\]
Plancherel and the fourth-moment identity yield (2).

**2. Removing the common origin.** Specialize to \(a=1\), \(b=\lambda\). Since the branches meet only at \(0\), \(\mathbf1_{S_\lambda}=f-\delta_0\), and
\[
\mathbf1_S*\mathbf1_S=f*f-2f+\delta_0.
\]
Directly, \(\sum_z f(z)^2=2q+2\), \(f(0)=2\), and
\[
(f*f)(0)=4+2(q-1)\mathbf1_{\{\lambda=-1\}}.
\tag{7}
\]
The essential triple-incidence term is
\[
\sum_z (f*f)(z)f(z)=14q-6+(q-1)\left[\chi(2\lambda-1)+\chi(\lambda(2-\lambda))\right].
\tag{8}
\]
Indeed, sum \(C_{a,b}(s,cs^2)\) over \(s\) for \(c=a,b\). The four same-branch or mixed-on-own-branch contributions each equal \(2q-1\), while the two cross-on-other-branch contributions are \(q+(q-1)\chi(a(2b-a))\) and \(q+(q-1)\chi(b(2a-b))\). In the \(a+b=0\) case, the exceptional \(s=0\) fiber still yields \(2q-1\) for the two mixed-on-own-branch contributions. The displayed sum follows.

Expanding the square of \(f*f-2f+\delta_0\), then substituting (6)--(8), gives
\[
E(S)=\sum(f*f)^2-4\sum(f*f)f+2(f*f)(0)+4\sum f^2-4f(0)+1,
\]
which simplifies exactly to (1). This proves the all-fields energy identity with no limiting or genericity assumptions.

**3. Exact character census.** Assume characteristic at least five. The two character polynomials vanish, among admissible \(\lambda\), at the distinct ratios \(1/2\) and \(2\). Over the remaining set \(U\), elementary character-sum identities give
\[
\sum_U\chi(2\lambda-1)=\sum_U\chi(\lambda(2-\lambda))=-R_q,
\quad
\sum_U\chi((2\lambda-1)\lambda(2-\lambda))=T_q-1.
\]
Here the second identity uses \(\sum_x\chi(1-(x-1)^2)=-\chi(-1)\); all omitted contributions are explicit. Expanding
\(\frac14(1+\sigma\chi(2\lambda-1))(1+\tau\chi(\lambda(2-\lambda)))\)
proves (3). The affine curve \(y^2=(2x-1)x(2-x)\) has three distinct roots in characteristic at least five, hence defines a nonsingular genus-one curve, and Hasse's point-count bound gives \(|T_q|\le2\sqrt q\).

In characteristic three, \(2=-1\), so for every allowed \(\lambda\ne-1\), the product of the two signs equals \(\chi(\lambda)\). Removing the three points \(0,1,-1\) from the complete sums gives
\(\sum_U A=\sum_U B=\sum_U AB=-(1+\chi(-1))\), which proves (4). At \(\lambda=-1\), both signs vanish and the correction in (1) is one.

**4. Sharp envelopes and the first persistent threshold.** Let \(D_\lambda=(E(S_\lambda)-B_q)/(4(q-1))\). Formula (1) gives
\(D_\lambda=-A_\lambda-B_\lambda+\mathbf1_{\{\lambda=-1\}}\).
If the characteristic is not three, the discriminant identity for \(x^2+x+1\) gives
\[\chi(-3)=1\iff q\equiv1\pmod3,\qquad\chi(-3)=-1\iff q\equiv2\pmod3.\]
At the opposite ratio \(\lambda=-1\), both signs equal \(\chi(-3)\). Consequently \(D_{-1}=3\) when \(q\equiv2\pmod3\), strictly larger than the maximum \(2\) for all other ratios. When \(q\equiv1\pmod3\), \(D_{-1}=-1\), so the true extremal levels \(-2,2\) can only arise at non-opposite ratios with both signs respectively positive or negative. In characteristic three, \(D_{-1}=1\), and the same two generic sign classes produce \(-2,2\).

To prove these classes occur uniformly in all sufficiently large fields, for characteristic at least five apply (3) and \(|T_q|\le2\sqrt q\). Since \(R_q\le3\) and \(R_q\ge-1\),
\[
4N_{+,+}\ge q-11-2\sqrt q>8,\qquad
4N_{-,-}\ge q-7-2\sqrt q>0
\]
for every \(q\ge31\). Thus there are at least two positive-positive choices even if one is the exceptional \(\lambda=-1\), and at least one negative-negative choice. In characteristic three, (4) supplies both sign pairs for \(q\ge27\), since \(q=3^{2m+1}\ge27\) gives \(e=-1\) and \(q=3^{2m}\ge81\) gives \(e=1\).

The remaining field orders from \(17\) through \(29\) are \(17,19,23,25,27,29\). Direct finite character evaluation gives the following counts of *non-opposite* positive-positive and negative-negative ratios, respectively:

| \(q\) | \((+,+)\) non-opposite | \((-,-)\) non-opposite |
| ---: | ---: | ---: |
| 17 | 2 | 2 |
| 19 | 4 | 4 |
| 23 | 6 | 6 |
| 25 | 4 | 8 |
| 27 | 6 | 6 |
| 29 | 4 | 4 |

These values follow from (3) or (4), including the quadratic extension at \(q=25\), and are separately checked by `CHECK.py`. The six smaller odd prime-power fields \(q=3,5,7,9,11,13\), evaluated by the same formulas, give precisely the exceptional extrema in the table under Finding; in none is the level \(-2\) attained. Hence the uniform first persistent lower threshold is exactly \(17\), with all minimizer and maximizer classifications as stated.

## Verification
The standalone standard-library script `CHECK.py` constructs every admissible pair of parabolas directly over the ten prime fields \(3,5,7,11,13,17,19,23,29,31\) and four extension fields \(\mathbb F_9,\mathbb F_{25},\mathbb F_{27},\mathbb F_{49}\). It independently counts all ordered additive quadruples by convolution (without using formula (1)) and compares against the formula for every available curvature ratio; 240 parameter cases pass. It separately checks character-pair census (3), exact integrality, and all applicable sharp extrema. The output `DIRECT_ENERGY_CHECK_OK 240` is reproducible with Python 3. These finite checks do not prove the all-field result; the convolution orthogonality proof and Hasse bound do.

## Relationship to prior work
Iosevich, Li and Yu (2026, arXiv:2609.25404v1, Sections 2 and 8) explain the Fourier fourth-moment/additive-energy identity and study spectral synthesis for single paraboloids. Their theorems do not give the two-component curvature-ratio energy formula, the intersection correction, or sharp extremizers. A published calculation titled *A sharp \(4/\pi\) amplification law for Fourier projection onto two opposite finite parabolas* analyzes the \(\ell^\infty\) Fourier projection norm at the particular opposite ratio; its explicit Fourier kernel implicitly permits recovering that one special fourth moment, so no independent novelty is claimed for the opposite-ratio specialization. It does not provide the full curvature-ratio profile, the character census, or sharp cross-ratio extremizers; its endpoint norm is a different functional from the fourth moment. Asgarli and Yip (2025) study mutual positions of smooth quadrics using quadratic characters, but their conic tangency counts are not additive-energy statements. The classical quadratic Gauss-sum and Hasse identities supply standard lemmas, not a prior formula for the present union's complete energy profile. The special ratio \(\lambda=-1\) is acknowledged as a previously considered geometric configuration; only the present additive-energy extremal claim is proposed as new.

## Limitations
The result concerns unions of exactly two nonzero distinct-curvature graphs sharing their origin, not arbitrary conics, vertically translated parabolas, weighted Fourier coefficients, or complex phases on the support. The fourth Fourier moment here is that of the indicator, not the *sharp* \(L^2\to L^4\) extension operator norm for arbitrary weights. Hasse's bound is invoked as a standard external theorem; the all-field energy formula itself is elementary and exact. The elliptic trace \(T_q\) in the histogram is not evaluated in closed arithmetic form for each field, nor is a new elliptic point-count theorem claimed. An older unindexed equivalent union-energy identity or a result whose generality immediately subsumes it remains a residual priority risk. No independent audit has been performed.

## References
- A. Iosevich, Z. Li and K. Yu, *Spectral synthesis with the complexity parameter in \(\mathbb Z_N^d\)*, arXiv:2609.25404v1, first public 2026-09-21, Sections 2, 5 and 8. https://arxiv.org/abs/2609.25404
- *A sharp \(4/\pi\) amplification law for Fourier projection onto two opposite finite parabolas*, published published-finding corpus record (2026), especially its Finding and Proof. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-4-pi-amplification-law-for-fourier-projection-onto-two-o--a4d0f8547404
- S. Asgarli and C. H. Yip, *Mutual position of two smooth quadrics over finite fields*, Designs, Codes and Cryptography 93 (2025), 4461–4472. https://doi.org/10.1007/s10623-025-01687-9
- H. Hasse, classical bound \(|\#E(\mathbb F_q)-(q+1)|\le2\sqrt q\) for an elliptic curve over \(\mathbb F_q\). Used only for the extremizer-existence census; the character identity is derived above.
