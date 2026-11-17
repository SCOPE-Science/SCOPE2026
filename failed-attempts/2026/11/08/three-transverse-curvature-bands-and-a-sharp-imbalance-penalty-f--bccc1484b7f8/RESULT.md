# Three transverse curvature bands and a sharp imbalance penalty for finite-field cubic Fourier extension

## Finding
Let \(F\) be any finite field of order \(q\), of characteristic other than \(2\) or \(3\), and let \(g:F\to\mathbb C\). Define \(S=\sum_{t\in F}|g(t)|^2\) and
\[
Q(g)=\sum_{\substack{a+b=c+d\\a^3+b^3=c^3+d^3}}g(a)g(b)\overline{g(c)g(d)}.
\]
The known sharp cubic-graph extension coefficient is \(C_q=3-6/(2q+1)\). This finding determines an **exact nonnegative decomposition** of \(\mathfrak D(g)=C_q S^2-Q(g)\), including a globally sharp imbalance penalty, and the **complete transverse second-variation spectrum** at every nonzero extremizer.

Choose one representative \(t_j\) of every antipodal pair \(\{t,-t\}\subset F^\times\), indexed by \(1\le j\le h=(q-1)/2\). Put
\[
\alpha=|g(0)|^2,\quad m_j=|g(t_j)|^2+|g(-t_j)|^2,\quad r_j=2|g(t_j)g(-t_j)|,
\quad \delta_j=m_j-r_j,\quad \Delta=\sum_j\delta_j,
\]
and \(w_0=g(0)^2\), \(w_j=2g(t_j)g(-t_j)\), and
\[
\Phi(g)=\bigl(\alpha+\sum_jr_j\bigr)^2-\bigl|w_0+\sum_jw_j\bigr|^2\ge0.
\]
Then, for **every** \(g\), including functions with zeros,
\[
\boxed{\begin{aligned}
\mathfrak D(g)={}&2\left(\alpha-\frac{3S}{2q+1}\right)^2
+\frac32\sum_j\left(m_j-\frac{4S}{2q+1}\right)^2\\
&+\sum_j \delta_j\left(2S-\Delta-\frac{m_j+r_j}{2}\right)+\Phi(g).
\end{aligned}}
\]
Every coefficient \(2S-\Delta-(m_j+r_j)/2\) is at least \(S/2\). Thus this formula gives the global quantitative stability inequality
\[
\boxed{\mathfrak D(g)\ge2\left(\alpha-\frac{3S}{2q+1}\right)^2
+\frac32\sum_j\left(m_j-\frac{4S}{2q+1}\right)^2
+\frac S2\sum_j\bigl(|g(t_j)|-|g(-t_j)|\bigr)^2+\Phi(g).}
\]
The coefficient \(1/2\) in the standalone imbalance term cannot be increased while retaining these other terms, because equality occurs for any one-site function supported at a nonzero element of \(F\).

On the real Hilbert space underlying \(\mathbb C^F\), at any unit-mass extremizer \(f_*\), the quadratic coefficient \(L\) in
\[
\mathfrak D(f_*+\varepsilon v)=\varepsilon^2\langle v,Lv\rangle+O(\varepsilon^3)
\]
has the following complete spectrum (the ordinary real Hessian is \(2L\)):
\[
\begin{array}{c|c}
\text{coefficient eigenvalue}&\text{real multiplicity}\\\hline
0&(q+3)/2\\
24/(2q+1)&(q-1)/2\\
4-8/(2q+1)&(q-1)/2\\
4&(q-1)/2
\end{array}
\]
The kernel is **exactly** the tangent space to the complex-scaling and antipodal-phase extremizer manifold. If \(\mathcal M\) denotes the unit-mass extremizer manifold and \(\|g\|_2=1\), the sharp local stability coefficient in ordinary Euclidean squared distance is
\[
\boxed{\liminf_{\operatorname{dist}_2(g,\mathcal M)\to0}\frac{C_q-Q(g)}{\operatorname{dist}_2(g,\mathcal M)^2}=\frac{24}{2q+1}.}
\]
In particular, the weakest transverse curvature is of order \(q^{-1}\), whereas the other two nonzero curvature bands remain bounded away from zero as \(q\to\infty\).

