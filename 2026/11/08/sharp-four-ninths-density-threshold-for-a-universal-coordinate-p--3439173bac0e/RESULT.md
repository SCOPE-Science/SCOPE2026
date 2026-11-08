# Sharp four-ninths density threshold for a universal coordinate-product ideal

## Finding
For \(E\subseteq\mathbb Z^2\), put \(P(E)=\{ab:(a,b)\in E-E\}\). Then
\[
 d^*(E)>\frac49\quad\Longrightarrow\quad 4\mathbb Z\subseteq P(E).
\]
The threshold is sharp for forcing the single integer \(4\): the periodic set
\[
 E_0=\{(x,y)\in\mathbb Z^2:x+y\pmod9\in\{0,1,2,3\}\}
\]
has \(d^*(E_0)=4/9\) but \(4\notin P(E_0)\).
For each fixed \(\delta\in(4/9,1/2]\), the smallest positive integer \(K\) such that \(K\mathbb Z\subseteq P(E)\) for every \(E\) with \(d^*(E)\ge\delta\) is \(K=4\). For \(\delta>1/2\) this smallest integer is \(K=1\).

## Assumptions and scope
All sets are subsets of the integer lattice \(\mathbb Z^2\). Differences are ordered differences of two (not necessarily distinct) points. Define upper Banach density by
\[
 d^*(E)=\limsup_{L\to\infty}\sup_{z\in\mathbb Z^2}
 \frac{|E\cap(z+\{0,\ldots,L-1\}^2)|}{L^2}.
\]
Only the coordinate product of the two coordinates of a *single* difference vector is used; the two coordinates are not independently selectable from separate difference sets. No regularity or periodicity is assumed of the arbitrary set \(E\). Negative multiples are included.

## Proof
**Nine-edge obstruction.** Fix any nonzero \(m\in\mathbb Z\). Set
\[
 u=(1,4m),\quad v=(2,2m),\quad w=(4,m).
\]
Each of \(u,v,w\) has coordinate product \(4m\), and the exact vector identity
\[
 2u-5v+2w=(0,0)
\]
produces a closed walk with nine edges, in this order:
\[
 u,\ u,\ -v,\ -v,\ -v,\ -v,\ -v,\ w,\ w.
\]
Suppose \(4m\notin P(E)\). Then no difference of two points of \(E\) is any of \(\pm u,\pm v,\pm w\). For each translate \(z\) of the nine-position closed walk, adjacent visited positions therefore cannot both lie in \(E\). An odd cyclic binary string of length nine with no adjacent ones has at most four ones. This argument remains valid even if some visited positions happened to coincide; indeed for \(m\ne0\) the nine positions here are distinct.

Let \(Q_L=t+\{0,\dots,L-1\}^2\) be any axis-parallel integer square. Sum the nine-position inequality over all \(z\in Q_L\). Each of the nine translated positions is a fixed displacement of \(z\), so its count differs from \(|E\cap Q_L|\) by at most \(O_m(L)\), uniformly in the translation \(t\). Hence
\[
 9|E\cap Q_L|\le4L^2+O_m(L).
\]
Taking the supremum over translates and then the upper limit gives \(d^*(E)\le4/9\), contradicting the hypothesis. Thus \(4m\in P(E)\) for every nonzero integer \(m\). As \(E\) is nonempty, \((0,0)\in E-E\) and \(0\in P(E)\), proving \(4\mathbb Z\subseteq P(E)\).

**Sharpness of the threshold.** Each residue class of \(x+y\pmod9\) has lattice density \(1/9\), so \(d^*(E_0)=4/9\). Differences of allowed sum residues belong to
\[
 \{0,\pm1,\pm2,\pm3\}\pmod9,
\]
which excludes the residues \(\pm4\pmod9\). The *only* integer vectors whose coordinate product is \(4\) are
\[
 (1,4),(2,2),(4,1),(-1,-4),(-2,-2),(-4,-1).
\]
Their coordinate sums are \(\pm5\) or \(\pm4\), i.e. precisely the excluded residues \(4,5\pmod9\). None can belong to \(E_0-E_0\); therefore \(4\notin P(E_0)\).

**Optimality of the modulus.** The checkerboard lattice
\[
 E_1=\{(x,y)\in\mathbb Z^2:x+y\equiv0\pmod2\}
\]
has density \(1/2\) and its difference set is exactly the set of vectors with even coordinate sum. Such vectors have either both coordinates odd (odd product) or both coordinates even (product divisible by four). Consequently \(P(E_1)\) contains no integer congruent to \(2\pmod4\). For each \(K\in\{1,2,3\}\) one can choose a multiple \(Kj\equiv2\pmod4\) (namely \(j=2,1,2\), respectively). Hence no smaller positive \(K\) works uniformly over the density class \(\delta\le1/2\).

Finally, if \(d^*(E)>1/2\), then for any fixed \(h\in\mathbb Z^2\), translated squares attaining upper density above \(1/2\) and a boundary comparison show that \(E\cap(E-h)\ne\varnothing\). Thus \(E-E=\mathbb Z^2\). Every integer \(n\) equals the coordinate product of \((1,n)\), so \(P(E)=\mathbb Z\) and \(K=1\) is optimal.

## Verification
Run `python3 verify.py`. The deterministic checker independently tests the exact nine-step vector relation for positive and negative multipliers, enumerates all binary length-nine cyclic patterns to verify the sharp independent-set cap, directly checks the six integer factor vectors for product four against the modulo-nine obstruction, and verifies the checkerboard congruence obstruction. A sample output is embedded as `verification_output.txt`. These finite checks are diagnostics; the infinite-density claim follows from the above translate-averaging proof, not computation.

## Relationship to prior work
Goswami and Liu (2026), Theorem 1.5 of arXiv:2609.06782, prove that for each positive density cutoff some integer modulus has its full ideal inside \(P(E)\); their theorem does not specify the value of this modulus. The result here gives the exact optimal universal modulus in a nontrivial explicit high-density interval, with a sharp boundary witnessed by a nine-class periodic example. Their paper does not state the four-ninths threshold or the nine-cycle argument. Goswami's earlier 2026 paper obtains weaker finite-sums containment, not an explicit optimal full ideal. Fish's 2017 preprint (2018 journal publication) treats products of two separate one-dimensional difference sets; it cannot directly supply the same-set coordinate-product conclusion or its sharp threshold.

## Limitations
The theorem does not determine the best modulus at density thresholds at most \(4/9\), and makes no claim of classification of all extremal density-\(4/9\) sets. Equality at \(4/9\) cannot be substituted for strict inequality in the forcing statement. The proof applies to integer lattices with the specified upper Banach density definition; the explicit extremizer demonstrates the boundary. Historical priority could be affected by an unindexed prior derivation. Independent mathematical validation is not claimed.

## References
1. S. Goswami and C. Liu, *A Uniform Product-Difference Theorem for Dense Subsets of \(\mathbb Z^2\)*, arXiv:2609.06782 (first publicly posted 2026-09-06), Theorem 1.5 and its proof. https://arxiv.org/abs/2609.06782
2. S. Goswami, *On difference sets of dense subsets of \(\mathbb Z^2\)*, arXiv:2601.03797 (2026), Theorems 1.6–1.7. https://arxiv.org/abs/2601.03797
3. A. Fish, *On product of difference sets for sets of positive density*, arXiv:1702.02544 (2017; published in Proc. Amer. Math. Soc. 146 (2018), 3449–3453), Theorem 1.1 and Corollary 1.1. https://arxiv.org/abs/1702.02544
