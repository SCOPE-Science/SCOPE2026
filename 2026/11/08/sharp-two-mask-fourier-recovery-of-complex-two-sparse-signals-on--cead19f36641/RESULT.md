# Sharp two-mask Fourier recovery of complex two-sparse signals on odd cycles

## Finding

**Theorem (exact deterministic identification and parity obstruction).** Fix an odd integer \(n\geq 3\) and any contrast bound \(R>1\). There are two explicitly specified, strictly positive real diagonal masks, with every transmission between \(R^{-1}\) and \(1\), whose two complete, unoversampled discrete Fourier intensity patterns identify **every** complex vector with at most two nonzero coordinates, up to multiplication by one constant of modulus one. Specifically, for indices \(j\in\{0,\ldots,n-1\}\), take
\[
 m_0(j)=1,\qquad m_1(j)=R^{j/(n-1)-1}.
\]
For \(\ell\in\{0,1\}\) and \(k\in\{0,\ldots,n-1\}\), measure
\[
 Y_\ell(k)=\left|\sum_{j=0}^{n-1}m_\ell(j)x_j e^{-2\pi i jk/n}\right|^2.
\]
The resulting map is injective modulo global phase on the entire at-most-two-sparse class; an exact reconstruction procedure follows below. No **single** diagonal-mask complete Fourier intensity pattern can have this property, even on the one-sparse subclass.

In contrast, for every even \(n\geq4\), **no family of real diagonal masks, of any cardinality**, identifies all complex vectors with at most two nonzero coordinates from its Fourier intensities. This latter parity obstruction is included to delimit the positive result; it is not claimed as a previously unknown impossibility phenomenon.

## Assumptions and scope

The indices form the cyclic group \(\mathbb Z/n\mathbb Z\), but the chosen attenuation profile uses their displayed representatives \(0,\ldots,n-1\). Thus the attenuation mask is not required to be a group character or a periodically geometric function across the wraparound. Fourier transforms are unnormalized, so the inverse intensity transform includes the factor \(1/n\). Every measurement is exact, and \(R>1\) is fixed before observing the signal. There is no assumption on the locations, magnitudes or phases of the at most two nonzero entries. A zero signal is included. No noise-stability or approximate-sparsity claim is made.

## Proof

**Step 1: Fourier intensity gives the cyclic autocorrelation.** For each mask define
\[
 C_\ell(h)=\frac1n\sum_{k=0}^{n-1}Y_\ell(k)e^{2\pi ikh/n}
 =\sum_{t-s\equiv h\pmod n}m_\ell(t)m_\ell(s)x_t\overline{x_s}.
\]
Both masks are real and positive. For a one-sparse nonzero input supported at \(u\), every nonzero lag vanishes, and
\[
 C_0(0)=|x_u|^2,\qquad
 \frac{C_1(0)}{C_0(0)}=R^{2u/(n-1)-2}.
\]
Because \(R>1\), this ratio uniquely determines \(u\); the first equality then determines \(|x_u|\). If all intensity data vanish, the signal is zero.

**Step 2: a nonzero two-sparse signal identifies its support.** Suppose the support consists of distinct \(u,v\in\{0,\ldots,n-1\}\). The only nonzero nonzero-lag autocorrelations occur at \(h\equiv v-u\) and \(-h\). As \(n\) is odd, these lags differ, and
\[
 C_0(v-u)=x_v\overline{x_u}\ne0,\qquad
 \frac{C_1(v-u)}{C_0(v-u)}=m_1(u)m_1(v)
 =R^{(u+v)/(n-1)-2}.
\]
The same ratio appears at the opposite lag. Its real positive value uniquely determines the **ordinary integer sum** \(s=u+v\). The two observed nonzero lags give the unordered residue pair \(\{h,-h\}\). Since \(2\) is invertible modulo the odd integer \(n\), the simultaneous relations \(u+v\equiv s\pmod n\) and \(v-u\equiv h\pmod n\) determine an unordered pair uniquely. Indeed, exchanging \(h\) and \(-h\) merely exchanges the two roots. Taking their unique representatives in \(\{0,\ldots,n-1\}\) recovers the precise support \(\{u,v\}\). This also separates the two-sparse stratum from the one-sparse stratum, for the former has nonzero-lag autocorrelation.

**Step 3: the two magnitudes and relative phase are recovered.** Order the recovered indices so that \(u<v\). Set \(A=|x_u|^2\), \(B=|x_v|^2\). The two zero-lag equations are
\[
 A+B=C_0(0),\quad m_1(u)^2 A+m_1(v)^2 B=C_1(0).
\]
Their determinant is nonzero because the attenuation values are strictly increasing, hence \(A,B\) are individually determined. Choose the representative \(x_u=\sqrt A>0\), and recover \(x_v=C_0(v-u)/\sqrt A\). This determines the original vector modulo its sole unavoidable global phase.

