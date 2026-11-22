# Full-shift dynamics and exact Bessel-attraction criteria for centered quadratic bias

## Finding
Fix an integer \(k\geq0\) and real numbers \(0<a<b<\infty\). For a strictly positive probability mass function \(p=(p_n)_{n\geq0}\), define its quadratic-Bessel tail ratios
\[
r_n(p)=(n+1)(n+k+1)\frac{p_{n+1}}{p_n}.
\]
Let \(\mathcal P_{k,a,b}\) comprise the mass functions for which \(a\leq r_n(p)\leq b\) at every index. Equip this family with total-variation distance. The centered quadratic-bias transform is
\[
(\mathcal T_k p)_n=\frac{(n+1)(n+k+1)p_{n+1}}{\sum_{j\geq1}j(j+k)p_j}.
\]
**Theorem.** The dynamical system \((\mathcal P_{k,a,b},\mathcal T_k)\) is topologically conjugate to the full one-sided shift on \([a,b]^{\mathbb N_0}\). The conjugating homeomorphism has an explicit factorially normalized form. Consequently:

1. Every positive integer occurs as the least period of a strictly positive, all-exponential-moments-finite law under \(\mathcal T_k\); periodic points are dense. There are genuinely nonconstant two-cycles.
2. The system has infinite topological entropy. A strictly positive law with all exponential moments finite has an orbit whose total-variation accumulation set is homeomorphic to the full binary one-sided shift, hence is uncountable. Indeed, choosing the tail ratios independently from any probability distribution of full support on \([a,b]\) gives, almost surely, an orbit dense in all of \(\mathcal P_{k,a,b}\).
3. A law \(p\in\mathcal P_{k,a,b}\) converges in total variation under iteration to a Bessel law with parameter \(\lambda\in[a,b]\) if and only if \(r_n(p)\to\lambda\). More generally, asymptotically periodic ratio tails produce the exact corresponding periodic orbit as a full subsequential total-variation limit, with an explicit quantitative bound.

Thus the Bessel family is the fixed-point family, not a universal attractor, even inside an invariant compact family of entire-moment-generating-function laws.

## Assumptions and scope
All indices start at zero. A probability mass function is strictly positive when \(p_n>0\) for every \(n\geq0\). Total variation is half the \(\ell^1\)-distance. The full one-sided shift is \(\sigma(r_0,r_1,\ldots)=(r_1,r_2,\ldots)\), with the product topology on the compact alphabet \([a,b]\). The integer \(k\) is fixed; the transform is the centered quadratic-bias transform for the weight \(n(n+k)\).

For \(r\in[a,b]^{\mathbb N_0}\), set \(B_0(r)=1\), \(B_n(r)=\prod_{j=0}^{n-1}r_j\) for \(n\geq1\), and
\[
Z_k(r)=\sum_{n=0}^\infty\frac{B_n(r)}{n!(n+k)!},\qquad
\Phi_k(r)_n=\frac{B_n(r)}{n!(n+k)! Z_k(r)}.
\]
The sum converges because \(B_n(r)\leq b^n\), and it is bounded below by its \(n=0\) term. Every distribution in this family has \(\mathbb E[e^{\theta N}]<\infty\) for every real \(\theta\).

## Proof
**Step 1 (exact conjugacy and homeomorphism).** From the definition, consecutive ratios satisfy
\[
(n+1)(n+k+1)\frac{\Phi_k(r)_{n+1}}{\Phi_k(r)_n}=r_n.
\]
Thus \(\Phi_k\) is a bijection from \([a,b]^{\mathbb N_0}\) onto \(\mathcal P_{k,a,b}\), with inverse given by these tail ratios. The unnormalized weight of \(\mathcal T_k\Phi_k(r)\) at index \(n\) is
\[
(n+1)(n+k+1)\frac{B_{n+1}(r)}{(n+1)!(n+k+1)!}
=\frac{r_0 B_n(\sigma r)}{n!(n+k)!}.
\]
Normalization cancels \(r_0\), so
\[
\mathcal T_k\circ\Phi_k=\Phi_k\circ\sigma.
\]
The transform is well-defined: its denominator is positive and finite because the laws have all moments. For coordinatewise convergent \(r^{(j)}\to r\), every \(B_n(r^{(j)})\to B_n(r)\), and the weights are bounded by \(b^n/[n!(n+k)!]\). Dominated convergence gives \(\ell^1\), hence total-variation, convergence of \(\Phi_k(r^{(j)})\). Conversely, total-variation convergence in \(\mathcal P_{k,a,b}\) implies convergence of each positive denominator \(p_n\) and each quotient \(r_n(p)\). Hence \(\Phi_k\) and its inverse are continuous; both spaces are compact metric spaces.

