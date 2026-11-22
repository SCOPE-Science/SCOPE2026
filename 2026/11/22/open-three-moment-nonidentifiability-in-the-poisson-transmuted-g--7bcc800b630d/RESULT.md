# Open three-moment nonidentifiability in the Poisson–transmuted geometric count family

## Finding

For the three-parameter Poisson–transmuted geometric (PoiTG) count family, **the first three moments do not determine its three parameters**, even away from parameter-space boundaries. There is an open set of moment vectors realized by at least two distinct, strictly interior distributions. One exact moment vector is

\[
\mathbb E[Y]=1,\qquad \mathbb E[Y^2]=3,\qquad \mathbb E[Y^3]=14.
\]

The two distributions are genuinely different, not merely different parameterizations of the same law. This excludes a globally unambiguous method-of-three-moments inversion for this family; it does not concern identifiability from the entire probability mass function or the maximum-likelihood procedures considered in the primary paper.

## Assumptions and scope

Let \(Y=P+T\), where \(P\) is Poisson with rate \(\lambda>0\), independently of a nonnegative integer random variable \(T\) with probability mass function

\[
\Pr(T=j)=(1-\alpha)(1-q)q^j+\alpha(1-q^2)q^{2j},\qquad j\in\{0,1,\ldots\},
\]

with \(0<q<1\) and \(0<\alpha<1\). This is the strictly interior, positively mixed part of the PoiTG model introduced by Nandi, Chakraborty and Biswas. The factorial cumulants \(\kappa_{[k]}\) are defined by the local Taylor expansion

\[
\log\mathbb E[(1+t)^Y]=\sum_{k\ge1}\kappa_{[k]}\frac{t^k}{k!}.
\]

Here and below, statements concerning an open region use the usual Euclidean topology on moment vectors, not a claim of exactly two preimages.

## Proof

**1. Exact factorial-cumulant coordinates.** Set

\[
 r=\frac{q(q+\alpha)}{1+\alpha q},\qquad
 a=\frac{q}{1-q},\quad b=\frac{q^2}{1-q^2},\quad c=\frac{r}{1-r}.
\]

Direct summation of the two geometric series gives

\[
G_Y(z)=e^{\lambda(z-1)}\frac{(1-q)(1+\alpha q)(1-rz)}{(1-qz)(1-q^2z)},
\]

where \(q^2<r<q\) and therefore \(b<c<a\). Normalizing at \(z=1\) and putting \(z=1+t\),

\[
\log G_Y(1+t)=\lambda t-\log(1-at)-\log(1-bt)+\log(1-ct).
\]

Consequently,

\[
(\kappa_{[1]},\kappa_{[2]},\kappa_{[3]})=
(\lambda+a+b-c,\;a^2+b^2-c^2,\;2(a^3+b^3-c^3)). \tag{1}
\]

These formulas follow from derivatives at zero; the geometric series and logarithms are analytic in a neighborhood of zero.

**2. A continuous path preserving the first two factorial cumulants.** Fix any \(s>0\) and define

\[
q_0=\frac{s}{1+s},\qquad q_1=\sqrt{\frac{s}{1+s}},\qquad q_0<q_1.
\]

For \(q_0<q<q_1\), define \(a(q)\) and \(b(q)\) as above and

\[
c(q)=\sqrt{a(q)^2+b(q)^2-s^2},\qquad
r(q)=\frac{c(q)}{1+c(q)},\qquad
\alpha(q)=\frac{r(q)-q^2}{q(1-r(q))}.
\]

On this interval \(a>s>b\), and hence \(b<c<a\); equivalently \(q^2<r<q\), which gives \(0<\alpha(q)<1\). Put \(m(q)=a+b-c\). It is strictly positive because \(c<a+b\). Also

\[
c^2-(a+b-s)^2=2(a-s)(s-b)>0,\qquad a+b-s>0,
\]

so \(m(q)<s\). Thus for every \(\mu>s\), the choice \(\lambda(q)=\mu-m(q)>0\) gives valid interior model parameters and fixes \(\kappa_{[1]}=\mu\), \(\kappa_{[2]}=s^2\).

**3. Every intermediate third cumulant has at least two preimages.** Let

\[
F_s(q)=a(q)^3+b(q)^3-\big(a(q)^2+b(q)^2-s^2\big)^{3/2}.
\]

This extends continuously to \([q_0,q_1]\), with \(F_s(q_0)=F_s(q_1)=s^3\). In its interior put \(d=a^2-s^2=c^2-b^2>0\). Strict convexity of \(x\mapsto x^{3/2}\) on positive arguments and \(s^2>b^2\) imply

\[
a^3-s^3=(s^2+d)^{3/2}-(s^2)^{3/2}
>(b^2+d)^{3/2}-(b^2)^{3/2}=c^3-b^3.
\]

