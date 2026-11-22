# Third-order Bernoulli mimicry and a fourth-order obstruction in a noisy majority automaton

## Finding

In the two-parameter synchronous probabilistic cellular automaton of Muñoz and Nuño, a whole nontrivial parameter line produces **exactly fair, three-wise independent output spins after one update from independent fair input spins**, while still failing to preserve the fair Bernoulli product law. The first possible dependence is a computable four-spin parity interaction. This gives a sharp all-ring-size classification of when the fair product law is stationary.

More precisely, fix \(p,r\in[0,1]\). On a cyclic ring \(\mathbb Z/n\mathbb Z\), or on \(\mathbb Z\), start from independent fair spins \(X_i\in\{-1,1\}\). Conditional on \(X\), independently generate updated spins \(Y_i\) according to the model in the next section. Set \(u=2p-1\), \(v=2r-1\). For every cyclic ring of length \(n\ge5\), and for \(\mathbb Z\),
\[
\mathbb E Y_iY_{i+1}=\frac{uv}{2},\qquad
\mathbb E Y_iY_{i+2}=\frac{v^2}{4}.
\]
For \(r=1/2\), every family of at most three distinct updated spins is independent and fair. Nevertheless, for every four consecutive sites,
\[
\boxed{\mathbb E(Y_iY_{i+1}Y_{i+2}Y_{i+3})=\frac{u^4}{16}.}
\]
Thus the **complete four-consecutive-spin distribution** is
\[
\boxed{\Pr(Y_i=y_0,\ldots,Y_{i+3}=y_3)
 =\frac1{16}\left(1+\frac{u^4}{16}\prod_{j=0}^{3}y_j\right),\quad y_j\in\{-1,1\}.}
\]
In particular the output is an independent fair field on \(\mathbb Z\), or a uniform configuration on any ring of length at least five, **if and only if** \(p=r=1/2\). At \(r=1/2\), \(p\ne1/2\), the four-spin law is nonuniform despite all three-spin marginals being uniform.

The complete cyclic boundary classification is as follows: on rings with \(n=1\) or \(n=2\), the fair product law is preserved for every \(p,r\); on \(n=3\), it is preserved exactly when \(p+r=1\); on every \(n\ge4\), it is preserved exactly when \(p=r=1/2\). For \(n=4\) and \(r=1/2\), three-wise fairness still holds, but the four-spin moment is \(u^4/4\) rather than \(u^4/16\).

## Assumptions and scope

The neighborhood is the ordered triple \((X_{i-1},X_i,X_{i+1})\), with indices taken cyclically on rings. Given the previous configuration, the new spins at distinct sites are independent. If the two neighboring spins agree, the new spin agrees with them with probability \(r\). If the neighbors disagree, the new spin agrees with the old center with probability \(p\). These are exactly the conditional local laws of the probabilistic interpolation of Wolfram rules 23, 77, 178 and 232 in Muñoz--Nuño (2026), Table 2. Independent randomness is resampled at each site, and only **one update from a fair product initial law** is under study. The parameters may include their endpoints.

A family is *three-wise independent fair* if every selection of one, two, or three distinct sites has the uniform product distribution. A distribution is *fair product* when this holds for all finite selections. On a finite ring, that is the uniform distribution over its \(2^n\) configurations.

## Proof

**Step 1: exact conditional response.** In spins \(\{-1,1\}\), let \(m_i(X)=\mathbb E[Y_i\mid X]\). Directly from the two update cases,
\[
m_i(X)=\begin{cases}
 vX_{i-1},&X_{i-1}=X_{i+1},\\
 uX_i,&X_{i-1}\ne X_{i+1}.
\end{cases}
\]
Equivalently,
\[
\boxed{m_i(X)=\frac u2\bigl(X_i-X_{i-1}X_iX_{i+1}\bigr)
+\frac v2\bigl(X_{i-1}+X_{i+1}\bigr).}\tag{1}
\]
Given independent updates, for any set of distinct output sites \(S\),
\[
\mathbb E\prod_{i\in S}Y_i=\mathbb E\prod_{i\in S}m_i(X).\tag{2}
\]
Fair input spin monomials are orthogonal: the expectation of a product of input spins is zero unless every input-spin index appears an even number of times. This remains true for the cyclic model even when coordinate indices coincide modulo the ring length, provided one first reduces them modulo \(n\).

