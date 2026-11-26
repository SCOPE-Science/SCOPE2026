# Exact pair-sum fibers and image density of the dyadic modular inverse hyperbola

## Finding

For every integer \(k\ge4\), put \(q=2^k\), \(R=\mathbb Z/q\mathbb Z\) and
\[\Gamma_q=\{(u,u^{-1}):u\in R^\times\}\subset R^2.\]
Write \(r_q(s,t)=\#\{(u,v)\in(R^\times)^2:u+v=s,\ u^{-1}+v^{-1}=t\}\), with ordered pairs. The theorem gives an explicit value of \(r_q(s,t)\) at **every** \((s,t)\in R^2\) in terms of square-root fibers modulo a smaller power of two. In particular, the complete twofold image has cardinality
\[
\boxed{|\Gamma_q+\Gamma_q|=
\begin{cases}
(q^2+40q+256)/96,&k\ \text{even},\\
(q^2+32q+256)/96,&k\ \text{odd}.
\end{cases}}
\]
Its ambient density therefore approaches \(1/96\). In comparison, every point of \(\Gamma_q\) has both coordinates odd, so the twofold sum can only have two even coordinates, but the theorem shows a much stronger obstruction than this parity restriction.

An exact corollary is the additive energy
\[\boxed{E(\Gamma_q)=\sum_{s,t\in R}r_q(s,t)^2=\frac32(k-3)q^2.}\]
Consequently, if \(K_q(a,b)=\sum_{u\in R^\times}\exp(2\pi i(au+bu^{-1})/q)\), then
\[\frac1{q^2}\sum_{a,b\in R}|K_q(a,b)|^4=\frac32(k-3)q^2.\]
The new focus is the complete **pointwise convolution and two-dimensional image**, rather than a standalone claim of novelty for the fourth-moment corollary.

## Assumptions and scope

All sums, inverses and congruences involving \(s,t,u,v\) are taken in \(R\). For a nonzero even residue \(s\), write \(h=v_2(s)\) for its unique valuation in \(\{1,\ldots,k-1\}\). If \(t\ne0\) has the same valuation, put \(m=k-h\), \(S=s/2^h\), \(T=t/2^h\), with \(S,T\) regarded as odd residues modulo \(2^m\). The quantity \(s/2\) has an unambiguous residue modulo \(2^m\) because \(m\le k-1\). Define
\[w=\left((s/2)^2-S T^{-1}\right)\bmod 2^m.\]
For \(\varepsilon\in\{0,1\}\), write
\[R_m^{(\varepsilon)}(w)=\#\{z\bmod 2^m:z^2=w\pmod{2^m},\ z\equiv\varepsilon\pmod2\}.\]
Then the **complete pointwise formula** is
\[
r_q(s,t)=
\begin{cases}
q/2,&(s,t)=(0,0),\\
2^h R_m^{(0)}(w),&s,t\ne0,\ v_2(s)=v_2(t)=h=1,\\
2^h R_m^{(1)}(w),&s,t\ne0,\ v_2(s)=v_2(t)=h\ge2,\\
0,&\text{otherwise}.
\end{cases}
\]
Here \(R_m^{(\varepsilon)}\) has a closed arithmetic description requiring no search. If \(w=0\), its even-root count is \(2^{\lfloor m/2\rfloor}\), and its odd-root count is zero. For nonzero \(w\), if \(v_2(w)\) is odd, both counts are zero. If \(v_2(w)=2j<m\), define \(n=m-2j\), \(U=w/2^{2j}\), and
\[c(n,U)=\begin{cases}1,&n=1,\\2,&n=2\text{ and }U\equiv1\pmod4,\\4,&n\ge3\text{ and }U\equiv1\pmod8,\\0,&\text{otherwise}.\end{cases}\]
There are exactly \(2^j c(n,U)\) roots, all odd if \(j=0\), and all even if \(j\ge1\). This specifies every \(r_q(s,t)\), not just its nonvanishing status.

## Proof

**Reduction to dyadic square roots.** Since \(u,v\) are units,
\[u^{-1}+v^{-1}=(u+v)(uv)^{-1}.\]
Thus \(s=0\) forces \(t=0\), with exactly \(q/2\) solutions, whereas nonzero \(s\) and \(t\) must have the same positive valuation \(h\). Substituting \(v=s-u\) gives
\[u(s-u)\equiv ST^{-1}\pmod{2^{k-h}}.\]
Completing the square after the integral translation \(z=u-s/2\) gives \(z^2\equiv w\pmod{2^m}\). If \(h=1\), then \(s/2\) is odd and \(z\) must be even; if \(h\ge2\), then \(s/2\) is even and \(z\) must be odd. Each permitted residue \(z\bmod2^m\) lifts to exactly \(2^h\) odd residues \(u\bmod2^k\). This proves the pointwise formula.

**Square-root enumeration.** For an odd residue modulo \(2^n\), a root exists automatically for \(n=1\), exactly when it is \(1\bmod4\) for \(n=2\), and exactly when it is \(1\bmod8\) for \(n\ge3\); the numbers of roots are respectively \(1,2,4\). These assertions follow by squaring odd residues and lifting roots two-adically: the four roots for \(n\ge3\) are the two signs and their shifts by \(2^{n-1}\). If \(w\ne0\) has valuation \(2j\), any root has valuation \(j\), so writing \(z=2^jZ\) leaves an odd-root equation modulo \(2^{m-2j}\) with \(2^j\) lifts per root. If \(w=0\), roots are precisely the multiples of \(2^{\lceil m/2\rceil}\). This establishes the explicit description above.

**Twofold image count.** Let \(\rho(m)\) count distinct odd squares modulo \(2^m\). The preceding lemma gives
\[\rho(1)=\rho(2)=1,\qquad\rho(m)=2^{m-3}\ (m\ge3).\]
For a fixed \(s\) with valuation \(h\ge2\), varying \(t\) over residues of that valuation permutes \(w\) through all odd residues modulo \(2^m\); therefore precisely \(\rho(m)\) choices of \(t\) occur. There are \(2^{m-1}\) choices of \(s\), with \(m=k-h\). When \(h=1\), varying \(t\) permutes \(w\) through every even residue modulo \(2^{k-1}\); the number of even squares modulo \(2^m\) is
\[\sigma(m)=1+\sum_{j=1}^{\lfloor(m-1)/2\rfloor}\rho(m-2j).\]
Thus
\[|\Gamma_q+\Gamma_q|=1+2^{k-2}\sigma(k-1)+\sum_{m=1}^{k-2}2^{m-1}\rho(m).\]
For even \(k\ge4\), \(\sigma(k-1)=(2^{k-4}+5)/3\); for odd \(k\ge5\), \(\sigma(k-1)=(2^{k-1}+32)/24\). Summing the geometric series yields exactly the two displayed cardinalities. Moreover, this argument specifies the full multiplicity histogram by valuation: for each \(h\ge2\) the \(2^{m-1}\rho(m)\) supported targets have count \(2^h(2^{m-1}/\rho(m))\); for \(h=1\), the square class \(w=0\) has count \(2^{1+\lfloor m/2\rfloor}\), and each even square with \(v_2(w)=2j<m\) has count \(2^{j+1}c(m-2j,w/2^{2j})\).

**Additive energy.** Write a quadruple with equal first-coordinate sums uniquely as
\[u\ \text{odd},\quad v=u+2d,\quad x=u+2e,\quad y=v-2e,\]
where \(u\) ranges modulo \(q\) and \(d,e\) range modulo \(q/2\). Equality of reciprocal-coordinate sums is, because all products are units, equivalent to
\[(u+v)(uv-xy)\equiv0\pmod q,\]
which becomes
\[8(u+d)e(e-d)\equiv0\pmod{2^k}.\]
Put \(K=k-3\). Reduction of \((u,d,e)\) modulo \(2^K\) has exactly \(8\cdot4\cdot4=128\) lifts. The bijection
\[(a,b,c)=(e,e-d,u+d)\]
turns the reduced condition into \(abc\equiv0\pmod{2^K}\) and \(a+b+c\equiv1\pmod2\). Exactly one of \(a,b,c\) must be odd: three odd factors cannot have zero product. For a prescribed odd factor there are \(2^{K-1}\) possibilities. The two remaining factors are even, and the number of even pairs with product zero modulo \(2^K\) is \(K2^{K-1}\). For \(K=1\) this is immediate; for \(K\ge2\), divide both even factors by two and use the identity that the number of pairs modulo \(2^r\) whose product vanishes modulo \(2^n\), for \(0\le n\le r\), is \((n+2)2^{2r-n-1}\). The identity follows by classifying the valuation of the first factor, with the zero factor handled separately. Hence
\[E(\Gamma_q)=128\cdot3\cdot2^{K-1}\cdot K2^{K-1}=3(k-3)2^{2k-1}.\]
Finally, finite-group Fourier orthogonality gives the stated fourth-moment identity, with the explicit factor \(q^{-2}\).

## Verification

The self-contained script `check_dyadic_inverse.py` calculates the convolution independently by enumerating ordered pairs and compares **every target** with the square-root formula, as well as checking the independent closed formulas for image size and additive energy. It passed for every \(k\in\{4,5,6,7,8,9,10,11\}\), including all \(4{,}194{,}304\) targets at \(k=11\). These are finite checks; the infinite-domain proof is the valuation and square-lifting argument above.

## Relationship to prior work

The modular-hyperbola survey of Shparlinski treats distribution and Kloosterman sums, not this complete twofold image law. Bower, Evans, Luo and Miller explicitly study **coordinate** sumsets such as \(\{u+u^{-1}\}\); those scalar projection sets are not the Minkowski pair sum \(\Gamma_q+\Gamma_q\subset R^2\). Gong, Veys and Wan study power moments of Kloosterman sums; those moments are closely related to the energy corollary but do not determine the pointwise convolution or twofold image. Nica establishes broader Kloosterman identities and fourth-moment results, with a different primary object. This work is framed as a complete two-dimensional dyadic representation and support classification, **not** as the first appearance of quadratic-congruence formulas or a novel general moment identity.

## Limitations

The theorem is proved only for \(q=2^k\) with \(k\ge4\). It does not classify mixed moduli, weighted Fourier extension extremizers, or higher convolutions. The explicit fourth moment could also be recovered through earlier Kloosterman-moment literature; the new claim does not depend on its novelty. Exact historical priority for the two-dimensional pointwise support law requires further independent literature examination, and the mathematical review is not independent.

## References

1. I. E. Shparlinski, *Modular Hyperbolas*, arXiv:1103.2879, publicly posted 2011-03-15, https://arxiv.org/abs/1103.2879.
2. A. Bower, R. Evans, V. Luo and S. J. Miller, *Coordinate sum and difference sets of d-dimensional modular hyperbolas*, arXiv:1212.2930, publicly posted 2012-12-12, https://arxiv.org/abs/1212.2930.
3. K. Gong, W. Veys and D. Wan, *Power Moments of Kloosterman Sums*, arXiv:1306.4104, publicly posted 2013-06-18, https://arxiv.org/abs/1306.4104.
4. B. Nica, *Kloosterman sums over finite Frobenius rings*, arXiv:1910.00165, publicly posted 2019-10-01, https://arxiv.org/abs/1910.00165.
