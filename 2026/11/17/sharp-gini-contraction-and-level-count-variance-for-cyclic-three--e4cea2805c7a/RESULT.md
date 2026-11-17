# Sharp Gini contraction and level-count variance for cyclic three-point averaging

## Finding

For each integer \(n\ge3\), let \(P_n\) be the uniform nearest-neighbor-plus-self average on the real cyclic vector space \(\mathbb R^{\mathbb Z/n\mathbb Z}\):
\[
(P_nf)_i=\frac{f_{i-1}+f_i+f_{i+1}}3.
\]
Define the unnormalized complete-pair Gini seminorm
\[
G_n(f)=\sum_{0\le i<j<n}|f_i-f_j|.
\]
The sharp induced quotient seminorm \(\gamma_n=\sup_{G_n(f)>0}G_n(P_nf)/G_n(f)\) is
\[
\boxed{\gamma_3=0,\qquad \gamma_n=1-\frac{8}{3\lfloor n^2/4\rfloor}\quad(n\ge4).}
\]
The supremum is attained: when \(n\ge5\), indicators of any contiguous cyclic arc containing \(\lfloor n/2\rfloor\) or \(\lceil n/2\rceil\) sites are sharp witnesses. At \(n=4\), every nonconstant input attains \(\gamma_4=1/3\). For all \(n\ge6\), the Dobrushin oscillation coefficient of \(P_n\) is \(1\), although \(\gamma_n<1\). In particular, \(1-\gamma_n\sim 32/(3n^2)\).

An exact cut-deficit identity is part of the proof. For a nonempty proper \(S\subset\mathbb Z/n\mathbb Z\), write \(k=|S|\) and let \(d,b,e\) count cyclic centers whose three-site windows contain, respectively, at least one, at least two, and all three sites of \(S\). Then
\[
\boxed{k(n-k)-G_n(P_n\mathbf1_S)=\frac{(d-k)^2+(b-k)^2+(e-k)^2}{3}.}
\]
This displays the sharp difference between a singleton cut (deficit \(2\)) and a cut with at least two sites on each side (deficit at least \(8/3\)).

## Assumptions and scope

All arithmetic indices are taken modulo \(n\). The three sites \(i-1,i,i+1\) are distinct because \(n\ge3\). Inputs are arbitrary real vectors, not necessarily nonnegative. No normalization factor is placed in \(G_n\); its kernel is exactly the constant vectors. The matrix of \(P_n\) is nonnegative, row-stochastic and column-stochastic. Its operator quotient seminorm is measured on nonconstant vectors modulo constants and concerns one simultaneous averaging step only.

## Proof

**1. Reduction to binary cuts.** For a real input \(f\), write \(a=\min_i f_i\), \(b=\max_i f_i\), and \(S_t=\{i:f_i>t\}\). The layer-cake formula gives \(f=a\mathbf1+\int_a^b\mathbf1_{S_t}\,dt\). Because \(P_n\mathbf1=\mathbf1\), the triangle inequality applied pairwise yields
\[
G_n(P_nf)\le\int_a^b G_n(P_n\mathbf1_{S_t})\,dt,
\qquad G_n(f)=\int_a^b |S_t|(n-|S_t|)\,dt.
\]
Thus the exact operator coefficient is the maximum of \(G_n(P_n\mathbf1_S)/(|S|(n-|S|))\) over nonempty proper binary cuts. Every cut itself is an admissible real input, so there is no relaxation in this reduction.

**2. A general mass-preserving level-count identity.** Let \(y\in[0,1]^n\) and assume \(\sum_i y_i=k\), where \(k\) is an integer. Put \(m(t)=|\{i:y_i>t\}|\) for \(0<t<1\). Pairwise layer cake gives
\[
G_n(y)=\int_0^1m(t)(n-m(t))\,dt,
\qquad\int_0^1m(t)\,dt=k.
\]
Consequently
\[
k(n-k)-G_n(y)=\int_0^1(m(t)-k)^2\,dt.\tag{1}
\]
For \(y=P_n\mathbf1_S\), bistochasticity gives \(\sum_i y_i=k\), while every \(y_i\) belongs to \(\{0,1/3,2/3,1\}\). Thus \(m(t)\) equals \(d,b,e\) on the three consecutive subintervals of length \(1/3\), proving the announced exact deficit identity. Identity (1) applies more generally to the image of any binary input under any doubly stochastic matrix, but the explicit three-level count is special to this operator.

**3. The geometric deficit lower bound.** Suppose \(2\le k\le n-2\). The cyclic complement of \(S\) contains at least two sites. Every nonempty contiguous run of the complement of length at least two contributes two distinct complement sites adjacent to \(S\); if all complement runs have length one, at least two distinct sites are adjacent to \(S\). Therefore at least two sites outside \(S\) have a window intersecting \(S\), so \(d\ge k+2\). Applying the same argument to \(S\), at least two sites of \(S\) have a neighboring site outside \(S\), so \(e\le k-2\). The deficit identity now yields
\[
k(n-k)-G_n(P_n\mathbf1_S)\ge\frac{2^2+(-2)^2}{3}=\frac83.\tag{2}
\]
For a single contiguous cyclic arc with both its length and its complement length at least two, direct inspection of its two endpoints gives \(d=k+2\), \(b=k\), \(e=k-2\). Such an arc attains equality in (2). In the range \(n\ge5\), equality in (2) forces a single cyclic run: it requires \(d-k=k-e=2\), while \(k-e\) equals the sum, over occupied runs, of the number of occupied sites within one step of a vacant site. Two occupied singleton runs can make \(k-e=2\) but, with \(n\ge5\), their two separating gaps cannot both have length one and therefore \(d-k\ge3\). All other multiple-run configurations give \(k-e>2\). Thus the balanced arcs below are also the only norming binary cut shapes when \(n\ge5\), up to complement and rotation.

