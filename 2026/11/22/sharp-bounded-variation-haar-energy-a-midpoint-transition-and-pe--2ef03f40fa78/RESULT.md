# Sharp bounded-variation Haar energy: a midpoint transition and period-two critical law

## Finding

Let \(h_{k,j}\) be the standard real \(L^2(0,1)\)-orthonormal Haar wavelets, indexed by \(k\in\mathbb N_0\) and \(0\le j<2^k\). For real \(f\in BV(0,1)\) define the all-scale quadratic Haar seminorm
\[
\mathcal E_s(f)=\sum_{k=0}^{\infty}2^{2sk}\sum_{j=0}^{2^k-1}|\langle f,h_{k,j}\rangle|^2,
\qquad C_s^2=\sup_{|Df|(0,1)>0}\frac{\mathcal E_s(f)}{|Df|(0,1)^2}.
\]

The complete sharp boundedness classification is as follows.

1. If \(s<1/2\), put \(r=2^{2s-1}\in(0,1)\), \(T(x)=2x\pmod 1\) and \(\phi(x)=\operatorname{dist}(x,\mathbb Z)\). Then
\[
C_s^2=\max_{0\le x\le1}\sum_{k=0}^{\infty}r^k\phi(T^kx)^2.
\]
Every nonconstant function attaining this norm is, modulo almost-everywhere equality, a nonzero multiple of a *single jump* \(\mathbf1_{[x,1)}\) plus a constant, with \(x\) a maximizer of the displayed discounted potential. No complete closed form of its maximizer set for \(0<s<1/2\) is asserted.

2. For every \(s\le0\), \(C_s^2=1/4\), and its only jump location is \(x=1/2\). For every \(0<s<1/2\), \(C_s^2>1/4\), so the midpoint jump strictly ceases to maximize the energy as soon as positive smoothness weighting is introduced.

3. For \(s\ge1/2\), no finite universal constant \(C_s\) exists; already a single jump at \(x=1/3\) has infinite energy.

4. As \(s\uparrow1/2\), the sharp critical coefficient and an explicit bounded remainder are
\[
\frac{1}{9(1-r)}\le C_s^2\le\frac{1}{9(1-r)}+\frac16,
\qquad \lim_{s\uparrow1/2}(1-r)C_s^2=\frac19,
\]
so \(C_s\sim [3\sqrt{2\log 2\,(1/2-s)}]^{-1}\). For any choices of maximizing jumps \(x_r\), their discounted scale-orbit occupation measures
\[
\nu_r=(1-r)\sum_{k=0}^{\infty}r^k\delta_{T^kx_r}
\]
converge weakly to \(\big(\delta_{1/3}+\delta_{2/3}\big)/2\). Thus the worst energy concentrates, in *scale distribution*, on the period-two orbit rather than at the levelwise tent maximum \(1/2\).

## Assumptions and scope

The interval is open \((0,1)\); \(|Df|(0,1)\) denotes the total variation of the distributional derivative on that interval, excluding fictitious endpoint jumps. Functions are real, considered as almost-everywhere equivalence classes, and constants have zero energy. Each Haar function is \(2^{k/2}\) on the left half of \([j2^{-k},(j+1)2^{-k})\), \(-2^{k/2}\) on its right half, and zero elsewhere. The wavelet weights are exactly \(2^{2sk}\); using other boundary conventions, wavelets, or norms gives a different problem. The circle is only the auxiliary phase space for the doubling-map potential, not the original function domain.

## Proof

**Jump reduction and exact sharpness.** Write \(g_x(t)=\mathbf1_{[x,1)}(t)\) for \(0<x<1\). A direct integral on the one dyadic cell containing \(x\) gives
\[
\sum_{j=0}^{2^k-1}|\langle g_x,h_{k,j}\rangle|^2
=2^{-k}\phi(2^kx)^2.
\]
For \(r<1\), the weighted coefficient vector \(G_x=(2^{sk}\langle g_x,h_{k,j}\rangle)_{k,j}\) belongs to \(\ell^2\) with \(\|G_x\|^2=F_r(x):=\sum r^k\phi(T^kx)^2\le1/[4(1-r)]\). The map \(x\mapsto G_x\) is continuous in \(\ell^2\) by uniform geometric domination. Every real \(BV\) function has a finite signed derivative measure \(\mu=Df\) and, modulo constants, \(f=\int g_x\,d\mu(x)\). Bochner integration and the triangle inequality yield
\[
\sqrt{\mathcal E_s(f)}=\left\|\int G_x\,d\mu(x)\right\|
\le \int\|G_x\|\,d|\mu|(x)
\le \sqrt{\max F_r}\,|Df|(0,1).
\]
A maximizing jump gives equality. Equality in the Hilbert-space triangle inequality requires its signed unit vectors \(G_x\) to have the same direction for \(|\mu|\)-almost every \(x\). By Haar completeness, two distinct interior jump functions cannot be proportional modulo constants; hence \(\mu\) is one point mass and every extremizer has the claimed form.

