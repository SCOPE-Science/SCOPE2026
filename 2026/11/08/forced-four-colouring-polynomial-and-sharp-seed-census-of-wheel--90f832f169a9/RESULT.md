# Forced four-colouring polynomial and sharp seed census of wheel graphs

## Finding
For every integer \(n\ge4\), let \(W_{n+1}=K_1\vee C_n\) be the labelled wheel with hub \(h\) and cyclic rim \(v_0,\ldots,v_{n-1}\). Fix four named colours, and use the local rule that a blank vertex is assigned its remaining colour when three distinct colours already occur on its neighbours. Let \(r=1-4p\), where each named colour is independently assigned to a vertex with probability \(p\), and leaving it blank has probability \(r\), with \(0\le p\le1/4\).

Define a twelve-state transfer matrix. Its states are \(\mathcal S=\{(a,b,e):a,b\in\{1,2,3\},\ a\ne b,\ e\in\{0,1\}\}\). For any \(S\subseteq\{1,2,3\}\), let \(T_S(u)\) have only the following nonzero entries, with \(b\ne c\):
\[
[T_S(u)]_{(a,b,e),(b,c,f)}=
\begin{cases}
1,&e=1\text{ and }b\in S,\\
u,&e=0,\ a\ne c,\ f=1,\\
0,&\text{otherwise.}
\end{cases}
\]
Here \(e=1\) means the current rim vertex is initially coloured and \(e=0\) means blank. Put
\[
F_n(u)=\operatorname{tr}(T_{\{1,2,3\}}(u)^n),\quad
G_n(u)=\sum_{S\subseteq\{1,2,3\}}(-1)^{3-|S|}\operatorname{tr}(T_S(u)^n),
\]
and write \(f_{n,j}=[u^j]F_n(u)\), \(g_{n,j}=[u^j]G_n(u)\). Then the entire forced four-colouring probability polynomial is
\[
\boxed{\operatorname{FC}(W_{n+1};p,4)=4\sum_{j=0}^{\lfloor n/2\rfloor}\left(f_{n,j}p^{n+1-j}r^j+g_{n,j}p^{n-j}r^{j+1}\right).}
\]
The formula is a fixed twelve-state transfer valid uniformly for all \(n\ge4\); it counts initial partial assignments, not full colourings with multiplicity.

Let \(\sigma_n\) be the least possible number of initially coloured vertices in a partial four-colouring that forces a proper total colouring, and let \(M_n\) be the number of such minimum-domain partial assignments, with the vertices and four colours named. For every \(n\ge5\),
\[
\boxed{\sigma_n=\left\lceil n/2\right\rceil.}
\]
Define, for every integer \(t\ge3\),
\[
Q_t=2^t+2(-1)^t-6\mathbf1_{2\mid t}.
\]
Then the exact multiplicities are
\[
\boxed{
M_n=\begin{cases}
4nQ_{(n+1)/2},&n\ge5\text{ odd},\\
8Q_{n/2},&n\ge6\text{ even},\\
144,&n=4.
\end{cases}}
\]
The small exceptional rim \(n=4\) has \(\sigma_4=3\). Thus the entire minimum-domain census is exact; in particular \(M_5=120\), \(M_6=48\), \(M_7=336\), and \(M_8=96\).

## Assumptions and scope
All graphs are finite, simple, and labelled. The wheel has one universal hub and a cycle of \(n\ge4\) rim vertices. A partial assignment is successful only when iterating the three-distinct-neighbour-colour rule produces a proper total four-colouring. A partial assignment already containing a monochromatic edge cannot succeed. The independent random initial assignments attach probability \(p\) to each individual named colour and probability \(r=1-4p\) to blank. No other forcing rule is used. Since the hub must have a colour distinct from the rim, every proper total four-colouring assigns one named colour to the hub and uses only the other three on the rim.

## Proof
**Exact forcing criterion.** Fix an arbitrary proper total four-colouring, whose hub colour is designated \(4\) and whose proper rim colouring is \(c_i\in\{1,2,3\}\). Let \(U\subseteq\mathbb Z/n\mathbb Z\) be the indices of initially blank rim vertices. If the hub is initially coloured, a rim blank has at most three neighbours, so it can be forced only when both adjacent rim vertices have already been coloured and carry distinct colours. Thus it is necessary that no two members of \(U\) be consecutive and that \(c_{i-1}\ne c_{i+1}\) for every \(i\in U\). It is sufficient: with no consecutive blanks, all such rim vertices can be forced at once. Conversely, a consecutive pair of blanks can never be the first vertex forced within its blank run, and a blank with equal-coloured rim neighbours can never be forced, so these conditions are also necessary.

If the hub is initially blank, no blank rim vertex can be forced before the hub, since it then sees colours on at most its two rim neighbours, fewer than the required three. The hub can be forced at the first step precisely when its initially coloured rim neighbours display all three rim colours. After that step the previous characterization applies. Hence the hub-blank cases satisfy the same independent-good-blank condition and the additional test that all three rim colours occur among the initially coloured rim vertices.

A successful initial partial assignment has a uniquely forced full colouring: every forcing step has precisely one permitted colour. Consequently the sum over the proper total colourings cannot overcount successful partial assignments.

