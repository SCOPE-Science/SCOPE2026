# Five sharp three-row optima for almost-sure Kaczmarz sampling on a pentagonal frame

## Finding

Let \(u_j=(\cos(j\pi/5),\sin(j\pi/5))\), \(j=0,\ldots,4\), be the unit normal rows of a consistent planar linear system. At each standard unrelaxed randomized Kaczmarz step, independently select row \(j\) with probability \(p_j\ge0\), where \(\sum_{j=0}^4p_j=1\). For the orthogonal error projector \(Q_j=I-u_ju_j^\top\), define the almost-sure *squared operator-norm contraction exponent*
\[
 R(p)=-\lim_{t\to\infty}\frac1t\log\|Q_{I_t}\cdots Q_{I_1}\|_2^2.
\]
The limit exists almost surely and is deterministic for every probability vector, including boundary points. Define
\[
 a=-\log\cos^2(\pi/5)=0.4238707110\ldots,\qquad
 b=-\log\cos^2(2\pi/5)=2.3487180112\ldots.
\]
Then, with indices interpreted modulo five,
\[
 R(p)=2a\sum_{j=0}^4p_jp_{j+1}+2b\sum_{j=0}^4p_jp_{j+2},
 \qquad \boxed{\max_pR(p)=\frac{2b^2}{4b-a}=1.2298462771\ldots}.
\]
There are **exactly five maximizing probability vectors**: for any center \(j\in\{0,\ldots,4\}\),
\[
 \boxed{p_j=\frac{2b-a}{4b-a},\quad
 p_{j-2}=p_{j+2}=\frac{b}{4b-a},\quad
 p_{j-1}=p_{j+1}=0.}
\]
Numerically, the three positive probabilities are \(0.4763755073\ldots,0.2618122463\ldots,0.2618122463\ldots\). The best sampler supported on at most two rows has rate \(b/2\), less by precisely \(ab/[2(4b-a)]\). Uniform sampling has rate \(2(a+b)/5\), also strictly less. These are *quenched/typical-path* rates, not annealed mean-square convergence factors.

For comparison, uniform sampling attains the global minimum \(1/2\) of the worst-direction **one-step expected squared error factor**, because the five rows form a tight frame. None of the five typical-rate-maximizing laws attains that one-step optimum: for each, the one-step factor equals
\[
 \frac12\left(1+\frac{2b-a-2b\cos(\pi/5)}{4b-a}\right)
 =0.526377\ldots>\frac12.
\]
Thus even a symmetric unit-norm planar frame can have strictly different typical-path-optimal and one-step mean-square-optimal iid sampling designs.

## Assumptions and scope

The five rows need only have the specified **directions**; their nonzero magnitudes, row order, and consistent right-hand sides do not affect the error projectors. For the displayed formulas fix the equivalent unit-normal representation. The rows span \(\mathbb R^2\). Independent, identically distributed row selections use a **fixed** probability law \(p\), which may assign zero mass. The norm is the Euclidean induced matrix norm and the contraction exponent measures the product as a linear operator, not one exceptional initialized error vector. The rows are unrelaxed orthogonal projectors; no adaptive, reshuffled, Markov, or noisy sampling is optimized.

## Proof

**1. Exact almost-sure exponent.** Let \(v_j=(-\sin(j\pi/5),\cos(j\pi/5))\). Then \(Q_j=v_jv_j^\top\), hence for every finite index sequence with \(t\ge2\),
\[
 \|Q_{i_t}\cdots Q_{i_1}\|_2^2
 =\prod_{s=2}^t |v_{i_s}^\top v_{i_{s-1}}|^2
 =\prod_{s=2}^t\cos^2((i_s-i_{s-1})\pi/5).
\]
No cosine factor vanishes for the five indicated projective directions. Split the logarithmic pair costs into the even and odd adjacent-pair subsequences, each of which consists of iid random variables. The strong law of large numbers, applied separately to those subsequences, yields the stated almost-sure limit. A pair at cyclic distance one contributes \(a\); one at cyclic distance two contributes \(b\); identical consecutive indices contribute zero. Because iid ordered pairs appear with probabilities \(p_ip_j\),
\[
 R(p)=2a\sum_jp_jp_{j+1}+2b\sum_jp_jp_{j+2}.
\]
This general *rank-one ergodic quadratic formula* is established in earlier literature; only its sharp pentagonal optimization is asserted here as a new finding.

