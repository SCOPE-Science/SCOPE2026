# Sharp cyclic two-block Fourier energy and Pell-resonant optimal spacings

## Finding

Let \(a\ge2\) be an integer. For any \(n\ge2a\), take two disjoint length-\(a\) cyclic intervals in \(G=\mathbb Z/n\mathbb Z\):
\[
I_a=\{0,1,\ldots,a-1\},\qquad
S_s=I_a\cup(s+I_a),\qquad a\le s\le n-a.
\]
Define the **ordered additive energy** and the unnormalized discrete Fourier transform by
\[
\mathcal E_{n,a}(s)
=\sum_{z\in G}\big(\mathbf1_{S_s}*\mathbf1_{S_s}(z)\big)^2
=\frac1n\sum_{k=0}^{n-1}\left|\sum_{x\in S_s}e^{-2\pi ikx/n}\right|^4.
\]
Write \(L=2a-1\) and \(E_0=4a^3+2a\).

**Sharp packing threshold.** For every \(n\ge2a\), \(\mathcal E_{n,a}(s)\ge E_0\) for all admissible \(s\). Equality for at least one \(s\) is possible **if and only if** \(n\ge3L=6a-3\). In that regime, after the reflection symmetry \(s\mapsto n-s\), **every** optimal separation is
\[
L\le s\le\left\lfloor\frac{n-L}{2}\right\rfloor.
\]

**Sharp near-threshold optimization.** For every integer \(0\le t\le a\), put \(n=3L-t\) and \(B(v)=\binom{v+2}{3}=v(v+1)(v+2)/6\) for nonnegative integers \(v\). Then
\[
\boxed{\min_s\mathcal E_{n,a}(s)
=E_0+\min_{0\le u\le\lfloor t/2\rfloor}
\left[8B(u)+2B(t-2u)\right].}
\]
Every minimizing separation, up to reflection, is exactly \(s=L-u\) for an integer \(u\) minimizing the bracket. Set
\[
r_t=t+\frac32-\frac12\sqrt{2t^2+12t+17}.
\]
For \(t=0,1\) the unique optimal parameter is \(u=0\). For \(t\ge2\), if \(r_t\notin\mathbb Z\) the optimal parameter is \(u=\lceil r_t\rceil\); if \(r_t\in\mathbb Z\), exactly the adjacent parameters \(u=r_t\) and \(u=r_t+1\) tie. The two-optimum defect values are precisely
\[
t=2,26,166,\ldots,
\qquad w^2-2(t+3)^2=-1,
\]
with positive Pell solutions \(w+(t+3)\sqrt2=(1+\sqrt2)^{2j+1}\) for \(j=1,2,\ldots\). The corresponding first optimal pairs are \(u\in\{0,1\}\), \(\{7,8\}\), and \(\{48,49\}\). Thus isolated ties occur infinitely often as the interval width is allowed to grow.

For \(t\to\infty\) subject to \(t\le a\), the optimally placed near-threshold blocks satisfy
\[
\frac{u}{t}\longrightarrow\frac1{2+\sqrt2},\qquad
\min_s\mathcal E_{3L-t,a}(s)-E_0
=\left(1-\frac{2\sqrt2}{3}\right)t^3+O(t^2).
\]

## Assumptions and scope

The group is finite cyclic and the intervals have integer endpoints, equal widths \(a\ge2\), and disjoint supports; the two gap lengths may differ. The optimization ranges over **all** such cyclic two-block supports of fixed \(n\) and \(a\), since translation reduces one start point to zero, and reflection interchanges \(s\) and \(n-s\). The energy counts ordered pairs and includes the zero Fourier frequency. The exact near-threshold minimizer formula requires \(0\le t\le a\); no formula for the optimizer at every smaller cyclic order is claimed. The packing threshold is valid for all \(n\ge2a\).

## Proof

