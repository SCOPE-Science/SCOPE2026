# A centered-walk law for Coxeter-period stabilization in type-A zero-Hecke monoids

## Finding
For every integer \(n\ge 3\), let \(H_0(S_n)\) be the type-A \(0\)-Hecke monoid, with generators \(\pi_1,\ldots,\pi_{n-1}\), idempotency \(\pi_i^2=\pi_i\), commuting relations for nonadjacent indices, and the usual braid relations. A *Coxeter element* \(c\) is a product of each generator exactly once. Denote by \(w_0\) the absorbing longest element, and define the least stabilization exponent
\[
K(c)=\min\{r\ge1:c^r=w_0\}.
\]
If \(\pi_i\) precedes \(\pi_{i+1}\) in the chosen Coxeter word, set \(\varepsilon_i=1\); otherwise set \(\varepsilon_i=-1\). Define \(H_1=0\) and \(H_{j+1}=H_j+\varepsilon_j\) for \(1\le j\le n-2\). These signs depend only on the monoid element, since nonadjacent generators can commute, and parametrise its \(2^{n-2}\) possible values.

**Exact stabilization theorem.** For every such \(c\),
\[
\boxed{K(c)=\frac{n+\max_{1\le a<n}|H_a-H_{n-a}|}{2}.}
\]
The numerator is always even. This formula makes the *entire* distribution of stabilization exponents explicit, not only their minimum.

For an interval of integer states \(I\) containing zero, let \(T_I\) be the matrix with rows and columns indexed by \(I\), with diagonal entries \(2\), immediate-neighbor entries \(1\), and all remaining entries zero. Let \(e_0\) be the unit vector at state zero and \(\mathbf1\) the all-one column. For every integer \(k\ge0\):
\[
\begin{aligned}
\#\{c\in\mathcal C_{2m}:K(c)\le m+k\}&=e_0^\mathsf{T}T_{[-k,k]}^{m-1}\mathbf1,\qquad m\ge2,\\
\#\{c\in\mathcal C_{2m+1}:K(c)\le m+1+k\}&=2e_0^\mathsf{T}T_{[-k-1,k]}^{m-1}\mathbf1,\qquad m\ge1.
\end{aligned}
\]
Here \(\mathcal C_n\) is the set of Coxeter elements and the interval notation means all integers between the endpoints. Probability equals these counts divided by \(2^{n-2}\); subtraction of successive cumulative counts gives every point probability. In particular, the extrema are \(\lceil n/2\rceil\le K(c)\le n-1\). At the minimum the counts are \(2^{m-1}\) for \(n=2m\), and \(2\cdot 3^{m-1}\) for \(n=2m+1\), the latter coinciding with the earlier Coxeter-word admissibility count of Kosuda, as discussed below.

**Asymptotic law.** For a uniformly selected element of \(\mathcal C_n\),
\[
\boxed{\frac{K(c)-n/2}{\sqrt n}\ \Longrightarrow\ \frac12\sup_{0\le t\le1}|B(t)|,}
\]
where \(B\) is standard Brownian motion. The limit is nondegenerate, giving a square-root fluctuation scale around half the chain length. Equivalently, for \(x>0\) the limiting distribution function is
\[
\frac4\pi\sum_{j=0}^\infty\frac{(-1)^j}{2j+1}
\exp\!\left(-\frac{(2j+1)^2\pi^2}{32x^2}\right).
\]

## Assumptions and scope
All finite claims hold for every integer \(n\ge3\) without a field or characteristic hypothesis. The power \(c^r\) is the monoid (Demazure) product, **not** the ordinary group power of a Coxeter permutation. The Coxeter element distribution is uniform over distinct monoid elements, equivalently the independent symmetric orientation-sign strings \((\varepsilon_1,\ldots,\varepsilon_{n-2})\), rather than uniform over all \((n-1)!\) generator orderings. Descending adjacent comparators realize the \(0\)-Hecke multiplication starting at the identity permutation \((1,2,\dots,n)\).

