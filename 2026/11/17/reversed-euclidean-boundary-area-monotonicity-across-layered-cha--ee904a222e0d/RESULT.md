# Reversed Euclidean boundary-area monotonicity across layered chain-order polytopes

## Finding

Let \(r\ge1\) and let \(m_1,\ldots,m_r\) be arbitrary **positive integers**, with \(n=\sum_{i=1}^r m_i\ge2\). Let \(P\) be the ordinal sum of antichains of sizes \(m_1,\ldots,m_r\). For each \(0\le k\le r\), take the canonical, unscaled, full-dimensional Euclidean chain-order polytope \(K_k\) whose first \(k\) ranks carry chain coordinates and whose remaining ranks carry order coordinates, as defined below. Write \(V_k=\operatorname{Vol}_n(K_k)\) and \(S_k=\mathcal H^{n-1}(\partial K_k)\).

All members have equal volume,
\[
 V_k=V=\frac{\prod_{i=1}^r m_i!}{n!}.
\]
Their **entire surface-area profile**, without assumptions on the individual rank sizes, is
\[
 \boxed{\frac{S_k}{V}=n\left(k+1+\sqrt{k+1}+(r-k-1)\sqrt2\right),\quad0\le k<r,}
\]
and
\[
 \boxed{\frac{S_r}{V}=n(r+\sqrt r).}
\]
For \(r\ge3\) the exact ordering is
\[
 \boxed{S_0=S_1>S_2>\cdots>S_{r-1}=S_r.}
\]
For \(r=1\) or \(r=2\), all the surfaces in the family are equal. Consequently, **passing from order constraints to chain constraints weakly decreases Euclidean boundary measure at equal volume**, whereas the previously established face-count inequalities run in the other direction.

For \(r\ge3\), the endpoint ratio is
\[
 \frac{S_r}{S_0}=\frac{r+\sqrt r}{2+(r-1)\sqrt2},
\]
which decreases in the large-rank limit to \(1/\sqrt2\). Thus the sharp limiting fractional boundary-area reduction within this canonical rank-interpolation is \(1-1/\sqrt2\), independent of the rank populations. The endpoint surface-area identities are known in related calculations; the finding here is the **complete intermediate-profile law and its reversed monotonicity**, nontrivial for \(r\ge4\).

## Assumptions and scope

Let \(I_i\) be disjoint sets of indices with \(|I_i|=m_i\), and use the standard Euclidean metric on \(\mathbb R^n\). For \(0\le k<r\), the polytope \(K_k\) is defined by all of the following inequalities:

- \(x_a\ge0\) for \(a\in I_i\), \(1\le i\le k\);
- \(x_a\le x_b\) for \(a\in I_i\), \(b\in I_{i+1}\), \(k+1\le i<r\);
- \(\sum_{i=1}^k x_{a_i}\le x_b\) for every \(a_i\in I_i\) (\(1\le i\le k\)) and \(b\in I_{k+1}\);
- \(x_b\le1\) for every \(b\in I_r\).

For \(k=0\), the sum in the third family is zero. For \(k=r\), require \(x_a\ge0\) for all coordinates and \(\sum_{i=1}^r x_{a_i}\le1\) for every selection \(a_i\in I_i\). All listed facet families are irredundant; the general facet statement for the ranked-poset interpolation is given in Ahmad–Fourier–Joswig, Lemma 3.2 and Proposition 2.3. Dimensions, volumes and facet areas use the ambient **ordinary** Euclidean normalization, not lattice-normalized facet measure. The lower-rank, singleton and all-singleton cases are included.

## Proof

