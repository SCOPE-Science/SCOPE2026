# Exact entrance shells and a discrete extreme-value cutoff for two-jump disjunctive circulants

## Finding

Let \(n\ge3\) and \(2\le s\le n-1\). On binary configurations \(x=(x_i)_{i\in\mathbb Z/n\mathbb Z}\), consider the synchronous disjunctive map
\[
F(x)_i=x_{i-1}\lor x_{i-s}.
\]
Put \(g=\gcd(n,s-1)\) and \(m=n/g\). For a state \(x\), let \(\tau(x)\) be the least nonnegative number of updates after which the state is on a periodic orbit. The following assertions hold for every permitted \(n,s\).

**Complete transient census.** For \(0\le t\le m-1\), construct the \((t+1)\)-state nonnegative integer matrix \(M_t\), indexed by \(0,\ldots,t\), with the only nonzero entries
\[
(M_t)_{j,0}=1\quad(0\le j\le t),\qquad (M_t)_{j,j+1}=1\quad(0\le j<t).
\]
Set \(C_m(t)=1+\operatorname{tr}(M_t^m)\). Then
\[
\#\{x:\tau(x)\le t\}=C_m(t)^g,
\]
so the exact first-periodic-entry populations are
\[
E_0=2^g,\qquad E_t=C_m(t)^g-C_m(t-1)^g\quad(1\le t\le m-1).
\]
The sharp global first-entry bound is \(m-1\). In particular, its last shell has size
\[
E_{m-1}=2^n-(2^m-m)^g.
\]

**Recurrent states and attraction basins.** There are exactly \(2^g\) recurrent states, namely those constant on each of the \(g\) residue classes modulo \(g\). The map rotates their \(g\)-bit class patterns. For a particular recurrent phase containing \(w\) active classes, the cardinality of its full \(F^{m-1}\)-preimage is exactly \((2^m-1)^w\). Hence the complete attraction basin of a primitive orbit of length \(d\), whose patterns all have \(w\) active classes, has size \(d(2^m-1)^w\). The familiar binary-necklace enumeration of these orbit lengths is prior theory, not asserted as new here.

**Discrete extreme-value cutoff.** Fix integers \(g\ge1\) and \(c\), and take \(m=2^h\), \(n=gm\), \(s=g+1\) as \(h\to\infty\). For independent uniformly random input bits and \(t=h+c-1\),
\[
\lim_{h\to\infty}\Pr\{\tau(x)\le h+c-1\}=\exp(-g2^{-c-1}).
\]
Thus the typical transient is logarithmic in the class size \(m\), although the sharp worst-case transient grows linearly in \(m\). The limiting distribution is a discrete extreme-value staircase, with a multiplicative \(g\)-dependence.

## Assumptions and scope

Indices are interpreted cyclically modulo \(n\). Both input arcs are distinct because \(2\le s\le n-1\). The update is simultaneous, not sequential. A state is periodic if \(F^d(x)=x\) for some \(d\ge1\). The quantity \(\tau(x)\) measures first entrance to **any** periodic orbit, not first return to the initial state. The transfer formula is for the finite integer ranges stated; the limiting law fixes \(g,c\) and varies \(h\), not \(n\) at arbitrary steps. All counts use labelled initial configurations.

## Proof

**1. A circular-window identity.** Idempotence and associativity of disjunction and commuting cyclic shifts give, by induction on \(t\),
\[
(F^t x)_i=\bigvee_{j=0}^{t}x_{i-t-j(s-1)}.
\]
The initial positions in a window all belong to a single residue class modulo \(g\). Because \(\gcd(m,(s-1)/g)=1\), increasing \(j\) cycles through every one of the \(m\) vertices in that class, in some order.

**2. Recurrent image.** At \(t=m-1\), each window contains every vertex of its residue class exactly once. Its disjunction is zero precisely when the whole input class is zero. Therefore \(F^{m-1}(x)\) is constant on every residue class. This class-constant set is invariant, and the update restricted to it is \(y_i\mapsto y_{i-1}\), a permutation of its \(g\) class bits. Consequently every state in this set is periodic and every periodic point lies in it (a periodic point whose iterate is in the set must itself lie in the set by rotation around its orbit). There are \(2^g\) such states.

**3. Exact entry shells.** A configuration is periodic by time \(t\) exactly if \(F^t(x)\) is constant on each class. For each input class there are two possibilities. If the entire class is zero, every length-\((t+1)\) OR window is zero and it qualifies. Otherwise at least one window is one, so class constancy requires that **every** circular window of \(t+1\) consecutive sites (in the cyclic order defined by \((s-1)/g\)) contain a one. This is equivalent to saying the binary word of length \(m\) has no cyclic zero-run of length \(t+1\) or greater. Its count, including the separately qualifying all-zero word, is \(C_m(t)\).

To compute the latter count, let state \(j\) record the length of the most recent zero-run (bounded by \(t\)). Reading a one resets the state to zero; reading a zero sends \(j\) to \(j+1\), unless \(j=t\), when that transition is forbidden. This is exactly \(M_t\). For any nonzero circular word avoiding the forbidden run there is one and only one compatible closed state path: the run length preceding each site. A word containing no one has no such closed path. Hence \(C_m(t)=1+\operatorname{tr}(M_t^m)\). Different residue classes provide independent input words, giving \(C_m(t)^g\). Taking differences yields all \(E_t\). At \(t=m-2\), precisely the \(m\) words containing exactly one one are the nonzero failures; hence \(C_m(m-2)=2^m-m\). At \(t=m-1\), all \(2^m\) words qualify. The last-shell formula follows and is strictly positive; one nonempty singleton class is an explicit sharpness witness.

