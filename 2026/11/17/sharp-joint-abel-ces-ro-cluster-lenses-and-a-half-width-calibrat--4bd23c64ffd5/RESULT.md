# Sharp joint Abel–Cesàro cluster lenses and a half-width calibration barrier

## Finding
For an infinite binary sequence \(a=(a_j)_{j\geq1}\in\{0,1\}^{\mathbb N}\), let
\[
C_n(a)=\frac1n\sum_{j=1}^n a_j,
\qquad
B_{n,\lambda}(a)=\frac{\lambda}{n}\sum_{j=1}^\infty
\left(1-\frac{\lambda}{n}\right)^{j-1}a_j,
\]
where \(\lambda>0\) is fixed and integers \(n>\lambda\) are considered. Set
\[
L_\lambda(u)=e^{-\lambda(1-u)}-e^{-\lambda},\qquad
U_\lambda(u)=1-e^{-\lambda u}+e^{-\lambda},
\quad 0\le u\le1.
\]
For every binary sequence, all subsequential limits of \((C_n(a),B_{n,\lambda}(a))\) belong to the exact closed lens
\[
\mathcal L_\lambda=\{(u,v):0\le u\le1,\ L_\lambda(u)\le v\le U_\lambda(u)\}.
\]
Moreover, there is one dense \(G_\delta\) subset \(\mathcal R\) of the Cantor space \(\{0,1\}^{\mathbb N}\) such that, **simultaneously for every real** \(\lambda>0\), each \(a\in\mathcal R\) has joint cluster set precisely \(\mathcal L_\lambda\).

The largest vertical diameter of these lenses is
\[
\sup_{0\le u\le1}\bigl(U_\lambda(u)-L_\lambda(u)\bigr)
=1+2e^{-\lambda}-2e^{-\lambda/2}
=\frac12+2\left(e^{-\lambda/2}-\frac12\right)^2.
\]
Consequently the sharp minimax diameter over all fixed positive discount rates is \(1/2\), attained at the **unique** rate \(\lambda=2\log2\). Thus a single exponential discount calibrated at the scale \(1/n\) cannot make the conditional Abel value determined to within an interval shorter than \(1/2\) by knowing only the contemporaneous Cesàro proportion; even the optimal calibration leaves that exact worst-case ambiguity.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\); \(n\) ranges over positive integers sufficiently large relative to any fixed \(\lambda>0\). The joint cluster set consists of finite limits of \((C_{n_k},B_{n_k,\lambda})\) along unbounded increasing integer subsequences. Topological terms refer to the product topology of the full binary sequence space. No mixing, stationarity, convergence, or regularity of the input is assumed.

For a **finite** length \(n\), put \(p=\lambda/n\in(0,1)\), \(q=1-p\), and fix exactly \(k\) ones among the first \(n\) coordinates. Among **all infinite binary extensions**, the exact sharp bounds are
\[
q^{n-k}-q^n\ \le B_{n,\lambda}(a)\ \le1-q^k+q^n.
\]
The lower bound is attained by placing those ones at the last \(k\) prefix positions and setting every later digit to zero. The upper bound is attained by placing them first and setting every later digit to one. These are bounds on the full discounted sum, not a claim that every intermediate real value is attained at a fixed finite length.

The maximum finite-prefix uncertainty width, over all possible prefix counts, is exactly
\[
1+2q^n-q^{\lfloor n/2\rfloor}-q^{\lceil n/2\rceil}.
\]
The formula follows because the strictly convex function \(k\mapsto q^k+q^{n-k}\) has its minimum at the central integer or integers. For every even \(n\), minimizing this width over \(0<p<1\) gives precisely \(1/2\), attained uniquely at \(p=1-2^{-2/n}\). The limiting optimal calibration below is the corresponding fixed-rate form. This uses extremal ranges, not the assertion of finite-level interval filling.

