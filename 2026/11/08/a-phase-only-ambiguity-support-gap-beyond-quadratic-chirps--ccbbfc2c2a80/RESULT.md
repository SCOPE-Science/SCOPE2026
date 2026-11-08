# A phase-only ambiguity support gap beyond quadratic chirps

## Finding
For every odd prime \(p\ge5\), a unimodular sequence on \(\mathbb Z_p\) has one of two sharply separated types of periodic self-ambiguity support. The classical minimum of \(p\) points occurs for a quadratic chirp. Every **nonchirp** unimodular sequence satisfies
\[
\boxed{|\operatorname{supp} A_f|\ge 4p-3.}
\]
More precisely, for every nonzero cyclic delay, the Fourier support of its phase-difference sequence has at least four points. All cardinalities strictly between \(p\) and \(4p-3\) are impossible for unimodular self-ambiguity. The latter endpoint is attained for \(p=5\), so the first prime instance is sharp. No assertion of sharpness for every larger prime is made.

## Assumptions and scope
Fix an odd prime \(p\ge5\), write \(\zeta=\exp(2\pi i/p)\), and use counting measure on \(\mathbb Z_p\). Let \(f:\mathbb Z_p\to\mathbb C\) obey \(|f(t)|=1\) for every \(t\). Define its unnormalized periodic ambiguity transform by
\[
A_f(x,k)=\sum_{t\in\mathbb Z_p}f(t)\overline{f(t-x)}\zeta^{-kt},\qquad(x,k)\in\mathbb Z_p^2.
\]
The support is the set of ordered pairs for which the indicated complex number is not zero; multiplying the ambiguity transform by any fixed nonzero normalization leaves the conclusion unchanged. A quadratic chirp means a function of the form \(f(t)=C\zeta^{at^2+bt}\) with \(|C|=1\) and \(a,b\in\mathbb Z_p\).

## Proof
**Unimodular three-frequency obstruction.** Let \(h:\mathbb Z_p\to\mathbb C\) be unimodular, and write its inverse discrete Fourier expansion
\[
h(t)=\sum_{j\in S}c_j\zeta^{jt},\qquad c_j\ne0,
\]
where \(S\) is the exact Fourier support. We claim \(|S|=1\) or \(|S|\ge4\). If \(|S|=2\), the difference of its two elements is uniquely represented as an ordered difference, so the corresponding nonzero Fourier coefficient of \(|h|^2\) is \(c_a\overline{c_b}\ne0\), contradicting \(|h|^2\equiv1\).

If \(|S|=3\), let \(m_d\) count ordered pairs \((a,b)\in S^2\) with \(a-b=d\), for \(d\ne0\). A nonzero difference cannot have three representations, since that would imply \(S+d=S\); as \(d\) generates the prime group, this would make the three-element set \(S\) equal to the full group, impossible for \(p\ge5\). Hence each positive multiplicity is \(1\) or \(2\). If none were \(1\), the six ordered pairs off the diagonal would occupy exactly three distinct nonzero difference values, each with multiplicity two. But \(m_d=m_{-d}\), and for odd \(p\), negation acts without fixed points on nonzero residues; consequently the number of represented differences must be even. Contradiction. Therefore some nonzero difference is uniquely represented; once again its Fourier coefficient \(c_a\overline{c_b}\ne0\) contradicts \(|h|^2\equiv1\). This proves the obstruction for **arbitrary complex phases**, not only root-of-unity phase alphabets.

**Delay rows.** For each \(x\in\mathbb Z_p\), set \(h_x(t)=f(t)\overline{f(t-x)}\). It is unimodular, and \(A_f(x,\cdot)\) is its Fourier transform. Hence every row has either one nonzero coefficient or at least four. The zero-delay row is \(h_0\equiv1\), so it has exactly one.

**Rigidity of a singleton nonzero-delay row.** Suppose a nonzero \(x\) has just one nonzero Fourier coefficient, so \(h_x(t)=c\zeta^{kt}\), with \(|c|=1\). Since \(x\) generates \(\mathbb Z_p\), recurrence along \(t=sx\) yields
\[
f(sx)=f(0)c^s\zeta^{kx\,s(s+1)/2}\qquad(s\in\mathbb Z).
\]
Periodicity at \(s=p\), using oddness of \(p\), forces \(c^p=1\). Thus \(c=\zeta^{\ell}\) for some \(\ell\in\mathbb Z_p\). Replacing \(s\) by \(x^{-1}t\) shows that \(f(t)=C\zeta^{at^2+bt}\) for some \(a,b\in\mathbb Z_p\); hence \(f\) is a quadratic chirp. Conversely, for any such chirp, every \(h_x\) is a scalar character, giving exactly one Fourier coefficient in each of the \(p\) delay rows. This equivalence at the minimum is compatible with the established time-frequency equality classification and is not claimed as new.

