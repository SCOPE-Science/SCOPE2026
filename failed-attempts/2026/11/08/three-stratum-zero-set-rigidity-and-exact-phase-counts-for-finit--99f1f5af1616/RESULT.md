# Three-stratum zero-set rigidity and exact phase counts for finite-parabola Fourier sums

## Finding
Let \(p\ge5\) be prime, let \(q=2^s\) for an integer \(s\ge1\), and let \(R\subsetneq\mathbb F_p\) be nonempty. Let \(\omega=e^{2\pi i/p}\), \(\eta=e^{2\pi i/q}\), and assign to each \(x\in R\) a phase \(u_x\in\{\eta^j:0\le j<q\}\). Consider the unnormalized two-variable Fourier sum
\[
F_{R,u}(a,b)=\sum_{x\in R}u_x\,\omega^{a x^2+b x},\qquad(a,b)\in\mathbb F_p^2.
\]
**Complete zero-set classification.** Its zero set is one of precisely three geometries: the empty set, the singleton \(\{(0,0)\}\), or exactly one line of \(p\) points
\[
L_c=\{(a,b)\in\mathbb F_p^2:b=-2ca\}
\]
for a unique \(c\in\mathbb F_p\). The line case holds if and only if \(R\) is a union of disjoint pairs \(\{c+t,c-t\}\) and the coefficients satisfy \(u_{c+t}=-u_{c-t}\) on every pair. If \(|R|\) is odd then the zero set is always empty, for every assignment of the permitted phases.

**All coefficient and support counts.** For even \(k=|R|=2r\), put \(m=q/2\) and
\[
A_{q,r}=(2r)!\sum_{\substack{t_0,\ldots,t_{m-1}\ge0\\\sum_j t_j=r}}\ \prod_{j=0}^{m-1}\frac1{(t_j!)^2}.
\]
Then on each fixed support \(R\), of size \(2r\), the numbers of phase assignments yielding respectively zero sets of size \(0,1,p\) are
\[
q^{2r}-A_{q,r},\quad A_{q,r}-I_Rq^r,\quad I_Rq^r,
\]
where \(I_R=1\) when \(R\) is invariant under a reflection \(x\mapsto 2c-x\) and \(I_R=0\) otherwise. Such a center, when it exists, is unique. Across **all** \(\binom p{2r}\) supports, the corresponding counts are
\[
\binom p{2r}(q^{2r}-A_{q,r}),\quad
\binom p{2r}A_{q,r}-p\binom{(p-1)/2}{r}q^r,\quad
p\binom{(p-1)/2}{r}q^r.
\]
For odd \(k\), all \(\binom p k q^k\) phase-decorated supports are zero-free. In particular, for quadrature phases \(q=4\), one has \(A_{4,r}=\binom{2r}{r}^2\).

## Assumptions and scope
Here \(p\) is a rational prime at least five; \(q\) is an arbitrary positive power of two; \(1\le|R|\le p-1\); each listed coefficient is nonzero and belongs to the full \(q\)-phase alphabet. Each coefficient assignment on a labeled support is counted separately. All Fourier frequencies are evaluated over the full Cartesian square \(\mathbb F_p^2\); the sign convention in the exponent is fixed above. No assertion is made for unrestricted complex coefficients, non-prime moduli, or supports equal to the whole field.

## Proof
**1. A cyclotomic separation lemma.** Set \(K=\mathbb Q(\eta)\). Since \(\gcd(p,q)=1\), \([\mathbb Q(\omega,\eta):\mathbb Q]=\varphi(pq)=(p-1)\varphi(q)\). Thus \([K(\omega):K]=p-1\) and the minimal polynomial of \(\omega\) over \(K\) is \(\Phi_p(T)=1+T+\cdots+T^{p-1}\). Therefore for any \(C_0,\ldots,C_{p-1}\in K\),
\[
\sum_{t=0}^{p-1}C_t\omega^t=0\quad\Longleftrightarrow\quad C_0=C_1=\cdots=C_{p-1}.
\]
Indeed, a polynomial of degree at most \(p-1\) vanishing at \(\omega\) must be a scalar multiple of this irreducible polynomial.

**2. Vanishing at nonzero frequencies forces pair reflection.** Fix \((a,b)\ne(0,0)\), and let \(h(x)=ax^2+bx\). Group terms of \(F_{R,u}\) by the value of \(h(x)\) to form \(C_t=\sum_{x\in R:h(x)=t}u_x\in K\). Since \(|R|<p\), at least one \(t\) has no preimage in \(R\), and hence \(C_t=0\). If \(F_{R,u}(a,b)=0\), step 1 forces **every** \(C_t\) to be zero. If \(a=0\), then \(b\ne0\) and \(h\) is injective; at least one \(C_t\) is a single nonzero \(u_x\), a contradiction. Thus \(a\ne0\). Completing the square with \(c=-b/(2a)\) shows that every fiber of \(h\) has at most two points, paired by \(x\mapsto2c-x\), and that the fixed point \(c\) is a singleton. Every \(C_t=0\) therefore implies \(c\notin R\), invariance of \(R\) under this reflection, and \(u_x=-u_{2c-x}\) for each \(x\in R\).

