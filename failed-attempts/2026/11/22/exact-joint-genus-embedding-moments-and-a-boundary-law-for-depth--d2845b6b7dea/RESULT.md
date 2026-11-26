# Exact joint genus–embedding moments and a boundary law for depth-two numerical semigroups

## Finding

Fix integers \(m>r\ge2\), put \(F=m+r\), and choose uniformly at random a numerical semigroup of multiplicity \(m\) and Frobenius number \(F\). A complete description of the joint genus–embedding behavior follows from a finite additive-sumset defect, with **an exact finite expectation, an exact genus-conditioned expectation, and a nontrivial limiting integer-valued boundary law**.

Write \(B\subseteq\{1,\ldots,r-1\}\), and put
\[
U_r(B)=\#\{i:2\le i\le r,\ i\notin B,\ i\notin B+B\}.
\]
Here \(B+B\) permits equal summands. Let \(g\) and \(e\) denote the genus and embedding dimension. Then
\[
g=m+r-1-|B|,\qquad e=m-r+1+|B|-\mathbf1_{\{1\in B\}}+U_r(B),
\]
so that
\[
e+g-2m=U_r(B)-\mathbf1_{\{1\in B\}}.
\tag{1}
\]
Uniformly in \(m>r\), the **exact** expectation is
\[
\mathbb Ee=m-\frac r2+\frac52-
\begin{cases}
2(3/4)^{r/2-1},&r\text{ even},\\
\frac32(3/4)^{(r-3)/2},&r\text{ odd}.
\end{cases}
\tag{2}
\]

For the full genus-conditioned refinement put \(n=r-1\), \(h_i=\lfloor(i-1)/2\rfloor\), and \(\delta_i=1\) for even \(i\) and \(0\) otherwise. For every \(0\le k\le n\), the conditional expectation at genus \(g=m+r-1-k\) is
\[
\mathbb E[e\mid |B|=k]=m-r+1+k-\frac{k}{n}
+\frac{1}{\binom nk}\sum_{i=2}^{r}[t^k]
(1+2t)^{h_i}(1+t)^{n-\mathbf1_{\{i<r\}}-2h_i-\delta_i}.
\tag{3}
\]
All displayed polynomial exponents are nonnegative.

There is also a limiting *boundary* rather than Gaussian law for the **joint defect**. Let \(B_\infty\subset\mathbb N_{\ge1}\) have independent fair membership indicators, and define
\[
W=\sum_{i=2}^\infty\mathbf1_{\{i\notin B_\infty,\ i\notin B_\infty+B_\infty\}}-\mathbf1_{\{1\in B_\infty\}}.
\tag{4}
\]
This sum is almost surely finite, the distribution of \(W\) is nondegenerate, and \(\mathbb EW=2\). For a universal constant \(C\), coupling the same first \(r-1\) Bernoulli coordinates gives
\[
 d_{\mathrm{TV}}(\mathcal L(e+g-2m),\mathcal L(W))\le C(3/4)^{\lfloor(r-1)/2\rfloor}.
\tag{5}
\]
Meanwhile, for any sequence of integers \(m=m(r)>r\),
\[
\frac{e-(m-r/2)}{\sqrt r/2}\ \Longrightarrow\ \mathcal N(0,1).
\tag{6}
\]

## Assumptions and scope

A numerical semigroup is a cofinite additive submonoid of the nonnegative integers. Its multiplicity is its least positive member, its Frobenius number its greatest missing integer, its genus the count of missing nonnegative integers, and its embedding dimension the number of elements in its unique minimal additive generating set. The result concerns **all** such semigroups with \(m>r\ge2\) and \(F=m+r\), equally weighted; no semigroups outside this domain are claimed. The singleton case \(r=1\) is omitted. The limit uses \(r\to\infty\), with \(m>r\) allowed to vary arbitrarily.

## Proof

