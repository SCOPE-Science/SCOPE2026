# Rank–nilpotency spectra and arithmetic upper tails in cyclic inverse monoids

## Finding

For every integer \(n\ge2\), let \(\Omega_n=\mathbb Z/n\mathbb Z\), let \(g(i)=i+1\), and let \(\mathcal{CI}_n\) consist of the empty partial map \(0\) and all nonempty restrictions \(g^k|_A\), where \(k\in\Omega_n\) and \(\varnothing\ne A\subseteq\Omega_n\). A map is nilpotent when a positive power is \(0\); its nilpotency index \(\nu(f)\) is the least such power, with \(\nu(0)=1\). Its rank is \(|\operatorname{dom}(f)|\).

Let \(t\ge1\), and define the \(t\)-state weighted transition matrix \(M_t(z)\), with rows and columns indexed by \(0,\ldots,t-1\), by
\[
(M_t(z))_{i,0}=1\quad(0\le i<t),\qquad
(M_t(z))_{i,i+1}=z\quad(0\le i<t-1),
\]
with all other entries zero. Then the complete cumulative joint rank–nilpotency enumerator is
\[
\boxed{C_{n,t}(z)=\sum_{\substack{f\in\mathcal{CI}_n\\ f^t=0}}z^{\operatorname{rank}f}
=1-n+\sum_{d\mid n}\varphi(d)\bigl(\operatorname{tr}(M_t(z)^d)\bigr)^{n/d}.}
\]
For each \(2\le t\le n\), the difference \(C_{n,t}(z)-C_{n,t-1}(z)\) counts elements with nilpotency index exactly \(t\), by rank; \(C_{n,1}(z)=1\). In particular, the polynomial counting every nilpotent element by rank is
\[
\boxed{N_n(z)=1-n+\sum_{d\mid n}\varphi(d)
\big((1+z)^d-z^d\big)^{n/d}.}
\]
The total number of nilpotents is \(N_n(1)=1-n+\sum_{d\mid n}\varphi(d)(2^d-1)^{n/d}\).

There is a sharp arithmetic upper tail: for every integer \(t\) satisfying \(n/2<t<n\),
\[
\boxed{\sum_{\nu(f)=t}z^{\operatorname{rank}f}
=n\varphi(n)z^{t-1}(1+z)^{n-t-1},}
\]
while at the maximal index \(t=n\) the exact polynomial is \(n\varphi(n)z^{n-1}\). Hence the number of maximal-index nilpotents is \(n\varphi(n)\), and for \(n/2<t<n\) the number of index-\(t\) nilpotents is \(n\varphi(n)2^{n-t-1}\). Thus the upper half of the nilpotency-index spectrum has a universal binomial rank profile and an Euler-totient factor.

If \(F_n\) is uniform on the nilpotent elements of \(\mathcal{CI}_n\), then, over every sequence of integers \(n\to\infty\),
\[
\boxed{\frac{\nu(F_n)}{\log_2 n}\xrightarrow{\mathbb P}1.}
\]
The nilpotent elements themselves form an asymptotically full proportion of \(\mathcal{CI}_n\). These are ordinary finite-semigroup probability assertions, with no assumption that \(n\) is prime.

## Assumptions and scope

The ground set is labeled, and elements of the monoid are actual partial maps, not conjugacy classes. The empty restriction is one element, independent of its ambient rotation. For a nonempty domain, the ambient rotation is unique (Fernandes, Lemma 1.1), so the \(n\) rotations do not create duplicates. The polynomial variable \(z\) records the cardinality of the domain (the rank of a partial injection). Euler's totient function \(\varphi(d)\) counts elements of order \(d\) in the cyclic group of order \(n\), for each divisor \(d\mid n\). Matrices are over \(\mathbb Z[z]\), not over a finite field. The formulas hold without a primality restriction on \(n\).

## Proof