Conversely, these pairwise opposite coefficients yield cancellation for every \((a,b)\) satisfying \(b=-2ca\), including \((0,0)\). The implication just proved excludes every other nonzero-frequency zero unless it has another reflection center. Two different centers would generate a nonzero translation preserving \(R\), forcing the nonempty set \(R\) to be all of \(\mathbb F_p\), contrary to the hypothesis. Hence any nontrivial zero set is exactly the single line \(L_c\).

**3. The zero at the origin and parity.** Let \(n_j\) be the number of coefficients equal to \(\eta^j\), \(0\le j<q\). Write \(m=q/2\). Since \(\Phi_q(T)=T^m+1\),
\[
F_{R,u}(0,0)=\sum_{j=0}^{m-1}(n_j-n_{j+m})\eta^j.
\]
The powers \(1,\eta,\ldots,\eta^{m-1}\) are rationally linearly independent; therefore the origin is a zero exactly when \(n_j=n_{j+m}\) for every \(j\). In particular \(|R|\) must be even. For \(|R|=2r\), write \(t_j=n_j=n_{j+m}\); the number of ordered phase assignments with these occupancies is \((2r)!/\prod_j(t_j!)^2\). Summing over all \(m\)-tuples adding to \(r\) proves \(A_{q,r}\). This also proves that odd-size supports are wholly zero-free.

**4. Counts for a fixed and for varying support.** A support \(R\) symmetric about a center consists of \(r\) of the \((p-1)/2\) available noncentral reflection pairs; at each chosen pair there are exactly \(q\) freely chosen phases with the partner forced to be its negative. Hence precisely \(q^r\) phase assignments give the full line on such a support, and none on nonsymmetric supports. These assignments are included among the origin-zero assignments, giving the fixed-support triple by subtraction. The center of a nonempty proper symmetric support is unique by step 2. There are \(p\binom{(p-1)/2}{r}\) symmetric supports of size \(2r\), so multiplying and subtracting yields the global triple. For \(q=4\), the Vandermonde identity \(\sum_{j=0}^{r}\binom{r}{j}^2=\binom{2r}{r}\) gives \(A_{4,r}=\binom{2r}{r}^2\). All assertions follow.

## Verification
`CHECK.py` works over the exact integer quotient \(\mathbb Z[T]/(\Phi_{pq}(T))\), whose polynomial is explicitly \(\sum_{j=0}^{p-1}(-1)^jT^{jq/2}\). It evaluates actual \(p^2\) Fourier coefficients, not a floating-point proxy, and compares every zero set with the theorem's predicted geometry and exact coefficient counts. Exhaustive cases include \((p,q)=(5,2),(5,4),(5,8),(7,2),(7,4)\) through four-point supports, plus all eight-phase assignments on one four-point support for \(p=7\). A run tested 45,188 assignments and 1,528,052 exact Fourier evaluations, reporting `CHECK_OK`. The all-primes/all-supports proof is steps 1–4; the finite checks are not substituted for it.

For example, with \(p=7,q=4,|R|=4\), among all support-and-phase pairs, 7,700 have no zeros, 924 have exactly the origin as a zero, and 336 have a full line of seven zeros; the sum is \(\binom74\,4^4=8,960\).

## Relationship to prior work
Li's 2026 finite-parabola uncertainty theorem treats **arbitrary complex nonzero coefficients** and gives parity-sensitive upper bounds on the number of Fourier zeros, together with rigidity in large-zero regimes. Those bounds do not identify exact zero sets and their numbers for power-of-two phase alphabets. In fact the arbitrary-complex problem allows isolated nonorigin zeros that cannot occur with the phase restriction proved here. The elementary cyclotomic irreducibility fact and the classification of possible lengths of vanishing root-of-unity sums are established background, notably Lam and Leung. The new subject of the theorem is their joint consequence for the two-parameter quadratic Fourier family, including exact counts on every labeled support and over all supports. A separate published exact five-point classification for \(\mathbb F_7\) concerns **arbitrary complex coefficients**, not this phase-restricted, all-prime classification.

## Limitations
Publication priority is assessed only against the cited material and available indexed comparisons; an older equivalent result formulated in polyphase chirp or MUB terminology may exist. The theorem is about exact zeros, not the size of small but nonzero Fourier coefficients, and it does not cover phase alphabets with odd prime factors or coefficients with \(p\)-cyclotomic dependence. No independent mathematical audit has been performed.

## References
1. D. Li, *Parity-Sensitive Fourier Uncertainty and Zero-Set Rigidity on the Finite Parabola*, arXiv:2609.16030, first posted 2026-09-11. https://arxiv.org/abs/2609.16030 .
2. T. Y. Lam and K. H. Leung, *On vanishing sums for roots of unity*, arXiv:math/9511209 (1995); Journal of Algebra 224 (2000), 91–109. https://arxiv.org/abs/math/9511209 .
3. *Exact five-point finite-parabola uncertainty over the field of seven elements*, publicly indexed research result (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-five-point-finite-parabola-uncertainty-over-the-field-of-s--c8e97af8983f .
