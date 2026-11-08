# Exact finite-grid orthant-shattering profiles and an alphabet-dependent coupon threshold

## Finding

For integers \(d\geq1\) and \(n_1,\ldots,n_d\geq1\), write
\[
G=\prod_{i=1}^{d}\{1,\ldots,n_i\},\qquad
\mathcal H=\bigl\{\{x\in G:x_i\leq t_i\text{ for every }i\}:0\leq t_i\leq n_i\bigr\}.
\]
This is the range space of anchored coordinatewise lower orthants, or principal downsets of the product order, together with the empty set. A support \(S\subseteq G\) is *shattered* when all \(2^{|S|}\) intersections of concepts with \(S\) occur. Let \(s_m\) denote the number of shattered \(m\)-element supports, including \(s_0=1\).

**Exact classification and polynomial.** A nonempty \(S\) is shattered if and only if every \(x\in S\) has a coordinate \(i\) satisfying
\[
x_i>\max\{y_i:y\in S\setminus\{x\}\},
\]
where the maximum over an empty set is zero. For \(m\geq1\), put
\[
A_m(n)=\sum_{v=1}^{n}(v-1)^{m-1},\qquad A_1(n)=n.
\]
Then the complete shattering polynomial is given by
\[
\boxed{\displaystyle
\Phi_G(z)=\sum_{m=0}^{|G|}s_mz^m,\qquad
s_m=\frac1{m!}\sum_{j=0}^{m}(-1)^j\binom mj
\prod_{i=1}^{d}\bigl(n_i^m-jA_m(n_i)\bigr)\ (m\geq1).}
\]
With \(r=|\{i:n_i\geq2\}|\), its VC dimension is precisely \(\max\{1,r\}\). In particular, \(s_m=0\) for all \(m>\max\{1,r\}\).

**Universal shattering phase transition.** For each \(m\geq2\), choose any integer alphabet size \(q_m\geq2\), and define
\[
p_m=\frac{A_m(q_m)}{q_m^m},\qquad
d_m=\left\lfloor\frac{\log m+c}{p_m}\right\rfloor
\]
for fixed real \(c\), restricting to sufficiently large \(m\) so that \(d_m\geq1\). If \(S_m\) is a uniformly chosen \(m\)-element subset of \(\{1,\ldots,q_m\}^{d_m}\), then
\[
\boxed{\displaystyle
\lim_{m\to\infty}\Pr(S_m\text{ is shattered})=\exp(-e^{-c}).}
\]
Thus the sharp transition location depends on alphabet size. For the Boolean alphabet \(q_m=2\), it is \(d_m\sim 2^m\log m\). For fixed \(q\geq2\), it is
\[
d_m\sim q\left(\frac q{q-1}\right)^{m-1}\log m,
\]
whereas if \(q_m/m\to\infty\), it is \(d_m\sim m\log m\). These are statements about uniformly sampled supports, not worst-case VC dimension.

## Assumptions and scope

All coordinates and thresholds are discrete. The empty orthant is explicitly present because a threshold may be zero. Shattering counts *unlabeled, distinct-point subsets*; the intermediate counting proof uses ordered tuples, with no repeated points among successful tuples. Every \(n_i\) may equal one, and all single-point and one-coordinate boundaries are included. The logarithm in the threshold is natural. The phase-transition theorem allows \(q_m\) to vary arbitrarily with \(m\), subject only to \(q_m\geq2\).

## Proof

**1. Private maxima are necessary.** If \(S\) is shattered and \(x\in S\), some lower orthant contains every element of \(S\setminus\{x\}\) but excludes \(x\). The threshold in coordinate \(i\) must be at least every \(y_i\) with \(y\ne x\). Excluding \(x\) therefore requires \(x_i>\max_{y\ne x}y_i\) in at least one coordinate. This also handles the singleton case because one threshold vector is all zero.

**2. Private maxima are sufficient.** For every prescribed nonempty trace \(T\subseteq S\), take \(t_i=\max\{x_i:x\in T\}\). All of \(T\) lie in the resulting orthant. For any \(y\in S\setminus T\), choose a coordinate where \(y\) is the unique strict maximum over \(S\). Every member of \(T\) then has a strictly smaller coordinate, so \(t_i<y_i\), excluding \(y\). For the empty trace, take all thresholds zero. Thus all traces occur.

**3. Count supports exactly.** Consider \(m\) independently labeled positions in a single coordinate, each taking values from \(\{1,\ldots,n\}\). For a specified label \(a\), the number of coordinate tuples in which label \(a\) is the unique strict maximum is
\(A_m(n)\): sum over its maximum value \(v\) and choose each other coordinate among \(v-1\) smaller values. The events for different labels are disjoint in one coordinate. Consequently, in coordinate \(i\), exactly \(n_i^m-jA_m(n_i)\) value assignments avoid private maxima for a specified set of \(j\) labels. Multiplying over independent coordinates and using inclusion–exclusion over the labels counts ordered \(m\)-tuples in which *each* label has a private maximum. Such tuples have no repeated points; otherwise two coincident points could not have distinct private maxima. Divide by \(m!\) to obtain the displayed coefficient formula. For \(m=1\), the convention \(A_1(n)=n\) gives \(s_1=|G|\).

