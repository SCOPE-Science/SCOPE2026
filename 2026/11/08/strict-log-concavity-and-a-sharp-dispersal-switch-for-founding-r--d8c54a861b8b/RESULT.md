# Strict log-concavity and a sharp dispersal switch for founding reproductive pairs

## Finding

In the two-patch capacity-three sexual-reproduction chain defined below, let \(F(a,b)\) be the probability that a reproductive pair (at least two individuals) is founded in the initially empty patch before reproduction becomes impossible. For all \(a,b>0\), \(\log F(a,b)\) has a **negative-definite Hessian** in the two successful-birth rate parameters. In particular, it is jointly strictly concave.

Allocate a total attempt-rate coefficient \(B>0\) between natal and migrant offspring. If \(m\in[0,1]\) is the migrant fraction and \(h\in(0,1]\) is survival in transit, then \(a=B(1-m)\) and \(b=Bhm\). The establishment probability has a unique global maximizing policy, classified completely as follows.

* If \(0<B\le9\), that policy is full dispersal \(m=1\), for every \(h\in(0,1]\).
* If \(B>9\), let \(h_c(B)\) denote the unique zero in \((0,1)\) of

\[
\begin{aligned}
Q_B(h)={}&228B^4h^4 + (2025B^3-65B^4)h^3 \\
 &+(6714B^2-493B^3)h^2 +(10320B-1080B^2)h \\
 &+6048-672B.
\end{aligned}
\]

For \(0<h<h_c(B)\), the unique optimum satisfies \(0<m_*<1\). For \(h_c(B)\le h\le1\), the unique optimum is \(m_*=1\). The internal maximizer is the unique interior root of \(\partial_mF(B(1-m),Bhm)=0\). In every admissible case, \(m=0\) has zero establishment probability and is not optimal.

Thus a positive allocation to natal reproduction is favored only when the total fecundity coefficient exceeds the sharp value \(9\) (with individual death rate normalized to one) and migrant survival lies below a second exact threshold.

## Assumptions and scope

There are exactly two habitat patches, each with three distinguishable capacity slots. Write \((X_t,Y_t)\) for the numbers of occupied slots, initially \((X_0,Y_0)=(3,0)\). Every individual dies independently at rate one. For a donor patch with \(i\) individuals and destination patch with \(j\) individuals, its successful birth into the destination is at rate

\[
\frac{r\,i(i-1)(3-j)}6,
\]

where \(r=a\) if donor and destination are the same patch, and \(r=b\) if they are different. Birth attempts requiring fewer than two donors or a vacant destination do nothing. There are no spontaneous immigrants and no movement of surviving adults. The factor \(i(i-1)\) models a two-parent requirement; these rates define the complete continuous-time Markov chain. The finite dispersal budget describes probabilities of sending a newborn, not migrating adults.

Define \(\tau=\inf\{t\ge0:Y_t\ge2\}\) and \(F(a,b)=\mathbb P_{(3,0)}(\tau<\infty)\). Reaching two individuals in the destination is a **first-pair event**, not a claim of indefinite ecological persistence. The destination may subsequently go extinct. For the optimization claim, \(B>0\), \(0<h\le1\), and \(0\le m\le1\). The corresponding rates are \(a=B(1-m)\) and \(b=Bhm\). The zero-cost baseline \(m=0\) is allowed through continuity.

## Proof

**Step 1: Exact absorption system.** Before \(Y_t\) first reaches two, a state with \(X_t<2\) has no reproductively capable patch and can never succeed. The remaining transient states, in order, are \((2,0),(3,0),(2,1),(3,1)\). Their success probabilities form the vector \(u\) satisfying \(Mu=v\), with

\[
M=\begin{pmatrix}
2+a/3+b&-a/3&-b&0\\
-3&3+3b&0&-3b\\
-1&0&3+a/3+2b/3&-a/3\\
0&-1&-3&4+2b
\end{pmatrix},\quad
v=\begin{pmatrix}0\\0\\2b/3\\2b\end{pmatrix}.
\]

The second coordinate, \(F(a,b)=u_2\), simplifies to

\[
F(a,b)=\frac{b^2J(a,b)}{D(a,b)},
\]

where

\[
\begin{aligned}
J(a,b)={}&a^2+5ab+21a+6b^2+45b+84,\\
D(a,b)={}&a^2b^2+5ab^3+21ab^2+15ab+3a\\
&+6b^4+45b^3+141b^2+195b+108.
\end{aligned}
\]

Both \(J\) and \(D\) are positive for \(a,b\ge0\), and \(F(a,b)>0\) for \(b>0\). The coefficient calculation is a finite linear-system identity, verified exactly in the included checker.

**Step 2: Joint strict log-concavity.** Put \(L=\log F=2\log b+\log J-\log D\), on \(a,b>0\). For variables \(z,w\in\{a,b\}\), the rational identity

\[
\partial_{zw}\log P=\frac{P\,P_{zw}-P_zP_w}{P^2}
\]

for a positive polynomial \(P\) makes every Hessian entry explicitly rational. Exact expansion gives

