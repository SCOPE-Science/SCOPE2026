# Signed-intersection convolution and dyadic absorption in symplectic rook monoids

## Finding

Fix an integer \(n\ge1\). On \(\Omega_n=\{1^+,1^-,\ldots,n^+,n^-\}\), a subset is *admissible* if it contains at most one member of each opposite pair \(\{i^+,i^-\}\). Let \(\mathcal S_n\) be the symplectic rook monoid: its singular elements are all partial bijections between admissible subsets, and its units are the signed permutations of \(\Omega_n\). Let \(\mathcal S_{n,r}\) denote its singular rank-\(r\) class, \(0\le r\le n\), and let \(\mu_r\) be uniform on this class. The unit rank is \(2n\), not \(n\).

The rank-class cardinalities are
\[
N_{n,r}=|\mathcal S_{n,r}|=4^r\binom nr^2r!.
\]
For every integer \(k\ge1\) and any ranks \(r_1,\ldots,r_k\in\{0,\ldots,n\}\), take independent \(X_i\sim\mu_{r_i}\) and form \(H=X_k\circ\cdots\circ X_1\). Put \(r_*=\min_i r_i\) and define, for \(0\le j\le r_*\),
\[
b_j=2^{-(k-1)j}\binom nj\prod_{i=1}^k\frac{\binom{r_i}j}{\binom nj},\qquad
p_t=\sum_{j=t}^{r_*}(-1)^{j-t}\binom jt b_j\quad(0\le t\le r_*).
\]
These numbers are exact probabilities: \(p_t=\Pr(\operatorname{rank}H=t)\). Conditional on \(\operatorname{rank}H=t\), the product is uniform over \(\mathcal S_{n,t}\). Hence for every *specified* singular element \(h\) of rank \(t\), the number of ordered rank-constrained products equal to \(h\) is
\[
\#\{(x_1,\ldots,x_k):x_i\in\mathcal S_{n,r_i},\ x_k\cdots x_1=h\}
=\frac{\prod_{i=1}^k N_{n,r_i}}{N_{n,t}}\,p_t.
\]
There are no representations when \(t>r_*\) or when the target is a unit. The convolution of these rank-uniform probability measures is commutative under permutations of their rank parameters, and their linear span is closed under convolution.

**Maximal proper-rank law.** If every \(r_i=n\), then, exactly for every \(n\ge1\) and \(k\ge1\),
\[
\operatorname{rank}(H)\sim\operatorname{Binomial}\bigl(n,2^{-(k-1)}\bigr),
\qquad
\Pr(H=0)=\bigl(1-2^{-(k-1)}\bigr)^n.
\]
Let \(T_n\) be the smallest **number of rank-\(n\) factors** whose product is zero, sampled successively and independently. Since zero is absorbing, \(\Pr(T_n\le k)=(1-2^{-(k-1)})^n\). Its expectation has the finite exact expression
\[
\mathbb ET_n=1+\sum_{j=1}^n(-1)^{j+1}\binom nj\frac1{1-2^{-j}}.
\]
For every fixed integer \(z\), along \(n=2^m\) as \(m\to\infty\),
\[
\Pr(T_{2^m}\le m+1+z)\longrightarrow \exp(-2^{-z}).
\]
For general subsequences with fractional parts \(\{\log_2 n\}\to\theta\in[0,1)\), the corresponding limit at \(\lfloor\log_2 n\rfloor+1+z\) is \(\exp(-2^{\theta-z})\). Thus absorption is logarithmic with a genuine lattice phase; a single unshifted continuous Gumbel limit is not asserted.

## Assumptions and scope

All ranks are numbers of points in a partial map's domain. A signed permutation is a bijection of \(\Omega_n\) that maps each opposite pair onto an opposite pair. Ordinary composition is used, with the rightmost factor acting first. The singular ideal contains ranks \(0,\ldots,n\), while the units have rank \(2n\). Uniformity requires independence and uniform sampling **within each specified singular rank class**; distributions of signed permutations alone and nonuniform factors are outside the theorem. Binomial coefficients with lower index outside the interval from zero to the upper index are zero; the factorial-moment formula is written only for \(0\le j\le r_*\), so no zero denominators arise.