**1. Three convolution packets and the exact energy.** Put \(T=\mathbf1_{I_a}*\mathbf1_{I_a}\), computed initially on the integers, with support \(\{0,\dots,L-1\}\) and entries \(1,2,\dots,a-1,a,a-1,\dots,1\). Because \(n\ge2a>L\), this packet embeds without self-aliasing in \(G\). For cyclic translation \(\tau_h\), one has the exact identity
\[
\mathbf1_{S_s}*\mathbf1_{S_s}=T+2\tau_sT+\tau_{2s}T.
\]
The three packet self-norms contribute \(6\|T\|_2^2=6(2a^3+a)/3=E_0\). Writing \(C_n(h)=\langle T,\tau_hT\rangle\ge0\), the cross terms give
\[
\boxed{\mathcal E_{n,a}(s)=E_0+8C_n(s)+2C_n(2s).}
\tag{1}
\]
The Fourier identity in the finding follows from \(\widehat{f*f}=\widehat f^{\,2}\) and cyclic Parseval with \(\widehat f(k)=\sum_xf(x)e^{-2\pi ikx/n}\). No analytic approximation is involved.

**2. The exact packing threshold.** Equality in (1) is equivalent to the pairwise disjointness of the three cyclic support intervals of length \(L\), starting at \(0,s,2s\). The circle must then contain at least \(3L\) sites. Conversely, if \(n\ge3L\), setting \(s=L\) produces three disjoint convolution packets. Restrict to \(a\le s\le\lfloor n/2\rfloor\) by reflection. The three successive cyclic center gaps are \(s,s,n-2s\). Their packet supports are disjoint exactly when \(s\ge L\) and \(n-2s\ge L\), proving the complete equality classification. In particular there are no ties from uncounted overlapping translates.

**3. Autocorrelation is strictly decreasing.** Define \(C(h)=\sum_{x\in\mathbb Z}T(x)T(x-h)\) for \(h\ge0\). It vanishes for \(h\ge L\), and is strictly decreasing on the integers \(0\le h\le L\). Indeed the triangular packet is the sum of indicators of its \(a\) nested centered level intervals \([r,L-1-r]\), \(0\le r<a\). The intersection length of any two such centered intervals, after translating one by a nonnegative amount, is nonincreasing in that amount. The largest-level interval with itself contributes \(L-h\) for \(0\le h\le L\), making the total decrease strict. For \(n>2L\) and \(0\le h\le n/2\), the circular correlation is exactly \(C_n(h)=C(h)\); no two distinct lifted overlaps can coexist.

**4. Reduction to one short discrete convex problem.** Assume \(0\le t\le a\), \(n=3L-t>2L\) and \(a\le s\le\lfloor n/2\rfloor\). Because \(2s\ge2a>L\), (1) becomes
\[
\mathcal E_{n,a}(s)=E_0+8C(s)+2C(n-2s).
\tag{2}
\]
For \(s\ge L\), the first correction is zero and the second grows with \(s\), so \(s=L\) is best in this range. For \(s<L-\lfloor t/2\rfloor\), the second correction vanishes and the first strictly decreases as \(s\) increases. The remaining first endpoint cannot beat \(s=L-\lfloor t/2\rfloor\): if \(t\) is even the latter has no second correction, and if \(t\) is odd it has just \(2C(L-1)=2\), while increasing \(s\) by one decreases \(8C(s)\) by at least \(8\). Hence every optimizer has \(s=L-u\) with \(0\le u\le\lfloor t/2\rfloor\).

When \(0\le v\le a\), overlapping the opposite tails of the two triangular packets over \(v\) sites gives
\[
C(L-v)=\sum_{j=0}^{v-1}(j+1)(v-j)=\frac{v(v+1)(v+2)}6=B(v).
\tag{3}
\]
For the permitted \(u\), the overlaps in (2) are of lengths \(u\) and \(t-2u\), each at most \(a\). Substituting (3) proves the claimed exact finite minimum and its complete optimizer correspondence.