**Step 2: one- and two-spin laws.** Equation (1) consists entirely of odd-degree monomials, so \(\mathbb EY_i=0\). For \(n\ge5\), the only matching input-spin monomials between \(m_i\) and \(m_{i+1}\) are the terms containing \(X_i\) or \(X_{i+1}\), each contributing \(uv/4\). Hence the adjacent correlation equals \(uv/2\). For sites two apart, their only matching input-spin monomial is \(X_{i+1}\), contributing \(v^2/4\). All other pairs are uncorrelated since their input neighborhoods are disjoint (or their identical-spin monomials do not match). The same statements hold on \(\mathbb Z\). For \(n=4\), the two neighboring contributions in the distance-two pair coincide cyclically and the result is \(v^2/2\), while adjacent correlation remains \(uv/2\). For \(n=3\), the two-spin moment is \((u+v)^2/4\), as is checked directly from the three independent input spins.

**Step 3: three-wise independence on the balanced-majority line.** At \(v=0\), each \(m_i(X)\) is \(uX_i\) times the indicator that its neighbors disagree. The pair formulas and disjoint-window observation imply that every two distinct outputs are uncorrelated for \(n\ge4\) and on \(\mathbb Z\). All odd output-spin moments vanish because negating the entire fair input negates every conditional mean, and preserves its law. Thus all one-, two-, and three-spin moments at distinct sites vanish. Walsh inversion on any subset of at most three sites makes its law the uniform product law. This holds also at \(u=\pm1\), where some conditional updates are deterministic.

**Step 4: the sharp four-spin witness.** At \(v=0\), write
\[
m_i(X)=\frac u2 X_i(1-X_{i-1}X_{i+1}).
\]
For consecutive sites \(S=\{0,1,2,3\}\), expand
\[
\mathbb E\prod_{i=0}^{3}m_i(X)=\frac{u^4}{16}
\sum_{H\subseteq S}(-1)^{|H|}\,
\mathbb E\left[\prod_{i\in S}X_i\prod_{j\in H}X_{j-1}X_{j+1}\right].\tag{3}
\]
A term survives exactly when, over \(\mathbb F_2\), the set of indices appearing with odd multiplicity in the two products is empty. Equivalently, the incidence vectors satisfy
\[
\sum_{i\in S}e_i=\sum_{j\in H}(e_{j-1}+e_{j+1}),\tag{4}
\]
with indices modulo \(n\) on a ring. For \(n\ge6\) and for \(\mathbb Z\), the two outer coordinates \(-1\) and \(4\) force \(0,3\notin H\); the coordinates \(0,3\) then force \(1,2\in H\). For \(n=5\), the potentially identified outer coordinates require a separate check: equations at \(0,3,1,2\) successively force \(1,2\in H\) and \(0,3\notin H\). Thus for every \(n\ge5\) the **only** survivor is \(H=\{1,2\}\), with positive sign, and (3) equals \(u^4/16\). For \(n=4\), exactly four subsets survive: \(\{0,1\}\), \(\{1,2\}\), \(\{0,3\}\) and \(\{2,3\}\), all with positive signs, yielding \(u^4/4\). The complete four-word law follows by the Fourier--Walsh inversion formula; every proper nonempty subset has zero moment and only the full four-set contributes \(u^4/16\) or \(u^4/4\).

**Step 5: stationary fair-law classification.** On every ring with \(n\ge4\), preservation of the fair product law implies zero correlation at distance two, hence \(v=0\). Then preservation also requires the positive fourth-order witness to vanish, forcing \(u=0\). Conversely at \(u=v=0\) every site independently chooses a fair new spin, so the law is preserved. On \(n=3\), global spin-flip symmetry makes odd moments zero, and every nontrivial even moment is a pair moment \((u+v)^2/4\); Walsh inversion therefore shows the output is fair product exactly when \(u+v=0\), equivalently \(p+r=1\). For \(n=1\), the output is fair by spin-flip symmetry; for \(n=2\), each updated conditional mean depends only on the *other* input spin, so the two updated spins are independent fair. On \(\mathbb Z\), the same pair-and-four obstruction as for \(n\ge5\) proves the classification.

