# Sharp two-coefficient greedy Fourier amplification on odd finite abelian groups

## Finding
Let \(G\) be any finite abelian group of odd order \(N\ge 3\), with dual group \(\widehat G\). Write
\[\widehat f(\gamma)=\frac1N\sum_{x\in G}f(x)\overline{\gamma(x)}.\]
Choose the two characters \(\gamma_1,\gamma_2\) associated to the two largest Fourier-coefficient magnitudes (any tie-breaking), and define the second greedy partial sum
\[\mathcal G_2 f(x)=\widehat f(\gamma_1)\gamma_1(x)+\widehat f(\gamma_2)\gamma_2(x).\]
If \(p\) is the smallest prime divisor of \(N\), then the exact nonlinear operator bound is
\[\boxed{\sup_{f\ne0}\frac{\|\mathcal G_2 f\|_{\ell^\infty(G)}}{\|f\|_{\ell^\infty(G)}}=\frac{2}{p\sin(\pi/(2p))}.}\]
It is attained with a strict separation between the selected two coefficient magnitudes and every other coefficient magnitude. Every nonzero extremizer, and no other one, has the form
\[f(x)=c\,\gamma(x)\,\frac{1+\psi(x-x_0)}{|1+\psi(x-x_0)|},\]
where \(c\in\mathbb C\setminus\{0\}\), \(x_0\in G\), \(\gamma\in\widehat G\), and \(\psi\in\widehat G\) has exact order \(p\). Thus the sharp second-stage constant on \((\mathbb Z/p\mathbb Z)^d\) is independent of \(d\), equals \(4/3\) for \(p=3\), and decreases to \(4/\pi\) as \(p\) tends to infinity.

## Assumptions and scope
Groups are finite, abelian, and of odd order at least three; functions may be complex. Every coefficient, including zeros, appears in the sorting, so \(\mathcal G_2\) is defined even for Fourier support of size below two. The ordering is by coefficient magnitude, not a fixed frequency ordering. The statement is about the second partial sum after two *individual* Fourier coefficients, with arbitrary choices inside ties; the exhibited extremizers have no tie at the selection boundary. The supremum is over all nonzero functions, without a mean-zero restriction. The norm uses counting-measure supremum and normalized Fourier coefficients as displayed.

## Proof
**Step 1: all two-character projections.** For distinct \(\alpha,\beta\in\widehat G\), let \(P_{\alpha,\beta}\) retain just those Fourier coefficients. Its convolution kernel is \(K(g)=N^{-1}(\alpha(g)+\beta(g))\). Since \(\chi=\beta\overline\alpha\) has some odd order \(q\ge3\), its values are uniformly distributed among the \(q\)-th roots of unity. Equality in the finite \(\ell^\infty\) convolution estimate is attained by the pointwise conjugate phase of a translated kernel; hence
\[\|P_{\alpha,\beta}\|_{\infty\to\infty}=\frac1q\sum_{j=0}^{q-1}|1+e^{2\pi i j/q}|=\frac{2}{q\sin(\pi/(2q))}=:C_q.\]
The last equality follows by pairing the cosine magnitudes, or by a finite geometric sum. For positive \(u\), the derivative of \(u\sin(a/u)\) is \(\sin(a/u)-(a/u)\cos(a/u)>0\) whenever \(0<a/u<\pi/2\); therefore \(C_q\) strictly decreases with odd \(q\ge3\). Since every \(q\) divides \(N\), \(q\ge p\). Thus \(\|\mathcal G_2 f\|_\infty\le C_p\|f\|_\infty\) for every \(f\), regardless of ties.

**Step 2: the greedy ordering is genuinely achieved.** Cauchy's theorem for finite abelian groups (equivalently duality and group decomposition) supplies a character \(\psi\) of exact order \(p\). The function \(h(x)=(1+\psi(x))/|1+\psi(x)|\) is defined everywhere because \(p\) is odd, and \(|h|=1\). Write \(p=2m+1\), \(\omega=e^{2\pi i/p}\), and pull \(h\) back from \(\mathbb Z/p\mathbb Z\). For \(j=0,\ldots,p-1\), \(h(j)=e^{\pi i j/p}\) for \(j\le m\), while \(h(j)=-e^{\pi i j/p}\) for \(j>m\). For \(k=0,\ldots,p-1\), put \(z=e^{\pi i(1-2k)/p}\); as \(z^p=-1\), exact summation gives
\[\widehat h(k)=\frac1p\left(\sum_{j=0}^{m}z^j-\sum_{j=m+1}^{p-1}z^j\right)=-\frac{2z^{m+1}}{p(1-z)},\quad |\widehat h(k)|=\frac1{p|\sin(\pi(1-2k)/(2p))|}.\]
Exactly \(k=0\) and \(k=1\) have the maximal magnitude \(1/[p\sin(\pi/(2p))]\), and every other \(k\) has strictly smaller magnitude. The Fourier transform on \(G\) is zero outside \(\langle\psi\rangle\), so the two largest Fourier coefficients of \(h\) occur at \(1\) and \(\psi\). Their partial sum at the identity has modulus \(C_p\), while \(\|h\|_\infty=1\). This proves sharpness, including strict separation.

