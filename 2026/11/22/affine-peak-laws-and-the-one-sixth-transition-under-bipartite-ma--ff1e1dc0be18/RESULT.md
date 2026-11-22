# Affine peak laws and the one-sixth transition under bipartite matching deletion

## Finding

Let \(n\ge 2\) and \(0\le m\le n\) be integers. Start from the labelled complete bipartite graph \(K_{n,n}\), and delete any matching of \(m\) edges; denote the resulting graph by \(H_{n,m}\). Give all \(2n\) vertices distinct labels in a uniformly random order. A *peak* is a vertex larger than every one of its graph neighbours, and \(S_{n,m}\) is the number of peaks.

Define, for \(1\le k\le n\),
\[
q_{n,k}=\frac{n}{2n-k}\prod_{j=1}^{k-1}\frac{n-j}{2n-j},\qquad
r_{n,m,k}=\frac{m}{n^3}\bigl(n-k+(2n-1)\mathbf1_{k=1}\bigr).
\]
The empty product is one. Then the **exact all-order probability generating function** is
\[
\boxed{\mathbb E[z^{S_{n,m}}]=\sum_{k=1}^{n}q_{n,k}z^k\bigl(1+(z-1)r_{n,m,k}\bigr).}
\]
In particular, an exact affine deletion law holds at the level of full distributions:
\[
\boxed{\mathcal L(S_{n,m})=\left(1-\frac mn\right)\mathcal L(S_{n,0})+\frac mn\mathcal L(S_{n,n}).}
\]
The right-hand side means a mixture of probability measures, not equality of random variables on a common probability space.

Let \(G\) be the geometric distribution on positive integers with \(\Pr(G=k)=2^{-k}\), and put \(\rho=m/n\). Uniformly over all \(0\le m\le n\), as \(n\to\infty\),
\[
\boxed{d_{\mathrm{TV}}\!\bigl(\mathcal L(S_{n,m}),\mathcal L(G)\bigr)=\frac{c(\rho)}n+O(n^{-2}),\quad
c(\rho)=\begin{cases}(3-\rho)/8,&0\le\rho\le1/6,\\(1+11\rho)/8,&1/6\le\rho\le1.\end{cases}}
\]
Thus the leading total-variation error is uniquely smallest at deletion density \(\rho=1/6\), where it is \(17/(48n)\), even though the limiting law remains geometric for every deletion density. The finite-order mean is
\[
\mathbb E S_{n,m}=\frac{2n}{n+1}+\frac{2m}{n(n+1)}.
\]

## Assumptions and scope

All graphs are simple, finite and undirected. The two vertex shores each have \(n\) distinctly named vertices, and the deleted edges are disjoint. Labels are a uniformly random bijection to \(\{1,\ldots,2n\}\). The peak condition compares only **present** edges. The total-variation convention is \(d_{\mathrm{TV}}(P,Q)=\frac12\sum_k|P(k)-Q(k)|\). The \(O(n^{-2})\) constant is absolute and uniform over integer \(m\in[0,n]\). No independence is asserted among peak indicators.

The related monochrome self-stabilizing \((\Delta+1)\)-colouring process under a random central daemon performs \(2n-S_{n,m}\) recolourings in law, by the reduction of de Panafieu et al. Consequently the exact law also determines the entire distribution of its recolouring count for this graph family.

## Proof

Write the shores as \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), taking missing edges \(a_i b_i\) for \(1\le i\le m\). Reveal the random order of labels from highest to lowest. By shore-exchange symmetry, condition on the first vertex being in \(A\). Let \(L\) be the length of the initial consecutive run of \(A\)-vertices, stopping at the first \(B\)-vertex. All \(L\) initial \(A\)-vertices are peaks. Without any missing edges, no later vertex is a peak.

The finite urn calculation gives \(\Pr(L\ge k)=\prod_{j=1}^{k-1}(n-j)/(2n-j)\); multiplying by the conditional probability \(n/(2n-k)\) that the next vertex comes from \(B\) gives \(\Pr(L=k)=q_{n,k}\), valid also at \(k=n\).

After deletion of a matching, there can be at most one extra peak. An \(A\)-vertex after the initial run can be a peak only if it is matched to the *first* \(B\)-vertex and precedes every remaining \(B\)-vertex. Conditionally on \(L=k\), the first \(B\)-vertex is paired to an \(A\)-vertex outside the initial run with probability \(m(n-k)/n^2\). Such an \(A\)-vertex precedes the other \(n-1\) vertices of \(B\) with probability \(1/n\). Hence the extra-\(A\) event has conditional probability \(m(n-k)/n^3\).

The only possible additional \(B\)-peak is the partner of the globally first \(A\)-vertex. This happens when that top \(A\)-vertex is matched (probability \(m/n\)) and its partner precedes all other \(n-1\) vertices of \(A\) (conditional probability \(1/n\)). Such an event forces \(L=1\), which itself has probability \(n/(2n-1)\). Therefore its conditional probability, given \(L=1\), is \(m(2n-1)/n^3\). The two extra-peak events cannot co-occur: the extra \(A\)-vertex must precede all other \(B\)-vertices, including the potential extra \(B\)-peak, whereas that \(B\)-peak must precede every other \(A\)-vertex. Thus \(S_{n,m}=L+I\), where conditionally on \(L=k\), \(I\) is Bernoulli with success probability \(r_{n,m,k}\). This proves the generating function. Since \(r_{n,m,k}\) is linear in \(m\) and \(q_{n,k}\) does not depend on \(m\), it also proves the exact affine mixture.