If \(f\) is not a quadratic chirp, no nonzero delay can have a singleton row. Every one of those \(p-1\) rows therefore has at least four nonzero coefficients. With the one coefficient at zero delay,
\[
|\operatorname{supp} A_f|=1+\sum_{x\ne0}|\operatorname{supp} A_f(x,\cdot)|\ge1+4(p-1)=4p-3.
\]

**Attainment at \(p=5\).** Let \(f(0)=\zeta\) and \(f(t)=1\) for \(t\ne0\). This is not a quadratic chirp, as its nonzero-delay ambiguity rows are not characters. For every \(x\ne0\),
\[
h_x(t)=1+(\zeta-1)\mathbf1_{\{0\}}(t)+(\zeta^{-1}-1)\mathbf1_{\{x\}}(t).
\]
At frequency \(k=0\), its Fourier coefficient is \(p-2+\zeta+\zeta^{-1}>0\). For \(k\ne0\), the coefficient is
\[
(\zeta-1)+(\zeta^{-1}-1)\zeta^{-kx},
\]
which vanishes precisely when \(kx=-1\pmod p\). Thus each nonzero delay row has exactly \(p-1\) nonzero coefficients, and the entire support has cardinality \(1+(p-1)^2\). At \(p=5\), this equals \(17=4p-3\), proving sharpness there.

## Verification
The self-contained program `verify_support.py` performs exact cyclotomic arithmetic without floating-point zero thresholds. Its output on the packaged program is `PHASE_AMBIGUITY_EXACT_CHECKS_PASS 3443 p5_histogram [(5, 25), (17, 500), (21, 100)]`. It exhausts the 625 five-phase codes modulo global phase at \(p=5\), checks every two- and three-element frequency-support difference configuration for primes \(5,7,11,13\), and checks additional prime-alphabet chirps and perturbations at \(p=7,11\). It is a finite corroboration only; the preceding difference-multiplicity and recurrence arguments establish the all-prime, arbitrary-phase claim.

Reproduce with a standard Python 3 interpreter: `python3 verify_support.py` in the directory containing this document and the program. No external packages or third-party data are needed.

## Relationship to prior work
Nicola's 2022 equality classification identifies all minimally supported short-time Fourier transforms, including the quadratic-chirp behavior in the full-support prime case. The new statement concerns a larger **forbidden interval immediately above** that minimum, restricted to unimodular self-ambiguity rather than general signal-window pairs. Krahmer, Pfander, and Rashkov establish general finite-group short-time Fourier support estimates, but their support-size inequality at full-support inputs gives only the standard \(p\) minimum. A published sharp second-support result gives \(2p\) as the next attainable level for arbitrary signal-window pairs; it does not imply the present stronger \(4p-3\) threshold under the two coupled unimodularity constraints.

Benedetto, Benedetto, and Woodworth investigate periodic ambiguity of unimodular prime-length sequences, notably pointwise magnitude bounds for Björck sequences; their stated results do not classify the support-gap cardinality. Ye and collaborators investigate low-ambiguity-zone magnitudes rather than exact global support counts. These are mathematically adjacent but not logical substitutes for the phase-only self-ambiguity bound.

## Limitations
This is a theorem about exact *zero/nonzero cardinality*, not a lower bound on the magnitudes of the nonzero ambiguity entries. It assumes prime odd length and full unimodularity, and does not extend as stated to arbitrary complex sequences, composite cyclic orders, perturbations or noisy thresholded support. The numerical endpoint \(4p-3\) is shown attainable only for \(p=5\); its optimality for every other odd prime is not claimed. Historical novelty remains provisional: an unindexed general statement about finite unimodular Fourier-sparsity or periodic ambiguity could conceivably imply this support gap.

## References
1. F. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176v1 (first public 29 April 2022), especially Theorem 1.2. https://arxiv.org/html/2204.14176v1
2. F. Krahmer, G. E. Pfander, and P. Rashkov, *Uncertainty in time-frequency representations on finite Abelian groups and applications*, arXiv:math/0611493v1 (2006), especially Proposition 4.4. https://arxiv.org/pdf/math/0611493
3. J. J. Benedetto, R. L. Benedetto, and J. T. Woodworth, *Optimal ambiguity functions and Weil's exponential sum bound*, arXiv:1107.1887v1 (2011), sections 1 and 3. https://arxiv.org/abs/1107.1887
4. Z. Ye et al., *Low Ambiguity Zone: Theoretical Bounds and Doppler-Resilient Sequence Design in Integrated Sensing and Communication Systems*, arXiv:2202.04793v1 (2022). https://arxiv.org/abs/2202.04793
5. *A sharp support gap above the odd-prime short-time Fourier uncertainty minimum* (published mathematical record, 2026), especially the all-pairs second-support theorem and its full-support argument. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-support-gap-above-the-odd-prime-short-time-fourier-uncer--c42ba46f36bb
