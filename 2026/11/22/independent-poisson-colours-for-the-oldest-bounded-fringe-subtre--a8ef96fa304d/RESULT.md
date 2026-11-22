# Independent Poisson colours for the oldest bounded fringe subtrees of a random recursive tree

## Finding

Let \(T_n\) be the uniform recursive tree on birth labels \(1,\ldots,n\): for each \(j\ge2\), vertex \(j\) independently chooses a uniformly random parent from \(1,\ldots,j-1\). Write \(F_{n,i}\) for the rooted descendant (fringe) subtree of vertex \(i\), including \(i\). Fix an integer \(K\ge1\). For each \(1\le s\le K\), let \(\mathcal R_s\) be the set of \((s-1)!\) increasing rooted trees on rank labels \(1,\ldots,s\), represented by their parent vectors. Every \(F_{n,i}\) is canonically rank-relabelled in increasing order of its original labels. For \(\tau\in\mathcal R_s\), define the point measure
\[
\Xi_{n,\tau}=\sum_{i=2}^n\mathbf1\{F_{n,i}\text{ has increasing shape }\tau\}\,\delta_{i/\sqrt n}.
\]
As \(n\to\infty\), the finite family \((\Xi_{n,\tau})_{\tau\in\bigcup_{s=1}^K\mathcal R_s}\) converges jointly (vaguely on bounded subsets of \([0,\infty)\)) to **independent** Poisson point processes, with respective intensity measures
\[
\boxed{\frac{x}{(s-1)!}\,dx\quad\text{for every }\tau\in\mathcal R_s.}
\]
In particular, after forgetting the finer shape but retaining subtree size, the \(K\) size-coloured processes are independent, **each with intensity \(x\,dx\)**.

Let \(M_{n,K}\) denote the smallest birth label of a vertex with fringe subtree size at most \(K\), taking \(+\infty\) if necessary. For every \(t\ge0\),
\[
\boxed{\lim_{n\to\infty}\Pr\{M_{n,K}/\sqrt n>t\}=e^{-Kt^2/2}.}
\]
The size of the subtree at this earliest vertex converges to the discrete uniform law on \(\{1,\ldots,K\}\), independently of the rescaled earliest label. Conditional on its size \(s\), the increasing shape is asymptotically uniform among the \((s-1)!\) possibilities. More generally, the complete ordered sequence of bounded-size fringe vertices has the corresponding independently marked Poisson-arrival law.

## Assumptions and scope

The tree is rooted at vertex \(1\), and all parent choices are independent. The fringe subtree of \(i\) contains \(i\) and **all** its descendants, not merely its immediate children or an arbitrary connected rooted subgraph. All size/shape labels are those induced by increasing relabelling of the selected subtree. The cutoff \(K\) and the number of requested marks or ordered arrivals remain fixed while \(n\to\infty\). The result is local in rescaled birth label, not an assertion about all \(n\) positions or sizes growing with \(n\). For \(n>K\), root \(1\) cannot qualify. The primary classification is combinatorial probability (MSC2020 60C05).

## Proof

**1. Exact one-root law.** Fix \(2\le i\le n\) and set \(S_{n,i}=|F_{n,i}|\). As later vertices arrive, the number already in the descendant subtree of \(i\) evolves as a two-colour Pólya urn, with initial populations \(1\) (inside) and \(i-1\) (outside) at time \(i\). Its future membership indicators are exchangeable. For \(1\le s\le n-i+1\), the beta-binomial law yields
\[
\boxed{
\Pr\{S_{n,i}=s\}
=\frac{(i-1)(n-i)_{\underline{s-1}}}{(n-1)_{\underline s}},
}
\tag{1}
\]
where \((a)_{\underline b}=a(a-1)\cdots(a-b+1)\). For larger \(s\) the probability is zero. Conditional on \(S_{n,i}=s\), the descendant set apart from \(i\) is a uniformly chosen \((s-1)\)-subset of \(\{i+1,\ldots,n\}\). Conditional on this set, every later inside vertex has a uniformly chosen parent among older inside vertices, while each later outside vertex has a uniformly chosen parent among older outside vertices. These parent choices are conditionally independent. The parent of \(i\) is outside, and it disappears on deletion. Consequently the rank-labelled internal tree is an independent uniform recursive tree of size \(s\); its probability of being any specified \(\tau\in\mathcal R_s\) is \(1/(s-1)!\). On deleting the entire fringe subtree at \(i\), the remaining tree, with labels relabelled in increasing order, is independently a uniform recursive tree on \(n-s\) vertices.