For the sharp asymptotic, let \(p_{n,m}(k)=\Pr(S_{n,m}=k)\), with \(q_{n,0}=0\). The exact law reads
\[
p_{n,m}(k)=q_{n,k}(1-r_{n,m,k})+q_{n,k-1}r_{n,m,k-1},
\]
where \(q_{n,k}=0\) outside \(1\le k\le n\). For \(k\le n/2\), uniformly over \(m\), elementary product expansion gives
\[
q_{n,k}=2^{-k}\left(1+\frac{k(3-k)}{4n}+O\left(\frac{(k+1)^4}{n^2}\right)\right).
\]
Indeed, each product factor is \(\frac12(1-j/(2n-j))\), and the first-order expansion of the nonnegative-factor product has an error bounded by a constant times the square of the sum of its factor deficits. Also
\[
r_{n,m,k}=\frac{\rho}{n}(1+2\mathbf1_{k=1})+O\left(\frac{k+1}{n^2}\right).
\]
Therefore for every fixed positive \(k\), and uniformly in \(\rho\in[0,1]\),
\[
p_{n,m}(k)=2^{-k}+\frac{b_k(\rho)}{n}+O\left(\frac{2^{-k}(k+1)^5}{n^2}\right),
\]
with
\[
b_1(\rho)=\frac14-\frac{3\rho}2,\quad
b_2(\rho)=\frac18+\frac{5\rho}4,\quad
b_k(\rho)=2^{-k}\left(\rho+\frac{k(3-k)}4\right)\ (k\ge3).
\]
The estimates are summable: \(\Pr(L\ge k)\le2^{-(k-1)}\), so for \(k>n/2\) the two distributions have exponentially small combined tails. Summing the remainders through \(n/2\) therefore yields \(O(n^{-2})\) in \(\ell^1\), uniformly over \(m\).

For \(0\le\rho\le1\), we have \(b_2>0\), \(b_3\ge0\), \(b_4\le0\), and \(b_k<0\) for \(k\ge5\). Only \(b_1\) changes sign, at \(\rho=1/6\). The coefficient sequence sums to zero (it is the first-order correction to a probability distribution), so half its absolute sum is the sum of its positive terms:
\[
\frac12\sum_{k\ge1}|b_k(\rho)|=b_2(\rho)+b_3(\rho)+\max\{b_1(\rho),0\}=c(\rho).
\]
This proves the uniform sharp total-variation formula and the unique minimum of its piecewise-linear coefficient. The mean follows either by summing the exact distribution or by the vertex-degree peak identity \(\sum_v1/(\deg(v)+1)\).

## Verification

The accompanying standalone file `verify_peak_law.py` uses only Python's standard library. Run `python verify_peak_law.py` to reproduce exact rational computations. It separately enumerates all \((2n)!\) labelled orders for \(n=2,3,4\), and uses a distinct subset dynamic program over all partially exposed vertex sets for all \(m=0,\ldots,n\) at \(n=2,\ldots,6\), plus \((n,m)=(7,3)\). Both agree with the formula. It also checks normalization, means, the affine mixture and numeric first-order total-variation coefficients. In particular \(H_{3,3}\) (the six-cycle) has peak probabilities \((2/15,11/15,2/15)\). These checks are finite corroboration; the unbounded-\(n\) conclusion uses the proof above.

## Relationship to prior work

De Panafieu, Mathieu, Potop-Butucaru and Tixeuil introduce the reduction of monochrome self-stabilizing recolouring to random-order local maxima and derive distributions for paths, cycles and certain random graph models; their Proposition 9 treats independent bipartite Erdős–Rényi edges and their fixed-density limit. It does not give the exact deterministic matching-deleted biclique law, the affine dependence on the number of deleted edges, or the sharp one-sixth total-variation transition. The general peak identity is inherited, not claimed as new.

Burdzy and Pal study uniformly random graph labellings conditioned on few peaks, with geometric results for grids and trees; no equivalent matching-deleted biclique law is identified in the inspected parts of their paper. Baldi, Rinott and Stein's older normal-approximation report concerns graph local maxima generally; its complete text was inaccessible, so it remains a historical-priority uncertainty. Published indexed searches and comparisons of related graph-colouring, FirstFit and matching results did not identify a stronger covering statement; these negative searches cannot establish absolute priority.

## Limitations

The theorem is proved for equal shores and deletion of a matching; it does not cover arbitrary deleted edge sets, unequal shores, nonuniform vertex priorities, or initially multicoloured configurations. The limit is a peak-count limit, not an assertion about the full chronological sequence of recolourings. The leading total-variation coefficient describes asymptotic accuracy, not finite-order monotonicity in the deletion count. No independent review or complete historical-priority certification is claimed.

## References

1. É. de Panafieu, F. Mathieu, M. Potop-Butucaru and S. Tixeuil, *The Exact Stabilization Time of Self-Stabilizing Coloring: Mean, Variance, and Distribution*, arXiv:2611.17989v1, first posted 2026-11-13, https://arxiv.org/abs/2611.17989v1 .
2. K. Burdzy and S. Pal, *Twin peaks*, arXiv:1606.08025, first posted 2016-06-26; *Random Structures & Algorithms* 56 (2020), https://arxiv.org/abs/1606.08025 .
3. P. Baldi, Y. Rinott and C. Stein, *A Normal Approximation for the Number of Local Maxima of a Random Function on a Graph*, Stanford report EFS NSF 306 (1988), https://statistics.stanford.edu/technical-reports/normal-approximation-number-local-maxima-random-function-graph .
