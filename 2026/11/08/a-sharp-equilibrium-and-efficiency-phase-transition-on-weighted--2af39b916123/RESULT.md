# A sharp equilibrium and efficiency phase transition on weighted wheel networks

## Finding

**Theorem (weighted-wheel anti-coordination phase diagram).** Let \(n\ge4\) and \(\lambda>0\). Let \(G_n\) be the labeled graph consisting of a rim cycle \(C_n\) and one hub adjacent to all \(n\) rim vertices. Every rim edge has weight \(1\), and every spoke has weight \(\lambda\). Each vertex is a player choosing one of two labeled actions \(0,1\), and receives the total weight of incident edges whose other endpoint chooses the opposite action. A profile is a pure Nash equilibrium if no single player can strictly increase its payoff by switching actions (payoff ties are stable).

Write \(P_0=3,P_1=0,P_2=2\) and \(P_n=P_{n-2}+P_{n-3}\) for \(n\ge3\) (Perrin numbers), and \(L_0=2,L_1=1,L_n=L_{n-1}+L_{n-2}\) for \(n\ge2\) (Lucas numbers). Counting labeled action profiles, including both global action complements, the number of pure Nash equilibria is exactly

\[
N_n(\lambda)=\begin{cases}
2P_n,&0<\lambda<2,\\
2L_n,&\lambda=2,\\
2,&\lambda>2.
\end{cases}
\]

More precisely, fix the hub to action \(0\) and let \(Z\subseteq V(C_n)\) be the set of rim vertices also using action \(0\). In the three respective regimes, equilibrium profiles correspond bijectively to (i) **maximal independent sets** \(Z\) of \(C_n\), (ii) **arbitrary independent sets** \(Z\) of \(C_n\), and (iii) the **empty set** \(Z=\varnothing\). Hub action \(1\) gives the complementary profiles.

For \(0<\lambda<2\), every equilibrium has \(z=|Z|\) in the exact range \(\lceil n/3\rceil\le z\le\lfloor n/2\rfloor\). Its weighted cut is \(\lambda(n-z)+2z\), and the number of equilibria with exactly \(z\) rim vertices agreeing with the hub, including both choices of the hub action, is

\[
2\frac{n}{z}\binom{z}{n-2z},
\]

using the convention that out-of-range binomial coefficients vanish. The exact **price of anarchy** (optimal welfare divided by minimum equilibrium welfare) is

\[
\operatorname{PoA}_n(\lambda)=\begin{cases}
\displaystyle\frac{\lambda\lceil n/2\rceil+2\lfloor n/2\rfloor}
{\lambda(n-\lceil n/3\rceil)+2\lceil n/3\rceil},&0<\lambda<2,\\
1,&\lambda\ge2.
\end{cases}
\]

The price of stability equals \(1\) for every \(\lambda>0\), and \(\operatorname{PoA}_n(\lambda)\le3/2\) uniformly. The latter is sharp as a supremum over \(n,\lambda\): along rim sizes divisible by \(6\), the ratio approaches \(3/2\) as \(\lambda\downarrow0\).

At \(\lambda=2\), all equilibria maximize welfare, yet the equilibrium count jumps from \(2P_n\) immediately below the threshold to \(2L_n\) at the threshold and collapses to \(2\) immediately above it. If \(\alpha\) is the unique positive root of \(x^3-x-1=0\) and \(\varphi=(1+\sqrt5)/2\), then \(P_n\sim\alpha^n\) and \(L_n\sim\varphi^n\), so \(N_n(2)/N_n(\lambda)\sim(\varphi/\alpha)^n\) for any \(0<\lambda<2\), while \(N_n(\lambda)/N_n(2)\sim\varphi^{-n}\) for any \(\lambda>2\).

## Assumptions and scope

The hub and all rim vertices are distinct and labeled. There are exactly two globally available actions, with each player's payoff equal to the *sum* of weights of incident discordant edges. All spoke weights are a common strictly positive \(\lambda\); rim weights are fixed to \(1\). For welfare, both endpoints receive the weight of a discordant edge, so total welfare equals twice weighted cut value. Weak best responses count as Nash equilibria; if ties were excluded, the boundary count at \(\lambda=2\) would change. The statements are for every integer \(n\ge4\), not merely tested small wheels.

## Proof

