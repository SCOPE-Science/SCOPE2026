# Sharp total-variation separation of vertex and leaf depths in uniform recursive trees

## Finding
For a uniform recursive tree \(T_n\) on labels \(1,\ldots,n\), with root \(1\) and \(n\ge3\), let \(D_V\) be the depth of a uniform vertex, and let \(D_L\) be the depth obtained by drawing an ordinary uniform tree and then a uniform leaf of that tree. The random choices include the tree. With \(S_n=\sum_{j=3}^{n}B_j\) for independent \(B_j\sim\operatorname{Bernoulli}(1/j)\),

\[
\left|d_{\mathrm{TV}}(\mathcal L(D_V),\mathcal L(D_L))
-\frac12\max_{k\in\mathbb Z}\Pr(S_n=k)\right|
\le\frac{1}{2\sqrt{3n}}.
\]

In particular,
\[
d_{\mathrm{TV}}(\mathcal L(D_V),\mathcal L(D_L))
\sim\frac{1}{2\sqrt{2\pi\log n}}\quad(n\to\infty).
\]

There is also an exact finite-size explanation: if a tree is instead chosen with probability proportional to its number of leaves, and then one leaf is sampled uniformly, the resulting depth \(D_L^\dagger\) satisfies
\[
D_V\overset d=S_n+B_2,\qquad D_L^\dagger\overset d=S_n+1,
\qquad d_{\mathrm{TV}}(\mathcal L(D_V),\mathcal L(D_L^\dagger))=\frac12\max_k\Pr(S_n=k),
\]
where \(B_2\sim\operatorname{Bernoulli}(1/2)\) is independent of \(S_n\).

## Assumptions and scope
The tree is rooted at label \(1\). For each integer \(j\ge2\), vertex \(j\) attaches independently to one uniformly chosen parent from \(\{1,\ldots,j-1\}\). A leaf is a vertex of outdegree zero; the root is not a leaf when \(n\ge2\). The sampling rule for \(D_L\) is **uniform tree, then uniform leaf of that tree**, not uniform over all leaf–tree pairs. The size-biased tree law is \(\Pr^\dagger(T)=2|L(T)|\Pr(T)/n\). All distances are edge counts. Total variation uses \(d_{\mathrm{TV}}(P,Q)=\frac12\sum_{k\in\mathbb Z}|P\{k\}-Q\{k\}|\).

## Proof
**1. Vertex-depth product.** Put \(h_j(z)=\mathbb E[z^{\operatorname{depth}(j)}]\) and \(H_j(z)=\sum_{a=1}^{j}h_a(z)\). Independence and uniform parental attachment give \(h_1(z)=1\) and, for \(j\ge2\),
\[
h_j(z)=\frac{zH_{j-1}(z)}{j-1},\qquad
H_j(z)=\left(1+\frac{z}{j-1}\right)H_{j-1}(z).
\]
Thus the probability-generating function for \(D_V\) is
\[
G_n(z)=\frac{H_n(z)}n=\prod_{j=2}^{n}\left(1-\frac1j+\frac zj\right).
\]
It is the product pgf of \(B_2+S_n\), proving the first identity.

**2. A leaf-size-biased depth product.** The event that label \(j\ge2\) remains a leaf depends solely on later choices and is independent of its existing depth. Its probability is \(\prod_{t=j+1}^n(1-1/(t-1))=(j-1)/(n-1)\). In particular, \(\mathbb E|L(T_n)|=\sum_{j=2}^n (j-1)/(n-1)=n/2\). Under leaf-size bias, a leaf–tree pair has mass \(2\Pr(T)/n\). Hence
\[
F_n(z):=\mathbb E[z^{D_L^\dagger}]
=\frac{2z}{n(n-1)}\sum_{m=1}^{n-1}H_m(z).
\]
The recurrence for \(H_m\) gives the telescoping identity
\[
\sum_{m=1}^{n-1}H_m(z)=\frac{n-1}{1+z}H_n(z)
\]
(first for nonnegative real \(z\), then as a polynomial identity after multiplication by \(1+z\)). Consequently,
\[
F_n(z)=\frac{2z}{1+z}G_n(z)
=z\prod_{j=3}^n\left(1-\frac1j+\frac zj\right).
\]
This proves \(D_L^\dagger\overset d=S_n+1\).

**3. An exact distance identity.** Let \(p_k=\Pr(S_n=k)\), with \(p_k=0\) outside its support. The vertex-depth mass at \(k\) is \((p_k+p_{k-1})/2\), while the size-biased leaf-depth mass is \(p_{k-1}\). Therefore
\[
d_{\mathrm{TV}}(D_V,D_L^\dagger)=\frac14\sum_{k\in\mathbb Z}|p_k-p_{k-1}|.
\]
An independent Bernoulli convolution has a log-concave and hence unimodal mass sequence: the base two-point Bernoulli sequence is log-concave, and convolution preserves log-concavity for nonnegative sequences with interval support. For any unimodal finite sequence starting and ending at zero, its total absolute first difference is twice its maximum. This proves the exact half-maximum identity.

