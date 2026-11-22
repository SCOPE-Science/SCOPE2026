# Alternating gap-block multiplicities for quotients of three consecutive coin systems

## Finding
Let \(p\ge3\) and \(k\ge2\) be integers. Define the numerical semigroup quotient
\[
Q_{p,k}=\{n\in\mathbb Z_{\ge0}:pn=x(pk+1)+y(pk+2)+z(pk+3)\text{ for some }x,y,z\in\mathbb Z_{\ge0}\}.
\]
A gap block means a maximal nonempty interval of consecutive positive integers outside \(Q_{p,k}\). Let \(H_{p,k}(\ell)\) count these blocks of length \(\ell\), and put
\[
t_p=\left\lceil\frac p3\right\rceil,\qquad
c_p=\left\lceil\frac{2p}{3}\right\rceil-\left\lceil\frac p3\right\rceil.
\]
Then the **complete block-length histogram** is
\[
\boxed{H_{p,k}(\ell)=
\begin{cases}
1,&\ell=kt_p,\\
c_p,&1\le\ell<k\ \text{and }k-\ell\text{ is odd},\\
p-c_p,&1\le\ell<k\ \text{and }k-\ell\text{ is even},\\
0,&\text{otherwise}.
\end{cases}}
\]
Thus every length from \(1\) through \(k-1\) occurs, with alternating multiplicities, and the unique longest block has length \(kt_p\). When \(p=3\), every length from \(1\) through \(k\) occurs; for every \(p\ge4\), there are **no** block lengths in the interval \([k,kt_p-1]\). This is a sharp phase transition at quotient modulus four.

The number of gap blocks and their total length (the genus) follow:
\[
\boxed{B_{p,k}=1+c_p\left\lfloor\frac k2\right\rfloor+(p-c_p)\left\lfloor\frac{k-1}{2}\right\rfloor,}
\]
\[
\boxed{g_{p,k}=kt_p+p\left\lfloor\frac{(k-1)^2}{4}\right\rfloor+c_p\left\lfloor\frac k2\right\rfloor.}
\]
The principal claim is the full histogram and its sharp support and multiplicity structure; general Frobenius/genus results for such quotients are not claimed as new.

## Assumptions and scope
All \(p,k\) are integers with \(p\ge3\), \(k\ge2\). The three coin denominations \(pk+1,pk+2,pk+3\) are consecutive and therefore have greatest common divisor one. The displayed quotient is cofinite. The interval endpoints refer to ordinary positive integers (not residue classes). The symbol \(\lceil\cdot\rceil\) denotes the ceiling and \(\lfloor\cdot\rfloor\) the floor. All formulas are exact, with no asymptotic qualifier.

## Proof
**1. Interval realization at a fixed coin count.** If a representation uses exactly \(t\) coins from \(pk+1,pk+2,pk+3\), its total is \(t(pk+1)+v\) for some \(0\le v\le2t\). Conversely every such \(v\) is realized (use \(\lfloor v/2\rfloor\) copies of the largest coin, one middle coin when \(v\) is odd, and the remaining smallest coins). Thus the represented multiples of \(p\), divided by \(p\), form exactly the integer interval
\[
J_t=\left[kt+\left\lceil\frac tp\right\rceil,\ kt+\left\lfloor\frac{3t}{p}\right\rfloor\right]\cap\mathbb Z.
\]
For \(1\le t<t_p\), this interval is empty. For \(t_p\le t<p\), its left correction is one and its right correction is at least one; for \(t\ge p\) the right correction is at least the left correction. Hence all \(J_t\) with \(t\ge t_p\) are nonempty. Both endpoints are strictly increasing with \(t\).

**2. The initial block and intervening lengths.** The first positive member of \(Q_{p,k}\) is \(kt_p+1\), so its initial gap block is \([1,kt_p]\), of length \(kt_p\). Between successive nonempty intervals \(J_t,J_{t+1}\), the number of missing integers, if any, is
\[
D_t=\max\left\{0,k+\left\lceil\frac{t+1}{p}\right\rceil-\left\lfloor\frac{3t}{p}\right\rfloor-1\right\}.
\]
Write \(t=pq+r\) with \(0\le r<p\), and let \(j=\lfloor3r/p\rfloor\in\{0,1,2\}\). Since \(\lceil(t+1)/p\rceil=q+1\), the expression inside the maximum is precisely \(k-2q-j\). As \(t\) increases, this expression is nonincreasing: it decreases within each quotient block, and the wraparound from \(r=p-1\) to \(r=0\) changes it by either zero or minus one. Therefore after two intervals touch or overlap, all later intervals connect without a new gap. Each strictly positive expression yields exactly one maximal gap block, with no spurious splitting.

**3. Exact residue multiplicities.** The number of residues \(r\in[0,p-1]\) with \(j=0,1,2\), respectively, is
\[
c_0=t_p,\qquad c_1=c_p,\qquad c_2=p-t_p-c_p.
\]
At \(q=0\), admissible \(t\) starts at \(t_p\), so the \(j=0\) residues are excluded. At every \(q\ge1\), all three classes are admissible. Set \(d=k-\ell\), where \(1\le\ell<k\). When \(d\) is odd, its unique representation \(d=2q+j\) with \(j\in\{0,1,2\}\) uses \(j=1\), contributing exactly \(c_1=c_p\) runs. When \(d\) is even, its two representations use \(j=2\) at \(q=(d-2)/2\) and \(j=0\) at \(q=d/2\). Their contributions are \(c_2+c_0=p-c_p\), including at the boundary \(d=2\), where the \(j=2\) class is admissible at \(q=0\). No further positive \(D_t\) exists. This establishes the complete histogram.