**Step 2 (cycles, entropy and accumulation sets).** By injectivity, \(\mathcal T_k^m p=p\) if and only if the ratio sequence is \(m\)-periodic. Its least period is exactly the least period of that ratio sequence. The ratio word \((a,b,\ldots,b)\), repeated with length \(m\geq2\), has least period \(m\), while constant words give fixed points. Given any finite initial ratio word, repeating that finite word gives a periodic sequence with the same prefix; therefore periodic points are dense. At \(k=0\) the ratios \((2,1/2,2,1/2,\ldots)\) generate the explicit two-cycle \(p_n\propto c_n/(n!)^2\), where \(c_{2j}=1\) and \(c_{2j+1}=2\).

For every integer \(L\geq2\), choose \(L\) distinct symbols in \([a,b]\). Their full shift is a closed invariant subsystem of topological entropy \(\log L\); the conjugacy carries it to a subsystem of \(\mathcal T_k\). Thus the entropy of \(\mathcal T_k\) is at least \(\log L\) for every \(L\), and hence infinite. For a concrete single orbit with uncountably many accumulation points, concatenate in order all finite binary words of lengths \(1,2,3,\ldots\), identifying the two letters with \(a,b\). Every finite binary word occurs arbitrarily far out, so the omega-limit set of its shifts is the entire binary shift. The homeomorphism \(\Phi_k\) transports that omega-limit set to the total-variation omega-limit set of the corresponding full-support law. There is also a probabilistically robust version: if the ratio letters are iid with any full-support distribution on \([a,b]\), every nonempty finite-coordinate open cylinder has positive probability. Its occurrences in disjoint blocks are independent, so the second Borel–Cantelli lemma gives infinitely many visits almost surely. A countable basis of cylinders then shows that almost surely the shifted ratio orbit is dense, with full shift as its omega-limit set, and the law orbit is dense in the full compact family. More generally, for every \(r\), the complete omega-limit set of \(\Phi_k(r)\) is
\[
\Phi_k\left(\bigcap_{N\geq0}\overline{\{\sigma^t r:t\geq N\}}\right).
\]

**Step 3 (necessary and sufficient attraction criterion).** A constant ratio sequence \(r_n=\lambda>0\) maps under \(\Phi_k\) to
\[
\pi_{k,\lambda}(n)=\frac{\lambda^n}{n!(n+k)!\,\sum_{j\geq0}\lambda^j/[j!(j+k)!]},
\]
which is the discrete Bessel law \(\mathrm{Bes}(k,2\sqrt\lambda)\). By continuity of \(\Phi_k\) and its inverse, \(\mathcal T_k^t p\to\pi_{k,\lambda}\) in total variation if and only if \(\sigma^t r(p)\) converges coordinatewise to the constant sequence \(\lambda\). The latter condition is equivalent to \(r_t(p)\to\lambda\).

More generally, let \(m\geq1\) and suppose that for every \(s\in\{0,\ldots,m-1\}\), \(r_{mq+s}(p)\to\alpha_s\in[a,b]\). Define the periodic sequence \(\alpha=(\alpha_0,\ldots,\alpha_{m-1})^\infty\) and \(\pi_s=\Phi_k(\sigma^s\alpha)\). For every such \(s\), coordinatewise convergence \(\sigma^{mq+s}r(p)\to\sigma^s\alpha\) proves
\[
\mathcal T_k^{mq+s}p\xrightarrow[q\to\infty]{\mathrm{TV}}\pi_s,
\qquad \mathcal T_k\pi_s=\pi_{s+1\bmod m}.
\]
The least period equals that of \(\alpha\). Conversely, if each residue subsequence converges in total variation to a positive \(m\)-cycle in \(\mathcal P_{k,a,b}\), continuity of the inverse ratio map yields the stated ratio-tail limits. Hence the asymptotic criterion is also necessary.