## Proof

**1. Uniform signed extension.** The signed-permutation group \(W_n=C_2\wr S_n\) has order \(2^nn!\). There are \(2^r\binom nr\) admissible rank-\(r\) domains. Fix a partial bijection \(h:D\to I\) of rank \(r\le n\) between two such domains. Exactly \(2^{n-r}(n-r)!\) signed permutations extend it: on the \(r\) occupied opposite pairs the images of the selected points specify the signs and pair permutation, while on the other pairs both may vary freely. Thus if \(D\) is a uniformly chosen admissible rank-\(r\) set and \(W\) is an independent uniform signed permutation, then \(W|_D\) is exactly uniform on \(\mathcal S_{n,r}\). This yields \(N_{n,r}=\bigl(2^r\binom nr\bigr)^2r!\).

**2. Product as signed-set intersection.** Generate independently \(X_i=W_i|_{D_i}\), with uniform signed permutations \(W_i\) and independently uniform admissible \(D_i\) of ranks \(r_i\). Put \(P_0=1\) and \(P_i=W_i\cdots W_1\). Direct expansion of the domain condition for a partial-function product yields
\[
H=P_k\Big|_{A_1\cap\cdots\cap A_k},\qquad A_i=P_{i-1}^{-1}(D_i).
\]
Conditioned on all \(W_i\), the \(A_i\) are independent and each has the uniform admissible rank-\(r_i\) distribution, because signed permutations preserve admissibility. Their joint conditional law is constant, so they are jointly independent of \(P_k\), which is itself uniform in \(W_n\). This proves a labeled-product coupling, not just a rank-count identity. It is symmetric in the \(r_i\); it also implies that the product is uniform over every attained rank class, by the transitive signed-permutation action on admissible rank-\(t\) subsets and uniformity of the independent terminal permutation.

**3. Exact factorial moments and inversion.** Write \(R=\operatorname{rank}H=|A_1\cap\cdots\cap A_k|\). There are \(2^j\binom nj\) admissible subsets of size \(j\). For each fixed such subset \(J\), the probability that a uniform rank-\(r_i\) admissible set contains \(J\) is
\[
\Pr(J\subseteq A_i)=2^{-j}\frac{\binom{r_i}j}{\binom nj}.
\]
Summing the indicator of \(J\subseteq\bigcap_i A_i\) over all admissible \(J\) gives \(\mathbb E\binom Rj=b_j\). Since \(b_j=\sum_{t=j}^{r_*}\binom tj\Pr(R=t)\), finite binomial inversion gives exactly \(p_t\) as displayed. The uniform-target property from Step 2 then gives every prescribed product fiber by multiplying its probability by \(\prod_iN_{n,r_i}\). Because the intersection representation is invariant under permutation of input ranks, all the \(\mu_r\) commute under convolution and their products lie in their linear span.

**4. Individual two-factor transition.** Given a current admissible output set \(I\) of size \(r\), and a fresh independent rank-\(s\) factor, the number of possible admissible input domains meeting \(I\) in exactly \(t\) signed points is
\[
\binom rt\sum_{j=0}^{\min(r-t,s-t)}\binom{r-t}j\binom{n-r}{s-t-j}2^{s-t-j},
\]
with invalid binomial terms zero. Dividing by \(2^s\binom ns\) yields the rank transition probability. This independent local formula verifies the same convolution constants as the all-length intersection proof. Its falling-factorial eigenvalues are \(2^{-j}\binom sj/\binom nj\) on ranks \(0,\ldots,n\) when \(j\le s\), and zero otherwise.

