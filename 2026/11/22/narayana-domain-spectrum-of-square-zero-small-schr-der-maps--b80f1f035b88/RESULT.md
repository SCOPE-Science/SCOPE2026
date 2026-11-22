# Narayana domain spectrum of square-zero small Schröder maps

## Finding
For every integer \(n\ge 2\), let \(\mathcal{SS}'_n\) consist of the partial maps \(f:D\to[n]\), where \(D\subseteq\{2,\dots,n\}\), \(f\) is isotone, and \(f(i)\le i\) on its domain. The zero is the empty map. For every \(0\le k\le n-1\), the number of elements with square equal to zero and domain size \(k\) is exactly
\[
Q_{n,k}:=\#\{f\in\mathcal{SS}'_n:f^2=0,\ |\operatorname{Dom} f|=k\}
=\frac1n\binom nk\binom n{k+1}
=\frac1{k+1}\binom nk\binom{n-1}k.
\]
Thus the domain spectrum is the Narayana row \(Q_{n,k}=N(n,k+1)\), and the full square-zero census is the Catalan number
\[
\#\{f\in\mathcal{SS}'_n:f^2=0\}
=\frac1{n+1}\binom{2n}{n}.
\]
Under the uniform distribution on this square-zero subset, its domain size \(K\) has exactly
\[
\mathbb E K=\frac{n-1}{2},\qquad
\operatorname{Var}(K)=\frac{n^2-1}{4(2n-1)}.
\]
The total number of nilpotent elements of \(\mathcal{SS}'_n\) is the large Schröder number \(R_{n-1}\), and so the fraction of nilpotent elements that are square-zero is
\[
\frac{\frac1{n+1}\binom{2n}n}{R_{n-1}}
=\Theta\!\left(\left(\frac4{3+2\sqrt2}\right)^n\right).
\]
The exponent is strictly less than one; in particular the square-zero condition is exponentially rare within nilpotency.

## Assumptions and scope
Composition is ordinary composition of partial functions; an undefined composition produces no domain point. Nilpotent means that a finite positive power is the empty partial map; square-zero means the *second* power is empty, not merely that an image-rank ideal quotient vanishes. Domain size \(k\) is distinct from image rank (which can be smaller when values repeat). The statements hold for every \(n\ge2\) and include the zero map with \(k=0\); no claim is made about the convention for \(n=1\).

## Proof
**Structural correspondence.** Fix \(D=\{d_1<\dots<d_k\}\subseteq\{2,\dots,n\}\) and write its complement as \(E=\{e_1<\dots<e_m\}\), where \(m=n-k\). Since \(f^2=0\) is equivalent to \(\operatorname{Im}f\cap D=\varnothing\), there are uniquely determined integers \(j_i\) with \(f(d_i)=e_{j_i}\). Define \(x_i=d_i-i\), the number of complement elements strictly below \(d_i\). The conditions that \(D\) omit one, \(f\) be isotone, and \(f(d_i)\le d_i\), together with disjointness, are exactly
\[
1\le x_1\le\cdots\le x_k\le m,\quad
1\le j_1\le\cdots\le j_k\le m,\quad j_i\le x_i.
\]
Indeed, \(e_{j_i}<d_i\) follows precisely from \(j_i\le x_i\). Conversely, any such pair of weakly increasing sequences determines a unique increasing domain \(d_i=x_i+i\) and a unique square-zero map \(f(d_i)=e_{j_i}\) with the requisite properties. This proves a bijection, including when \(k=0\).

**Enumeration.** Reverse the two rows \((x_i)\) and \((j_i)\) and subtract one from every entry. This yields a plane partition in a \(2\times k\) rectangle with parts at most \(m-1\), and every such partition arises. The rectangular plane-partition product formula gives
\[
Q_{n,k}=\prod_{b=1}^k
\frac{m+b-1}{b}\frac{m+b}{b+1}
=\binom{n-1}k\frac{\binom nk}{k+1}.
\]
Alternatively, the two-row array can be counted by the two-row nonintersecting-lattice-path determinant, so the product identity does not require experimental extrapolation. The equality to \(\frac1n\binom nk\binom n{k+1}\) follows from the binomial identity. Summing by Vandermonde gives
\[
\sum_{k=0}^{n-1}Q_{n,k}
=\frac1n\binom{2n}{n-1}
=\frac1{n+1}\binom{2n}n.
\]

**Moments.** The first two factorial moments follow from \(k\binom nk=n\binom{n-1}{k-1}\), \(k(k-1)\binom nk=n(n-1)\binom{n-2}{k-2}\), and Vandermonde, with out-of-range binomial coefficients interpreted as zero:
\[
\sum kQ_{n,k}=\binom{2n-1}{n-2},\qquad
\sum k(k-1)Q_{n,k}=(n-1)\binom{2n-2}{n-3}.
\]
After division by the Catalan total and using \(K^2=K(K-1)+K\), simplification yields the asserted mean and variance (including \(n=2\)).

**All nilpotents.** Because every map is order decreasing on a finite chain, a directed cycle can only be a fixed point. Thus \(f\) is nilpotent precisely if \(f(i)<i\) for all \(i\in D\). Send such a map to the partial map \(g\) on \([n-1]\) with domain \(D-1\) and values \(g(i-1)=f(i)\). This is a bijection with all isotone order-decreasing partial maps on \([n-1]\), counted by the large Schröder number \(R_{n-1}\) (Laradji–Umar). The standard large Schröder generating function
\[
\sum_{s\ge0}R_sz^s=\frac{1-z-\sqrt{1-6z+z^2}}{2z}
\]
has dominant positive singularity \(3-2\sqrt2\) and \(R_s=\Theta((3+2\sqrt2)^s s^{-3/2})\). Combining with the Catalan estimate \(\frac1{n+1}\binom{2n}n=\Theta(4^n n^{-3/2})\) proves the exponentially decaying fraction.

## Verification
The accompanying standalone Python checker `verify.py` enumerates the ordered domains and all admissible nondecreasing image words *without using the proposed answer to generate candidates*. For every \(2\le n\le9\), it checks all \(Q_{n,k}\), independently enumerates the paired weakly increasing rows, checks total square-zero and nilpotent counts, and checks the exact first two moments using rational arithmetic. Its captured output ends `VERIFY_OK`. These finite checks support, but do not replace, the preceding all-\(n\) proof.

## Relationship to prior work
Zubairu–Umar–Al-Kharousi (arXiv:2512.19422, v1 publicly submitted December 22, 2025; subsequently published in *AIMS Mathematics* 2026) defines this same small Schröder semigroup and proves Green-relation, abundance, idempotent and semigroup-rank results. Its sections 1–3 do not count the elements whose *square is empty*. Laradji–Umar (2004; 2013 preprint, later published) proves the large Schröder count for all decreasing isotone partial transformations and Catalan counts for the different class of full Catalan transformations; its lattice-path bijections and Narayana-type formulas for *full transformation image rank* are important background. None of those statements directly identifies or enumerates the domain spectrum of square-zero *partial* maps in this small Schröder semigroup. The plane-partition and Narayana enumerations themselves are classical and are not claimed as newly discovered identities.

## Limitations
The claim concerns domain size, not image rank or the minimum nonzero nilpotency index beyond square zero. A previously overlooked equivalent bijection or explicit square-zero count in older transformation-semigroup literature would affect historical priority. The mathematical proof is self-contained given the classical rectangular plane-partition product and cited classical Schröder asymptotics; the verification script checks only finite dimensions through nine. No independent external mathematical audit is claimed.

## References
1. M. M. Zubairu, A. Umar and F. S. Al-Kharousi, *On the small Schröder semigroup*, arXiv:2512.19422 (first posted 2025-12-22); *AIMS Mathematics* 11 (2026), 17191–17207, doi:10.3934/math.2026705. https://arxiv.org/abs/2512.19422
2. A. Laradji and A. Umar, *On the number of decreasing and order-preserving partial transformations*, technical report (2004). https://www.academia.edu/74903889/On_the_Number_of_Decreasing_and_Order_Preserving_Partial_Transformations
3. A. Laradji and A. Umar, *Lattice paths and order-preserving partial transformations*, arXiv:1304.7574 (2013), later *Utilitas Mathematica* 101 (2016), 23–36. https://arxiv.org/abs/1304.7574
4. Classical MacMahon boxed-plane-partition formula; classical Narayana and Catalan identities.