For each fixed \(K,T<\infty\), uniformly for \(2\le i\le T\sqrt n\) and \(1\le s\le K\), equation (1) gives
\[
\Pr\{S_{n,i}=s\}=\frac{i}{n}+O_{K,T}(n^{-1}),
\qquad \Pr\{S_{n,i}=s\}=O_{K,T}(n^{-1/2}).
\tag{2}
\]
The first error is absolute, so it remains valid even for the first few labels.

**2. Joint rare-event lemma.** Fix \(r\ge1\), \(T<\infty\), \(K\ge1\), and distinct labels \(2\le i_1<\cdots<i_r\le T\sqrt n\). Prescribe \(\tau_a\in\mathcal R_{s_a}\), \(s_a\le K\). We prove uniformly that
\[
\boxed{
\Pr\{F_{n,i_a}\cong\tau_a\text{ for }a=1,\ldots,r\}
=\prod_{a=1}^r\frac{i_a}{n(s_a-1)!}
+O_{r,K,T}(n^{-(r+1)/2}).
}
\tag{3}
\]
Here \(\cong\) means equality of the increasing rank-labelled tree, not an unlabelled graph isomorphism.

We use induction on \(r\); \(r=1\) is (1)–(2). Condition on \(F_{n,i_1}\cong\tau_1\), an event of probability \(O(n^{-1/2})\), and on its uniformly random \((s_1-1)\)-set \(D\) of later descendants. If no later prescribed root lies in \(D\), deletion of \(\{i_1\}\cup D\) leaves a uniform recursive tree. Each surviving prescribed label \(i_a\) is shifted by at most \(s_1\), the new total is \(n-s_1\), and its fringe subtree and increasing shape are unchanged: since \(i_a>i_1\), it could not be an ancestor of \(i_1\), hence could not have descendants in \(D\). The probability that none of the finitely many other prescribed labels is in \(D\) is \(1+O_{r,K}(n^{-1})\). The induction hypothesis, together with the bounded shifts, gives the product in (3) with the stipulated error.

For completeness, events with some later prescribed roots in \(D\) do not change this main term. If exactly \(m\ge1\) specified later roots lie in \(D\), the probability of their inclusion in this fixed-size uniformly selected set is \(O_{r,K}(n^{-m})\). Their required subtree events inside \(D\) can be bounded by one, while the other \(r-1-m\) roots live in the independent outside recursive tree and, by induction, have joint probability \(O_{r,K,T}(n^{-(r-1-m)/2})\). The entire contribution is therefore at most
\[
O(n^{-1/2})\,O(n^{-m})\,O(n^{-(r-1-m)/2})
=O(n^{-(r+m)/2}),
\]
which is \(O(n^{-(r+1)/2})\). There are only finitely many membership patterns. This establishes (3), including the possibility of nested prescribed fringe subtrees.

**3. Multitype Poisson point processes.** Let \(A\subseteq[0,T]\) be an interval with null boundary in the limiting measure and let \(\tau\in\mathcal R_s\). Equation (3), summed over distinct prescribed birth labels, shows that all joint falling-factorial moments of the vector of counts \(\Xi_{n,\tau}(A)\), over any finite collection of intervals and marks, converge to those of independent Poisson random variables with respective means
\[
\frac1{(s-1)!}\int_A x\,dx.
\]
Indeed each fixed-order joint moment sums \(O(n^{r/2})\) tuples; the uniform remainder in (3) sums to \(O(n^{-1/2})\). The main term is a Riemann sum. The one-mark bound in (2) also shows local tightness, and the limiting multivariate Poisson law is moment-determinate (its moment generating function exists everywhere). Thus counts in disjoint bounded windows converge jointly. This proves joint vague point-process convergence, with independent colours and locally finite simple limiting processes. All results remain valid when increasing-shape colours of equal size are superposed; their intensities sum to \(x\,dx\), since \(|\mathcal R_s|=(s-1)!\).

