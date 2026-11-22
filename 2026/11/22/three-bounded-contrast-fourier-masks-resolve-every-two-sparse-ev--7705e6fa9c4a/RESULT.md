# Three bounded-contrast Fourier masks resolve every two-sparse even-cycle phase ambiguity

## Finding

**Theorem.** For every even integer \(N=2h\ge4\), put \(\rho=2^{1/N}\), \(q=\rho^2\), and define the three diagonal masks for \(j\in\{0,\ldots,N-1\}\) by
\[
 m_0(j)=1,\qquad m_1(j)=\rho^j,\qquad
 m_2(j)=q^j\exp(\pi i j/N).
\]
For \(\ell\in\{0,1,2\}\) and \(k\in\{0,\ldots,N-1\}\), observe the complete, **unoversampled** Fourier intensity pattern
\[
 Y_\ell(k)=\left|\sum_{j=0}^{N-1}m_\ell(j)x_j\exp(-2\pi i jk/N)\right|^2.
\]
Together, these three patterns uniquely determine **every** complex vector \(x\in\mathbb C^N\) with at most two nonzero coordinates, up to one common unimodular factor. The masks are deterministic and have uniformly bounded nonzero transmission amplitudes, \(1\le |m_\ell(j)|<4\), independently of \(N\). This holds in particular for antipodal support pairs, whose relative imaginary phase cannot be recovered using **any number of real diagonal masks**. No claim is made that three complex masks are necessary among all possible complex-mask designs.

## Assumptions and scope

Coordinates are represented by the integers \(0,\ldots,N-1\), though Fourier differences are reduced modulo \(N\). The masks depend on these chosen representatives. Fourier transforms above are unnormalized; inverse discrete transforms therefore carry a factor \(1/N\). The signal has at most two **complex** nonzero entries, of arbitrary magnitudes and phases, and all \(3N\) scalar intensities are known without error. This is a finite cyclic Fourier-analysis claim (MSC2020 42A38), not a general-signal or stable noisy-recovery theorem. The final complex mask uses a deterministic half-Nyquist phase ramp and strictly positive amplitude profile.

## Proof

**1. Extract the masked cyclic correlations.** Fourier inversion gives, for each \(s\in\mathbb Z/N\mathbb Z\),
\[
 C_\ell(s)=\frac1N\sum_{k=0}^{N-1}Y_\ell(k)e^{2\pi i ks/N}
 =\sum_{t-u\equiv s\ (\mathrm{mod}\ N)}m_\ell(t)\overline{m_\ell(u)}x_t\overline{x_u}.
\]
Denote \(M_\ell=C_\ell(0)\). If \(M_0=0\), the signal is zero. A one-sparse nonzero signal at \(a\) has \(M_1/M_0=q^a\), which uniquely determines \(a\) because \(q>1\); \(M_0\) then gives its magnitude.

For a two-sparse signal at \(0\le a<b<N\), write \(U=|x_a|^2>0\), \(V=|x_b|^2>0\), \(P=x_b\overline{x_a}\ne0\), and \(A=q^a\), \(B=q^b\). The three zero-lag measurements satisfy
\[
 M_0=U+V,\qquad M_1=AU+BV,\qquad M_2=A^2U+B^2V.
\]
The discriminant \(M_0M_2-M_1^2=UV(A-B)^2>0\) separates all genuine two-sparse signals from all one-sparse and zero signals, with no genericity assumptions.

**2. Nonantipodal supports.** Suppose \(b-a\ne h\), and let \(s=b-a\). Then \(s\not\equiv-s\pmod N\), so the masked correlations at \(s\) have only one product term:
\[
 C_0(s)=P,\qquad C_1(s)=\rho^{a+b}P.
\]
Both differences \(s\) and \(-s\) are detected; their ratios are equal and determine the **ordinary integer sum** \(S=a+b\) uniquely. It follows that \(AB=q^S\). The zero-lag identity
\[
 M_2=(A+B)M_1-ABM_0
\]
now recovers \(A+B=(M_2+q^SM_0)/M_1\). Therefore \(A,B\) are the unordered roots of a known quadratic, and their distinct values determine the original support \(\{a,b\}\) uniquely. The nonsingular first two moment equations determine \(U,V\). Finally \(C_0(b-a)=P\) fixes the relative phase; take \(x_a=\sqrt U>0\) and \(x_b=P/\sqrt U\).

A second two-sparse signal with the same data and nonantipodal support must have the same ordinary sum and the same quadratic roots. An antipodal competitor cannot have the same nonzero-lag pattern, since a nonantipodal two-sparse signal has two distinct nonzero-lag entries in \(C_0\).

**3. Antipodal supports: observable real product.** Suppose \(b=a+h\), where necessarily \(0\le a<h\). Since the two cross terms occur at the same cyclic lag \(h\),
\[
 C_0(h)=2\operatorname{Re}P,\quad
 C_1(h)=2\rho^{a+b}\operatorname{Re}P,\quad
 C_2(h)=-2q^{a+b}\operatorname{Im}P.
\]
The last formula follows because \(\exp(\pi i(b-a)/N)=i\), so the two terms at lag \(h\) add as \(iP-i\overline P\). If \(\operatorname{Re}P\ne0\), the ratio \(C_1(h)/C_0(h)=\rho^{2a+h}\) determines \(a\). The two zero-lag equations determine \(U,V\), and the displayed lag equations determine \(\operatorname{Re}P\) and \(\operatorname{Im}P\), hence the signal up to global phase.

