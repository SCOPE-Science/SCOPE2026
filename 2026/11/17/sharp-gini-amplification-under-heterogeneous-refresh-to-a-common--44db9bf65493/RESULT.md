# Sharp Gini amplification under heterogeneous refresh to a common mean

## Finding

For every integer \(n\ge 2\), let \(J_n f=(n^{-1}\sum_{j=1}^n f_j)\mathbf 1\), let \(a\in[0,1]^n\), and define the positive, unital, one-step averaging operator
\[
(P_a f)_i=(1-a_i)f_i+a_i(J_n f)_i.
\]
For real signals, equip the quotient by constants with complete-pair Gini variation
\[
G_n(f)=\sum_{1\le i<j\le n}|f_i-f_j|.
\]
The exact worst operator seminorm across **all** independent site-refresh probabilities is
\[
\boxed{\displaystyle
\max_{a\in[0,1]^n}\ \sup_{G_n(f)>0}\frac{G_n(P_a f)}{G_n(f)}
=1+\frac{\lfloor(n-2)^2/4\rfloor}{n(n-1)}=:M_n.}
\]
This maximum is attained for every finite \(n\). It equals one exactly in dimensions two and three, is \(13/12\) for four sites, and is strictly greater than one for every \(n\ge4\). Its sharp across-dimension envelope is
\[
\boxed{\displaystyle\sup_{n\ge2}M_n=\frac54,}
\]
which no finite dimension attains.

There is a stronger positive-kernel consequence: for every \(n\ge4\), an averaging operator \(P_a\) with **every matrix entry strictly positive** still amplifies \(G_n\) on some nonconstant signal. Thus strict Doeblin/oscillation contraction does not guarantee one-step Gini contraction. In four dimensions the explicit example below amplifies whenever \(0<\varepsilon<1/13\).

## Assumptions and scope

The state set is \(\{1,\ldots,n\}\), with \(n\) a finite integer at least two. Input signals are arbitrary real column vectors, and the reference mean is the uniform arithmetic mean. Each fixed coefficient \(a_i\) belongs to the **closed** interval \([0,1]\). No rate equality is assumed. The operator is row stochastic, since its matrix is
\[
P_a=I-\operatorname{diag}(a)+\frac1n a\mathbf1^{\mathsf T}.
\]
The single-step norm is on real signals modulo additive constants, not on probability measures or on graph-edge variation. This is not a statement about arbitrary products or powers of distinct averaging operators.

For completeness, for any fixed rate vector \(a\), an exact finite-cut norm formula is available. If \(S\) is a nonempty proper subset, \(k=|S|\), \(m=n-k\), and \(A_S=\sum_{i\in S}a_i\), then
\[
\begin{aligned}
G_n(P_a\mathbf1_S)={}&km-\frac{m^2}{n}A_S-\frac{k^2}{n}A_{S^c}\\
&+\frac mn\sum_{\{i,j\}\subset S}|a_i-a_j|
+\frac kn\sum_{\{i,j\}\subset S^c}|a_i-a_j|,
\end{aligned}
\]
where each unordered pair is counted exactly once. Therefore
\[
\|P_a\|_{G_n\to G_n}=
\max_{\varnothing\ne S\subsetneq\{1,\ldots,n\}}
\frac{G_n(P_a\mathbf1_S)}{|S|(n-|S|)}.
\]
This cut expression is an exact formula, not a requirement to enumerate all real inputs.

## Proof

**Step 1: Binary-cut reduction.** For any linear map \(T\) satisfying \(T\mathbf1=\mathbf1\), and any real \(f\), sort the distinct entries of \(f\) and write the exact positive-layer decomposition
\[
f=c\mathbf1+\sum_{\ell}d_\ell\mathbf1_{S_\ell},\qquad d_\ell>0,
\]
where \(S_\ell\) is the set of coordinates above a successive input level. The sets are nested. Every pairwise difference has consistent sign across these layers, so
\[
G_n(f)=\sum_\ell d_\ell |S_\ell|(n-|S_\ell|).
\]
Since \(G_n\) is a seminorm and \(T\) preserves constants,
\(G_n(Tf)\le\sum_\ell d_\ell G_n(T\mathbf1_{S_\ell})\).
Hence the operator seminorm is exactly the maximum ratio over nontrivial binary cuts, achieved by one of those cuts. This argument also handles repeated input levels.

**Step 2: Reduce refresh probabilities to endpoints.** Fix any cut \(S\). Every output coordinate \((P_a\mathbf1_S)_i\) is affine in the complete rate vector \(a\), so \(a\mapsto G_n(P_a\mathbf1_S)\) is convex. The maximum of a convex function on the cube \([0,1]^n\) occurs at a vertex (iteratively replace each coordinate by an endpoint without decreasing the value). Thus it suffices to take every \(a_i\) equal to zero or one. This step is an exact optimization over the entire cube, not an approximation by binary rates.

**Step 3: Exact three-level count.** With \(k=|S|\), \(m=n-k\), let \(r\) of the \(k\) selected sites and \(s\) of the \(m\) unselected sites refresh completely. The output has \(m-s\) zero entries, \(r+s\) entries equal to \(k/n\), and \(k-r\) entries equal to one. Directly summing the three types of pairwise distances gives the exact identity
\[
\boxed{\displaystyle
G_n(P_a\mathbf1_S)
=km+\frac{k s(m-k-s)+m r(k-m-r)}{n}.}
\]
If \(k\le m\), the \(r\)-term is nonpositive; maximizing sets \(r=0\). The remaining quadratic is maximized by \(s\) as close as possible to \((m-k)/2\), with maximum \(\lfloor(m-k)^2/4\rfloor\). Complementing the input cut gives the symmetric case \(k>m\). Consequently the largest ratio with a fixed cut size \(1\le k\le n/2\), optimized over every rate vector, is
\[
1+\frac{\lfloor(n-2k)^2/4\rfloor}{n(n-k)}.
\]