**Transfer construction.** Write a state \((a,b,e)\) for the preceding rim colour, current rim colour, and seeded status of the current rim vertex. The entry to \((b,c,f)\) enforces the proper-colouring condition \(b\ne c\). When \(e=1\) the current vertex contributes weight one and, in \(T_S\), requires \(b\in S\); when \(e=0\) it contributes weight \(u\), requires \(a\ne c\), and forces its next neighbour to be seeded (\(f=1\)). The preceding transition has already checked that its previous neighbour is seeded. Therefore each closed walk of length \(n\) corresponds uniquely to a proper three-coloured cyclic rim word and an independent set of good blank positions. The number of blanks is tracked by \(u\). This proves the interpretation of \(F_n\). By inclusion–exclusion over three named rim colours, \(G_n\) counts exactly those words for which all three colours occur among the seeded rim vertices. With the four choices of hub colour, the hub-seeded and hub-blank events have weights \(p^{n+1-j}r^j\) and \(p^{n-j}r^{j+1}\), respectively, which proves the polynomial formula.

**Minimum domain and multiplicity.** Every successful blank rim set is independent in \(C_n\), so \(|U|\le\lfloor n/2\rfloor\). With the hub initially blank, attaining this bound leaves exactly \(\lceil n/2\rceil\) initially coloured vertices. For \(n\ge5\) this bound is attainable by selecting an independent blank rim set of maximum size and assigning three distinct rim colours among the remaining vertices so that consecutively retained rim vertices in cyclic order receive different colours. For odd \(n=2m+1\ge5\), there are \(n\) maximum independent blank sets and the \(m+1\) retained vertices form a cyclic constraint graph \(C_{m+1}\). For even \(n=2m\ge6\), there are exactly two alternating maximum independent blank sets and the \(m\) retained vertices form \(C_m\). Every proper colouring of the respective cyclic constraint graph using all three named rim colours makes each blank vertex forceable after the hub and forces the hub first. The number of surjective proper three-colourings of \(C_t\) is \(Q_t\): the standard chromatic polynomial gives \(2^t+2(-1)^t\), and for even \(t\) exactly six of these use only two colours. Multiplying by the four choices of hub colour and by the number of maximum independent blank sets yields the stated multiplicities.

When \(n=4\), two seeded rim vertices cannot display three colours; hence the hub-blank mechanism requires three rim seeds. There are four choices of the blank rim vertex and \(3!=6\) proper assignments of three distinct rim colours on the remaining path, giving \(4\cdot4\cdot6=96\) minimum assignments after choosing the hub's eventual named colour. With the hub initially seeded, precisely two opposite rim seeds suffice; two parity choices and six distinct rim-colour assignments yield \(4\cdot2\cdot6=48\) more. Thus \(\sigma_4=3\) and \(M_4=144\). This completes the proof.

## Verification
The accompanying standalone `verify.py` independently implements the original local rule on the actual wheel adjacency lists. It enumerates every partial assignment from five choices (blank or one of four colours) at each vertex for rim orders \(4\) through \(7\), compares the resulting cardinality distributions with a direct proper-rim-colouring and allowed-blank enumeration, and separately multiplies the twelve-state transfer matrices over integer-polynomial coefficients. It checks equality against direct structural enumeration through rim order \(10\), and the minimum-domain formulas through rim order \(12\). A successful run prints `VERIFY_OK`. The unrestricted result follows from the preceding proof, not finite enumeration.

For rim orders \(4,5,6,7,8\), the distributions by number of initially coloured vertices are, respectively,
\[
\begin{array}{ll}
4:&(3:144,\ 4:144,\ 5:72),\\
5:&(3:120,\ 4:360,\ 5:480,\ 6:120),\\
6:&(3:48,\ 4:480,\ 5:1368,\ 6:960,\ 7:264),\\
7:&(4:336,\ 5:2184,\ 6:3360,\ 7:2352,\ 8:504),\\
8:&(4:96,\ 5:2064,\ 6:6720,\ 7:9312,\ 8:5040,\ 9:1032).
\end{array}
\]
The numbers at the maximum cardinality equal four times the ordinary number of proper three-colourings of the rim, as expected.

## Relationship to prior work
The initiating study by G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1 (15 September 2026), defines precisely the same local forcing probability function and proves general properties, algebraic observations, and hardness; its introductory material discusses explicit small-graph cases. The present result specializes to the fundamental wheel family but obtains an all-order matrix and a sharp, counted minimum seeded domain. A general definition or arbitrary subset-sum representation of the forcing function does not imply this twelve-state reduction or its closed extremal formulas without the structural argument above. The classical cycle chromatic polynomial supplies the factor \(Q_t\) but does not impose the partial-colouring forcing condition. Prior searches have not identified the resulting full wheel formula; historical priority remains provisional because not all parts of the initiating full text could be accessed during the final literature comparison.

## Limitations
The result uses four available named colours and the exact three-distinct-colours local forcing rule; it does not treat other palette sizes, graph families or asynchronous noisy forcing. The transfer formula is a fixed-size exact matrix power rather than a single elementary binomial formula for every coefficient. The enumerator counts labelled partial assignments, not wheel-automorphism classes. Absence of a matched formula in targeted searches is not proof of global novelty.

## References
1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1 (publicly submitted 2026-09-15), https://arxiv.org/abs/2609.17108.
2. Classical cycle chromatic polynomial identity: \(P(C_t;3)=2^t+2(-1)^t\) for integer \(t\ge3\), used only for the optimizer count.