**Step 1: exact local best responses.** Fix the hub action to \(0\), without loss of generality by global complementation. Let \(d_i\in\{0,1,2\}\) denote the number of rim neighbors playing opposite to vertex \(i\). If its action equals the hub's action, its current payoff is \(d_i\) while a deviation gives \(2-d_i+\lambda\). Therefore it is stable precisely when \(2d_i\ge2+\lambda\). If its action opposes the hub's, its current payoff is \(d_i+\lambda\) while deviation gives \(2-d_i\), hence stability is equivalent to \(2d_i\ge2-\lambda\). Finally, the hub currently receives \(\lambda(n-z)\) and would receive \(\lambda z\) by changing action, so hub stability is \(z\le n/2\).

**Step 2: all three regimes.** For \(0<\lambda<2\), a rim vertex in \(Z\) needs \(d_i=2\), so no two vertices of \(Z\) can be adjacent. A rim vertex outside \(Z\) needs \(d_i\ge1\), so it must have a neighbor inside \(Z\). Thus \(Z\) is an independent and dominating set, equivalently a maximal independent set. Such a set automatically has \(z\le n/2\) because the rim is a cycle, so the hub condition adds no constraint. Conversely, these conditions imply every player's inequalities. For \(\lambda=2\), vertices in \(Z\) still need \(d_i=2\), while the condition for a vertex outside \(Z\) becomes vacuous; hence \(Z\) is any independent set. Again \(z\le n/2\). For \(\lambda>2\), no rim vertex can agree with the hub because its necessary inequality \(2d_i\ge2+\lambda>4\) is impossible. All rim vertices must therefore oppose the hub, which is a valid equilibrium. Each \(Z\) has precisely one profile with hub \(0\), and action complementation doubles every count.

**Step 3: enumeration, with the known combinatorial counts explicitly credited.** The number of independent sets of an \(n\)-cycle equals \(L_n\): split on an arbitrary vertex or use the trace of the matrix \(\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)^n\); this trace satisfies the Lucas recurrence and equals \(2,1\) at lengths \(0,1\) in its algebraic continuation. Maximal independent sets correspond to cyclic binary strings with no adjacent chosen vertices and no run of three unchosen vertices. If such a set contains \(z\) chosen vertices, the cyclic gaps between successive chosen vertices have lengths either \(2\) or \(3\). Their sum is \(n\), hence exactly \(n-2z\) of the \(z\) gaps have length \(3\); this forces \(\lceil n/3\rceil\le z\le\lfloor n/2\rfloor\). With a distinguished chosen vertex, there are \(n\binom{z}{n-2z}\) possible labeled starting points and gap-type strings, and each undistinguished set has \(z\) such choices. Therefore the count is \((n/z)\binom{z}{n-2z}\). Summing gives the known Perrin value \(P_n\), equivalently obtainable by the standard recurrence for cyclic independent dominating sets; this underlying Perrin enumeration was established previously and is **not** claimed as new combinatorics. This proves both the total and refined counts.

**Step 4: welfare and inefficiency.** For a maximal independent set \(Z\), every chosen vertex has two nonchosen rim neighbors. Consequently exactly \(2z\) rim edges cross the action cut, while precisely \(n-z\) spokes cross, giving cut value \(\lambda(n-z)+2z\). Since \(2-\lambda>0\), the smallest equilibrium cut uses \(z=\lceil n/3\rceil\), and the largest uses \(z=\lfloor n/2\rfloor\); both are realizable by gap compositions of lengths \(2,3\). For an arbitrary action profile with \(k\) rim vertices opposite the hub, at most \(2\min\{k,n-k\}\) rim edges cross. If \(0<\lambda<2\), the upper bound \(\lambda k+2\min\{k,n-k\}\) increases as \(k\) approaches \(\lceil n/2\rceil\) from below and decreases thereafter; at \(k=\lceil n/2\rceil\), an alternating rim with at most one equal-adjacent pair attains it. The optimum cut is therefore \(\lambda\lceil n/2\rceil+2\lfloor n/2\rfloor\). A maximizing equilibrium exists because its \(Z\) is a maximal independent set with \(z=\lfloor n/2\rfloor\). For \(\lambda\ge2\), \(\lambda k+2\min\{k,n-k\}\le\lambda n\), with equality attained by putting all rim vertices opposite the hub; every equilibrium has cut \(\lambda n\) if \(\lambda>2\), and \(2n\) if \(\lambda=2\). Thus PoS equals \(1\), and the PoA formula follows since welfare has the same factor of two in numerator and denominator. For \(0<\lambda<2\), the displayed ratio decreases (weakly) with \(\lambda\), so it is at most \(\lfloor n/2\rfloor/\lceil n/3\rceil\le3/2\). If \(6\mid n\), the latter limit is exactly \(3/2\).