## Proof
**1. Finite extremizers.** In the prefix the geometric coefficients \(p q^{j-1}\) decrease strictly with \(j\). With \(k\) ones, their smallest possible sum uses positions \(n-k+1,\ldots,n\) and equals \(q^{n-k}-q^n\); their largest uses positions \(1,\ldots,k\) and equals \(1-q^k\). The unconstrained tail has nonnegative coefficient mass exactly \(q^n\). Choosing its digits identically zero or one proves the finite formulas and attainment.

**2. Continuum necessity.** If \(n_j\to\infty\) and \(C_{n_j}(a)=k_j/n_j\to u\), then \((1-\lambda/n_j)^{n_j-k_j}\to e^{-\lambda(1-u)}\), \((1-\lambda/n_j)^{k_j}\to e^{-\lambda u}\), and \((1-\lambda/n_j)^{n_j}\to e^{-\lambda}\). The finite bounds imply every joint subsequential limit lies in \(\mathcal L_\lambda\).

**3. Approximation of every lens point after any prescribed finite prefix.** Fix \(\lambda>0\), a target \((u,v)\in\mathcal L_\lambda\), and a finite binary word of prescribed initial digits. Let \(\theta\in[0,1]\) satisfy \(v=(1-\theta)L_\lambda(u)+\theta U_\lambda(u)\) (if the endpoints coincide choose any \(\theta\)). Define on \([0,\infty)\)
\[
f_-(t)=\mathbf1_{(1-u,1]}(t),\qquad
f_+(t)=\mathbf1_{[0,u]}(t)+\mathbf1_{(1,\infty)}(t),\qquad
f(t)=(1-\theta)f_-(t)+\theta f_+(t).
\]
Then \(\int_0^1 f(t)\,dt=u\), and direct integration gives
\[
\int_0^\infty\lambda e^{-\lambda t}f(t)\,dt
=(1-\theta)L_\lambda(u)+\theta U_\lambda(u)=v.
\]
Choose a large finite cutoff \(T>1\) so the exponential mass after \(T\) is less than a prescribed error. On the index interval after the fixed prefix and up to \(Tn\), use digits with the following balanced-rounding rule: set the digit at index \(j\) to the difference of successive integer parts of the cumulative sum of \(f((i-1/2)/n)\) over the not-yet-prescribed indices. Because each summand is in \([0,1]\), all chosen digits are binary, and cumulative count discrepancy from the sampled control is at most one. Set the digits beyond \(Tn\) to zero. As \(n\to\infty\), the prescribed prefix is negligible, the ordinary prefix average converges to \(u\), and summation by parts plus Riemann convergence shows the discounted sum converges to the truncated exponential integral, whose tail error is arbitrarily small. Hence for every finite initial word, every error tolerance and every lower bound on \(n\), a finite extension exists that makes both averages that close to \((u,v)\).

**4. Simultaneous residual universality.** For every rational \(\lambda>0\), rational \(u,\theta\in[0,1]\), and positive integers \(m,N\), consider the union over integers \(n\ge N\), \(n>\lambda\), of sets where the two averages are each within \(1/m\) of the target \((u,(1-\theta)L_\lambda(u)+\theta U_\lambda(u))\). The sets are open in the Cantor space: the finite prefix mean is continuous, and the geometric series is a uniform limit of continuous cylinder functions. Step 3 makes each union dense. The Baire category theorem therefore supplies one dense \(G_\delta\) set whose sequences visit every rational-parameter rational-target neighborhood at arbitrarily large indices.

For fixed \(n>\lambda,\mu>0\), differentiation of geometric coefficients gives
\[
\sum_{j\ge1}\left|\frac{\partial}{\partial\lambda}
\left[\frac\lambda n(1-\lambda/n)^{j-1}\right]\right|\le\frac2\lambda.
\]
Indeed the sum is at most \(1/\lambda\) plus \(\mathbb E(J-1)/(n-\lambda)=1/\lambda\) for the geometric law with success probability \(\lambda/n\). Integrating yields the **uniform-in-\(n\)** parameter bound
\[
|B_{n,\lambda}(a)-B_{n,\mu}(a)|
\le\frac{2|\lambda-\mu|}{\min(\lambda,\mu)}
\quad(n>\max(\lambda,\mu)).
\]
Continuity of \(L_\lambda,U_\lambda\), density of rational \((u,\theta)\), and this estimate allow the rational parameter to approach **any** real positive \(\lambda\) along increasing indices. Thus every point of every \(\mathcal L_\lambda\) is a cluster point for every sequence in the same residual set. Step 2 gives the converse.