**1. Powers and rotation cycles.** Fix a rotation \(g^k\) of order \(d=n/\gcd(n,k)\), with \(n/d\) disjoint cycles of length \(d\). For a domain \(A\), the restriction \(f=g^k|_A\) has \(f^t\ne0\) precisely if some orbit cycle contains \(t\) consecutive (possibly cyclically repeated) vertices of \(A\). If a whole rotation orbit lies in \(A\), every power of \(f\) is nonzero. Otherwise each orbit is broken into finite directed paths; the longest block of consecutive domain sites, plus one, is \(\nu(f)\). Consequently \(f^t=0\) if and only if, on every rotation orbit, the binary indicator word of \(A\) has no cyclic run of \(t\) ones. In particular, the all-ones word is forbidden for every \(t\ge1\), including \(t>d\), since its periodic extension has arbitrarily long runs.

**2. Weighted cyclic words.** State \(i\in\{0,\ldots,t-1\}\) records the number of consecutive ones since the last zero. Appending zero sends every state to zero, with weight one; appending one sends state \(i<t-1\) to \(i+1\), with weight \(z\). These are exactly the nonzero entries of \(M_t(z)\). A cyclic word containing a zero and avoiding \(t\) ones has a unique closed state trajectory, since each state at a cut is forced by the last zero. The all-ones word has no closed trajectory: without a reset, state indices strictly increase. Conversely, a closed trajectory encodes exactly such a cyclic word. Hence \(\operatorname{tr}(M_t(z)^d)\) is the polynomial enumerating allowed length-\(d\) labeled cyclic words by their number of ones. The \(n/d\) orbit words are independent choices, so the contribution of a rotation of order \(d\) is the corresponding trace raised to \(n/d\). There are \(\varphi(d)\) such rotations. Every empty restriction is represented once for each of the \(n\) rotations; replacing those \(n\) copies by the one actual zero map subtracts \(n-1\), proving the formula for \(C_{n,t}(z)\).

**3. All nilpotents.** Because a proper subset of a \(d\)-cycle has maximum cyclic run at most \(d-1\), the length-\(d\) words accepted when \(t=n\ge d\) are precisely all words except the all-ones word. Their weight polynomial is \((1+z)^d-z^d\). Also, every nilpotent partial map on \(n\) points has index at most \(n\), because it is a disjoint union of directed chains. Substitute this polynomial in the previous divisor sum to obtain \(N_n(z)\).

**4. Sharp upper tail.** If \(\nu(f)=t>n/2\), the order \(d\) of its ambient rotation must be at least \(t\): no nilpotent restriction of a permutation with \(d\)-cycles has index exceeding \(d\). Every proper divisor of \(n\) is at most \(n/2\); hence \(d=n\), and there are \(\varphi(n)\) possible rotations. Their action consists of one labeled \(n\)-cycle. For \(n/2<t<n\), an index-\(t\) restriction has a block of exactly \(t-1\) successive domain sites, flanked by two omitted sites. This block is unique: two distinct maximal blocks of that length would require at least \(2t\) cycle sites. Its starting site has \(n\) choices, and the remaining \(n-t-1\) sites are arbitrary. No second run can equal or exceed \(t-1\), because \(n-t-1<t-1\). Thus the rank polynomial is \(n\varphi(n)z^{t-1}(1+z)^{n-t-1}\). For \(t=n\), there is one missing site and \(n\) choices for it, yielding \(n\varphi(n)z^{n-1}\).

**5. Uniform logarithmic index.** First sample \(K\) uniformly from \(\mathbb Z/n\mathbb Z\) and, independently, a uniform subset \(A\); collapse all empty restrictions to zero. This induces a distribution on \(\mathcal{CI}_n\) whose total-variation distance from the uniform distribution is at most \(2^{1-n}\): the only multiplicity discrepancy is at zero. Let \(d\) be the order of \(g^K\). For any integer \(s\ge1\),
\[
\Pr(d<s)\le\frac1n\sum_{j=1}^{s-1}\varphi(j)\le\frac{s^2}{2n}.
\]
When \(d\ge s\), there are \(n/d\) cycles of length \(d\), containing at least \((n/d)\lfloor d/s\rfloor\ge n/(2s)\) mutually disjoint consecutive blocks of \(s\) sites. The events that these blocks lie wholly in \(A\) are independent, each with probability \(2^{-s}\). Therefore
\[
\Pr(\nu\le s)\le\frac{s^2}{2n}+\exp\bigl(-n2^{-s}/(2s)\bigr),
\]
where \(\nu=\infty\) for a nonnilpotent map. For the opposite tail, when \(d\ge s\), any occurrence of \(s\) consecutive sites of \(A\) uses distinct sites, and there are at most \(n\) possible starting sites. Thus a union bound gives
\[
\Pr(\nu>s)\le\frac{s^2}{2n}+n2^{-s}.
\]
For fixed \(0<\epsilon<1\), take respectively \(s=\lfloor(1-\epsilon)\log_2n\rfloor\) in the first inequality and \(s=\lceil(1+\epsilon)\log_2n\rceil\) in the second. Both right-hand sides tend to zero. In particular the probability of nonnilpotence tends to zero. Conditioning on nilpotence and passing from the pair-sampling law to the uniform law on actual monoid elements does not change the limiting statement, proving the logarithmic concentration.

