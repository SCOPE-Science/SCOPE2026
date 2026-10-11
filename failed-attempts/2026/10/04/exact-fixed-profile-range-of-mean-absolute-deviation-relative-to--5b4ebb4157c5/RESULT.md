# Exact fixed-profile range of mean absolute deviation relative to standard deviation

## Finding

Fix positive category masses
\[
p_1,\ldots,p_m,
\qquad
\sum_{i=1}^m p_i=1,
\]
and cumulative masses
\[
P_j=\sum_{i=1}^j p_i.
\]
Let \(X\) range over all random variables with distinct ordered atoms
\[
x_1<\cdots<x_m,
\qquad
\Pr(X=x_i)=p_i.
\]
Write
\[
\mu=\mathbb EX,
\qquad
D=\mathbb E|X-\mu|,
\qquad
\sigma^2=\operatorname{Var}(X).
\]

Define
\[
\boxed{
L(\mathbf p)
=
2\sqrt{\frac{p_1p_m}{p_1+p_m}}
}
\tag{1}
\]
and
\[
\boxed{
U(\mathbf p)
=
2\max_{1\le j<m}
\sqrt{P_j(1-P_j)}.
}
\tag{2}
\]

For \(m=2\),
\[
\boxed{
\frac{D}{\sigma}
=
2\sqrt{p_1p_2}.
}
\tag{3}
\]

For \(m=3\), the exact attainable set is
\[
\boxed{
\frac{D}{\sigma}\in[L(\mathbf p),U(\mathbf p)).
}
\tag{4}
\]
The lower endpoint is attained exactly when the middle atom is the mean:
\[
x_2=\mu.
\]
Equivalently,
\[
\boxed{
\frac{x_2-x_1}{x_3-x_1}
=
\frac{p_3}{p_1+p_3}.
}
\tag{5}
\]

For every
\[
m\ge4,
\]
the exact attainable set is
\[
\boxed{
\frac{D}{\sigma}\in(L(\mathbf p),U(\mathbf p)).
}
\tag{6}
\]

The lower endpoint is approached by collapsing all interior atoms toward the mean. The upper endpoint is approached by collapsing the support to two levels across any cut \(j\) maximizing
\[
P_j(1-P_j).
\]
Every interior value is attained.

For equal masses
\[
p_i=\frac1m,
\]
the endpoints simplify to
\[
\boxed{
L=\sqrt{\frac2m}
}
\tag{7}
\]
and
\[
\boxed{
U=
\begin{cases}
1,&m\text{ even},\\[1mm]
\sqrt{1-\frac1{m^2}},&m\text{ odd}.
\end{cases}
}
\tag{8}
\]

Thus a prescribed finite frequency profile gives both a positive floor and, unless a cumulative mass can approach one half, a sharpened ceiling for the classical comparison
\[
D\le\sigma.
\]

## Assumptions and scope

The support is finite, every listed mass is positive, and all atoms are distinct.

The probability profile is fixed; only the ordered support locations vary.

The quantity \(D\) is the mean absolute deviation about the arithmetic mean, not the mean absolute deviation about a median and not the pairwise Gini mean difference.

The ratio \(D/\sigma\) is invariant under nonzero affine rescaling, so only support shape matters.

## Proof

Center the variable:
\[
Z=X-\mu.
\]
Because
\[
\mathbb EZ=0,
\]
the positive and negative first moments balance:
\[
\mathbb E Z_+
=
\mathbb E(-Z)_+
=
\frac D2.
\]
Put
\[
S=\frac D2.
\]

For the negative side, every negative deviation has magnitude at most
\[
\mu-x_1.
\]
Hence
\[
\sum_{x_i<\mu}p_i(x_i-\mu)^2
\le
(\mu-x_1)
\sum_{x_i<\mu}p_i(\mu-x_i)
=
(\mu-x_1)S.
\tag{9}
\]
Since the endpoint \(x_1\) contributes to the negative first moment,
\[
S
\ge
p_1(\mu-x_1),
\]
and therefore
\[
\sum_{x_i<\mu}p_i(x_i-\mu)^2
\le
\frac{S^2}{p_1}.
\tag{10}
\]

The same argument at the upper endpoint gives
\[
\sum_{x_i>\mu}p_i(x_i-\mu)^2
\le
\frac{S^2}{p_m}.
\tag{11}
\]
An atom equal to the mean contributes zero. Summing (10)--(11),
\[
\sigma^2
\le
S^2
\left(
\frac1{p_1}+\frac1{p_m}
\right).
\]
Since
\[
D=2S,
\]
this is exactly
\[
\frac D\sigma
\ge
2\sqrt{\frac{p_1p_m}{p_1+p_m}}
=
L(\mathbf p).
\tag{12}
\]

The equality conditions in (10) and (11) are rigid. Equality requires every non-endpoint atom below the mean to have zero deviation and every non-endpoint atom above the mean to have zero deviation. Thus all interior atoms must equal the mean.

For two atoms this is vacuous and equality holds. For three atoms it means exactly
\[
x_2=\mu,
\]
which after normalizing \(x_1=0\), \(x_3=1\) gives
\[
x_2=p_2x_2+p_3,
\]
hence (5). For at least four distinct atoms, equality is impossible.

The lower constant remains sharp for every \(m\). Normalize the limiting endpoint configuration to
\[
x_m=1,
\qquad
x_1=-\frac{p_m}{p_1},
\]
with all interior atoms at zero. This limiting law has mean zero and attains (12). Replace the coincident interior points by distinct points of order \(O(\varepsilon)\), and adjust \(x_1\) by \(O(\varepsilon)\) so that the mean remains zero. The resulting strict supports converge to the limiting configuration, proving sharpness of the lower infimum.

