# Sharp parity liminf constants for geometric cyclic Gabor ambiguity

## Finding
Let \(a=\log 2\), \(\vartheta=\arctan(3/4)\), and, for each integer \(N\ge2\), put
\[
\gamma_N=\exp\!\left(\frac{a+i\pi/2}{N}\right),\qquad
v_N(j)=\frac{\gamma_N^j}{\left(\sum_{t=0}^{N-1}|\gamma_N|^{2t}\right)^{1/2}}\quad(0\le j<N).
\]
On \(\mathbb Z/N\mathbb Z\), let \(T_k f(j)=f(j-k\bmod N)\), \(M_\ell f(j)=e^{2\pi i\ell j/N}f(j)\), and define the normalized ambiguity margin
\[
\alpha_N=\min_{0\le k,\ell<N}|\langle v_N,M_\ell T_kv_N\rangle|,
\]
where the Hermitian inner product conjugates the first entry. Then the **sharp parity-subsequence lower envelopes** are
\[
\boxed{\liminf_{\substack{N\to\infty\\N\ \mathrm{odd}}}N^2\alpha_N
=\frac{10}{9}\sqrt{\frac52}(\log2)^2
=0.844069907041\ldots}
\]
and
\[
\boxed{\liminf_{\substack{N\to\infty\\N\ \mathrm{even}}}N^2\alpha_N
=\frac{20}{9}(\log2)^2
=1.067673364262\ldots.}
\]
In particular, \(N^2\alpha_N\) has no limit as \(N\to\infty\). Both constants are attained as limits along explicitly described infinite subsequences of the indicated parity. These are **liminf results, not assertions of convergence along either entire parity class**.

## Assumptions and scope
The window uses the principal complex exponential with \(\gamma_N^N=2i\), not an arbitrary root of \(2i\). Every ambiguity coefficient is computed with the counting-measure \(\ell^2\) inner product and a unit-norm window. The modulation and translation indices run over all \(N^2\) pairs, with the above cyclic wrap-around convention; the absolute value makes the usual conjugation convention immaterial. The problem is the exact dimension-asymptotic lower envelope for this fixed seed, not an optimization over arbitrary Gabor windows or over perturbations of this seed.

## Proof
**1. Exact starting identity.** Define \(r_N=e^{a/N}\), \(u_\ell=r_N^2e^{2\pi i\ell/N}\), and \(w=(8+6i)/5=2e^{i\vartheta}\). Since \(\gamma_N^N=2i\), the normalization sum equals \(\sum_{j=0}^{N-1}r_N^{2j}=3/(r_N^2-1)\). Splitting the cyclic ambiguity sum at the wrap point \(j=k\), and summing the resulting two geometric progressions, gives
\[
\langle v_N,M_\ell T_kv_N\rangle
=\frac{\gamma_N^{-k}(1-2i)(r_N^2-1)}{3}
\frac{u_\ell^k-w}{1-u_\ell}
\]
up to an irrelevant unit-modulus factor depending only on the inner-product convention. Consequently, **without any asymptotic approximation**,
\[
\boxed{\displaystyle
|\langle v_N,M_\ell T_kv_N\rangle|
=\frac{\sqrt5}{3}e^{-ak/N}(e^{2a/N}-1)
\frac{|u_\ell^k-w|}{|1-u_\ell|}.\tag{1}}
\]
The denominator is nonzero since \(|u_\ell|=e^{2a/N}>1\). Formula (1) may also be derived by the geometric-series identity for general complex geometric cyclic windows.