\[
-L_{aa}=\frac{U(a,b)}{J^2D^2},\qquad
-L_{bb}=\frac{V(a,b)}{b^2J^2D^2},\qquad
\det \nabla^2L=\frac{W(a,b)}{b^2J^3D^3}.
\]

The exhaustive coefficient certificate `hessian_certificate.json` specifies every nonzero coefficient of \(U,V,W\) as an integer monomial table, with respectively \(37\), \(58\) and \(79\) terms. **Every listed coefficient is strictly positive.** The accompanying exact checker reconstructs these three numerator identities directly from \(J,D\) and checks every coefficient and denominator, not merely evaluations at sample points. Therefore \(L_{aa}<0\) and \(\det\nabla^2L>0\) for all \(a,b>0\), proving that the Hessian of \(L\) is negative definite. Consequently \(m\mapsto\log F(B(1-m),Bhm)\) is strictly concave on \((0,1)\).

**Step 3: Classify the budget optimum.** The probability is zero at \(m=0\), positive for \(m>0\), and behaves as a positive constant times \(m^2\) near zero. Strict concavity of its logarithm implies that its logarithmic derivative is strictly decreasing. A unique interior maximum exists if and only if the derivative at the other endpoint \(m=1\) is negative; otherwise \(m=1\) is the unique maximum. Exact substitution gives

\[
\left.\frac{dF(B(1-m),Bhm)}{dm}\right|_{m=1}
=\frac{B^2h^2Q_B(h)}{3(B^2h^2+5Bh+9)^2(2B^2h^2+5Bh+4)^2}.
\]

For \(B\le9\), every coefficient of \(Q_B\) as a polynomial in \(h\) is nonnegative, and at least one is positive for \(h>0\). For \(B>9\), the ascending coefficients of its constant, linear, quadratic, cubic, and quartic terms change from positive to negative, as \(B\) increases, at

\[
9,\quad\frac{86}{9},\quad\frac{6714}{493},\quad\frac{405}{13},\quad\text{and never},
\]

respectively. These breakpoints are strictly increasing. Thus the ordered coefficient signs of \(Q_B\) (from constant to quartic) have **exactly one sign change** for every \(B>9\). Descartes' rule gives at most one positive zero. But \(Q_B(0)=672(9-B)<0\) and

\[
Q_B(1)=163B^4+1532B^3+5634B^2+9648B+6048>0.
\]

There is therefore exactly one root \(h_c(B)\in(0,1)\) and the sign pattern stated in the finding follows. Strict concavity supplies global optimality and uniqueness, including the endpoint equality case.

## Verification

Run `python verify.py` in the directory containing `verify.py` and `hessian_certificate.json`, with SymPy installed. The script reconstructs the exact four-state system and success formula; recomputes all \(174\) positive monomial terms of the three Hessian certificates and the exact rational denominators; verifies the optimal-boundary derivative and the ordered threshold signs; and compares \(25\) independently generated exact-rate absorption calculations using rational Gaussian elimination.

An illustrative parameter choice is \(B=40\), \(h=1/20\). Numerical maximization, *after* the symbolic proof, gives \(m_*\approx0.674\), with success probability approximately \(0.6164\), versus approximately \(0.5217\) under full dispersal. These numerical figures are examples, not proof of the universal statement.

## Relationship to prior work

Lanchier's 2013 sexual-reproduction patch model supplies the pair-dependent birth mechanism and the ecological motivation for mate-limited range expansion. Its main results concern survival/extinction on infinite networks, large patch capacity, and dispersal range, rather than finite two-patch first-pair probabilities or a jointly concave rate allocation objective. Foxall and Lanchier's 2015 development emphasizes mean-field expansion/retreat and stochastic large-capacity criteria. The earlier Kang–Lanchier 2010 two-patch Allee work studies a distinct migration/exchange process and asymptotic expansion, not the present finite pair-production chain. These precise differences were checked against accessible article text, but the literature comparison is not a proof of historical priority.

## Limitations

The target is first attainment of a reproductive pair, not permanent establishment or eventual occupation of both patches. The model assumes three slots per patch, homogeneous individual death rate, pair-dependent Poisson birth attempts, no adult movement, no immigration, and independent migrant survival. The sharp number \(9\) is specific to these rates and this capacity and scales with the death-rate normalization; it is not asserted for larger patch capacities, arbitrary networks, or empirical populations. Relevant historical dispersal-optimization results outside the inspected sources could reduce the originality assessment.

## References

1. N. Lanchier, *Survival and extinction results for a patch model with sexual reproduction*, arXiv:1307.6618v1, first publicly available 2013-07-25. https://arxiv.org/abs/1307.6618
2. E. Foxall and N. Lanchier, *Survival and extinction results for a patch model with sexual reproduction*, arXiv:1504.01409v1, first available 2015-04-06. https://arxiv.org/abs/1504.01409
3. Y. Kang and N. Lanchier, *Expansion or extinction: deterministic and stochastic two-patch models with Allee effects*, arXiv:1003.0121v1, first available 2010-02-27. https://arxiv.org/abs/1003.0121
4. U. Motro, *Optimal rates of dispersal II. Diploid populations*, Theoretical Population Biology **21** (1982), 412–429, DOI:10.1016/0040-5809(82)90027-2. Historical optimization context only; full text not assessed.
