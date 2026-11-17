# Collision-column parity and joint fixed-state statistics of the HPP lattice gas on two-row tori

## Finding

Consider the four-velocity Hardy–Pomeau–de Pazzis (HPP) lattice gas with periodic boundary conditions on the labelled square-lattice cylinder \(\mathbb Z_2\times\mathbb Z_n\), for every integer \(n\ge3\). A site has four independently occupied-or-empty channels, pointing north, east, south and west. The reversible head-on collision exchanges exactly the two pure opposite-pair masks \(NS\) and \(EW\), leaving the other fourteen masks unchanged. Streaming moves each occupied channel by one lattice edge in its direction. On a two-row periodic lattice, north and south channels stream to the same site in the opposite row but remain distinct channels.

Let \(P(x)\) be the total number of occupied velocity channels in a configuration \(x\). For a fixed configuration, let \(K(x)\) be the number of columns containing a head-on collision mask (at either site). Each such column actually contains one collision mask at **both** sites, so it corresponds to two collision events per synchronous step. Put

\[
H_n(u,v)=\sum_{x:\,\Phi(x)=x}u^{P(x)}v^{K(x)},
\]

where \(\Phi\) is one full collision-and-streaming step. Define

\[
\begin{aligned}
a(u)&=u^2(1+u^2)^2,& b(u)&=u(1+2u^2),\\
c(u)&=u^5(2+u^2),&d(u)&=1+2u^2,\\
e(u)&=u^6(2+u^2),&f(u)&=2u^4.
\end{aligned}
\]

**Theorem (complete joint stationary census).** For all \(n\ge3\),

\[
\boxed{H_n(u,v)=(a(u)+u^4v)^n+(a(u)-u^4v)^n
+2a(u)^n+4b(u)^n+4c(u)^n+d(u)^n+e(u)^n+2f(u)^n.}
\]

In particular every fixed configuration has an **even** number of collision columns, and

\[
|\operatorname{Fix}(\Phi)|=5^n+2\cdot4^n+11\cdot3^n+2\cdot2^n.
\]

The exact number having precisely \(k\) collision columns, for even \(k\ge2\), is \(2\binom nk4^{n-k}\); it is zero for odd \(k\). The collision-free population is \(4\cdot4^n+10\cdot3^n+2\cdot2^n\).

For uniformly chosen fixed configurations, the occupation and collision-column counts satisfy

\[
\mathbb E[P_n\mid K_n=k]=4n\quad\text{for every admissible }k,
\qquad \operatorname{Cov}(P_n,K_n)=0
\]

**at every circumference**, and have the joint weak limit

\[
\left(\frac{P_n-4n}{\sqrt n},\frac{K_n-n/5}{\sqrt n}\right)
\Longrightarrow\mathcal N_2\!\left(
\binom00,\begin{pmatrix}8/5&0\\0&4/25\end{pmatrix}\right).
\]

Thus the two fluctuation coordinates are asymptotically independent. The fixed-state spatial entropy is \(\frac12\log5\) per lattice site. The probability of no collision columns is asymptotic to \(4(4/5)^n\), although every configuration in this ensemble is invariant under a full dynamical step.

## Assumptions and scope

The lattice is labelled: spatial translations, reflections, direction labels, and global particle-hole complementation are **not** identified. Every site has four channels, including distinct north and south labels even though their destinations coincide on this thin periodic torus. Only states with \(\Phi(x)=x\), not general recurrent trajectories or invariant probability measures, are counted. The convention \(\Phi=S\circ C\) applies the local collision involution \(C\) before the streaming permutation \(S\). The opposite update convention \(C\circ S\) has the same joint polynomial because it is conjugate by streaming, and that conjugacy preserves the two statistics on the fixed set (as proved below). The exponent of \(v\) counts collision *columns*, not individual site collisions; individual collision events per step number \(2K(x)\). The limit \(n\to\infty\) runs through all integers \(n\ge3\).

## Proof

