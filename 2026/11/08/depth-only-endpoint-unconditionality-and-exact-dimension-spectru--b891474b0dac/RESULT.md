# Depth-only endpoint unconditionality and exact dimension spectrum of adaptive Haar trees

## Finding
Let \(\mathcal T\) be any finite rooted **proper** binary tree: every nonterminal vertex has exactly two children, but different leaves may have different depths. Give the root mass \(1\), split every internal mass equally between its children, and let \(X_{\mathcal T}\) be the real space of functions on the terminal leaves with its \(L^\infty\) norm. Take the orthonormal Haar basis consisting of the constant function and the normalized differences at all internal vertices. Let \(U(\mathcal T)\) be the largest \(L^\infty\)-operator norm among all independent signs of those coefficients. Write \(H\) for the maximum leaf depth and put
\[
F_h=\frac{2h}{3}+\frac59+\frac49\left(-\frac12\right)^h,\qquad h\geq0.
\]
**Depth-only law:** \(U(\mathcal T)=F_H\). More precisely, the largest signed-kernel row norm at a specified leaf \(x\) is exactly \(F_{|x|}\), independently of all branches outside its ancestral path. When \(H\ge2\), precisely the deepest leaves can support a norm-maximizing output evaluation; all deepest leaves do so with suitable signs. For each maximizing output row, norming inputs agree with the sign of its kernel on every nonzero entry, up to a common global sign; their values on zero entries are arbitrary in \([-1,1]\) when the input has \(L^\infty\)-norm one.

**Exact dimension spectrum:** If \(\mathcal T\) has \(N\ge2\) leaves, the set of possible sharp constants, over all such trees with exactly \(N\) leaves, is
\[
\boxed{\left\{ F_h:\ \lceil\log_2N\rceil\le h\le N-1,\ h\in\mathbb Z\right\}.}
\]
The minimum is attained exactly by trees of least possible height \(\lceil\log_2N\rceil\); the maximum is attained exactly by the comb trees (each nonterminal vertex has a leaf child, except possibly the last one, which has two leaf children), up to child swaps. A comb with only \(H+1\) leaves has the **same** worst-case amplification as the complete balanced tree with \(2^H\) leaves. At \(N=1\), the only constant is \(F_0=1\). In particular, the maximum-to-minimum ratio for fixed \(N\) is asymptotic to \(N/\log_2N\).

## Assumptions and scope
The tree is finite, proper and rooted. Each parent-to-child split has conditional probability exactly \(1/2\); terminal masses are \(\mu(x)=2^{-|x|}\). Each internal node \(v\) supplies the real Haar vector
\[
h_v=\mu(v)^{-1/2}(\mathbf1_{v0}-\mathbf1_{v1}),
\]
where \(\mathbf1_{va}\) is the indicator of the entire descendant set of child \(va\). These vectors and \(1\) form an orthonormal basis of the \(N\)-dimensional space \(X_{\mathcal T}\) in its probability-weighted \(L^2\) inner product. The sign operator \(T_\varepsilon\) is the diagonal multiplier with independent coefficients \(\varepsilon\in\{\pm1\}\), including the constant. Its operator norm is measured from the real weighted atomic \(L^\infty\) space to itself, so there is no suppression, arbitrary local weighting, or extension to a different input space.

## Proof
**1. Exact signed row reduction.** Fix a terminal leaf \(x\) of depth \(k\). Multiplying all signs by one common sign leaves the norm unchanged, so set the constant sign to \(+1\). Let \(\sigma_j\in\{\pm1\}\) be the sign of the Haar vector at the ancestor of \(x\) at depth \(j\), for \(0\le j<k\). The signed operator kernel is
\[
K_\varepsilon(x,y)=1+\sum_{v\text{ internal}}\varepsilon_v h_v(x)h_v(y).
\]
The summands at vertices not ancestral to \(x\) vanish. The leaf masses in the sibling subtree first diverging from \(x\) at depth \(j\) add to \(2^{-j-1}\), no matter how that subtree is subsequently refined. Every kernel entry on that subtree equals \(1+\sum_{i<j}\sigma_i2^i-\sigma_j2^j\); the entry at \(x\) is \(1+\sum_{i<k}\sigma_i2^i\). Thus the entire row \(L^1\) norm is
\[
\sum_{j=0}^{k-1}2^{-j-1}\left|1+\sum_{i<j}\sigma_i2^i-\sigma_j2^j\right|+2^{-k}\left|1+\sum_{i<k}\sigma_i2^i\right|.
\]
Set \(z_0=1\) and \(z_{j+1}=(z_j+\sigma_j)/2\). Then \(|z_j|\le1\) and the previous expression becomes
\[
\sum_{j=0}^{k-1}\frac{|z_j-\sigma_j|}{2}+|z_k|
=\sum_{j=0}^{k-1}\frac{1-\sigma_jz_j}{2}+|z_k|.
\]
This establishes, exactly and without a homogeneous-depth assumption, that the optimal row depends only on \(k\).