**Step 4: one mask is never sufficient.** Let \(m\) be any complex diagonal mask and assume \(n\ge3\). If some coordinate of \(m\) vanishes, a nonzero impulse there and the zero signal have identical measurements. If every coordinate is nonzero, choose distinct \(u,v\) and nonzero impulses at these positions, with their amplitudes adjusted so that the masked impulses have equal modulus. Their single-mask Fourier intensities coincide at every frequency, although the two signals are not related by global phase. Thus at least two complete patterns are necessary even on the one-sparse subclass.

**Step 5: the even-order obstruction for real masks.** If \(n\) is even, fix any \(u\) and put \(v=u+n/2\pmod n\). Consider two signals with values \((x_u,x_v)=(1,1+i)\) and \((x'_u,x'_v)=(1,1-i)\). They cannot differ by a global phase. For any real mask \(m\), their Fourier intensity at each frequency is
\[
 |m(u)|^2+2|m(v)|^2+2m(u)m(v)(-1)^k,
\]
which is the same for both signals. Hence no number of real masks can uniformly recover the even-cycle two-sparse class. This establishes exactly the stated parity boundary.

## Verification

Run `python3 CHECK.py` in an environment with NumPy (`requirements.txt`). The finite checker computes both complete intensity patterns and their inverse DFTs, executes explicit recovery on randomly phased two-sparse vectors, checks every one-sparse support, exhaustively checks uniqueness of the support signatures for each tested odd order, and tests the even-order counterexample against independent random real masks. Its successful output is:

`CHECK_OK phase_recovery_tests=2866 exact_support_signatures=905`

The analytic argument above, not the finite experiments, proves all unbounded quantifiers over odd and even dimensions and all nonzero complex coefficients.

## Relationship to prior work

The recent full-dimensional PhaseLift result of Huang and Li [1] uses on the order of the logarithm of the ambient dimension in random masks to recover arbitrary complex signals. The present statement concerns the much smaller two-sparse stratum and gives two deterministic, positive, bounded-contrast masks and an elementary exact autocorrelation decoder, without claiming to solve unrestricted full-signal retrieval. Bandeira, Chen and Mixon [2] consider power spectra of masked signals and general identifiability constructions. Jaganathan, Eldar and Hassibi [3] study two specific masks in an oversampled measurement model and generic recovery, not the present complete unoversampled two-sparse guarantee. Ranieri et al. [4] analyze uniqueness for unmasked sparse phase retrieval up to additional shift/flip ambiguities. Guerrero, Pinilla and Arguello [5] study designed coded apertures and sparsity-dependent estimation using different acquisition and recovery guarantees. Real-mask parity obstructions for broader complex-signal classes are also discussed by Li and Li [6]; the even-case example here is a boundary illustration, not a separate novelty claim.

## Limitations

Measurements are exact and both full length-\(n\) intensity patterns are assumed known. Reconstruction can be poorly conditioned as \(R\) approaches \(1\), when one coefficient is very small, or when data are noisy. The result makes no claim for three or more nonzero coefficients or about minimal scalar intensity samples under arbitrary (non-Fourier) designs. The limitation to real diagonal masks in the negative even-order statement is essential; the proof does not rule out two or more complex-valued masks in even dimensions. The closest masked-Fourier article by Li and Li [6] was available through its abstract and bibliographic page but not its complete proof text, leaving possible unrecognized overlap. An earlier unindexed equivalent two-sparse construction is possible.

## References

[1] G. Huang and S. Li, *PhaseLift for Coded Diffraction Patterns: Optimal Sampling Rate*, arXiv:2608.02450 (first posted 2026-08-03). https://arxiv.org/abs/2608.02450

[2] A. S. Bandeira, Y. Chen and D. G. Mixon, *Phase retrieval from power spectra of masked signals*, arXiv:1303.4458 (2013). https://arxiv.org/abs/1303.4458

[3] K. Jaganathan, Y. C. Eldar and B. Hassibi, *Phase Retrieval: An Overview of Recent Developments*, arXiv:1510.07713 (2015), particularly the masked recovery discussion. https://arxiv.org/abs/1510.07713

[4] J. Ranieri, A. Chebira, Y. M. Lu and M. Vetterli, *Phase retrieval for sparse signals: Uniqueness conditions*, arXiv:1308.3058 (2013). https://arxiv.org/abs/1308.3058

[5] A. Guerrero, S. Pinilla and H. Arguello, *Phase Recovery Guarantees From Designed Coded Diffraction Patterns in Optical Imaging*, IEEE Transactions on Image Processing **29** (2020), 5687–5697. https://doi.org/10.1109/TIP.2020.2985208

[6] H. Li and S. Li, *Phase retrieval from Fourier measurements with masks*, Inverse Problems and Imaging **15** (2021), 1051–1075. https://doi.org/10.3934/ipi.2021028
