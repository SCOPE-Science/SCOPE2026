# Poisson–Bernoulli deficiency law for involutive partial star isometries

## Finding
Let \(S_{m+1}=K_{1,m}\) be the metric star with hub \(0\) and \(m\ge 2\) labelled leaves, and let \(\mathcal D_m\) be its inverse monoid of all distance-preserving partial bijections. Call \(f\in\mathcal D_m\) self-inverse when \(f=f^{-1}\) as partial maps. Set
\[
 t_k=\sum_{j=0}^{\lfloor k/2\rfloor}\frac{k!}{2^j j!(k-2j)!}.
\]
The complete domain-rank polynomial of the self-inverse elements is
\[
 F_m(z)=\sum_{\substack{f\in\mathcal D_m\\ f=f^{-1}}}z^{|\operatorname{dom}f|}
 =(1+z)\sum_{k=0}^m\binom mk t_k z^k+m z^2.
\]
Exactly \(m\) self-inverse partial isometries fail to extend to self-inverse full isometries: the swaps of the hub with a single leaf on their two-point domains.

For a uniformly sampled self-inverse \(f\), put \(D_m=m+1-|\operatorname{dom}f|\) and \(r_m=\sqrt{m+1}-1\). Let \(P_m\sim\operatorname{Poisson}(r_m)\) and \(B\sim\operatorname{Bernoulli}(1/2)\) be independent. Then, in total variation,
\[
 d_{\mathrm{TV}}\bigl(\mathcal L(D_m),\mathcal L(P_m+B)\bigr)\longrightarrow0
 \qquad(m\to\infty).
\]
In particular,
\[
 \frac{D_m-\sqrt m}{m^{1/4}}\ \xrightarrow{\mathrm d}\ \mathcal N(0,1).
\]
The total-variation limit is a stronger assertion than this Gaussian consequence.

## Assumptions and scope
The graph has one distinguished hub and at least two leaves. Graph distance is the ordinary shortest-path distance, taking the values zero, one and two. A partial isometry is an injective map between arbitrary vertex subsets preserving all their pairwise distances. The inverse \(f^{-1}\) is the ordinary inverse partial bijection. Domain rank means \(|\operatorname{dom}f|\), not minimal semigroup generating rank. The limit is taken through all integers \(m\ge2\), with no parity restriction.

## Proof
**1. Exact decomposition.** A self-inverse partial injection has equal domain and image and restricts to an involutive permutation on that common subset. If the hub is absent, every partial involution on a subset of the leaves is an isometry. If the hub belongs to the subset and is fixed, arbitrary leaf involutions remain isometries. If the hub is moved, preserving all star distances forces the domain to be exactly \(\{0,i\}\) and the map to transpose \(0\) and \(i\). Indeed, any additional leaf would have distance two from \(i\) before the swap but distance one after it. Thus the self-inverse elements form two disjoint copies of leaf partial involutions, one with the hub fixed and one without the hub, together with precisely \(m\) exceptional edge swaps.

A partial involution on \(k\) specified leaves is an ordinary permutation of order dividing two, and there are \(t_k\) of these. The disjoint decomposition gives the formula for \(F_m(z)\). The two ordinary classes extend by fixing every omitted leaf and the hub, while none of the edge swaps extends, because every full star isometry fixes the unique vertex of degree \(m\) when \(m\ge2\).

**2. Finite deficiency probability-generating function.** Write \(a_m=\sum_{k=0}^m\binom mk t_k\), and let \(U_m\) be the number of omitted leaves in a uniformly selected leaf partial involution. Labelled decomposition into omitted singletons, included fixed singletons and included transpositions gives
\[
 A_m(s):=a_m\,\mathbb E(s^{U_m})
 =m![x^m]\exp\bigl((1+s)x+x^2/2\bigr),
 \qquad a_m=A_m(1).
\]
Consequently the exact deficiency pgf on the star is
\[
 \mathbb E(s^{D_m})=\frac{(1+s)A_m(s)+m s^{m-1}}{2a_m+m}.
\]
Except for a mass \(m/(2a_m+m)\), its distribution is exactly that of \(U_m+B\), where \(B\) is independent and fair. Since \(a_m\ge2^m\), the exceptional mass tends to zero.

**3. Asymptotically Poisson omitted leaves.** Put \(r=r_m\), so \(r^2+2r=m\). Take independent Poisson variables \(X,Y,Z\) with means \(r,r,r^2/2\), respectively, and set \(T=X+Y+2Z\). Conditioning on \(T=m\) gives the exact labelled partial-involution component weights: if \(u\) leaves are omitted, \(v\) are included singleton fixed points and \(w\) are paired in transpositions, the conditional weight is proportional to
\[
 \frac{m!}{u!v!2^w w!},\qquad u+v+2w=m.
\]
Thus \(U_m\) has precisely the law of \(X\mid T=m\).

