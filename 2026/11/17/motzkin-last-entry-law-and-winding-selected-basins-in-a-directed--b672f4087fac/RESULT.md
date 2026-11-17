# Motzkin last-entry law and winding-selected basins in a directed three-colour cyclic automaton

## Finding

For every integer \(n\ge2\), place states \(x_i\in\mathbb Z/3\mathbb Z\) on the oriented ring \(i\in\mathbb Z/n\mathbb Z\). Define synchronous dynamics by
\[
F(x)_i=\begin{cases}x_i+1\pmod3,&x_{i+1}=x_i+1\pmod3,\\x_i,&\text{otherwise}.\end{cases}
\]
Let \(\tau(x)\) be the least nonnegative time at which \(F^{\tau(x)}(x)\) belongs to a periodic orbit (the first periodic-entry time, not the first time the state repeats in a forward list). Then \(\tau(x)\le n-1\), and equality is attained for every \(n\ge2\).

Let \(M_j\) be the Motzkin number counting length-\(j\) walks from height zero back to zero with increments \(-1,0,+1\), never becoming negative. The exact count of labelled initial configurations first becoming periodic at the last permitted update is
\[
E_n=\#\{x:\tau(x)=n-1\}=3nM_{n-2}.
\]
In particular, for uniformly random independent initial states,
\[
\mathbb P(\tau=n-1)=\frac{3nM_{n-2}}{3^n}
\sim\frac{\sqrt3}{2\sqrt{\pi n}}.
\]

