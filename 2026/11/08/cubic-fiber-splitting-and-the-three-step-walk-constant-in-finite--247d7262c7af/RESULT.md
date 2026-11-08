# Cubic-fiber splitting and the three-step-walk constant in finite Fourier projection norms

## Finding

Let \(q=p^m\) be any prime power and \(F=\mathbb F_q\). On the additive group \(G=F^3\), consider the quartic monomial graph
\[
 S_q=\{(x,y,xy^3):x,y\in F\}.
\]
Let \(P_{S_q}\) be the Fourier multiplier with symbol \(1_{S_q}\), acting on complex functions on \(G\). Its sharp endpoint projection norm and the entire multiset of magnitudes of its convolution kernel have the following classification.

**Bijective-cube branch.** If \(\gcd(3,q-1)=1\), then
\[
 \|P_{S_q}\|_{\ell^\infty(G)\to\ell^\infty(G)}=q-1+q^{-1}.
\]
The kernel has one coefficient of magnitude \(q^{-1}\), exactly \(q^2(q-1)\) coefficients of magnitude \(q^{-2}\), and all remaining coefficients vanish. This includes characteristic three and fields with \(q\equiv2\pmod 3\).

**Three-to-one-cube branch.** If \(q\equiv1\pmod3\), let \(\zeta\in F\) be any primitive cube root of unity and let \(\psi(v)=\exp(2\pi i\operatorname{Tr}_{F/\mathbb F_p}(v)/p)\). Write
\[
 H_q=\sum_{b\in F}|\psi(b)+\psi(\zeta b)+\psi(\zeta^2b)|.
\]
Then the exact sharp norm is
\[
 \boxed{\|P_{S_q}\|_{\ell^\infty\to\ell^\infty}=1+\frac{(q-1)^2}{3q^2}H_q.}
\]
Its kernel has exactly \(1+q(q-1)+q(q-1)^2/3\) nonzero coefficients. The full kernel magnitude multiset consists of one \(q^{-1}\), exactly \(q(q-1)\) copies of \(q^{-2}\), and, for each of \((q-1)^2/3\) groups, the \(q\) values
\[
 \left\{q^{-2}|\psi(b)+\psi(\zeta b)+\psi(\zeta^2b)|:b\in F\right\}
\]
with multiplicity, together with zeros filling the remaining \(q^3\) positions. None of these three-phase values is zero. Thus the limiting proportion of nonzero kernel coefficients is one in the bijective branch and one third in the three-to-one branch, even though both frequency sets have exactly \(q^2\) elements.

Despite being defined over fields of arbitrarily high extension degree, the normalized three-phase sum \(A_p=H_q/q\) depends only on the prime characteristic and on whether the cube roots lie in the prime subfield. Set \(e_p(t)=\exp(2\pi it/p)\). Precisely,
\[
 A_p=\begin{cases}
 \displaystyle\frac1p\sum_{t\in\mathbb F_p}|e_p(t)+e_p(\zeta t)+e_p(\zeta^2t)|,&p\equiv1\pmod3,\\[6pt]
 \displaystyle\frac1{p^2}\sum_{u,v\in\mathbb F_p}|1+e_p(u)+e_p(v)|,&p\equiv2\pmod3\quad(m\ \text{even}).
 \end{cases}
\]
In the first line \(\zeta\) denotes its reduction in \(\mathbb F_p\). Equivalently the split-branch norm is \(1+(q-1)^2A_p/(3q)\). The normalized unitary Fourier ratio of the indicator satisfies the exact relation
\[
 \operatorname{FR}(1_{S_q})=\sqrt q\,\|P_{S_q}\|_{\ell^\infty\to\ell^\infty}.
\]

There is a shared large-characteristic constant in both split subbranches:
\[
 C_3=\frac1{(2\pi)^2}\int_0^{2\pi}\!\int_0^{2\pi}|1+e^{i\theta}+e^{i\phi}|\,d\theta\,d\phi
 =1.574597\ldots.
\]
As the prime \(p\to\infty\) through either congruence class, \(A_p\to C_3\); hence along any sequence of three-to-one-cube fields with characteristics tending to infinity,
\[
 \boxed{\frac{\|P_{S_q}\|}{q}\longrightarrow\frac{C_3}{3}=0.524865\ldots.}
\]
By contrast the bijective-cube branch has \(\|P_{S_q}\|/q\to1\). The constant \(C_3\), the mean displacement of a three-step uniform planar random walk, is classical; its identification as the asymptotic coefficient of this Fourier projection is part of the present claim, not a claim that the random-walk integral is newly evaluated.