**Volume identity.** For \(k<r\), let \(M=\sum_{i>k}m_i\), and let \(t_i=\max_{a\in I_i}x_a\) for \(1\le i\le k\). Fixing the chain coordinates leaves a translated and dilated ordinary order polytope on the remaining ranks; its side parameter is \(h=1-\sum_{i=1}^k t_i\). The relative volume of that tail is \(h^M\prod_{i>k}m_i!/M!\). The cumulative volume of a nonnegative cube with maximum at most \(t_i\) is \(t_i^{m_i}\), so integration over the maxima has density \(m_i t_i^{m_i-1}\). Therefore
\[
 \begin{aligned}
 V_k&=\frac{\prod_{i>k}m_i!}{M!}
 \int_{\substack{t_i\ge0\\\sum t_i\le1}}
 \left(1-\sum_{i=1}^k t_i\right)^M
 \prod_{i=1}^k m_i t_i^{m_i-1}\,dt_1\cdots dt_k\\
 &=\frac{\prod_{i>k}m_i!}{M!}
 \frac{M!\prod_{i=1}^k m_i!}{n!}
 =\frac{\prod_{i=1}^r m_i!}{n!}.
 \end{aligned}
\]
The second equality is the elementary Dirichlet beta integral. For \(k=0\) it reduces to the usual order-polytope formula; for \(k=r\) the same integration of coordinate-level maxima over \(\sum t_i\le1\) yields the identical formula. Set \(E=\prod_{i=1}^r m_i!\), so \(V=E/n!\).

**Facet-volume lemma.** Suppose a facet equation is \(x_b=\sum_{a\in J}x_a+c\), with \(J\) a set of \(s\) distinct coordinates and \(b\notin J\). Eliminating coordinate \(b\) in favor of the others multiplies Euclidean \((n-1)\)-measure by \(\sqrt{s+1}\). For a coordinate equation the factor is one. For an order equality \(x_a=x_b\) the factor is \(\sqrt2\). These follow directly from the Gram determinant of the graph parametrization; no combinatorial normalization is implicit.

**Zero and top facets.** Deleting a coordinate in a chain rank by setting it to zero leaves the same volume calculation with that rank size reduced by one; if it was a singleton, its now-empty rank is simply omitted. Every such facet in rank \(i\le k\) has Euclidean area
\[
 \frac{E}{m_i(n-1)!}=\frac{nV}{m_i}.
\]
The same value holds for the top coordinate facet \(x_b=1\) with \(b\in I_r\), of area \(nV/m_r\). Summing gives one budget \(nV\) for every chain rank and another \(nV\) for the top rank.

**Order-cover facets.** For \(k+1\le i<r\), impose \(x_a=x_b\) with \(a\in I_i\), \(b\in I_{i+1}\). The quotient poset is a complete layered poset whose ranks \(i,i+1\) change to \(m_i-1,1,m_{i+1}-1\), omitting zero-sized ranks. Its standard chain-order face has coordinate volume \(E/[m_i m_{i+1}(n-1)!]\) by the same beta integral. The \(\sqrt2\) Gram factor gives facet area
\[
 \frac{nV\sqrt2}{m_i m_{i+1}}.
\]
There are \(m_i m_{i+1}\) such facets at the interface, so every order-cover interface contributes exactly \(nV\sqrt2\).

**Mixed chain-to-order facets.** Fix indices \(a_i\in I_i\), \(1\le i\le k\), and \(b\in I_{k+1}\), and impose \(\sum_{i=1}^k x_{a_i}=x_b\). Write \(t_i=x_{a_i}\) and \(z=\sum t_i\). All other chain coordinates in level \(i\) range independently over \([0,t_i]\). All remaining order coordinates, shifted by \(z\), lie in the ordinary tail order polytope with one distinguished minimum coordinate fixed at zero. Its coordinate \((M-1)\)-volume, when the remaining scale is \(1-z\), is
\[
 \frac{\prod_{i>k}m_i!}{m_{k+1}(M-1)!}(1-z)^{M-1}.
\]
The Dirichlet integral gives the projected facet coordinate volume
\[
 \begin{aligned}
 &\frac{\prod_{i>k}m_i!}{m_{k+1}(M-1)!}
 \int_{\substack{t_i\ge0\\\sum t_i\le1}}
 (1-\sum t_i)^{M-1}\prod_{i=1}^k t_i^{m_i-1}\,dt\\
 &\hspace{1cm}=\frac{E}{(n-1)!\prod_{i=1}^{k+1}m_i}.
 \end{aligned}
\]
Multiplying by the graph Gram factor \(\sqrt{k+1}\), each mixed facet has area
\[
 \frac{nV\sqrt{k+1}}{\prod_{i=1}^{k+1}m_i}.
\]
Exactly \(\prod_{i=1}^{k+1}m_i\) such facets exist. Their combined surface budget is therefore \(nV\sqrt{k+1}\). At \(k=0\), this correctly represents the coordinate-zero facets of the first order rank; at \(k=r-1\), the mixed facets meet the final order rank.

