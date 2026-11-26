# A six-residue Lucas law for recurrent majority dynamics on circular prisms

## Finding
Let \(G_n=C_n\square K_2\), for any integer \(n\ge3\), and let \(F_n\) be synchronous strict-neighbor-majority on its binary configurations. Write \(L_0=2\), \(L_1=1\) and \(L_{j+2}=L_{j+1}+L_j\) for the Lucas numbers. The exact number \(P_n=|\{x:F_n^2(x)=x\}|\) of configurations on recurrent orbits is
\[
P_n=\begin{cases}
L_{2n}+8L_n+18,&n\equiv0\pmod6,\\
L_{2n}+2L_n+3,&n\equiv2,4\pmod6,\\
L_{2n}+4,&n\equiv3\pmod6,\\
L_{2n}+1,&n\equiv1,5\pmod6.
\end{cases}
\]
The exact number of fixed configurations is
\[
Q_n=|\{x:F_n(x)=x\}|=L_n+2+2\cos(n\pi/3).
\]
Consequently the exact number of distinct primitive two-cycles is \((P_n-Q_n)/2\). In particular, writing \(\varphi=(1+\sqrt5)/2\), the number of distinct primitive two-cycles is asymptotic to \(\varphi^{2n}/2\), while the fixed-point count is asymptotic to \(\varphi^n\). These are different exponential growth rates for two types of recurrent behavior on the same cubic graph family.

## Assumptions and scope
The simple prism graph has vertices \((i,r)\) with \(i\in\mathbb Z/n\mathbb Z\) and \(r\in\{0,1\}\); the three neighbors of \((i,r)\) are \((i-1,r)\), \((i+1,r)\), and \((i,1-r)\). Each site updates simultaneously to the majority of its **three neighbors**, without counting its own state. There are no ties. Configurations are labelled by their actual vertices (not quotienting spatial rotations or layer exchange). A primitive two-cycle is an unordered pair of distinct configurations swapped by \(F_n\).

## Proof
**Period restriction.** On every finite undirected graph, synchronous symmetric threshold dynamics have only fixed points and primitive two-cycles as eventual attractors (Goles--Olivos). Strict majority of three neighbors is in that class. Accordingly every recurrent configuration satisfies \(F_n^2(x)=x\); no assumption about how rapidly it becomes recurrent is needed.

**Fixed configurations.** Encode column \(i\) by its two row-bits. In a fixed configuration, a mixed column \((0,1)\) forces both neighboring columns to be \((0,1)\): the top site, whose rung neighbor is \(1\), requires both ring neighbors to be \(0\), and the bottom site symmetrically requires both to be \(1\). The same holds for \((1,0)\). Thus precisely two fixed configurations contain mixed columns (the two uniform mixed-column patterns). Every other fixed configuration consists only of pure columns \((0,0)\) or \((1,1)\). At a pure column the rung neighbor reinforces its bit, so it changes precisely if both adjacent columns are the opposite pure type. These configurations are cyclic binary words with no isolated bit. Their number is \(\operatorname{tr}(K^n)\), where the states of \(K\) are ordered pairs \((a,b)\in\{0,1\}^2\) and \(K_{(a,b),(b,c)}=1\) exactly when \(\neg(a=c\ne b)\). The polynomial \(\det(tI-K)=(t^2-t-1)(t^2-t+1)\). Summing its eigenvalue powers and adding the two mixed patterns yields the asserted \(Q_n\).

**Two-time transfer.** Let a spatial column label \(s\in\{0,1\}^4\) represent \((x_{i,0},x_{i,1},y_{i,0},y_{i,1})\). For triple \(a,b,c\) of such labels define \(R(a,b,c)=1\) if, for each \(r=0,1\), both equalities hold:
\[
 y_{i,r}=\operatorname{maj}(x_{i-1,r},x_{i+1,r},x_{i,1-r}),\qquad
 x_{i,r}=\operatorname{maj}(y_{i-1,r},y_{i+1,r},y_{i,1-r}).
\]
Here \(\operatorname{maj}\) is the Boolean majority of three arguments, so the three labels supply the neighbor bits as indicated. Form a zero-one \(256\times256\) matrix \(M\) on ordered pairs of labels, with \(M_{(a,b),(b,c)}=R(a,b,c)\), and all other entries zero. Cyclically closed walks of length \(n\) correspond bijectively to spatial sequences of pairs \((x,y)\) with \(F_n(x)=y\) and \(F_n(y)=x\). Every \(x\) with \(F_n^2(x)=x\) determines exactly one \(y\). Therefore \(P_n=\operatorname{tr}(M^n)\) for every \(n\ge3\).