Write \(N_{rj},E_{rj},S_{rj},W_{rj}\in\{0,1\}\) for the channel bits at row \(r\in\mathbb Z_2\) and column \(j\in\mathbb Z_n\). Work first with \(\Psi=C\circ S\). Since \(C^2=1\), a configuration is fixed by \(\Psi\) exactly when \(Sx=Cx\). Let \(t_{rj}\) be one if the local mask of \(x\) is either \(NS\) or \(EW\), and zero otherwise. Collision complements all four channel bits at exactly these two masks. Comparing the four components in \(Sx=Cx\) yields

\[
\begin{aligned}
N_{rj}\oplus N_{1-r,j}&=t_{rj},&S_{rj}\oplus S_{1-r,j}&=t_{rj},\\
E_{rj}\oplus E_{r,j-1}&=t_{rj},&W_{rj}\oplus W_{r,j+1}&=t_{rj}.
\end{aligned}
\]

The north equality in the two rows forces \(t_{0j}=t_{1j}=:t_j\). The east equality summed around the ring gives \(\sum_jt_j\equiv0\pmod2\). If at least one \(t_j=1\), the two local masks in that column must be complementary: one \(NS\), the other \(EW\). Furthermore the east and west equations imply that \(E_{rj}\oplus W_{rj}\oplus t_j\) is constant across \(j\), and its value must be one at a collision column. Therefore \(E_{rj}\ne W_{rj}\) for every column with \(t_j=0\), while the two rows' east bits are complementary in every column. After choosing an even nonempty set of collision columns, one initial east bit determines all horizontal channels in both rows. There are exactly two such global choices. In each noncollision column, north and south are respectively shared between the two rows and may be chosen independently, producing the polynomial \(a(u)=u^2(1+u^2)^2\). In a collision column, the two opposite pure pairs are forced and give four occupied channels, hence weight \(u^4v\). Conversely every such choice obeys the four displayed equalities and has exactly the intended collision masks. Thus the contribution from exactly \(k\ge2\) collision columns is

\[
2\binom nk a(u)^{n-k}(u^4v)^k,\qquad k\text{ even}.
\]

If there are no collision columns, each row's east and west bits are constant in \(j\), while north and south bits are each common between the two rows in a column. There are sixteen ordered pairs of constant row-horizontal masks. Excluding pure head-on masks gives the following exhaustive cases (each weight is per column and is raised to the \(n\)-th power):

| Horizontal masks across the two rows | Multiplicity | Per-column weight |
|---|---:|---|
| Both masks mixed (one east and one west) | 4 | \(a(u)\) |
| One empty horizontal pair and one mixed | 4 | \(b(u)\) |
| One full horizontal pair and one mixed | 4 | \(c(u)\) |
| Both horizontal pairs empty | 1 | \(d(u)\) |
| Both horizontal pairs full | 1 | \(e(u)\) |
| One empty and one full horizontal pair | 2 | \(f(u)\) |

The zero-collision contribution is therefore \(4a^n+4b^n+4c^n+d^n+e^n+2f^n\). Summing the even nonempty collision-column contribution via the binomial theorem gives \((a+u^4v)^n+(a-u^4v)^n-2a^n\), proving the boxed identity.

For the usual collision-then-streaming convention, \(\Phi=S\Psi S^{-1}\). If \(y\in\operatorname{Fix}(\Psi)\), then \(Sy=Cy\), so \(x=Sy=Cy\) is fixed by \(\Phi\). The local involution preserves the particle count and which sites have pure head-on masks, even at the swapped masks. Therefore \(P(x)=P(y)\) and \(K(x)=K(y)\), proving that the same joint census applies.

Particle-hole complementation of all channels commutes with \(S\) and \(C\), preserves \(K\), and maps \(P\) to \(8n-P\). Hence the conditional occupation law is symmetric about \(4n\) for each attainable collision count, proving exact conditional half filling and zero covariance.

Finally, in a complex neighborhood of \(u=v=1\), the unique term of largest modulus in the joint polynomial is \((a(u)+u^4v)^n\); all other terms are exponentially smaller uniformly near that point. With \(u=e^t\), \(v=e^s\), its normalized logarithmic moment generating function converges locally to

