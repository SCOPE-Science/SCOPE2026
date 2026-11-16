# Sharp Fourier gaps and square resonances in fixed-excess bipartite connected subgraphs

## Finding
Fix integers \(n\ge2\) and \(0\le k\le n-1\). Let \(K_{2,n}\) be the labelled complete bipartite graph with hubs \(u,v\) and right vertices \(w_1,\ldots,w_n\). Let \(\mathcal C_{n,k}\subseteq\mathbb F_2^{2n}\) comprise the edge-incidence vectors of **connected spanning** subgraphs with exactly \(n+1+k\) edges, equivalently cyclomatic excess \(k\). Define their unnormalized Walsh coefficients by
\[
W_{n,k}(b)=\sum_{H\in\mathcal C_{n,k}}(-1)^{\langle b,\mathbf1_H\rangle}.
\]
Write \(a_i=(-1)^{b_{uw_i}}\), \(c_i=(-1)^{b_{vw_i}}\); let \(t\) be the number of indices where \(a_i=-c_i\), and among the other \(q=n-t\) indices let \(j\) count those with \(a_i=c_i=-1\). For \(0\le r\le q\), define the binary Krawtchouk integer
\[
K_r(j;q)=[z^r](1-z)^j(1+z)^{q-j}=\sum_{h=0}^r(-1)^h\binom jh\binom{q-j}{r-h},
\]
using zero for out-of-range binomial coefficients. Then the **complete all-excess signed Fourier law** is
\[
\boxed{W_{n,k}(b)=\begin{cases}
0,&t>k+1,\\
(-1)^t2^{n-k-1}\bigl(\prod_{i:a_i=c_i}a_i\bigr)K_{k+1-t}(j;n-t),&t\le k+1.
\end{cases}}
\]
Every pair \((t,j)\) with \(0\le t\le n\), \(0\le j\le n-t\) occurs at exactly \(\binom nt2^t\binom{n-t}j\) frequencies. In particular the exact convolution rank is the explicitly computable finite integer
\[
R_{n,k}=\sum_{t=0}^{k+1}\binom nt2^t\sum_{j=0}^{n-t}\binom{n-t}j\mathbf1_{\{K_{k+1-t}(j;n-t)\ne0\}}.
\]
The smallest **positive absolute** multiplier and the largest one are, sharply,
\[
\boxed{\sigma_{n,k}=2^{n-k-1},\qquad \max_b|W_{n,k}(b)|=\binom n{k+1}2^{n-k-1}.}
\]
Thus the unnormalized XOR convolution by \(\mathbf1_{\mathcal C_{n,k}}\) has exact Moore--Penrose inverse norm \(2^{k+1-n}\) in \(\ell^2\), and the sharp condition number on its range is \(\binom n{k+1}\). These operator statements hold even when the convolution is singular.

For the first positive excess \(k=1\), put \(s=\lfloor\sqrt n\rfloor\). The rank specializes to the closed formula
\[
\boxed{R_{n,1}=2^n\left(1+n+\binom n2\right)
-\mathbf1_{\{n\text{ odd}\}}\,2n\binom{n-1}{\lfloor(n-1)/2\rfloor}
-\mathbf1_{\{n=s^2\}}\,2\binom n{\lfloor(n-s)/2\rfloor}.}
\]
The two separate extra nullity resonances are an odd-length cancellation at \(t=1\) and a perfect-square cancellation at \(t=0\), beyond the universal \(t\ge3\) zeros. This explicit square resonance is not present in the spanning-tree case \(k=0\).

