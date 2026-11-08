# Square-zero and stabilized-square census for order-reversing decreasing partial maps

## Finding
For every integer \(n\geq1\), consider the nonempty partial maps \(f:D\to[n]\) with \(\varnothing\ne D\subseteq[n]=\{1,\dots,n\}\), satisfying \(f(x)\leq x\) for every \(x\in D\) and \(x<y\) in \(D\) implies \(f(x)\geq f(y)\). Their powers are computed in the full partial transformation monoid, whose zero is the empty map. Every such map satisfies \(f^3=f^2\); moreover \(f^2\) is either zero or a nonzero rank-one idempotent.

Writing \(w=|D|\) and \(h=|f(D)|\), the exact counts in the two mutually exclusive cases are
\[
\begin{aligned}
Z_{n,w,h}&=\#\{f:f^2=0\}=\binom{w-1}{h-1}\binom{n}{w+h},\\
P_{n,w,h}&=\#\{f:f^2\neq0\}=\binom{w-1}{h-1}\binom{n}{w+h-1}.
\end{aligned}
\]
Here both sets on the left are additionally restricted to the stated width \(w\) and height \(h\), with \(1\le h\le w\le n\). All binomial coefficients whose lower index exceeds the upper index, or is negative, are zero. Thus the nonzero-square stratum first occurs at \(n=w+h-1\), while the zero-square stratum first occurs at \(n=w+h\). At each admissible width and height their sum is \(\binom{w-1}{h-1}\binom{n+1}{w+h}\), the established width-height census.

With Fibonacci normalization \(F_0=0\), \(F_1=1\), \(F_{j+2}=F_{j+1}+F_j\), their respective total counts are
\[
\#\{f:f^2\neq0\}=F_{2n},\qquad
\#\{f:f^2=0\}=F_{2n-1}-1,
\]
and therefore the whole nonempty order-reversing decreasing class has size \(F_{2n+1}-1\). In particular the generating function for the nonzero-square count is \(\sum_{n\ge1} F_{2n}z^n=z/(1-3z+z^2)\).

## Assumptions and scope
A partial transformation may be undefined outside its nonempty domain. Products and powers use ordinary partial function composition; \(f^2(x)=f(f(x))\) is defined exactly when \(x\in D\) and \(f(x)\in D\). The empty map is the zero of the ambient monoid and is **not** counted among the initial maps. The class of antitone maps is a sector of the monoid of monotone decreasing maps, **not** asserted to be a subsemigroup: the composition of two antitone maps can be isotone. The result is valid for every integer \(n\ge1\), including boundary cases where a binomial count is zero.

## Proof
**Step 1 (the square dichotomy).** Fix a map \(f\), and write \(d=\min D\) and \(H=f(D)\). Since \(f\) is antitone and decreasing, \(\max H=f(d)\le d\). Every member of \(D\) is at least \(d\), while every member of \(H\) is at most \(d\). Therefore \(H\cap D\) is either empty or \(\{d\}\), and the latter possibility occurs exactly when \(f(d)=d\). If \(f(d)<d\), no second iterate is defined, so \(f^2=0\). If \(f(d)=d\), then
\[
\operatorname{dom}(f^2)=\{x\in D:f(x)=d\},\qquad f^2(x)=d
\]
on that nonempty domain. In particular \(d\) belongs to this domain, and its image is the singleton \(\{d\}\); hence \((f^2)^2=f^2\) and \(f^3=f^2\). In the zero case \(f^3=f^2=0\) as well. This proves the dynamical assertion without assuming closure of the antitone class under multiplication.

**Step 2 (fixed width and height).** Arrange the domain as \(a_1<\cdots<a_w\) and the image as \(b_1<\cdots<b_h\). Antitonicity and surjectivity mean that the values down the ordered domain consist of \(h\) nonempty consecutive constant runs, with values \(b_h,b_{h-1},\dots,b_1\). Choosing the \(h-1\) boundaries between these runs gives exactly \(\binom{w-1}{h-1}\) maps for each compatible domain and image set.

By Step 1, a square-zero map has \(\max H<\min D\). Thus the domain and image are disjoint, every image point precedes every domain point, and their union is an arbitrary \((w+h)\)-subset of \([n]\). Conversely that subset uniquely determines the two sets by taking its first \(h\) points for \(H\) and its last \(w\) for \(D\). This gives \(Z_{n,w,h}\). A nonzero-square map instead has \(\max H=\min D=d\), with \(H\cap D=\{d\}\). Their union is an arbitrary \((w+h-1)\)-subset of \([n]\), uniquely partitioned as the first \(h\) points for \(H\) and the last \(w\) for \(D\), sharing the boundary point \(d\). Multiplying by the same run-partition factor gives \(P_{n,w,h}\). The support thresholds follow immediately. Pascal's identity gives the established unsplit formula, but that older unsplit formula alone does not specify the dynamical partition.