**4. Exact attraction-fiber populations.** The image of \(F^{m-1}\) records, for each source residue class, whether the class contains at least one one. A prescribed zero class has one input pattern; a prescribed one class has \(2^m-1\) patterns. Multiplication over classes gives \((2^m-1)^w\). The states of one primitive necklace orbit have equal \(w\), and the inverse images of its distinct phases are disjoint. Their sum is the asserted full attraction-basin population.

**5. Poisson limit.** Let \(\ell=t+1=h+c\). On a uniformly random length-\(m\) circular word, let \(W\) count occurrences of the block consisting of one followed by \(\ell\) consecutive zeros. A nonzero word avoids zero-runs of length \(\ell\) or more if and only if \(W=0\). The all-zero word also has \(W=0\). Thus the class meets the entry condition if and only if \(W=0\), exactly, not merely asymptotically.

Each specified block occurrence has probability \(2^{-(\ell+1)}\), so \(\mathbb EW=m2^{-(\ell+1)}=2^{-c-1}=: \lambda\). Two distinct starts separated by at most \(\ell\) in cyclic distance cannot both occur, because the required leading one of one block lies within the zeros of the other. For distinct starts whose cyclic gaps exceed \(\ell\), the determining blocks are disjoint and independent. For each fixed positive integer \(k\), all but \(O_k(m^{k-1}\ell)\) ordered \(k\)-tuples of starts have mutually disjoint blocks. It follows that the \(k\)th factorial moment of \(W\) tends to \(\lambda^k\), proving \(W\Rightarrow\operatorname{Poisson}(\lambda)\). Consequently \(\Pr(W=0)\to e^{-\lambda}\). The \(g\) input residue classes are independent, yielding \(e^{-g\lambda}\).

## Verification

`verify_direct.py` independently enumerates every labelled state for each \(n=3,\ldots,12\) and every \(s=2,\ldots,n-1\). It compares the actual first entrance into the class-constant recurrent set with direct circular-word counts, checks the sharp last shell, and (when \(n\le10\)) checks each recurrent phase's basin fiber. `verify_transfer.py` separately evaluates the transfer trace and compares it with direct cyclic-word enumeration for every \(m=2,\ldots,14\) and \(0\le t<m\); it also checks sample arithmetic and numerical convergence toward the Poisson limit. Both scripts executed successfully with standard Python and no third-party dependencies.

For \(n=12,s=4\) (so \(g=3,m=4\)), the first-entry shell counts are \((8,504,1216,2368)\). For \(n=12,s=3\) (so \(g=2,m=6\)), they are \((4,357,1239,1104,660,732)\). The different sharp entrance times despite identical numbers of variables exhibit an arithmetic resonance controlled by \(\gcd(n,s-1)\).

## Relationship to prior work

Jarrah, Laubenbacher, and Veliz-Cuba (first public arXiv version 2008-05-02) developed period and periodic-orbit theory for conjunctive/disjunctive Boolean networks, including necklace structure for strongly connected dependencies. Gao, Chen, and Başar (2016) studied conjunctive-network periodic orbits and stability after single-bit perturbations. Gadouleau (2021) studied image, periodic and fixed points of disjunctive networks. These prior results supply the recurrent-network context but, in the consulted texts, do not state this two-jump graph's exact **all-state entrance-time distribution**, weighted attraction-phase population, or critical discrete cutoff. The finite-state reduction to forbidden circular zero-runs connects the present result with classical longest-run and Poisson rare-block methods; novelty is **not** claimed for those generic methods or the necklace formula alone.

## Limitations

The exact transient census applies to two distinct incoming cyclic shifts and homogeneous synchronous OR; it does not cover arbitrary directed circulants, mixed AND/OR gates, or heterogeneous updates. The probability cutoff assumes independent unbiased input bits, fixed \(g\), and \(m=2^h\). Independent external verification has not been performed. Although pertinent primary literature and indexed related results were compared, unseen equivalents in earlier run-length or Boolean-network literature remain a possible priority risk. Finite computation corroborates, but does not replace, the all-size proof.

## References

- Abdul Salam Jarrah, Reinhard Laubenbacher, Alan Veliz-Cuba, *The Dynamics of Conjunctive and Disjunctive Boolean Networks*, first publicly available 2008-05-02, https://arxiv.org/abs/0805.0275.
- Zuguang Gao, Xudong Chen, Tamer Başar, *Stability Structures of Conjunctive Boolean Networks*, first publicly available 2016-03-14, https://arxiv.org/abs/1603.04415.
- Maximilien Gadouleau, *Dynamical Properties of Disjunctive Boolean Networks*, first publicly available 2021-04-09, https://arxiv.org/abs/2104.04403.
- E. Goles and M. Noual, *Disjunctive networks and update schedules*, Advances in Applied Mathematics (2012), https://doi.org/10.1016/j.aam.2011.11.009 (bibliographic/abstract comparison only; full text not inspected).
