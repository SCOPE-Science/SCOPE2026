# Complete temporal orbit census for the four-color cyclic cellular automaton on rings

## Finding

For every labelled cyclic ring of \(n\ge3\) sites and every integer \(t\ge1\), the number of configurations fixed after \(t\) simultaneous steps of the four-color cyclic successor-contact rule is

\[
\left|\operatorname{Fix}(F_n^t)\right|=2^{n+1}+8\sum_{k=1}^{g}\binom{g}{k}\mathbf 1_{4\mid ak}\mathbf 1_{4\mid bk},\qquad g=\gcd(n,t),\quad a=n/g,\quad b=t/g.
\]

The exact recurrent sector consists of frozen configurations with spatial differences only zero or two, and two traveling-wave sectors with differences only zero or respectively positive one or negative one, taken modulo four. Consequently the number of states lying on a temporal cycle is

\[
\left|\operatorname{Per}(F_n)\right|=2^{n+2}+4\operatorname{Re}(1+i)^n-8.
\]

The possible least temporal periods are exactly one and the divisors of \(n\) at least four. For any positive divisor \(p\) of \(n\), the number of primitive temporal \(p\)-orbits is

\[
\frac1p\sum_{d\mid p}\mu(p/d)\left|\operatorname{Fix}(F_n^d)\right|,
\]

where \(\mu\) is the number-theoretic Möbius function. The periodic sector has exponential growth rate two (one bit per site), although the full configuration space has size \(4^n\).

## Assumptions and scope

Sites are indexed \(i\in\mathbb Z/n\mathbb Z\), and colors are \(x_i\in\mathbb Z/4\mathbb Z\). All sites update simultaneously by

\[
(F_nx)_i=\begin{cases}x_i+1\pmod4,&x_{i-1}=x_i+1\pmod4\text{ or }x_{i+1}=x_i+1\pmod4,\\x_i,&\text{otherwise.}\end{cases}
\]

There are no self-neighbors. For \(n\ge3\), the two neighbors are distinct. A configuration is *recurrent* if it is periodic from the initial moment: \(F_n^t(x)=x\) for some \(t\ge1\). This is distinct from eventual periodicity after a transient.

Define cyclic interface differences \(d_i=x_{i+1}-x_i\pmod4\). A difference of one is a positive moving interface, three a negative moving interface, two a stationary interface, and zero no interface. The cyclic sum of the differences vanishes modulo four. A choice of differences satisfying that constraint has precisely four realizations, by choosing \(x_0\).

## Proof