**2. Localization of all near-minimizers.** Select \(k\) within one unit of \(N/2\), and select a modulation index of the required parity within bounded distance of the corresponding continuous phase-resonance target specified below. Formula (1) shows \(\alpha_N\le C N^{-2}\) for an absolute \(C\) in both parity classes. Now take any minimizing pair \((k_N,\ell_N)\). Since \(0\le k_N<N\), the prefactor \(e^{-ak_N/N}(e^{2a/N}-1)\) is bounded below by a positive constant times \(N^{-1}\), while \(|1-u_{\ell_N}|\le1+e^{2a/N}\) is uniformly bounded. Hence \(|u_{\ell_N}^{k_N}-w|=O(N^{-1})\). Taking moduli and logarithms yields
\[
\left|e^{2ak_N/N}-2\right|=O(N^{-1})
\quad\Longrightarrow\quad h_N:=k_N-N/2=O(1).\tag{2}
\]
For any sequence along which \(N^2\alpha_N\) approaches its parity liminf, pass to a subsequence on which the bounded half-integers \(h_N\) are equal to a fixed \(h\), \(\ell_N\) have fixed parity, and \(s_N=\ell_N/N\to s\in[0,1]\). The phase equation forced by \(u_{\ell_N}^{k_N}\to w\) is
\[
(-1)^{\ell_N}e^{2\pi i h s}=e^{i\vartheta}.\tag{3}
\]
In particular \(s\) is neither \(0\) nor \(1\) in a valid resonance with the small \(h\)'s occurring below. A general lower bound, valid even at endpoint \(s\), follows by combining the radial reverse triangle inequality with (1):
\[
\liminf N|u_{\ell_N}^{k_N}-w|
\ge \lim N\left|e^{2ak_N/N}-2\right|=4a|h|,
\]
so, if \(s\in(0,1)\),
\[
\liminf N^2\alpha_N\ge
\frac{2a\sqrt{5/2}}3\,
\frac{4a|h|}{2|\sin(\pi s)|}.\tag{4}
\]
For \(s=0\) or \(1\), the same lower bound via \(|1-u_{\ell_N}|\le 2+o(1)\) suffices to exclude the large \(|h|\) cases; \(h=0\) is excluded by (3) whenever \(N\) is even.

**3. Odd-order lower envelope.** If \(N\) is odd, \(h\in\mathbb Z+1/2\). Every \(|h|\ge3/2\) gives the bound \(3aB\), where \(B=2a\sqrt{5/2}/3\), strictly exceeding the announced odd constant. For \(h=+1/2\), (3) forces \(\ell\) even and \(s=\vartheta/\pi\). For \(h=-1/2\), it forces \(\ell\) odd and \(s=1-\vartheta/\pi\). Thus in either case \(|1-e^{2\pi is}|=2\sin\vartheta=6/5\), and (4) gives
\[
\liminf_{N\to\infty,\ N\ \mathrm{odd}}N^2\alpha_N
\ge\frac{B a}{\sin\vartheta}
=\frac{10}{9}\sqrt{\frac52}a^2.\tag{5}
\]

**4. Even-order lower envelope.** If \(N\) is even, \(h\in\mathbb Z\). The case \(h=0\) contradicts (3), since \((-1)^\ell\ne e^{i\vartheta}\). Every \(|h|\ge2\) contributes at least \(4aB\), greater than the claimed even constant. For \(h=\pm1\), equation (3) has four possible phase solutions in \([0,1]\). The two with odd \(\ell\) are
\[
(h,s)=(1,\tfrac12+\tfrac{\vartheta}{2\pi}),\qquad
(-1,\tfrac12-\tfrac{\vartheta}{2\pi}),
\]
and maximize the denominator \(|1-e^{2\pi is}|=2\cos(\vartheta/2)=6/\sqrt{10}\); the even-\(\ell\) alternatives give the smaller denominator \(2\sin(\vartheta/2)\). Formula (4) therefore gives
\[
\liminf_{N\to\infty,\ N\ \mathrm{even}}N^2\alpha_N
\ge\frac{2Ba}{\cos(\vartheta/2)}
=\frac{20}{9}a^2.\tag{6}
\]
Here \(\sin\vartheta=3/5\) and \(\cos(\vartheta/2)=3/\sqrt{10}\).

