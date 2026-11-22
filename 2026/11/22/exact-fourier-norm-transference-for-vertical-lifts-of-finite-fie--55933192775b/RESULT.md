# Exact Fourier-norm transference for vertical lifts of finite-field parabolas

## Finding
Let \(q=p^m\), where \(p\) is an odd prime, and let \(H\subseteq\mathbb F_q\) be any nonempty set. Consider the frequency set
\[
S_H=\{(x,x^2+h):x\in\mathbb F_q,\ h\in H\}\subseteq\mathbb F_q^2.
\]
Its complete unnormalized Fourier-magnitude multiset is
\[
\boxed{\{q|H|\}\ \cup\ \{0\}^{q-1}\ \cup\
\bigcup_{v\in\mathbb F_q^\times}\{\sqrt q\,|\mathcal F_H(v)|\}^{q},\qquad
\mathcal F_H(v)=\sum_{h\in H}\psi(vh).}
\]
Here exponented braces denote multiplicities, and \(\psi(z)=\exp(2\pi i\operatorname{Tr}(z)/p)\) is the canonical additive character. Consequently, the Fourier projection \(P_{S_H}\) has the **sharp** counting-measure endpoint norm
\[
\boxed{\|P_{S_H}\|_{\ell^\infty\to\ell^\infty}
=\|P_{S_H}\|_{\ell^1\to\ell^1}
=\frac{|H|}{q}+\frac1{\sqrt q}\sum_{v\ne0}|\mathcal F_H(v)|.}
\]
The same Fourier-magnitude identity determines the additive energy:
\[
\boxed{E(S_H)=(q^2-q)|H|^4+q^2 E(H),\qquad
E(A)=|\{(a,b,c,d)\in A^4:a+b=c+d\}|.}
\]
In particular, when \(H=\{0,\eta\}\) for any nonzero \(\eta\in\mathbb F_q\), the two parabolas are disjoint and the exact norm is independent of their separation:
\[
\boxed{\|P_{S_H}\|_{\ell^\infty\to\ell^\infty}
=\frac{2\sqrt q}{p\sin(\pi/(2p))}-\frac2{\sqrt q}+\frac2q.}
\]
The Fourier transform of this two-sheet set vanishes at exactly \(q-1\) points, all at nonzero horizontal dual frequencies, and its additive energy is \(22q^2-16q\). For fixed odd characteristic \(p\), the ratio of its endpoint norm to the one-sheet norm tends, as \(m\to\infty\), to \(2/[p\sin(\pi/(2p))]\). Along prime fields \(q=p\to\infty\), the ratio tends to \(4/\pi\).

## Assumptions and scope
All Fourier characters are indexed by \(\mathbb F_q^2\), with the trace pairing \(\psi(ux+vy)\). The Fourier projection means
\[
(P_{S_H}f)(z)=q^{-2}\sum_{\xi\in S_H}\sum_{w\in\mathbb F_q^2}f(w)\psi(\langle z-w,\xi\rangle).
\]
The endpoint sequence norms use counting measure. The unnormalized Fourier transform of an indicator \(1_A\) is \(\mathcal F_A(\zeta)=\sum_{a\in A}\psi(\langle\zeta,a\rangle)\); its sign is immaterial for the magnitudes. The finite-field trace is the absolute trace to \(\mathbb F_p\), and \(p\) is odd. The two-sheet formula requires \(\eta\ne0\). Exact Fourier-magnitude multiplicities permit additional zeros for a general \(H\) when \(\mathcal F_H(v)=0\); only the two-sheet nonvanishing assertion excludes such extra zeros.

## Proof
**1. Factorization.** For \((u,v)\in\mathbb F_q^2\), the Fourier sum of the indicator factorizes as
\[
K(u,v)=\mathcal F_H(v)G(u,v),\qquad
G(u,v)=\sum_{x\in\mathbb F_q}\psi(vx^2+ux).
\]
For \(v=0\), additive orthogonality gives \(G(0,0)=q\) and \(G(u,0)=0\) for \(u\ne0\). For every \(v\ne0\) and every \(u\), \(|G(u,v)|=\sqrt q\). To establish this without assuming a Gauss-sum phase formula, change variables \(a=x-y\), \(b=x+y\) (invertible because \(p\) is odd):
\[
|G(u,v)|^2=\sum_{x,y}\psi(v(x^2-y^2)+u(x-y))
=\sum_{a,b}\psi(vab+ua)=q.
\]
Indeed, summing over \(b\) gives zero for every \(a\ne0\), and \(q\) for \(a=0\). The displayed multiset follows, with \(q\) choices of \(u\) for each nonzero \(v\).

**2. Sharp endpoint norms.** The multiplier is convolution by \(q^{-2}K\), up to reversal of its argument. On a finite group, the convolution \(\ell^\infty\)-operator norm is exactly the sum of the absolute kernel coefficients: the triangle inequality gives one direction, while choosing the input at every position as a conjugate phase of its kernel coefficient attains equality at a fixed output. Hence
\[
\|P_{S_H}\|_{\infty\to\infty}=q^{-2}\sum_{u,v}|K(u,v)|
=q^{-1}|H|+q^{-1/2}\sum_{v\ne0}|\mathcal F_H(v)|.
\]
The adjoint convolution kernel has the same absolute-value sum, proving the \(\ell^1\) equality.

