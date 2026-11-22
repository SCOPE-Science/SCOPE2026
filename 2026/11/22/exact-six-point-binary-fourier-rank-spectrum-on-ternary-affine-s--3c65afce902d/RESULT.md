# Exact six-point binary Fourier-rank spectrum on ternary affine spaces

## Finding

Let \(d\ge 2\), \(V=\mathbb F_3^d\), and let \(S\subset V\) have exactly six distinct points. Write \(T_S f=\mathbf 1_S*f\) for **unnormalized** convolution acting on \(\mathbb C^V\), and \(R(S)=\operatorname{rank}_{\mathbb C}T_S\). The complete set of possible normalized ranks, across all six-point subsets, is

\[
\frac{R(S)}{3^d}\in
\left\{\frac13,\frac59,\frac{17}{27},\frac79,
\frac{23}{27},\frac{71}{81},\frac{25}{27},1\right\}.
\]

At dimensions \(d=2,3,4,\ge5\), respectively, exactly \(2,6,7,8\) of these values occur. The sharp lower bound is \(R(S)\ge 3^{d-1}\); equality holds **if and only if** \(S\) is the complement of one affine line inside an affine plane (equivalently, the union of two distinct parallel lines in that plane).

There is also an exact cardinality formula for every rank stratum in every dimension. Define the Gaussian binomial coefficient \({d\brack r}_3=\prod_{i=0}^{r-1}(3^{d-i}-1)/(3^{r-i}-1)\) and the number of affine \(r\)-flats \(H_r(d)=3^{d-r}{d\brack r}_3\), interpreted as zero for \(r>d\). Set \(K_4=2{,}729{,}376\) and \(K_5=160{,}503{,}685{,}056\). The following formula counts *unordered* six-point subsets at each normalized rank:

| \(R(S)/3^d\) | Number of six-point subsets |
|---|---:|
| \(1/3\) | \(12H_2\) |
| \(5/9\) | \(10530H_3\) |
| \(17/27\) | \(K_4H_4\) |
| \(7/9\) | \(72H_2+75816H_3\) |
| \(23/27\) | \(113724H_3+75K_4H_4\) |
| \(71/81\) | \(K_5H_5\) |
| \(25/27\) | \(75816H_3+30K_4H_4\) |
| \(1\) | \(16848H_3\) |

Each \(H_r\) in this table is evaluated at \(d\). The eight counts sum exactly to \(\binom{3^d}{6}\). For \(d=3\), the ranks \(9,15,21,23,25,27\) occur with respective multiplicities \(468,10530,78624,113724,75816,16848\), totaling \(296010\).

## Assumptions and scope

All arithmetic in \(V\) is over the field of three elements, while the convolution rank is over the complex numbers. Support points are distinct, each has coefficient exactly one, and no arbitrary-weight assertion is made. Frequencies are all additive characters of \(V\), and neither the Fourier transform nor convolution is divided by \(|V|\). The result includes every \(d\ge2\), not only the directly enumerated three-dimensional instance.

## Proof

**(1) Fourier-zero criterion and affine reduction.** With \(\zeta=e^{2\pi i/3}\), the character at \(a\in V\) evaluates the mask as \(\widehat{\mathbf1_S}(a)=\sum_{s\in S}\zeta^{-a\cdot s}\). Writing \(n_j\) for the number of sites giving phase \(j\), the only rational relation among \(1,\zeta,\zeta^2\) is \(1+\zeta+\zeta^2=0\), hence this Fourier coefficient vanishes exactly when \(n_0=n_1=n_2=2\). Since Fourier diagonalizes \(T_S\), its rank equals the number of nonzero characters. Let the affine dimension of \(S\) be \(r\); necessarily \(2\le r\le\min(5,d)\). Every frequency on its affine span has exactly \(3^{d-r}\) extensions, and the translation phase does not change vanishing. Consequently \(R(S)=3^{d-r}R_r(S)\), with \(R_r\) the rank calculated in the intrinsic affine span.

**(2) Two-dimensional spans.** A six-point set in \(\mathbb F_3^2\) is the complement of a three-point set. The complement of a line has Fourier rank \(3\); the complement of a noncollinear triple has rank \(7\). There are respectively \(12\) lines and \(\binom93-12=72\) noncollinear triples per plane.

**(3) Three-dimensional spans.** Enumerate the \(\binom{27}{6}=296010\) subsets, taking point index \(i=9x+3y+z\) for \((x,y,z)\in\mathbb F_3^3\). Translation in each coordinate, swapping adjacent coordinates, one elementary shear, and scaling a coordinate by \(2\) generate the full affine group. The complete ten-orbit certificate is in `orbit_certificate.json`; `check_orbits.py` rederives the orbit partition from the group generators with integer arithmetic, and `check_direct.py` independently enumerates all subsets and checks all \(26\) nontrivial characters. The two plane-contained orbits have sizes \(468,2808\) and ranks \(9,21\); they are excluded when assigning subsets to intrinsic dimension three. The five intrinsic dimension-three rank strata, with counts, are

\[
R_3: \qquad 15:10530,\quad21:75816,\quad23:113724,
\quad25:75816,\quad27:16848.
\]

The ten orbit sizes add to \(296010\), and their ranks are computed from exact \((2,2,2)\) plane-section counts. Every subset is reached, not sampled.