**5. Sharp optimizer and arithmetic ties.** Write \(F_t(u)=8B(u)+2B(t-2u)\). Whenever both \(u\) and \(u+1\) are allowed, direct integer algebra gives
\[
F_t(u+1)-F_t(u)=4(u+1)(u+2)-2(t-2u)^2.
\tag{4}
\]
This is strictly increasing as \(u\) increases in the admissible range. Its smaller real zero is exactly \(r_t\), and its other zero lies outside the interval. The sign changes in (4) prove the ceiling rule, including the end cases \(t=0,1\), and show that a tie occurs precisely when \(r_t\) is an integer. This is equivalent to the integer-square equation \(w^2=2(t+3)^2-1\). The positive solutions of this standard negative Pell equation are exactly \(w+(t+3)\sqrt2=(1+\sqrt2)^{2j+1}\); the condition \(t\ge2\) selects \(j\ge1\). Each Pell tie gives two and only two minimizing parameters.

**6. The cubic boundary profile.** As \(t\to\infty\), the smaller zero satisfies \(r_t/t\to1-1/\sqrt2=1/(2+\sqrt2)\). Since the selected integer differs from \(r_t\) by at most one, \(u/t\) has the same limit. Expanding \(B(v)=v^3/6+O(v^2)\) uniformly over \(0\le v\le t\) gives
\[
F_t(u)=\frac43u^3+\frac13(t-2u)^3+O(t^2).
\]
Substitution of \(u/t=1/(2+\sqrt2)+O(t^{-1})\) yields the asserted leading coefficient \(1-2\sqrt2/3\). The proof does not require assuming any field characteristic or an unverified computational pattern.

## Verification

`CHECK.py` (Python 3, standard library) directly forms every ordered two-sum histogram, without using (1), in 504 separate pairs \((n,a)\) with \(2\le a\le13\) and \(2a\le n\le4(2a-1)\); it compares the optimal energy and complete optimizer sets with both the packing regime and the near-threshold formula, and verifies strictness below the threshold. It additionally checks integer Pell/tie equivalence for 500 successive defects and the first three ties. The checks passed. These finite enumerations support reproducibility but do not replace the universally quantified proof above.

## Relationship to prior work

The motivating Fourier phase-retrieval study by Xia and Xu (2026) addresses uniqueness and stability for finite unions of **real** intervals, not the minimization of a cyclic discrete fourth Fourier moment. Willms's autocorrelation/run-structure results (2013) establish general methods to compute periodic correlations of binary sequences; they do not supply a sharp optimal separation, threshold, or Pell-indexed ties for the two-block fourth moment. The publicly available exact continuous equal-interval intensity-stability calculation (2026, title below) measures distance **between intensity data at different gaps**, not the fourth moment of one cyclic binary aperture. The common convolution and Parseval principles are standard and are not claimed as new. The contribution asserted here is their combination into an all-width sharp near-packing design and exact arithmetic degeneracy classification.

## Limitations

The problem optimizes equal-size, contiguous, disjoint blocks with constant unit coefficients, not arbitrary binary supports or unequal widths. The closed optimizer classification below the packing threshold is proved only in the near-threshold window \(0\le t\le a\). This is a deterministic exact theorem, not a stochastic guarantee or a claim about phaseless inverse reconstruction. The original Xia–Xu preprint's full text was not accessible for complete inspection; the explicit known result statements concern a different (real-line inverse) question, but an implicit priority overlap cannot be ruled out categorically. Full historical priority review and independent mathematical audit remain open.

## References

1. Yu Xia and Zhiqiang Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855 (first public June 18, 2026), https://arxiv.org/abs/2606.19855.
2. Jürgen Willms, *Autocorrelations of Binary Sequences and Run Structure*, arXiv:1206.4572 (preprint, revised April 2013), https://arxiv.org/abs/1206.4572.
3. *Sharp local and global Fourier-intensity stability of two equal intervals* (2026), publicly available at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-local-and-global-fourier-intensity-stability-of-two-equal--9eae37fe4ea0.