**4. Removing size bias.** Let \(L_n=|L(T_n)|\). For \(n\ge2\), adjoining the next vertex increases the leaf count by one exactly when the chosen parent was not a leaf, so
\[
\mathbb E[L_{n+1}\mid L_n]=(1-1/n)L_n+1,
\quad \operatorname{Var}(L_{n+1})=(1-2/n)\operatorname{Var}(L_n)+\frac14,
\]
where the second equation uses \(\mathbb E L_n=n/2\). With \(L_2=1\), it gives \(\operatorname{Var}(L_n)=n/12\) for all \(n\ge3\). Since the two depth experiments only change the tree law, their total variation distance is at most that between the tree laws:
\[
d_{\mathrm{TV}}(D_L,D_L^\dagger)
\le\frac12\mathbb E\left|\frac{2L_n}{n}-1\right|
\le\frac{\sqrt{\operatorname{Var}(L_n)}}n
=\frac{1}{2\sqrt{3n}}.
\]
The reverse triangle inequality for total variation completes the finite-size bound.

**5. Sharp asymptotics.** The variance \(v_n\) of \(S_n\) is \(\sum_{j=3}^n (j-1)/j^2=\log n+O(1)\), and its mean is \(\mu_n=\sum_{j=3}^n1/j\). The centered characteristic function obeys
\[
|\varphi_n(t)|\le\exp(-2v_n\sin^2(t/2))\qquad(-\pi\le t\le\pi).
\]
Near zero, uniformly for \(|t|\le v_n^{-2/5}\), its logarithm is \(-v_nt^2/2+O(v_n|t|^3)\) after removing the mean phase. Fourier inversion, splitting at this small interval and bounding the complement by the displayed exponential estimate, gives the uniform local limit estimate
\[
\sup_{k\in\mathbb Z}\left|\sqrt{v_n}\Pr(S_n=k)-\frac1{\sqrt{2\pi}}
\exp\left(-\frac{(k-\mu_n)^2}{2v_n}\right)\right|\longrightarrow0.
\]
An integer lies within \(1/2\) of \(\mu_n\), hence \(\max_kp_k\sim(2\pi\log n)^{-1/2}\). The size-bias error \(O(n^{-1/2})\) is negligible compared with \((\log n)^{-1/2}\), completing the claim.

## Verification
The accompanying standalone `checker.py` enumerates every recursive tree on \(2\le n\le8\) labels and independently computes rational laws for ordinary-vertex, ordinary-uniform-leaf and size-biased-leaf depths. It also checks the exact Bernoulli decomposition, the exact total-variation identity, the leaf-count moments and finite-size error inequality; it performs separate numerical local-limit sanity tests for \(n=100,1000,10000\). It passed 99 assertions. Such finite enumeration is corroborative, not a proof of the all-size statements.

## Relationship to prior work
Lundblad and Wagner (2026) compare **tree-wise average depths** of vertices and leaves; their July 13 AofA paper precedes their November 12 expanded arXiv version. The present result compares **annealed depth laws** in total variation, distinguishes ordinary-leaf and leaf-size-biased sampling, and gives the exact leading rate. Panholzer–Prodinger (2007) and Elizalde (2024) address depths of labelled or indexed individual nodes in increasing/tree families; the latter full text was unavailable for definitive whole-document comparison. An existing published recursive-tree result concerns Gaussian fluctuations of a tree-wise mean-depth difference, not the distribution-level total-variation constant derived here.

## Limitations
The precise asymptotic applies only to uniform random recursive trees and ordinary unconditional sampling, not to every realization of the tree or to other increasing-tree models. The finite-sample half-mode identity pertains to **leaf-size-biased** tree sampling; for ordinary tree-first uniform-leaf sampling it is only accurate to the specified error. Neither an exact finite ordinary-leaf pgf nor a quenched total-variation limit is asserted. No claim of exhaustive historical priority is made; inaccessible full text could change the novelty assessment.

## References
1. J. Lundblad and S. Wagner, *Path Length and External Path Length in Random Trees*, LIPIcs AofA 2026, DOI [10.4230/LIPIcs.AofA.2026.2](https://doi.org/10.4230/LIPIcs.AofA.2026.2), publicly released 2026-07-13.
2. J. Lundblad and S. Wagner, *The External Path Length and Terminal Wiener Index in Random Trees*, [arXiv:2611.16674](https://arxiv.org/abs/2611.16674), first version 2026-11-12.
3. A. Panholzer and H. Prodinger, *Level of nodes in increasing trees revisited*, Random Structures & Algorithms 31 (2007), 203–226, DOI [10.1002/rsa.20161](https://doi.org/10.1002/rsa.20161).
4. S. Elizalde, *On individual leaf depths of trees*, Discrete Applied Mathematics 353 (2024), 151–180, DOI [10.1016/j.dam.2024.04.017](https://doi.org/10.1016/j.dam.2024.04.017); [arXiv:2302.05252](https://arxiv.org/abs/2302.05252).