**1. Local particle algebra and monotonicity.** Set \(p_i=\mathbf1_{d_i=1}\), \(m_i=\mathbf1_{d_i=3}\), and \(e_i=\mathbf1_{p_i=1\text{ or }m_{i-1}=1}\). Exactly the sites with \(e_i=1\) increment. Hence \(d'_i=d_i+e_{i+1}-e_i\pmod4\). For \(A=p_{i+1}\) and \(B=m_{i-1}\), direct substitution gives the exhaustive four-case table

\[
\begin{array}{c|c}
d_i&d'_i\\\hline
0&A-B\pmod4\\
1&A\\
2&2+A-B\pmod4\\
3&-B\pmod4
\end{array}.
\]

Let \(K(x)\) be the number of nonzero differences. Each new nonzero interface can be charged to one old interface, and no old interface is charged twice: for old difference zero charge to its unique incoming positive or negative interface (two simultaneous incoming interfaces cancel); for old difference one charge to the incoming positive interface; for difference three charge to the incoming negative interface; for difference two charge to the stationary interface when \(A=B\), and otherwise to its unique incoming interface. Any old moving interface can be charged only at its destination (positive: one edge left; negative: one edge right), and each stationary interface only at its original edge. Thus \(K(F_nx)\le K(x)\).

If equality holds, all old interfaces must have charged a new interface. In particular, every positive one advances left as a positive one, every negative one advances right as a negative one, and every stationary two remains stationary: there are no collisions or conversions. This necessary condition is also checked independently in the supplied finite local-interface and exhaustive ring verification.

**2. Classification of recurrent configurations.** If a configuration is periodic then the nonincreasing integer \(K\) is constant all along the orbit. Its interfaces therefore propagate freely with the three respective velocities \(-1,0,+1\) forever. On a finite ring, a moving and a stationary interface must eventually meet, because their relative position shifts by one at each update. Similarly, oppositely moving positive and negative interfaces must eventually meet or cross: their relative displacement shifts by two, and for either parity of ring size it eventually attains a collision or crossing placement. Both contradict the equality condition just proved. Therefore all nonzero interfaces have one common type. If they are stationary twos, no color has a successor neighbor and the state is fixed. If they are all positive ones or all negative ones, the local table shows that the interfaces simply shift left or right, with unchanged types; thus these configurations are periodic. No other recurrent configurations exist.

**3. Exact fixed-iterate counts.** The frozen sector permits differences only zero and two. Its cyclic closure forces an even number of twos, so it has \(4\cdot2^{n-1}=2^{n+1}\) distinct states. For the positive traveling sector, write \(p_i\in\{0,1\}\) for the differences and exclude the all-zero word. Then \(p'_i=p_{i+1}\), and a return after \(t\) updates implies the binary pattern is invariant under rotation by \(t\); it consists of \(a=n/g\) repetitions of a word of length \(g=\gcd(n,t)\), say of weight \(k\ge1\). Spatial color closure holds iff \(4\mid ak\). During \(t\) updates each color increases by exactly \(bk\), where \(b=t/g\); full state return holds iff \(4\mid bk\). Each admissible binary word has four choices of its starting color, hence contributes \(4\binom gk\) configurations. The negative traveling sector contributes identically, giving the claimed \(8\)-factor. The two moving sectors do not overlap when \(k>0\), and neither overlaps the frozen sector.

**4. Total recurrent census, possible periods, and growth.** Every traveling configuration returns by time \(n\) because its number of moving interfaces is divisible by four. Therefore the total recurrent population equals \(|\operatorname{Fix}(F_n^n)|\). The fourth-root-of-unity filter yields

\[
\sum_{\substack{0\le k\le n\\4\mid k}}\binom nk=2^{n-2}+\tfrac12\operatorname{Re}(1+i)^n,
\]

and gives \(2^{n+2}+4\operatorname{Re}(1+i)^n-8\). On a pure traveling sector, a temporal return entails a spatial shift return, so the least temporal period divides \(n\). Every nonconstant traveling sector has at least four interfaces, hence no period two or three. Conversely, for any divisor \(p\ge4\) of \(n\), repeat a primitive length-\(p\) binary word consisting of four consecutive ones and the remaining zeros, producing a closed positive-interface configuration with least period precisely \(p\) (for \(p=4\), the all-one word also has temporal period four because a site advances by one each step). The fixed sector supplies period one. Möbius inversion gives the primitive orbit census. Finally \(|\operatorname{Re}(1+i)^n|\le (\sqrt2)^n\), so periodic states have growth \(4\cdot2^n+O((\sqrt2)^n)\).

## Verification

The standalone `verify.cpp` builds the transition map directly from the four-color local rule and enumerates all \(4^n\) initial states for \(3\le n\le10\). It independently checks the recurrent-sector classification and every claimed fixed-iterate count for \(1\le t\le n\). The separate `check_interfaces.py` exhaustively verifies all \(4^3\) local difference triples and checks interface monotonicity and equality-case propagation for all states with \(3\le n\le8\). The stored exact outputs are `verify_output.txt` and `interfaces_output.txt`. Reproduction: `g++ -std=c++17 -O3 verify.cpp -o verify && ./verify` and `python3 check_interfaces.py`. Finite checks corroborate but do not replace the all-length combinatorial proof.

## Relationship to prior work

Fisch's original 1990 study introduced this very cyclic successor-contact automaton and its interacting-particle interpretation. Hellouin de Menibus and Sablik, Section 5.1, explicitly identify interfaces moving left, right or staying stationary and prove qualitative one-direction survival for shift-ergodic measure limit sets. These qualitative insights are acknowledged prior coverage, not claimed as discoveries here. The new statement is the exact labelled finite-ring fixed-iterate polynomial, arithmetic closure conditions for every \(n,t\), total periodic census and exact least-period spectrum. The freely accessible full text of Fisch, Gravner and Griffeath’s 1991 *Statistics and Computing* paper (also deposited on arXiv in 1993) addresses the broader threshold-range wave patterns, especially in two dimensions, and its sections and bibliography do not state these finite-ring counts. The inspected portions of Belitsky and Ferrari concern infinite-line ballistic annihilation for three colors. A precise comparison with the complete 1990 source remains a priority limitation because its full text was not accessible.

## Limitations

The result concerns only four colors, threshold-one successor contact, synchronous updates and finite undirected rings \(n\ge3\). It does not classify attraction basins, transient lengths, infinite-lattice invariant measures or higher-color automata. The supplied finite enumerations are not independent all-length proofs. Although the exact quantitative enumeration was not found in the examined literature, priority cannot be certified without full access to certain older sources and wider archival indexing; an independent mathematical audit has not been performed.

## References

1. R. Fisch, “The one-dimensional cyclic cellular automaton: A system with deterministic dynamics that emulates an interacting particle system with stochastic dynamics,” *Journal of Theoretical Probability* **3** (1990), 311–338. https://doi.org/10.1007/BF01045164 (full text not retrieved).
2. R. Fisch, J. Gravner, D. Griffeath, “Threshold-Range Scaling of Excitable Cellular Automata,” *Statistics and Computing* **1** (1991), 23–39; public arXiv deposit submitted 1993-04-02. https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf (complete 1991 journal text available and sections, focus, and bibliography inspected). https://arxiv.org/abs/patt-sol/9304001.
3. B. Hellouin de Menibus, M. Sablik, “Self-organization in cellular automata: a particle-based approach,” especially §5.1. https://www.digiscope.fr/~hellouin/Articles/Selforg.pdf (abstract, introduction, particle theorem and §5.1 read).
4. V. Belitsky, P. A. Ferrari, “Ballistic Annihilation and Deterministic Surface Growth,” 1995. https://citeseerx.ist.psu.edu/document?doi=3cbbc5b180ab06b51c7721f2dfe009ecda68310d&repid=rep1&type=pdf (introduction and theorem overview read).
