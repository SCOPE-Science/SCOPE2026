# A quarter-probability majority-inversion boundary on complete split networks

## Finding
For integers \(c\ge2\), \(\ell\ge1\) with \(N=c+\ell\) odd, let \(G_{c,\ell}=K_c\vee\overline{K}_{\ell}\) be the complete split graph: \(c\) core vertices form a clique; \(\ell\) peripheral vertices form an independent set; and every core vertex is connected to every peripheral vertex. Initially each labeled vertex votes independently and fairly for one of two alternatives. Every vertex simultaneously casts its *local* vote by strict majority of its **closed neighborhood** (itself and all its neighbors), retaining its own initial vote in a tie. The final network choice is the strict majority of these local votes. Let \(R(c,\ell)\) be the probability that the final choice disagrees with the initial population-wide strict majority.

**Exact formula and structural boundary.** If \(\ell<c\), then \(R(c,\ell)=0\) identically. If \(\ell>c\), write \(t=(N+1)/2\) and \(a=\lfloor(c-2)/2\rfloor\). Then
\[
R(c,\ell)=\frac{2}{2^N}\sum_{x=0}^{a}\binom cx\sum_{y=\max(0,t-x)}^{\ell}\binom\ell y,
\]
where an inner sum with lower limit above \(\ell\) is zero. This formula counts all initial labeled profiles, not just typical ones.

**Asymptotic boundary.** Along integer sequences \(c\to\infty\) and \(\ell>c\) with \(\ell/c\to\rho\in[1,\infty)\),
\[
R(c,\ell)\longrightarrow\frac1\pi\arccos\!\left(\frac1{\sqrt{1+\rho}}\right).
\]
In particular, for every integer \(m\ge2\), compare two networks with the same \(2m+1\) labeled vertices, \(G_{m+1,m}\) and \(G_{m,m+1}\). The first has exactly zero inversions; in the second,
\[
\lim_{m\to\infty}R(m,m+1)=\frac14.
\]
Thus changing one vertex's position from the all-connected core class to the peripheral class (and deleting its edges to the other peripheral vertices) creates an asymptotic inversion probability of one quarter, although both graphs still have a clique joined to an independent set.

## Assumptions and scope
The only randomness is independent initial Bernoulli-\(1/2\) voting at all \(N\) labeled vertices. Only one simultaneous local-majority stage occurs; no further opinion updates take place. Each voter includes itself in its local majority. If an even-sized closed neighborhood splits equally, its owner retains its own initial vote. The population size \(N\) is odd, so both the initial and final global majorities are strict and unambiguous. Here \(K_c\vee\overline K_{\ell}\) is a graph join, not a bipartite graph: all core vertices are mutually adjacent. Results concern only complete split graphs with \(c\ge2\), \(\ell\ge1\) and odd \(N\). The formula for \(\ell>c\) also applies to finite odd \(N\) without asymptotic assumptions. The asymptotic formula requires \(\rho\) finite.

## Proof
Let \(X\) count initial affirmative votes in the core, and \(Y\) count affirmative votes in the periphery. Independently, \(X\sim\mathrm{Bin}(c,1/2)\) and \(Y\sim\mathrm{Bin}(\ell,1/2)\). Write \(M=1\) if \(X+Y\ge(N+1)/2\), and \(M=0\) otherwise. Every core vertex has closed neighborhood equal to all \(N\) vertices, hence **every core local vote equals \(M\)**.

Each peripheral vertex has closed neighborhood consisting of itself and the entire core. There are exactly three regimes. When \(2X>c+1\), every peripheral local vote is affirmative; when \(2X<c-1\), every peripheral local vote is negative; and when \(c-1\le2X\le c+1\), each peripheral local vote equals its own initial vote. To check the boundary, if a peripheral voter initially votes \(0\), its closed neighborhood contains \(X\) affirmative votes; if it initially votes \(1\), it contains \(X+1\). The strict-majority comparison, followed by tie retention, gives the claimed three regimes. In particular, the last interval may contain one or two integer values of \(X\), depending on the parity of \(c\).

In that middle regime, the total number of affirmative local votes is \(cM+Y\), and its global majority also equals \(M\): if \(M=1\), then \(c+Y\ge X+Y\ge(N+1)/2\), whereas if \(M=0\), then \(Y\le X+Y\le(N-1)/2\). Thus the middle regime never reverses the initial global outcome.

If \(\ell<c\), core local votes comprise a strict final majority, and therefore the final decision equals \(M\) for all profiles. If \(\ell>c\), the periphery comprises a strict final majority. In the outer regimes it dictates the outcome: the final vote is \(0\) when \(2X<c-1\) and \(1\) when \(2X>c+1\). Hence inversion occurs precisely when these dictated votes contradict \(M\). By complementation symmetry (interchanging all initial votes), the numbers of the two inversion directions are equal. Counting the event \(2X<c-1\) and \(M=1\), equivalently \(0\le X\le\lfloor(c-2)/2\rfloor\) and \(Y\ge(N+1)/2-X\), produces the double-binomial formula after multiplying by two and dividing by \(2^N\).