**Step 4: A singleton always maximizes.** For even \(n=2h\), the nonconstant part of this expression is \((h-k)^2/[n(2h-k)]\), which decreases with integer \(k\in[1,h]\), since the continuously extended function has derivative proportional to \(-(h-k)(3h-k)\). For odd \(n=2h+1\), it is \((h-k)(h-k+1)/[n(2h+1-k)]\); putting \(u=h-k\), the quotient \(u(u+1)/(h+1+u)\) increases with \(u\ge0\). Thus \(k=1\) gives the maximum in both parity cases, proving the displayed formula for \(M_n\).

**Step 5: Attainment, onset, and envelope.** Choose a singleton input \(f=\mathbf1_{\{1\}}\). Refresh exactly \(s=\lfloor(n-2)/2\rfloor\) of the other sites completely, and leave all remaining sites unrefreshed. Steps 3 and 4 give precisely \(G_n(P_a f)=M_nG_n(f)\). For \(n=2,3\) the integer numerator \(\lfloor(n-2)^2/4\rfloor\) vanishes, while it is positive for all \(n\ge4\). Also \(M_n<5/4\) at every finite \(n\), because \((n-2)^2<n(n-1)\) for \(n\ge2\), and \(M_n\to5/4\) as \(n\to\infty\). This proves the sharp limiting envelope.

**Step 6: Strictly positive Markov kernels still amplify.** Fix any \(n\ge4\) and the binary maximizing rate vector \(b\) from Step 5. Choose \(0<\varepsilon<1-M_n^{-1}\) and set \(a=\varepsilon\mathbf1+(1-\varepsilon)b\). Its kernel obeys
\[
P_a=\varepsilon J_n+(1-\varepsilon)P_b.
\]
Because \(J_n f\) is constant,
\[
\frac{G_n(P_a f)}{G_n(f)}=(1-\varepsilon)M_n>1
\]
for the same singleton \(f\). Every entry of \(P_a\) is at least \(\varepsilon/n>0\), so this is a strict Doeblin kernel. In particular, for \(n=4\), choose \(b=(0,1,0,0)\); the ratio is \((1-\varepsilon)13/12>1\) whenever \(0<\varepsilon<1/13\). All assertions follow.

## Verification

The standalone file `verify_refresh_gini.py` uses only Python's standard library and exact rational arithmetic. Run:

```text
python verify_refresh_gini.py
```

It independently evaluates every binary input cut against every binary rate profile in dimensions two through eight, comparing actual output Gini sums with the algebraic three-level identity and the sharp constant. It also checks rational interior rate vectors and signals, the exact singleton extremizers through dimension 400, and strictly positive rate profiles through dimension 100. These finite computations are checks only; the proof above handles every finite dimension and every real input and rate vector.

## Relationship to prior work

Gaubert and Qu develop sharp contraction coefficients for Hopf oscillation and their total-variation duals, including Doeblin–Dobrushin formulas. Their results govern different normed spaces: for every row-stochastic map, oscillation is nonincreasing, while the present theorem shows that complete-pair Gini variation can increase even for an entrywise positive map. The dual total-variation action on measures is not the Gini action on real signals. The published gossip analysis of Boyd, Ghosh, Prabhakar, and Shah emphasizes averaging time and spectral decay for doubly stochastic pairwise update kernels. In contrast, \(P_a\) is doubly stochastic only when all rates agree; the theorem optimizes over its heterogeneous, generally non-doubly-stochastic members.

Related finite-graph Gini norm calculations for normalized heat, lazy walks, and split-graph transitions apply to other operators. In particular, a graph random walk does not reduce to this independently rate-controlled common-mean refresh family by relabeling a graph parameter. The shared binary-cut method does not imply the exact all-rate supremum, finite-size onset, or strict-Doeblin counterexample above.

## Limitations

The exact optimization is for one discrete step with a **uniform** reference mean and rate vector in \([0,1]^n\), and for **unweighted** complete-pair Gini variation. Nothing here establishes the same constant for unequal reset distributions, signed relaxation weights, continuous-time semigroups, nonhomogeneous products, other pair weights, or nonlinear updates. The simple extremizers at zero rates do not themselves produce strictly positive kernels; Step 6 gives separate strictly positive amplifying kernels with a ratio arbitrarily close to the sharp bound but not attaining that rate-closed maximum. Historical priority beyond the inspected literature remains subject to independent evaluation.

## References

1. S. Gaubert and Z. Qu, *Dobrushin ergodicity coefficient for Markov operators on cones, and beyond*, first public arXiv version, 21 February 2013, arXiv:1302.5226, https://arxiv.org/abs/1302.5226.
2. S. Gaubert and Z. Qu, *Dobrushin's ergodicity coefficient for Markov operators on cones*, arXiv:1307.4649, initial public version 17 July 2013, https://arxiv.org/abs/1307.4649.
3. S. Boyd, A. Ghosh, B. Prabhakar, and D. Shah, *Randomized Gossip Algorithms*, IEEE Transactions on Information Theory **52** (2006), 2508–2530, DOI 10.1109/TIT.2006.874516, https://web.stanford.edu/~boyd/papers/pdf/gossip.pdf.