For the upper bound, choose the unique cut \(k\) such that
\[
x_k\le\mu<x_{k+1}.
\]
Let
\[
H=\mathbf 1_{\{X>\mu\}}.
\]
Then
\[
\Pr(H=0)=P_k,
\qquad
\Pr(H=1)=1-P_k.
\]
Because the centered positive and negative first moments are equal,
\[
\operatorname{Cov}(X,H)
=
\mathbb E[(X-\mu)H]
=
\frac D2.
\tag{13}
\]
Cauchy--Schwarz gives
\[
\frac D2
\le
\sigma
\sqrt{P_k(1-P_k)},
\]
so
\[
\frac D\sigma
\le
2\sqrt{P_k(1-P_k)}
\le
U(\mathbf p).
\tag{14}
\]

Equality in the first inequality of (14) requires \(X-\mu\) to be a scalar multiple of the centered Bernoulli variable
\[
H-\mathbb EH.
\]
Therefore \(X\) must take only two values. Hence equality occurs only when \(m=2\); for every \(m\ge3\) the upper inequality is strict.

To prove sharpness of the upper endpoint, choose a cut \(j_*\) maximizing
\[
P_j(1-P_j).
\]
Cluster the first \(j_*\) support points around one level and the remaining support points around a second level, preserving strict order. In the limit the distribution becomes a two-point law with masses
\[
P_{j_*},
\qquad
1-P_{j_*},
\]
whose mean-absolute-deviation/standard-deviation ratio is
\[
2\sqrt{P_{j_*}(1-P_{j_*})}
=
U(\mathbf p).
\]

Finally, after fixing \(x_1=0\) and \(x_m=1\), the set
\[
0<x_2<\cdots<x_{m-1}<1
\]
is connected, and \(D/\sigma\) is continuous on it. Its image is therefore an interval. The endpoint analysis above gives exactly (3), (4), and (6).

For equal masses,
\[
L^2
=
\frac{4/m^2}{2/m}
=
\frac2m.
\]
Also
\[
U^2
=
4\max_{1\le j<m}
\frac jm
\left(1-\frac jm\right),
\]
which equals \(1\) for even \(m\) and \(1-1/m^2\) for odd \(m\).

## Verification

The accompanying exact-rational checker evaluates the mean absolute deviation and variance for random rational profiles and random strict rational supports.

It verifies the squared lower and upper inequalities
\[
\frac{D^2}{\sigma^2}
\ge
\frac{4p_1p_m}{p_1+p_m}
\]
and
\[
\frac{D^2}{\sigma^2}
\le
4\max_jP_j(1-P_j)
\]
without floating-point arithmetic.

It separately checks exact two-point equality, exact three-point lower equality at \(x_2=\mu\), strict inequalities for larger strict supports, and rational support families approaching both sharp endpoints.

Finite replay is supplementary. The universal statement follows from the endpoint second-moment bounds, the covariance identity (13), Cauchy--Schwarz, and connectedness.

## Relationship to prior work

Mean absolute deviation about the mean is a classical dispersion measure. Goroncy's work on positive \(L\)-statistics treats sharp bounds expressed in units generated by central absolute moments and singles out mean absolute deviation as exceptional among such scale units. That work optimizes expectations of \(L\)-statistics over broad parent-distribution classes rather than comparing mean absolute deviation directly with standard deviation after fixing a finite atom-probability profile.

El Amir emphasizes the covariance representation of mean absolute deviation about the mean and uses it to construct association and skewness measures. The covariance identity is closely related to (13), but the published abstract and accessible bibliographic material do not state a prescribed-frequency range for \(D/\sigma\).

Choulakian and Abou Samra's full arXiv article compares mean absolute deviation with standard deviation, states the classical inequality
\[
D\le\sigma,
\]
and develops a cut-norm representation of the centered absolute-deviation functional. It does not impose fixed category frequencies or derive the profile-specific lower floor and cumulative-cut upper ceiling above.

Berend and Kontorovich derive sharp nonasymptotic estimates for the mean absolute deviation of a binomial law and explicitly compare its behavior with the standard deviation. Their problem fixes the binomial family rather than allowing support locations to vary at a prescribed finite probability profile.

Targeted semantic and exact-formula searches for fixed probabilities, endpoint masses, cumulative cuts, and the ratio of mean absolute deviation to standard deviation did not locate formulas (1)--(2) or the complete attainment classification.

## Limitations

The probability profile is fixed and every atom has positive mass. If endpoint masses are allowed to tend to zero, the lower floor can tend to zero.

The result concerns mean absolute deviation about the mean. Median-based absolute deviation and pairwise Gini dispersion have different extremal geometry.

The originality search was targeted. Older finite-population, moment-inequality, or isotonic-cone literature may contain an equivalent profile-specific norm comparison under different notation.

The full text of the 2009 Goroncy paper and the 2012 El Amir paper was not available through the open routes inspected here, so neither was used as a whole-document noncoverage certificate.

## References

1. A. Goroncy, “Lower Bounds on Positive L-Statistics,” *Communications in Statistics—Theory and Methods* 38 (2009), 1989–2002, DOI 10.1080/03610920802393087.
2. E. A. H. El Amir, “On uses of mean absolute deviation: decomposition, skewness and correlation coefficients,” *METRON* 70 (2012), 145–164, DOI 10.1007/BF03321972.
3. D. Berend and A. Kontorovich, “A sharp estimate of the binomial mean absolute deviation with applications,” *Statistics & Probability Letters* 83 (2013), 1254–1259, DOI 10.1016/j.spl.2013.01.023.
4. V. Choulakian and G. Abou-Samra, “Mean absolute deviations about the mean, the cut norm and taxicab correspondence analysis,” arXiv:2003.02906, first submitted 2020-03-05.
