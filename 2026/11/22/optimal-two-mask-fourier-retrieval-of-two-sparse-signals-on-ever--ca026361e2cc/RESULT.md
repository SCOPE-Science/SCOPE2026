# The exact phase-alphabet criterion for two-mask Fourier recovery of two-sparse signals on even cycles

## Finding

Let \(N=2h\ge4\). Take one flat mask and one diagonal mask whose entries have phases in a prescribed nonempty alphabet \(\mathcal P\subseteq\{z\in\mathbb C:|z|=1\}\). Given any amplitude budget \(\rho>0\), their two full, unoversampled \(N\)-point Fourier intensity patterns can identify **every** complex signal with at most two nonzero coordinates, up to global phase, with the second mask's amplitudes in \([1,1+\rho)\), **if and only if** \(\mathcal P\) contains two phases \(p,q\) with \(q/p\notin\{1,-1\}\).

The construction uses only those two phase values: \(p\) on the first half-cycle and \(q\) on the second. Thus a two-level phase alphabet is sufficient and minimal, and the two levels can be any prescribed noncollinear pair. For example, \(1,i\) give exact quadrature. There is no positive minimum amplitude contrast in this exact model: every strictly positive budget works, but a constant-amplitude second mask cannot distinguish even equal-magnitude impulses at different sites.

## Model and scope

The unknown \(x\in\mathbb C^N\) has zero, one or two nonzero coordinates at arbitrary sites on \(\mathbb Z_N\). Mask \(m_0(a)=1\) is flat and the other mask \(m_1\) is fixed before measurement. For \(\ell=0,1\) the full exact data are
\[
Y_\ell(k)=\left|\sum_{a=0}^{N-1}m_\ell(a)x_a e^{-2\pi i ak/N}\right|^2,\qquad 0\le k<N.
\]
Only multiplication of \(x\) by one common unit complex scalar is ignored. The phase alphabet need not be exhausted; only the selected \(p,q\) are used. The amplitudes are all nonzero. A common nonzero scaling of the second mask just rescales its measured intensities, so the amplitude normalization can be changed to passive transmissions without changing injectivity or contrast. No stability in noise, higher-sparsity recovery, or phase-only recovery is asserted.

## Proof

**Necessity.** If \(\mathcal P\) has no noncollinear pair, it is contained in \(\{p,-p\}\) for some unit \(p\). A global phase on a mask does not affect intensities, so both masks are effectively real. The two signals \(e_0+i e_h\) and \(e_0-i e_h\) are not related by global phase. For any real diagonal mask with entries \(r_a\), their Fourier values at \(k\) are \(r_0\pm i(-1)^k r_h\) and hence have equal magnitudes. This rules out every collinear alphabet. If both masks have constant amplitude (each with its own constant), then any two unit impulses give the same pair of patterns irrespective of phases. More generally one mask alone is never enough, even without a phase constraint: a zero entry hides the impulse there; otherwise one can scale impulses at different sites to have the same masked modulus. These obstructions do not depend on a choice of decoder.

**Construct the amplitudes independently of the phases.** For \(0\le j<h\) put
\[
L=2h^2+1,\qquad R=2h+1,\qquad B_j=Lj+j^2,\qquad
E_j=RB_j,\qquad E_{j+h}=RB_j+j+1,\qquad M=RB_{h-1}+h+1.
\]
Let \(w_a=(1+\rho)^{E_a/M}\), and take \(m_1(j)=p w_j\), \(m_1(j+h)=q w_{j+h}\). The strict interleaving \(E_j<E_{j+h}<E_{j+1}\) for \(j<h-1\) follows from the group spacing, and \(E_{h-1}<E_{2h-1}=M-1\). Consequently the weights are distinct, lie in \([1,1+\rho)\), and the intervals \([w_j^2,w_{j+h}^2]\) are disjoint.

All \(w_aw_b\) for unordered pairs of distinct physical sites are distinct. To see this, equality of sums of two \(B\)'s, allowing repeated group indices, first forces equality of the sums of group indices: the difference of the two quadratic sums is in absolute value at most \(2(h-1)^2<L\). Equality of the quadratic sums then forces equality of the products of the group indices, hence equality of the unordered group multisets. In \(E_a+E_b\), division by \(R\) recovers the sum of the two \(B\)'s as quotient, since the total of the upper-half offsets is at most \(2h<R\). For different groups \(j,k\), the four possible remainders \(0,j+1,k+1,j+k+2\) are different. For a repeated group \(j\), the physical pair must be \(j,j+h\). This proves uniqueness of \(E_a+E_b\), hence of the amplitude products for any \(\rho>0\).

**Decode the correlations.** Inverse DFT of \(Y_\ell\) yields
\[
C_\ell(d)=\frac1N\sum_k Y_\ell(k)e^{2\pi i kd/N}
=\sum_{a-b\equiv d\;(\mathrm{mod}\ N)}m_\ell(a)\overline{m_\ell(b)}x_a\overline{x_b}.
\]
In particular, \(C_0(0)=\sum_a|x_a|^2\) and \(C_1(0)=\sum_a w_a^2|x_a|^2\). Zero total energy gives the zero signal. For a nonzero one-sparse signal the off-zero correlations vanish, and the ratio of the zero-lag coefficients equals the unique \(w_a^2\) at its site. The two-site cases below have nonzero off-zero information in at least one pattern, so there is no confusion with one-sparse data.

