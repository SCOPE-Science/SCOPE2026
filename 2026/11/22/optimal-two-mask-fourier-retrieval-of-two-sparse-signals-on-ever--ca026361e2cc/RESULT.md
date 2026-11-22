# Optimal two-mask Fourier retrieval of two-sparse signals on every even cycle

## Finding

**Theorem (two patterns are both sufficient and necessary).** For every even integer \(N=2h\ge4\), there are two explicitly specified nonvanishing diagonal masks, one flat and the other with amplitudes in \([1,2)\) and phases in \(\{1,i\}\), such that their two full, unoversampled \(N\)-point discrete Fourier intensity patterns identify **every** complex vector supported on at most two coordinates, up to global phase. A single masked Fourier intensity pattern never does so. Thus the exact minimum number of complete, length-\(N\) coded patterns in this class is two, without any signal-dependent genericity assumption.

Here is one uniform construction. Let \(h=N/2\), set
\[
 L=2h^2+1,\quad R=2h+1,\quad B_j=Lj+j^2\quad (0\le j<h),
\]
\[
 E_j=RB_j,\qquad E_{j+h}=RB_j+j+1,\qquad M=RB_{h-1}+h+1,
\]
and put \(w_j=2^{E_j/M}\) for \(0\le j<N\). Define
\[
 m_0(j)=1,\qquad
 m_1(j)=\begin{cases}w_j,&0\le j<h,\\ i w_j,&h\le j<2h.\end{cases}
\]
These masks satisfy \(1\le |m_1(j)|<2\). With the unnormalized Fourier transform, the measured data are
\[
 Y_\ell(k)=\left|\sum_{j=0}^{N-1}m_\ell(j)x_j e^{-2\pi i jk/N}\right|^2,
 \quad \ell\in\{0,1\},\ k\in\{0,\ldots,N-1\}.
\]
No assumption is made on the two support locations, their relative phase, their relative nonzero magnitudes, or an ambient minimum-separation condition.

## Assumptions and scope

All arithmetic in the Fourier sampling indices is modulo \(N\), with the displayed representatives \(0,\ldots,N-1\) used to define the masks. The unknown \(x\in\mathbb C^N\) may be zero, one-sparse or exactly two-sparse, and the intensities are exact. Global multiplication by \(e^{it}\) is unobservable and is the only remaining ambiguity. The mask values are fixed in advance for each \(N\). No oversampling is used: each mask supplies exactly \(N\) scalar intensities. The masks depend on \(N\), but their maximum-to-minimum amplitude ratio stays strictly below two. No claim is made for three-sparse inputs or uniform-in-\(N\) stability in measurement noise.

## Proof

**1. An exact pair-product code.** We first show that the numbers \(E_j\) are pairwise distinct and that the unordered pair sums \(E_a+E_b\), for \(0\le a<b<N\), are all distinct. Suppose
\(B_p+B_q=B_r+B_s\), where \(p,q,r,s\in\{0,\ldots,h-1\}\), allowing repetition. Then
\[
 L(p+q-r-s)=r^2+s^2-p^2-q^2.
\]
The absolute value on the right is at most \(2(h-1)^2<L\), so \(p+q=r+s\). Equality of quadratic sums then gives \(pq=rs\), whence the unordered multisets \(\{p,q\}=\{r,s\}\).

Any two different mask indices \(a,b\) belong to groups \(p=a\bmod h\), \(q=b\bmod h\). Their exponent sum has the unique quotient–remainder form
\[
 E_a+E_b=R(B_p+B_q)+e,\qquad 0\le e<R.
\]
For \(p\ne q\), the remainder is one of \(0,p+1,q+1,p+q+2\), according to whether neither, only the first, only the second, or both indices lie in the upper half. These four values are distinct because \(p+1\ne q+1\) and both are positive. For \(p=q\), the two distinct indices are necessarily \(p,p+h\), giving remainder \(p+1\). Therefore quotient–remainder uniqueness and the preceding uniqueness of \(B_p+B_q\) prove the pair-sum assertion. Individual exponents are also distinct, because the two members of each group differ by \(j+1\), while consecutive groups are separated by more than \(h\). Hence all \(w_j\) are distinct and all products \(w_aw_b\) indexed by unordered distinct pairs are distinct.

