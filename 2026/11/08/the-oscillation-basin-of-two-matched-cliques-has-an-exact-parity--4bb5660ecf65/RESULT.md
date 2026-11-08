# The oscillation basin of two matched cliques has an exact parity law

## Finding
For every integer \(n\ge2\), let \(G_n=K_2\square K_n\), the graph of two labelled \(n\)-vertex complete graphs with corresponding vertices joined by a perfect matching. Apply synchronous strict open-neighbor binary majority, retaining the current spin at a tie. Let \(P_2(n)\) be the number of configurations of **least period two at time zero**, and let \(B_2(n)\) be the number of configurations that **eventually reach a least-period-two orbit**, allowing a transient. Then

\[
B_2(n)=\begin{cases}
\binom{n}{n/2}\bigl(\binom{n}{n/2}-1\bigr),&n\text{ even},\\[3pt]
\dfrac{n^2+2n+5}{2}\binom{n}{(n-1)/2},&n\text{ odd}.
\end{cases}
\]

Every configuration counted by \(B_2(n)\) enters its two-cycle by time one. Exactly
\[
B_2(n)-P_2(n)=\begin{cases}
0,&n\text{ even},\\
2n(n-1)\binom{n-2}{(n-3)/2},&n\text{ odd},
\end{cases}
\]
configurations enter a primitive two-cycle after **one** update rather than starting in it. The immediate-period count is
\[
P_2(n)=\begin{cases}
\binom{n}{n/2}\bigl(\binom{n}{n/2}-1\bigr),&n\text{ even},\\
(n+3)\binom{n}{(n-1)/2},&n\text{ odd}.
\end{cases}
\]
The numbers of fixed configurations are \(P_1(n)=4+\binom{n}{n/2}\) for even \(n\) and \(P_1(n)=4\) for odd \(n\). No orbit has least period greater than two. Every starting configuration first becomes periodic in at most two updates when \(n\) is even, or at most three when \(n\) is odd; these two bounds are attained when \(n\ge4\) is even and \(n\ge5\) is odd, respectively. The exceptional maximum transient lengths are one at \(n=2\) and two at \(n=3\).

For unbiased independent initial spins, the eventual oscillation probabilities are
\[
\frac{B_2(n)}{4^n}\sim\begin{cases}
\dfrac{2}{\pi n},&n\to\infty\text{ through even integers},\\[3pt]
\dfrac{n^{3/2}}{\sqrt{2\pi}}\,2^{-n},&n\to\infty\text{ through odd integers}.
\end{cases}
\]
Thus, **newly entering oscillatory states exist only at odd clique orders**, and even after all transients are included the oscillation basin has an exponential-versus-polynomial parity gap.

## Assumptions and scope
The graph is finite, loopless and simple. Both cliques have exactly \(n\ge2\) vertices and a single corresponding-vertex perfect matching. Vertices are distinguished by row and column. A configuration is \((x,y)\in\{-1,+1\}^n\times\{-1,+1\}^n\). If \(X=\sum_i x_i\), \(Y=\sum_i y_i\), its update \(M(x,y)=(x',y')\) has local fields
\[
H^x_i=X-x_i+y_i,\qquad H^y_i=Y-y_i+x_i.
\]
The updated spin is the sign of a nonzero local field; if a field is zero, its spin is retained. Entry time is the least nonnegative \(t\) for which \(M^{t+2}(x,y)=M^t(x,y)\). The oscillation basin additionally requires \(M^{t+1}(x,y)\ne M^t(x,y)\). Counts include all labelled initial configurations, not orbits modulo graph automorphisms.

## Proof
**1. The row-threshold reductions.** A row with total spin \(X\ge3\) becomes uniformly positive in one update because \(X-x_i+y_i\ge X-2>0\); the negative case is symmetric. Every uniform row stays uniform forever: its field has its own sign or is a tie retaining that sign, since \(n\ge2\).

