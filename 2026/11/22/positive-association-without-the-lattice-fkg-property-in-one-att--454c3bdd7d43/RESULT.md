# Positive association without the lattice-FKG property in one-attempt antagonistic adsorption

## Finding

In one-attempt, two-species antagonistic random sequential adsorption, a species' occupied-site field is positively associated on **every finite simple graph** at every time, although its probability law need not satisfy the stronger FKG lattice (log-supermodularity) inequality. In fact, the FKG failure first occurs on a **three-vertex graph**, and the triangle is an obstruction for every nondegenerate color bias and every positive observation time.

Let \(G=(V,E)\) be finite. Independently for each vertex \(v\), choose \(U_v\) uniformly from \([0,1]\) and a proposed species \(Y_v\), with \(\Pr(Y_v=A)=p\in(0,1)\) and \(\Pr(Y_v=B)=q=1-p\). At time \(U_v\) the site makes its only proposal: it accepts \(A\) unless a neighbor is already occupied by \(B\), and accepts \(B\) unless a neighbor is already occupied by \(A\). Rejected sites remain empty. Write \(X^A_v(t)\) and \(X^B_v(t)\) for species occupation indicators by time \(t\in[0,1]\).

For any coordinatewise increasing functions \(F,H:\{0,1\}^V\to\mathbb R\),

\[
\operatorname{Cov}(F(X^A(t)),H(X^A(t)))\ge0,\qquad
\operatorname{Cov}(F(X^B(t)),H(X^B(t)))\ge0,
\]

whereas for increasing \(F,H\),

\[
\operatorname{Cov}(F(X^A(t)),H(X^B(t)))\le0.
\]

Thus there is positive *association* within either species and negative cross-species association for increasing observables. These assertions hold for every finite graph, without bipartiteness or degree restrictions.

Let \(\mu_{p,t}\) be the probability law of the exact \(A\)-occupied vertex set on the triangle \(K_3\). For any fixed, distinct vertices labelled \(1,2,3\), one has the **strict reversed FKG minor**

\[
\boxed{
\mu_{p,t}(\{1\})\mu_{p,t}(\{1,2,3\})
-\mu_{p,t}(\{1,2\})\mu_{p,t}(\{1,3\})
=-\frac{p^4(1-p)t^5}{9}\,[3-(p+2)t]<0.
}
\]

This is true for every \(0<p<1\) and \(0<t\le1\). By contrast, every graph with at most two vertices has an FKG (log-supermodular) \(A\)-occupied-set law for all such parameters, so **three is the sharp smallest graph order** for failure. At \(p=1/2\), \(t=1\), the minor equals \(-1/576\).

The failure is not confined to triangles: on the complete graph \(K_n\), at saturation \(t=1\), the exact probability of an \(A\)-occupied set \(S\) is

\[
\mu_{p,1}(S)=
\begin{cases}
q,&S=\varnothing,\\
\frac{|S|}{n}p^{|S|}q^{n-|S|},&S\ne\varnothing.
\end{cases}
\]

For every \(n\ge3\), nonempty \(S\) with \(1\le|S|\le n-2\), and distinct \(i,j\notin S\), the associated lattice minor is exactly

\[
\mu(S)\mu(S\cup\{i,j\})-\mu(S\cup\{i\})\mu(S\cup\{j\})
=-\frac{p^{2|S|+2}q^{2n-2|S|-2}}{n^2}<0.
\]

## Assumptions and scope

Each vertex has exactly one proposed deposition, including if that attempt is rejected. Species labels and times are independent across sites; all clocks are continuous, so ties have probability zero. The graph is finite and simple; isolated vertices are permitted. The time variable \(t\) is the probability-scale uniform proposal time, not an exponential physical time. Species and observation time boundaries \(p\in\{0,1\}\) or \(t=0\) are degenerate and excluded from strict inequalities. A site counted as empty in \(\mu_{p,t}\) may be an unattempted site or a rejected site, and either kind of emptiness is allowed.

Positive association is an inequality for arbitrary pairs of increasing observables of the full Boolean species field. It does **not** assert that the field satisfies the lattice-FKG inequality; the explicit three-vertex example proves the opposite.

## Proof

### 1. A monotone two-clock representation