**Pure chain endpoint.** For \(k=r\), the \(r\) zero-facet groups each have budget \(nV\). The \(\prod_i m_i\) maximal-chain facets each have Euclidean area
\[
 \frac{\sqrt r\prod_i(m_i-1)!}{(n-1)!}
 =\frac{nV\sqrt r}{\prod_i m_i}.
\]
Thus their total is \(nV\sqrt r\) and \(S_r/V=n(r+\sqrt r)\).

**Strict ordering.** Summing the four disjoint facet budgets for \(k<r\) yields \(S_k/V=n[k+1+\sqrt{k+1}+(r-k-1)\sqrt2]\). For \(0\le k\le r-2\),
\[
 \frac{S_{k+1}-S_k}{nV}
 =1-\sqrt2+\sqrt{k+2}-\sqrt{k+1}.
\]
It equals zero for \(k=0\). For \(k\ge1\) it is negative because \(\sqrt{k+2}-\sqrt{k+1}<\sqrt2-1\). Finally \(S_{r-1}=S_r=nV(r+\sqrt r)\); for \(r=1,2\), these identities give only equalities. The endpoint area ratio tends to \(1/\sqrt2\) as \(r\to\infty\). No argument uses lower bounds on the individual \(m_i\).

## Verification

The standalone `checks/check_layered_surface.py` independently enumerates all feasible zero-one vertices for every ordered composition of \(2\le n\le6\), constructs its Euclidean convex hull, and compares its actual numerical volume and boundary area to the formulas above for **all** \(0\le k\le r\). It also verifies that every prescribed facet is a codimension-one face. Its executed output was:

```text
LAYERED_SURFACE_PASS hull_cases=253 facet_rank_checks=2204 n=2..6
```

The finite checks include singleton ranks, unequal ranks, and both endpoints. The infinite theorem depends on the Dirichlet integrals, exact facet descriptions, Euclidean Gram factors and elementary square-root comparison, **not** on extrapolation from these finite cases.

## Relationship to prior work

Fang–Fourier introduced marked chain-order interpolations and established Ehrhart equivalence; the particular maximal-ranked family and its defining facets are treated explicitly by Ahmad–Fourier–Joswig (originally public in 2023). Their central theorem establishes monotonicity of face counts along the same interpolation. Freij-Hollanti–Lundström obtain face-vector inequalities for a broader class of ordinal sums. These structural and combinatorial results are used as prior mathematics, not claimed anew.

The endpoint surface/volume expressions for standard layered order and chain polytopes have appeared separately in prior calculations. Those endpoint identities alone do not determine any intermediate metric profile; the **new claim** is the simultaneous exact formula for every interior \(k\), all positive rank sizes, and the direction-reversing strict comparison with face-vector monotonicity. The difference between lattice-equivalent volume and Euclidean facet measure is essential: the latter depends on the facet-normal Gram factors \(1\), \(\sqrt2\) and \(\sqrt{k+1}\).

## Limitations

This result concerns the specific coordinate embedding and discrete rankwise chain-order interpolation, not arbitrary marked posets, arbitrary partition orders, oblique coordinate metrics, or continuously varying marked-polytope families. Face-count monotonicity is a previously published result, not proved anew here. A previous formula for the same intermediate Euclidean area profile could remain unindexed; historical priority therefore requires further independent literature checking. No independent audit of this proof has been performed.

## References

1. I. Ahmad, G. Fourier, M. Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626 (first posted 2023-09-04), especially Definition 2.2, Lemma 3.2, Theorem 4.1. https://arxiv.org/abs/2309.01626
2. R. Freij-Hollanti, T. Lundström, *\(f\)-vector inequalities for order and chain polytopes*, arXiv:2312.13890 (first posted 2023-12-21). https://arxiv.org/abs/2312.13890
3. X. Fang, G. Fourier, *Marked chain-order polytopes*, European Journal of Combinatorics 58 (2016), 267–282; arXiv:1508.02232 (first posted 2015-08-10). https://arxiv.org/abs/1508.02232
4. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23. https://doi.org/10.1007/BF02187680