## Assumptions and scope
All graphs are simple, labelled, spanning subgraphs of \(K_{2,n}\); every vertex is retained. Every edge-mask character is considered, with the **unnormalized** Walsh sum. The cycle rank is \(|E(H)|-|V(H)|+1=k\) for connected graphs. The ambient group \(\mathbb F_2^{2n}\) has cardinality \(2^{2n}\). Fourier characters simultaneously diagonalize the operator \((C_{n,k}f)(x)=\sum_{h\in\mathcal C_{n,k}}f(x+h)\) on counting-measure \(\ell^2\). A null eigenvalue is omitted from the positive condition number and Moore--Penrose inverse norm. The formula for \(k=0\) is included to show continuity with the previously studied tree slice, not claimed as a new tree result.

## Proof
**Connected subgraph parametrization.** Every right vertex has degree one or two. Connectedness requires at least one right vertex with degree two: otherwise the hubs are disconnected. Conversely, if every right vertex has degree at least one and some vertex has degree two, every vertex lies in the same component as both hubs. The total number of edges equals \(n+d\), with \(d\) the number of two-edge right vertices. Hence \(\mathcal C_{n,k}\) consists exactly of choosing \(k+1\) two-edge columns and one of the two possible single edges in each of the remaining \(n-k-1\) columns. Its cardinality is \(\binom n{k+1}2^{n-k-1}\).

**Fourier coefficient.** For a chosen doubled-column set \(D\subseteq[n]\), \(|D|=k+1\), the total signed weight of its allowable singly occupied complementary columns is
\[
\left(\prod_{i\in D}a_ic_i\right)\prod_{i\notin D}(a_i+c_i).
\]
Therefore \(W_{n,k}(b)\) is the sum of these products over all \(D\). If \(a_i=-c_i\), the factor \(a_i+c_i\) is zero, so every such index must lie in \(D\): when \(t>k+1\) the coefficient vanishes. When \(t\le k+1\), all opposed indices contribute \(a_ic_i=-1\). Let \(A\) be the set of the \(n-t\) agreeing indices, and set \(s_i=a_i=c_i\) there. To complete \(D\), choose \(r=k+1-t\) indices from \(A\) to double. Each remaining \(i\in A\setminus D\) contributes \(2s_i\), and each doubled \(i\in A\cap D\) contributes \(1\). Thus the signed sum is
\[
(-1)^t2^{n-k-1}\left(\prod_{i\in A}s_i\right)
\sum_{\substack{B\subseteq A\\|B|=r}}\prod_{i\in B}s_i.
\]
The last sum is the coefficient of \(z^r\) in \(\prod_{i\in A}(1+s_i z)=(1-z)^j(1+z)^{n-t-j}\), proving the boxed formula without asymptotic or probabilistic assumptions.

**Multiplicities and exact rank.** Choose the \(t\) opposed columns in \(\binom nt\) ways, and choose which of the two signs is negative in each opposed column in \(2^t\) ways. Among the \(n-t\) agreeing columns select the \(j\) negative signs in \(\binom{n-t}j\) ways. There are no other independent parameters affecting whether \(W\) vanishes, so the multiplicity and rank formula follow. This sums over all \(2^{2n}\) characters when the zero strata are included.

**Sharp spectral bounds.** Every nonzero integer Krawtchouk value has absolute value at least one, so \(|W|\ge2^{n-k-1}\). To attain equality, choose exactly \(t=k+1\) opposed columns; then \(r=0\) and \(K_0(j;n-k-1)=1\). Triangle inequality bounds \(|W(b)|\) by the number of subgraphs \(\binom n{k+1}2^{n-k-1}\), with equality at the zero frequency. The Fourier diagonalization of XOR convolution gives the exact pseudoinverse norm and positive condition number.