**4. VC dimension.** For \(m\geq2\), any coordinate can have at most one privately maximal label, and no coordinate of length one can have a strict maximum over a competing label. Therefore \(m\leq r\) for shattered \(m\)-point supports. When \(r\geq2\), select one support point for each nontrivial coordinate, giving it value two there and value one in every other coordinate. Each point is privately maximal, so size \(r\) is attained. A singleton is shattered in every nonempty grid, including \(r=0\) and \(r=1\).

**5. Exact coupon process.** For independent uniformly sampled labeled points \(X_1,\ldots,X_m\) of the cube \(\{1,\ldots,q\}^d\), a fixed coordinate has one uniquely maximal label \(a\) with probability
\(p=A_m(q)/q^m\), independently of its identity. The events for the \(m\) possible labels are disjoint, so the coordinate outputs label \(a\) with probability \(p\) or no label with probability \(1-mp\). These outputs are independent between coordinates. The private-maxima criterion says the points are shattered exactly when every label has appeared at least once. Inclusion–exclusion gives the exact labeled-sample probability
\[
\Pr(\text{every label has a private maximum})
=\sum_{j=0}^{m}(-1)^j\binom mj(1-jp)^d.
\]
This is also \(m!s_m/q^{dm}\). Since the event is impossible when two full points coincide, conditioning on the sampled points being distinct converts it into the uniform-subset probability after division by
\[
\Pr(\text{distinct})=\frac{(q^d)_m}{q^{dm}}.
\]

**6. Limit.** Disjointness of winners gives \(p_m\leq1/m\). Hence \(d_m\geq m(\log m+c)-1\), and the probability of any repeated full points is at most \(\binom m2q_m^{-d_m}\to0\). Moreover \(d_mp_m=\log m+c+O(p_m)\), and \(d_mp_m^2=O(\log m/m)\to0\). For every fixed nonnegative integer \(j\),
\[
\binom mj(1-jp_m)^{d_m}\longrightarrow\frac{e^{-cj}}{j!}.
\]
The Bonferroni even and odd partial sums bound the probability that no label is missing, and after taking \(m\to\infty\), their limits tend to
\(\sum_{j\geq0}(-1)^j e^{-cj}/j!=\exp(-e^{-c})\). The distinctness conditioning tends to one, proving the claimed random-support limit.

For \(q=2\), \(A_m(2)=1\) when \(m\geq2\), hence \(p=2^{-m}\). For fixed \(q\), the term \((q-1)^{m-1}\) dominates the power sum, giving \(p\sim (q-1)^{m-1}/q^m\). Finally elementary upper and lower Riemann sums imply
\[
\frac1m\left(1-\frac1q\right)^m\leq p_m\leq\frac1m;
\]
when \(q_m/m\to\infty\), this proves \(p_m\sim1/m\). These yield the three transition scales.

## Verification

A standalone Python standard-library script, `verify.py`, constructs all actual lower orthants and their traces on small grids, independently evaluates private coordinate maxima, and compares the exhaustive shattering counts with the inclusion–exclusion formula. The checked grids are
\((1)\), \((2)\), \((3)\), \((1,1)\), \((2,2)\), \((3,3)\), \((1,2,3)\), \((2,2,2)\), \((2,3,3)\), \((2,3,4)\), and \((3,3,3)\).
Examples include \(\Phi_{(2,2,2)}(z)=1+8z+9z^2+z^3\) and \(\Phi_{(3,3,3)}(z)=1+27z+162z^2+125z^3\). The script terminates with `ALL_ANCHORED_ORTHANT_PROFILE_CHECKS_PASS 11`. Finite checks are corroborating evidence, not an infinite proof; the phase transition follows from the analytic argument above.

## Relationship to prior work

The general notion of shattering and higher-arity VC complexity is developed by Chernikov and Towsner [1]; that work analyzes qualitative higher-arity regularity rather than this coordinatewise principal-downset polynomial. Chalopin, Chepoi and Knauer [2] treat convex geometries, downset alignments, and VC dimension of associated set systems; Section 4.5 and Section 5.3 distinguish their ambient class of all downsets or convex sets from the **single-principal-downset** concept class here. In particular, a result counting shattered supports for an ambient family of all Cartesian boxes or all order ideals does not imply the coefficients for the restricted family of anchored orthants. The pointwise private-maximum characterization makes that distinction explicit. The limiting distribution is a coupon-collector law with an alphabet-dependent probability of producing a usable private maximum per coordinate. Classical coupon collection and standard VC-dimension calculations are acknowledged ingredients, not independently new claims.

## Limitations

The result concerns anchored lower orthants of finite products of chains, not arbitrary rectangles, nonanchored intervals, or all order ideals. The polynomial counts shattered supports rather than traces on a fixed support of arbitrary size. The random-support limit is asymptotic, with an exact finite probability preceding it, and does not quantify finite-size approximation error. Earlier literature may contain equivalent results under monotone-conjunction, principal-ideal or coordinate-record terminology; exhaustive historical priority has not been established. Independent mathematical review has not been performed.

## References

[1] A. Chernikov and H. Towsner, *Hypergraph regularity and higher arity VC-dimension*, arXiv:2010.00726, first publicly posted 2020-10-01. https://arxiv.org/abs/2010.00726

[2] J. Chalopin, V. Chepoi, and K. Knauer, *Geometry of convex geometries*, arXiv:2405.12660, first publicly posted 2024-05-21. https://arxiv.org/abs/2405.12660
