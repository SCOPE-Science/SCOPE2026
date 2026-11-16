# Weighted two-tap affine wavelets: exact prime-cycle tightness and scale-erasure spectra

## Finding
Let \(p\ge3\) be an odd prime, \(d\in\mathbb F_p^\times\), and \(a,b\in\mathbb C\setminus\{0\}\). Write \(g=a\delta_0+b\delta_d\). For nonnegative weights \(w_s\), not all zero, form the weighted collection of **all translations** of each scale, \(\mathcal W=\{\sqrt{w_s}T_kD_sg:k\in\mathbb F_p,\ s\in\mathbb F_p^\times,\ w_s>0\}\). Set \(u=\operatorname{Re}(a\overline b)\), \(v=\operatorname{Im}(a\overline b)\), \(Q=|a|^2+|b|^2\), and \(W=\sum_s w_s\).

**Exact classification.** The orthogonal projections of \(\mathcal W\) to the mean-zero subspace \(H_0=\{f:\sum_x f(x)=0\}\) form a tight frame precisely in the following mutually exclusive situations:

1. \(u=0\): every antipodal pair has equal weights, \(w_s=w_{-s}\). Its frame bound is \(WQ\).
2. \(v=0\): the sum \(w_s+w_{-s}=\gamma\) is independent of the pair. Its frame bound is \(WQ-u\gamma\).
3. \(uv\ne0\): all weights equal the same positive constant \(w\). Its frame bound is \(WQ-2uw\).

The original vectors, without projection, form a tight frame of the **entire** \(\ell^2(\mathbb F_p)\) precisely in case 1, with bound \(WQ\). These are statements about positive tight bounds, not merely a scalar frame operator with zero scalar.

**Unweighted designs.** For a nonempty set \(A\subseteq\mathbb F_p^\times\) and weights \(w_s=\mathbf1_A(s)\), the mean-zero criterion is exactly: \(A\) is the full multiplicative group, or \(u=0\) and \(A=-A\), or \(v=0\) and \(A\) contains exactly one element from each pair \(\{s,-s\}\). In particular, for the real zero-mean difference generator \(g=\delta_0-\delta_d\), the smallest tight mean-zero dilation sets have cardinality \((p-1)/2\). They are precisely the \(2^{(p-1)/2}\) antipodal transversals. A **multiplicative subgroup** can be one of these minimizers exactly when \(p\equiv3\pmod4\); then the unique candidate, the quadratic-residue subgroup, works.

**Exact scale-packet erasure.** If \(A\) is any such transversal, replace the generator by \(g=(\delta_0-\delta_d)/\sqrt p\). Then \(\mathcal W\) is Parseval on \(H_0\). Delete the entire collection of \(p\) translates at any one \(s\in A\). For \(p\ge5\), the remaining system is a frame on \(H_0\) with **sharp**, attained bounds
\[
L_p=\frac{p-2-2\cos(\pi/p)}p,\qquad U_p=\frac{p-2+2\cos(2\pi/p)}p.
\]
These bounds do not depend on the transversal, erased scale, or nonzero tap separation. For \(p=3\), the sole scale is erased and both bounds are zero.

## Assumptions and scope
All group arithmetic is modulo the specified odd prime. The space \(\ell^2(\mathbb F_p)\) has the counting-measure inner product. Define \(T_k f(x)=f(x-k)\) and \(D_s f(x)=f(s^{-1}x)\); each is unitary. Weights attach to dilations, not translations, and all \(p\) translations at each retained scale must be present. An unweighted scale set means the displayed zero-one weights. The frame bound of the projected family on \(H_0\) is exactly its Rayleigh quotient on that subspace. The full-space assertion uses the unprojected atoms.

## Proof
Use the unitary discrete Fourier transform \(\widehat f(\xi)=p^{-1/2}\sum_x f(x)\zeta^{-\xi x}\), where \(\zeta=e^{2\pi i/p}\). Plancherel and orthogonality of all translations give, for every \(f\),
\[
\sum_{s,k}w_s|\langle f,T_kD_sg\rangle|^2
=\sum_{\xi\in\mathbb F_p}\Lambda(\xi)|\widehat f(\xi)|^2,
\quad
\Lambda(\xi)=\sum_s w_s\big|a+b\zeta^{-sd\xi}\big|^2.
\]
Writing \(c=a\overline b=u+iv\), expansion yields
\[
\Lambda(\xi)=WQ+\sum_{t\ne0}h(t)\zeta^{t\xi},
\qquad h(ds)=c w_s+\overline c w_{-s},\quad h(0)=0.
\]
The Fourier series has \(\Lambda(\xi)\) constant for all \(\xi\ne0\) **if and only if** \(h(t)\) is one common real number \(\beta\) for all \(t\ne0\): inverse Fourier transformation gives \(h(t)=(\Lambda(0)-\Lambda(\xi\ne0))/p\). Conversely, a constant \(h(t)=\beta\) gives \(\sum_{t\ne0}\zeta^{t\xi}=-1\) for nonzero frequency, hence bound \(WQ-\beta\). For each antipodal pair,
\[
h(ds)=u(w_s+w_{-s})+iv(w_s-w_{-s}),\qquad
h(-ds)=u(w_s+w_{-s})-iv(w_s-w_{-s}).
\]
These are a common real constant precisely when \(v(w_s-w_{-s})=0\) for every pair and \(u(w_s+w_{-s})\) is independent of the pair. Since \(c\ne0\), these equations yield the three mutually exclusive alternatives and their stated bounds. All bounds are positive: a nonzero pair of coefficients satisfies \(Q\ge2|u|\); in the second case \(W=(p-1)\gamma/2\), \(\gamma>0\), while in the third case \(W=(p-1)w\), \(w>0\). For the full space, constancy also at \(\xi=0\) requires \(h(t)=0\) for every nonzero \(t\) because \(h(0)=0\). The pair equations force \(u=0\) and \(w_s=w_{-s}\), and conversely those conditions work.