For each vertex \(v\), independently sample \(E_v^A\sim\operatorname{Exp}(p)\) and \(E_v^B\sim\operatorname{Exp}(q)\). Set \(E_v=\min(E_v^A,E_v^B)\), let the species be the clock that wins, and put \(U_v=1-e^{-E_v}\). Since \(p+q=1\), \(E_v\sim\operatorname{Exp}(1)\), hence \(U_v\) is uniform on \([0,1]\). The winning label is independent of \(U_v\) and is \(A\) with probability \(p\). Different vertices remain independent, proving this representation has exactly the specified deposition law.

Compare two deterministic arrays of potential clock values \((a_v,b_v)\) and \((a'_v,b'_v)\), satisfying \(a'_v\le a_v\) and \(b'_v\ge b_v\) at every vertex. A standard earliest-violation argument proves that at each elapsed exponential time \(s\),

\[
\{v:\text{accepted }A\text{ in the first array by }s\}\subseteq
\{v:\text{accepted }A\text{ in the second array by }s\},
\]

and the accepted-\(B\) inclusion is reversed. Here is the critical step, including the effect of the **one-attempt** rule. Suppose the first violation is an original \(A\) acceptance at vertex \(v\) that is absent from the second array. Its original first clock is \(a_v<b_v\). In the second array \(a'_v\le a_v<b_v\le b'_v\), so the site's proposal is also \(A\) and occurs no later. If rejected there, a \(B\) neighbor was already accepted there; by the earlier-time inclusion this neighbor was also \(B\) in the first array, where it would prevent the supposedly accepted \(A\). This is impossible. For the other type of first violation, a \(B\) is accepted in the second array but absent from the first. Since \(b_v\le b'_v<a'_v\le a_v\), the first array proposed \(B\) no later. Any \(A\) neighbor that rejected it in the first array would remain an \(A\) neighbor in the second array, contradicting acceptance there. Thus neither violation occurs. This argument also covers proposals rejected permanently: it never treats a rejection as an available later attempt.

Consequently \(X^A(t)\) is coordinatewise increasing in the mutually independent variables \((-E_v^A,E_v^B)_{v\in V}\), and \(X^B(t)\) is coordinatewise decreasing in exactly those variables. Harris' product-measure association inequality applied to the two coordinatewise increasing compositions proves both same-color inequalities. Applying it to one increasing and one decreasing composition proves the mixed negative inequality. No FKG condition on the *output law* is used.

### 2. Exact three-vertex obstruction for all observation times

On \(K_3\), the first proposal controls the occupied species: if it is \(A\), later proposed \(A\)'s are all accepted and later proposed \(B\)'s are rejected; the reverse holds if the first proposal is \(B\). The probability \(w_k\) of any **particular** \(A\)-occupied set of size \(k\), for \(k=1,2,3\), can be found by conditioning on its earliest proposal time \(s\):

\[
 w_k=k p^k\int_0^t(t-s)^{k-1}[1-pt-qs]^{3-k}\,ds.
\]

Indeed, its remaining \(k-1\) vertices have \(A\)-proposals in \((s,t]\), while every vertex outside that set either attempts nothing through \(t\), or attempts \(B\) after \(s\). Direct integration gives

\[
\begin{aligned}
 w_1&=\frac{pt}{3}\bigl[3-3(p+1)t+(p^2+p+1)t^2\bigr],\\
 w_2&=\frac{p^2t^2}{3}\bigl[3-(2p+1)t\bigr],\\
 w_3&=p^3t^3,
\end{aligned}
\]

while \(\mu_{p,t}(\varnothing)=q+p(1-t)^3\). An elementary multiplication yields

\[
 w_1w_3-w_2^2=-\frac{p^4qt^5}{9}[3-(p+2)t].
\]

For \(0<p<1\), \(0<t\le1\), its bracket is bounded below by \(q>0\), so the quantity is strictly negative. This contradicts the lattice condition \(\mu(S\cap T)\mu(S\cup T)\ge\mu(S)\mu(T)\) for the sets \(S=\{1,2\}\), \(T=\{1,3\}\), whose intersection is \(\{1\}\) and union is \(\{1,2,3\}\).

### 3. Sharpness of three sites

For two nonadjacent vertices, \(A\)-occupations are independent Bernoulli variables with probability \(pt\), so the lattice condition holds with equality. For a two-vertex edge, symmetry and the same first-proposal argument yield