**Unicyclic resonance.** Set \(k=1\). For \(t=2\), \(r=0\), so all \(\binom n2 2^n\) such frequencies have nonzero multiplier. For \(t=1\), \(r=1\), hence \(K_1(j;n-1)=n-1-2j\): zeros occur exactly if \(n\) is odd, when \(j=(n-1)/2\). Their multiplicity is \(\binom n1 2^1\binom{n-1}{\lfloor(n-1)/2\rfloor}\). For \(t=0\), \(r=2\), and
\[
K_2(j;n)=\frac{(n-2j)^2-n}{2}.
\]
Its integer zeros occur exactly if \(n=s^2\) is a perfect square, and then at the two distinct integer values \(j=(n\pm s)/2\), since \(n\ge2\). The combined binomial multiplicity is \(2\binom n{(n-s)/2}\). For \(t\ge3\) all coefficients vanish by the main formula. Subtracting these disjoint extra-zero counts from the count \(2^n\sum_{t=0}^2\binom nt\) of frequencies with \(t\le2\) proves the claimed unicyclic rank.

## Verification
The self-contained exact-integer program `checks/check_cyclomatic.py` independently generates every edge mask of every connected fixed-excess spanning subgraph of \(K_{2,n}\) for \(2\le n\le8\) by graph-union connectivity testing. It computes complete Walsh--Hadamard transforms (not by using the polynomial formula), then compares **all 669,920 coefficients** across all \((n,k)\) to the predicted integers. It additionally verifies the exact subgraph counts, Parseval identity, sharp minimum/maximum spectral magnitudes and the closed unicyclic rank formula, including the square exception at \(n=4\). Run `python3 checks/check_cyclomatic.py`. Success ends with `CONNECTED_FIXED_EXCESS_KRAWTCHOUK_PASS coefficients= 669920`.

## Relationship to prior work
The previously published result *Complete Walsh spectrum and sharp Fourier projection norms for the spanning trees of \(K_{2,n}\)* gives the tree slice \(k=0\) and its endpoint Fourier-projection norms. It does **not** imply the square-root condition \(K_2(j;n)=0\) for the distinct unicyclic slice or establish the sharp all-excess spectral-gap hierarchy. The present theorem explicitly includes that classical/tree case without claiming it is new.

Coleman's *On Krawtchouk polynomials* develops the standard binary Krawtchouk polynomials, their generating functions and real-root structure independently of connected-subgraph Fourier analysis. The new point here is a complete graph-incidence Walsh identification, a uniform sharp **nonzero** spectral gap, and the exact odd/square extra-nullity formula. Dong and Ge count **trees** in complete bipartite graphs containing a prescribed forest; their theorem does not enumerate unicyclic edge subsets or determine their signed Fourier cancellations. The general XOR-rank/Fourier-sparsity theory of Tsang et al. provides the spectral interpretation but not these graph-specific numerical invariants.

## Limitations
For larger positive excess \(k\ge2\), the exact rank is a finite Krawtchouk-integer-zero sum; no closed form classifying all its integer roots is claimed. The result does not extend the sharp spectral-gap formula to arbitrary \(K_{m,n}\) with \(m\ge3\) or to arbitrary graphs. Specialized literature on multivariate signed reliability polynomials could contain an equivalent expression; the priority comparison is bounded and does not certify uniqueness. No independent mathematical audit has been performed. The finite checker supports, but does not replace, the all-length proof.

## References
1. Rodney Coleman, *On Krawtchouk polynomials*, arXiv:1101.1798, first submitted 2011-01-10. https://arxiv.org/abs/1101.1798
2. *Complete Walsh spectrum and sharp Fourier projection norms for the spanning trees of \(K_{2,n}\)*, research record `2026/11/8/SCOPE-complete-walsh-spectrum-and-sharp-fourier-projection-norms-for-t--89f45551846c`, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-walsh-spectrum-and-sharp-fourier-projection-norms-for-t--89f45551846c
3. Fengming Dong and Jun Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, arXiv:2103.05294, first submitted 2021-03-09. https://arxiv.org/html/2103.05294v2
4. Hing Yin Tsang, Chung Hoi Wong, Ning Xie and Shengyu Zhang, *Fourier sparsity, spectral norm, and the Log-rank conjecture*, arXiv:1304.1245, first submitted 2013-04-04. https://arxiv.org/html/1304.1245v2