## Proof
**Step 1: binary threshold principle.** In any fixed order of the \(n-1\) adjacent positions, let a round apply each comparator \(j\), replacing the entries at positions \(j,j+1\) by their maximum followed by their minimum. Repeated rounds applied to the ascending permutation give precisely the successive powers of \(c\) as permutation labels. These comparators commute with every monotone binary threshold. Thus the ascending permutation becomes fully descending after \(r\) rounds **if and only if**, for every \(1\le a<n\), the binary input \(0^a1^{n-a}\) becomes \(1^{n-a}0^a\) after \(r\) rounds: necessity follows by thresholding the original labels at \(a\); sufficiency follows because all these thresholds of the output must be descending, forcing the entire permutation to be descending. Thus \(K(c)\) is the maximum of the individual binary-block sorting times.

**Step 2: exact last-crossing time.** Fix \(a,b\ge1\), \(a+b=n\). Index the \(a\) zeros from right to left by \(i=1,\ldots,a\), and the \(b\) ones from left to right by \(j=1,\ldots,b\). Each zero-one pair must cross once, and the crossing indexed \((i,j)\) occurs at adjacent comparator position \(p=a-i+j\). It can happen only after the crossings \((i-1,j)\) and \((i,j-1)\) when present. The greedy comparator dynamics realize each required crossing in the earliest round respecting these two predecessors and the fixed within-round order; there are no additional precedence constraints, since all other pairs either have disjoint wires or are already enforced by the grid partial order.

Let \(R_{i,j}\) be that earliest round. Set \(R_{1,1}=1\). With \(p=a-i+j\), the predecessor \((i-1,j)\) uses position \(p+1\), so the current crossing requires an additional round exactly when \(\pi_p\) occurs before \(\pi_{p+1}\), namely when \(\varepsilon_p=1\). Likewise \((i,j-1)\) uses \(p-1\), and an extra round is required exactly when \(\varepsilon_{p-1}=-1\). Therefore
\[
R_{i,j}=\max\left\{
 R_{i-1,j}+\frac{1+\varepsilon_p}{2}\ (i>1),\quad
 R_{i,j-1}+\frac{1-\varepsilon_{p-1}}2\ (j>1)
 \right\},
\]
where absent predecessors are omitted. On an edge of this grid the added weight is always \((1-\Delta H)/2\), where \(\Delta H\) is the change in the height at the comparator position from predecessor to current. Every monotone path from \((1,1)\) to \((a,b)\) has exactly \(a+b-2=n-2\) edges, starts at position \(a\), and ends at position \(b\). Its weight telescopes to \((n-2-H_b+H_a)/2\), independently of the path. Consequently
\[
R_{a,b}=1+\frac{n-2-H_b+H_a}{2}=\frac{n+H_a-H_b}{2}.
\]
Maximizing over \(a\in\{1,\ldots,n-1\}\), with \(b=n-a\), and noting that interchanging \(a,b\) reverses the sign of \(H_a-H_b\), proves the formula. The parity follows because \(H_a-H_{n-a}\) is a sum of \(|n-2a|\) signs, hence has the parity of \(n\).

**Step 3: exact orientation census.** A uniform Coxeter element is a uniform choice of \(\varepsilon_1,\ldots,\varepsilon_{n-2}\), all independently \(\pm1\). For \(n=2m\), the symmetric central interval sums of length \(2r\) are twice a lazy random walk \(Y_r\) starting at zero, \(0\le r\le m-1\). Its independent increments are \(-1,0,+1\), with multiplicities \(1,2,1\) among four sign-pairs. Therefore \(K=m+\max_r|Y_r|\). The transfer matrix \(T_{[-k,k]}\) exactly counts paths never leaving the integer interval \([-k,k]\), proving the even formula.