**Step 3 (Fibonacci totals).** Let \(P_n=\sum_{w,h}P_{n,w,h}\) and \(t=z/(1-z)\). The binomial series identity \(\sum_{n\ge r}\binom nr z^n=z^r/(1-z)^{r+1}\) implies, as formal power series,
\[
\sum_{n\ge1}P_nz^n
=\frac1{1-z}\sum_{w\ge h\ge1}\binom{w-1}{h-1}t^{w+h-1}.
\]
Put \(j=h-1\) and \(k=w-h\). The inner sum is
\[
\sum_{j,k\ge0}\binom{j+k}{j}t^{2j+k+1}
=\frac{t}{1-t-t^2}.
\]
Substituting \(t=z/(1-z)\) gives \(\sum_{n\ge1}P_nz^n=z/(1-3z+z^2)\). Its coefficients are \(F_{2n}\), using the initial terms \(P_1=1\), \(P_2=3\) and recurrence \(P_n=3P_{n-1}-P_{n-2}\) for \(n\ge3\).

For the zero-square maps, subtract one from each element of the domain, leaving its values unchanged. The strict inequality \(\max H<\min D\) ensures this yields an arbitrary nonempty antitone decreasing partial map of \([n-1]\); conversely, shift the domain of any such map right by one. The maps are mutual inverses and preserve width and height. Thus the number of square-zero maps at size \(n\) equals the total number of nonempty maps at size \(n-1\). Since the total at size \(n\) is \(P_n+Z_n\), we obtain \(Z_1=0\) and \(Z_n=P_{n-1}+Z_{n-1}\) for \(n\ge2\). Therefore \(Z_n=\sum_{k=1}^{n-1}F_{2k}=F_{2n-1}-1\), proving the claimed totals. The identity \(F_{2n}+F_{2n-1}=F_{2n+1}\) supplies the overall cardinality.

## Verification
The included standalone standard-library program `verify.py` enumerates all nonempty order-reversing decreasing partial maps on chains of sizes \(1\) through \(9\), computes their second and third iterates directly, independently tallies every width-height-square stratum, and matches it to both binomial formulas. It also checks that every nonzero square has image \(\{\min D\}\). Running `python verify.py` returns `VERIFY_OK` and prints the triples (total, nonzero square, square zero): \((1,1,0)\), \((4,3,1)\), \((12,8,4)\), \((33,21,12)\), \((88,55,33)\), \((232,144,88)\), \((609,377,232)\), \((1596,987,609)\), and \((4180,2584,1596)\). These finite checks corroborate, but do not replace, the proof for arbitrary \(n\).

## Relationship to prior work
Zubairu, Umar and Al-Kharousi, Theorem 1.4 of arXiv:2512.21134 (first public posting December 24, 2025), prove the **unsplit** exact width-height count \(\binom{w-1}{h-1}\binom{n+1}{w+h}\) for the antitone sector of their monotone-decreasing monoid. That source also describes ranks, ideals, and Green-type structure. The finding here is the exact dynamical split by vanishing/nonvanishing second iterate, its idempotent stabilization, the sharp support thresholds and the Fibonacci totals; it agrees with the prior unsplit theorem by addition and does not claim the unsplit count as new.

Cornelius, Shalangwa, Ajiya and Ishaku (2026) examine fixed points and refinements of the **injective** order-reversing decreasing partial maps. The present classification includes all noninjective maps and its squares; their injective results cover a strict subclass (the case \(h=w\)) and must not be misrepresented as absent. Ayık, Ayık, Dimitrova and Koppitz, arXiv:2507.06047, discuss cardinalities and ranks of related monotone-decreasing semigroups; that preprint was subsequently withdrawn. Umar's earlier work addresses nilpotent subsemigroups of other order-decreasing transformation classes. None of these inspected accessible results explicitly provides the stated full noninjective width-height square partition.

## Limitations
The antitone sector is not closed under composition and the theorem makes no claim that it is a semigroup. This is a classification of the second powers of its elements inside the ambient partial-transformation monoid, not a classification of the powers of all monotone-decreasing transformations. The comparison to older or unindexed literature is necessarily incomplete; the withdrawn preprint and Umar's thesis were not available in complete readable form. There is no independent mathematical audit or formal proof assistant certification. The enumerator covers only \(n\le9\); the infinite result follows from the mathematical proof.

## References
1. M. M. Zubairu, A. Umar, F. S. Al-Kharousi, *The monoid of monotone and decreasing partial transformations on a finite chain*, arXiv:2512.21134 (version 1 posted December 24, 2025), Theorem 1.4, https://arxiv.org/abs/2512.21134.
2. M. Cornelius, A. A. Shalangwa, Y. Ajiya, A. Ishaku, *Combinatorial Properties of Order Decreasing and Order Reversing Partial One-to-One Transformation Semigroup*, International Journal of Development Mathematics 3(2) (2026), 90–98, DOI:10.62054/ijdm/0302.06.
3. G. Ayık, H. Ayık, I. Dimitrova, J. Koppitz, *On certain semigroups of finite monotone and order-decreasing partial transformations*, arXiv:2507.06047 (2025; withdrawn January 2026).
4. A. Umar, *Semigroups of order-decreasing transformations* (1992), thesis; public abstract at https://www.researchgate.net/publication/277106344_Semigroups_of_order-decreasing_transformations.
