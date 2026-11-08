# Poisson cross-orientations and the first rank-three probability gap in sparsely marked tournaments

## Finding
Fix a sequence of integers \(n\to\infty\) and \(1\le k_n<n\) for which
\[
k_n\to\infty,\qquad (n-k_n)2^{-k_n}\to\lambda\in(0,\infty).
\]
Choose a uniform labelled tournament on \([n]\), and independently choose a uniform \(k_n\)-element subset \(P\) as the interpretation of a unary predicate. The language has just equality, the tournament arc relation \(R\), and \(P\). Define the two disjoint classes of **unmarked extreme vertices**
\[
A_n=\{x\notin P:\forall z\in P,\ R(x,z)\},\qquad
B_n=\{y\notin P:\forall z\in P,\ R(z,y)\},
\]
and let \(H_n\) count the arcs from \(A_n\) to \(B_n\).

**Single theorem (three linked conclusions).** First, the vector \((|A_n|,|B_n|,H_n)\) converges in distribution to \((A,B,H)\), where \(A,B\) are independent \(\operatorname{Poisson}(\lambda)\) variables and, conditionally on them, \(H\sim\operatorname{Binomial}(AB,1/2)\). In particular, for \(s,t,u\in[0,1]\),
\[
\mathbb E[s^At^Bu^H]=e^{-2\lambda}\sum_{a,b\ge0}\frac{\lambda^{a+b}s^at^b}{a!b!}\left(\frac{1+u}{2}\right)^{ab}.
\]
Second, on the subsequence \(n=2^m\), \(k_n=m\), all limiting probabilities of sentences of first-order quantifier rank at most two form **exactly twelve values**:
\[
\mathcal L_2=\{a q^2+bq(1-q)+c(1-q)^2:\ a,c\in\{0,1\},\ b\in\{0,1,2\}\},\qquad q=e^{-1}.
\]
Third, the rank-three sentence
\[
\begin{aligned}
\chi:=\exists x\exists y\big[&x\ne y\land\neg P(x)\land\neg P(y)\land R(x,y)\\
&\land\forall z\big(P(z)\to(R(x,z)\land R(z,y))\big)\big]
\end{aligned}
\]
has, on the same subsequence, limiting probability
\[
h(1)=1-e^{-2}\sum_{a\ge0}\frac{e^{2^{-a}}}{a!},
\quad\text{with}\quad q(1-q)<h(1)<q.
\]
The open interval between \(q(1-q)\) and \(q\) contains **no rank-two limiting probability**. Thus \(\chi\) gives a strict, sharp passage from rank two to rank three for limiting probabilities in this fixed two-symbol relational signature.

## Assumptions and scope
A tournament means a finite irreflexive orientation of every unordered pair of distinct vertices, with each direction chosen independently with probability \(1/2\). The marked set has **fixed cardinality**, chosen uniformly and independently of the arcs; it is not an independent Bernoulli coloring. Quantifier rank is ordinary first-order nesting depth (all Boolean connectives and negations have rank zero). The comparison is for nonempty finite structures with one unary predicate and one binary tournament relation. All limits keep \(\lambda\) fixed and positive; only the stated dyadic subsequence is used for the twelve-value and rank-gap assertions.

## Proof
**1. Exact finite conditional law.** By relabelling, take \(P=[k]\) and \(N=n-k\). For each \(v\notin P\), the \(k\) arcs between \(v\) and \(P\) are an independent fair bit vector. Exactly one vector makes \(v\in A_n\), exactly one makes \(v\in B_n\), and these are disjoint because \(k\ge1\). Their common probability is \(t=2^{-k}\). Distinct unmarked vertices use disjoint sets of arc variables. Hence \((|A_n|,|B_n|,N-|A_n|-|B_n|)\) is multinomial with probabilities \((t,t,1-2t)\). All arcs between unmarked vertices are independent of this multinomial classification. In particular, conditional on the two exceptional classes, the \(|A_n||B_n|\) possible cross-arcs from \(A_n\) to \(B_n\) are independent fair bits. Thus, for \(a+b\le N\), \(0\le h\le ab\), the **exact** law is
\[
\Pr(|A_n|=a,|B_n|=b,H_n=h)
=\frac{N!}{a!b!(N-a-b)!}t^{a+b}(1-2t)^{N-a-b}
\binom{ab}{h}2^{-ab}.
\]
It also follows exactly that \(\chi\) holds if and only if \(H_n>0\). For \(k=1\), the third multinomial probability vanishes; the same formula still holds.

