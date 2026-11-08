# Parity-universal bipartitions and single-tree distinguishability in walk-redirection growth

## Finding

A broad class of random walk-redirection rules has an exact, graph-structure-independent bipartition-size law. For each integer \(n\ge2\), when every attachment walk traverses an **odd** number of edges,
\[
\Pr\{|A_n|=k\}=\frac{1}{n-1},\qquad 1\le k\le n-1.
\]
When every walk traverses an **even** number of edges,
\[
\Pr\{|A_n|=k\}=\frac{\left\langle {n-1\atop k-1}\right\rangle}{(n-1)!},\qquad 1\le k\le n-1,
\]
where \(\left\langle {m\atop j}\right\rangle\) is the number of permutations of \(m\) elements with exactly \(j\) descents. These formulas do not depend on the precise walk length, choice of neighbors along the walk, or adaptive dependence of these choices on the previously grown tree.

Let \(\mathcal L_n^{\rm odd}\) and \(\mathcal L_n^{\rm even}\) denote the respective induced probability laws on unlabelled, unrooted trees of order \(n\). For all \(n\ge3\),
\[
d_{\rm TV}(\mathcal L_n^{\rm odd},\mathcal L_n^{\rm even})\ge1-\frac{1}{3\sqrt n}-\frac{n^{3/4}+1}{n-1}.
\]
In particular the total-variation distance tends to one, uniformly over all the allowed odd and even attachment-walk rules. A single unlabelled tree therefore permits consistent inference of the attachment-walk parity in this class.

## Assumptions and scope

Begin with \(T_2\), the edge \(\{1,2\}\). For each integer \(n\ge2\), independently of previous randomness, choose a vertex \(V_n\) uniformly from the vertex set of \(T_n\). Conditional on \(T_n,V_n\), let a (possibly non-simple, possibly history-adaptive) nearest-neighbor walk traverse finitely many **actual tree edges**, ending at \(W_n\). Its length can be random and the transition mechanism can depend on the whole history, provided its parity is the same deterministic \(\varepsilon\) at every step. Add vertex \(n+1\) and the edge \(\{n+1,W_n\}\). There are no stationary steps or loop traversals. The growing graph remains a connected simple tree. The odd and even cases are separate classes, not processes randomly mixing the two parities.

Because a tree is bipartite, there is a unique proper two-coloring with vertex \(1\) in class \(A_n\) and vertex \(2\) in class \(B_n\). Write \(a_n=|A_n|\) and \(b_n=|B_n|=n-a_n\). The imbalance \(I_n=|a_n-b_n|\) does not depend on these class labels and is invariant under unrooted tree isomorphism.

## Proof

**Parity reduction.** On a tree every edge traversal reverses color, regardless of the chosen neighbor. When the walk length is odd, \(W_n\) has the opposite color to \(V_n\), so the new leaf has the **same** color as \(V_n\). Hence, conditional on the complete growth history,
\[
\Pr(a_{n+1}=a_n+1\mid\mathcal F_n)=\frac{a_n}{n}.
\]
When the walk length is even, \(W_n\) has the same color as \(V_n\), so the new leaf has the **opposite** color, giving instead
\[
\Pr(a_{n+1}=a_n+1\mid\mathcal F_n)=\frac{n-a_n}{n}.
\]
No geometric or degree-dependent feature of the walk survives in this projection. The initial value is \(a_2=1\).

**Odd case.** The first transition is the classical balanced two-color Pólya urn. Inductively, if \(\Pr(a_n=k)=1/(n-1)\) for all \(1\le k\le n-1\), the mass at \(1\le k\le n\) at time \(n+1\) equals
\[
\frac{k-1}{n}\frac{1}{n-1}+\frac{n-k}{n}\frac{1}{n-1}=\frac1n
\]
for interior \(k\), with the endpoint masses likewise \(1/n\). The displayed algebra is interpreted with absent boundary terms zero. Thus \(a_n\) is discrete uniform on \(\{1,\ldots,n-1\}\).

**Even case.** Put \(p_{n,k}=\Pr(a_n=k)\). The transition above yields
\[
p_{n+1,k}=\frac{k}{n}p_{n,k}+\frac{n-k+1}{n}p_{n,k-1}.
\]
Eulerian numbers \(E(m,j)=\left\langle {m\atop j}\right\rangle\) obey the standard insertion recursion
\[
E(m+1,j)=(j+1)E(m,j)+(m+1-j)E(m,j-1),
\]
with \(E(1,0)=1\) and values outside the descent range zero. Substituting \(p_{n,k}=E(n-1,k-1)/(n-1)!\) into the preceding probability recursion gives the formula at time \(n+1\), proving it for all \(n\).

