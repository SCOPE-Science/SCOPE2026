# Exact identifiability boundary for four expected order statistics
## Finding
Let \(\beta_1<\beta_2<\beta_3<\beta_4\), and define the consecutive gaps
\[
a=\beta_2-\beta_1,\qquad
b=\beta_3-\beta_2,\qquad
c=\beta_4-\beta_3.
\]
Okolewski and Papadatos proved that these four numbers can occur as the expected order statistics of an iid sample of size four if and only if
\[
9ac\ge 4b^2.
\]
Within this feasible region, the same quadratic boundary is exactly the boundary between identification and nonidentification of the parent distribution.

If
\[
9ac=4b^2,
\]
there is exactly one integrable nondegenerate parent law. It is a two-point distribution
\[
\Pr\{X=x\}=p,\qquad \Pr\{X=y\}=1-p,
\]
with
\[
p=\frac{\sqrt c}{\sqrt a+\sqrt c},
\]
\[
x=\beta_1-\frac{a^{3/2}}{4\sqrt c},
\qquad
y=\beta_4+\frac{c^{3/2}}{4\sqrt a}.
\]

If instead
\[
9ac>4b^2,
\]
there are uncountably many distinct integrable parent laws sharing these same four expected order statistics. More strongly, an explicit one-parameter family can be chosen entirely among three-point laws. Put
\[
S=3a+4b+3c,\qquad
m=\frac{3c+2b}{S},\qquad
v=\frac{9ac-4b^2}{S^2}.
\]
For every
\[
u\in\left(\frac{v}{1-m},m\right),
\]
set
\[
r=m-u,\qquad
s=m+\frac vu,\qquad
w=\frac{v}{u^2+v},
\]
and
\[
d_1=\frac{w}{r(1-r)},\qquad
d_2=\frac{1-w}{s(1-s)}.
\]
Define
\[
z_0=-(1-r)d_1-(1-s)d_2,\qquad
z_1=z_0+d_1,\qquad
z_2=z_1+d_2.
\]
Finally let
\[
\bar\beta=\frac{\beta_1+\beta_2+\beta_3+\beta_4}{4},
\qquad
\lambda=\frac{S}{12}.
\]
The distribution assigning masses
\[
r,\qquad s-r,\qquad 1-s
\]
to
\[
\bar\beta+\lambda z_0,\qquad
\bar\beta+\lambda z_1,\qquad
\bar\beta+\lambda z_2,
\]
respectively, has expected order statistics \(\beta_1,\beta_2,\beta_3,\beta_4\). As \(u\) varies over the displayed open interval, these laws are distinct.

Thus feasible four-term expected-order-statistic data identify their parent distribution if and only if they lie on
\[
9ac=4b^2.
\]
Every strict interior point is already nonidentified within the class of three-point distributions.

## Assumptions and scope
The parent distribution is any nondegenerate integrable real distribution, and the four observations whose order statistics are averaged are iid. The four expected order statistics are required to be strictly increasing. No continuity, density, bounded-support, or parametric assumption is imposed.

The result concerns identification from exactly four expected order statistics. It does not claim identification from fewer summaries, nor does it classify identification for five or more expected order statistics.

## Proof
Let
\[
S=3a+4b+3c.
\]
For a feasible four-term sequence, Theorem 1 of Okolewski and Papadatos provides a generator \(T\) supported in \((0,1)\). Specializing their binomial-moment identity to a sample of size four gives
\[
\mathbb E(1-T)^2=\frac{3a}{S},
\qquad
2\mathbb E[T(1-T)]=\frac{4b}{S},
\qquad
\mathbb ET^2=\frac{3c}{S}.
\]
Hence
\[
m:=\mathbb ET
=\frac{3c+2b}{S}
\]
and
\[
v:=\operatorname{Var}(T)
=\frac{3c}{S}-\left(\frac{3c+2b}{S}\right)^2
=\frac{9ac-4b^2}{S^2}.
\]

The source's feasibility condition \(9ac\ge4b^2\) is therefore exactly \(v\ge0\).

Suppose first that \(9ac=4b^2\). Then \(v=0\), so every admissible generator is the same degenerate variable \(T\equiv p\), where
\[
p=m=\frac{\sqrt c}{\sqrt a+\sqrt c}.
\]
The source proves that its generator-to-parent map is one-to-one after the canonical location-scale normalization, and it explicitly shows that a degenerate generator produces a two-point parent. Therefore the parent law is unique.

For a two-point parent with lower atom \(x\), upper atom \(y\), lower-atom probability \(p\), upper-atom probability \(q=1-p\), and spacing \(h=y-x\), the four-sample expected-order-statistic gaps are
\[
a=4hpq^3,\qquad
b=6hp^2q^2,\qquad
c=4hp^3q.
\]
Consequently
\[
p=\frac{\sqrt c}{\sqrt a+\sqrt c},
\qquad
q=\frac{\sqrt a}{\sqrt a+\sqrt c},
\qquad
h=\frac{(\sqrt a+\sqrt c)^4}{4\sqrt{ac}}.
\]
Also
\[
\beta_1=x+hq^4,\qquad
\beta_4=y-hp^4,
\]
which gives exactly
\[
x=\beta_1-\frac{a^{3/2}}{4\sqrt c},
\qquad
y=\beta_4+\frac{c^{3/2}}{4\sqrt a}.
\]