**Midpoint threshold.** Haar Parseval for \(g_x\) (subtracting its constant mean) gives \(F_{1/2}(x)=\|g_x-\int_0^1g_x\|_2^2=x(1-x)\). Thus \(F_r(x)\le F_{1/2}(x)\le1/4\) if \(r\le1/2\), and \(x=1/2\) attains \(1/4\) since all its later orbit terms vanish. The strict inequality \(x(1-x)<1/4\) away from \(1/2\) proves location uniqueness. For \(r>1/2\), set \(x_m=1/2-2^{-m}\), \(m\ge2\). Because \(T^mx_m=0\), exact summation gives
\[
F_r(x_m)-\frac14=-2^{-m}+4^{-m}\left(1+\sum_{k=1}^{m-1}(4r)^k\right)>0
\]
for all sufficiently large \(m\): the last positive term dominates because \(2r>1\). This proves the sharp change precisely at \(s=0\).

**Critical bound via a calibrated identity.** For \(v(x)=x(1-x)\) and all \(x\in[0,1]\), the following *pointwise exact identity* holds (verify it separately on the two tent branches):
\[
\phi(x)^2=\frac19+\frac23\big(v(x)-v(Tx)\big)
-\left(\phi(x)-\frac13\right)^2.
\tag{*}
\]
Discounted summation and a geometric telescoping yield, for \(0<r<1\),
\[
F_r(x)=\frac1{9(1-r)}+\frac23\left[v(x)-(1-r)\sum_{k=1}^{\infty}r^{k-1}v(T^kx)\right]
-\sum_{k=0}^{\infty}r^k\left(\phi(T^kx)-\frac13\right)^2.
\]
All omitted terms are nonnegative and \(0\le v\le1/4\), so \(F_r(x)\le1/[9(1-r)]+1/6\). At \(x=1/3\), the doubling orbit alternates between \(1/3\) and \(2/3\), with \(\phi=1/3\) at every level; hence \(F_r(1/3)=1/[9(1-r)]\). Both bounds hold for the supremum, giving the exact critical coefficient. Since \(1-r\sim2\log2\,(1/2-s)\), the stated asymptotic follows.

**Scale-orbit concentration.** For every maximizing \(x_r\), the lower bound \(F_r(x_r)\ge1/[9(1-r)]\) and the calibrated identity imply
\[
0\le\int\left(\phi-\frac13\right)^2\,d\nu_r
\le\frac{1-r}{6}.
\]
The probability measures \(\nu_r\) satisfy \(\nu_r-rT_*\nu_r=(1-r)\delta_{x_r}\). Any weak limit as \(r\uparrow1\) is therefore invariant under the continuous circle doubling map and supported on the zero set of \((\phi-1/3)^2\), namely \(\{1/3,2/3\}\). Those two points are exchanged by \(T\), forcing equal mass; uniqueness of the limiting measure gives convergence of the whole family.

**Failure at and above the critical exponent.** The same jump \(g_{1/3}\) gives \(\mathcal E_s(g_{1/3})=\sum_{k\ge0}r^k/9=+\infty\) for \(r\ge1\), while \(|Dg_{1/3}|(0,1)=1\).

## Verification

The standalone `check.py` in this package executes 12,802 exact rational assertions checking the calibrated potential identity, Haar jump-coefficient normalization, finite dyadic Parseval identity, positive-smoothness jump advantage, two-cycle sums, global pointwise upper bound and finite discounted telescoping. Execute `python check.py` with Python 3. The analytical steps above, not a finite grid or checker, prove the universal and infinite-scale statements.

## Relationship to prior work

Cohen, Dahmen, Daubechies and DeVore (2003) developed weak-\(\ell^1\) wavelet coefficient estimates and interpolation statements for the space \(BV\). Shchitov (2016) gave exact bounds for individual Haar coefficients and fixed-level aggregates under variation constraints. Neither result as inspected computes the sharp *jointly weighted all-level quadratic* \(BV\)-to-Haar norm, its midpoint-extremizer threshold, or the period-two critical residue. Galkin, Galkina and Tronov (2021) studied the different one-parameter Takagi power family \(\sum(2^{-k}\phi(2^kx))^p\), predominantly for \(0<p<1\); here the tent exponent is fixed at two and the independent discount \(r\) varies toward one. The single-scale bound cannot generally be saturated simultaneously at all levels. The period-two identity (*) supplies the simultaneous-scale constraint. These comparisons do not exclude an unindexed equivalent in dyadic ergodic optimization or wavelet embedding literature.

## Limitations

For \(0<s<1/2\), the maximizing jump set is characterized exactly by a convergent one-variable variational principle but not enumerated in a closed form. The convergence of \(\nu_r\) is an occupation-measure statement; no convergence of the initial maximizing locations \(x_r\) is claimed. The theorem concerns the real one-dimensional standard Haar basis and this specific Hilbert energy; it does not transfer automatically to other wavelet families or ordinary Fourier Sobolev norms. Independent expert validation has not been performed.

## References

- A. Cohen, W. Dahmen, I. Daubechies, R. A. DeVore, *Harmonic Analysis of the space BV*, Revista Matemática Iberoamericana 19 (2003), 235–263, https://doi.org/10.4171/RMI/345 (published 2003-04-30).
- A. N. Shchitov, *The Exact Estimates of Fourier-Haar Coefficients of Functions of Bounded Variation*, International Journal of Advanced Research in Mathematics 4 (2016), 14–22, https://doi.org/10.18052/www.scipress.com/IJARM.4.14 (online 2016-02-15).
- O. E. Galkin, S. Yu. Galkina, A. A. Tronov, *On the properties of functions of the Takagi power class*, arXiv:2112.08420, https://arxiv.org/abs/2112.08420 (initial version 2021-12-15).
