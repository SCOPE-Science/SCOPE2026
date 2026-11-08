# First mean-phylogenetic-diversity ambiguity at nine taxa, resolved by variance

## Finding

Let \(\mathcal T_n\) be the set of nonisomorphic rooted nonplane full-binary tree shapes with \(n\) leaves, no root stem, and **all edges of length one**. Each leaf survives independently with common probability \(p\in(0,1)\). Write \(X_T(p)\) for the rooted phylogenetic diversity (PD) of the surviving set, including the root in the spanned subtree and taking PD of the empty set to be zero.

**Theorem.** For every \(2\le n\le8\), the complete mean-response curve \(p\mapsto\mathbb E X_T(p)\) uniquely determines the unlabeled shape \(T\in\mathcal T_n\). At \(n=9\), exactly one unordered pair of distinct shapes has the same mean-response curve. With the conventional rooted Newick representation (all listed branches having unit length), that pair is

```text
A = ((a,(b,(c,d))),(e,((f,g),(h,i))));
B = (((a,b),(c,d)),(e,(f,(g,(h,i)))));
```

For \(q=1-p\), both mean-response curves are

\[
\mathbb E X_A(p)=\mathbb E X_B(p)
=16-9q-3q^2-q^3-2q^4-q^5,
\]

but their variance curves satisfy the strict identity

\[
\operatorname{Var}(X_B(p))-\operatorname{Var}(X_A(p))
=2q^7(1-q)=2p(1-p)^7>0.
\]

Consequently the **mean-and-variance response curves together identify every unlabeled rooted full-binary nine-leaf shape**, even though the mean alone does not. The mean ambiguity persists for every number of leaves \(n\ge9\) after grafting the exhibited pair as the same nine-leaf component within any fixed larger binary tree; their variances remain different by the same positive amount. The result concerns **unlabeled tree shapes**, not recovery of leaf names, and the equal-unit-edge model is essential to the stated threshold.

At \(p=1/2\), both trees have mean \(335/32\), while their variances are \(6483/1024\) and \(6491/1024\), respectively.

## Assumptions and scope

A full-binary rooted tree has precisely two children at each internal vertex; its children are unordered and its leaves are unlabeled for purposes of shape comparison. For each nonroot edge \(e\), let \(C(e)\) be the set of descendant leaves and \(s_e=|C(e)|\). The root has no incoming edge. Every present edge contributes exactly one unit to rooted PD if and only if at least one descendant leaf survives. Each of the \(n\) leaf-survival indicators is independent with common parameter \(p\). All claims of strict variance separation hold for every real \(p\in(0,1)\), not merely a sampled grid of values. The enumeration concerns the complete finite class \(\mathcal T_n\) for \(2\le n\le9\).

## Proof

**1. The mean fingerprints the multiset of clade sizes.** Put \(q=1-p\). Write \(I_e\) for the indicator that some leaf in \(C(e)\) survives. Then

\[
X_T(p)=\sum_{e}I_e,\qquad
\mathbb E X_T(p)=\sum_e(1-q^{s_e}).
\]

Since every full-binary shape with \(n\) leaves has exactly \(2n-2\) nonroot edges, equality of mean curves for all \(p\in(0,1)\) is equivalent, by polynomial coefficient uniqueness, to equality of the multisets \(\{s_e:e\in E(T)\}\). This is not the full labelled clade system: it retains only the cardinalities.

**2. Complete finite shape classification.** Every \(n\)-leaf nonplane full-binary shape is a root with two shapes having \(a\) and \(b\) leaves, where \(a+b=n\) and \(1\le a\le b\). Generate these recursively from the single one-leaf shape; when \(a=b\), impose a canonical ordering on the child shapes and retain one representative of each unordered pair. By induction this constructs every shape exactly once. For each generated shape, recursively list the sizes of both root-child clades and all of their descendant clades. The complete counts are:

| Leaves \(n\) | Shapes | Distinct mean fingerprints |
|---:|---:|---:|
| 2 | 1 | 1 |
| 3 | 1 | 1 |
| 4 | 2 | 2 |
| 5 | 3 | 3 |
| 6 | 6 | 6 |
| 7 | 11 | 11 |
| 8 | 23 | 23 |
| 9 | 46 | 45 |

The complete finite recurrence and the per-shape comparisons are implemented in `check_pd_fingerprints.py`; its assertions exhaust every shape through nine leaves, not just a sample. At nine leaves, exactly one mean-fingerprint class has two members and all remaining 44 are singletons. Its two members are \(A\) and \(B\) displayed above. Both have nine edges with descendant size one, three with size two, one with size three, two with size four, and one with size five. Their root-four-leaf subtrees differ (caterpillar versus balanced), so they are not isomorphic. The mean formula in the theorem follows immediately.

**3. An exact variance discriminator.** For each edge, \(\operatorname{Var}(I_e)=q^{s_e}-q^{2s_e}\). If the descendant clades of two edges are disjoint, their indicators are independent. If the edge of size \(u\) is ancestral to an edge of size \(v\), then the nested clades satisfy