With zero-one weights, the second case has \(\gamma\in\{1,2\}\) because the weights are nonzero somewhere; \(\gamma=1\) gives the antipodal transversals and \(\gamma=2\) the full set. The first case means exact antipodal symmetry. The third forces the full set. This proves the unweighted classification. For \(g=\delta_0-\delta_d\), \(u=-1\), \(v=0\), and a transversal has exactly one of each of the \((p-1)/2\) pairs, proving cardinality and count. A multiplicative subgroup of order \((p-1)/2\) is necessarily the subgroup of quadratic residues. It is an antipodal transversal precisely when \(-1\) is a quadratic nonresidue, namely \(p\equiv3\pmod4\).

For the normalized generator \(a=1/\sqrt p\), \(b=-1/\sqrt p\), a transversal has \(W=(p-1)/2\), \(Q=2/p\), \(u=-1/p\), and \(\gamma=1\). Hence the mean-zero tight bound is \(1\). Removing one scale leaves at every \(\xi\ne0\)
\[
\Lambda_{\rm erased}(\xi)=1-\frac{|1-\zeta^{-sd\xi}|^2}{p}=1-\frac{2-2\cos(2\pi sd\xi/p)}p.
\]
Since \(sd\ne0\), multiplication by \(sd\) permutes nonzero residues. The maximum cosine is \(\cos(2\pi/p)\), attained at residues \(\pm1\), and the minimum is \(-\cos(\pi/p)\), attained at residues \((p\pm1)/2\). These give the **attained**, sharp upper and lower bounds. The lower bound is positive for \(p\ge5\) and zero for \(p=3\). This completes every asserted classification and boundary case.

## Verification
The accompanying standalone script `verify_wavelet_two_tap.py` can be run with `python3 verify_wavelet_two_tap.py` using only Python's standard library. It exhausts 6,624 unweighted phase/support examples for primes \(3,5,7,11\) and 4,896 nonnegative integer-weighted examples for primes \(3,5,7\). It also independently assembles the actual time-domain frame matrix at prime \(7\), and checks the exact erasure endpoints at primes \(3,5,7,11,13,17\). Its final assertion prints `TWO_TAP_AFFINE_PASS unweighted_cases=6624 weighted_cases=4896`. The proof, rather than these finite tests, establishes the theorem uniformly for all odd primes and admissible complex coefficients and weights.

## Relationship to prior work
Rahimi and Seddighi's 2017 works develop finite-prime wavelet frame coefficients, subgroup-based frame criteria, and construction of equal-norm Parseval systems. The present result specializes to time-domain two-point generators but allows **arbitrary** nonnegative dilation weights, and gives a simultaneous necessity-and-sufficiency classification separating complex phase, antipodal scale balancing, and full-space versus mean-zero tightness. Iosevich, Lai, and Mayeli (2017) consider tight finite wavelet frame sets from Fourier-indicator generators and frequency tilings; their hypotheses are different from the two-point time-domain generator considered here. The subgroup case and Fourier diagonalization are classical inputs, not claimed as new.

## Limitations
The classification assumes an odd **prime** modulus, two nonzero taps, all translations at every retained dilation, and nonnegative dilation weights. It does not classify incomplete translation sets, multi-tap generators, arbitrary composite cycles, or nonlinear erasures. One-scale-erasure bounds are for the normalized real-difference tight transversal on the mean-zero subspace; they are not full-space frame bounds. A specialist equivalence under filter-bank or Calderón-sum terminology remains a historical-priority risk; an earlier subgroup-frame formula alone does not supply the arbitrary-weight classification and packet-erasure endpoints stated here. Independent verification of novelty is not established.

## References
1. A. Rahimi and N. Seddighi, *A Constructive Approach to the Finite Wavelet Frames over Prime Fields*, arXiv:1703.05012 (first public version 2017-03-15).
2. A. Rahimi and N. Seddighi, *Finite equal norm Parseval Wavelet Frames over Prime Fields*, arXiv:1705.11127 (first public version 2017-05-30).
3. A. Iosevich, C.-K. Lai, and A. Mayeli, *Tight Wavelet Frame Sets in Finite Vector Spaces*, arXiv:1703.06842 (first public version 2017-03-20).
4. A. Ghaani Farashahi, *Structure of finite wavelet frames over prime fields*, Bulletin of the Iranian Mathematical Society 43 (2017), 109–120. The publicly accessible abstract was inspected; its complete text was not independently assessed here.
