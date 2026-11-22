# A universal in-degree spectrum for characteristic-two chain-ring structure graphs

## Finding
Let \(R\) be a finite commutative chain ring of characteristic \(2\), with maximal ideal \(J=(\pi)\), residue-field size \(q=2^f\), and length \(k\ge1\), so \(J^k=0\ne J^{k-1}\). Consider the directed functional graph on \(R^2\) of
\[
\Phi(a,b)=(a+b,ab).
\]
Put \(h=\lceil k/2\rceil\), and let \(C_d\) be the number of vertices of in-degree \(d\). For every positive integer \(d\), the entire in-degree distribution is
\[
\boxed{C_d=q^k\mathbf{1}_{\{d=q^{\lfloor k/2\rfloor}\}}+\sum_{v=0}^{h-1}\frac{q-1}{2}\,q^{2k-2v-1}\mathbf{1}_{\{d=2q^v\}}.}
\]
Here indicator coefficients are added when two displayed degrees coincide (notably when \(q=2\)). The remaining number of vertices, of in-degree zero, is
\[
\boxed{C_0=q^{2k}-q^k-\frac{q-1}{2}\sum_{v=0}^{h-1}q^{2k-2v-1}.}
\]
In particular, the sharp maximum in-degree is \(q^{k/2}\) for even \(k\), and \(2q^{(k-1)/2}\) for odd \(k\). All these counts depend only on \((q,k)\), not on a choice of presentation of \(R\).

## Assumptions and scope
The ring is commutative, unital, finite, and of characteristic exactly \(2\). Its ideals form the chain \(R\supset J\supset\cdots\supset J^k=0\). Write \(\nu(x)=v\) when \(x\in J^v\setminus J^{v+1}\) and \(\nu(0)=k\). We use \(|R|=q^k\), \(|J^a|=q^{k-a}\). A loop contributes one incoming edge in the usual functional-graph sense. No assertion is made for rings of characteristic \(4\) or higher, nor for non-chain rings.

## Proof
Fix a target \((s,p)\in R^2\). A predecessor has the unique form \((x,s+x)\) with
\[
 x^2+sx=p.
\]
Since \(\operatorname{char}(R)=2\), the map \(L_s:R\to R\), \(L_s(x)=x^2+sx\), is additive. Every nonempty fiber is therefore a coset of \(\ker L_s\), and its cardinality is \(|\ker L_s|\). For fixed \(s\), exactly \(q^k/|\ker L_s|\) choices of \(p\) have predecessors.

We determine the kernel without an appeal to a choice of coefficients. Its defining equation is \(x(x+s)=0\).

If \(\nu(s)=v\) and \(2v<k\), the nonarchimedean valuation rules show that a solution cannot have \(\nu(x)<v\): then \(\nu(x+s)=\nu(x)\) and \(\nu(x(x+s))=2\nu(x)<k\). A solution with \(\nu(x)>v\) must satisfy \(\nu(x)+v\ge k\), hence belongs to \(J^{k-v}\). A solution with \(\nu(x)=v\) must have \(\nu(x+s)\ge k-v\), hence belongs to \(s+J^{k-v}\). Conversely, every element of either coset solves the equation. Since \(k-v>v\), the two cosets are disjoint and each has \(q^v\) elements. Consequently,
\[
 |\ker L_s|=2q^v\quad(2v<k).
\]

If \(2\nu(s)\ge k\), including \(s=0\), then \(s\in J^{\lceil k/2\rceil}\). Any \(x\in J^{\lceil k/2\rceil}\) satisfies \(x(x+s)=0\). Conversely, if \(\nu(x)<\lceil k/2\rceil\), then \(\nu(x)<\nu(s)\), so \(\nu(x+s)=\nu(x)\) and \(2\nu(x)<k\), contradicting the kernel equation. Therefore
\[
 \ker L_s=J^{\lceil k/2\rceil},\qquad |\ker L_s|=q^{\lfloor k/2\rfloor}.
\]

For \(0\le v<h\), exactly \((q-1)q^{k-v-1}\) elements \(s\) have \(\nu(s)=v\). Each supplies \(q^k/(2q^v)\) target vertices of in-degree \(2q^v\); multiplying gives \((q-1)q^{2k-2v-1}/2\). The \(q^{k-h}=q^{\lfloor k/2\rfloor}\) elements \(s\in J^h\) each supply \(q^k/q^{\lfloor k/2\rfloor}\) targets of in-degree \(q^{\lfloor k/2\rfloor}\), yielding exactly \(q^k\) targets. Summing these strata proves the formula for positive degrees. Subtraction from \(|R^2|=q^{2k}\) proves the zero-degree formula.

The largest low-valuation fiber size is \(2q^{h-1}\), while the high-valuation fiber size is \(q^{\lfloor k/2\rfloor}\). If \(k=2m\), these are \(2q^{m-1}\le q^m\), since \(q\ge2\), giving maximum \(q^m\). If \(k=2m+1\), they are \(2q^m\) and \(q^m\), giving maximum \(2q^m\). Both are attained because the indicated valuation strata are nonempty. This proves the sharp assertion. \(\square\)

## Verification
The standalone file `verify.py` computes every image of \(\Phi\) directly for \(R=\mathbb F_q[t]/(t^k)\), using polynomial arithmetic with explicit binary finite-field multiplication. It does **not** call the kernel-count formula to produce its observed histograms. It compares the observed number of targets of each in-degree with the closed formula and checks the total number of arrows. All tested cases passed: \(q=2\) through \(k=9\), \(q=4\) through \(k=4\), and \(q=8\) through \(k=3\). The output is in `VERIFICATION_OUTPUT.txt`. In particular, for \((q,k)=(4,3)\) the degree multiplicities at \(0,2,4,8\) are respectively \(2400,1536,64,96\). Computation supplements, but does not replace, the all-length valuation proof.

## Relationship to prior work
Lipkovski's 2012 Proposition 2.1 gives the general identification of in-degree with the number of roots of a quadratic and treats fields; that elementary identification is used here and is **not** new. The 2017 paper describes a squarefree-residue-ring upper bound and surveys cycle structure. Chernev and Chernev (2026) concentrate on connected components and the existence of nontrivial cycles, not the complete incoming-degree census over characteristic-two chain rings. The present result specializes the general root observation to a full multiplicity distribution and sharp maximum for every finite characteristic-two chain ring. It is separate from cyclic-period results for binary chain rings.

## Limitations
The assertion is restricted to characteristic two and finite chain rings; it does not classify incoming degrees in arbitrary Artinian rings or determine global cycle lengths. Earlier literature on finite-ring structure graphs includes studies of sources and quadratic factorization, so historical priority under alternate terminology cannot be guaranteed. The source search and self-review are not independent publication-priority or mathematical certification.

## References
1. A. M. Chernev and N. A. Chernev, *On the Connected Components of Structure Graphs of Associative Rings*, arXiv:2611.07521v1 (first posted 2026-11-05), https://arxiv.org/abs/2611.07521.
2. A. T. Lipkovski, *Digraphs associated with finite rings*, Publications de l'Institut Mathématique 92(106), 35–41 (2012), https://doi.org/10.2298/PIM1206035L.
3. A. T. Lipkovski, *Structure Graphs of Rings: Definitions and First Results*, Journal of Mathematical Sciences 225, 658–665 (2017), https://doi.org/10.1007/s10958-017-3484-3.
4. C. Ang and A. Shulte, *Directed Graphs of Commutative Rings with Identity*, Rose-Hulman Undergraduate Mathematics Journal 14(1) (2013), https://scholar.rose-hulman.edu/rhumj/vol14/iss1/7/.
