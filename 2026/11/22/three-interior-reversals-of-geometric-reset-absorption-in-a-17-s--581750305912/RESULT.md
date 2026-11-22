# Three interior reversals of geometric-reset absorption in a 17-state birth–death chain

## Finding
There exists an absorbing, no-holding, nearest-neighbor birth–death chain on exactly 17 states whose probability of absorption at the left endpoint under independent geometric resetting to a single interior site has **at least three distinct strict local extrema** as the reset-survival parameter ranges over \(0<s<1\). An explicit chain is given below; its derivative reverses sign in three disjoint intervals. Thus a two-turn classification is insufficient for general inhomogeneous birth–death chains.

## Assumptions and scope
Let the state space be \(\{0,1,\ldots,16\}\), with absorbing states \(0,16\). Start at \(z=7\). At each interior site \(i\), move right with probability \(p_i\) and left with \(q_i=1-p_i\), without holding. The 15 exact rational rightward probabilities, in increasing site order, are

\[
(p_1,\ldots,p_{15})=10^{-6}(995517, 148739, 992235, 3511, 967337, 5952, 998114, 839557, 998092, 971199, 963413, 13393, 997802, 40422, 23406).
\]

All entries lie strictly between zero and one. For each \(s\in(0,1)\), independently continue the original walk after each nonabsorbing step with probability \(s\) and otherwise reset to site \(7\), beginning a fresh independent cycle. If a boundary is reached, absorption takes precedence over resetting. Denote the eventual probability of absorption at \(0\) by \(Q(s)\). This statement concerns one fixed chain, not an all-parameter classification, not a minimal-state bound, and not an exact count of extrema.

## Proof
For an unreset walk, let \(A(s)=\mathbb E_7[s^T\mathbf1_{\{J=0\}}]\) and \(B(s)=\mathbb E_7[s^T\mathbf1_{\{J=16\}}]\), with \(T\) the first absorption time and \(J\) the absorbing state. The renewal identity gives \(Q(s)=A(s)/(A(s)+B(s))\); multiplying all cycle weights by \(s\) does not affect the quotient.

Let \(P_I\) be the tridiagonal substochastic transition matrix of the original walk killed upon leaving a consecutive set of sites \(I\). Define \(t=s^2\),
\[
L(t)=\det(I-sP_{\{1,\ldots,6\}}),\qquad R(t)=\det(I-sP_{\{8,\ldots,15\}}).
\]
These are polynomials in \(t\) because the underlying graph is bipartite. Tridiagonal cofactor expansion of the discounted hitting equations yields
\[
\frac{B(s)}{A(s)}=C\,s^2\frac{L(s^2)}{R(s^2)},\quad
C=\frac{\prod_{i=7}^{15}p_i}{\prod_{i=1}^7q_i}>0,
\quad Q(s)=\frac{R(t)}{R(t)+CtL(t)}.
\]
The exponent \(2\) is \(16-2(7)\). For all \(0\le s\le1\), both determinants are positive: each killed finite subchain has spectral radius less than one (it can escape with positive probability from every site). Consequently the denominator is positive.

The exact polynomials can be formed without determinants by the following continuant recurrence. For each consecutive interval \([u,v]\), set \(D_0(t)=D_1(t)=1\) and, for \(j=u+1,\ldots,v\), iterate
\[
D_{j-u+1}(t)=D_{j-u}(t)-t\,p_{j-1}q_jD_{j-u-1}(t).
\]
Then \(L=D_6\) for \([1,6]\) and \(R=D_8\) for \([8,15]\). Put
\[
W(t)=[L(t)+tL'(t)]R(t)-tL(t)R'(t).
\]
Differentiating the quotient gives the exact identity
\[
Q'(s)=-\frac{2sCW(s^2)}{[R(s^2)+Cs^2L(s^2)]^2}.
\]
All following signs are **exact rational statements**, verified by the standalone integer/fraction certificate (not by floating-point rounding):
\[
W(3/5)>0,\qquad W(3/4)<0,\qquad W(19/20)>0,\qquad W(1)<0.
\]
Continuity gives at least one sign-changing zero in each of \((3/5,3/4)\), \((3/4,19/20)\) and \((19/20,1)\). The rational derivative is analytic, so in each interval it has a zero at which its sign genuinely switches, hence \(Q\) has a **strict local extremum** at each corresponding \(s=\sqrt t\in(0,1)\). The three intervals are disjoint, so all three extrema are distinct. In increasing \(s\), their observed alternating types may be chosen minimum, maximum, minimum, respectively. This proves the claim.

## Verification
Run `python check.py` with Python 3. The certificate uses `fractions.Fraction`, verifies the four strict signs exactly, checks positivity of \(L,R\) at the sign points, and independently solves the 15-dimensional discounted hitting equations by exact Gaussian elimination at two rational survival parameters to confirm the cofactor quotient. It does not rely on simulation or approximate root locations. The analytic argument from rational sign changes to existence is by continuity and analyticity; the checker does not claim to count every root.

For orientation only, decimal evaluations of \(W\) at \(t=3/5,3/4,19/20,1\) are approximately \(0.00120733,-0.000700254,0.00000378186,-0.0000000139736\); these are **not** the proof certificate.

## Relationship to prior work
Newton and Vega Coso (2026), section 10.3, explicitly ask for classification of one or several interior extrema under reset-intensity changes. Their time-indexed switching example and its spectral sign-change bound concern the *exact-time* exit pair and do not imply three stationary points of the geometric-reset splitting curve. Previously available explicit examples establish two extrema and a sharp minimality result for two extrema on a smaller chain; a new three-extremum witness is not obtained from either by a limiting or relabeling argument. The renewal identity itself is established earlier and is not claimed to be new. The novelty claimed here is specifically the exact three-extremum finite-chain witness.

## Limitations
The result proves at least three strict extrema for one highly inhomogeneous rational chain, not exactly three, not robustness at a uniform quantitative margin, not minimal possible size for three extrema, nor classification of all environments. Near \(t=1\) the final certified derivative sign is small, making exact arithmetic essential. No independent review has been performed. Historical priority in broader restart-control and finite Markov-chain literature is not exhaustively settled.

## References
1. Newton and Vega Coso, *Stochastic Orders of the Exit Pair and the Monotone Response to Resetting*, arXiv:2611.01756v1 (first public 2026-11-01), sections 2, 7 and 10.3, https://arxiv.org/html/2611.01756v1.
2. Vega Coso, *Critical Spectral Invariants in Random Walks with Geometric Resetting*, arXiv:2603.24803, first public 2026-03-25, https://arxiv.org/abs/2603.24803. This concerns related homogeneous gambler's-ruin resetting, not the present heterogeneous witness.
3. Vega Coso, *Spectral Duality and Reset-Neutral Distributions in Random Walks with Multi-Site Geometric Resetting*, arXiv:2605.00657, first public 2026-05-01, https://arxiv.org/abs/2605.00657. The emphasis is reset-neutral distributions, not multiple interior extrema for this one-site chain.