## Assumptions and scope
The ambient Fourier transform uses normalized surface counting on \(C=\{(t,t^3):t\in F\}\) and ordinary counting measure on \(F^2\): \(E g(x,y)=q^{-1}\sum_t g(t)\psi(xt+yt^3)\), with any nontrivial additive character \(\psi\). Orthogonality gives \(\|Eg\|_{\ell^4(F^2)}^4=q^{-2}Q(g)\), while \(\|g\|_{L^2(C)}^4=q^{-2}S^2\), so \(\mathfrak D\) is exactly the sharp fourth-power extension deficit multiplied by \(S^2\). All quantities in the theorem are unnormalized counting quantities; \(\operatorname{dist}_2\) is the counting Euclidean distance in \(\mathbb C^F\). The characteristic condition is essential for the cubic fiber identity and antipodal pair decomposition.

## Proof
**Collision identity.** At fixed sum \(s=a+b=c+d\), \(a^3+b^3=s^3-3abs\). When \(s\ne0\), cubic equality forces \(ab=cd\) and hence the unordered pairs coincide. At \(s=0\), all pairs \((a,-a)\) collapse to the same cubic value. Counting the diagonal terms and replacing the zero-sum fiber yields
\[
Q(g)=2S^2-\sum_t|g(t)|^4-2\sum_t|g(t)|^2|g(-t)|^2+|g(0)|^4+\left|\sum_t g(t)g(-t)\right|^2.
\]
Grouping the nonzero elements in antipodal pairs gives
\[
Q(g)=2S^2-2\alpha^2-\sum_j m_j^2-\tfrac12\sum_jr_j^2+\left|w_0+\sum_jw_j\right|^2.
\]
Since \(S=\alpha+\sum_jm_j\), \(\sum_{j=0}^h|w_j|=\alpha+\sum_jr_j=S-\Delta\), and \(r_j^2=m_j^2-\delta_j(m_j+r_j)\), subtracting the preceding formula from \(C_qS^2\) and completing the square gives the boxed identity. The amplitude square completion uses
\[
2\left(\frac{3S}{2q+1}\right)^2
+\frac32\,\frac{q-1}{2}\left(\frac{4S}{2q+1}\right)^2=\frac{6S^2}{2q+1}.
\]
The phase term \(\Phi\) is the triangle-inequality deficit, and is nonnegative even if some \(w_j=0\). Finally,
\[
2S-\Delta-\frac{m_j+r_j}{2}
=S+\alpha+\sum_{i\ne j}r_i-\frac{\delta_j}{2}\ge\frac S2
\]
because \(0\le\delta_j\le S\). For the vector supported at one nonzero site, the relevant coefficient is exactly \(S/2\) and \(\Phi=0\). This proves the stated sharpness.

**Second variation.** All nonzero extremizers have \(|f_*(0)|^2=3/(2q+1)\), \(|f_*(t)|^2=2/(2q+1)\) for \(t\ne0\), and aligned antipodal products; this follows also from the exact identity. Diagonal unitary pair-phase symmetries and complex scaling reduce the computation to positive \(a=\sqrt{3/(2q+1)}\) at zero and \(b=\sqrt{2/(2q+1)}\) elsewhere. Let \(T=2q+1\). For a real perturbation \(v\), split each antipodal pair into symmetric and antisymmetric coordinates \(v_j^+=(v(t_j)+v(-t_j))/\sqrt2\) and \(v_j^-=(v(t_j)-v(-t_j))/\sqrt2\). On the real symmetric subspace \((v(0),v_j^+)\), the amplitude-square part has quadratic coefficient \(24/T\) on the hyperplane perpendicular to \((a,\sqrt2 b,\ldots,\sqrt2 b)\) and zero along that unit radial vector. On the antisymmetric real subspace \(\delta_j=2\varepsilon^2(v_j^-)^2+O(\varepsilon^3)\), and the imbalance coefficient at the extremizer equals \(2-4/T\), yielding \(4-8/T\).