**Step 5: entropy discontinuity.** Perrin's characteristic polynomial is \(x^3-x-1\), with a unique positive dominant root \(\alpha\) and two conjugate roots of modulus strictly less than \(1\). Lucas numbers have dominant root \(\varphi\), with smaller conjugate root \(-\varphi^{-1}\). Their Binet formulas give \(P_n\sim\alpha^n\) and \(L_n\sim\varphi^n\), yielding the displayed exponential jump ratios. This also shows the jump is not an artifact of fixed small wheel sizes.

## Verification

Run `python verify.py` using Python 3's standard library. It tests \(54\) pairs consisting of rim lengths \(4\) through \(12\) and spoke weights \(1/7,1,3/2,2,5/2,4\). For every one of the \(98{,}112\) enumerated labeled profiles, it checks the unilateral best-response inequalities against the structural classification; for each pair it compares equilibrium cardinality, minimum equilibrium cut, maximum cut over all profiles, and existence of an optimal equilibrium against the exact formulas. It additionally checks the size-refined Perrin sum through \(n=100\). The verifier uses `fractions.Fraction` for exact arithmetic. These finite checks do **not** establish the theorem for arbitrary \(n\), which follows from the proof above.

For example, when \(n=12\), the equilibrium counts below, at, and above \(\lambda=2\) are respectively \(58\), \(644\), and \(2\). The largest possible PoA over positive \(\lambda\) approaches \(3/2\) as \(\lambda\downarrow0\); at \(\lambda=1\), it is \(9/8\).

## Relationship to prior work

Deligkas, Eiben, Gutin, Neary and Yeo introduce and study the computational complexity of binary-action anti-coordination polymatrix games, welfare maximization, and potential maximization. Their general complexity results do not state the wheel-specific three-regime equilibrium characterization, equality threshold, exact efficiency ratio, or exponential count discontinuity. The game belongs to their model, but the present claim is a specialization with a separate exact structural theorem rather than a complexity improvement.

The enumerative input is **known**: Bisdorff and Marichal (2008), building on Füredi's earlier observation, explicitly count maximal independent sets of \(C_n\) by Perrin numbers. The Lucas count for all cycle independent sets is classical. The contribution here is the payoff-to-independent-set correspondence with its sharp spoke-weight regimes, the full equilibrium welfare spectrum and PoA/PoS, and the ensuing exponential threshold phenomenon. General local-cut and Ising metastability methods apply in principle but do not automatically provide these exact wheel-specific thresholds and welfare statements. No claim of unique or independent priority is made.

## Limitations

Only a homogeneous spoke weight, homogeneous rim weight (normalized to one), binary actions, and unilateral Nash deviations are considered. Unequal spokes, action-specific bonuses, stochastic learning, and strong/coordinated deviations are outside scope. Counts distinguish labeled profiles and count global action complements separately. The equality phase is sensitive to the convention that payoff indifference is allowed in Nash equilibrium. A bibliographic risk remains that an unindexed equivalent weighted-wheel analysis exists; the already-known Perrin counting fact is not original to this result. No independent external audit has been performed.

## References

1. A. Deligkas, E. Eiben, G. Gutin, P. R. Neary and A. Yeo, *Complexity of Efficient Outcomes in Binary-Action Polymatrix Games with Implications for Coordination Problems*, arXiv:2305.07124v1, first public May 11, 2023, https://arxiv.org/html/2305.07124v1 .
2. A. Deligkas, E. Eiben, G. Gutin, P. R. Neary and A. Yeo, *Some coordination problems are harder than others*, arXiv:2311.03195, first public November 6, 2023, https://arxiv.org/html/2311.03195v2 .
3. R. Bisdorff and J.-L. Marichal, *Counting Non-Isomorphic Maximal Independent Sets of the n-Cycle Graph*, Journal of Integer Sequences 11 (2008), Article 08.5.7, https://cs.uwaterloo.ca/journals/JIS/VOL11/Marichal/marichal.pdf .
4. B. Waclaw and Z. Burda, *Counting metastable states of Ising spin glasses on arbitrary graphs*, Physical Review E 77 (2008), 041114, https://doi.org/10.1103/PhysRevE.77.041114 .