**1. Boolean parametrization.** Every semigroup with these invariants is uniquely
\[
S_B=\{0,m\}\cup\{m+b:b\in B\}\cup\{F+1,F+2,\ldots\},
\quad B\subseteq\{1,\ldots,r-1\}.
\]
Indeed \(F<2m\), so sums of two positive members are automatically beyond \(F\); there are no additional closure restrictions. The gaps comprise \(1,\ldots,m-1\) and those among \(m+1,\ldots,m+r\) not selected, yielding the genus formula.

**2. Minimal generators.** For residue \(i\) modulo \(m\), \(1\le i<m\), the minimal member of \(S_B\) in that residue is \(m+i\) if \(i\in B\) or \(i>r\), and \(2m+i\) otherwise. The former are indecomposable since they lie below \(2m\). The latter satisfy \(2m+i<3m\) and can decompose only as \((m+a)+(m+b)\) with \(a,b\in B\) and \(a+b=i\); decomposing as \(m+(m+i)\) is excluded because \(i\notin B\). Thus \(e=m-|\{i\le r:i\notin B,\ i\in B+B\}|\). Separating the special residue \(i=1\), which is never in \(B+B\), yields (1) and the formula for \(e\). No generators can be hidden above the least member of each residue class: any larger member is that least member plus a positive multiple of \(m\).

**3. Exact first moment.** In a uniform subset \(B\), the distinct summand pairs for \(i\) form a matching. Write \(a=3/4\). The probability that \(i\notin B+B\) is \(a^{\lfloor(i-1)/2\rfloor}\) for odd \(i\), and \(a^{i/2-1}/2\) for even \(i\), because the diagonal summand must also be absent. If \(i<r\), the further requirement \(i\notin B\) gives an independent factor \(1/2\); at \(i=r\), this factor is absent. Summing over \(2\le i\le r\) gives
\[
\mathbb E U_r=\frac52-\begin{cases}2a^{r/2-1}&r\text{ even},\\ \frac32a^{(r-3)/2}&r\text{ odd}.\end{cases}
\]
Since \(\mathbb E|B|=(r-1)/2\) and \(\mathbb P(1\in B)=1/2\), this proves (2).

**4. Fixed-genus coefficient.** Condition on \(|B|=k\). For each \(i\), the number of admissible \(k\)-subsets with \(i\notin B\) and \(i\notin B+B\) is the coefficient in (3): there are \(h_i\) disjoint two-vertex summand pairs (each contributes \(1+2t\)), one forbidden diagonal vertex when \(i\) is even, an additional forbidden vertex at \(i\) when \(i<r\), and all remaining selectable vertices contribute \(1+t\). Dividing by \(\binom nk\), summing, and using \(\mathbb E[\mathbf1_{\{1\in B\}}\mid |B|=k]=k/n\) proves (3).

**5. Boundary limit.** For \(i\ge2\) let \(I_i\) be the indicator in (4). The matching calculation shows \(\sum_i\mathbb E I_i<\infty\), hence only finitely many \(I_i\) are nonzero almost surely. More precisely,
\[
\sum_{i=2}^\infty\mathbb E I_i=\sum_{j\ge1}\tfrac14a^{j-1}+\sum_{j\ge1}\tfrac12a^j=\tfrac52.
\]
Therefore \(\mathbb EW=5/2-1/2=2\). Couple \(B=B_\infty\cap\{1,\ldots,r-1\}\). All indicators for \(i<r\) agree exactly between the finite and infinite models. The possible discrepancy at \(i=r\) has probability at most \(\tfrac12\mathbb P(r\notin B_\infty+B_\infty)\), and the expected number of discrepancies at indices \(i>r\) is bounded by the geometric tail of the preceding probabilities. Markov's inequality therefore yields (5). The law is nondegenerate: if the first two Bernoulli bits are absent, then the summand at \(i=2\) is present in \(W\) and \(W\ge1\). Conversely, force the first \(L\) bits present. Every integer from \(2\) through \(2L\) then either belongs to \(B_\infty\) or to \(B_\infty+B_\infty\). By monotonicity of the remaining missing-sum events and the exponentially small tail expectation, the event \(W=-1\) has strictly positive probability for sufficiently large \(L\).

