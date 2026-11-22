# Two almost-flat Fourier masks recover every complex two-sparse signal on even cycles

## Finding

**Theorem (sharp number of unoversampled coded Fourier patterns, all even lengths).** For every even integer \(N=2m\ge 2\) and every \(0<\varepsilon,\delta\le 1/2\), the following **two explicitly specified masks** recover *every* vector \(x\in\mathbb C^N\) having at most two nonzero coordinates, up to global phase, from two complete length-\(N\) Fourier intensity patterns. One mask is flat; the other has strictly passive transmissions and can be arbitrarily close to flat in amplitude and phase. No single diagonal mask has this recovery property, even for one-sparse inputs.

Use representatives \(0,\ldots,N-1\), and for \(0\le j<m\) put
\[
 u_j=1-\varepsilon+\frac{2\varepsilon j}{N},\qquad
 u_{j+m}=1-\varepsilon+\frac{\varepsilon(2j+1)}{N},
 \qquad \phi_a=\frac{\delta 2^a}{2^N}\quad(0\le a<N).
\]
The masks are \(w^{(0)}_a=1\) and \(w^{(1)}_a=\sqrt{u_a}\,e^{i\phi_a}\), with measurement patterns
\[
 Y_\ell(k)=\left|\sum_{a=0}^{N-1}w^{(\ell)}_a x_a e^{-2\pi i ka/N}\right|^2,
 \qquad \ell\in\{0,1\},\quad 0\le k<N.
\]
Both masks are known before observation. They satisfy \(\sqrt{1-\varepsilon}\le |w^{(1)}_a|<1\) and \(0<\arg w^{(1)}_a\le\delta/2\). In particular, \(\max_a|w^{(1)}_a-1|\to0\) as \(\varepsilon,\delta\downarrow0\) for every fixed \(N\).

## Assumptions and scope

The signal has zero, one or two nonzero complex coordinates and need not have known support, phase or amplitude. The measurements are exact squared moduli of **unoversampled** discrete Fourier transforms (\(N\) samples per mask); no zero-padding or generic-support assumption is made. Recovery means uniqueness modulo multiplication by one common number of modulus one. The endpoints \(\varepsilon=0\) and \(\delta=0\) are excluded. There is no assertion of noise stability, uniform condition numbers, recovery for three-sparse inputs or uniqueness from fewer than \(N\) frequencies per mask.

## Proof

**Autocorrelation inversion.** Inverse-transform each intensity pattern as
\[
 C_\ell(h)=\frac1N\sum_{k=0}^{N-1}Y_\ell(k)e^{2\pi i kh/N}
 =\sum_{a-b\equiv h\pmod N}w^{(\ell)}_a\overline{w^{(\ell)}_b}x_a\overline{x_b}.
\]
Thus \(C_0(0)=\sum_a|x_a|^2\) and \(C_1(0)=\sum_a u_a|x_a|^2\). The \(N\) numbers \(u_a\) are distinct, since their ordered values are exactly \(1-\varepsilon+\varepsilon q/N\) for \(q=0,\ldots,N-1\), though displayed in antipodal-pair order.

**Binary-difference phase code.** The differences \(2^a-2^b\) are distinct as \((a,b)\) runs over ordered pairs with \(a\ne b\). For positive differences, the \(2\)-adic valuation recovers \(b\) and then \(a\); for negative differences interchange the indices. Since all phase differences \(\phi_a-\phi_b\) lie strictly between \(-1/2\) and \(1/2\), exponentiation \(e^{i(\phi_a-\phi_b)}\) is injective on those differences. Therefore the products \(w^{(1)}_a\overline{w^{(1)}_b}\) uniquely identify **every ordered pair of distinct indices**, through their arguments alone. Moreover, each such product has nonzero imaginary part because its argument is nonzero and has magnitude below \(1/2\).

**Zero- and one-sparse cases.** Both measured patterns vanish precisely for the zero vector. If a nonzero signal is one-sparse at \(a\), then all nonzero lags vanish and the ratio \(C_1(0)/C_0(0)=u_a\) determines its unique site; \(C_0(0)\) determines its modulus. Conversely, a genuinely two-sparse signal cannot have every nonzero lag vanish: for distinct sites with non-antipodal difference, \(C_0\) has a nonzero off-zero coefficient; for antipodal sites, the two observed lag coefficients cannot simultaneously vanish by the nonreal cross-mask product shown below.

**Non-antipodal two-site case.** If the support is \(\{a,b\}\) with \(a-b\not\equiv N/2\pmod N\), the two off-zero lag coefficients are at \(a-b\) and \(b-a\), which are different, and at the former lag
\[
 C_0(a-b)=x_a\overline{x_b}\ne0,\qquad
 \frac{C_1(a-b)}{C_0(a-b)}=w^{(1)}_a\overline{w^{(1)}_b}.
\]
The binary-difference code identifies the ordered support \((a,b)\) uniquely, even if other unordered pairs have the same cyclic difference. The invertible two-by-two system
\[
 |x_a|^2+|x_b|^2=C_0(0),\qquad
 u_a|x_a|^2+u_b|x_b|^2=C_1(0)
\]
recovers both energy levels. The complex off-zero coefficient recovers their relative phase, and hence the signal up to global phase.

