# Exact stable-extension multiplicities in uniform functional attack frames

## Finding
For each finite set \([n]=\{1,\dots,n\}\), consider **all** \(n^n\) functions \(f:[n]\to[n]\), interpreting each arrow \(v\to f(v)\) as a Dung attack. Self-attacks are allowed, and the empty function at \(n=0\) is included by convention. Write \(Z(f)\) for the number of stable extensions; a preferred extension is an inclusion-maximal admissible set. For each mapping, **preferred extensions and stable extensions coincide if and only if \(Z(f)>0\)**. The positive numbers \(Z(f)\) are powers of two.

Define the unique formal series \(R,U\in z\mathbb Q[[z]]\) by
\[
R=z\exp(R),\qquad U\exp(U)=R.
\]
The complete, size-refined count of positive stable-extension multiplicities is
\[
\boxed{F(z,y)=\sum_{n\ge0}\frac{z^n}{n!}\sum_{f:[n]\to[n],\,Z(f)>0} y^{\log_2Z(f)}
=\frac{1-U(z)}{1-R(z)}\bigl(1-U(z)^2\bigr)^{-y/2}.}
\]
In particular \([z^n]F(z,0)n!\) counts mappings with a **unique** stable extension, while \([z^n]F(z,1)n!\) counts mappings where all preferred extensions are stable. Their counts for \(n=1,2,\ldots,8\) respectively are
\[
(0,2,9,112,1225,19836,338149,7097280),
\]
\[
(0,3,9,157,1375,26091,398419,9005529).
\]

Let \(w\in(0,1)\) be the positive solution of \(w\exp(w)=1\), and let \(\lambda=-\frac12\log(1-w^2)\). If \(f\) is chosen uniformly from all \(n^n\) maps, then for each fixed integer \(k\ge0\),
\[
\boxed{\lim_{n\to\infty}\Pr(Z(f)=2^k)= (1-w)\frac{\lambda^k}{k!};\quad
\lim_{n\to\infty}\Pr(Z(f)=0)=1-\sqrt{\frac{1-w}{1+w}}.}
\]
Numerically, the limiting probabilities of no stable extension, a unique stable extension, and at least one stable extension are approximately \(0.4744455435\), \(0.4328567096\), and \(0.5255544565\), respectively. Conditional on existence, the limiting exponent \(\log_2Z(f)\) has a Poisson law of mean \(\lambda\approx0.1940470644\).

## Assumptions and scope
An admissible set is conflict-free and defends all its members: every attacker of an accepted vertex must itself be attacked by an accepted vertex. Preferred means inclusion-maximal admissible; stable means conflict-free and attacking every vertex not accepted. These are the ordinary Dung definitions, not kernels with the opposite orientation of absorption. The attack graph has **exactly one outgoing attack per vertex**, but unrestricted incoming degree. In particular this is not the model where each vertex has at most one incoming attacker. Both looped and nonlooped functional components are included.

A connected functional digraph is one directed cycle (of length one or more) with finite directed in-trees attached. In each tree (excluding cycle vertices), label a vertex IN if all its tree children are OUT, and OUT if at least one tree child is IN, computing from leaves upward. A cycle vertex is *blocked* if one of its noncycle children is IN; otherwise it is *free*. A cycle is *unblocked* when all its vertices are free.

## Proof
**1. Force the acyclic in-trees.** Starting from every unattacked tree leaf, the grounded labelling is forced IN, and every vertex attacked by IN is OUT; a vertex whose attackers are all OUT is IN. Induction on distance from the leaves shows all noncycle vertices have definite grounded labels IN/OUT, identical in every complete and hence every preferred extension. Their labels do not depend on the cyclic part because attacks point from descendants toward ancestors. Each blocked cycle vertex is forced OUT.

**2. Classify the cycles.** If at least one vertex on a directed cycle is blocked, it is OUT, and the remaining cycle labels are forced successively: a free cycle vertex is IN exactly when its cycle predecessor is OUT, and OUT when that predecessor is IN. The resulting assignment is consistent around the cycle because the blocked vertex is OUT regardless of its predecessor; it is stable on the component and is the sole preferred assignment. If all cycle vertices are free, the cycle has two alternating stable/preferred assignments when its length is even. If its length is odd, no assignment of IN/OUT labels exists and no cycle vertex belongs to any admissible set: accepting one requires accepting alternating predecessors to defend it, contradicting conflict-freeness around the odd cycle. Thus the unique preferred assignment leaves the whole cycle undecided and is not stable. Components combine independently. Therefore an unblocked odd cycle forces \(Z(f)=0\); otherwise, \(Z(f)=2^k\), where \(k\) is the number of unblocked even cycles, and all preferred extensions are stable.

**3. Count tree decorations.** The exponential generating series of nonempty labelled in-trees is the Cayley tree series \(R=z\exp(R)\). Split them according to the IN/OUT status of their root when regarded as an acyclic tree. If \(U\) counts IN roots and \(V\) OUT roots, the unordered-set construction gives
\[
U=z\exp(V),\quad V=z(\exp(U+V)-\exp(V)),\quad R=U+V.
\]
Consequently \(U\exp(U)=z\exp(R)=R\). At a cyclic vertex, an arbitrary attached set of noncycle child trees has total weight \(R\), with free weight \(U\) (every child OUT) and blocked weight \(V=R-U\). These weights already include the cyclic vertex itself exactly once.