## Assumptions and scope

The theorem holds for every finite field \(F\), including characteristic two and three. All characters are the canonical trace characters for the displayed formulas; another nontrivial additive character gives the same kernel-magnitude multiset after reindexing frequencies. No primality assumption on \(q\) is made. The prime-field asymptotics concern the parameter \(p\to\infty\), **not** extension degree at fixed characteristic. For fixed \(p\), the split-branch slope is \(A_p/3\), which need not equal \(C_3/3\).

We use \(\widehat f(\xi)=\sum_{g\in G}f(g)\overline{\psi(\xi\cdot g)}\) and inversion with factor \(q^{-3}\). The projection kernel is \(K_q(g)=q^{-3}\sum_{\xi\in S_q}\psi(\xi\cdot g)\). The Fourier ratio uses the unitary transform \(q^{-3/2}\widehat f\) and counting-measure \(\ell^1,\ell^2\) norms.

## Proof

**Step 1: an exact fiber formula and sharpness.** For \(g=(a,b,c)\in G\), summing in the graph parameter \(x\) first and using nontrivial character orthogonality gives
\[
 K_q(a,b,c)=q^{-3}\sum_{x,y\in F}\psi(ax+by+cxy^3)
 =q^{-2}\sum_{y\in F:\ a+cy^3=0}\psi(by). \tag{1}
\]
Convolution by \(K_q\) has sharp \(\ell^\infty\)-norm \(\sum_g|K_q(g)|\): the upper bound is the triangle inequality, and equality at zero is attained by taking the input at \(-g\) to be the complex conjugate of the phase of \(K_q(g)\) for nonzero kernel values.

If \(c=0\), formula (1) vanishes except at \((a,b,c)=(0,0,0)\), where it equals \(q^{-1}\). If \(c\ne0\), for \(a=0\) there is just the root \(y=0\), yielding \(K_q=q^{-2}\) for every \(b\). If \(a\ne0\), the root count of \(y^3=-a/c\) is \(d=\gcd(3,q-1)\) or zero. In the case \(d=1\) there is exactly one root for every \((a,c)\in(F^\times)^2\); hence there are \(q^2(q-1)\) nonzero coefficients of magnitude \(q^{-2}\) away from the origin. Summing proves the first branch.

Suppose \(d=3\). Then exactly \((q-1)^2/3\) nonzero pairs \((a,c)\) have a fiber, each of the form \(\{t,t\zeta,t\zeta^2\}\) for \(t\ne0\). Multiplication by \(t\) bijects the \(b\)-variable, so each such pair contributes the same sum \(H_q\) of absolute three-phase amplitudes. Together with the origin and the \(q(q-1)\) singleton fibers, this proves
\[
 \sum_{g\in G}|K_q(g)|=q^{-2}\left(q+q(q-1)+\frac{(q-1)^2}{3}H_q\right)
 =1+\frac{(q-1)^2}{3q^2}H_q.
\]
Every three-phase sum is nonzero. Indeed, three unit complex numbers sum to zero only when their ratios include primitive cube roots of unity. For an additive character of characteristic \(p\ne3\), all those ratios are \(p\)-th roots of unity, which cannot include primitive cube roots. Since \(d=3\) forces \(p\ne3\), the claimed nonzero count and the complete kernel magnitude multiset follow.

**Step 2: trace rank determines the exact characteristic formula.** When \(p\equiv1\pmod3\), all three elements \(1,\zeta,\zeta^2\) are in the prime subfield. Because the field trace maps onto \(\mathbb F_p\) with equally sized fibers, \(\operatorname{Tr}(\zeta^j b)=\zeta^j\operatorname{Tr}(b)\). This gives the one-variable formula for \(A_p\).

