# The sharp antipodal rigidity window for nonnegative multiples of \(\Phi_{70}\)

## Finding

Let \(F\in\mathbb R[X]\) be nonzero with nonnegative coefficients, and write \(D(F)=\max\operatorname{supp}(F)-\min\operatorname{supp}(F)\). If \(\Phi_{70}\mid F\) and \(D(F)\le53\), then necessarily
\[
F(X)=X^b(1+X^{35})H(X),\qquad b\in\mathbb Z_{\ge0},\quad H\in\mathbb R_{\ge0}[X]\setminus\{0\},\quad\deg H\le18.
\]
Conversely, every such polynomial is divisible by \(\Phi_{70}\) and has diameter at most \(53\). Equivalently, the cone of nonnegative multiples supported in the fixed interval \(0,\ldots,53\) is simplicial with exactly nineteen extreme rays \(X^j(1+X^{35})\), \(0\le j\le18\). The cutoff is **sharp**: a nonnegative, nonzero multiple of \(\Phi_{70}\) of diameter \(54\) exists that is not divisible by \(1+X^{35}\). Hence \(54\) is the least support diameter of a nonnegative cyclotomic multiple at index \(70\) that cannot be decomposed into antipodal pairs.

The exceptional polynomial is
\[
W(X)=\sum_{e\in E}X^e,\quad E=\{0,1,3,11,12,13,14,23,31,40,41,42,43,51,53,54\}.
\]

## Assumptions and scope

The divisibility condition is in \(\mathbb R[X]\), so **arbitrary nonnegative real coefficients**, not only integer or rational ones, are permitted. The support comprises indices with strictly positive coefficients. The zero polynomial is excluded. All exponent bounds concern the difference between greatest and least occupied indices, and are invariant under multiplication by a monomial. This result is confined to the cyclotomic index \(70=2\cdot5\cdot7\); it makes no assertion for other indices or for signed coefficients.

## Proof

**1. An exact separating functional.** Put \(P(X)=\Phi_{70}(X)\). Direct computation from \(X^{70}-1=\prod_{d\mid70}\Phi_d(X)\) gives
\[
\begin{aligned}
P(X)={}&1+X-X^5-X^6-X^7-X^8+X^{10}+X^{11}+X^{12}+X^{13}+X^{14}\\
&-X^{16}-X^{17}-X^{18}-X^{19}+X^{23}+X^{24}.
\end{aligned}
\]
For any polynomial \(G\), let \(R(G)\) be the remainder of division by the monic polynomial \(P\), of degree less than \(24\). Define the real-linear functional
\[
L(G)=2[X^{19}]R(G)+[X^{20}]R(G)+2[X^{21}]R(G)+[X^{22}]R(G)+[X^{23}]R(G).
\]
Here \([X^j]\) denotes coefficient extraction. Exact integer polynomial reduction yields, for every integer \(0\le j\le53\),
\[
L(X^j)=\begin{cases}w_{j-19},&19\le j\le34,\\0,&0\le j\le18\text{ or }35\le j\le53,\end{cases}
\]
where, in increasing order of \(j\),
\[
(w_0,\ldots,w_{15})=(2,1,2,1,1,1,2,3,3,2,1,1,1,2,1,2).
\]
All sixteen weights are **strictly positive**. These are finite identities in \(\mathbb Z[X]/(P)\), not numerical approximations. They can be reproduced by the included dependency-free `verify.py`; alternatively, use the monic relation \(X^{24}\equiv-\sum_{i=0}^{23}[X^i]P\,X^i\pmod P\) iteratively.