**2. Joint limit, including orientations.** The bivariate probability generating function of the first two counts is
\[
\bigl(1+t(s-1)+t(v-1)\bigr)^N
\longrightarrow e^{\lambda(s-1)+\lambda(v-1)},
\]
so the counts converge to independent Poisson variables. The conditional binomial law is the same stochastic kernel at finite and infinite sizes. Since the count pair is tight, this kernel preserves convergence of the joint distribution, proving the first assertion. Equivalently, the displayed triple generating function follows by summing the limiting count probabilities against the binomial kernel. The standard Poissonization coupling gives total-variation error \(O(Nt^2)\) relative to the same kernel driven by two independent Poisson counts of mean \(Nt\); no rate in \(|Nt-\lambda|\) is asserted.

**3. Complete rank-two profile classification.** For any vertex in a finite colored tournament, its one-neighbor profile consists of its own unary color and, for each of the two colors, whether it has an incoming and an outgoing neighbor of that color. Two such tournaments agree on **all sentences of rank at most two** if and only if they realize the same set of these profiles. Indeed, in a two-round Ehrenfeucht–Fraïssé game the first chosen vertex can be matched precisely when a vertex of identical profile exists; the second response is then guaranteed by equality/color/orientation of the corresponding neighbor. Conversely, any unmatched profile lets Spoiler first choose that vertex and then use a missing neighbor type to win. This also shows every profile-existence test has a rank-two definition, by one outer existential quantifier and Boolean combinations of one inner existential or universal quantifier.

We next show that, with probability \(1-o(1)\), exactly two profiles are always present and only two optional profiles remain. The two always-present profiles are the normal marked and normal unmarked vertices, each having incoming and outgoing neighbors in **both** color classes. The two optional profiles are the unmarked \(A_n\)- and \(B_n\)-vertices, missing respectively all marked in-neighbors and all marked out-neighbors.

For marked vertices, a union bound gives probability at most \(2k2^{-(k-1)}\) that some one lacks either orientation toward the other marked vertices, and at most \(2k2^{-N}\) for the unmarked vertices. For all unmarked vertices, the failure of either direction toward other unmarked vertices has probability at most \(2N2^{-(N-1)}\). Each unmarked vertex is normal toward the marked class except with probability \(2t\); the number of such normal vertices is \(\operatorname{Binomial}(N,1-2t)\), so it is nonzero with probability \(1-o(1)\). All these bounds vanish because \(k\to\infty\), \(N\to\infty\) and \(Nt\to\lambda\).

It follows that, outside an event of probability \(o(1)\), the complete rank-two theory depends solely on the two bits \(1_{|A_n|>0}\) and \(1_{|B_n|>0}\). Conversely, both bits are individually defined by the rank-two sentences
\[
\alpha=\exists x\big[\neg P(x)\land\forall z(P(z)\to R(x,z))\big],
\qquad
\beta=\exists y\big[\neg P(y)\land\forall z(P(z)\to R(z,y))\big].
\]
Every Boolean function of these two bits is definable by a rank-two sentence. At \(\lambda=1\), the two bits tend to independent Bernoulli variables with absence probability \(q=e^{-1}\). The four atomic event probabilities are \(q^2,q(1-q),q(1-q),(1-q)^2\); their subset sums are precisely the twelve values displayed. They are all distinct: the coefficient map from \((a,b,c)\) to the polynomial in \(q\) is injective, and \(e^{-1}\) is transcendental.