**5. Exact dyadic thinning and absorption.** When every \(r_i=n\), each \(A_i\) independently selects one sign from each opposite pair. A given coordinate survives their intersection exactly when the \(k\) independent signs agree, with probability \(2^{-(k-1)}\); these events are independent across the \(n\) opposite pairs. Therefore the entire product rank is binomial. The zero time identity follows from monotonicity of the product domain. Put \(S_n=T_n-1\). Then \(\Pr(S_n\le t)=(1-2^{-t})^n\) for integers \(t\ge0\), and tail-summing gives \(\mathbb ET_n=1+\sum_{t\ge0}[1-(1-2^{-t})^n]\). The finite binomial expansion and the geometric series in \(2^{-j}\) yield the displayed finite sum. Finally, for \(n=2^m\) and fixed integer \(z\), the zero probability is \((1-2^{-m-z})^{2^m}\to e^{-2^{-z}}\); for a general logarithmic fractional part the same substitution yields the stated lattice-phased limit. These are analytic conclusions, not extrapolations from finite enumeration.

## Verification

The included stand-alone exact-arithmetic Python checker represents each singular element as a partial-function value tuple on \(2n\) signed points and multiplies actual maps. It exhaustively verifies every prescribed output fiber for **every rank-pair** at \(n=1,2,3\), rank-\(n\) repeated products through lengths six, five and four respectively, all 27 rank-triple profiles at \(n=2\), and three mixed rank triples at \(n=3\). Exact formulas, rather than floating-point approximations, are compared against every enumerated target and rank histogram. The captured output ends with `ALL EXHAUSTIVE CHECKS PASSED` followed by successful mixed all-arity checks. The proof above, not the finite checks, establishes all-\(n\), all-length assertions.

## Relationship to prior work

The symplectic rook monoid and its signed-admissible subset description originate in work of Li and Renner and are given explicitly in Li–Li–Cao (2008), with the systematic statement in Li–Li–Cao (2014), Sections 2.5.2 and 4.1, Theorems 10 and 24. Their representation theory, character formulas, cardinalities and order-generating functions provide the established objects and elementary sizes; those sources do not state this rank-conditioned product distribution, individual prescribed fibers or its dyadic absorption law. The 2006 Li–Li–Cao enumeration paper is explicitly not a new counting result here. Feng–Li (2019) classify congruences on the same monoid; congruence classification neither gives nor implies exact finite multiplication fibers. The known rank-uniform convolution theorem for the ordinary symmetric inverse monoid concerns arbitrary unpaired subsets, where deletion is hypergeometric and fixed-corank absorption is coupon-collector scale. Its product law does not establish the signed-transversal intersection law or the binomial and logarithmic absorption formulas proved here. Discrete extreme-value asymptotics for maxima of geometric random variables are classical; novelty is not claimed for that probabilistic limit in isolation.

## Limitations

The result applies to the singular rank classes, not to arbitrary distributions on the unit group or to the parity-restricted even orthogonal rook monoid. The finite verification uses small \(n\), while the universal assertions are proved symbolically. Historical priority may reside in unindexed work on inverse semigroup convolution or signed-rank association schemes. A relevant 2008 publisher full text was not freely retrievable here; the accessible full 2008 preprint on general Renner monoids and the 2014 signed-rook exposition were inspected instead.

## References

1. Z. Li, Z. Li, and Y. Cao, *Representations of the symplectic rook monoid*, International Journal of Algebra and Computation **18** (2008), 837–852. https://doi.org/10.1142/S0218196708004640. Primary mathematics classification 20M30.
2. Z. Li, Z. Li, and Y. Cao, *Representations of the Renner Monoid*, arXiv:0812.1173, first public version 2008-12-05, especially Introduction and Section 3. https://arxiv.org/abs/0812.1173.
3. Z. Li, Z. Li, and Y. Cao, *Algebraic Monoids and Renner Monoids*, Fields Institute Communications **71** (2014), Chapter 2.5.2 and Theorem 24. https://www-users.cse.umn.edu/~reiner/REU/REU2018notes/li-li-cao-renner-monoids.pdf.
4. Z. Li, Z. Li, and Y. Cao, *Enumeration of symplectic and orthogonal injective partial transformations*, Discrete Mathematics **306** (2006), 1781–1787. https://doi.org/10.1016/j.disc.2006.03.047.
5. J. Feng and Z. Li, *Congruences on Orthogonal Rook Monoids and Symplectic Rook Monoids*, arXiv:1906.02880, 2019, especially Theorem 5.2. https://arxiv.org/abs/1906.02880.