**4. First-event law and its mark.** The superposed process of all sizes \(1,\ldots,K\) has cumulative intensity \(Kt^2/2\) on \([0,t]\). Its probability of no point gives the stated tail of \(M_{n,K}/\sqrt n\), which also implies tightness because the tail tends to zero as \(t\to\infty\). The limiting coloured process can equivalently be constructed by assigning independent marks to each point of the rate-\(Kx\) process. Each size has probability \(1/K\), each shape of size \(s\) has conditional probability \(1/(s-1)!\), and the marks are independent of locations. Hence the earliest-mark and ordered-arrival assertions follow.

## Verification

The standalone standard-library script `verify.py` enumerates **all** uniform recursive trees through eight vertices, checks formula (1) for every feasible root and size, checks the uniformity of conditioned descendant sets, and checks the conditional uniform distributions of both the internal and pruned outside recursive trees. It also tests exact finite sums at three larger orders against the predicted first-moment scale. The script completed successfully with **1,336 exact and deterministic analytic consistency assertions**. Exhaustive checks are finite, not a substitute for Steps 1–4, which prove the infinite-limit statement.

Run: `python verify.py` using a standard Python 3 interpreter.

## Relationship to prior work

Holmgren and Janson [1, Theorems 1.4, 1.5 and 1.9] give global counts of fringe subtrees by size and shape, including Gaussian and rare-large-subtree Poisson regimes. Their marked statistic is total **subtree size**, whereas the coordinate here is the original **birth rank** of a root with *fixed bounded* subtree size. Their formulas do not state independent Poisson processes across early birth ranks or the uniform size mark of the first qualifying root. Feng and Mahmoud [2, Theorem 1 and Section 3] give Gaussian fluctuations of fixed-shape fringe counts and the shape functional, not the present extreme-birth-rank process. Mahmoud and Smythe [3] address a subtree at one fixed original label and its large-size behaviour; their abstract does not provide a growing family of early small-subtree roots. The existing published earliest-leaf point-process result [4] corresponds precisely to the special case \(K=1\) and is acknowledged, not claimed new. Its general leaf-indicator identity does not imply the multitype result for distinct fixed positive subtree sizes, which requires the conditional deletion argument and controls nested selected roots.

## Limitations

The cutoff \(K\) must be fixed, and no bound uniform in \(K\) or in growing ranks is proved. No total-variation rate for the joint point process is asserted. The finite exact law and independence-by-deletion are proof ingredients, not independent priority claims. Historical equivalence to a more general unpublished or inaccessible result is possible. The 1991 fixed-root paper was only available in abstract-level form; this is an explicit historical-priority risk. The mathematical verification is not an independent expert audit.

## References

1. C. Holmgren and S. Janson, *Limit Laws for Functions of Fringe Trees for Binary Search Trees and Recursive Trees*, arXiv:1406.6883, first posted **2014-06-26**, subsequently *Electronic Journal of Probability* 20 (2015), article 4. https://arxiv.org/abs/1406.6883 (primary MSC 60C05).
2. Q. Feng and H. M. Mahmoud, *On the Variety of Shapes on the Fringe of a Random Recursive Tree*, *Journal of Applied Probability* 47 (2010), 191–200. https://doi.org/10.1239/jap/1269610825 .
3. H. M. Mahmoud and R. T. Smythe, *On the Distribution of Leaves in Rooted Subtrees of Recursive Trees*, *Annals of Applied Probability* 1 (1991), 406–418. https://doi.org/10.1214/aoap/1177005874 .
4. *The oldest leaves of random recursive trees form a Poisson point process*, published published-finding corpus record (2026-10-18), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-the-oldest-leaves-of-random-recursive-trees-form-a-poisson-point--0a1a1c4bbf35 .