**2. Solve the finite Bellman equation.** For \(|z|\le1\), let \(V_0(z)=|z|\) and
\[
V_m(z)=\max_{\sigma\in\{\pm1\}}\left\{\frac{1-\sigma z}{2}+V_{m-1}\left(\frac{z+\sigma}{2}\right)\right\}.
\]
Inductively write \(V_m(z)=a_m+c_m|z|\). Since \(|z+\sigma|=1+\sigma z\), the induction holds with \(a_0=0,c_0=1\) and
\[
a_m=a_{m-1}+\frac{1+c_{m-1}}2,\qquad c_m=\frac{1-c_{m-1}}2.
\]
It follows that
\[
c_m=\frac13+\frac23\left(-\frac12\right)^m,\qquad
a_m=\frac{2m}{3}+\frac29\left(1-\left(-\frac12\right)^m\right).
\]
Therefore \(V_k(1)=F_k\). Every maximizing ancestral sign sequence comes from the Bellman rule: when more than one step remains and \(z\ne0\), choose \(\sigma=-\operatorname{sgn}(z)\); when \(z=0\), either sign ties; at the last step either sign ties. Signs off the output leaf's ancestry are unrestricted.

**3. From rows to the operator norm.** For an atomic integral operator, \(\|T_\varepsilon\|_{\infty\to\infty}=\max_x\sum_y\mu(y)|K_\varepsilon(x,y)|\). For any selected row, the input \(f(y)=\operatorname{sgn}K_\varepsilon(x,y)\) realizes that row sum. Thus \(U(\mathcal T)=\max_{x\text{ leaf}}F_{|x|}\). Directly,
\[
F_{h+1}-F_h=\frac23\left(1-\left(-\frac12\right)^h\right),
\]
which vanishes only at \(h=0\) and is strictly positive for every \(h\ge1\). Since every nontrivial proper tree has all leaves at depth at least one, the maximum is \(F_H\) and, for \(H\ge2\), only deepest leaves attain it. Equality for a chosen row is exactly equality in the Bellman rule and sign matching of its kernel.

**4. Exact fixed-dimension spectrum.** A proper binary tree with \(N\) leaves has exactly \(N-1\) internal vertices. A longest leaf path contains \(H\) internal vertices, hence \(H\le N-1\). No depth-\(H\) binary tree has more than \(2^H\) leaves, hence \(H\ge\lceil\log_2N\rceil\). Equality \(H=N-1\) forces all internal vertices onto the longest path: exactly a comb, up to child swaps. For every integer \(h\) between these bounds, begin with a height-\(h\) comb, which has \(h+1\) leaves. Split its off-spine leaves, one at a time, only at depths below \(h\), until the complete height-\(h\) tree with \(2^h\) leaves is reached; each split adds one leaf and never changes the height. Because \(h+1\le N\le2^h\), some intermediate tree has exactly \(N\) leaves. The strict increase of \(F_h\) for \(h\ge1\) gives the stated exact spectrum and equality classes. The asymptotic ratio follows from \(F_h=2h/3+O(1)\).

## Verification
The accompanying standalone `verify_adaptive_haar.py` uses exact rational arithmetic and independently constructs all signed Haar kernel matrices on **every ordered proper binary tree with one through seven leaves**. For every leaf of every such tree, it maximizes the absolute kernel row sum over all independent signs of the ancestral Haar coefficients, confirming the \(F_{|x|}\) formula without using the Bellman recurrence to compute those row norms. It also independently checks the exact set of possible heights and therefore exact possible constants at each of these leaf counts. Run `python3 verify_adaptive_haar.py`. Finite verification is corroborative; the proof above covers all finite trees.

## Relationship to prior work
Geiss and Müller study arbitrary collections of dyadic Haar functions via Haar-type and Carleson packing conditions in Banach spaces, but their theorems concern \(1<p\le2\) upper \(\ell^p\) inequalities and not the finite real endpoint signed-operator norm classified here. Gach, Nickl and Spokoiny use spatially variable Haar resolutions for density estimation, supplying a natural adaptive motivation but not sign-transform unconditionality constants. Osękowski establishes sharp restricted weak-type inequalities for Haar projections and martingale transforms; his sharp constants concern finite \(p\), distribution functions and bounded inputs rather than the exact, arbitrary-pruning \(L^\infty\) row profile. The complete fixed-depth dyadic constant is a baseline special case; the new substance is the depth-only law for arbitrary proper prunings, complete dimension spectrum, and extremal tree-shape classification. These comparisons do not exclude an equivalent identity in uncatalogued older work.

## Limitations
The result is scalar, real, sign-only, and restricted to finite binary trees with exactly fair conditional splits and a complete Haar basis on the terminal partition. It does not apply unchanged to suppression operators, non-Haar rotations, general \(L^p\) norms, node-dependent split biases, ternary local bases not realized as binary Haar splits, or infinite trees. The result is an explicit finite-dimensional theorem; no infinite-dimensional unconditional basis claim is made.

## References
- S. Geiss and P. F. X. Müller, *Haar type and Carleson constants*, Bulletin of the London Mathematical Society 40 (2008), 432–438, DOI: 10.1112/blms/bdn022; freely accessible preprint arXiv:0902.1955 (posted February 11, 2009). Journal first online April 23, 2008.
- F. Gach, R. Nickl and V. Spokoiny, *Spatially adaptive density estimation by localised Haar projections*, discussion paper dated November 10, 2011; arXiv:1111.2807 (first arXiv posting November 11, 2011); published in Annales de l'I.H.P. Probabilités et statistiques 49 (2013), 900–914.
- A. Osękowski, *Sharp inequalities for the Haar system and Fourier multipliers*, Journal of Function Spaces 2013, Article ID 646012, DOI: 10.1155/2013/646012; first published December 5, 2013.