Moreover, for \(0\le j<h-1\),
\[
 E_j<E_{j+h}<E_{j+1}.
\]
Thus the closed intervals \([w_j^2,w_{j+h}^2]\), for \(0\le j<h\), are pairwise disjoint. Finally, \(0\le E_j<M\) gives the asserted uniform mask-amplitude bound.

**2. Fourier intensities determine masked cyclic correlations.** Invert each full intensity pattern:
\[
 C_\ell(d)=\frac1N\sum_{k=0}^{N-1}Y_\ell(k)e^{2\pi i kd/N}
 =\sum_{a-b\equiv d\ (\mathrm{mod}\ N)}m_\ell(a)x_a\overline{m_\ell(b)x_b}.
\]
In particular,
\[
 C_0(0)=\sum_j|x_j|^2,\qquad
 C_1(0)=\sum_jw_j^2|x_j|^2.
\]
If \(C_0(0)=0\), then \(x=0\). If all nonzero-lag correlations vanish for both masks, \(x\) is one-sparse: a nonantipodal two-sparse vector has a nonzero flat correlation at each of the distinct lags \(\pm(a-b)\); an antipodal two-sparse vector has at least one nonzero correlation at lag \(h\), as proved in step 4. For a nonzero one-sparse vector, the ratio \(C_1(0)/C_0(0)=w_j^2\) identifies its location and \(C_0(0)\) its modulus.

**3. Nonantipodal supports.** Let \(x_a,x_b\ne0\), \(a\ne b\), and \(a-b\not\equiv h\pmod N\). The only nonzero nonzero-lag flat correlations are at the two distinct lags \(d\equiv a-b\) and \(-d\), and they cannot cancel. At either of those lags,
\[
 \frac{|C_1(d)|}{|C_0(d)|}=w_aw_b.
\]
The pair-product code of step 1 therefore uniquely identifies the *unordered physical support* \(\{a,b\}\), not merely its cyclic distance. Order it with \(a<b\) and write \(u=|x_a|^2\), \(v=|x_b|^2\). The equations
\[
 u+v=C_0(0),\qquad w_a^2u+w_b^2v=C_1(0)
\]
have a unique solution because \(w_a\ne w_b\). Choose \(x_a=\sqrt u>0\) by global-phase normalization; then \(x_b=C_0(b-a)/\sqrt u\). This is the complete signal up to its global phase.

**4. Antipodal supports.** If \(b=a+h\pmod N\), choose the unique representative \(a=j\in\{0,\ldots,h-1\}\) and put \(b=j+h\). Write \(z=x_j\overline{x_{j+h}}\ne0\). Only lag \(h\) can have a nonzero nonzero-lag correlation, and the special quadrature phase gives
\[
 C_0(h)=2\operatorname{Re}z,\qquad
 C_1(h)=2w_jw_{j+h}\operatorname{Im}z.
\]
These cannot both vanish, so antipodal supports are recognizable from the two correlation arrays, even when either individual correlation vanishes. Their support index \(j\) is uniquely identified because the positive convex-combination ratio
\[
 \frac{C_1(0)}{C_0(0)}
 =\frac{w_j^2|x_j|^2+w_{j+h}^2|x_{j+h}|^2}{|x_j|^2+|x_{j+h}|^2}
 \in(w_j^2,w_{j+h}^2)
\]
falls inside exactly one of the pairwise disjoint intervals from step 1. The two zero-lag equations recover the individual squared magnitudes. The two lag-\(h\) equations recover both real and imaginary parts of \(z\). Choosing \(x_j=\sqrt{|x_j|^2}>0\), then \(x_{j+h}=\overline z/x_j\), completes the reconstruction.

