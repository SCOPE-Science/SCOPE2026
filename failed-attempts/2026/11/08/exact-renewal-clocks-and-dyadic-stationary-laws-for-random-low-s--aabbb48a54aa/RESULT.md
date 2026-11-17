# Exact renewal clocks and dyadic stationary laws for random low-slope interval maps

## Finding
For the random interval-map family described below, visits to the upper half of the unit interval form an **exact ordinary renewal process**, for every probability distribution of the reset parameter (including infinite-mean distributions). Return coordinates are independently uniform; the excursions have a simple generating function. The same structure produces a canonical, exact, piecewise constant invariant density on all dyadic shells and a closed generating function for return correlations when the invariant measure is finite.

Write \(P(z)=\sum_{b\ge1}p_bz^b\). With an independent geometric random variable \(G\) satisfying \(\Pr(G=g)=2^{-g-1}\), the successive excursion lengths are independent copies of \(\tau=B+G+1\), where \(B\sim p\). Consequently, for \(0\le z<1\),
\[
F(z)=\mathbb E[z^\tau]=\frac{zP(z)}{2-z},\qquad
U(z)=\sum_{n\ge0}u_nz^n=\frac{2-z}{2-z-zP(z)},
\]
where \(u_n\) is the probability, starting uniformly on the return section, of being on that section at time \(n\).

Let \(J_0=(1/2,1]\) and \(J_j=(2^{-j-1},2^{-j}]\) for integers \(j\ge1\). The exact mass of the canonical invariant measure with \(\nu(J_0)=1\) is
\[
\nu(J_j)=q_j:=\Pr(B+G\ge j)
=\sum_{b\ge j}p_b+\sum_{1\le b<j}p_b2^{b-j},\quad j\ge1.
\]
Therefore \(\nu((0,1])=\mathbb E[B]+2\), possibly infinite, giving a sharp exact normalization and finite/infinite phase criterion. If \(\mathbb E[B]<\infty\), the normalized stationary probability \(\pi=\nu/(\mathbb E[B]+2)\) satisfies
\[
\operatorname{Cov}_\pi(\mathbf1_{J_0}(X_0),\mathbf1_{J_0}(X_n))
=\pi(J_0)\bigl(u_n-\pi(J_0)\bigr),\quad \pi(J_0)=\frac1{\mathbb E[B]+2}.
\]
For the deterministic reset parameter \(B=1\), this yields the all-lag identity
\[
\operatorname{Cov}_\pi(\mathbf1_{J_0}(X_0),\mathbf1_{J_0}(X_n))
=\frac29\left(-\frac12\right)^n,\quad n\ge0.
\]

## Assumptions and scope
At each original discrete time, independently sample an integer \(B_t\ge1\) with \(\Pr(B_t=b)=p_b\), \(\sum_{b\ge1}p_b=1\). The state \(X_t\in[0,1]\) evolves under
\[
T_b(x)=\begin{cases}2x,&0\le x\le1/2,\\2^{-b}(2x-1),&1/2<x\le1.\end{cases}
\]
All probabilistic laws below are **annealed** over the sequence of independent random map choices. Starting from the section \(Y=J_0\), use normalized Lebesgue measure on \(Y\), with density \(2\). On the stationary probability space, use the normalized measure \(\pi\) above. Endpoints and the fixed point \(0\) are ignored in assertions about equivalent measures and almost-sure return laws; this qualification is essential because \(0\) supports an additional singular invariant atom. No finite-moment hypothesis is used for the renewal or sigma-finite invariant-measure formulas; the covariance formula requires \(\mathbb E[B]<\infty\).

## Proof
**1. Excursion digit decomposition.** Put \(Y=(1/2,1]\) and write \(y=2x-1\) for a section point \(x\in Y\). Under normalized Lebesgue measure on \(Y\), \(y\) is uniform on \((0,1]\). At the first map application the orbit is \(2^{-B}y\), after which every step is the deterministic left-branch doubling map until the next visit to \(Y\). There is a unique nonnegative integer \(G\) satisfying \(2^{-G-1}<y\le2^{-G}\). This event has probability \(2^{-G-1}\), independent of the sampled reset \(B\). The orbit spends \(B+G\) steps outside the return section, so its first return occurs at \(\tau=B+G+1\) and its return position is \(X_\tau=2^G y\in Y\).

Conditional on \(B=b,G=g\), the variable \(y\) is uniform on \((2^{-g-1},2^{-g}]\), hence \(2^g y\) is uniform on \(Y\). This is a stronger property than uniformity of the induced invariant measure: the return point is independent of the entire current excursion label \((B,G)\). Since future sampled maps are independent of past maps and the section point, induction yields independent and identically distributed excursion labels, lengths, and independently uniform returned positions. This also proves almost-sure recurrence by finiteness of each integer excursion length, even when its expectation is infinite.

**2. Generating functions.** The geometric-digit variable has generating function \(\mathbb E[z^G]=\sum_{g\ge0}2^{-g-1}z^g=(2-z)^{-1}\). Hence \(F(z)=zP(z)/(2-z)\). With \(S_0=0\) and \(S_k\) the sum of the first \(k\) excursion lengths, visit times are exactly the renewal times, so \(u_n=\sum_{k\ge0}\Pr(S_k=n)\). For \(0\le z<1\), Tonelli's theorem yields \(U(z)=\sum_{k\ge0}F(z)^k=1/(1-F(z))\), as displayed.