**4. Singleton cuts.** If \(k=1\), its image has three entries equal to \(1/3\) and the other \(n-3\) entries zero. Hence \(G_n(P_n\mathbf1_S)=n-3\), while \(G_n(\mathbf1_S)=n-1\), giving the exact deficit \(2\). For \(k=n-1\) the same result follows from \(P_n\mathbf1=\mathbf1\) and complement symmetry. When \(n=3\), all rows of \(P_3\) coincide and its image consists of constants; hence \(\gamma_3=0\).

**5. Sharp combination.** Set \(F_n=\lfloor n^2/4\rfloor\). For \(n\ge4\), every cut with \(2\le k\le n-2\) satisfies, by (2),
\[
\frac{G_n(P_n\mathbf1_S)}{G_n(\mathbf1_S)}\le1-\frac{8}{3k(n-k)}\le1-\frac{8}{3F_n}.
\]
The singleton/complement ratio equals \(1-2/(n-1)\), which is no larger because \(F_n\ge4(n-1)/3\), with equality only at \(n=4\). Choosing a cyclic arc with \(k\in\{\lfloor n/2\rfloor,\lceil n/2\rceil\}\) attains \(k(n-k)=F_n\) and equality in (2). Hence the formula holds in all dimensions \(n\ge4\). When \(n=4\), writing \(T\) for the cyclic shift yields \(P_4=(J-T^2)/3\), with \(Jf=(\sum_j f_j)\mathbf1\). Since a permutation and addition of a constant preserve \(G_4\), we have \(G_4(P_4f)=G_4(f)/3\) for every real \(f\). For \(n\ge5\), a norming binary cut must have \(k(n-k)=F_n\) and equality in (2), giving precisely balanced contiguous arcs.

**6. Comparison with the oscillation coefficient.** Let \(D(f)=\max_i f_i-\min_i f_i\). Any row-stochastic matrix has \(D(Pf)\le D(f)\). For \(n\ge6\), the supports of the rows centered at cyclic sites \(0\) and \(3\) are disjoint. Assigning input zero on the first support and one on the second gives \(D(P_nf)=D(f)=1\), proving the exact Dobrushin coefficient is \(1\). The Gini coefficient above is strictly less than one for every finite \(n\ge4\). Finally, \(F_n=n^2/4+O(1)\), so \(1-\gamma_n\sim32/(3n^2)\).

## Verification

The standalone Python 3 script `check_three_tap.py` uses exact integers and no third-party libraries. It exhaustively tests the binary cut identity and claimed optimal inequality for all \(3\le n\le16\), including equality geometry for \(5\le n\le16\). It additionally checks \(7650\) deterministic nonbinary integer vectors, the four-site identity and disjoint-row witnesses. Execute `python3 check_three_tap.py` after extracting the file from the same package. The all-dimension assertions rest on the proof, not on extrapolation from finite enumerations.

## Relationship to prior work

Yitzhaki (2003), especially Section 2, develops Gini mean difference as a dispersion functional and gives its pairwise and sorted-gap representations. Those identities motivate the chosen seminorm but do not provide an operator norm for a cyclic averaging filter. Gaubert and Qu (2013, 2014) establish sharp contraction results for Markov operators in Hopf oscillation and the dual total-variation norm on measures. Their Dobrushin coefficient for this three-point filter equals one from six sites onward and does not imply the strictly contracting Gini norm here. The present proof depends on a different level-set cardinality variance and identifies its sharp cyclic boundary geometry.

An exact calculation for a directed two-tap cyclic filter is not a covering statement: the symmetric three-point Fourier multiplier has the three-term polynomial \((1+z+z^2)/3\), which does not factor into two real nonnegative linear-tap filters, and the two-tap sharp deficit does not determine the three-level variance bound (2). Literature and mathematical-record searches did not identify a previously stated equivalent all-dimensional three-point result; this is a best-knowledge comparison rather than a proof of historical uniqueness.

## Limitations

The result applies to uniform simultaneous three-point averaging with periodic boundary conditions, counting-measure pair weights and real signals. It does not supply the exact norm for arbitrary nonuniform tap weights, repeated steps, weighted pairwise dispersion, or nonperiodic boundaries. The universal identity (1) is elementary and is not claimed as a new theorem by itself. Possible unindexed historical evaluations of this specific three-point operator remain a priority risk. Independent external validation has not been performed.

## References

1. Shlomo Yitzhaki, *Gini's Mean Difference: A Superior Measure of Variability for Non-Normal Distributions*, METRON 61(2) (2003), 285–316, https://www.dss.uniroma1.it/RePec/mtn/articoli/2003-2-8.pdf .
2. Stéphane Gaubert and Zheng Qu, *Dobrushin ergodicity coefficient for Markov operators on cones, and beyond*, arXiv:1302.5226 (first submitted 2013-02-21), https://arxiv.org/abs/1302.5226 .
3. Stéphane Gaubert and Zheng Qu, *Dobrushin's ergodicity coefficient for Markov operators on cones*, arXiv:1307.4649 (first submitted 2013-07-17), https://arxiv.org/abs/1307.4649 .