Now suppose \(9ac>4b^2\), so \(v>0\). Since
\[
m-\mathbb ET^2=\frac{2b}{S}>0,
\]
we have
\[
0<v<m(1-m).
\]
Therefore the interval
\[
\left(\frac{v}{1-m},m\right)
\]
is nonempty. For any \(u\) in this interval, define
\[
r=m-u,\qquad s=m+\frac vu,\qquad
w=\frac{v}{u^2+v}.
\]
The interval restrictions give \(0<r<s<1\), and direct calculation shows that the two-point random variable \(T_u\) satisfying
\[
\Pr\{T_u=r\}=w,\qquad
\Pr\{T_u=s\}=1-w
\]
has
\[
\mathbb ET_u=m,\qquad \operatorname{Var}(T_u)=v.
\]
Thus it has the same first two moments as every generator compatible with the given four expected order statistics, and hence it satisfies the source's four-term binomial-moment equations.

For completeness, the corresponding parent can be written explicitly. Set
\[
d_1=\frac{w}{r(1-r)},\qquad
d_2=\frac{1-w}{s(1-s)},
\]
and
\[
z_0=-(1-r)d_1-(1-s)d_2,\qquad
z_1=z_0+d_1,\qquad
z_2=z_1+d_2.
\]
Give \(z_0,z_1,z_2\) probabilities \(r,s-r,1-s\). Its mean is zero. Its distribution function equals \(r\) on the gap of length \(d_1\) and \(s\) on the gap of length \(d_2\), so
\[
\int F_Z(t)(1-F_Z(t))\,dt
=d_1r(1-r)+d_2s(1-s)=1.
\]
Under the source's generator construction, those two gaps therefore produce \(T_u=r\) with mass \(w\) and \(T_u=s\) with mass \(1-w\).

The canonical scale for the original four expected order statistics is
\[
\lambda=\frac{3a+4b+3c}{12}=\frac{S}{12},
\]
and their common mean is
\[
\bar\beta=\frac{\beta_1+\beta_2+\beta_3+\beta_4}{4}.
\]
Hence the affine image \(\bar\beta+\lambda Z\) has exactly the required four expected order statistics.

Different values of \(u\) give different two-point generator laws. Because the source's generator-to-normalized-parent map is one-to-one, the associated parent laws are distinct. Since the admissible \(u\)-interval is open and nonempty, this yields uncountably many distinct three-point parents.

## Verification
The proof is analytic and establishes all quantifiers above. The standalone script `verify_four_eos_identifiability.py` performs two independent regression checks.

First, it generates twenty-seven rational two-point parents, computes their four expected order statistics exactly, verifies the boundary identity \(9ac=4b^2\), and checks that the displayed reconstruction recovers the original atom probability and support.

Second, for five strict-interior gap triples and four different values of the free parameter \(u\) in each case, it verifies the generator moments, constructs the associated three-point parent, computes its four order-statistic expectations directly from the discrete order-statistic distribution, and recovers the prescribed sequence. The successful output is:
`VERIFY_OK boundary_cases=27 strict_generators=20`.

These finite checks are supplementary. They do not replace the proof of the continuum statement.

## Relationship to prior work
Okolewski and Papadatos give the exact feasibility inequality for four expected order statistics. They also prove the general one-to-one correspondence between normalized parent laws and generator distributions, note that finitely many generator moments need not determine a generator, and state the general truncated-moment determinacy criterion. In their four-term example they identify one boundary sequence, \((0,2,5,7)\), whose generator is degenerate and whose parent is uniquely two-valued.

The present result combines and sharpens those ingredients specifically at the first nontrivial sample size. It classifies every feasible four-term sequence by identifiability, proves that the entire quadratic boundary and only that boundary gives a unique parent, gives the unique parent in closed form, and gives an explicit continuum of three-point parents at every strict interior point.

Older work of Mallows addresses sharp distribution-function bounds from expected order statistics, and Kadane relates order-statistic expectation arrays to moment problems. The inspected accessible descriptions do not state this four-term identification/nonidentification dichotomy or the explicit three-point family.

Targeted searches for four expected order statistics, uniqueness of the parent law, equality in the quadratic feasibility condition, and three-point parents with the same four expectations found no covering statement.

## Limitations
The source already contains the key generator correspondence and the general moment-determinacy machinery, so the new contribution is a complete specialization and explicit structural classification at the four-term level, not a new general moment theorem.

An equivalent four-term identification statement may exist in older order-statistics or truncated-moment literature under terminology not retrieved by the searches. Mallows's 1973 paper was identified as relevant background through the source and bibliographic search, but its complete text was not materially inspected here; this is the main residual originality risk.

The result does not describe all parents at a strict interior point. It proves nonidentification by an explicit uncountable three-point subfamily.

## References
A. Okolewski and N. Papadatos, *Finite Sequences Representing Expected Order Statistics*, arXiv:2204.13949v1, first public version 2022-04-29; Sankhya A 86 (2024), 755--774, DOI:10.1007/s13171-024-00343-z.

C. L. Mallows, *Bounds on distribution functions in terms of expectations of order-statistics*, Annals of Probability 1 (1973), 297--303, DOI:10.1214/AOP/1176996981.

J. B. Kadane, *A characterization of triangular arrays which are expectations of order statistics*, Journal of Applied Probability 11 (1974), 413--416, DOI:10.2307/3212766.
