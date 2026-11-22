# Parity-rigid optimal two-color probing on balanced complete multipartite resolvents

## Finding
Let \(G=K_{m,\ldots,m}\) have \(q\ge3\) nonempty independent parts, each of size \(m\ge2\), let \(L\) be its unweighted combinatorial Laplacian, and put \(B=(\mu I+L)^{-1}\) for any \(\mu>0\). Partition all vertices into **exactly two nonempty classes** and estimate \(\operatorname{tr}B\) by one independent Rademacher quadratic form supported on each class. Among every possible two-class partition, including ones that split graph parts, the complete collection of variance minimizers is as follows.

- If \(q\) is even, every graph part is monochromatic; exactly \(q/2\) parts have each probe color.
- If \(q\) is odd, precisely one graph part is divided as evenly as its size permits, and the other \(q-1\) parts are monochromatic with equally many of each probe color. For even \(m\), the divided part has \(m/2\) vertices of each color; for odd \(m\), its two color counts are \((m-1)/2\) and \((m+1)/2\).

These are **all** minimizers for every finite positive \(\mu\). Define
\[
N=qm,\quad d=(q-1)m,\quad b=\frac{1}{\mu(\mu+N)},\quad
 a=\frac{d}{\mu(\mu+N)(\mu+d)},\quad\epsilon=m\bmod 2.
\]
The minimum variance is
\[
V_*=
\begin{cases}
2q m(m-1)a^2+q(q-2)m^2b^2,&q\ \text{even},\\
\big[(2q-1)m^2-2qm+\epsilon^2\big]a^2+(q-1)^2m^2b^2,&q\ \text{odd}.
\end{cases}
\]
For odd \(q\), the minimum variance among **all assignments that keep each original graph part monochromatic** exceeds \(V_*\) by the strictly positive, exact amount
\[
\boxed{a^2(m^2-\epsilon^2)}.
\]
Thus a two-color stochastic trace estimator of an odd-part complete multipartite resolvent provably must split exactly one graph part to attain its sharp variance, regardless of screening strength.

For instance, on \(K_{2,2,2}\) with \(\mu=1\), one has \(a=4/35\), \(b=1/7\). The optimal coloring (two monochromatic opposite-color parts, one part split \(1+1\)) has variance \(528/1225\). The best coloring which keeps every graph part intact has variance \(592/1225\), so the variance improvement is exactly \(4/37\) of the latter value.

## Assumptions and scope
All \(q\ge3\), \(m\ge2\) are integers and \(\mu>0\) is real. The graph is unweighted and all original parts have the same cardinality. The probes are \(z_C\), with independent equiprobable signs on their respective support classes and zeros elsewhere. The two vectors are independently sampled. The estimator is \(T=z_{C_1}^{\mathsf T}Bz_{C_1}+z_{C_2}^{\mathsf T}Bz_{C_2}\), which is unbiased because each vertex appears in exactly one probe support. The objective is \(\operatorname{Var}(T)\), not total running time, setup cost, or an estimator with correlated, repeated or deterministically chosen probes. All two-color assignments are admissible, not necessarily proper graph colorings.

## Proof
**1. Resolvent structure.** The Laplacian has eigenvalue zero on global constants, eigenvalue \(N\) on the \((q-1)\)-dimensional space of vectors constant on each part and summing to zero, and eigenvalue \(d\) on contrasts within parts. The corresponding orthogonal projectors give
\[
B=\frac1{\mu+d}P_{\mathrm{within}}+\frac1{\mu+N}P_{\mathrm{between}}+\frac1\mu P_{\mathrm{constant}}.
\]
Every distinct pair of vertices in the same original part has resolvent entry \(a\), and every pair in different original parts has entry \(b\). In detail, the latter entry is \(\frac1{N}(\frac1\mu-\frac1{\mu+N})=1/[\mu(\mu+N)]\); the former differs from it by \(-1/[(\mu+N)(\mu+d)]\), giving the stated \(a\). In particular \(0<a<b\), and \(r=a/b=d/(\mu+d)\) lies strictly between zero and one.

**2. Exact partition objective.** Let \(k_i\in\{0,\dots,m\}\) be the number of color-one vertices in original part \(i\), and write \(s_i=2k_i-m\), \(S=\sum_i s_i\), and \(Q=\sum_i s_i^2\). The Rademacher fourth-moment identity gives \(\operatorname{Var}(T)=4\sum_{u<v:\,\mathrm{same\ color}}B_{uv}^2\). Counting the same-color pairs inside a part and between distinct parts gives **exactly**
\[
\operatorname{Var}(T)=a^2\big[q(m^2-2m)+Q\big]
+b^2\big[q(q-1)m^2+S^2-Q\big]. \tag{1}
\]
Thus, after omitting constants and dividing by \(b^2\), it remains to minimize
\[
E(s)=S^2-(1-r^2)Q,\qquad s_i\in\{-m,-m+2,\ldots,m\}.\tag{2}
\]

**3. Even number of graph parts.** Since \(1-r^2>0\), equation (2) implies \(E\ge-(1-r^2)qm^2\). Equality forces \(S=0\) and \(Q=qm^2\). The latter holds exactly when every \(|s_i|=m\), and the former then requires an equal number of full plus and minus graph parts. This is attainable when \(q\) is even, and it characterizes every optimum.