For a nonantipodal two-site signal at \(a,b\), the off-zero lags are \(d=a-b\) and \(-d\), which are distinct. Both flat correlations there are nonzero. The magnitude ratio \(|C_1(d)/C_0(d)|=w_aw_b\) determines the unordered pair without using a phase code. At that pair the zero-lag coefficients determine \(u=|x_a|^2\) and \(v=|x_b|^2\) by \(u+v=C_0(0)\), \(w_a^2u+w_b^2v=C_1(0)\). Normalize the phase so \(x_a=\sqrt u>0\), then \(x_b=C_0(b-a)/\sqrt u\).

For an antipodal pair \(j,j+h\), the only possible off-zero lag is \(h\). Set \(z=x_j\overline{x_{j+h}}\) and \(q/p=e^{i\theta}\). The data at that lag are
\[
C_0(h)=2\operatorname{Re}z,\qquad
C_1(h)=2w_jw_{j+h}\bigl(\cos\theta\operatorname{Re}z+\sin\theta\operatorname{Im}z\bigr).
\]
The two projections are independent because \(\sin\theta\ne0\). Since \(z\ne0\) at a genuine pair, at least one of the two lag values is nonzero. The zero-lag ratio \(C_1(0)/C_0(0)\) is a strict convex combination of \(w_j^2,w_{j+h}^2\), so it locates \(j\) in the unique antipodal interval. The same invertible system recovers the individual squared magnitudes. Then the two projections determine \(z\), so after normalizing \(x_j>0\) one recovers \(x_{j+h}=\overline z/x_j\). This completes the proof for every allowed alphabet, budget and signal.

## Relationship to existing results

The unrestricted optimal pattern count of two is not the distinguishing claim. *Two almost-flat Fourier masks recover every complex two-sparse signal on even cycles* gives the same signal-uniform recovery and the one-mask lower bound, with arbitrarily near-flat passive masks. Its construction uses \(N\) distinct phases and explicitly identifies nonantipodal pairs from distinct phase differences. That guarantee does not enforce a two-level alphabet: collapsing its phase code to two levels removes pair identification by phase alone. Here the amplitude products identify nonantipodal pairs; the two phase levels independently resolve the real/imaginary ambiguity at the antipodal lag. The collinear-alphabet obstruction is already implicit in the known real-mask obstruction and is used here as the necessity half of the alphabet classification.

*Sharp two-mask Fourier recovery of complex two-sparse signals on odd cycles* uses two positive real masks on odd orders and proves the real-mask obstruction at even orders. *Three bounded-contrast Fourier masks resolve every two-sparse even-cycle phase ambiguity* uses a third pattern to resolve the antipodal case. Neither gives the two-pattern theorem with a prescribed two-level phase alphabet. The general coded-diffraction theorems of Bandeira–Chen–Mixon and Huang–Li address recovery from larger families of masks, not this exact phase-alphabet criterion.

The matched records are compared by their mathematical statements, without claiming chronological priority between findings carrying the same date. The decoder uses exact arithmetic; making \(\rho\) small can shrink the gaps between the amplitude codes, and making the two phases nearly collinear makes the antipodal inversion sensitive. Exact recovery is not a dimension-uniform or contrast-uniform noise guarantee.

## Verification

The original finite diagnostic `CHECK.py` is unchanged. Its recorded checks specialize to \(p=1,q=i,\rho=1\); they test the same integer code through \(N=120\) and finite Fourier decoding through \(N=18\). These are not tests of the full phase/budget quantifier. That quantifier follows analytically: positive \(\rho\) makes exponentiation strictly increasing, and the two antipodal projections have determinant proportional to \(\sin\theta\).

## References

1. *Two almost-flat Fourier masks recover every complex two-sparse signal on even cycles*, [published record](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-two-almost-flat-fourier-masks-recover-every-complex-two-sparse-s--d1a29ce552bb).
2. *Sharp two-mask Fourier recovery of complex two-sparse signals on odd cycles*, [published record](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-sharp-two-mask-fourier-recovery-of-complex-two-sparse-signals-on--cead19f36641).
3. *Three bounded-contrast Fourier masks resolve every two-sparse even-cycle phase ambiguity*, [published record](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-three-bounded-contrast-fourier-masks-resolve-every-two-sparse-ev--7705e6fa9c4a).
4. A. S. Bandeira, Y. Chen and D. G. Mixon, *Phase retrieval from power spectra of masked signals*, [arXiv:1303.4458](https://arxiv.org/abs/1303.4458).
5. G. Huang and S. Li, *PhaseLift for Coded Diffraction Patterns: Optimal Sampling Rate*, [arXiv:2608.02450](https://arxiv.org/abs/2608.02450).