## Verification

Run `python verify_fair_pca.py` using only the Python standard library. It evaluates the update rule directly from its two cases rather than using the polynomial response (1), and computes moments by exact rational enumeration of fair input configurations. It performed **2,082 exact checks** over cyclic rings of lengths one through ten and six rational parameter pairs (including boundary cases), checking all claimed one- and two-point formulas, every output spin moment of order at most three on the balanced-majority line, the fourth-order formula, and the complete 16-point four-word law for selected rings. Every check passed. Equation (4) and the orthogonality proof, not this finite enumeration, establish the all-length and infinite-lattice results.

## Relationship to prior work

Muñoz and Nuño (2026), first publicly available 29 March 2026, introduce precisely this probabilistic local rule and derive stationary distributions for small rings. Their displayed formula for the three-site stationary law implies the special line \(p+r=1\) in that small case; it is **not claimed to be newly discovered here**. Their four-site transition matrix provides another finite-size route to one part of the boundary case. The new point here is the exact **all-size, one-update third-order independence and fourth-order parity interaction**, including the infinite lattice, with the resulting complete stationarity obstruction for fair product input.

The published published-finding corpus result *A sharp reversible line and odd--even correlation law for a two-parameter probabilistic cellular automaton* (2026) treats **detailed balance** and an explicit second-neighbor Ising stationary law along \(p=1/2\). This agrees with the fair stationary point \(p=r=1/2\) on that line; it does not provide the nontrivial off-reversible \(r=1/2\) three-wise-independent output or the \(u^4\) four-spin witness. The published published-finding corpus result *Exact dependence phases of elementary cellular-automaton Bernoulli images* (2026) classifies dependence of outputs of **deterministic** elementary rules; its product-input dependency framework is relevant but its stated classification does not cover independent randomized site updates in the two-parameter family.

Coe, Ahnert and Fink (2008) analyze randomness across *time* for deterministic and probabilistic cellular automata, with specific local-rule criteria. That is not a statement that a single updated spatial field has uniform marginals through order three but a nonuniform fourth moment. Lemoy, Mozeika and Seki (2013/2014) treat thermal noise applied to majority voting, with equilibrium transfer matrices and marginal/correlation results for a different thermal parameterization. The exact noisy-majority three-/four-spin one-step identity of the present theorem was not identified in the inspected material.

## Limitations

Only a single synchronous update from an **independent fair** initial field is addressed; the theorem does not characterize arbitrary initial measures, transition mixing rates, temporal correlations, or full stationary laws when the fair product law is not invariant. The three-site exceptional product-preservation line is already implied by the original finite-size calculation. Historical priority against unidentified generalized stochastic-block-moment results cannot be ruled out by searches. Independent review of the mathematical argument has not been performed.

## References

1. F. J. Muñoz and J. C. Nuño, *Probabilistic Cellular Automata: between deterministic Wolfram's rules 23, 77, 178 and 232*, arXiv:2603.27799, first posted 29 March 2026, https://arxiv.org/html/2603.27799 (see Table 2 and Section 4).
2. *A sharp reversible line and odd--even correlation law for a two-parameter probabilistic cellular automaton*, published-finding corpus research record `2026/11/1/SCOPE-a-sharp-reversible-line-and-odd-even-correlation-law-for-a-two-p--1b530a390287`, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-sharp-reversible-line-and-odd-even-correlation-law-for-a-two-p--1b530a390287.
3. *Exact dependence phases of elementary cellular-automaton Bernoulli images*, published-finding corpus research record `2026/10/25/SCOPE-exact-dependence-phases-of-elementary-cellular-automaton-bernoul--3b362554036a`, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-dependence-phases-of-elementary-cellular-automaton-bernoul--3b362554036a.
4. J. B. Coe, S. E. Ahnert and T. M. A. Fink, *When are cellular automata random?*, EPL **84** (2008), 50005, https://doi.org/10.1209/0295-5075/84/50005.
5. R. Lemoy, A. Mozeika and S. Seki, *Transfer matrix analysis of one-dimensional majority cellular automata with thermal noise*, Journal of Physics A **47** (2014), 105001; first preprint 18 November 2013, https://arxiv.org/abs/1311.4388.
