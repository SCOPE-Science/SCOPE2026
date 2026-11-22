# Rank-refined inverse fibers of two-point addition in reduced finitary power monoids

## Finding

For \(d\ge 1\), a nonzero \(v\in\mathbb N_0^d\), and a finite \(T\subset\mathbb N_0^d\) containing the origin, count every finite \(Y\) containing the origin such that \(Y+\{0,v\}=T\), recording \(|Y|\). A complete, arbitrary-target answer is a product of explicit binomial polynomials over the maximal consecutive \(v\)-runs of \(T\). Among all targets of the same cardinality, one consecutive run is uniquely optimal **at every input cardinality simultaneously**.

Define
\[
H_{T,v}(z)=\sum_{\substack{0\in Y\subset\mathbb N_0^d\\Y+\{0,v\}=T}}z^{|Y|},\qquad
h_\ell(z)=\sum_{r=\lceil\ell/2\rceil}^{\ell-1}\binom{r-1}{\ell-1-r}z^r\quad(\ell\ge2).
\]
The sum is finite because any summand \(Y\) must lie in \(T\). Partition \(T\) into its maximal consecutive strings in the direction \(v\), with lengths \(\ell_1,\ldots,\ell_s\). Then
\[
H_{T,v}(z)=\begin{cases}0,&\text{if some }\ell_j=1,\\\prod_{j=1}^s h_{\ell_j}(z),&\text{otherwise.}\end{cases}
\]
For every \(t=|T|\ge2\), the coefficientwise inequality
\[
H_{T,v}(z)\preccurlyeq h_t(z)
\]
holds, and equality of polynomials holds exactly for \(T=\{0,v,2v,\ldots,(t-1)v\}\). Thus, for each integer \(r\), the number of rank-\(r\) input factors is at most \(\binom{r-1}{t-1-r}\), with the convention that the binomial is zero outside its admissible range. The greatest total fiber size is \(F_{t-1}\), where \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\), and its unique maximizing target is that single \(v\)-run.

## Assumptions and scope

Here \(\mathbb N_0\) consists of nonnegative integers, \(d\) is any positive integer, \(v\ne0\) has nonnegative coordinates, and \(T\) is finite and contains \(0\). Addition of finite sets is Minkowski addition. We work in the reduced finitary power monoid \(\mathcal P_{\mathrm{fin},0}(\mathbb N_0^d)\), with identity \(\{0\}\). An algebraic fiber is the set of all admissible \(Y\), not a count of additive representations \((y,e)\). Since the ambient monoid is torsion-free, each \(\mathbb Zv\)-coset intersects \(T\) in one or more disjoint finite runs. A maximal run means \(\{a,a+v,\ldots,a+(\ell-1)v\}\subseteq T\) whose predecessor \(a-v\) and successor \(a+\ell v\) do not belong to \(T\); the predecessor may be outside the nonnegative orthant. Each point is in one such run. For \(|T|=1\), the fiber is empty (the formula with a singleton run gives zero). No claim is made for \(v=0\), noncancellative base monoids, or infinite sets.

## Proof

**Run localization.** If \(Y+\{0,v\}=T\), then \(Y\subseteq T\). Every \(y\in Y\) requires both \(y\) and \(y+v\) in \(T\). Therefore \(y\) lies in a run but cannot be its final point. Distinct runs cannot interact under addition of either \(0\) or \(v\): the image of a point lies in the same \(\mathbb Zv\)-coset and is adjacent to that point, and maximal runs are separated by at least one missing point. In a run \(R=\{a,a+v,\ldots,a+(\ell-1)v\}\), the first and last target points have to be covered. The first has only \(a\) as a possible input, and the last only \(a+(\ell-2)v\), so both inputs are required. If \(\ell=1\), there is no input whose translate covers the unique target point without leaving \(T\), hence the full fiber is empty.

**Local polynomial.** Let \(\ell\ge2\). Represent choices among the \(\ell-1\) input positions by bits \(b_0,\ldots,b_{\ell-2}\). The target run is covered if and only if \(b_0=b_{\ell-2}=1\) and no two successive bits are both zero (for \(\ell=2\), the endpoint conditions coincide). If exactly \(r\) input positions are selected, there are \(q=\ell-1-r\) unselected positions, none at an endpoint and no two consecutive. The \(r\) ones define \(r-1\) interior gaps in which at most one zero may be inserted. Hence the number is \(\binom{r-1}{q}=\binom{r-1}{\ell-1-r}\); permissible \(r\) range from \(\lceil\ell/2\rceil\) through \(\ell-1\). Choices on different runs are independent. The first target run starts at \(0\), because \(T\) contains \(0\) and \(v\) has nonnegative coordinates, so the forced first input there is \(0\). Thus all constructed inputs belong to the reduced monoid. Multiplying local polynomials gives the asserted fiber formula.