**4. Block and genus sums.** There are \(\lfloor k/2\rfloor\) odd integers in \([1,k-1]\), and \(\lfloor(k-1)/2\rfloor\) even ones, yielding \(B_{p,k}\). Weighting each length by its frequency, and summing the two alternating arithmetic progressions, gives
\[
\sum_{\ell=1}^{k-1}\ell H_{p,k}(\ell)
=p\left\lfloor\frac{(k-1)^2}{4}\right\rfloor+c_p\left\lfloor\frac k2\right\rfloor.
\]
Adding the initial block of length \(kt_p\) gives \(g_{p,k}\). Since \(kt_p\ge k\), that block is uniquely longest. Finally \(t_3=1\) and \(t_p\ge2\) for \(p\ge4\), proving the phase transition.

## Verification
The standalone Python 3 program `verify_gap_spectrum.py` independently constructs coin representability via dynamic programming for each input, extracts maximal missing intervals, and compares every length count and the genus with the theorem. Its executed test suite passed 219 pairs of \((p,k)\), including all \(3\le p\le15\), \(2\le k\le15\), plus larger moduli, with over 2.7 million checked coin-membership positions. It additionally checks neighboring boundary cases \(p=2\) and \(k=1\) outside the stated claim. Run `python verify_gap_spectrum.py` with Python 3 and no external packages.

As an example, for \((p,k)=(7,8)\), the short lengths \(1,3,5,7\) each occur twice, while \(2,4,6\) each occur five times, and the unique long block has length \(24\). Here \(B_{7,8}=24\) and \(g_{7,8}=116\). These finite checks are corroboration, not an infinite proof; the preceding exact interval argument proves the theorem for every allowed parameter pair.

## Relationship to prior work
Liu (2023, arXiv:2312.10889) develops general representation generating functions and generator descriptions for quotients of numerical semigroups, including three-variable cases. The general rational-function construction encodes quotient membership, but the inspected text does not state this two-parameter alternating maximal-gap-length histogram. Liu (2023, arXiv:2312.06096) gives explicit Apéry/Frobenius/genus formulas in several quotient families under a divisor assumption; the present family has \(p\nmid(pk+1)\), so those hypotheses do not apply directly. Komatsu and Ying (2022, arXiv:2206.13052) treat representation thresholds of three-term arithmetic progressions, not this quotient-block statistic. Published 2026 results already establish exact Frobenius and genus quasipolynomials for general quotients of three consecutive denominations. Their inspected proofs also describe the gap intervals of the *unquotiented* semigroup and count their multiples of the modulus. These structural prerequisites are acknowledged as known; they do not state the alternating **maximal quotient-gap block-length histogram** established here. A published half-quotient result supplies a complete gapset for quotient modulus two, expressly excluded from the theorem's domain.

## Limitations
The classification is restricted to the two-parameter family with first coin \(pk+1\) and quotient modulus \(p\), not an arbitrary triple or arbitrary quotient. The originality comparison is provisional even after inspection of the closely related Frobenius/genus proofs: their known original-semigroup interval decomposition, or general quotient-generating-function methods, might yield an equivalent alternating histogram through a different extraction. No independent priority certificate is claimed. The result has not undergone independent mathematical audit. All finite test coverage is bounded; it does not replace the proof.

## References
- F. Liu, *Generating functions for the quotients of numerical semigroups*, arXiv:2312.10889 (first public 2023-12-18), https://arxiv.org/abs/2312.10889; *Bulletin of the Australian Mathematical Society* 110 (2024), 427–438, DOI:10.1017/S0004972724000054.
- F. Liu, *On quotients of numerical semigroups for almost arithmetic progressions*, arXiv:2312.06096 (first public 2023-12-11), https://arxiv.org/abs/2312.06096.
- T. Komatsu and H. Ying, *The \(p\)-numerical semigroup of the triple of arithmetic progressions*, arXiv:2206.13052 (first public 2022-06-27), https://arxiv.org/abs/2206.13052.
- P. A. García-Sánchez, L. González and F. Planas-Vilanova, *Elements with unique length factorization of a numerical semigroup generated by three consecutive numbers*, arXiv:2404.06358, https://arxiv.org/abs/2404.06358 (related unquotiented family).
- *Sharp quotient-Frobenius quasiperiod for three consecutive generators* (2026; public research identifier f97e4a87e254), especially the exact original-semigroup interval lemma.
- *Exact least genus quasiperiod for quotients of three consecutive generators* (2026; public research identifier 972b2eeba586), especially the exact genus floor-sum theorem.
- *Complete pseudo-Frobenius spectra for half-quotients of interval numerical semigroups* (2026; public research identifier 028b7bb60928), concerning the excluded modulus-two case.