**5. Exact calibration.** With \(z=e^{-\lambda/2}\in(0,1)\), the difference of the boundary functions is
\(1+2z^2-e^{-\lambda u}-e^{-\lambda(1-u)}\). The arithmetic–geometric mean inequality gives
\(e^{-\lambda u}+e^{-\lambda(1-u)}\ge2z\), with equality only for \(u=1/2\). Thus the worst vertical width is \(1-2z+2z^2=1/2+2(z-1/2)^2\). Its unique minimum occurs at \(z=1/2\), equivalently \(\lambda=2\log2\), proving the claimed sharp barrier.

## Verification
The standard-library Python file `check_abel_lens.py` independently exhausts the finite conditional bounds by exact rational arithmetic for all binary prefixes of lengths \(2\) through \(11\) and four rational discount probabilities. It also checks the exact half-width identity on even lengths and constructs balanced binary approximations for several interior continuum points. Execution returned all checks passing. The Baire-category argument and unrestricted universal quantifiers are analytical; finite tests do not establish them.

## Relationship to prior work
Classical Abelian/Tauberian literature compares convergence or summability, rather than the entire two-observable cluster set of a fixed binary input under horizon-matched discounting. Estrada and Vindas (2012) treat converse Abel-to-Cesàro theorems under analytic/distributional hypotheses. Ziliotto (2015) proves a convergence equivalence for appropriate nonexpansive operators and studies game-theoretic exceptions; this is not a conditional lens theorem for arbitrary infinite binary sequences. Abadias–Lizama–Miana–Velasco (2015, §5.1) give Abel/Cesàro operator subordination and boundedness, not a sharp finite-prefix conditional interval or universal residual cluster classification.

Related exact analyses determine either the joint cluster lens of **first and second Cesàro iterations** or the **unconditional** minimax discrepancy of universal Abel–Cesàro operator averages. Neither statement supplies this exponential-tail conditional region, its simultaneous-for-all-discounts residual realization, or the uniquely optimal half-width calibration. A general rearrangement principle explains the finite endpoint ordering but alone does not prove the topological joint-realization theorem. Historical priority is qualified by the possibility of older equivalent formulations under different summability terminology.

## Limitations
The results concern binary sequences and geometric discounts of the specific horizon-matched form \(\lambda/n\), with \(\lambda\) fixed when taking subsequential limits. They do not classify the joint cluster set of an arbitrary individual sequence, cover changing discount scales \(\lambda_n\) without further hypotheses, or give a corresponding sharp lens for nonbinary alphabets. The residual universality statement is topological, not probabilistic or almost-sure under Bernoulli measure. 

## References
1. R. Estrada and J. Vindas, *Distributional versions of Littlewood's Tauberian theorem*, arXiv:1201.1408, initial submission 2012-01-06, https://arxiv.org/abs/1201.1408.
2. B. Ziliotto, *A Tauberian theorem for nonexpansive operators and applications to zero-sum stochastic games*, arXiv:1501.06525, initial submission 2015-01-26, https://arxiv.org/abs/1501.06525.
3. L. Abadias, C. Lizama, P. J. Miana, and M. P. Velasco, *Cesàro sums and algebra homomorphisms of bounded operators*, arXiv:1504.01357, initial submission 2015-04-06, https://arxiv.org/abs/1504.01357.
4. R. D. Lord, *On Some Relations Between the Abel, Borel, and Cesàro Methods of Summation*, Proc. London Math. Soc. s2-38 (1935), 241–256, DOI 10.1112/plms/s2-38.1.241. Historical background; full text not inspected.