**Finite exact algebra certificate.** The transition predicate has 400 allowed triples. The directed graph of \(M\) has precisely six strongly connected components containing cycles, with sizes \(16,8,8,2,1,1\). The other 222 singleton components contain no loop, so contribute zero to the trace of every positive power. The characteristic polynomial of the 16-vertex block factors as
\[
(t-1)^2(t+1)^2(t^2-3t+1)(t^2+t+1)
(t^4-t^3+2t^2+t+1)(t^4+t^3+2t^2-t+1).
\]
Each 8-vertex block has characteristic polynomial
\[
(t^2-t-1)(t^2-t+1)(t^2+t-1)(t^2+t+1).
\]
The 2-vertex block contributes \((t-1)(t+1)\); both 1-vertex blocks contribute \((t-1)\). All of these statements are finite exact consequences of the given Boolean predicate. The accompanying standalone program builds the 256-state directed graph, finds its strongly connected components, computes the six characteristic polynomials over the integers and asserts these factorizations; the finite computation is not an extrapolation from sampled ring sizes.

**Evaluation of traces.** Write \(\varphi=(1+\sqrt5)/2\). The roots of \(t^2-3t+1\) are \(\varphi^2\) and \(\varphi^{-2}\). The eight roots of the two quartics are \(\pm\varphi e^{\pm i\pi/3}\) and \(\pm\varphi^{-1} e^{\pm2i\pi/3}\); the two 8-vertex blocks have roots \(\pm\varphi\), \(\pm\varphi^{-1}\), and roots from \(t^2-t+1\) and \(t^2+t+1\), with the multiplicities encoded above. Summing the \(n\)-th powers, using \(L_n=\varphi^n+(-\varphi^{-1})^n\), then separating \(n\bmod6\) gives the displayed four-case formula for \(P_n\). In particular the leading term is \(L_{2n}\) and all others are \(O(\varphi^n)\). Subtracting \(Q_n\), dividing by two, and using \(L_j\sim\varphi^j\) proves the asymptotic assertion.

## Verification
Run `python verify_prism_majority.py` using Python 3 and SymPy. This recomputes the 256-state transfer graph from the Boolean rule, its exact SCC decomposition and characteristic-polynomial factorization, and evaluates transfer traces at circumference \(3\le n\le10\). Separately, it exhaustively enumerates all \(2^{2n}\) original configurations at each of these eight circumferences, checking the explicit formulas for fixed points and for \(F_n^2\)-fixed points. The observed \((Q_n,P_n)\) values are \((4,22),(8,64),(14,124),(22,484),(32,844),(48,2304),(76,5782),(124,15376)\). Symbolic factorization, rather than the finite ring enumeration, is the all-size certificate.

## Relationship to prior work
Goles and Olivos (1980) establish the general period-at-most-two theorem for finite symmetric threshold systems, which supplies no prism-specific orbit counts. Kaaser, Mallmann-Trenn and Natale (arXiv:1508.03519v1, 2015) study voting-time upper bounds and algorithmic complexity; their 28-page preprint does not contain a circular-prism recurrent-state enumeration. Nakar and Ron (arXiv:2205.08972) study majority cellular automata with self-inclusive one-dimensional radius neighborhoods on a **single** cyclic row, not the two-row prism with rung interaction. Exact Lucas-number formulas for recurrent states on prisms are not implications of those statements. The new contribution here is the complete two-cycle count, its six-residue Lucas structure, and the exact exponential orbit-growth law.

## Limitations
The claim concerns recurrent-state counts, not basin volumes, maximal transient length, random-initial-condition convergence probabilities, or graph families other than circular prisms. The analytic all-size proof is conditional only on the stated, reproducible finite symbolic graph computation. No independent external verification or literature-exhaustiveness assertion is made. Database and published-literature searches can miss unindexed equivalent formulas.

## References
1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187--189, doi:10.1016/0012-365X(80)90121-1.
2. D. Kaaser, F. Mallmann-Trenn, E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519v1, first posted 2015-08-14, https://arxiv.org/abs/1508.03519.
3. Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, arXiv:2205.08972, https://arxiv.org/abs/2205.08972.
