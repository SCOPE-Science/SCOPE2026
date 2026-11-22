# A Poisson–forest homophily window in rare-community recursive attachment

## Finding

Fix \(c>0\), \(q_B\in(0,1)\), and put \(a=q_B/(1-q_B)\). Let \(n\) be the number of new vertices appended to a fixed connected simple initial graph with \(r\ge1\) type-A vertices and \(b\ge1\) type-B vertices. In the \(n\)-th experiment, use independent type-A birth probability \(p_n=c/n\) at each of the \(n\) arrivals. Set the degree exponent to \(\gamma=0\) and take the type-A cross-community preference \(q_{A,n}\in[0,1]\), with \(nq_{A,n}\to\theta\in[0,\infty]\). Assume \(n>c\).

Order the newly born type-A vertices by time. Their normalized birth times converge to the ordered points \(0<U_1<\cdots<U_K<1\) of a rate-\(c\) Poisson point process on \((0,1)\). Conditional on those times, the limiting parent decisions of the new A vertices are independent. At \(U_i=u\), there are \(r+i-1\) existing type-A vertices. For finite \(\theta\), each of them is selected as parent with probability

\[
\frac1{r+i-1+\theta u},
\]

while the probability of choosing a type-B parent is \(\theta u/(r+i-1+\theta u)\). The latter event has probability one at \(\theta=\infty\). These decisions define a finite random rooted forest on the newly born type-A vertices, the fixed A founders, and a generic B-parent boundary symbol; the precise B endpoint is not part of the limit object.

Let \(J_i\) count children of the \(i\)-th new-A vertex that are subsequently born of type B. Given the entire limiting birth-time process, the \(J_i\) are independent with

\[
J_i\sim\operatorname{Poisson}\!\left(a\log\frac1{U_i}\right),
\qquad a=\frac{q_B}{1-q_B},
\]

and independent of the A-parent decisions. Its final degree is \(1+J_i+H_i\), where \(H_i\) is its number of later new-A children in the finite limiting forest.

Simultaneously, if \(d_v\) is the initial degree and \(D_{v,n}\) the final degree of an initial vertex \(v\), define \(\beta_v=a\) for an A founder and \(\beta_v=1\) for a B founder. Then, jointly over all founders,

\[
\left(\frac{D_{v,n}-d_v-\beta_v\log n}{\sqrt{\beta_v\log n}}\right)_{v\in V(G_0)}
\Longrightarrow \mathcal N_{r+b}(0,I_{r+b}),
\]

and this Gaussian vector is asymptotically independent of the entire finite A-birth process and its parent and child-count marks.

At the endpoint \(\theta=\infty\) every new A vertex attaches to B. Therefore the counts \(N_k\) of new-A vertices with final degree \(k\ge1\) converge jointly to mutually independent Poisson variables with means

\[
\boxed{\mathbb E N_k=\frac{c}{1+a}\left(\frac{a}{1+a}\right)^{k-1},\qquad k\ge1.}
\]

The finite \(\theta\)-window is the sharp scale \(q_{A,n}\asymp n^{-1}\) separating A-ancestry retention from complete escape to the majority community.

## Assumptions and scope

The underlying growth mechanism is the *soft* (Model 2) two-community attachment rule of Ben-Hamou, Broutin and Cazaux. A vertex born of type \(T\) chooses an existing vertex of type \(T\) with weight \(1-q_T\) per vertex and an existing vertex of the opposite type with weight \(q_T\) per vertex. We use \(\gamma=0\), so these weights do not depend on degrees. Every experiment contains exactly \(n\) new vertices; \(c,q_B,r,b,G_0\) are fixed, while \(p_n,q_{A,n}\) may vary with \(n\). All type choices are independent. After conditioning on the complete birth-type word, each attachment choice is independent of every other attachment choice because the two current population counts are then deterministic. Both founder types are nonempty, so attachment probabilities are defined even at the endpoints of \(q_{A,n}\). Convergence of finite marked configurations uses the usual marked finite-point-process topology on compact subintervals of \((0,1)\); no assertion is made about the label of the selected majority-community parent.

## Proof

**1. Rare birth process.** The newborn type indicators are independent Bernoulli\((c/n)\). For disjoint subintervals \(I_1,\ldots,I_m\subset(0,1)\), their type-A counts have independent binomial laws with expectations \(c|I_j|+o(1)\), hence converge to independent Poisson variables. The total count is tight: \(K_n\Rightarrow\operatorname{Poisson}(c)\). Moreover, \(\mathbb P(\text{some A birth before }\varepsilon n)\le c\varepsilon\). This permits restricting to \(K_n\le M\) and birth times in \([\varepsilon n,n]\), then sending \(M\uparrow\infty\), \(\varepsilon\downarrow0\).

**2. Conditional attachment kernels.** Condition on a type word with \(K_n\le M\). Immediately before the \(j\)-th new vertex, write \(A_j=r+h_j\), \(B_j=b+j-1-h_j\), where \(h_j\) is the number of earlier new-A births. If the new vertex is B, it attaches to any particular existing A vertex with probability \(a/(B_j+aA_j)\), and to any particular B vertex with probability \(1/(B_j+aA_j)\). The denominator is \(j+(r+b-1)+(a-1)(r+h_j)=j+O_M(1)\). If new vertex \(j_i\) is A, it attaches to a particular A vertex with probability

\[
\frac{1-q_{A,n}}{(1-q_{A,n})(r+i-1)+q_{A,n}(b+j_i-i)},
\]