For \(n=2m+1\), the symmetric intervals have lengths \(1,3,5,\ldots,2m-1\). Their signed sums are \(\varepsilon_m+2Y_r\) for the same lazy increments and \(0\le r\le m-1\). Conditional on \(\varepsilon_m=+1\), the bound \(K\le m+1+k\) is equivalent to \(-k-1\le Y_r\le k\) at all times; the negative-center case has a reflected, equally numerous set of walks. This proves the odd formula and the factor \(2\). Setting \(k=0\) gives the minimum counts; the maximal time \(n-1\) occurs only when all orientation signs agree, in two cases.

**Step 4: scaling.** The lazy increments have mean zero and variance \(1/2\). The walk runs for \(m-1\sim n/2\) steps. Donsker's invariance principle yields \(Y_{\lfloor(m-1)t\rfloor}/\sqrt n\Rightarrow B(t)/2\) in the continuous path limit. The center sign and fixed half-integer shift in odd dimensions vanish after division by \(\sqrt n\). Applying the continuous supremum-absolute-value functional proves the Brownian maximum limit. The optional series follows from the standard two-sided Brownian exit-time spectral expansion.

## Verification
The standalone `CHECKER.py` performs the direct monoid operation by sequential adjacent max/min comparators, separately constructs an orientation-compatible order, computes the stated height formula, computes binary-block sort times, and evaluates the transfer recursions. It exhaustively verifies every orientation for \(3\le n\le11\) (\(1022\) Coxeter elements in total) and all \(9216\) associated binary-block comparisons. It also makes \(840\) seeded direct checks at larger sizes up to \(n=60\) and checks minimum/maximum transfer counts for \(3\le n\le30\). The output `CHECKER_OUTPUT.txt` records all passes. These finite checks are corroboration; the infinite theorem follows from Steps 1–4.

## Relationship to prior work
Denton–Hivert–Schilling–Thiéry (arXiv:1010.3455v1, first public 2010-10-17) supplies the finite \(0\)-Hecke presentation and Coxeter background. Speyer (arXiv:0710.3188v1, 2007-10-16) studies reduced powers in infinite Coxeter groups and demonstrates existence of compatible subwords reaching longest elements in finite groups; it does not enumerate finite type-A repeated-period completion times. Kosuda (arXiv:1411.5761v1, 2014-11-21) treats Coxeter words whose half-length ordinary-group powers give longest words. Its admissibility criteria and minimal-level counts overlap the extreme fastest case here and are acknowledged as prior work. The claim assessed here is the **complete numerical stabilization threshold for every orientation, all finite threshold distributions, and the nondegenerate Brownian supremum limit for uniform Coxeter elements**. These are not stated in the relevant passages inspected from the above primary texts. The present result uses a separate binary threshold/crossing-grid argument and makes no claim to novelty for the foundational definitions or minimum-power counts.

## Limitations
Only type-A \(0\)-Hecke Coxeter elements are considered, not arbitrary elements or arbitrary finite Coxeter types. The random law is for uniform **distinct Coxeter elements**, not uniform generator-order words. General sorting-network/heap results may implicitly imply the finite formula; the literature search is not a proof of priority, and independent historical review remains unperformed. The Brownian limit is weak convergence and does not itself provide uniform finite-size tail error bounds.

## References
- D. E. Speyer, *Powers of Coxeter Elements in Infinite Groups are Reduced*, arXiv:0710.3188v1 (2007-10-16), https://arxiv.org/abs/0710.3188.
- T. Denton, F. Hivert, A. Schilling and N. M. Thiéry, *On the Representation Theory of Finite J-Trivial Monoids*, arXiv:1010.3455v1 (2010-10-17), https://arxiv.org/abs/1010.3455.
- M. Kosuda, *Coxeter elements of the symmetric groups whose powers afford the longest*, arXiv:1411.5761v1 (2014-11-21), https://arxiv.org/abs/1411.5761.
- O. Angel, V. Gorin and A. E. Holroyd, *A Pattern Theorem for Random Sorting Networks*, arXiv:1110.0160v1 (2011-10-02), https://arxiv.org/abs/1110.0160 (comparison context, distinct random sorting-network model).