**Uniform separation without vertex labels.** Define signed imbalance \(D_n=2a_n-n\). In the even case its next increment is \(+1\) with probability \((n-D_n)/(2n)\) and \(-1\) otherwise, so
\[
\mathbb E[D_{n+1}^2\mid D_n]=\left(1-\frac2n\right)D_n^2+1.
\]
Using \(D_2=0\), first \(\mathbb E D_3^2=1\), then induction gives \(\mathbb E D_n^2=n/3\) for every integer \(n\ge3\). For the isomorphism-invariant event
\[
H_n=\{I_n\le n^{3/4}\},
\]
Markov's inequality applied to \(D_n^2\) gives
\[
\Pr_{\rm even}(H_n^c)\le\frac{1}{3\sqrt n}.
\]
In the odd case, \(a_n\) is uniform on \(\{1,\ldots,n-1\}\), and at most \(n^{3/4}+1\) of those integers satisfy \(|2a_n-n|\le n^{3/4}\). Consequently
\[
\Pr_{\rm odd}(H_n)\le\frac{n^{3/4}+1}{n-1}.
\]
By the definition of total variation, its value for the full unlabelled-tree laws is at least the difference of their probabilities of \(H_n\). The two displayed inequalities give the stated uniform lower bound, which converges to one. The test \(H_n\) has the same two error bounds.

## Verification

The standalone exact enumerator `check_parity.py` follows all possible growing labelled tree histories, performs the random-walk transition using rational probabilities, and compares the actual bipartition-size distribution against the two formulas for every \(2\le n\le6\) and each fixed walk length \(0,1,2,3\). It asserts normalization at each stage. Executing `python check_parity.py` reports 612 exact finite-state checks passed. Finite enumeration is a consistency check, not a proof of the universal, infinite-size statement; the latter is given by the parity reduction, recurrences and probability bounds above.

## Relationship to prior work

Hartle, Krapivsky, Redner and Zhang (2026) examine isotropic redirection and leaf-based tree growth, with emphasis on degrees and anomalous core growth. In particular, their one-step isotropic-redirection rule is an odd-walk member of the present family. Addario-Berry and collaborators introduced and studied the random friend tree in a preprint from 2024 (journal version 2026), explicitly discussing attachment after multiple walk steps. Those models and their provenance are prior work, not new here. Pólya and Friedman urn laws and Eulerian recurrences are likewise classical. The contribution evaluated here is the *walk-rule-independent bipartition projection*, its exact parity-classification for growing tree laws and the resulting label-free, quantitatively consistent parity test. Neither of the two inspected tree-growth articles stated a parity-universal bipartition-size theorem or the uniform unlabelled-law separation proved here. Literature and research-record searches cannot conclusively establish global historical priority; older results on bipartitions of random recursive trees, and broader urn descriptions, remain relevant priority risks.

## Limitations

The conclusion applies only when each insertion starts at a uniformly selected existing vertex and every walk in a given model has the same parity. Lazy steps, self-loops, variable parity mixing, different seed trees or nonuniform starting vertices require separate analysis. No assertion is made about a common joint coupling between different walk lengths, individual vertex degree distributions, or total-variation distances between two models with the **same** parity. Prior-work coverage is assessed on available material, not certified exhaustively; the elementary urn descriptions are acknowledged as established mathematics.

## References

1. H. Hartle, P. L. Krapivsky, S. Redner and Y. Zhang, *Anomalous scaling in redirection networks*, arXiv:2604.01540v1, publicly posted 2026-04-02. https://arxiv.org/html/2604.01540v1
2. L. Addario-Berry, S. Briend, L. Devroye, S. Donderwinkel, C. Kerriou and G. Lugosi, *Random Friend Trees*, arXiv:2403.20185, first posted 2024-03-29; journal version *Random Structures & Algorithms* 69 (2026), DOI 10.1002/rsa.70082. https://onlinelibrary.wiley.com/doi/full/10.1002/rsa.70082
3. J. Shi, Q. Yin and W. Miao, *Central Limit Theorem for a Pólya-Friedman Mixed Urn Model*, arXiv:2605.26669 (2026); general mixed-urn context, not a claim of the specific graph projection. https://arxiv.org/abs/2605.26669
4. L. Comtet, *Advanced Combinatorics*, Reidel, 1974; classical Eulerian-number insertion recurrence.