**2. Rigidity for every nonnegative real multiple.** Divide out the lowest monomial of \(F\), giving \(G=\sum_{j=0}^{D}c_jX^j\) with \(c_0>0\), \(c_j\ge0\), \(D\le53\), and \(P\mid G\) because \(P(0)=1\). Hence \(L(G)=0\). The displayed table forces \(c_{19}=\cdots=c_{34}=0\). Thus
\[
G(X)=A(X)+X^{35}B(X),\quad\deg A,\deg B\le18,
\]
with \(A,B\) nonnegative; a missing block is understood as the zero polynomial. Since every primitive \(70\)-th root \(\zeta\) satisfies \(\zeta^{35}=-1\), we have \(P\mid(1+X^{35})\) and so \(P\mid(A-B)\). But \(\deg(A-B)\le18<\deg P=24\), forcing \(A=B\). The stated factorization follows with \(H=A\). Conversely \(P\mid1+X^{35}\), and \(D(X^b(1+X^{35})H)=35+\deg H-\operatorname{ord}_X(H)\le53\) for every nonzero \(H\ge0\) of degree at most \(18\).

**3. Sharpness at the next degree.** For the sixteen-exponent polynomial \(W\) in the statement, exact multiplication verifies the identity \(W(X)=P(X)Q(X)\), where
\[
\begin{aligned}
Q(X)={}&1+X^3-X^4+2X^5-X^6+2X^7+X^{10}+2X^{12}+X^{14}+X^{16}\\
&+2X^{18}+X^{20}+2X^{23}-X^{24}+2X^{25}-X^{26}+X^{27}+X^{30}.
\end{aligned}
\]
Every coefficient of \(W\) is either zero or one, and its occupied extremes are \(0\) and \(54\), so \(D(W)=54\). If \(1+X^{35}\mid W\), then because \(\deg W<70\), its coefficients in positions \(0\) and \(35\) would agree. They are respectively \(1\) and \(0\), a contradiction. This completes the sharpness proof.

## Verification

Run `python3 verify.py` using Python's standard library. It reconstructs \(\Phi_{70}\) independently from the cyclotomic factorization, checks all \(54\) zero/positive separation identities and the boundary coefficient at degree \(54\), verifies exact divisibility of \(W\) by \(\Phi_{70}\), and checks that \(W\) is not divisible by \(1+X^{35}\). The expected final status is `VERIFY_OK`. The universal assertion for all real coefficient vectors follows from the proof's linearity and positivity, not from finite sampling.

## Relationship to prior work

Tan and Zhang's 2026 theorem establishes the universal minimum diameter \(N(1-1/p)\) and characterizes equality; at \(N=70\) this minimum is \(35\). The result above instead identifies **the entire nonnegative coefficient cone through diameter \(53\)** and its first escape at \(54\), a different optimization constraint. Their quantitative near-equality theorem controls concentration near a regular polygon but does not in its stated form give this exact finite threshold. Steinberger's earlier work derives cyclotomic linear certificates for the smallest-degree problem, including indices with three prime factors, but does not report the present sharp antipodal cutoff. Christie–Dykema–Klep classify minimal vanishing sums of small *weight*, including order-\(70\) types; weight classification neither bounds the diameter of arbitrary (possibly high-weight) nonnegative real combinations nor gives the current exact coefficient-cone assertion without additional analysis. The explicit \(16\)-term witness should not be mistaken for a claim that its underlying vanishing-sum type is new.

## Limitations

This is a single-index finite structural theorem, not an asymptotic or a universal formula for all cyclotomic indices. It does not enumerate all exceptional rays at diameter \(54\), nor identify the smallest *weight* of a non-antipodal vanishing sum. An independent mathematical audit has not been performed; comparisons may miss unindexed preexisting diameter-specific tables. The finite remainder calculations are exact and their relevance to all real coefficients is justified algebraically above.

## References

1. H. Tan and Y. Zhang, *Sharp Diameter Bounds for Nonnegative Cyclotomic Multiples*, arXiv:2609.07646v1 (first publicly submitted 2026-09-07), https://arxiv.org/abs/2609.07646.
2. J. P. Steinberger, *The lowest-degree polynomial with nonnegative coefficients divisible by the \(n\)-th cyclotomic polynomial*, Electronic Journal of Combinatorics 19(4) (2012), P1.
3. L. Christie, K. J. Dykema and I. Klep, *Classifying minimal vanishing sums of roots of unity*, arXiv:2008.11268 (first submitted 2020-08-25; revised 2025-12-16), https://arxiv.org/abs/2008.11268.
