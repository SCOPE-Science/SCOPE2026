# Complete Fourier recovery on triangular block graphs

## Finding

Let \(H\) be any finite abelian group of cardinality \(q\ge3\), and let \(G=(V,E)\) be a finite connected simple graph in which every block is either a bridge \(K_2\) or a triangle \(K_3\). Write \(e\) for the number of bridge blocks and \(t\) for the number of triangle blocks, so \(N=|V|=1+e+2t\). The edgeless one-vertex graph is included with \(e=t=0\). Let \(P_G\subset H^V\) be the proper colourings, and use the **unnormalized** transform
\[
 W_G(\xi)=\sum_{c\in P_G}\prod_{v\in V}\xi_v(c_v),\qquad \xi\in\widehat H^V.
\]
For a character \(\gamma\in\widehat H\), define \(s(\gamma)=q-1\) if \(\gamma\) is trivial, and \(s(\gamma)=-1\) otherwise. Fix a root vertex and orient the block-cut tree away from it. Each bridge introduces one new vertex \(u\), and each triangle introduces two new vertices \(u,v\). Define the **aggregate character** \(\eta_w\) at a nonroot vertex as the product of frequencies \(\xi_z\) over all vertices in the rooted descendant subgraph of \(w\), including \(w\), with all blocks at \(w\) oriented away from the root.

Then \(W_G(\xi)=0\) whenever \(\prod_{v\in V}\xi_v\) is nontrivial. For a balanced frequency, meaning \(\prod_v\xi_v=1\), the exact multiplier is
\[
\boxed{W_G(\xi)=q\prod_{K_2\text{ blocks}}s(\eta_u)\prod_{K_3\text{ blocks}}\left[s(\eta_u)s(\eta_v)-s(\eta_u\eta_v)\right].}
\]
Every balanced coefficient is nonzero. More precisely, the complete **multiset** of balanced coefficients is the multiplicative convolution (with multiplicities) of a factor \(q\), \(e\) copies of
\[
 \mathcal E_q=\{(q-1)\ [1],\ -1\ [q-1]\},
\]
and \(t\) copies of
\[
 \mathcal T_q=\{(q-1)(q-2)\ [1],\ -(q-2)\ [3(q-1)],\ 2\ [(q-1)(q-2)]\}.
\]
Here \(a\ [m]\) denotes the integer value \(a\) repeated \(m\) times, and equal products must be merged. This multiset depends **only** on \(q,e,t\), not on the shape of the block tree nor the isomorphism type of \(H\). Exactly \(q^{N-1}\) of the \(q^N\) Fourier coefficients are nonzero.

Let \(d_q=\min\{q-2,2\}\). The largest and smallest nonzero multiplier magnitudes are attained and equal, respectively, to
\[
 M_{q,e,t}=q(q-1)^e\bigl((q-1)(q-2)\bigr)^t,\qquad
 m_{q,e,t}=q\,d_q^t.
\]
Thus counting convolution \(f\mapsto\mathbf1_{P_G}*f\) on \(\ell^2(H^V)\) has rank \(q^{N-1}\), vanishes exactly on the non-balanced Fourier modes, and restricts to an invertible operator on the space of functions invariant under simultaneous translation of all vertex colours. Its sharp inverse operator norm on that space is \(1/(q d_q^t)\), and its sharp (singular-value) condition number is
\[
 \boxed{\kappa_{q,e,t}=(q-1)^e\left(\frac{(q-1)(q-2)}{d_q}\right)^t.}
\]
In particular, \(\kappa_{3,e,t}=2^{e+t}\) and \(\kappa_{4,e,t}=3^{e+t}\). No stronger graph-shape restriction is required.

## Assumptions and scope

All graphs are finite, simple and connected. The word *block* means a maximal 2-connected subgraph, with bridges counted as two-vertex blocks. Every block is exactly an edge or a triangle; cycles longer than three and shared-edge triangles are excluded. Proper colourings assign an element of \(H\) to every vertex with unequal values across each edge. No ordering or field multiplication on \(H\) is assumed. Frequencies lie in the Pontryagin dual \(\widehat H\), so their product is a character of \(H\). In the labelled cyclic case \(H=\mathbb Z/q\mathbb Z\), balance means the sum of coordinate frequencies vanishes modulo \(q\). Convolution is \((f*g)(x)=\sum_y f(y)g(x-y)\), with no probability normalization; the quoted operator norms use counting \(\ell^2\) and its unitary Fourier convention. Absolute multiplier extrema are unchanged if normalized counting \(L^2\) is used on both source and target.

## Proof

**Block coordinates.** Choose any vertex \(r\) as root. Because the block-cut incidence graph of a connected graph is a tree, each block can be listed in an outward order in which it meets previously introduced vertices in precisely one attachment vertex. An edge introduces one vertex; a triangle introduces two. Let \(\eta_u\) be the product of all original coordinate characters in the subtree rooted at \(u\), where every new vertex is a child of its block attachment. This yields an ordinary rooted tree on vertices, with an extra triangle constraint between each sibling pair. Descendant sets are therefore unambiguously defined.