**3. Exact invariant shell masses.** Define \(q_j=\Pr(B+G\ge j)\) for \(j\ge1\), and \(q_0=1\). The formula for \(q_j\) follows by conditioning on \(B\). Put a piecewise constant nonnegative density \(h\) on \((0,1]\) by
\[
h(x)=2\text{ on }J_0,\qquad h(x)=2^{j+1}q_j\text{ on }J_j\ (j\ge1).
\]
Then \(\nu(J_0)=\tfrac12(2)=1\) and \(\nu(J_j)=q_j\). We verify the annealed Frobenius–Perron equation. For a target point in \(J_0\), only the left inverse contributes, with density \(h|_{J_1}/2=2q_1=2=h|_{J_0}\), since \(q_1=1\). For a target point in \(J_j\), \(j\ge1\), the left inverse contributes \(h|_{J_{j+1}}/2=2^{j+1}q_{j+1}\), while the right inverse for each \(b\le j\) contributes \(p_b 2^b\) because its derivative is \(2^{1-b}\) and its section density is \(2\). The exact identity
\[
q_j-q_{j+1}=2^{-j-1}\sum_{b\le j}p_b2^b
\]
therefore gives \(2^{j+1}q_{j+1}+\sum_{b\le j}p_b2^b=2^{j+1}q_j=h|_{J_j}\). Thus \(\nu\) is invariant. Since \(q_j>0\) for every \(j\), it is equivalent to Lebesgue measure on \((0,1]\), and since each \(q_j\le1\), it is sigma-finite. Finally Tonelli and the tail-sum formula give
\[
\nu((0,1])=1+\sum_{j\ge1}\Pr(B+G\ge j)=1+\mathbb E[B+G]=\mathbb E[B]+2.
\]
This proves the finite/infinite criterion without applying any unjustified interchange of signed infinite sums.

**4. Stationary correlations.** For finite \(\mathbb E[B]\), normalization gives \(\pi(Y)=1/(\mathbb E[B]+2)\). The conditional law of \(X_0\) given \(X_0\in Y\) under \(\pi\) is uniform on \(Y\); hence \(\Pr_\pi(X_n\in Y\mid X_0\in Y)=u_n\). Subtracting the square of the stationary mean proves the covariance identity. For \(p_1=1\), algebra gives \(U(z)=(2-z)/((1-z)(2+z))\), whose coefficients are \(u_n=\tfrac13+\tfrac23(-\tfrac12)^n\), yielding the displayed exact covariance.

## Verification
The standalone Python 3 checker `checker.py` uses rational arithmetic, not floating-point approximations. It tests six distinct finitely supported parameter distributions, 282 instances of the transfer-operator identities, 270 renewal generating-function identities, 100 two-digit conditional-uniformity intersection identities, and 50 instances of the closed-form deterministic-reset covariance. Execute in the same directory with `python3 checker.py`; a successful run prints `PASS`. This is **finite corroboration**, not a proof for all countable laws; the proof above establishes those quantifiers.

## Relationship to prior work
Inoue and Toyokawa's 2023 article defines exactly these low-slope maps in Section 4.1 and proves existence of a Lebesgue-equivalent conservative ergodic sigma-finite invariant measure together with **asymptotic comparability** of dyadic shell masses (Proposition 4.1). Their earlier April 2022 proceedings article gives the same map and a corresponding comparability result (Example 1). Consequently neither the map's construction nor the existence/finiteness framework is claimed as new here. The claim assessed here is the explicit i.i.d. excursion decomposition, full generating function of return probabilities, exact shell normalization for every reset law, and observable stationary correlation identity. General first-return/inducing theory supplies a framework, but the independence of successive return coordinates and the precise return-time law are verified directly for this map.

## Limitations
The statements concern the specified random affine family with i.i.d. parameter choices and annealed laws, not its arbitrary deterministic environments or general piecewise-convex maps. There is no claim of independence of observations at every original map time: only excursion records and induced return positions have the stated independent structure. The singular invariant atom at zero is outside the Lebesgue-equivalent measure classification. The exact formulas for \(\pi\) and its covariance require a finite first moment. The Japanese proceedings article is dated only to April 2022 in the available bibliographic record; the verified date `2023-03-20` attached to the 2023 arXiv source is that *source's* first public version date, not a claim that the mathematical model first appeared then. Potential equivalent expressions in older general first-return literature or non-indexed material remain a priority risk.

## References
1. Tomoki Inoue and Hisayoshi Toyokawa, *Invariant measures for random piecewise convex maps*, arXiv:2303.10873, version 1 publicly posted 2023-03-20, Section 4.1, Proposition 4.1. https://arxiv.org/abs/2303.10873
2. Tomoki Inoue and Hisayoshi Toyokawa, *区分的に凸なランダム写像の不変測度について*, RIMS Kôkyûroku 2217 (2022-04), 127–136, Example 1. https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/2217-11.pdf
3. Tomoki Inoue, *First return maps of random maps and invariant measures*, Nonlinearity (2020), DOI: 10.1088/1361-6544/ab4c83, general inducing context; complete text not inspected.
4. Kalle and Maggioni, *Invariant densities for random systems of the interval*, arXiv:1805.11430; its expansion assumptions do not cover the present low-slope right branch.