For even \(n\), a row sum \(X\ne0\) has magnitude at least two and becomes uniformly \(\operatorname{sgn}(X)\), with ties retaining the already matching sign. A row with \(X=0\) is copied from the opposite row: \(x'_i=y_i\). Therefore if both row sums are zero, \(M(x,y)=(y,x)\), an immediate involution. If either sum is nonzero, a uniform row appears after one step; at most one additional update makes both rows uniform, after which the state is fixed. There are four uniform-row fixed states and exactly \(\binom{n}{n/2}\) additional fixed states \((x,x)\) with \(X=0\). Subtracting these diagonal states from the \(\binom{n}{n/2}^2\) pairs of zero-sum rows proves the even formulas, and shows that no even-order transient ever enters a two-cycle.

For odd \(n\), any row that has total spin with magnitude at least three becomes uniform and cannot subsequently join a primitive two-cycle. Once a row is uniform, the other row becomes uniform in at most two more updates. To see this, take the first row positive by sign symmetry. With an odd current other-row sum \(Y\), that row becomes entirely positive if \(Y\ge1\), entirely negative if \(Y\le-3\), and changes every spin if \(Y=-1\); in the last case its new sum is \(+1\) and it becomes uniformly positive at the following update.

Consequently all primitive two-cycles and their nonperiodic predecessors must initially have both row sums among \(\{-1,+1\}\). Such a predecessor cannot have had a row with magnitude at least three, because uniformity is irreversible.

**2. Odd-order four-type classification.** Let \(n=2k+1\) with \(k\ge1\). Classify matched columns by spin types \((+,+),(+,-),(-,+),(-,-)\) and denote their multiplicities by \((a,b,c,d)\). The row sums satisfy
\[
X=a+b-c-d,\qquad Y=a+c-b-d.
\]
When \(X=Y=+1\), these equations give \(a=d+1\) and \(b=c\). The update has negative first-row spins exactly at the \(b\) columns of type \((+,-)\), and negative second-row spins exactly at the \(c\) columns of type \((-,+)\); both new sums equal \(2d+1\). If \(d\ge1\), the next state has two uniform positive rows and is not oscillatory. If \(d=0\), then \((a,b,c,d)=(1,k,k,0)\), and the map swaps the two mismatch types, giving a primitive two-cycle. Sign reversal similarly yields \((0,k,k,1)\) for \(X=Y=-1\).

When \(X=+1,Y=-1\), the equations give \(a=d\), \(b=c+1\), and the first update makes **every** matched column opposite. If \(a=0\), the original state is already opposite in every column, with multiplicities \((0,k+1,k,0)\); the update flips all columns and yields a primitive two-cycle. If \(a=1\), then \((a,b,c,d)=(1,k,k-1,1)\); the updated state has opposite columns and row sums \(+1,-1\), hence is an immediately primitive two-periodic state, while the original is not (it contains two same-sign columns). If \(a\ge2\), the updated sums are \(2a-1\) and \(1-2a\), so the subsequent state has two uniform rows and cannot oscillate. The sign-reversed case has respectively \((0,k,k+1,0)\) as immediate two-cycle and \((1,k-1,k,1)\) as one-step predecessor. Opposite columns remain opposite under every update, including ties, because their two local fields are negatives and their old signs are negatives.

There are no other candidate row-sum pairs. This also proves that all odd-order oscillatory states have entry time at most one and no odd-order fixed state is nonuniform. The four uniform-row configurations are fixed.

**3. Count the classified types.** Each ordered quadruple \((a,b,c,d)\) contributes \(n!/(a!b!c!d!)\) labelled states. The four immediate two-cycle types contribute
\[
P_2(n)=2\frac{n!}{k!k!}+2\frac{n!}{(k+1)!k!}=(n+3)\binom nk.
\]
The two additional one-step types contribute
\[
2\frac{n!}{k!(k-1)!}=2n(n-1)\binom{n-2}{k-1}
=\frac{n^2-1}{2}\binom nk.
\]
Adding gives \(B_2(n)=\frac{n^2+2n+5}{2}\binom nk\). Neither case permits periods above two, because the explicit row reductions send every state either to a fixed point or to one of the described two-cycles within the stated finite time.

**4. Sharp entry bounds.** For even \(n\ge4\), choose the first row of sum zero and a nonuniform second row of sum two. After one update the second row is uniform, while the first row becomes the original nonuniform second row; after the second update both rows are uniform. For odd \(n\ge5\), choose the first row with exactly one negative spin and the second row of sum \(-1\), with its negative set containing the unique negative first-row vertex. The first row becomes uniformly positive at time one; the second row then has sum \(-1\), flips all spins at time two, and becomes uniformly positive at time three. These exhibit the bounds. Direct small-order checking or the same local cases give maxima one and two for \(n=2,3\).

**5. Asymptotics.** Stirling's formula gives \(\binom{n}{n/2}\sim2^n\sqrt{2/(\pi n)}\) along even \(n\), and \(\binom{n}{(n-1)/2}\sim2^n\sqrt{2/(\pi n)}\) along odd \(n\). Substitution gives both probability estimates.

## Verification
The proof applies to **every** integer \(n\ge2\). The included `check_direct.py` independently constructs every open-neighbor mask and exhaustively iterates all configurations for \(n=2,\ldots,8\): 87,376 initial configurations. It verifies exact fixed and immediate two-cycle populations, eventual two-cycle basin populations, and the maximum transient lengths, including that oscillation-entry times never exceed one. `check_multinomial.py` independently enumerates all four matched-column types with exact multinomial weights for \(n=2,\ldots,40\), totaling 135,746 type cases. It checks both formulas and the one-step predecessor population. Their exact standard outputs are supplied separately. Run with `python3 check_direct.py` and `python3 check_multinomial.py`, using the standard Python library only. Finite tests provide independent error detection, not a substitute for the general proof.

## Relationship to prior work
Benjamini, Chan, O'Donnell, Tamuz and Tan (initial arXiv posting May 11, 2014) formulate tie-retaining majority dynamics and study random and unimodular graphs; their general period-two framework does not count the basin on the present deterministic matched-clique family. Goles–Olivos (1980) establish general period-at-most-two behavior of symmetric threshold systems, without the graph-specific basin census. Fountoulakis–Kang–Makai (2020) study rapid consensus on random dense graphs. Bujtás and coauthors (2026) determine the maximum number of majority-coloring classes on Hamming graphs; in the two-color case their *static* coloring condition matches majority fixed points, but their Theorem 4 is a chromatic-number statement, not a count of dynamic two-cycle basins or transients.

This census is for binary majority with inertia at ties. It is not implied by results for three-state excitation dynamics on the same graph, by static majority-colorability, or by immediately periodic counts for a different paired graph. Alternative names for the graph include the two-row rook graph and two matched cliques.

## Limitations
No formula is supplied for basin sizes of *individual* two-cycles, or for outcomes under biased initial measures. The novelty comparison covers the identified relevant primary material and semantic-database searches but cannot exclude unindexed equivalent results. The full 1980 article was not inspected; its accessible abstract states the general two-cycle theorem, not a particular matched-clique census. The counting and transient theorem is fully mathematical, but has not undergone independent external review.

## References
1. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486 (first public version May 11, 2014), https://arxiv.org/abs/1405.2486.
2. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189, DOI:10.1016/0012-365X(80)90121-1.
3. N. Fountoulakis, M. Kang, T. Makai, *Resolution of a conjecture on majority dynamics: Rapid stabilization in dense random graphs*, Random Structures & Algorithms **57** (2020), 1134–1156, DOI:10.1002/rsa.20970.
4. C. Bujtás, M. Dettlaff, H. Furmańczyk, A. Laskowska, Z. Tuza, *Majority C-coloring in Cartesian products*, arXiv:2608.27669 (first public version August 27, 2026), https://arxiv.org/abs/2608.27669.