**2. A strict weight inequality.** Set \(c=\cos(\pi/5)=(1+\sqrt5)/4\), \(d=\cos(2\pi/5)=(\sqrt5-1)/4\). Direct algebra gives \(c^3=(2+\sqrt5)/8\), and \(c^3-d=(4-\sqrt5)/8>0\). Taking logarithms of squares yields \(b>3a>0\).

**3. No maximum has four or five positive probabilities.** Regard the objective as the quadratic form \(R(p)=p^\top Wp\), where \(W_{ii}=0\), \(W_{ij}=a\) for cyclic distance one, and \(W_{ij}=b\) for cyclic distance two. If at least four entries of \(p\) are positive, some four consecutive cyclic indices \(j,j+1,j+2,j+3\) all have positive masses. On these four indices let \(z=(1,-1,1,-1)\), zero elsewhere, so \(\sum_i z_i=0\) and, by listing the six unordered pair types,
\[
 z^\top Wz=2(b-3a)>0.
\]
Both \(p+\varepsilon z\) and \(p-\varepsilon z\) remain probability vectors for sufficiently small positive \(\varepsilon\), while
\[
 \frac{R(p+\varepsilon z)+R(p-\varepsilon z)}2
 =R(p)+2\varepsilon^2(b-3a)>R(p).
\]
Therefore no such \(p\) can maximize the objective. Any maximizer has at most three nonzero entries.

**4. Exhaustive three-vertex support types.** Every three-point subset of the five-cycle has either two distance-two pairs and one distance-one pair (type A) or one distance-two pair and two distance-one pairs (type B). The five type-A triples are exactly \(\{j,j-2,j+2\}\). For a type-A triple let the center probability be \(x\), with the two end probabilities \(y,z\) and \(x+y+z=1\). The objective is
\[
 R=2bx(y+z)+2ayz\le 2bx(1-x)+\frac a2(1-x)^2.
\]
Equality requires \(y=z=(1-x)/2\). The right-hand quadratic is strictly concave because \(4b-a>0\); its unique maximizer on \([0,1]\) is
\[
 x=\frac{2b-a}{4b-a},\qquad y=z=\frac{b}{4b-a},
 \qquad R=\frac{2b^2}{4b-a}.
\]
For a type-B triple, let \(x\) be the center linked by two cost-\(a\) pairs, with leaves \(y,z\) linked by cost \(b\). Then, since \(b>2a\),
\[
 R=2ax(y+z)+2byz
 \le 2ax(1-x)+\frac b2(1-x)^2
 \le\frac b2(1-x^2)\le\frac b2.
\]
For at most two occupied rows, \(R\le b/2\). The type-A value exceeds this by the strictly positive quantity
\[
 \frac{2b^2}{4b-a}-\frac b2=\frac{ab}{2(4b-a)}.
\]
Consequently exactly the five indicated type-A probability vectors maximize \(R\), with no other maximizers.

**5. Comparison with uniform and mean-square sampling.** For \(p_j=1/5\), count five near and five far unordered pairs to get \(R_{\rm unif}=2(a+b)/5\). The difference from the optimum is
\[
 \frac{2b^2}{4b-a}-\frac{2(a+b)}5
 =\frac{2(b^2-3ab+a^2)}{5(4b-a)}>0,
\]
where positivity follows from \(b>3a\). For one Kaczmarz step from deterministic error \(e\),
\[
 \sup_{\|e\|_2=1}\mathbb E\|Q_Ie\|_2^2
 =\lambda_{\max}\left(\sum_jp_jQ_j\right)
 =\frac12\left(1+\left|\sum_jp_je^{2\pi i j/5}\right|\right).
\]
The trace of \(\sum_jp_jQ_j\) is one, giving a universal lower bound \(1/2\), attained by uniform sampling because \(\sum_j e^{2\pi i j/5}=0\). For a type-A maximizer centered at \(j=0\), the doubled-angle sum is \(x-2y\cos(\pi/5)\). This is strictly positive since \(b>3a\) implies \(x/y=2-a/b>5/3>2\cos(\pi/5)=(1+\sqrt5)/2\). The same modulus holds for every cyclic rotation, so all five typical-optimal distributions have strictly larger one-step factor. This proves the full classification and the objective reversal.