**6. Gaussian marginal limit.** Equation (1) yields \(e=m-r+1+|B|+O_{\mathbb P}(1)\). The error is tight because \(\mathbb E U_r\le5/2\). The binomial variable \(|B|\sim\operatorname{Bin}(r-1,1/2)\) obeys the ordinary central limit theorem. Its centering differs from \(m-r/2\) only by a bounded constant. Slutsky's theorem proves (6).

## Verification

A standalone standard-library checker exhausts all \(2^{r-1}\) parameter subsets for \(2\le r\le10\), independently constructs each cofinite semigroup, tests its minimal generators by direct decomposition, and compares the predicted embedding dimension, exact mean (2), and every genus-conditioned coefficient formula (3). The checker prints `SHORT_CONDUCTOR_EMBEDDING_OK` upon successful completion. Finite checks support the algebra; the infinite limit laws follow from the proof rather than from enumeration.

## Relationship to prior work

Bras-Amorós and Torra (2026), *Multiparameter counting of numerical semigroups by Frobenius number, genus, and multiplicity* (arXiv:2611.11559v1), count the \((F,m,g)\) families and derive recurrences. The present statement additionally studies the **embedding dimension**, gives explicit conditional first moments within a fixed genus, and identifies a joint boundary distribution. García-García, Marín-Aragón, Moreno-Frías, Rosales, and Vigneron-Tenorio (2017), *Semigroups with fixed multiplicity and embedding dimension* (arXiv:1710.03523), give a more general algorithmic enumeration rather than the displayed closed conditional and limiting formulas. Sean Li (2022), *Counting numerical semigroups by Frobenius number, multiplicity, and depth* (arXiv:2208.14587), and Singhal (2022) study total counts and maximal embedding dimension, not the full embedding-dimension law. Moreno-Frías and Rosales (2024/2025), *The ratio-covariety of numerical semigroups having maximal embedding dimension with fixed multiplicity and Frobenius number*, classify the **maximal** case via algorithms, not the whole joint distribution.

The Boolean presentation alone and the general properties of the Apéry set are standard and not claimed as new. The contribution assessed here is the **joint finite and limiting quantitative statement**, not its elementary parametrization or the abstract central limit theorem. A complete historical novelty assertion remains subject to the literature coverage described in the accompanying review.

## Limitations

Only the depth-two domain \(m< F <2m\) with \(F=m+r\) and \(r\ge2\) is covered. The genus-conditioned statistic is a coefficient formula, not a closed one-line polynomial for every genus. The boundary random variable (4) is specified via a rapidly convergent Bernoulli construction, not by a closed probability generating function. Numerical enumeration is not a proof of the asymptotics. Historical priority is provisional; no independent mathematical audit has been performed.

## References

1. M. Bras-Amorós and V. Torra, *Multiparameter counting of numerical semigroups by Frobenius number, genus, and multiplicity*, arXiv:2611.11559v1 (first public 2026-11-08), https://arxiv.org/abs/2611.11559.
2. J. I. García-García et al., *Semigroups with fixed multiplicity and embedding dimension*, arXiv:1710.03523 (2017), https://arxiv.org/abs/1710.03523.
3. S. Li, *Counting numerical semigroups by Frobenius number, multiplicity, and depth*, arXiv:2208.14587 (2022), https://arxiv.org/abs/2208.14587.
4. M. A. Moreno-Frías and J. C. Rosales, *The ratio-covariety of numerical semigroups having maximal embedding dimension with fixed multiplicity and Frobenius number*, International Electronic Journal of Algebra 38 (2025), 12–28; first online 2024-10-30, https://doi.org/10.24330/ieja.1575996.
5. D. Singhal, *Distribution of genus among numerical semigroups with fixed Frobenius number*, Semigroup Forum (2022), https://doi.org/10.1007/s00233-022-10282-6.