**4. Rank-three separation by a strict probability gap.** Given the limiting counts \(A,B\), the conditional probability \(H=0\) is \(2^{-AB}\). Consequently
\[
\Pr(H>0)=1-\mathbb E[2^{-AB}]
=1-e^{-2\lambda}\sum_{a\ge0}\frac{\lambda^a}{a!}e^{\lambda2^{-a}}.
\]
At \(\lambda=1\), let \(q=e^{-1}\). Since \(\Pr(A=B=1)=q^2\) and \(\Pr(A,B\ge1)=(1-q)^2\), on the event \(A=B=1\) the success chance is \(1/2\), while on every other event with \(A,B\ge1\) it is between \(3/4\) and \(1\). Thus
\[
\frac34(1-q)^2-\frac14q^2
\ \le\ h(1)\ \le\ (1-q)^2-\frac12q^2.
\]
The elementary bounds \(8/3<e<11/4\) yield \(4/11<q<3/8\). Substitution makes the displayed lower bound strictly larger than \(q(1-q)\) and the displayed upper bound strictly smaller than \(q\). The twelve rank-two limits have no member in \((q(1-q),q)\): their first four ordered values are \(0,q^2,q(1-q),q\), and every subset involving the atom \((1-q)^2\) is larger than \(q\), while other subsets without it are \(0,q^2,q(1-q),q,2q(1-q),q^2+2q(1-q)\), with the last two exceeding \(q\). This proves the sharp rank gap. Since \(\chi\) has precisely three nested quantifiers, it cannot be equivalent on all finite colored tournaments to a rank-two sentence.

## Verification
A standalone Python checker, `checker.py`, independently exhausts every orientation of the labelled tournaments on \(2\) through \(6\) vertices, taking every legal size of the marked set up to isomorphism. It compares the exact multinomial/binomial distribution of \((|A_n|,|B_n|,H_n)\) with empirical exact rational frequencies, and independently evaluates the three-quantifier sentence against the condition \(H_n>0\). The tested code prints `MARKED_TOURNAMENT_EXACT_OK tournament_instances=168146 formula_checks=168146`. An additional independent two-round game test checks 1,098 colored tournaments through four worlds, grouped into 59 profile signatures, and prints `RANK_TWO_COLORED_TOURNAMENT_EF_OK models=1098 signatures=59 representative_pair_games=6786`. These are finite checks only; Sections 2–4 prove the asymptotic and rank statements.

## Relationship to prior work
Koponen (2026) investigates finite-model properties and necessary structure for random expansions of finite base structures; its Example 2.12 and Remark 2.15 motivate asking for more precise limiting laws, but do not contain the present sparse-color tournament model or its quantified rank gap. Larrauri (2020) proves convergence laws for different sparse random relational models, including variants with unary predicates whose probabilities approach positive constants. Classical random-tournament domination bounds already give the marginal probability that one fixed marked set is dominated by every outside vertex. The present finding does **not** claim that marginal as novel: it concerns a *joint pair of opposite extreme types*, their **induced cross-orientations**, and a complete rank-two spectrum with an explicit rank-three probability outside it. Published work on finite tournament spectra with Bernays–Schönfinkel quantifier prefixes concerns possible finite carrier sizes, not these limit probabilities.

## Limitations
The marked-set size is fixed, the tournament is uniformly oriented, and the asymptotic parameter \(\lambda\) is finite and positive. The full logical classification is at rank two only, not rank three; the rank-three calculation is for the displayed natural witness and the entire joint cross-orientation count. The result makes no claim for independent Bernoulli markings, nonuniform tournaments, or growing quantifier rank. The elementary limit argument does not establish historical priority in all unpublished work or specialized random-tournament literature. Independent audit is not claimed here.

## References
1. Vera Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163, first submitted 2026-10-12, https://arxiv.org/abs/2610.16163.
2. Lázaro Alberto Larrauri, *Probabilities of first-order sentences on sparse random relational structures: An application to definability on random CNF formulas*, *Journal of Logic and Computation* 31 (2021), 444–472; first online 2020-10-27, https://doi.org/10.1093/logcom/exaa061.
3. Fedor Petrov, answer to *Minimum dominating sets in tournaments*, MathOverflow, 2019-01-11, https://mathoverflow.net/questions/286218/minimum-dominating-sets-in-tournaments.
4. R. Fagin, *Probabilities on finite models*, *Journal of Symbolic Logic* 41 (1976), 50–58; classic background on first-order random structures, not an asserted source for the present theorem.