## Verification

Run `python3 verify_cyclic_spectrum.py` using Python's standard library. It enumerates every nonempty restriction of every rotation for \(2\le n\le10\), computes powers as partial maps until zero or a repeat, and records rank and least zero power; zero is recorded once. Independently, it constructs the polynomial transfer matrix \(M_t(z)\) and its traces over integer polynomial dictionaries, verifies every coefficient of every cumulative spectrum \(C_{n,t}(z)\), and tests every coefficient in the exact upper-tail rank law. It also compares the total nilpotent count against the divisor sum. The check prints `VERIFY_OK` only after all assertions succeed. This finite verification does not replace the general proof or establish asymptotic results.

For illustration, at \(n=6\) the exact index histogram (summed over ranks) is \((1,90,108,24,12,12)\), indexed by the nilpotency indices \(1,2,3,4,5,6\), respectively. At \(n=8\), it is \((1,360,480,448,128,64,32,32)\), and the final four counts agree with the upper-tail formula. These are counts within \(\mathcal{CI}_n\), not within the full symmetric inverse monoid.

## Relationship to prior work

Fernandes, *On the cyclic inverse monoid on a finite set* (arXiv:2211.02155, first posted 2022-11-03), introduces the exact monoid considered here and establishes its size \(n2^n-n+1\), rank two, and presentations. The original full text was inspected, including its size/rank and presentation sections; no rank–nilpotency-index distribution or arithmetic upper-tail formula was found there. Its unique-extension Lemma 1.1 is used as an established fact.

Elliott, Levine, and Mitchell, *Counting monogenic monoids and inverse monoids* (arXiv:2303.12387, first posted 2023-03-22), classify and count isomorphism types of monogenic submonoids of full transformation and symmetric inverse monoids using threshold and period. That is a different enumerative question: it does not supply the number of *elements* of each nilpotency index and rank in the cyclically restricted inverse monoid.

OEIS A261764 records the number of nilpotent subpermutations on a labeled set, by bounded index, for the full symmetric inverse monoid. The full-monoid counts do not recover the cyclically restricted spectrum: for instance, the number of nilpotents at size four is \(73\) in the unrestricted symmetric inverse monoid but \(37\) here. Counting forbidden cyclic binary runs with transfer matrices is a standard technique; the contribution is its divisor-arithmetic assembly for this particular inverse monoid, the fully rank-refined index spectrum, and the exact totient-controlled upper half.

## Limitations

The theorem concerns restrictions of one fixed regular cyclic permutation group on a labeled set, not arbitrary partial permutations, general group actions, or the order-preserving submonoid. The limit is only first-order logarithmic concentration, not a centered extreme-value limit. Computational checks are exhaustive only for \(2\le n\le10\). Existing results on general cycle decompositions and forbidden-run transfer matrices are ingredients, not claimed as newly discovered. It remains possible that an equivalent bivariate spectrum has appeared under different terminology in less accessible literature; no exhaustive priority certification is asserted.

## References

1. V. H. Fernandes, *On the cyclic inverse monoid on a finite set*, arXiv:2211.02155 (initial submission 2022-11-03), https://arxiv.org/abs/2211.02155 . Primary MSC2020: 20M20.
2. L. Elliott, A. Levine, J. D. Mitchell, *Counting monogenic monoids and inverse monoids*, arXiv:2303.12387 (initial submission 2023-03-22), https://arxiv.org/abs/2303.12387 .
3. OEIS A261764, *Triangle of nilpotent subpermutations by maximum nilpotency index*, https://oeis.org/A261764 .