**5. Exact sharpness along infinite subsequences.** The number \(\vartheta/\pi\) is irrational: otherwise \(e^{i\vartheta}\) would be a root of unity, so \(2\cos\vartheta=8/5\) would be a rational algebraic integer, hence an integer, a contradiction. The irrational rotation theorem implies that \(N\vartheta/\pi\) modulo \(2\) approaches zero along arbitrarily large **odd** \(N\). Choose \(k=(N+1)/2\) and an even \(\ell\) with \(\ell-N\vartheta/\pi=o(1)\). Then
\[
N|u_\ell^k-w|\to2a,\qquad
|1-u_\ell|\to2\sin\vartheta.
\]
Substitution into (1) yields equality in (5). Similarly the even subsequence \(N=4m\) has \(N(1/2+\vartheta/(2\pi))=2m+2m\vartheta/\pi\), whose residue modulo \(2\) approaches the odd integers along infinitely many \(m\). Choose \(k=N/2+1\) and odd \(\ell\) with \(\ell-N(1/2+\vartheta/(2\pi))=o(1)\). Then
\[
N|u_\ell^k-w|\to4a,\qquad
|1-u_\ell|\to2\cos(\vartheta/2),
\]
which gives equality in (6). Both lower envelopes are sharp. Since they differ, the full scaled sequence cannot converge. \(\square\)

## Verification
`geometric_parity_checker.py` independently computes direct cyclic inner products and the closed formula (1) in all 4,899 coefficient cases with \(2\le N\le24\); it compares four entire finite-dimensional minima and four constructed near-resonant high-dimensional samples. The checker was executed from its packaged source with output `CHECK_OK direct_coefficients=4899 finite_minima=4 near_resonances=4`. It reports the two constants as approximately \(0.844069907041\) and \(1.067673364263\), respectively. These finite computations independently check the algebra but do **not** prove an infinite limit; Steps 2–5 do so analytically.

## Relationship to prior work
D. Li's September 9, 2026 initial preprint introduces this explicit complex-geometric Gabor seed and proves its normalized ambiguity margin has scale \(N^{-2}\), including a uniform positive lower bound and an upper example. The exact cyclic geometric-series formula is an ingredient of that work and is **not** claimed as new. The present finding instead determines two distinct **sharp parity-restricted leading liminf constants**, the associated near-resonant translation/frequency geometry, and nonconvergence of the dimension-scaled margin. These statements are not supplied by a two-sided bound of order \(N^{-2}\).

A published general geometric-window result gives the entire finite-\(N\) ambiguity formula, rank discriminant and phase-perturbation slopes at fixed even order. Its exact formula algebraically contains the starting identity (1), but its limit is taken in a phase perturbation at fixed \(N\); the new arithmetic optimization takes \(N\to\infty\) with a dimension-dependent root. Another published result on positive geometric windows classifies **critically sampled synthesis matrices** for selected translations, not the full ambiguity margin of the complex root \(2i\). Classical nonzero-ambiguity criteria for Gabor phase retrieval and their matrix-lifting interpretation are taken as background, not independent contributions.

## Limitations
The constants apply only to the specified principal root \(\gamma_N\), not other roots or arbitrary geometric tapers. Both parity expressions are liminf values, not full parity limits; no claim is made about a complete set of accumulation points or rates at which favorable subsequences occur. The sharp leading values use standard irrational-rotation density, not an effective Diophantine rate. The entire finite-\(N\) geometric identity is previously available; the contribution is the dimension-asymptotic resonance classification. General Gabor tomography or globally optimal window conditioning is not addressed. Priority relative to unindexed equivalent dimension-asymptotic treatments remains provisional; independent mathematical validation has not been performed.

## References
1. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614v1, first public 2026-09-09; initial version, especially its geometric-window bound. https://arxiv.org/abs/2609.09614v1
2. *Rank strata and sharp phase-resonance instability for complex-geometric cyclic Gabor measurements*, published mathematical result, full statement and proof at https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-rank-strata-and-sharp-phase-resonance-instability-for-complex-ge--51cfce1c5210/RESULT.md
3. *Geometric cyclic Gabor windows: exact translation-mask rank, spectral rigidity, and optimal taper*, published mathematical result, full statement and proof at https://github.com/published-finding corpus/2026/blob/main/2026/11/16/SCOPE-geometric-cyclic-gabor-windows-exact-translation-mask-rank-spect--92fb6f3665eb/RESULT.md
4. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1 (2015). https://arxiv.org/abs/1503.05800