**Step 4 (quantitative stability).** With the preceding \(\alpha_s\), fix \(t\equiv s\pmod m\), and suppose
\[
\varepsilon_t=\sup_{j\geq t}\left|\frac{r_j(p)}{\alpha_{j\bmod m}}-1\right|<1.
\]
Set
\[
D_s(z)=\sum_{n=0}^\infty \frac{z^n\prod_{j=0}^{n-1}\alpha_{(s+j)\bmod m}}{n!(n+k)!}.
\]
The unnormalized \(n\)-th weight of \(\mathcal T_k^t p\), after division by the positive factor at index zero, is squeezed between \((1-\varepsilon_t)^n\) and \((1+\varepsilon_t)^n\) times the unnormalized weight of \(\pi_s\). For any two positive summable weight sequences \(u,v\), their normalized total-variation distance is at most \(\sum_n|u_n-v_n|/\sum_nu_n\). The pointwise difference is bounded by \(((1+\varepsilon_t)^n-1)v_n\), while \(\sum u_n\geq D_s(1-\varepsilon_t)\). Therefore
\[
\boxed{d_{\mathrm{TV}}(\mathcal T_k^t p,\pi_s)
\leq\frac{D_s(1+\varepsilon_t)-D_s(1)}{D_s(1-\varepsilon_t)}.}
\]
For fixed \(m,k,\alpha\), the right side is \(O(\varepsilon_t)\) as \(\varepsilon_t\downarrow0\), since \(D_s\) is entire and positive on the positive real line. This completes the proof.

## Verification
The standalone standard-library script `check_bias_shift.py` checks 2,209 exact finite rational assertions and positive-tail numerical diagnostics. It reconstructs tail ratios for several \(k\) and periods, checks the shift identity against the quadratic-bias formula, verifies a genuine two-cycle, and tests the finite truncation version of the total-variation stability inequality. Execute with `python3 check_bias_shift.py`. These are diagnostic checks only; the infinite-dimensional conjugacy, topological entropy, full-support conclusions and convergence criteria are proved above and do not rely on finite enumeration.

## Relationship to prior work
DeSalvo [1, Definition 3.1 and Proposition 3.2] introduces the centered quadratic-bias transform and determines its fixed points as Bessel laws. Its Sections 3, 9 and 10 describe Stein approximation and the fixed-point characterization; they do not state a dynamical classification of all iterates, all periods, omega-limit sets, or topological entropy. The polynomial-bias framework of Goldstein and Reinert [2] and the existence theory of Döbler [3] supply broader distributional-transformation background, but the inspected portions do not assert the conjugacy for this centered discrete quadratic-bias map. The present theorem concerns iteration dynamics, not an improved Stein factor or an approximation theorem. The conjugacy is model-specific but uses a general weighted-tail normalization idea; mathematical priority beyond the inspected sources is not certified.

## Limitations
The full conjugacy is asserted on the bounded positive tail-ratio family \(\mathcal P_{k,a,b}\), not on every law for which a single quadratic-bias transform exists. The Bessel attraction equivalence uses convergence to a positive-parameter Bessel law inside this compact family. No claim is made for unbounded or vanishing tail ratios or for random iterations with changing quadratic-bias parameter. The binary full shift demonstrates possible complex deterministic dynamics of distributions; it does not describe typical convergence for a randomly sampled law. The literature comparison cannot exclude an unlocated more general shift-conjugacy theorem.

## References
[1] S. DeSalvo, *Two moments suffice for Bessel approximation: conditioned differences, contingency tables, and probabilistic divide-and-conquer*, arXiv:2611.00263v1 (first public 2026-10-30), revised arXiv:2611.00263v2 (2026-11-14). https://arxiv.org/html/2611.00263v2

[2] L. Goldstein and G. Reinert, *Distributional transformations, orthogonal polynomials, and Stein characterizations*, Journal of Theoretical Probability 18 (2005), 237–260; arXiv:math/0510240. https://arxiv.org/abs/math/0510240

[3] C. Döbler, *Distributional transformations without orthogonality relations*, Journal of Theoretical Probability 30 (2017), 600–631; arXiv:1312.6093. https://arxiv.org/abs/1312.6093

[4] S. DeSalvo, *Stein’s method for negative binomial and hyper-negative-binomial laws, with applications*, arXiv:2611.00275v1 (2026). https://arxiv.org/html/2611.00275v1