because precisely \(i-1\) A immigrants precede it. For \(j_i/n\to U_i\), multiplication of the numerator and denominator by the same factor gives the stated finite-\(\theta\) transition and its \(\theta=\infty\) endpoint. Independence of the parent decisions conditional on the type word passes to the finite limit, including the forest constraints induced by existing A vertices.

**3. Conditional Poisson marks.** Given the birth word, for a particular new A vertex born at \(j_i\), its number of later B children is a sum of independent Bernoulli indicators with parameters \(a/(B_j+aA_j)\) at the B birth times \(j>j_i\). Uniformly for \(K_n\le M\) and \(j_i\ge\varepsilon n\), its mean is \(a\log(n/j_i)+O_{M,\varepsilon}(n^{-1})\). At a given B birth one vertex alone is chosen, so the joint probability-generating function of all these marks is a product of factors \(1+\sum_i p_{i,j}(z_i-1)\). On \([\varepsilon n,n]\), \(\sum_j(\sum_i p_{i,j})^2=O_{M,\varepsilon}(n^{-1})\), so the logarithm tends to \(\sum_i a\log(1/U_i)(z_i-1)\). This is the generating function of independent Poisson marks. Conditional independence from the A-parent forest is exact before taking the limit.

**4. Joint founder central limit.** For each founder \(v\), its B-arrival attachment count is a sum of conditionally independent indicators of probability \(\beta_v/(j+O_M(1))\). Its conditional mean is \(\beta_v\log n+O_M(1)\), its variance is \(\beta_v\log n+O_M(1)\), and the conditional off-diagonal covariance between distinct founders is \(-\sum_j p_{v,j}p_{w,j}=O_M(1)\). Increments are bounded, so the multivariate Lindeberg theorem yields independent standard Gaussian limits after division by \(\sqrt{\beta_v\log n}\). Contributions from the at-most-\(M\) A-born arrivals to any founder are bounded by \(M\) and vanish on this scale.

To prove independence from the Poisson forest and its marks, on the event of no type-A birth before \(\varepsilon n\), approximate the founder Gaussian vector using only attachment decisions at times \(j\le\varepsilon n\). The omitted centered sum has conditional variance at most \(O_M(\log(1/\varepsilon))\), hence is negligible relative to \(\log n\) for fixed \(\varepsilon\). Its conditional mean discrepancy is also \(O_M(1+\log(1/\varepsilon))\). All forest and Poisson-mark decisions then use times strictly after \(\varepsilon n\), which are independent of this truncated founder vector given the birth word. Uniform conditional Gaussian convergence and the Poisson-process limit establish the claimed stable joint independence; finally \(\varepsilon\downarrow0\) and \(M\uparrow\infty\).

**5. Geometric degree intensities.** At \(\theta=\infty\), each new A vertex chooses a B parent with limiting probability one, hence has no A children. A Poisson point at time \(u\) is independently marked by a \(\operatorname{Poisson}(a\log(1/u))\) count, so Poisson thinning yields independent counts by final degree. For \(k\ge1\), the intensity is

\[
\frac{c}{(k-1)!}\int_0^1 u^a\big(a\log(1/u)\big)^{k-1}\,du
=\frac{c\,a^{k-1}}{(1+a)^k}.
\]

The intensities sum to \(c\), as required by the limit of the total number of newly born A vertices. This completes the proof.

## Verification

Run `python verify.py` with Python 3 and no external packages. It checks finite attachment-kernel normalization and factorization for all two-type birth words through seven arrivals, exact multi-vertex moment calculations, finite-size critical-window probabilities and exact geometric-intensity arithmetic. The executable reports 3,662 passed finite or arithmetic assertions. The proof of the infinite-dimensional statements above is analytic, not an inference from these assertions.

## Relationship to prior work

Ben-Hamou, Broutin and Cazaux [1] define both community attachment mechanisms and establish fixed-parameter limiting empirical degree laws. This theorem concerns their soft Model 2 at \(\gamma=0\) under the *vanishing* type-A birth probability \(p_n=c/n\) and potentially vanishing \(q_{A,n}\); it identifies finite rare-subpopulation ancestry, conditional Poisson marks, an exact inverse-size crossover, and independent Gaussian fluctuations for finitely many founders. Bhamidi, Fan, Fraiman and Nobel [2] study community-modulated recursive trees and fixed-composition population limits. Their per-type geometric degree phenomena do not imply joint finite rare-immigrant Poisson counts or the critical homophily window when the minority population is tight. The present statement concerns a different scaling question, not a contradiction or extension by mere substitution in a fixed-parameter limit.

## Limitations

Only the degree-independent \(\gamma=0\) *soft* attachment mechanism is covered. The identity of the majority-type parent of a rare A arrival is intentionally not retained. No generalization to degree reinforcement, a growing initial graph, vanishing \(q_B\), or a fixed positive minority proportion is proved. The source comparison is not exhaustive, and an unindexed pre-existing result on rare-color recursive trees or Poisson marking could entail part of the conclusion. No independent proof assessment has been performed.

## References

[1] A. Ben-Hamou, N. Broutin and C. Cazaux, *Sublinear multi-type preferential attachment*, arXiv:2611.06904v1, first submitted 2026-11-04. https://arxiv.org/abs/2611.06904

[2] S. Bhamidi, R. Fan, N. Fraiman and A. Nobel, *Community modulated recursive trees and population dependent branching processes*, arXiv:2004.02697 (2020); *Random Structures & Algorithms* 60 (2022), 201–232. https://arxiv.org/abs/2004.02697