## Verification

The standalone Python 3 checker `verify_pentagonal.py` uses only the standard library and prints `VERIFY_OK 10829 assertions`. It checks the strict parameter inequality, all five claimed solutions, all ten three-subset support patterns, five four-coordinate exchange certificates, exact rational analogues of the algebraic optimum/difference identities, 10,000 seeded random interior probability vectors and face samples, and simulated finite-length transition averages. The experiments are finite and **do not replace the strong-law argument or the global analytic support proof**. Reproduce with `python3 verify_pentagonal.py` from the extracted package.

## Relationship to prior work

Strohmer and Vershynin (2007) introduced random row-norm-based Kaczmarz with expected exponential convergence; their theorem does not optimize the almost-sure exponent for this five-direction design. Agaskar, Wang, and Lu (2014) analyze exact **annealed mean-square** behavior and optimized row-selection semidefinite programs; this differs from the typical-path objective here. Altschuler and Parrilo (2019) already prove the general rank-one quadratic expression for the Lyapunov exponent and its hard distribution-design problem: that formula is **prior art**, not a new contribution of this note. Their inspected manuscript does not state the regular-pentagon five-row optimum, the complete five-point equality set, or the strict comparison against optimal one-step mean-square sampling.

The closest indexed planar Kaczmarz optimizer result (published-finding corpus, 2026-10-13) establishes exact coincidence between optimizers of the **annealed** asymptotic mean-square factor and the classical one-step bound. Its `RESULT.md`, including scope and limitations, expressly excludes quenched exponents. The present calculation is on a different stochastic objective and demonstrates a strict noncoincidence with that one-step bound on a natural tight frame. These comparisons distinguish mathematical statements; mere absence from a search index cannot certify publication priority.

## Limitations

The result concerns five equally spaced **real projective row directions** in the plane, iid fixed-probability unrelaxed Kaczmarz, and the almost-sure **operator** exponent. It does not classify other polygon sizes, perturbations of directions, higher-dimensional frames, per-iteration mean-square error, arbitrary initial vectors with possible exact zero projections, or adaptive sampling. In the general rank-one setting, the quadratic Lyapunov formula is known. An equivalent solution of this specific weighted-five-cycle quadratic optimization might exist in unindexed optimization literature; any such prior result would affect originality. The finite checker is only corroborative, and no independent audit has been performed.

## References

1. T. Strohmer and R. Vershynin, *A randomized Kaczmarz algorithm with exponential convergence*, first public arXiv version 2007-02-08, arXiv:math/0702226v1. https://arxiv.org/abs/math/0702226
2. A. Agaskar, C. Wang, and Y. M. Lu, *Randomized Kaczmarz Algorithms: Exact MSE Analysis and Optimal Sampling Probabilities*, GlobalSIP 2014, DOI:10.1109/GlobalSIP.2014.7032145. Lawful author manuscript: https://dash.harvard.edu/server/api/core/bitstreams/7312037d-8b4a-6bd4-e053-0100007fdf3b/content
3. J. Altschuler and P. A. Parrilo, *Lyapunov Exponent of Rank One Matrices: Ergodic Formula and Inapproximability of the Optimal Distribution*, arXiv:1905.07531v1, first public 2019-05-18. https://arxiv.org/abs/1905.07531
4. *Planar coincidence theorem for optimal randomized Kaczmarz sampling*, public `RESULT.md`, 2026-10-13. https://github.com/published-finding corpus/2026/blob/main/2026/10/13/SCOPE-planar-coincidence-theorem-for-optimal-randomized-kaczmarz-sampl--54597ea58934/RESULT.md