Write \(d_i=(x_{i+1}-x_i)\bmod3\in\{0,1,2\}\) and define the integer signed winding \(K(x)=\#\{d_i=1\}-\#\{d_i=2\}\). It is an exact invariant, always divisible by three. If \(K>0\), the eventual dynamics rotates the state word by one site at every update; if \(K\le0\), the eventual dynamics is fixed. Define
\[
T_n=\sum_{j=0}^{\lfloor n/2\rfloor}\frac{n!}{j!^2(n-2j)!}.
\]
Then the exact labelled attraction-basin sizes are
\[
N_{\rm rotating}=\frac{3^n-3T_n}{2},\qquad
N_{\rm fixed}=\frac{3^n+3T_n}{2}.
\]
The rotational orbits can have primitive periods properly dividing \(n\), and this statement concerns the entire basins, not just the periodic configurations. The two limiting basin probabilities are both \(1/2\), whereas the extreme settling-time probability is of order \(n^{-1/2}\).

## Assumptions and scope

The ring contains \(n\) individually labelled sites and exactly one directed observed neighbour per site, namely \(i+1\) modulo \(n\). All updates are simultaneous and deterministic. An initial condition is any of the \(3^n\) colour words; probability statements use the uniform product measure on these words. No undirected or two-sided-neighbour dynamics is claimed. At time \(t\), site states are read modulo three but the signed winding \(K\) is an ordinary integer.

## Proof

**1. Exact particle conjugacy.** Let \(a_i=\mathbf1_{\{d_i=1\}}\). Since \(F(x)_i=x_i+a_i\pmod3\),
\[
d_i'=d_i+a_{i+1}-a_i\pmod3.
\]
Checking \(d_i=0,1,2\) gives the following complete local rule: a particle of type \(1\) moves from edge \(i+1\) to edge \(i\) in one update; a particle of type \(2\) does not move; whenever the moving \(1\) arrives on an occupied \(2\), both disappear. Formally, with indicators \(p_i=\mathbf1_{\{d_i=1\}}\), \(q_i=\mathbf1_{\{d_i=2\}}\),
\[
p_i'=p_{i+1}(1-q_i),\qquad q_i'=q_i(1-p_{i+1}).
\]
No particle is created. Every annihilation removes exactly one particle of each type, so \(K=\sum_i(p_i-q_i)\) is invariant. Because \(\sum_i d_i\equiv0\pmod3\), \(K\equiv0\pmod3\). Conversely, any edge word with \(K\equiv0\pmod3\) admits exactly three vertex-colour lifts (choose \(x_0\), then accumulate the differences).

**2. Exact terminal dynamics and sharp deadline.** If both particle types were present after \(n-1\) updates, select one surviving type-\(1\) particle and one surviving stationary type-\(2\) particle. The former moves left at every update without interruption because it survives, thus has visited all \(n-1\) other sites over those updates; it must have landed on the latter stationary particle, contradicting their joint survival. Therefore, within \(n-1\) updates at least one type vanishes. The resulting one-type state is already periodic: if no type-\(1\) remains, no vertex updates and the state is fixed; if no type-\(2\) remains, the difference word consists solely of zeros and ones, so \(F(x)_i=x_i+d_i=x_{i+1}\), a rigid left rotation. In these cases no further annihilation can occur. If \(K>0\), a positive number of type-\(1\) particles must survive, hence the rotating case holds (the constant colour case has \(K=0\)). If \(K<0\), type-\(2\) survives and the state is fixed; at \(K=0\), both types annihilate completely, leaving a constant fixed state.

**3. Bijection for last-entry trajectories.** A configuration with \(\tau=n-1\) has a collision in update \(n-1\); otherwise, one particle type would already have vanished. There is exactly one collision at that update: two surviving moving particles would each have traversed the starting locations of all stationary particles except their own, hence could not both make distinct last-round collisions. Choose the last stationary type-\(2\) particle as the origin of an oriented edge-word reading from its position in the increasing site direction. The last moving type-\(1\) particle must start at the immediately preceding site in that direction, because its collision takes the full \(n-1\) moves. Thus the initial difference word, read from the stationary origin, is
\[
(2,u_1,\ldots,u_{n-2},1).
\]
Every other particle lies in the interior. They must annihilate internally before the outer moving particle arrives at the origin. Reading this interior word in the increasing direction, type \(2\) (stationary target) is an opening symbol and type \(1\) (moving particle) is its closing symbol. Exactly those interiors with every prefix having at least as many type-\(2\) as type-\(1\) symbols, and with equal total numbers, have all their particles matched internally; zeros contribute horizontal steps. This is the Motzkin-excursion condition \(u\in\mathcal M_{n-2}\). The matching is the ordinary last-in-first-out noncrossing matching: an interior type-\(1\) annihilates at the closest unmatched type-\(2\) to its left, and any such collision needs fewer than \(n-1\) moves. Conversely every Motzkin interior cancels completely before time \(n-1\), leaving the outer pair to meet only at update \(n-1\). The last collision is unique, so the specified origin is unique for every initial edge word; cyclicly rotating a construction cannot cause double counting. Hence there are exactly \(nM_{n-2}\) eligible edge words. All contain equal numbers of types one and two, so their modular edge sum is zero and each has three colour lifts. This proves \(E_n=3nM_{n-2}\) and exhibits examples attaining the bound (take the all-zero interior).

**4. Basin count by winding sign.** An edge word with \(K=0\) contains \(j\) particles of each type and \(n-2j\) zeros for some \(j\), giving \(T_n\) words as stated. There are \(3T_n\) lifts. The involution that swaps type \(1\) and type \(2\) on every edge reverses the sign of \(K\) and preserves the modular-lift condition. Thus, among the remaining \(3^n-3T_n\) colour words, exactly half have positive winding and half have negative winding. By Step 2 this gives the basin formulas.

**5. Asymptotic calculations.** The Motzkin generating function satisfies \(M(z)=1+zM(z)+z^2M(z)^2\), whence
\[
M_j\sim\frac{3\sqrt3}{2\sqrt\pi}\frac{3^j}{j^{3/2}}.
\]
Substituting into the expression for \(E_n\) proves its square-root tail. Independently, \(T_n\) is the central trinomial coefficient: a local central limit theorem for the sum of \(n\) independent uniform \(-1,0,1\) steps gives \(T_n\sim 3^n\sqrt3/(2\sqrt{\pi n})\); hence each basin fraction tends to \(1/2\).

## Verification

Reproducible Python 3 standard-library scripts are included as `verify_direct.py` and `verify_motzkin.py`. The first independently updates all labelled vertex words through sizes \(2\le n\le10\), identifies the least periodic-entry time by a genuine cycle test, and checks the deadline, winding-selected basin counts, and last-entry formula. The second implements the derived particle rule independently, exhaustively compares the late-collision particle words with the cyclic Motzkin constructions for \(2\le n\le11\), and computes exact asymptotic ratios at \(n=50,100,200,400\). Outputs are preserved in `direct_output.txt` and `motzkin_output.txt`; the scripts use no nonstandard dependencies. Finite checks are supporting tests, not a replacement for the all-size proof.

## Relationship to prior work

The nearest dynamical predecessor is **Kůrka, Formenti and Dennunzio (2011/2012)**, *Asymptotic distribution of entry times in a cellular automaton with annihilating particles* (DOI `10.46298/dmtcs.2976`). Their asymmetric-gliders cellular automaton has **exactly the same stationary/left-moving particle-annihilation rule** as our edge-difference system, so the particle rule and its random-walk matching method are **not** claimed as new. Its source is the bi-infinite line with independent particle symbols, and its **entry time** (Definition 1) is the waiting time for a particle to appear **at a specified site after a chosen age**, rather than the least time a **finite periodic ring enters its eventual periodic orbit**. Theorems 1–3 and the subsequent proofs derive scaled infinite-line particle arrival distributions. They do not state or directly imply the cyclic zero-sum lifted-word Motzkin last-entry count, the uniform maximum \(n-1\) cutoff, or the signed-winding basin census for the vertex automaton. This closest paper's 12 pages were read in full.

Foundational work on cyclic cellular automata includes Fisch's 1990 work, Durrett–Griffeath's 1993 excitable-automaton study, and Belitsky–Ferrari's ballistic-annihilation work. The fully inspected Hellouin de Menibus–Le Borgne (2019) article studies the **two**-neighbour three-state process on the bi-infinite line, with particles moving in both directions. The present claim is restricted to the extra global finite-ring combinatorics, not a new particle reduction, nor any novelty claim about Motzkin numbers themselves. Searches alone cannot prove historical priority.

## Limitations

The result does not cover the two-sided standard cyclic automaton, thresholds greater than one, other numbers of colours, nonuniform initial probabilities, or arbitrary directed graphs. The original asymmetric-glider paper (Kůrka–Formenti–Dennunzio) already establishes the underlying collision rule, and the full text of Belitsky–Ferrari (1995) was not accessible during the literature comparison, leaving residual priority risk; a similar formula in unpublished or less-indexed finite-ring treatments remains possible. Independent mathematical audit has not been performed. The first day-resolved public posting used for archival-source dating is the 1993-03-22 arXiv release of Durrett–Griffeath, not the publication dates of older foundational papers.

## References

1. R. Fisch, *The one-dimensional cyclic cellular automaton: A system with deterministic dynamics that emulates an interacting particle system with stochastic dynamics*, Journal of Theoretical Probability **3** (1990), 311–338. DOI: `10.1007/BF01045164`. The paper's rule observes two neighbours.
2. R. Fisch, *Clustering in the One-Dimensional Three-Color Cyclic Cellular Automaton*, Annals of Probability **20** (1992), 1528–1548. DOI: `10.1214/aop/1176989705`.
3. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, first arXiv posting 1993-03-22, `patt-sol/9303002`.
4. V. Belitsky and P. A. Ferrari, *Ballistic annihilation and deterministic surface growth*, Journal of Statistical Physics **80** (1995), 517–543. DOI: `10.1007/BF02178546` (abstract/bibliography inspected; full text not accessed).
5. P. Kůrka, E. Formenti and A. Dennunzio, *Asymptotic distribution of entry times in a cellular automaton with annihilating particles*, Automata 2011, DMTCS Proceedings AP (2012), 47–58. DOI: `10.46298/dmtcs.2976` (complete 12-page article inspected).
6. B. Hellouin de Menibus and Y. Le Borgne, *Asymptotic behaviour of the one-dimensional “rock-paper-scissors” cyclic cellular automaton*, arXiv `1903.12622` (2019; full available article inspected).
