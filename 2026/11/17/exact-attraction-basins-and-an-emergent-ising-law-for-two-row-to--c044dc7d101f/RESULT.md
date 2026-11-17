# Exact attraction basins and an emergent Ising law for two-row Toom dynamics

## Finding

Let \(n\ge3\). Apply synchronous deterministic north-east-center majority to two binary rows of length \(n\), with periodic coordinates in both directions. The columns are labelled; north of either row is the other row, and east of column \(i\) is column \(i+1\pmod n\). For any binary word \(y=(y_0,\ldots,y_{n-1})\), let \(B_n(y)\) be the number of initial two-row configurations which eventually become the stationary configuration with both rows equal to \(y\). Define its cyclic interface count by \(k(y)=\#\{i:y_i\ne y_{i+1\bmod n}\}\). Then the **complete pointwise basin census** is

\[
 B_n(y)=\begin{cases}
 3^n-2^n,&k(y)=0,\\
 3^{n-k(y)},&k(y)>0.
 \end{cases}
\]

Exactly \(4^n-2^n\) of the \(4^n\) labelled initial states reach such a stationary configuration. The other \(2^n\) states have unequal row bits in every column and undergo cyclic spatial translation. If at least one initially agreeing column exists, the exact first-entry time into a fixed state is the length of the longest cyclic consecutive run of initially unequal columns (zero if all columns agree), and the sharp global maximum is \(n-1\).

For uniform independent initial bits, condition on reaching a row-equal fixed state, and encode its common-row spins as \(s_i=2y_i-1\). The conditional output law is an exact finite-ring ferromagnetic Ising weight with two explicit exceptional masses:

\[
 \Pr(Y=y\mid\text{absorption})=\frac{3^{n-k(y)}-2^n\mathbf1_{k(y)=0}}{4^n-2^n}.
\]

For integer \(1\le r<n\), its exact spin correlation is

\[
 \mathbb E[s_0s_r\mid\text{absorption}]
 =\frac{4^{n-r}2^r+4^r2^{n-r}-2^{n+1}}{4^n-2^n}.
\]

For each fixed separation \(r\), as \(n\to\infty\) the correlations converge to \(2^{-r}\), and all fixed-window distributions converge to the stationary zero-field Ising chain with coupling \(J\) satisfying \(2J=\log3\) (unit inverse temperature). Its one-step spin transition probabilities are \(3/4\) to remain equal and \(1/4\) to change sign. The limiting correlation length is \(1/\log2\). This is a statement about the deterministic *pushforward of uniform initial data under eventual absorption*, not about a unique stochastic stationary distribution on the original two-dimensional model.

## Assumptions and scope

Every update is simultaneous. Binary states are \(0,1\); the local rule is strict majority of exactly three inputs: current site, northern site and eastern site. Spatial columns \(i\in\mathbb Z/n\mathbb Z\) are labelled; no quotient by spatial rotations, reflections or row interchange is taken. Horizontal circumference \(n\ge3\), while vertical circumference is exactly two. Initial distribution in the probabilistic assertions is uniform on all \(2^{2n}=4^n\) configurations, and the absorption conditioning event means that at least one initial column has equal bits. There is no dynamical random noise.

## Proof

Write the column at site \(i\) as \(c_i=(a_i,b_i)\). Directly from majority,

\[
 c_i(t+1)=\begin{cases}
 c_i(t),&a_i(t)=b_i(t),\\
 c_{i+1}(t),&a_i(t)\ne b_i(t).
 \end{cases}
\]

Indeed, with equal inputs \(a_i=b_i\), they outvote any eastern bit at both sites; with unequal inputs, the eastern bit is the deciding vote at each row. Call an equal-bit column a seed. Seeds never move or change. An unequal column follows the column immediately to its east; it remains unequal until it encounters the first seed to its east. If there is at least one seed, every column becomes equal and fixed within \(n-1\) updates. Moreover, the final bit \(y_i\) is exactly the bit of the first initial seed at \(i,i+1,\ldots\) in eastward cyclic order. Each initially unequal column at distance \(d\) from that seed becomes equal at time \(d\), establishing the exact relaxation time. If there are no seeds, every column is unequal forever and the entire column word translates one site west each update.

Now fix a desired output word \(y\). If \(y_i\ne y_{i+1}\), column \(i\) must initially be a seed with value \(y_i\), since otherwise the two eventual values must coincide. Conversely, if all these interface columns are initially seeds with their prescribed bits, then every other column may be either a seed carrying \(y_i\) (one option) or an unequal column (two options); the next seed to the east is necessarily inside the same constant run of \(y\), so every such choice converges to \(y\). When \(k(y)>0\), there are \(k(y)\) forced sites and hence exactly \(3^{n-k(y)}\) initial states. If \(k(y)=0\), any site may be a seed of the constant bit or one of two unequal columns, with the sole exclusion of having no seed anywhere. This gives \(3^n-2^n\).

Summing basins by introducing the two-by-two matrix

\[
 T=\begin{pmatrix}3&1\\1&3\end{pmatrix}
\]

shows \(\sum_y3^{n-k(y)}=\operatorname{tr}(T^n)=4^n+2^n\) because the eigenvalues are \(4\) and \(2\). Subtracting \(2^n\) for each of the two constant words gives \(4^n-2^n\). This agrees with the direct partition into seeded and seedless initial configurations.

For the conditional output distribution, divide the basin formula by \(4^n-2^n\). For spins \(s_i\in\{-1,+1\}\), define \(Z=\operatorname{diag}(-1,1)\). The correlation numerator before the two constant-word corrections is \(\operatorname{tr}(ZT^rZT^{n-r})\), which evaluates using the two eigenvalues of \(T\) to \(2^r4^{n-r}+4^r2^{n-r}\). In both constant outputs \(s_0s_r=1\); subtract their exceptional total weight \(2^{n+1}\) and divide by the normalizer, giving the displayed formula.

Finally, for any fixed finite set of sites, matrix powers in their cyclic weight sum are dominated by the simple Perron eigenvalue \(4\) of \(T\). The subleading eigenvalue \(2\) is exponentially smaller, as is the total exceptional correction \(2^{n+1}\) relative to \(4^n\). Normalized finite-window probabilities therefore converge to those of the stationary Markov chain with transition matrix \(T/4\). Since a nearest-neighbor zero-field Ising weight is proportional to \(\exp(J\sum_i s_is_{i+1})\), the ratio \(T_{aa}/T_{ab}=3\) implies \(e^{2J}=3\). Its correlation eigenvalue is \(1/2\), proving the limit and correlation length.

## Verification

The embedded `verify_exhaustive.py` computes synchronous majority directly from the two site rows, iterates each of the \(4^n\) initial states for every \(3\le n\le8\), and checks each of the \(2^n\) individual basin sizes against the theorem. It independently checks the exact absorbing/shifting partition and sharp maximum relaxation time. The embedded `verify_transfer.py` uses exact integer two-by-two matrix arithmetic to verify the partition sum and all two-point correlation numerators for \(3\le n\le21\); for \(n\le9\) it independently enumerates all output words and their weights. Both programs finished successfully; their complete outputs are embedded. These finite tests support, but do not replace, the all-circumference argument above.

## Relationship to prior work

The north-east-center deterministic majority rule and its general erosion properties are classical. Gács' *A Toom rule that increases the thickness of sets* (arXiv:math-ph/0102009v1, 8 February 2001) specifies the rule, discusses planar and square-torus erosion and compares an augmented rule, but does not give the two-row attraction-basin law or the exact limiting pushforward measure. Makowiec's *Critical properties of Toom cellular automata* (arXiv:cond-mat/9808247v1, 22 August 1998) investigates noisy two-dimensional Toom dynamics and tests Ising-style thermodynamic properties; it does not establish this noise-free, two-row, initial-data-to-absorbing-state measure. Other published work on anchored Toom interfaces and on Toom stationary states concerns different spatial domains and/or noise.

A previously indexed three-row Toom fixed-point enumeration studies stationary-state *population*, not initial-state basin sizes or this two-row limiting measure. The two-row basin theorem is not implied by that enumeration. The present theorem concerns an attraction-selected measure and does not assert that the two-dimensional noisy Toom invariant measures are Gibbsian.

## Limitations

The theorem is specific to exactly two vertically periodic rows and to deterministic north-east-center majority. It does not classify noisy stationary measures or widths three and above. The exceptional seedless trajectories never enter row-equal fixed points and are excluded from the conditional output law. The fixed-ring law is a finite-ring Ising weight with explicit corrections at the two constant words, not an uncorrected finite-ring Gibbs distribution. General literature cannot rule out unindexed historical anticipation; the 1997 full text *Ground-state configurations for Toom cellular automata: Experimental hints* could not be accessed, though its abstract and scope were examined. Independent external validation has not been performed.

## References

1. P. Gács, *A Toom rule that increases the thickness of sets*, arXiv:math-ph/0102009v1 (first arXiv posting 2001-02-08). https://arxiv.org/pdf/math-ph/0102009
2. D. Makowiec, *Critical properties of Toom cellular automata*, arXiv:cond-mat/9808247v1 (first arXiv posting 1998-08-22). https://arxiv.org/pdf/cond-mat/9808247
3. D. Makowiec, *Ground-state configurations for Toom cellular automata: Experimental hints*, Physical Review E 56 (1997), 5195-5203, DOI: 10.1103/PhysRevE.56.5195. Abstract verified; primary full text inaccessible during review.
4. B. Derrida, J. L. Lebowitz, E. R. Speer and H. Spohn, *Dynamics of an anchored Toom interface*, Journal of Physics A 24 (1991), 4805-4834, DOI: 10.1088/0305-4470/24/20/015.