When \(p\equiv2\pmod3\), a field admitting \(\zeta\) must have even extension degree, and \(1,\zeta\) are linearly independent over \(\mathbb F_p\). Nondegeneracy of the trace pairing implies that the two linear functionals \(b\mapsto\operatorname{Tr}(b)\) and \(b\mapsto\operatorname{Tr}(\zeta b)\) are independent, so their joint map onto \(\mathbb F_p^2\) is surjective with fibers of size \(q/p^2\). Since \(1+\zeta+\zeta^2=0\), the third trace is the negative sum of the first two. Finally,
\[
 |e_p(s)+e_p(t)+e_p(-s-t)|=|1+e_p(2s+t)+e_p(s+2t)|.
\]
The linear change \((s,t)\mapsto(2s+t,s+2t)\) has determinant three, nonzero modulo \(p\ne3\), and is a bijection. This proves the two-variable formula.

**Step 3: the asymptotic constant.** Define the continuous \(2\pi\)-periodic function \(\Phi(\theta,\phi)=|1+e^{i\theta}+e^{i\phi}|\). For \(p\equiv2\pmod3\), the two-dimensional \(p\)-grid Riemann sum converges to its torus integral \(C_3\).

For \(p\equiv1\pmod3\), divide the three phases by the last one. The first-line average for \(A_p\) becomes
\[
 \frac1p\sum_{u\in\mathbb F_p}|1+e_p(u)+e_p(\rho_pu)|,
 \quad \rho_p=-\zeta^2\in\mathbb F_p,
 \quad \rho_p^2-\rho_p+1=0.
\]
For any fixed integers \((k,\ell)\ne(0,0)\), the discrete mean of the torus Fourier character \(e_p((k+\ell\rho_p)u)\) can be nonzero only if \(p\mid k+\ell\rho_p\). Multiplying by its conjugate root \(1-\rho_p\) shows that this forces
\[
 p\mid k^2+k\ell+\ell^2.
\]
The integer on the right is strictly positive and fixed, so this cannot occur for all sufficiently large primes. Thus the one-dimensional probability measures are asymptotically Haar on the two-torus: their integrals converge for trigonometric polynomials, then for every continuous function by uniform approximation. Applying this to \(\Phi\) proves \(A_p\to C_3\). Dividing the exact norms by \(q\) gives the two stated limiting slopes. The Fourier-ratio relation follows immediately from \(|S_q|=q^2\), Parseval and \(\widehat{1_{S_q}}=q^{3/2}K_q\) up to reflection.

## Verification

The standalone Python 3 script `CHECK.py` carries out finite-field arithmetic and direct Fourier character sums. It tests the full kernel norm and nonzero counts in 11 fields, including split and bijective branches and prime-degree-two extensions. It evaluates the direct defining Fourier sum at all triples for fields through order 13, and at 125 deterministically sampled triples in each larger field. The test output is `CHECK_OK fields=11`. The analytical proof covers all prime powers and the asymptotic statements; none is inferred from the finite checks.

## Relationship to prior work

Fourier algebra norms and Fourier ratios of finite spectral supports are natural invariants in Iosevich, Li and Yu's work on spectral synthesis; its explicit examples concern hyperplanes and paraboloids and do not establish the cubically fibered surface formula here. Classical finite-field extension theory on nondegenerate quadratic surfaces likewise has a different geometry and operator invariant. An earlier quadratic-fiber calculation for \(\{(x,y,xy^2)\}\) reduces to a two-phase cosine average; it does not determine the present three-phase magnitude multiset, its two possible trace ranks, or the joint three-step constant. The integral \(C_3\) itself belongs to established random-walk analysis and is not asserted to be new.

## Limitations

The stated formula is for the specific cubic-fiber monomial graph, not arbitrary quartic surfaces or general polynomial fibers. The limiting constant requires prime characteristic tending to infinity; the exact fixed-characteristic slopes are \(A_p/3\). Equivalence to an older result under finite-field monomial exponential-sum or Fourier-idempotent terminology remains a residual literature risk. No independent external audit or publication-priority certification is asserted.

## References

1. A. Iosevich, Z. Li and K. Yu, *Spectral synthesis with the complexity parameter in* \(\mathbb Z_N^d\), arXiv:2609.25404, first posted 2026-09-21, https://arxiv.org/abs/2609.25404.
2. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505, first posted 2008-04-28, https://arxiv.org/html/0804.4505v1.
3. J. M. Borwein, D. Nuyens, A. Straub and J. Wan, *Some arithmetic properties of short random walk integrals*, Ramanujan Journal 26 (2011), 109–132, DOI:10.1007/s11139-011-9325-y, https://arminstraub.com/pub/walks.