**Step 3: all extremizers.** If equality holds, the selected distinct characters \(\alpha,\beta\) must satisfy \(C_{\operatorname{ord}(\beta\overline\alpha)}=C_p\); strict monotonicity forces the quotient character to have order \(p\). At some \(x_0\in G\), equality must also hold in the \(\ell^\infty\) convolution triangle inequality. As \(p\) is odd, \(K(x_0-y)\ne0\) for all \(y\), so every \(|f(y)|\) must equal \(\|f\|_\infty\), and all convolution summands must have one phase. This uniquely forces
\[f(y)=c\,\alpha(y)\frac{1+(\beta\overline\alpha)(y-x_0)}{|1+(\beta\overline\alpha)(y-x_0)|}\]
for some nonzero \(c\). Conversely each displayed function is a modulation, translate, and scalar multiple of the witness in Step 2, so it attains equality and selects those two characters. This proves the classification.

## Verification
The companion `verify.py` independently computes discrete Fourier coefficients and the second greedy partial sum for every odd \(p\) from \(3\) through \(199\). It checks the exact modulus formula, the strict gap, and the norm equality numerically. It also checks the finite kernel norm and monotonicity for odd \(q\) from \(3\) through \(199\). This is a supplementary finite stress test; the proof above applies to every finite odd-order abelian group. Reproduction: run `python3 verify.py` with the standard Python library.

## Relationship to prior work
Nielsen, *Divergence of decreasing rearranged Fourier series on every infinite compact abelian group* (arXiv:2609.03506, first posted 2026-09-03), develops arbitrarily large magnitude-threshold amplification on products of odd cyclic groups. Its theorems are asymptotic in the number of coordinates and do not furnish the exact order-two greedy coefficient cutoff for a fixed group. Standard finite Fourier projection calculations yield \(C_q\), but knowing the norm of a linear two-character projection alone does not establish that its extremizing input has its two largest Fourier coefficients inside the projected pair. Step 2 supplies that missing compatibility and Step 3 yields rigidity of all nonlinear extremizers.

A published published-finding corpus result titled *Exact two-frequency \(L^1\) concentration on every cyclic group* computes normalized spatial \(L^1\) concentration of two-character **idempotent sums**, including the denominator \(\sum|1+\chi|\). That is a different optimization over the output polynomials with prescribed equal Fourier coefficients. Its denominator recovers the linear projection norm used in Step 1, but it does not give the nonlinear magnitude-ranked-input theorem, the sharp minimum-prime law on arbitrary finite odd abelian groups, or the equality characterization. Existing Chebyshev-threshold greedy approximation estimates for trigonometric systems concern best approximants and asymptotic rates, not this exact two-coefficient partial sum.

## Limitations
This result controls exactly two individually selected Fourier coefficients, not arbitrary longer greedy prefixes or the maximum over all thresholds. It does not imply convergence or divergence for any infinite group. The Fourier-ordering rigidity is complex-valued and uses an odd-order character; no extension to even-order groups is claimed. Older or unindexed finite-dimensional greedy-basis formulae could still contain an equivalent theorem; the cited searches and inspected sources do not prove absolute novelty.

## References
1. M. Nielsen, *Divergence of decreasing rearranged Fourier series on every infinite compact abelian group*, arXiv:2609.03506v1 (2026-09-03), https://arxiv.org/abs/2609.03506.
2. *Exact two-frequency \(L^1\) concentration on every cyclic group*, published published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-two-frequency-l-1-concentration-on-every-cyclic-group--aabfaa5078e3.
3. *Lebesgue constants for Chebyshev thresholding greedy algorithms*, Journal of Inequalities and Applications (2018), https://doi.org/10.1186/s13660-018-1694-y.
4. W. Rudin, *Fourier Analysis on Groups*, Interscience, 1962 (standard finite-abelian Fourier conventions).