For the asymptotic assertion, normalize \(X\) by its mean \(c/2\) and standard deviation \(\sqrt c/2\), and normalize \(X+Y\) by its mean \(N/2\) and standard deviation \(\sqrt N/2\). Their joint distribution tends to a centered bivariate normal with unit marginal variances and correlation \(r=(1+\rho)^{-1/2}\). Indeed, the two independent centered binomial components satisfy the ordinary central limit theorem, and the covariance is exactly \(\operatorname{Cov}(X,X+Y)=c/4\). The middle peripheral regime has probability at most two times the largest point mass of \(\mathrm{Bin}(c,1/2)\), hence tends to zero. Outside that negligible regime, inversion is exactly the event that the centered core count and the centered population count have opposite signs. For centered standard Gaussian variables with correlation \(r\), this sign-disagreement probability is \(\arccos(r)/\pi\): represent the pair as projections of a rotationally invariant planar normal vector onto two unit directions making angle \(\arccos(r)\), and count the two symmetric angular sectors on which the signs differ. The boundary lines have zero Gaussian probability, so weak convergence yields the limit. Taking \(\rho=1\) along \(\ell=c+1\) gives \(\arccos(1/\sqrt2)/\pi=1/4\); taking \(\ell=c-1\) gives the exact zero branch.

## Verification
An independent direct finite checker in `check.py` enumerates every binary initial profile for all \(2\le c\le7\), \(1\le\ell\le9\), odd \(3\le N\le16\). It separately evaluates each vertex's closed-neighborhood vote with explicit tie handling, compares the initial and final strict global majorities, and checks the resulting inversion total against the exact double-binomial formula. It exhaustively checks \(114{,}408\) labeled input profiles across all tested network sizes. Exact rational examples include \(R(2,3)=1/16\), \(R(4,5)=25/256\), \(R(6,7)=121/1024\), and \(R(10,11)=37249/262144\); all \(R(c,c-1)\) cases tested vanish. Reproduce with `python3 check.py` (Python standard library only). The proof above, not the finite enumeration or numerical sequence, establishes all infinite statements.

## Relationship to prior work
Chebotarev and Peleg's *The Power of Small Coalitions under Two-Tier Majority on Regular Graphs* (arXiv:2210.03410, first publicly submitted 2022-10-07) studies the majority-of-majorities/faithfulness question, but its main classification quantifies over regular looped graphs of fixed order and degree. Its discussion (section 7.1, figure 8) explicitly reports a two-vertex coalition controlling local majorities on a complete bipartite graph; minority control and local-to-global disagreement are **not** claimed new here. Those conclusions do not provide the inversion probability on complete split graphs nor the same-order core-classification boundary proved here. In particular, \(G_{c,\ell}\) is irregular when \(\ell\ne1\).

Kaniovski and Zaigraev's *Asymptotic Probability of Majority Inversion under a General Binomial Voting Model* (Operations Research Letters 2022; openly available author manuscript dated 2021-09-17) addresses inversion probabilities for voters **partitioned into nonoverlapping constituencies** with separate first-tier majority outcomes. Here the voting neighborhoods overlap extensively: each core vertex sees the complete initial electorate, while each peripheral voter sees every core member and itself. The paper's theorem for disjoint constituencies is not a result for this neighborhood map. The preceding Kaniovski--Zaigraev 2018 study likewise treats disjoint states and different probability laws.

Cruciani, Natale, Nusser and Scornavacca's *Phase transition of the 2-Choices dynamics on core-periphery networks* (2021) studies stochastic, iterated sampling of two neighbors and consensus/metastability; it does not apply to a single deterministic simultaneous majority-of-closed-neighborhood stage. The existence of powerful elites is also discussed in Avin, Lotker, Mizrachi and Peleg's 2019 study, but that empirical issue does not determine the finite inversion polynomial here.

## Limitations
The inversion probability is computed under independent fair initial votes, not correlated preferences, heterogeneous group reliabilities, or strategic campaigning. The zero-versus-one-quarter boundary compares two specified graph families and is not asserted for every possible core-periphery graph. The theorem does not address iterated dynamics or other local tie rules. A separate independent mathematical audit has not been performed. Possible equivalent results in older graph-voting literature, especially informal accounts of majority monopolies and overlap-voting, remain a bibliographic risk despite the targeted comparison above.

## References
1. P. Chebotarev and D. Peleg, *The Power of Small Coalitions under Two-Tier Majority on Regular Graphs*, arXiv:2210.03410 (initial submission 2022-10-07), https://arxiv.org/abs/2210.03410 .
2. S. Kaniovski and A. Zaigraev, *Asymptotic probability of majority inversion under a general binomial voting model*, Operations Research Letters 50 (2022), 391–398, doi:10.1016/j.orl.2022.05.003; author manuscript https://serguei.kaniovski.wifo.ac.at/fileadmin/pdf/maj_inv_asymptotic.pdf .
3. S. Kaniovski and A. Zaigraev, *The probability of majority inversion in a two-stage voting system with three states*, Theory and Decision 84 (2018), 525–546, doi:10.1007/s11238-018-9660-1; open preprint https://serguei.kaniovski.wifo.ac.at/fileadmin/pdf/maj_inv.pdf .
4. E. Cruciani, E. Natale, A. Nusser and G. Scornavacca, *Phase transition of the 2-Choices dynamics on core-periphery networks*, Distributed Computing 34 (2021), 207–225, doi:10.1007/s00446-021-00396-5 .
5. C. Avin, Z. Lotker, A. Mizrachi and D. Peleg, *Majority vote and monopolies in social networks*, ICDCN (2019), 342–351, doi:10.1145/3288599.3288633 .