**3. Additive energy.** For any finite abelian group \(G\), character orthogonality implies \(E(A)=|G|^{-1}\sum_{\gamma\in\widehat G}|\mathcal F_A(\gamma)|^4\). Apply this for \(G=\mathbb F_q^2\) and split \(v=0\) from \(v\ne0\):
\[
E(S_H)=q^2|H|^4+q\sum_{v\ne0}|\mathcal F_H(v)|^4.
\]
In one dimension \(\sum_v|\mathcal F_H(v)|^4=qE(H)\) and \(\mathcal F_H(0)=|H|\). Substituting yields the claimed transfer identity, including both small and full fiber sets without exceptional cases.

**4. Two disjoint lifts and characteristic transition.** For \(H=\{0,\eta\}\),
\[
|\mathcal F_H(v)|=|1+\psi(v\eta)|=2|\cos(\pi\operatorname{Tr}(v\eta)/p)|.
\]
The nonzero linear functional \(v\mapsto\operatorname{Tr}(v\eta)\) has each trace value exactly \(q/p\) times, and \(v=0\) contributes magnitude two. The elementary finite trigonometric sum for every odd prime is
\[
\sum_{r=0}^{p-1}2|\cos(\pi r/p)|=\frac2{\sin(\pi/(2p))}.
\]
To verify it, the positive cosine terms are indexed by \(0\le r\le(p-1)/2\), and the negative terms reflect them; evaluate the resulting finite cosine progression using the geometric-series identity. Thus
\[
\sum_{v\ne0}|\mathcal F_H(v)|=\frac{2q}{p\sin(\pi/(2p))}-2,
\]
which gives the stated exact endpoint norm. No \(\mathcal F_H(v)\) can vanish for nonzero \(v\): that would require a \(p\)-th root of unity to equal \(-1\), impossible for odd \(p\). Therefore only \((u\ne0,v=0)\) are zeros. There are exactly \(q-1\) of them. Since \(E(H)=6\) in odd characteristic, the energy identity yields \(22q^2-16q\).

**5. Scaling comparisons.** For \(|H|=1\), the general formula gives the one-sheet endpoint norm \(\sqrt q-q^{-1/2}+q^{-1}\). Divide the two-sheet formula by this expression. For fixed \(p\), the highest-order terms in \(\sqrt q\) give \(2/[p\sin(\pi/(2p))]\). If \(q=p\) tends through primes, \(\sin(\pi/(2p))\sim\pi/(2p)\) gives \(4/\pi\). The finite size and exactness of all formulas follow from finite sums, not from asymptotic estimates.

## Verification
Run `python3 CHECK.py` from the same directory using Python 3 with only the standard library. Its direct double Fourier sums calculate the projection-kernel absolute-value sum without using the factorization as their definition, and its separate pair-sum census calculates additive energy without using Fourier transform. It checks fibers including singleton, two-point, multipt and full field over prime orders \(3,5,7,11,13,17\), plus five fiber choices over the nonprime field \(\mathbb F_9\) with a polynomial basis, for 100 comparisons. The numerical checks use a tolerance of \(10^{-8}\) and support, but do not replace, the all-prime-power proof above.

## Relationship to prior work
Iosevich, Li and Yu (2026, arXiv:2609.25404v1, first posted September 21, 2026) formalize the indicator Fourier algebra norm and exact synthesis constants for affine-transitive paraboloids. The vertical lifts considered here are generally not affine-transitive, and the cited exact affine-transitive theorem does not evaluate their Wiener norms. A published finite-field projection result for **opposite parabolas** treats \(\{(x,x^2)\}\cup\{(x,-x^2)\}\), which intersects at the origin and has a different kernel and full finite sum: it neither includes the two disjoint vertical lifts nor implies the all-fiber transfer formula. Another published result for the **cubic fold** in three dimensions gives a distinct cosecant-type norm through two-root counts, not the present parabolic fiber factorization. The recent line-cover theorem for vertical translated parabolas has the same geometric objects, but concerns covering numbers rather than Fourier projection norms or additive energies. These comparisons are of claims and reductions, not merely titles.

## Limitations
The theorem does not extend by the displayed proof to characteristic two, where the quadratic Gauss magnitude degenerates, or to arbitrary nonlinear curves replacing the parabola. For arbitrary \(H\), the one-dimensional Fourier \(\ell^1\) sum is not further evaluated; the theorem is an **exact transference identity**, not a classification of optimal fiber choices of fixed cardinality. The norm concerns the indicator projection, not sharp synthesis over arbitrary weights supported on \(S_H\). It does not claim independence from all earlier finite-field exponential-sum or idempotent-norm calculations; older equivalent statements may be unindexed. Independent mathematical validation is not part of the evidence given here.

## References
- A. Iosevich, Z. Li, K. Yu, *Spectral synthesis with the complexity parameter in* \(\mathbb Z_N^d\), arXiv:2609.25404v1, first public 2026-09-21, especially Sections 1–3 and 5–6. https://arxiv.org/abs/2609.25404
- P. Bhowmik, S. Deodhar, A. Iosevich, *On spectral synthesis in* \(\mathbb Z_N^d\), arXiv:2508.12194v1, 2025-08-17, general finite-group synthesis bounds. https://arxiv.org/abs/2508.12194
- *A sharp \(4/\pi\) amplification law for Fourier projection onto two opposite finite parabolas*, published 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-4-pi-amplification-law-for-fourier-projection-onto-two-o--a4d0f8547404
- *A characteristic-sensitive sharp Fourier-projection norm for a cubic fold*, published 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-characteristic-sensitive-sharp-fourier-projection-norm-for-a-c--e0347a2c3e00
- *Characteristic-sensitive line covers of translated finite-field parabolas*, published 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-characteristic-sensitive-line-covers-of-translated-finite-field--e3c5b7989e12