**Antipodal two-site case.** The only off-zero lag is \(m\); write the support uniquely as \(\{j,j+m\}\) with \(0\le j<m\). Set \(A=|x_j|^2>0\), \(B=|x_{j+m}|^2>0\), and \(z=x_{j+m}\overline{x_j}\ne0\). The zero-lag ratio is
\[
 \frac{C_1(0)}{C_0(0)}=\frac{u_jA+u_{j+m}B}{A+B}\in(u_j,u_{j+m}).
\]
The \(m\) open intervals \((u_j,u_{j+m})\) are pairwise disjoint: for consecutive indices, \(u_{j+m}<u_{j+1}\). This identifies the support pair from its zero-lag ratio alone. The same invertible energy equations yield \(A,B\). At the self-inverse lag,
\[
 C_0(m)=2\operatorname{Re}(z),\qquad
 C_1(m)=2\operatorname{Re}(q_j z),\qquad
 q_j=w^{(1)}_{j+m}\overline{w^{(1)}_j}.
\]
Since \(\operatorname{Im}(q_j)\ne0\), these are linearly independent real projections of the unknown complex number \(z\), and determine both its real and imaginary parts. Consequently the relative phase is also recovered. This resolves precisely the even-order phase collision that persists under any collection of real diagonal masks.

**Mask minimality.** For an arbitrary single diagonal mask \(w\), if some entry vanishes, a nonzero impulse at that site is invisible. Otherwise, for two different sites \(a,b\), choose nonzero one-sparse impulses scaled so that their masked amplitudes \(|w_a x_a|\) and \(|w_b x_b|\) agree. Their complete Fourier intensity patterns are the same constant sequence, although their supports differ. One pattern can never suffice; the two-pattern construction is therefore sharp. This proves the theorem.

## Verification

Run `python3 CHECK.py` after installing `requirements.txt`. The program directly simulates both complete Fourier intensity patterns, inverse Fourier autocorrelations, site selection and coefficient recovery. For dimensions \(N=2,\ldots,17\), it tests all support sets of size at most two with three randomly selected nonzero complex amplitudes each (2,952 test signals), verifies the distinct binary-power differences, the disjoint antipodal amplitude intervals, and recovery up to global phase. A successful replay prints:

`PASS 2952 signal_reconstructions, n=2..17; all ordered binary differences distinct`

The universal conclusion follows from the preceding algebra and interval arguments, **not** from these finite tests. The test range includes odd dimensions as a supplemental arithmetic stress test; the theorem asserted here is for even \(N\).

## Relationship to prior work

Bandeira, Chen and Mixon [1], inspected through its full open HTML manuscript (especially Sections 1–3), give general polarization-based masked Fourier recovery using order-logarithmic numbers of masks, not a two-pattern theorem on the complete two-sparse even-cycle class. Li and Li [2] address random masks, with polylogarithmic counts for unrestricted complex signals, and discuss real-mask obstructions in even dimension. Their published abstract and article metadata were accessible, but the full proof text was not, so unobserved specialized overlap remains possible. Jaganathan, Eldar and Hassibi [3] give two *oversampled* masks for almost-all-signal recovery (or five unoversampled), which neither implies a uniform two-unoversampled-pattern guarantee on all two-sparse even-order signals nor has the present near-flat explicit construction.

A closely matching earlier published two-sparse claim [4] proves two positive real masks suffice at odd cyclic lengths, and explains the even-length impossibility for *real* masks. Its accessible full theorem explicitly does **not** settle what two complex masks can do at even lengths. The present construction uses a small complex phase code to recover the missing self-inverse-lag quadrature and orders the antipodal amplitude intervals to identify their supports. The odd-length result is background, not a new claim here.

## Limitations

The result assumes noiseless full-length intensities; quantitative conditioning deteriorates as the phase or amplitude contrast approaches zero, and near-zero signal entries also undermine stable support identification. The theorem gives a deterministic exact decoder, not an efficient or robust estimator in noise. It does not claim that every pair of near-flat masks succeeds, nor that this is the first possible construction without a full historical audit. Full access to one relevant 2021 masked-Fourier paper was unavailable; the originality comparison with that paper uses only its verifiable published abstract and metadata.

## References

[1] A. S. Bandeira, Y. Chen and D. G. Mixon, *Phase retrieval from power spectra of masked signals*, arXiv:1303.4458v2 (2013). https://arxiv.org/html/1303.4458v2

[2] H. Li and S. Li, *Phase retrieval from Fourier measurements with masks*, *Inverse Problems and Imaging* **15** (2021), 1051–1075; first online 2021-05-11. https://doi.org/10.3934/ipi.2021028

[3] K. Jaganathan, Y. C. Eldar and B. Hassibi, *Phase retrieval with masks using convex optimization*, IEEE ISIT (2015), 1655–1659. https://doi.org/10.1109/ISIT.2015.7282737

[4] *Sharp two-mask Fourier recovery of complex two-sparse signals on odd cycles*, published mathematical record, 2026-11-08, identifier `cead19f36641`. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-two-mask-fourier-recovery-of-complex-two-sparse-signals-on--cead19f36641
