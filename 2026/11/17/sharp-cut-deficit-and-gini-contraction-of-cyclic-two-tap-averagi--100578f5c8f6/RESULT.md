# Sharp cut-deficit and Gini contraction of cyclic two-tap averaging

## Finding
For each integer \(n\ge2\) and real \(\theta\in[0,1]\), let \(P_{n,\theta}\) act on real samples indexed cyclically by
\[
 (P_{n,\theta}f)_i=(1-\theta)f_i+\theta f_{i+1\bmod n}.
\]
For complete-pair Gini variation
\[
 G_n(f)=\sum_{0\le i<j<n}|f_i-f_j|,
\]
the attained operator quotient seminorm is
\[
 \boxed{\|P_{n,\theta}\|_{G_n\to G_n}=1-\frac{2\min\{\theta,1-\theta\}}{\lfloor n^2/4\rfloor}.}
\]
More precisely, if \(S\) is any nonempty proper subset, \(k=|S|\), and \(r\) is the number of its cyclic runs of consecutive elements, then
\[
 \boxed{G_n(P_{n,\theta}{\bf1}_S)=k(n-k)-2\min\{\theta,1-\theta\}r^2.}
\]
For interior weights \(0<\theta<1\), exactly the single cyclic arcs of cardinality \(\lfloor n/2\rfloor\) or \(\lceil n/2\rceil\) maximize the quotient **among binary cuts**. The optimal mixing parameter \(\theta=1/2\) uniquely minimizes the norm, with value \(1-1/\lfloor n^2/4\rfloor\).

For \(n\ge4\) and \(0<\theta<1\), the Dobrushin oscillation coefficient is exactly one even though the above Gini coefficient is strictly below one.

## Assumptions and scope
Signals are arbitrary real \(n\)-vectors, not necessarily nonnegative. Indices are in \(\mathbb Z/n\mathbb Z\); the two positions \(i\) and \(i+1\) are distinct because \(n\ge2\). The Gini seminorm vanishes exactly on constant vectors. The induced quotient coefficient is the supremum of \(G_n(Pf)/G_n(f)\) over all nonconstant real signals. No stationarity or probabilistic sampling hypothesis is needed. Both endpoint parameters \(\theta=0\) and \(\theta=1\) are included, as are both parities of \(n\).

## Proof
**Step 1: an exact binary-cut deficit.** For each nonempty proper \(S\subset\mathbb Z/n\mathbb Z\), put \(s_i={\bf1}_S(i)\), \(k=|S|\), and \(\alpha=\min\{\theta,1-\theta\}\). By the cyclic shift symmetry of complete-pair variation,
\[
 \sum_{i<j}\big((1-\theta)|s_i-s_j|+\theta|s_{i+1}-s_{j+1}|\big)=G_n(s)=k(n-k).
\]
The triangle inequality is an equality for each pair unless the differences \(s_i-s_j\) and \(s_{i+1}-s_{j+1}\) have opposite nonzero signs. For such a pair the difference between the weighted sum of absolute values and the absolute value of the weighted sum is \(1-|1-2\theta|=2\alpha\). A pair has opposite signs precisely when one of the indexed directed cyclic edges is a transition \(0\to1\) and the other a transition \(1\to0\). A binary cyclic word with \(r\) runs of ones has exactly \(r\) edges of each transition type, giving precisely \(r^2\) unordered conflicting edge pairs. Summing proves
\[
 G_n(P_{n,\theta}s)=k(n-k)-2\alpha r^2.
\]

**Step 2: sharp optimization over cuts.** For every nontrivial \(S\), \(r\ge1\) and \(k(n-k)\le B_n:=\lfloor n^2/4\rfloor\), so
\[
 \frac{G_n(P_{n,\theta}s)}{G_n(s)}=1-\frac{2\alpha r^2}{k(n-k)}\le1-\frac{2\alpha}{B_n}.
\]
Choose \(S\) as a contiguous cyclic arc of \(\lfloor n/2\rfloor\) sites. Then \(r=1\) and \(k(n-k)=B_n\), giving equality. If \(0<\theta<1\), equality forces both \(r=1\) and \(k(n-k)=B_n\), proving the claimed complete classification of binary-cut maximizers.

**Step 3: arbitrary real signals.** Let \(m=\min_i f_i\), \(M=\max_i f_i\), and \(S_t=\{i:f_i>t\}\). For every coordinate,
\[
 f_i=m+\int_m^M {\bf1}_{S_t}(i)\,dt.
\]
Because \(P_{n,\theta}\) is linear and preserves constants, subadditivity of \(G_n\) gives
\[
 G_n(P_{n,\theta}f)\le\int_m^M G_n(P_{n,\theta}{\bf1}_{S_t})\,dt\le
 (1-2\alpha/B_n)\int_m^M G_n({\bf1}_{S_t})\,dt
 =(1-2\alpha/B_n)G_n(f).
\]
The final equality is the pairwise layer-cake identity. Step 2 supplies an attaining nonconstant binary signal. The endpoint cases \(\alpha=0\) give identity or cyclic permutation, each of norm one.

**Step 4: optimal weight and the oscillation contrast.** The coefficient depends affinely and decreasingly on \(\alpha\in[0,1/2]\); its unique minimum is at \(\theta=1/2\). For \(n\ge4\), distinct rows numbered \(0\) and \(2\) of the stochastic matrix have disjoint supports \(\{0,1\}\) and \(\{2,3\}\). The classical Dobrushin coefficient is therefore one; since \(\alpha>0\), the Gini coefficient is strictly below one. This comparison also holds at \(n=4\).

## Verification
A standalone Python checker, `verify_two_tap_gini.py`, uses `fractions.Fraction` arithmetic. It tests the exact cut-deficit identity and sharp balanced witnesses for all binary words of lengths 2 through 12 and five rational weights; it separately verifies 58,500 nonconstant rational-input cases of lengths 2 through 6 and the disjoint-support comparison for dimensions 4 through 29. Its reported results are:

```
EXACT_ALL_BINARY_CUT_DEFICITS_AND_SHARP_BISECTIONS_PASSED 40830
EXACT_NONBINARY_RATIONAL_SIGNAL_CHECKS_PASSED 58500
EXACT_DOBRUSHIN_SEPARATION_CHECKS_PASSED_N4_TO_N29
ALL_TWO_TAP_CYCLIC_GINI_CHECKS_PASSED
```
The exact proof, not the finite enumeration, establishes every dimension and every real parameter.

## Relationship to prior work
Gaubert and Qu (2013, arXiv:1302.5226, Theorem 1.1 and its finite stochastic specialization) develop the Dobrushin coefficient as the induced Hopf-oscillation contraction and the dual total-variation coefficient. For the present local kernel that coefficient is one from dimension four onward, and hence does not supply the new strict Gini coefficient. Majorization implies nonincrease of every permutation-invariant convex variation under bistochastic averaging; it does not quantify this exact positive deficit. The present cut calculation determines the sharp finite-size deficit and its balanced-arc attainment.

## Limitations
This is a one-step result for the homogeneous, directed two-tap cyclic kernel and **unweighted** complete-pair Gini variation. It does not determine optimal contraction for powers of this kernel, spatially variable weights, or arbitrary circulant convolutions. The equality statement classifies binary extremizers, not all real extremizers. Historical unindexed equivalents cannot be excluded merely by a database search.

## References
- S. Gaubert and Z. Qu, *Dobrushin ergodicity coefficient for Markov operators on cones, and beyond*, arXiv:1302.5226, first public version dated 2013-02-21, Sections 1 and 4; https://arxiv.org/abs/1302.5226.