**4. Odd number of graph parts.** Let \(\epsilon\in\{0,1\}\) be the parity of \(m\). Every \(s_i\) has the same parity as \(m\), hence \(|S|\ge\epsilon\). At fixed \(S\), the largest possible \(Q\) over the continuous cube \([-m,m]^q\) occurs with at least \(q-1\) coordinates at the endpoints, by convexity of the squared norm on the fixed-sum section. When \(|S|\le m\) and \(q\) is odd, the \(q-1\) endpoint coordinates must contain equally many \(+m\) and \(-m\) if \(|S|<m\); the remaining coordinate is \(S\). The same bound holds at \(|S|=m\). Therefore \(Q\le(q-1)m^2+S^2\) in this range, so
\[
E(s)\ge-(1-r^2)(q-1)m^2+r^2S^2
\ge -(1-r^2)(q-1)m^2+r^2\epsilon^2.\tag{3}
\]
Both equalities are attained when \(q-1\) parts are monochromatic, half plus and half minus, and the final part has imbalance \(s_i=\pm\epsilon\). Strict positivity of \(r^2\) and \(1-r^2\) forces precisely these equality conditions.

If \(|S|>m\), use \(Q\le qm^2\). The difference between the right side of (2) and the candidate value in (3) is at least
\[
S^2-\epsilon^2-(1-r^2)(m^2-\epsilon^2)
>r^2(m^2-\epsilon^2)>0,
\]
where \(m\ge2\) ensures \(m^2>\epsilon^2\). Thus no missing high-imbalance partition can minimize. This completes the global classification.

**5. Values and whole-part gap.** Substitute \((S^2,Q)=(0,qm^2)\) for even \(q\), or \((S^2,Q)=(\epsilon^2,(q-1)m^2+\epsilon^2)\) for odd \(q\), into (1). For odd \(q\), a whole-part monochromatic assignment has \(Q=qm^2\), and its least possible \(S^2\) is \(m^2\). Its variance minus \(V_*\) is \(b^2r^2(m^2-\epsilon^2)=a^2(m^2-\epsilon^2)\). The strict sign follows from \(\mu>0\) and \(m\ge2\).

## Verification
The independently executable file `verify.py` uses Python 3 standard-library exact fractions. It checks exact inverses of the shifted Laplacians against both off-diagonal classes, enumerates every possible pair of probe-color counts for \(2\le q\le6\), \(1\le m\le4\), for four rational screening strengths, and compares every enumerated optimum with the theorem's predicted classification. It also compares direct inverse-matrix Rademacher variance with formula (1) for a selection of graphs. The completed run passed 109,166 exact-rational assertions. This finite check is supplementary: the universal claim depends on the above inequality proof, not on enumeration.

To reproduce: `python3 verify.py` from the folder containing the file. No third-party dependencies or external data are needed.

## Relationship to prior work
Frommer, Rinelli and Schweitzer (arXiv:2308.07722, Theorem 3.3 and Lemma 3.5) establish the general stochastic-probing variance of a **given partition** and discuss sample allocation and distance-based coloring. That result supplies the variance identity used here but does not itself classify globally optimal two-class partitions of the particular balanced multipartite resolvent family. Switzer and collaborators (arXiv:2106.01275) study trace probing on displaced toroidal lattices, with a different graph structure and optimization target. A previously published exact theorem for complete **bipartite** shifted-Laplacian resolvents establishes a two-class optimum and potential within-side splitting for unequal part sizes; it neither states nor directly entails the odd-\(q\) parity obstruction and all-\(q\) extremizer classification here. The extra comparison requires the multiple-part spectral identity and global fixed-sum analysis, not merely a change of labels.

## Limitations
This is a complete idealized theorem for equal-part complete multipartite graphs, not a runtime claim: on this highly symmetric graph family the trace itself can be evaluated without stochastic probing. It is a diagnostic variance-optimal coloring model for fixed two-solve budgets. The guarantee does not extend as stated to unequal class sizes, nonuniform conductances, alternative matrix functions, varying numbers of samples, or correlated probe designs. Known weighted-MaxCut/Ising ground-state classifications might imply this special case; no such dominating statement was located in the checked sources, but publication priority remains provisional.

## References
1. A. Frommer, M. Rinelli, M. Schweitzer, *Analysis of stochastic probing methods for estimating the trace of functions of sparse symmetric matrices*, arXiv:2308.07722v1, first public 15 August 2023, Sections 2–3, especially Theorem 3.3 and Lemma 3.5. https://arxiv.org/abs/2308.07722
2. H. Switzer, A. Stathopoulos, E. Romero, J. Laeuchli, K. Orginos, *Probing for the Trace Estimation of a Permuted Matrix Inverse Corresponding to a Lattice Displacement*, arXiv:2106.01275v1, first public 2 June 2021, Introduction and Section 2. https://arxiv.org/abs/2106.01275
3. *Sharp two-color stochastic-probing transition on complete bipartite resolvents*, publicly accessible scientific result, 2026, full proof and statement examined. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-two-color-stochastic-probing-transition-on-complete-bipart--1edc2b42b895/RESULT.md