**Coefficientwise extremum.** A monomial of \(h_a(z)h_b(z)\) corresponds to a pair of allowable bitstrings of lengths \(a-1\) and \(b-1\), with endpoints equal to one and no consecutive zeroes. Send the pair \((u,w)\) to the concatenated string \(u0w\). Its length is \(a+b-1\), its endpoints are one, and its zeros are still nonadjacent because the inserted zero is flanked by ones. The map is injective, because the insertion position is fixed, and preserves the number of ones. Consequently \(h_a(z)h_b(z)\preccurlyeq h_{a+b}(z)\). By repeated merging, every product over runs of total length \(t\) is coefficientwise at most \(h_t\). If any run is a singleton the polynomial is identically zero. If all runs have length at least two but there are at least two runs, the largest possible degree of the product is \(\sum_j(\ell_j-1)=t-s<t-1\), while \(h_t\) has a term \(z^{t-1}\) with coefficient one. Thus equality occurs only for a single run. Such a run must start at the origin: otherwise the target would not contain zero. Hence the unique equality case is \(T=\{0,v,\ldots,(t-1)v\}\).

**Fibonacci evaluation.** The total number of allowable bitstrings of length \(\ell-1\) with forced endpoint ones is the number of length-\(\ell-3\) binary interior strings without consecutive zeroes, for \(\ell\ge3\), which is \(F_{\ell-1}\). The case \(\ell=2\) also has one solution, equal to \(F_1\). Evaluating the coefficientwise inequality at \(z=1\) yields the maximal total fiber \(F_{t-1}\), and strict inequality of the top coefficient yields uniqueness of the maximizing target for \(t\ge3\); for \(t=2\), a nonzero fiber requires the single length-two run, also unique.

## Verification

The accompanying standalone Python program `verify.py` checks the exact polynomial against exhaustive enumeration of all reduced input sets for all targets containing the origin on one-dimensional grids of lengths two through nine and a two-dimensional three-by-three grid, using multiple primitive and nonprimitive step vectors. It compared 3,066 target/step configurations and produced `VERIFY_OK`. An independent combinatorial check enumerates all compositions into run lengths at least two through total size sixteen, checking coefficientwise dominance and the Fibonacci sum. These finite checks are reproducibility evidence, not substitutes for the proof above.

## Relationship to prior work

Xu and Wong [1, Lemma 3.4] counted exactly \(2^{|X|}\) factors in the specially separated equation \(Y+\{0,w\}=X+\{0,w,2w,3w\}\). In the present notation, these special targets have \(|X|\) separate runs of length four, for which \(h_4(z)=z^2+z^3\), so the unrefined count \(h_4(1)^{|X|}=2^{|X|}\) is **already known**, not new. The proposed extension is an exact, rank-refined formula for every target and the sharp coefficientwise inequality with its unique extremizer. Rago [2] studies the isomorphism problem for reduced finitary power monoids, and Fan and Tringali [3] study their factorization arithmetic; their reviewed sections do not state the full arbitrary-target rank-polynomial formula. Tringali and Yan [4] study automorphisms of reduced power monoids. The identity of binary dilation with Minkowski addition is classical [5]; the novelty claim concerns this specific exact fiber distribution and extremum, not the general run decomposition idea or binary morphology.

## Limitations

The mathematical assertion is limited to finite sets over the torsion-free, nonnegative additive lattice and to multiplication by one two-point set. The central run-counting ingredients are elementary and related to standard Fibonacci tilings; historical priority could be affected by older work phrased in binary mathematical morphology, inverse Boolean convolution, or cellular preimage enumeration. The cited recent Lemma 3.4 is a genuine covered special case. This proof is a mathematical derivation with finite consistency tests, not an externally audited theorem; it does not claim a larger factorization-theoretic consequence.

## References

1. Songnian Xu and Dein Wong, *Automorphisms of the Reduced Finitary Power Monoid of \(\mathbb N^d\)*, arXiv:2611.13956v1 (first public November 10, 2026), especially Lemma 3.4. https://arxiv.org/abs/2611.13956
2. Balint Rago, *The isomorphism problem for reduced finitary power monoids*, arXiv:2601.22469v1 (January 30, 2026). https://arxiv.org/abs/2601.22469
3. Yushuang Fan and Salvatore Tringali, *Power monoids: A bridge between Factorization Theory and Arithmetic Combinatorics*, arXiv:1701.09152v6 (2018), published in *Journal of Algebra* 512, 252–294. https://arxiv.org/abs/1701.09152
4. Salvatore Tringali and Qinghai Yan, *On power monoids and their automorphisms*, arXiv:2312.04439 (2023). https://arxiv.org/abs/2312.04439
5. Standard binary mathematical morphology: dilation of finite point sets equals Minkowski addition by a structuring element; see the definition of binary dilation, https://en.wikipedia.org/wiki/Dilation_(morphology).