Let \(W=Y+2Z\). Its mean is \(r+r^2\) and variance is \(r+2r^2\); \(T\) has mean \(m\) and variance \(2r+2r^2\). Both admit a central lattice local limit estimate
\[
 \Pr(W=s)=\frac{1+o(1)}{\sqrt{2\pi(r+2r^2)}}
\quad\text{uniformly for }|s-(r+r^2)|=o(r),
\]
and
\[
 \Pr(T=m)=\frac{1+o(1)}{\sqrt{2\pi(2r+2r^2)}}.
\]
For completeness, these follow by Fourier inversion from the characteristic functions
\[
 \exp\{r(e^{it}-1)+(r^2/2)(e^{2it}-1)\}
\quad\text{and}\quad
 \exp\{2r(e^{it}-1)+(r^2/2)(e^{2it}-1)\}.
\]
On the arc \(|t|\le r^{-3/4}\), Taylor expansion after centering gives the Gaussian integral with error \(O(r^2|t|^3)=O(r^{-1/4})\). Outside the central arc the modulus is bounded by
\(\exp\{r(\cos t-1)+(r^2/2)(\cos2t-1)\}\) (or the same expression with \(2r\) replacing \(r\)); the secondary arc around \(\pi\) has exponentially small size because the singleton Poisson mean tends to infinity. This proves both estimates, including their asserted uniformity in the central displacement.

Poisson concentration gives \(\Pr(|X-r|>r^{2/3})=o(1)\). Uniformly for \(|u-r|\le r^{2/3}\), the displayed local limits imply
\[
 \frac{\Pr(W=m-u)}{\Pr(T=m)}=1+o(1).
\]
The identity
\[
 \Pr(U_m=u)=\Pr(X=u)\frac{\Pr(W=m-u)}{\Pr(T=m)}
\]
then implies \(d_{\mathrm{TV}}(\mathcal L(U_m),\operatorname{Poisson}(r_m))\to0\): the ratio converges uniformly to one on a Poisson-high-probability window, and normalization controls the mass outside it. Convolution by the same independent Bernoulli variable cannot increase total variation. Combining this with the exceptional mass bound proves the stated Poisson–Bernoulli limit.

Finally \(r_m=\sqrt m+O(1)\), and the ordinary Poisson central limit theorem gives \((P_m-r_m)/\sqrt{r_m}\Rightarrow\mathcal N(0,1)\). The bounded independent \(B\) does not change this limit, and \(\sqrt{r_m}\sim m^{1/4}\), yielding the stated Gaussian scaling.

## Verification
The independent direct enumerator in `check.py` constructs every self-inverse partial permutation of each star on \(3\) through \(7\) vertices, checks the metric condition on every pair in its domain, and confirms the formula for \(m=2,3,4,5,6\). It also checks the recurrence for the two-colour telephone-number assembly through \(m=100\). Numerical total-variation values at five further parameter sizes are illustrative only; the infinite limit follows from the proof, not these experiments.

## Relationship to prior work
Fernandes and Paulista (first public preprint March 10, 2022) explicitly decompose the full star partial-isometry monoid into two symmetric-inverse-monoid copies and small exceptional classes (their Proposition 2.1 and equation (1)), and compute its cardinality, rank, Green relations and a presentation. That existing structural decomposition is used and credited. The elementary finite-rank specialization alone is not claimed as an independently deep result. The specific new assertion assessed here is the total-variation Poisson–Bernoulli deficiency law for uniform self-inverse partial star isometries, together with its exact finite bridge and extension obstruction. Literature on random involutions supplies broader analytic context but no identified statement establishing this specific star-monoid law.

## Limitations
This addresses only self-inverse partial isometries, not arbitrary partial maps or nilpotent partial maps. The limit is asymptotic and gives no explicit uniform finite-size total-variation error rate. The Poisson approximation is for the number of omitted leaves, with the hub contributing the independent fair Bernoulli term asymptotically. Existing general assembly limit theorems may offer an alternative deduction; no assertion of historical priority beyond the inspected sources is made. The direct finite checker is not a proof of the asymptotic theorem, and independent validation has not been performed.

## References
1. V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a finite star graph*, arXiv:2203.05504 (first posted 2022-03-10); *Communications in Algebra* 51 (2023), 1028–1048. https://arxiv.org/abs/2203.05504; accepted-manuscript full text https://run.unl.pt/bitstreams/a452b46f-eec5-469f-9883-018bf1c1a4a4/download.
2. L. Elliott, A. Levine and J. D. Mitchell, *Counting monogenic monoids and inverse monoids*, *Communications in Algebra* 51 (2023), 4654–4661. https://doi.org/10.1080/00927872.2023.2214821.
3. S. Miner, D. Rizzolo and E. Slivken, *Asymptotic distribution of fixed points of pattern-avoiding involutions*, *DMTCS* 19:2 (2017). https://doi.org/10.23638/DMTCS-19-2-5. This is related context for involution statistics, not a source for the present result.
