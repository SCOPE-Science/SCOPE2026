# Degree distributions and a four-periodic minimum-degree law for Tribonacci-cube networks

## Finding

For each integer \(n\ge1\), consider the induced subgraph \(\mathcal T_n\) of the binary hypercube with vertices all labelled binary length-\(n\) words having no contiguous `111`. An edge flips exactly one coordinate and retains the constraint. Define the degree polynomial
\[
D_n(t)=\sum_{w\in V(\mathcal T_n)} t^{\deg_{\mathcal T_n}(w)}.
\]
The complete degree distribution, not merely its first moment, has the constant-size rational transfer representation below. Its sharp smallest degree is
\[
\boxed{\delta(\mathcal T_n)=\left\lceil\frac n2\right\rceil+\mathbf1_{\{n\equiv2\pmod4\}}}.
\]
In dimensions divisible by four, the *only* minimum-degree vertex is the word \((0110)^{n/4}\). The largest degree is \(n\); for \(n\ge3\) its exact multiplicity is
\[
\boxed{M_n=\sum_{j\ge0}\binom{n-2j+2}{j}},
\]
with negative or out-of-range binomial arguments interpreted as zero. The multiplicity is \(2^n\) for \(n=1,2\).

## Assumptions and scope

Words are *indexed*, not necklaces. The forbidden factor is three consecutive ones in linear coordinates, with no cyclic wraparound. The graph contains all permitted words, with no fixed-weight restriction. Every edge is an undirected one-bit change. The formula applies at every integer \(n\ge1\), and the transfer construction also defines the empty-length polynomial \(D_0(t)=1\).

For a legal word \(w\), let \(b(w)\) be the number of zero positions at which replacement by one would create `111`. Every one-bit-to-zero replacement remains legal, so
\[
\deg_{\mathcal T_n}(w)=n-b(w).
\]
A zero in the central position of five consecutive bits \((a,b,c,d,e)\), with missing exterior bits taken as zeros, is blocked precisely when
\[
\beta(a,b,c,d,e)=\mathbf1_{\{c=0\}}\,\mathbf1_{\{ab=11\ \mathrm{or}\ bd=11\ \mathrm{or}\ de=11\}}.
\]
Here expressions `ab=11`, `bd=11`, and `de=11` mean the indicated two bits both equal one; no multiplication is intended.

## Proof