For imaginary perturbations, the pair-antisymmetric directions are tangent to the exact phase symmetries and have zero curvature. On the remaining imaginary symmetric coordinates \((v(0),v_j^+)\), the quadratic phase deficit is exactly
\[
4\left(\sum_j |v_j^+|^2+|v(0)|^2
-\left|a\,v(0)+\sqrt2 b\sum_jv_j^+\right|^2\right),
\]
so it equals \(4\) times squared distance from the global-phase direction. These real and imaginary sectors are orthogonal; their dimensions sum to \(2q\). The nullity is \(h+2\), exactly the dimension of the smooth extremizer cone: one real scaling, one global phase, and \(h\) independent opposite-pair phase rotations. On the unit sphere, the radial direction disappears and the remaining nullspace is precisely tangent to \(\mathcal M\). Thus Taylor expansion transverse to the compact smooth \(\mathcal M\) gives the stated sharp local distance coefficient, attained in any unit symmetric real direction orthogonal to \(f_*\).

## Verification
`python3 artifacts/verify.py` uses exact rational arithmetic to verify the global identity and nonnegative terms on 175 randomized Gaussian-integer inputs for the prime fields of orders \(5,7,11,13,17\), as well as 15 independently enumerated inputs over \(\mathbb F_{25}\), by computing every cubic collision fiber. It also checks the optimal imbalance coefficient on a one-point input, and numerically probes all six tangent/transverse quadratic sectors at the positive extremizers for these prime fields. Expected output: `CUBIC_STABILITY_EXACT_AND_CURVATURE_PASS cases=175 primes=5 bands=6 extension_fields=1`. The finite tests, including the quadratic extension-field example, do not prove the infinite family; the characteristic-independent algebra above does.

## Relationship to prior work
Mockenhaupt--Tao (first public 2002) introduced the finite-field restriction framework and the even-exponent representation-count technique, but do not evaluate the stability of the cubic graph. Hughes--Wooley (2019) analyze the analogous integer curve with high even moments and distinguish zero from nonzero pair-sum fibers; their results are not the finite-field sharp local curvature theorem. González-Riquelme--Oliveira e Silva (2024) treat sharp inequalities on quadratic surfaces rather than this cubic graph. A public earlier cubic-graph sharp theorem (`SCOPE-exact-sharp-finite-field-cubic-graph-l-2-to-l-4-extension-norm-a--2db777d1e47b`, 2026) establishes \(C_q\) and the equality cases; its full result and proof contain neither the present quantitative global deficit with optimal componentwise imbalance coefficient nor the three-band local Hessian spectrum. The new statements refine, rather than reassert, the known sharp inequality.

## Limitations
The coefficient \(1/2\) is optimal for the **displayed componentwise global inequality with the other terms unchanged**; it is not claimed to be the optimal constant for every possible metric distance to the extremizer set. The number \(24/(2q+1)\) is a **sharp local** squared-distance stability coefficient, not a claimed global distance inequality. The proof excludes characteristics \(2\) and \(3\). The exact checker covers five prime fields through \(17\) and one extension field of order \(25\); the all-field result is symbolic. An earlier unindexed quantitative stability theorem or a broader general principle could potentially cover some part of the conclusions.

## References
1. G. Mockenhaupt and T. Tao, “Restriction and Kakeya phenomena for finite fields,” arXiv:math/0204234v1 (first public 2002-04-18), Duke Math. J. 121 (2004), 35–74. https://arxiv.org/html/math/0204234v4
2. K. Hughes and T. D. Wooley, “Discrete restriction for \((x,x^3)\) and related topics,” arXiv:1911.12262v1 (2019-11-27). https://arxiv.org/html/1911.12262v1
3. C. González-Riquelme and D. Oliveira e Silva, “Sharp extension inequalities on finite fields,” arXiv:2405.16647v1 (2024-05-26). https://arxiv.org/abs/2405.16647
4. “Exact sharp finite-field cubic-graph \(L^2\) to \(L^4\) extension norm and extremizers,” public research record, 2026-10-04. https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-sharp-finite-field-cubic-graph-l-2-to-l-4-extension-norm-a--2db777d1e47b/RESULT.md