**4. Antipodal supports: purely imaginary product.** It remains to rule out two different antipodal supports sharing data when \(\operatorname{Re}P=0\). Put \(R=q^h=2\), \(X=q^a\), and \(t=M_1/M_0\). The support equations in this case are
\[
 M_2=(R+1)X M_1-RX^2M_0,\quad
 U=\frac{RXM_0-M_1}{(R-1)X},\quad
 V=\frac{M_1-XM_0}{(R-1)X}.
\]
The positivity of \(U,V\) gives \(X<t<RX\). Because \(P\) is purely imaginary with \(|P|^2=UV\), the complex-mask lag provides
\[
 |C_2(h)|^2=\frac{4R^2M_0^2}{(R-1)^2}
 X^2(t-X)(RX-t).
\]
If a distinct antipodal support \(a'\) had the same moments, set \(Z=q^{a'}\), and interchange candidates if needed so \(X<Z\). Since both \(a,a'\in\{0,\ldots,h-1\}\), one has \(X<Z<RX\). Subtracting their two quadratic zero-lag equations forces
\[
 t=\frac{R(X+Z)}{R+1}.
\]
Substitution into the two predicted squared nonzero-lag magnitudes yields the **exact, nonzero** difference
\[
 \begin{split}
 &X^2(t-X)(RX-t)-Z^2(t-Z)(RZ-t)\\
 &\qquad=-\frac{R(X-Z)(X+Z)(RX-Z)(X-RZ)}{(R+1)^2}\ne0.
 \end{split}
\]
Every displayed factor is nonzero because \(X<Z<RX\). Thus the observed \(|C_2(h)|^2\) excludes the other support. With \(a\) fixed, recover \(U,V\) and the sign and magnitude of \(\operatorname{Im}P\) from the signed real value \(C_2(h)\). The same phase normalization reconstructs the unique signal. Nonantipodal competitors are impossible: their flat-mask correlations have two nonzero lags, whereas \(C_0\) here has none.

**5. Reality is a genuine obstruction.** For any even \(N\) and any collection of real diagonal masks, consider vectors supported at \(0\) and \(h\) with values \((1,1+i)\) and \((1,1-i)\), respectively. Their intensity patterns agree for every real mask, because the cross term at frequency \(k\) involves only \(2m(0)m(h)(-1)^k\operatorname{Re}(1+i)\). They are not related by global phase. Thus real masks of any cardinality cannot remove this antipodal ambiguity, whereas the explicit third complex mask above does. This proves the theorem and the stated contrast with all-real masks.

## Verification

The standalone `CHECK.py` is a supplementary standard-library numerical/exact-arithmetic checker: run `python3 CHECK.py`. The observed output was `CHECK_OK two_sparse_cases=3678 rational_factor_identities=18 dimensions=4,6,...,20`. It verifies every support pair at nine even dimensions and several magnitudes and relative phases, including purely imaginary antipodal products; also checks singletons and zero signals, and tests the key rational factor identity. The exact argument in the proof, not the finite checker, establishes the all-even-dimension and all-amplitude statements.

## Relationship to prior work

Huang and Li [1] prove a probabilistic \(O(\log N)\)-mask PhaseLift recovery theorem for each fixed arbitrary signal; their Theorem 1 expressly does not provide simultaneous recovery of all signals from one drawn collection, whereas our theorem is deterministic, uniform on the entire two-sparse set, and uses exactly three full Fourier intensity patterns for every even \(N\). An existing published result [2] gives explicit **two real positive masks** for all two-sparse signals in **odd** dimension but explicitly leaves open how complex masks can resolve the even-dimensional antipodal obstruction. Its even-dimensional impossibility is confined to all-real masks. Our three-mask result proves an affirmative, structurally distinct even-dimensional statement, and does not merely restate that odd-dimensional theorem.

Li and Li [3] obtain many random complex masks for general-signal recovery and describe the impossibility of real-mask recovery for even-dimensional complex signals. Jaming and Rathmair [4] establish three-mask phase retrieval on a continuous Fourier domain, but also document that straightforward finite-dimensional analogues can fail; their continuous-space theorem does not imply the present complete unoversampled finite cyclic two-sparse result. These are implication comparisons, not claims that absence of matching titles proves originality.

## Limitations

No stability estimate under noisy or approximate measurements is proved. The exponential attenuation depends on labelled coordinate representatives, and the three full length-\(N\) intensity patterns are required. The theorem says nothing about more than two nonzero coordinates or unrestricted signal recovery. The three-mask count is an explicit sufficient count **not** asserted minimal over arbitrary complex masks. The exact algebra and computational checking do not constitute independent validation. Possible earlier equivalent two-sparse constructions using different mask parametrizations, particularly in full-text versions of older coded-diffraction literature not inspected completely, remain a bibliographic risk.

## References

[1] G. Huang and S. Li, *PhaseLift for Coded Diffraction Patterns: Optimal Sampling Rate*, arXiv:2608.02450, first posted 2026-08-03. https://arxiv.org/abs/2608.02450

[2] *Sharp two-mask Fourier recovery of complex two-sparse signals on odd cycles*, publicly available 2026-11-08, complete theorem and proof. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-two-mask-fourier-recovery-of-complex-two-sparse-signals-on--cead19f36641

[3] H. Li and S. Li, *Phase retrieval from Fourier measurements with masks*, Inverse Problems and Imaging **15** (2021), 1051–1075. https://doi.org/10.3934/ipi.2021028

[4] P. Jaming and M. Rathmair, *Uniqueness of phase retrieval from three measurements*, arXiv:2205.08753 (2022). https://arxiv.org/abs/2205.08753

[5] A. S. Bandeira, Y. Chen and D. G. Mixon, *Phase retrieval from power spectra of masked signals*, arXiv:1303.4458 (2013). https://arxiv.org/abs/1303.4458