**Exact transfer for the whole distribution.** Let \(S\) consist of the thirteen four-bit strings without a `111` factor. For \(s=(a,b,c,d)\in S\) and \(e\in\{0,1\}\) satisfying \((c,d,e)\ne(1,1,1)\), put \(s'=(b,c,d,e)\) and assign the transition the monomial \(u^{\beta(a,b,c,d,e)}\). Sum the weights over transitions to define the \(13\)-by-\(13\) polynomial matrix \(T(u)\); define \(T_0(u)\) by allowing only the appended symbol \(e=0\). Define the row \(v\) to have entry one at each state \((0,0,a,b)\) for \(a,b\in\{0,1\}\) and zero elsewhere, and let \(\mathbf1\) be the all-ones column.

Writing \(B_n(u)=\sum_{w\in V(\mathcal T_n)}u^{b(w)}\), one has \(B_0(u)=1\), \(B_1(u)=2\) and, for every \(n\ge2\),
\[
\boxed{B_n(u)=vT(u)^{n-2}T_0(u)^2\mathbf1}.
\]
Indeed, the initial `00` and terminal `00` are sentinel bits. When a new bit is appended, the five-bit context uniquely determines whether the oldest unscored real bit, now central, is blocked. The first \(n-2\) steps append the remaining real bits, and the final two append zero sentinels; thus every real position is scored once, with no extraneous scoring. All and only `111`-avoiding real words occur, once each. Hence
\[
\sum_{n\ge0}B_n(u)z^n=1+2z+z^2v(I-zT(u))^{-1}T_0(u)^2\mathbf1
\]
is rational, and \(D_n(t)=t^nB_n(t^{-1})\) gives every degree multiplicity. The construction specifies each matrix entry without hidden numerical data.

**Sharp lower bound on degree.** Decompose the ones in \(w\) into maximal runs; each run has length one or two. Write \(r_1\) and \(r_2\) for their counts. Every blocked zero either touches a length-two ones-run or lies in a `101` factor between two singleton ones-runs. Each double-run touches at most two blocked zeros. The additional `101` zeros form gaps between consecutive singleton ones-runs, so there are at most \(r_1-1\) of them when \(r_1>0\). Consequently \(b(w)\le 2r_2+r_1\), strictly when \(r_1>0\). Since \(2r_2+r_1\) is the number of ones and \(b(w)\) cannot exceed the number of zeros, always
\[
b(w)\le\left\lfloor\frac n2\right\rfloor.
\]
If \(n\equiv2\pmod4\) and equality held, the numbers of ones and zeros would both equal \(n/2\), and equality \(b(w)=\#\text{ones}\) would preclude singleton ones-runs. Every double-run would need two *distinct* flanking blocked zeros and every zero would have to be one of these. Then all internal gaps between double-runs must have exactly two zeros, and each boundary must have exactly one zero: the word would be \((0110)^r\), of length divisible by four. Contradiction. Thus for \(n\equiv2\pmod4\) the upper bound on \(b\) improves by one.

Every one of these bounds is attained. For \(n=4r,4r+1,4r+2,4r+3\), respectively, use
\[
(0110)^r,\qquad (0110)^r0,\qquad (0110)^r00,\qquad (0110)^r011.
\]
The small cases \(n=1,2,3\) are included. Substituting \(\deg(w)=n-b(w)\) proves the displayed minimum degree. When \(4\mid n\), equality forces no singleton ones-runs and all adjacent-blocked-zero conditions to be tight, uniquely giving \((0110)^{n/4}\).

**Largest degree.** Degree \(n\) means no zero is blocked. For \(n\ge3\), this holds exactly when every three consecutive coordinates contain at most one one, so any two ones are separated by at least two zeros. If there are \(j\) ones, removing two obligatory zeros after each of the first \(j-1\) ones gives \(\binom{n-2j+2}{j}\) strings. Summing over \(j\) yields the claimed multiplicity. In dimensions one and two no triple can exist, so all \(2^n\) vertices have degree \(n\).

## Verification

The attached standard-library program `verify.py` constructs the transition dynamic program independently of an exhaustive graph enumerator. It checks all vertex degrees by individually flipping every bit of every legal word for each \(0\le n\le17\), comparing the entire distribution to the transfer output. It additionally checks the minimum formula, the unique minimum-degree state at multiples of four, the maximum-degree count, and the expected Tribonacci vertex count for \(1\le n\le84\). These finite checks test the implementation; the infinite assertion follows from the preceding combinatorial argument.

Examples, displaying degree followed by multiplicity, are: \(n=4\): \((2,1),(3,6),(4,6)\); \(n=6\): \((4,17),(5,14),(6,13)\); and \(n=8\): \((4,1),(5,24),(6,60),(7,36),(8,28)\).

## Relationship to prior work

Hassler, Vajnovszki and Wong (2024, arXiv:2406.16405v1) study Gray-code generation for constrained binary words, with their main fixed-weight results using different transpositions; they neither state this whole-degree distribution nor its minimum-degree law. Rho and Vesel (2016, Section 3, especially Lemma 3.6) recognize generalized Fibonacci cubes and give a local degree-deficiency characterization; that earlier local idea is explicitly *not* claimed as new. Azarija, Klavžar, Lee and Rho (2015) study connectivity and minimum degrees of the ordinary `11`-avoiding Fibonacci cubes and raise a broader generalized-cube question. Belbachir and Ould-Mohamed (2020) count vertices by weight, total edges and induced cubes for the `111`-avoiding graph, which do not themselves specify the distribution of ordinary vertex degrees. The last article's full body could not be inspected, so historical priority for a possible equivalent refinement remains uncertain.

## Limitations

Only the linear `111` constraint, one-coordinate flips and finite indexed words are covered. No equality between graph connectivity and minimum degree is asserted. The rational transfer description is an exact algorithmic formula rather than a factored minimal-denominator closed form. The displayed finite enumerations are not substitutes for the all-length proof. Comparison of the full body of the 2020 Tribonacci-cube enumeration article remains an outstanding historical-priority risk; independent validation of the present proof has not been performed.

## References

1. N. Hassler, V. Vajnovszki, D. Wong, *Greedy Gray Codes for some Restricted Classes of Binary Words*, 2024, arXiv:2406.16405v1, https://arxiv.org/html/2406.16405v1 (first posted 2024-06-24).
2. Y. Rho and A. Vesel, *Linear recognition of generalized Fibonacci cubes Q_h(111)*, Discrete Mathematics & Theoretical Computer Science 17(3), 2016, https://doi.org/10.46298/dmtcs.2165.
3. J. Azarija, S. Klavžar, J. Lee, Y. Rho, *Connectivity of Fibonacci cubes, Lucas cubes and generalized cubes*, Discrete Mathematics & Theoretical Computer Science 17(1), 2015, https://doi.org/10.46298/dmtcs.2115.
4. H. Belbachir and R. Ould-Mohamed, *Enumerative properties and cube polynomials of Tribonacci cubes*, Discrete Mathematics 343(8), 2020, https://doi.org/10.1016/j.disc.2020.111922.