\[
\begin{aligned}
\mu(\varnothing)&=q+p(1-t)^2,\\
\mu(\{1\})=\mu(\{2\})&=pt[1-(p+1)t/2],\\
\mu(\{1,2\})&=p^2t^2.
\end{aligned}
\]

Its only lattice determinant equals

\[
\mu(\varnothing)\mu(\{1,2\})-\mu(\{1\})\mu(\{2\})
=\frac{p^2qt^3}{4}(4-qt)>0.
\]

A one-vertex graph has no nontrivial lattice inequality. Hence no graph on fewer than three vertices fails FKG, proving minimality.

### 4. Complete-graph family at saturation

On \(K_n\), once the earliest proposal is accepted, only proposals of its same species can subsequently be accepted. For a nonempty set \(S\) of size \(k\) to be the exact \(A\)-occupied set at saturation, all vertices of \(S\) must propose \(A\), all other vertices must propose \(B\), and the first vertex in the uniformly random ordering must be in \(S\). This has probability \((k/n)p^kq^{n-k}\). The empty \(A\)-set occurs precisely when the first proposal is \(B\), with probability \(q\). Substituting four set cardinalities \(k,k+1,k+1,k+2\) gives the stated strictly negative minor \(-p^{2k+2}q^{2n-2k-2}/n^2\).

## Verification

The standalone `CHECK.py` uses only Python's standard library. It enumerates every attempted-site subset, every relative order, and every proposed-color assignment with **exact rational probability weights**, independently of the two-clock proof. It compares those probabilities with the closed three-site formulas at nine rational parameter pairs, the all-size complete-graph formula through five vertices at three biases, and the two-vertex FKG inequality at nine parameter pairs. It also tests the earliest-violation monotonicity prediction across all potential-clock orders and graphs with two or three vertices. On replay, all 297 exact-law assertions and 28,944 one-clock comparisons passed. These finite checks support arithmetic and interpretation; the proofs of the universal inequalities and all-parameter non-FKG classification are the analytic arguments above.

To reproduce: run `python CHECK.py` with Python 3.10 or later from the directory containing this document and the script.

## Relationship to prior work

The one-deposition-per-site antagonistic model and its one-site densities are due to do Amaral and dos Santos (arXiv:2306.09786, first posted June 16, 2023). Their earlier paper arXiv:2210.05627 concerns a single-species, nearest-neighbor-exclusion adsorption process with very different pair correlations. Standard Harris and FKG inequalities are classical, not new contributions here; the new structural content is the specific two-clock monotonic representation for this competitive one-attempt dynamics **together with** its exact, uniform-in-parameters, minimal obstruction to output-measure log-supermodularity.

Related results on one-shot antagonistic adsorption include exact distance-two same-color correlations and cluster laws; their marginal and pairwise formulas do not by themselves imply full association for all increasing observables, nor the three-vertex FKG failure. Results for **repeated-proposal** antagonistic adsorption use a different update rule and are not interchangeable. The comparison is to statements and implications, not merely titles; a full publication-priority survey is outside this result.

## Limitations

This theorem concerns finite graphs and independent, one-time proposals, not repeated attempts, moving particles, or arbitrary spatially correlated clocks. Positive association is weaker than the lattice-FKG condition and cannot be substituted for it in arguments requiring log-supermodularity or monotone conditioning. The strict triangle obstruction requires both species to have positive proposal probability and a positive observation time. The proof contains no claim about the sign of covariances of total occupied-site indicators \(X^A+X^B\), which need not inherit either species' monotonicity. The result does not establish publication priority or independent validation.

## References

1. C. S. do Amaral and D. C. dos Santos, *One-dimensional AB random sequential adsorption with one deposition per site*, arXiv:2306.09786 (first public posting 2023-06-16), https://arxiv.org/abs/2306.09786.
2. C. S. do Amaral and D. C. dos Santos, *Density and correlation in a random sequential adsorption model*, arXiv:2210.05627 (first public posting 2022-10-11), https://arxiv.org/abs/2210.05627.
3. C. M. Fortuin, P. W. Kasteleyn and J. Ginibre, *Correlation inequalities on some partially ordered sets*, Communications in Mathematical Physics **22** (1971), 89–103, https://doi.org/10.1007/BF01651330.
4. T. E. Harris, *A lower bound for the critical probability in a certain percolation process*, Proceedings of the Cambridge Philosophical Society **56** (1960), 13–20.