**5. Sharp mask count.** For any one diagonal mask, if it has a zero at a coordinate, an impulse there is indistinguishable from the zero vector. If the mask is nonvanishing, choose two different coordinate impulses and adjust their amplitudes so that their *masked* values both have modulus one. Every Fourier intensity of either masked impulse equals one, but the two input vectors have different supports and cannot differ by global phase. Thus one mask cannot distinguish all one-sparse inputs, let alone every at-most-two-sparse input. Steps 1–4 construct two masks that do, proving optimality.

## Verification

Run `python3 CHECK.py` in an ordinary Python 3 environment; no third-party package is needed. The program checks the integer pair-product-code invariant through \(h=60\), verifies the disjoint antipodal signature intervals, and reconstructs finite test vectors in all support regimes using the two complete Fourier-intensity arrays. In its recorded run it printed

`CHECK_OK exact_integer_pair_sums=145789 decoder_tests=1660 antipodal_tests=132`

These finite experiments are diagnostic only. The unbounded assertions for **every** even \(N\) and **every** complex at-most-two-sparse input follow from the analytic proof above, not from finite enumeration.

## Relationship to prior work

The 2026 coded-diffraction PhaseLift result of Huang and Li [1] concerns \(O(\log N)\) random masks for general complex signals, without the present sharp deterministic two-sparse two-pattern assertion. Bandeira, Chen and Mixon [2] develop full-signal recovery using a Fourier-mask polarization construction and \(O(\log N)\) masks. Jaganathan, Eldar and Hassibi [3] describe two-mask generic recovery when each mask supplies \(2N\) oversampled Fourier measurements, a different guarantee. Li and Li [4] study random masked measurements and the failure of real masks for arbitrary complex signals in even dimension.

The published odd-cycle two-sparse theorem [5] gives two bounded-contrast **real** masks and explicitly notes the real-mask obstruction for even cycles; its statement and proof do not imply that two **complex** masks suffice on every even cycle. The present construction overcomes the antipodal obstruction using quadrature phases and a separated pair-product code. In contrast to three-mask even-cycle designs, the present theorem proves the optimal mask count of two. These are comparisons of the mathematical guarantees, not claims about title uniqueness or all possible unindexed literature.

## Limitations

The result gives exact identifiability and an explicit decoder, not a dimension-independent Lipschitz stability theorem. Although the *amplitude* contrast is uniformly below two and the exponent code is polynomially sized, recovery can deteriorate near vanishing signal entries or under noise. The result does not address more than two occupied sites, phase-only masks, or arbitrary complex signals. The exact two-mask even-cycle theorem was not found in the sources inspected, but an older specialized deterministic construction may remain unidentified; the full text of [1] and [4] was not fully available for inspection.

## References

[1] G. Huang and S. Li, *PhaseLift for Coded Diffraction Patterns: Optimal Sampling Rate*, arXiv:2608.02450, first public 2026-08-03. https://arxiv.org/abs/2608.02450

[2] A. S. Bandeira, Y. Chen and D. G. Mixon, *Phase retrieval from power spectra of masked signals*, arXiv:1303.4458, 2013. https://arxiv.org/abs/1303.4458

[3] K. Jaganathan, Y. C. Eldar and B. Hassibi, *Phase retrieval with masks using convex optimization*, IEEE ISIT (2015). https://doi.org/10.1109/ISIT.2015.7282737

[4] H. Li and S. Li, *Phase retrieval from Fourier measurements with masks*, Inverse Problems and Imaging 15 (2021), 1051–1075. https://doi.org/10.3934/ipi.2021028

[5] *Sharp two-mask Fourier recovery of complex two-sparse signals on odd cycles*, published published-finding corpus mathematical record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-two-mask-fourier-recovery-of-complex-two-sparse-signals-on--cead19f36641