**Exact local character sums.** For any character \(\gamma\), orthogonality gives
\[
\sum_{h\in H\setminus\{0\}}\gamma(h)=s(\gamma).
\]
Conditional on the colour at the attachment vertex \(a\), introduce a single new colour \(b=a+h\) in an edge block: properness requires \(h\ne0\), so its weighted sum is \(\gamma(a)s(\gamma)\). For a triangle block write the two new colours \(b=a+h\) and \(c=a+k\), with \(h,k\ne0\) and \(h\ne k\). Their character sum is
\[
\sum_{h,k\ne0,\ h\ne k}\alpha(h)\beta(k)
=\left(\sum_{h\ne0}\alpha(h)\right)\left(\sum_{k\ne0}\beta(k)\right)-\sum_{h\ne0}(\alpha\beta)(h)
=s(\alpha)s(\beta)-s(\alpha\beta).
\]
The dependence on \(a\) is exactly the product character \((\alpha\beta)(a)\). Eliminate terminal blocks one by one. At each elimination, multiply by the edge or triangle factor above and push the product character of the eliminated descendants into the attachment vertex. After every nonroot vertex is eliminated, the remaining sum over the root colour is \(q\) if the total frequency character is trivial and zero otherwise. This proves the displayed formula for every \(H,G,\xi\).

**Local levels and independence.** An edge factor is \(q-1\) for one value of its aggregate character and \(-1\) for the other \(q-1\). For a triangle, if both aggregate characters are trivial the factor is \((q-1)(q-2)\). If exactly one is trivial, or both are nontrivial and mutually inverse, it is \(-(q-2)\). This occurs in \(2(q-1)+(q-1)=3(q-1)\) ordered pairs. In all remaining \((q-1)(q-2)\) ordered pairs the factor is \(2\). These three cases exhaust \(q^2\) choices, and no factor vanishes for \(q\ge3\).

For a balanced tuple \(\xi\), the aggregate-character assignment \(\xi\mapsto(\eta_w)_{w\ne r}\) is a bijection from the balanced dual subgroup onto \(\widehat H^{V\setminus\{r\}}\). In fact, if all aggregates are prescribed, reconstruct original characters recursively from leaves by \(\xi_w=\eta_w\prod_{u\text{ child of }w}\eta_u^{-1}\) for \(w\ne r\), and set \(\xi_r\) to enforce balance. Hence the local aggregate values at distinct newly introduced vertices range independently over all their possibilities. This proves the complete multiplier multiset, its shape independence, and exactly \(q^{e+2t}=q^{N-1}\) nonzero frequencies.

**Sharpness of extrema and recovery.** The largest local absolute values are \(q-1\) for an edge and \((q-1)(q-2)\) for a triangle; the smallest are \(1\) and \(d_q\). All are genuinely attained, jointly, because aggregate characters can be prescribed independently. The maximum is also the unweighted chromatic count obtained at trivial frequency. Fourier diagonalization of counting convolution gives the rank and identifies its kernel as precisely the non-balanced modes. Functions invariant under the diagonal subgroup \(\{(h,\ldots,h):h\in H\}\) are exactly those supported on balanced frequencies, so inversion there has reciprocal spectral bounds. The ratio of largest to smallest nonzero absolute eigenvalue yields the sharp condition number. The special values at \(q=3\) and \(q=4\) follow by substitution. This completes the proof.

## Verification

Two standalone Python 3 programs (standard library only) independently check the formula. `verify_direct.py` directly enumerates all proper colourings and frequencies of several small nonisomorphic block trees over cyclic colour groups of orders three, four and five; it evaluates Fourier sums as **exact integer cyclotomic-residue histograms**, and compares each coefficient with the rooted-block formula. `verify_klein.py` uses a different representation: the Klein four-group \(H=(\mathbb Z/2\mathbb Z)^2\), an exact fast Walsh–Hadamard transform of the full proper-colouring indicator, and an independent tensor-product prediction of the complete coefficient histogram. It compares all frequency values, including zeros, for seven small examples. Run:

```sh
python3 verify_direct.py
python3 verify_klein.py
```

These finite checks confirm the formulas on the specified examples, including noncyclic colour groups; the general result is proved by the block-tree elimination and aggregate-character bijection, not by an extrapolation from finite data.

## Relationship to prior work

Chromatic-polynomial and Potts partition-function techniques give ordinary counts of graph colourings. In particular, Fendley–Krushkal (2008) study chromatic/Potts algebra, Loh–Pikhurko–Sudakov (2008) study extremal counts of proper colourings, and Chang–Shrock (2009) derive weighted colouring formulas, including a multiple-colour external field and a full triangle example. Their published structural sums provide relevant background, but do not state the **all-frequency nonvanishing** and **block-shape-independent complete multiplier multiset** established here. A separate published Fourier-frame computation for friendship graphs gives the degree-one covariance/conditioning and explicitly restricts itself to the first band, not the full convolution spectrum. The distinction is important: exact ordinary colouring counts and first-band sampling cannot recover the present full frequency-by-frequency zero set, spectral multiplicities or sharp convolution inverse norm without additional analysis.

## Limitations

The factorization requires that blocks meet only at cut vertices and are all \(K_2\) or \(K_3\); attaching any block with more vertices requires new local character calculations, which might have zeros. The theorem assumes at least three colours: the triangle factor vanishes identically with two colours because there are no proper triangle colourings. The result concerns exact, unnormalized counting convolution, not noisy data or first-harmonic sampling alone. General multivariate Potts formulas could conceivably encode equivalent special cases; the explicit block-level nonvanishing and sharp spectra are the claims assessed here. A bounded literature comparison cannot exclude unindexed historical computations of the same spectra.

## References

1. P. Fendley and V. Krushkal, *Link invariants, the chromatic polynomial and the Potts model*, arXiv:0806.3484v1 (20 June 2008), https://arxiv.org/abs/0806.3484 .
2. P.-S. Loh, O. Pikhurko and B. Sudakov, *Maximizing the number of q-colorings*, arXiv:0811.2625v1 (17 November 2008), https://arxiv.org/abs/0811.2625 .
3. S.-C. Chang and R. Shrock, *Weighted Graph Colorings*, arXiv:0908.2375v1 (17 August 2009), especially Sections II and XII, https://arxiv.org/html/0908.2375v1 .