**(4) Four-dimensional spans.** Label the six points \(s_0,\ldots,s_5\). Their affine-coordinate vectors possess a unique projective affine relation \(\alpha=(\alpha_0,\ldots,\alpha_5)\in\mathbb F_3^6/\mathbb F_3^\times\) with \(\sum\alpha_i=0\); its support has size at least three because the points are distinct. Conversely, every such relation arises for ordered distinct six-tuples spanning dimension four. With the phase at \(s_0\) normalized to zero, the phase words are exactly \((u_0,\ldots,u_5)\in\mathbb F_3^6\) satisfying \(u_0=0\) and \(\sum\alpha_i u_i=0\). Among the thirty words containing two copies of each field element and \(u_0=0\), the numbers satisfying the relation are:

| Relation type (up to permutation and common nonzero scalar) | Number of projective relations | Fourier zeros out of \(81\) |
|---|---:|---:|
| Three equal nonzero entries | 20 | 12 |
| Four entries, two \(1\)'s and two \(2\)'s | 45 | 12 |
| Five entries, one of one sign and four of the other | 30 | 6 |
| Six equal nonzero entries | 1 | 30 |
| Six entries, three of each sign | 10 | 12 |

Thus the only local ranks are \(51,69,75\), respectively occurring for \(1,75,30\) projective relation classes. For each fixed projective relation on the six **labelled** positions, the number of ordered spanning six-tuples is \(3^4|\mathrm{GL}_4(3)|\), since one chooses \(s_0\) and then an isomorphism of a four-dimensional quotient. Summing over the projective relation vectors of each permutation-invariant type and dividing the resulting total by \(6!=720\) yields that type's unordered count as its relation-vector count times \(K_4=3^4|\mathrm{GL}_4(3)|/720=2{,}729{,}376\). The exact relation and zero-word counts are independently verified by `check_relations.py`.

**(5) Five-dimensional spans.** Every spanning six-point set is affinely independent. Relative to one point, its remaining five differences form a basis; therefore every one of the \(3^5\) phase words occurs and exactly \(30\) are balanced. The local rank is \(3^5-30=213\). The number of such unordered sets per five-flat is \(K_5=3^5|\mathrm{GL}_5(3)|/720=160{,}503{,}685{,}056\).

**(6) Global counts and sharpness.** Each subset has one unique intrinsic affine span. Multiplying each local count by \(H_r(d)\), and combining equal rank fractions across dimensions, yields the eight formulas. The minimum local proportion is \(1/3\), occurring only for the plane-minus-line case; this proves the rigidity assertion. Every listed rank has an explicit realization from one of the ten affine orbit representatives or one of the relation types in the four- and five-dimensional constructions. These embed into every larger dimension, giving the claimed dimension thresholds.

## Verification

The package contains three Python 3 programs using only the standard library and an embedded orbit certificate. From the directory containing these files, execute:

```sh
python3 check_orbits.py
python3 check_direct.py
python3 check_relations.py
```

`check_orbits.py` performs exact generated-affine-orbit partitioning of all \(296010\) six-sets; `check_direct.py` independently enumerates them against all \(26\) nonzero frequency vectors; `check_relations.py` enumerates all \(106\) projective dimension-four relations, checks their balanced-word counts, and checks the formula against \(\binom{3^d}{6}\) for dimensions \(2\) through \(8\). These finite checks support the enumerative steps. The extrapolation to all \(d\) follows from the affine-span and relation arguments, rather than extrapolation from experiments.

## Relationship to prior work

Meshulam's 2003 uncertainty inequality gives a general lower bound on Fourier-support size for arbitrary functions on finite abelian groups, but not the rank-by-cardinality census for six-point **indicators** or its extremizer classification. In fact, for six points in a ternary vector space its bound is \((2/9)3^d\), weaker than the sharp \((1/3)3^d\) established here.

Kiss and Somlai's work on special directions in finite affine planes includes a structural classification of the planar equidistribution cases; the two-dimensional part of the present analysis is compatible with and not asserted to supersede that work. The new dimension-three affine-orbit census, dimension-four affine-circuit law, five-dimensional simplex rank, and all-dimensional combined multiplicity formula concern objects not classified by that planar theorem. Other existing finite Fourier-support results treat four-point supports or binary (rather than ternary) underlying groups and do not imply these six-point formulas.

## Limitations

The coefficient alphabet is fixed to unit indicator weights; arbitrary complex weights can yield different Fourier zeros. No singular-value magnitudes or condition-number claims are made. The dimension-three orbit calculation is a rigorously specified exhaustive finite proof, not an independent symbolic closed-form orbit derivation. Historical priority cannot be guaranteed against an unindexed or inaccessible published table. Independent external mathematical validation is not claimed.

## References

1. R. Meshulam, *An Uncertainty Inequality for Finite Abelian Groups*, arXiv:math/0312407v1, first public posting 2003-12-22, https://arxiv.org/abs/math/0312407 .
2. G. Kiss and G. Somlai, *Special directions on the finite affine plane*, arXiv:2109.13992, first posted 2021, https://arxiv.org/abs/2109.13992 .
3. D. L. Donoho and P. B. Stark, *Uncertainty principles and signal recovery*, SIAM Journal on Applied Mathematics 49 (1989), 906–931. DOI: 10.1137/0149053 .