\[
\log\frac{e^{2t}+2e^{4t}+e^{6t}+e^{4t+s}}5.
\]

Its gradient at zero is \((4,1/5)\) and its Hessian is \(\operatorname{diag}(8/5,4/25)\). The local analytic expansion of the normalized moment generating functions at scale \(n^{-1/2}\) proves the bivariate normal limit. Evaluation at \(u=v=1\) and \(v=0\) gives the asserted growth, entropy, and collision-free probability.

## Verification

A direct site-by-site C++ implementation of streaming and the head-on collision checks every one of the \(16^{2n}\) configurations for \(n=2,3\); its complete bivariate histograms agree coefficient-by-coefficient with the independently implemented polynomial formula. The extra \(n=2\) test is a boundary check only, not part of the stated geometric domain. A separate 65,536-pair-state finite transfer graph, enforcing the original local update rather than the proof classification, gives 566 fixed configurations for \(n=3\) and 2,060 for \(n=4\). The independent transfer computation also matches the complete width-four bivariate histogram. The proof classifies all \(n\ge3\); numerical checks do not replace that proof. Reproduction instructions and recorded outputs are in the accompanying verification package.

| Circumference \(n\) | Fixed states | With at least one collision column |
|---:|---:|---:|
| 3 | 566 | 24 |
| 4 | 2,060 | 194 |
| 5 | 7,910 | 1,320 |
| 6 | 31,964 | 8,162 |
| 7 | 135,206 | 47,544 |
| 8 | 594,380 | 266,114 |

## Relationship to prior work

Hardy, Pomeau and de Pazzis introduced this reversible square-lattice gas in 1973 and studied invariant statistical states and time correlations; their 1976 continuation investigated hydrodynamic behavior. Those studies motivate the object and the collision observable. This theorem instead counts individual, exactly one-step fixed finite-torus microstates and resolves them jointly by mass and active collision columns. General transfer-matrix methods can encode local constraints but do not themselves supply the displayed HPP-specific classification or the parity and fluctuation conclusions. The accessible secondary model description was inspected in full. The original 1973 and 1976 primary full texts could not be accessed, so this account does not claim that they were checked throughout or that absence of the formula in those works is established.

## Limitations

The result is confined to two labelled rows with four distinct velocity channels at each site. It does not classify nonstationary periodic trajectories, thicker tori, mixing of invariant probability measures or fluid behavior. The Gaussian statement refers to **uniform selection among fixed microstates**, not to a typical evolving gas or to the equilibrium distributions in the historical hydrodynamic literature. The first original paper's abstract and publisher metadata were accessible, but its full text and the 1973 invariant-states full text were not; priority remains subject to those and unindexed earlier sources. No independent mathematical audit has been performed.

## References

1. J. Hardy, Y. Pomeau and O. de Pazzis, “Time Evolution of a Two-Dimensional Classical Lattice System,” *Physical Review Letters* **31** (1973), 276–279, published 30 July 1973. https://doi.org/10.1103/PhysRevLett.31.276
2. J. Hardy, Y. Pomeau and O. de Pazzis, “Time evolution of a two-dimensional model system. I. Invariant states and time correlation functions,” *Journal of Mathematical Physics* **14** (1973), 1746–1759. https://doi.org/10.1063/1.1666248
3. J. Hardy, O. de Pazzis and Y. Pomeau, “Molecular dynamics of a classical lattice gas: Transport properties and time correlation functions,” *Physical Review A* **13** (1976), 1949–1961. https://doi.org/10.1103/PhysRevA.13.1949
4. J.-P. Rivet and J. P. Boon, *Lattice Gas Hydrodynamics*, Chapter 3, “Microdynamics: various examples,” Cambridge University Press (2001). https://doi.org/10.1017/CBO9780511524707.004
5. “HPP model,” model description and formal collision/transport rules. https://en.wikipedia.org/wiki/HPP_model