**4. Labelled functional components.** Directed cycles of decorated vertices form a labelled CYC construction; their connected-component generating series is \(\sum_{j\ge1} R^j/j=-\log(1-R)\). Every cycle containing a blocked vertex is admissible for stability; its aggregate series is
\[
\sum_{j\ge1}\frac{R^j-U^j}{j}=-\log(1-R)+\log(1-U).
\]
An unblocked even cycle of length \(2j\) gives precisely one multiplicative factor two in the number of stable extensions, so mark such a cycle by \(y\). Their series is \(y\sum_{j\ge1}U^{2j}/(2j)=-\frac y2\log(1-U^2)\). Unblocked odd cycles are excluded. Taking SET of these components and exponentiating proves the formula for \(F(z,y)\), including the empty mapping. Extraction of \([y^k]\) gives
\[
\frac{1-U}{1-R}\frac{\bigl(-\frac12\log(1-U^2)\bigr)^k}{k!}.
\]

**5. Asymptotic transfer.** The series for all mappings is \(1/(1-R)\), whose \(z^n/n!\) coefficient is \(n^n\). Its dominant singularity is \(z=1/e\), and \(R\to1\), with \(1-R\sim\sqrt{2(1-ez)}\). The function \(U=W(R)\) is analytic near \(R=1\) and tends to \(w=W(1)\in(0,1)\). Hence the fixed-\(k\) coefficient ratio to \(1/(1-R)\) tends to \((1-w)\lambda^k/k!\) by square-root singularity transfer. Summing over \(k\) at \(y=1\), equivalently evaluating the same analytic factor there, yields limiting existence probability
\[
\frac{1-w}{\sqrt{1-w^2}}=\sqrt{\frac{1-w}{1+w}}.
\]
The complement gives the zero-stable probability. Normalizing the positive-count generating function at \(y=1\) gives the stated Poisson conditional limit. No inference about a growing \(k\) is made from fixed-\(k\) transfer alone.

## Verification
Run `python3 verify.py` from the extracted package using standard-library Python. It constructs the formal series through order eight using exact rational arithmetic and independently enumerates all \(n^n\) labelled mappings for each \(1\le n\le6\). On each mapping, it independently enumerates all \(2^n\) candidate subsets and tests conflict-freeness, admissibility, maximality and stability; it then compares the resulting two extension counts with the classification obtained by pruning acyclic leaves and inspecting cycle parity. Finally it checks every size-refined coefficient of the EGF against the exhaustive mapping census. These finite checks corroborate but do not establish the all-order proof or asymptotics.

## Relationship to prior work
Dung (1995) introduced the extension semantics. Gao (2017) analyzes a *pairwise-edge random* framework and a threshold for existence, not the uniform one-out mapping model or its exact multiplicity series. Elaroussi (2025) proves polynomial-time preferred-acceptance problems for one-in/one-out degree restrictions, but gives no corresponding all-order labelled count. Zhang and Liu (2026, first public October 19) establish structural *sufficient* conditions for preferred–stable agreement; the exact random functional-frame census is not stated in the accessible abstract, while the complete preprint text could not be accessed.

The closest published published-finding corpus comparison, *Grounded undecided mass and parity-resolved stable limits in sparse one-attacker frameworks* (2026), samples at most one **incoming** attacker independently for each target (with a positive no-attacker probability). Its unicyclic in-tree attachments remain entirely undecided, unlike the present one-**outgoing**-attacker model, whose attached trees force and can block cycles. Although both models lead to Poisson laws with a related algebraic form, parameter substitution does not transfer the other model's sampling statement to this one. Published results on kernels in digraphs and random mappings provide important structural background but were not found to imply the displayed full finite-size polynomial. Originality remains subject to historical review.

## Limitations
The result assumes exactly one outgoing edge from each vertex, allows loops, and uses the uniform distribution on all total functions. It does not address arbitrary sparse digraphs, independent-edge sampling, partial functions, or correlated maps. The asymptotic multiplicity formula is pointwise for fixed \(k\). The full text of the October 2026 path-based paper was inaccessible from available primary-host mirrors, so direct theorem-by-theorem comparison there remains a residual priority risk. Earlier kernel/random-map enumerations may use equivalent language, and no independent mathematical or historical-priority validation has been performed.

## References
1. P. M. Dung, "On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games", *Artificial Intelligence* 77 (1995), 321–357, DOI:10.1016/0004-3702(94)00041-X.
2. Y. Zhang and K. Liu, "When Stable and Preferred Semantics Agree: A Path-Based Approach", arXiv:2610.30176, originally submitted 2026-10-19, https://arxiv.org/abs/2610.30176.
3. M. Elaroussi, "Analyzing the impact of bounded degree constraints on computational complexity of argumentation frameworks", first published online 2025-02-14, DOI:10.1177/19462174241306715, https://journals.sagepub.com/doi/10.1177/19462174241306715.
4. Y. Gao, "A Random Model for Argumentation Framework: Phase Transitions, Empirical Hardness, and Heuristics", *IJCAI* (2017), DOI:10.24963/ijcai.2017/71, https://ijcai.org/proceedings/2017/71.
5. "Grounded undecided mass and parity-resolved stable limits in sparse one-attacker frameworks", published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-grounded-undecided-mass-and-parity-resolved-stable-limits-in-spa--a4704bc344df.
6. H. Langlois and F. Meunier, "Revisiting classical results on kernels in digraphs", arXiv:2502.02482 (2025), https://arxiv.org/abs/2502.02482.