Therefore \(F_s(q)>s^3\) throughout the interior. Define \(M_s=\max_{[q_0,q_1]}F_s(q)>s^3\). For each \(y\) strictly between \(s^3\) and \(M_s\), apply the intermediate-value theorem on either side of an interior maximizer: there are two distinct interior values \(q_-<q_+\) with \(F_s(q_-)=F_s(q_+)=y\). Formula (1) then yields exactly the same factorial cumulants \((\mu,s^2,2y)\) at both parameter triples. The transformation between the first three factorial cumulants and the first three raw moments is polynomial and invertible, so these raw moment vectors also coincide. Since the maximization is over a continuously moving compact interval (rescale it to \([0,1]\)), \(s\mapsto M_s\) is continuous. Accordingly, \(\{(\mu,s,y):s>0,\;\mu>s,\;s^3<y<M_s\}\) is open, and so is the corresponding three-moment region.

**4. An explicit shared moment vector.** Take \(s=1\), so \(q_0=1/2\), \(q_1=1/\sqrt2\), and choose \(\mu=1\) (the strict inequality \(\lambda(q)>0\) still holds because \(m(q)<1\)). At the interior witness \(q=3/5\),

\[
a=\frac32,\quad b=\frac9{16},\quad c=\frac{\sqrt{401}}{16},\quad
F_1(3/5)=\frac{14553-401\sqrt{401}}{4096}>\frac32.
\]

The final strict inequality is equivalent to the positive integer comparison \(8409^2-401^3=6230080>0\). Since \(F_1(1/2)=F_1(1/\sqrt2)=1\), there exist \(q_-\in(1/2,3/5)\) and \(q_+\in(3/5,1/\sqrt2)\), each with \(F_1=3/2\). Their associated \(\lambda=1-a-b+c\) and \(\alpha\) are strictly admissible. Formula (1) gives \((\kappa_{[1]},\kappa_{[2]},\kappa_{[3]})=(1,1,3)\). The ordinary cumulants satisfy \(\kappa_1=\kappa_{[1]}\), \(\kappa_2=\kappa_{[1]}+\kappa_{[2]}\), \(\kappa_3=\kappa_{[1]}+3\kappa_{[2]}+\kappa_{[3]}\). Thus the ordinary mean, variance and third centered moment equal \(1,2,7\), yielding raw moments \(1,3,14\).

**5. Distinct laws rather than redundant coordinates.** For strictly interior parameters, \(q^2<r<q\) ensures no cancellation of the pole of \(G_Y(z)\) at \(z=1/q\). Its positive radius of convergence is therefore exactly \(1/q\), which is a distributional invariant. Since \(q_-\ne q_+\), the two probability laws are different.

## Verification

The standalone reproducibility program `check_moment_collision.py` verifies the rational probability-generating-function factorization and factorial-cumulant derivatives at twelve interior rational parameter pairs; it checks the exact radical witness with the positive integer comparison and calculates numerical diagnostics for both crossing branches. Run with `python check_moment_collision.py` using Python 3 and SymPy. The program is a finite algebraic cross-check; the all-parameter and open-region conclusions are proved by the preceding convexity and continuity arguments, not by finite sampling.

## Relationship to prior work

Nandi, Chakraborty and Biswas introduced the Poisson–transmuted geometric convolution, published its generating function and its first moments, and developed numerical maximum-likelihood and EM estimation methods. Their source supplies this theorem's underlying probability model, but its moment formulas alone do not assert or establish the open-region two-to-one failure of the three-moment map. A later presentation of the same convolution treats dispersion and inference, without a corresponding moment-fiber theorem in the material inspected. Related published results about geometric mixtures or other Poisson convolutions address different parameter spaces or inference questions and are not logically equivalent. This is a mathematical comparison, not an absolute priority claim.

## Limitations

The result only asserts at least two preimages on an open region, not the exact number or global geometry of every moment fiber. The explicitly displayed moment vector uses \(\mu=s=1\), whereas the proved open region requires \(\mu>s\). The full count distribution is distinguishable by its tail radius; maximum likelihood using the whole data may therefore remain identifiable. No finite-sample inference guarantees or optimization procedures are derived. Independent historical-priority and mathematical validation remain to be performed.

## References

- Nandi, A., Chakraborty, S. and Biswas, A. (2023). *A new count model based on Poisson-Transmuted Geometric convolution*. arXiv:2306.07219v1, first publicly posted 12 June 2023. https://arxiv.org/abs/2306.07219
- Open author/preprint full-text transcription of the same work, including probability mass function, generating function, moments and estimation sections. https://www.researchgate.net/publication/371506994_A_new_count_model_based_on_Poisson-Transmuted_Geometric_convolution
- *Poisson-Transmuted Geometric Convolution for Overdispersed Count Data* (later treatment; model and moment formulas compared). https://www.researchgate.net/publication/397316675_Poisson-Transmuted_Geometric_Convolution_for_Overdispersed_Count_Data