\[
\operatorname{Cov}(I_u,I_v)=q^u-q^{u+v}.
\]

Consequently

\[
\operatorname{Var}(X_T)=\sum_e(q^{s_e}-q^{2s_e})
 +2\sum_{(e,f):\,e\text{ strictly ancestral to } f}
 (q^{s_e}-q^{s_e+s_f}).
\]

For the two nine-leaf shapes, the diagonal size terms coincide. All unordered ancestral pair counts, classified by \((u,v)\), also coincide except that \(A\) has two \((5,2)\) pairs and zero \((5,3)\) pairs, while \(B\) has one pair of each type. Thus the difference of the two variance polynomials is

\[
2[(q^5-q^8)-(q^5-q^7)]
=2(q^7-q^8)=2p(1-p)^7,
\]

with the order \(B-A\). This is strictly positive for all \(p\in(0,1)\). Since the nine-leaf mean fingerprint has only this one collision, adding the variance curve distinguishes every nine-leaf shape.

**4. Persistence under grafting.** For any \(n>9\), graft \(A\) or \(B\) in place of the same designated nine-leaf subtree of a fixed \(n\)-leaf full-binary tree, assigning unit length to every new edge. Both resulting trees have identical edge-size multisets: the external edges are unchanged and the internal nine-leaf spectra agree. Any ancestral pair with both edges external is unchanged; each ancestral pair with one external ancestor and one internal descendant is determined entirely by the common nine-leaf size multiset. The only altered ancestral pairs have both edges within the grafted subtree and yield exactly the previously calculated variance difference. Distinctness persists because the replaced nine-leaf subtrees are nonisomorphic.

## Verification

Run `python3 check_pd_fingerprints.py` with Python 3 and no external dependencies. The script (i) constructs all 46 nonplane rooted full-binary nine-leaf shapes by the complete ordered-child recurrence, (ii) verifies uniqueness of size-multiset fingerprints through eight leaves and exactly one collision at nine, (iii) compares mean and variance polynomial coefficients exactly as integer dictionaries, and (iv) independently enumerates all \(2^9=512\) survivor configurations for each witness at \(p=1/2\) using rational arithmetic. It checks the exact moments \(335/32,6483/1024,6491/1024\). The all-parameter statement follows from the proved polynomial identity, not from finite sampling. A successful run ends with `VERIFY_OK`.

## Relationship to prior work

The field-of-bullets extinction model, rooted PD, and the edge-indicator expectation identity are standard; see Steel, Mimoto and Mooers (2007) and Faller, Pardi and Steel (first preprint August 2, 2007; journal 2008). Faller et al. study the distribution and its moments, not an observed sharp mean-fingerprint shape-identifiability cutoff in the accessible abstract. Nipperess and Matsen (2013) derive exact PD mean and variance under **fixed-count** rarefaction, not independent Bernoulli extinction, and discuss tree-shape sensitivity. Matsen and Evans (2012) study nonidentification of tree shapes by adjacency/Laplacian/distance **matrix spectra**, a distinct notion of fingerprint from the clade-size mean-response polynomial. These works provide methods and motivations; the present theorem concerns a complete first-collision census and exact variance separation. The inaccessible full text of Faller et al. leaves a residual historical-priority risk, not a claim that its whole contents were excluded.

## Limitations

The sharp nine-leaf threshold is for unlabeled rooted **full-binary** shapes with **equal unit edge lengths**, independently and identically surviving leaves, and all survival probabilities considered as a complete curve. Heterogeneous lengths, correlated extinctions, fixed-size sampling, nonbinary trees, and reconstruction of labelled topology are outside the theorem. The variance gap may be small: at \(p=1/2\) it is only \(1/128\), and a theoretical exact-identification distinction does not imply good statistical estimation under noise. The result has no independent external validation. Historical priority remains provisional, particularly because the full Faller–Pardi–Steel paper could not be inspected.

## References

1. Steel, M., Mimoto, A., and Mooers, A. Ø. (2007), *Hedging Our Bets: The Expected Contribution of Species to Future Phylogenetic Diversity*, Evolutionary Bioinformatics 3. https://doi.org/10.1177/117693430700300024
2. Faller, B., Pardi, F., and Steel, M. (2007 preprint; 2008 journal), *Distribution of phylogenetic diversity under random extinction*, arXiv:0708.0425; Journal of Theoretical Biology 251, 286–296. https://arxiv.org/abs/0708.0425 ; https://doi.org/10.1016/j.jtbi.2007.11.034
3. Nipperess, D. A., and Matsen, F. A. (2013), *The mean and variance of phylogenetic diversity under rarefaction*, Methods in Ecology and Evolution 4, 566–572. https://doi.org/10.1111/2041-210X.12042
4. Matsen, F. A., and Evans, S. N. (2012), *Ubiquity of synonymity: almost all large binary trees are not uniquely identified by their spectra or their immanantal polynomials*, Algorithms for Molecular Biology 7, 14. https://doi.org/10.1186/1748-7188-7-14
