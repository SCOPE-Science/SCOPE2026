# Quasi-kernel spectra and a sharp real-rootedness transition in pendant-amplified directed cycles

## Finding

For integers \(n\ge3\) and \(k\ge1\), take the consistently directed cycle \(v_0\to v_1\to\cdots\to v_{n-1}\to v_0\) and add \(k\) private terminal vertices at each cycle vertex, with arcs directed from that cycle vertex to its private terminals. Let \(Q_{n,k}(z)\) be the ordinary size polynomial of its quasi-kernels. The precise quasi-kernel convention is given below. Then
\[
Q_{n,k}(z)=\sum_{\substack{a,b\ge0\\2a+3b=n}}\frac{n}{a+b}\binom{a+b}{b}\,z^{a+(k+1)b}(1+z)^{k(a+b)}.
\]
In particular, for every \(n\ge3\), \(Q_{n,1}\) has only real zeros. For \(k\ge2\), \(Q_{n,k}\) has only real zeros **if and only if** \(n\in\{3,4,5,7\}\). The first non-real-rooted instance occurs at \(n=6\) and \(k=2\):
\[
Q_{6,2}(z)=z^3(1+z)^4\bigl[2(1+z)^2+3z^3\bigr],
\]
where the cubic factor has discriminant \(-876\). These assertions concern the complete polynomial, not merely its first few coefficients.

The minimum quasi-kernel size is \(n/2\) for even \(n\), attained by exactly two sets, and \((n-1)/2+k\) for odd \(n\), attained by exactly \(n\) sets.

## Assumptions and scope

All digraphs are finite and loopless. A quasi-kernel is a **nonempty independent** vertex set \(S\) such that every vertex is reachable **from some vertex of** \(S\) by a directed walk of length at most two (a length-zero walk is permitted). Independence means that no arc has both endpoints in \(S\). The direction convention matters: in the opposite convention, every arc must be reversed. The parameters are integers \(n\ge3\) and \(k\ge1\); there are exactly \(n(k+1)\) vertices. The polynomial sums \(z^{|S|}\) over distinct labeled quasi-kernels \(S\), so it records the entire cardinality spectrum.

## Proof

**1. Cyclic gap classification.** No pendant terminal vertex can reach any cycle vertex. Hence \(S\) must include at least one cycle vertex; otherwise the cycle is unreachable. Distinct selected cycle vertices cannot be consecutive because of independence. A directed cycle vertex can reach only the next two cycle vertices in at most two steps; therefore between successive selected cycle vertices there may be only one or two omitted cycle vertices. Thus every cyclic gap between selected cycle vertices has length exactly two or three. Conversely such a selection makes every cycle vertex reachable within two steps.

For a gap of length two, its initial vertex is selected, its intermediate cycle vertex is not, and each of the \(k\) intermediate pendant vertices is independently optional: they are already at distance two from the selected initial vertex. The pendant vertices at a selected cycle vertex cannot be selected, and are reached in one step. The local generating weight is therefore \(z(1+z)^k\). For a gap of length three, pendant vertices at the first omitted cycle vertex are likewise optional; all \(k\) pendant vertices at the second omitted cycle vertex are mandatory because none is reachable in two steps from a selected cycle vertex. The local weight is \(z^{k+1}(1+z)^k\). These conditions are necessary and sufficient, including across the cyclic closing gap.

With \(a\) gaps of length two and \(b\) gaps of length three, necessarily \(2a+3b=n\), and the number of ways to arrange those gaps around the labeled cycle is \(\frac{n}{a+b}\binom{a+b}{b}\). To see this, count a distinguished selected cycle vertex (\(n\) choices) followed by an ordered sequence of \(a+b\) gaps (\(\binom{a+b}{b}\) choices), then divide by the \(a+b\) possible distinguished selected vertices of each resulting selection. Multiplication of the local weights proves the displayed full polynomial.

For even \(n=2h\), necessarily \(b=2j\), \(a=h-3j\); for odd \(n=2h+1\), necessarily \(b=2j+1\), \(a=h-1-3j\). Thus, defining positive-coefficient polynomials
\[
F_{2h}(w)=\sum_{j=0}^{\lfloor h/3\rfloor}\frac{2h}{h-j}\binom{h-j}{2j}w^j,
\quad
F_{2h+1}(w)=\sum_{j=0}^{\lfloor(h-1)/3\rfloor}\frac{2h+1}{h-j}\binom{h-j}{2j+1}w^j,
\]
we obtain, with \(d=\deg F_n\),
\[
Q_{2h,k}(z)=z^h(1+z)^{k(h-d)}\,(1+z)^{kd}F_{2h}\!\left(\frac{z^{2k-1}}{(1+z)^k}\right),
\]
\[
Q_{2h+1,k}(z)=z^{h+k}(1+z)^{k(h-d)}\,(1+z)^{kd}F_{2h+1}\!\left(\frac{z^{2k-1}}{(1+z)^k}\right).
\]
Both equalities are polynomial identities after cancellation of denominators. The minimum-size assertions follow because the exponent increases by exactly \(2k-1>0\) with each increment of \(j\). At \(j=0\), the counts are respectively two and \(n\).

**2. Every root of \(F_n\) is distinct and strictly negative.** Define \(T_m(q)\) as the sum of the \(m\)-th powers of the three roots of \(t^3-t-q=0\). Newton identities give \(T_m=T_{m-2}+qT_{m-3}\) for \(m\ge3\), with \(T_0=3\), \(T_1=0\), \(T_2=2\), and \(T_3=3q\). Counting cyclic compositions into blocks of lengths two and three yields
\[
T_m(q)=\sum_{2a+3b=m}\frac{m}{a+b}\binom{a+b}{b}q^b,
\]
so \(T_{2h}(q)=F_{2h}(q^2)\) and \(T_{2h+1}(q)=qF_{2h+1}(q^2)\).

For real \(s>0\), put \(q=-is(1+s^2)\), \(R=\sqrt{1+s^2}\), and \(\theta=\arctan(s/\sqrt{4+3s^2})\). The roots of the cubic are exactly \(is\), \(Re^{-i\theta}\), and \(-Re^{i\theta}\). As \(s\) increases from zero to infinity, \(\theta\) strictly increases from zero to \(\pi/6\), and \(w=q^2=-s^2(1+s^2)^2\) decreases through all negative real values. Consequently
\[
F_{2h}(w)=2R^{2h}\cos(2h\theta)+(-1)^h s^{2h},
\]
\[
F_{2h+1}(w)=\frac{2R^{2h+1}\sin((2h+1)\theta)-(-1)^h s^{2h+1}}{s(1+s^2)}.
\]
Since \(2R^m>s^m\), the first expression at each finite phase \(m\theta=j\pi\) has strict sign \((-1)^j\); the second expression at each finite phase \(m\theta=(j+\frac12)\pi\) has strict sign \((-1)^j\). Comparing the available phase points with the degree shows the following. For \(m=6r+2\) or \(6r+4\) even, the phase points \(j=0,\dots,r\) give \(r\) sign changes. For \(m=6r\), phase points \(j=0,\dots,r-1\) give \(r-1\) changes, and the sign \((-1)^r\) as \(w\to-\infty\) gives the last. For odd \(m=6r+1\), the half-integer phases \(j=0,\dots,r-1\) give \(r-1\) changes. For odd \(m=6r+3\), with \(r\ge1\), half-integer phases \(j=0,\dots,r-1\) plus the sign at \(-\infty\) yield \(r\) changes; \(m=3\) is constant. For odd \(m=6r+5\), half-integer phases \(j=0,\dots,r\) give \(r\) changes. In every case the number of distinct negative roots is precisely \(\deg F_m\). All are therefore simple, and there can be no other complex roots. Because the coefficients are strictly positive, zero and positive real numbers are not roots.

**3. The sharp real-rootedness transition.** Write \(F_n(w)=A_0\prod_{j=1}^d(1+w/c_j)\), where all \(c_j>0\), and \(A_0=2\) for even \(n\) or \(A_0=n\) for odd \(n\). The polynomial in Step 1 factors as a positive constant times its explicit powers of \(z\) and \(1+z\), and the factors
\[
H_{k,c_j}(z)=(1+z)^k+\frac{z^{2k-1}}{c_j}.
\]
When \(k=1\), every \(H_{1,c}\) has exactly one real root, \(-c/(c+1)\in(-1,0)\), establishing complete real-rootedness for all \(n\).

For \(k\ge3\) odd, \(H_{k,c}\) has no real roots outside \((-1,0)\), and exactly one inside: for \(z=-t\in(-1,0)\), its root equation is \(c=t^{2k-1}/(1-t)^k\), strictly increasing from zero to infinity. Since its degree is \(2k-1\ge5\), it has nonreal roots. For \(k\ge4\) even, the same argument gives one root in \((-1,0)\), and there can be at most two further real roots to the left of \(-1\): setting \(z=-t\) for \(t>1\) gives \(c=t^{2k-1}/(t-1)^k\), whose logarithmic derivative vanishes at only \(t=(2k-1)/(k-1)\). There are no positive real roots. Thus a degree at least seven factor has nonreal roots.

It remains to treat \(k=2\). For \(H_{2,c}\), the function \(t^3/(t-1)^2\) on \(t>1\) has minimum \(27/4\). Hence if \(c<27/4\), that cubic has exactly one real root and two nonreal roots. When \(d\ge1\), at least one \(c_j\le3\). Indeed \(\sum_j1/c_j=A_1/A_0\); for \(n=2h\ge6\), this ratio is \(h(h-2)/2\), while for \(n=2h+1\ge9\), it is \((h-2)(h-3)/6\). In both cases \(A_1/A_0\ge d/3\). Therefore one \(c_j\le3<27/4\), and the full polynomial has nonreal roots for \(k=2\) as well. The condition \(d=0\), which means \(n\in\{3,4,5,7\}\), makes \(Q_{n,k}\) a monomial times a power of \(1+z\), so it is real-rooted for every \(k\). This proves the classification.

## Verification

The standalone `verify.py` uses directed-edge reachability within two steps and independent-set testing directly, without employing the cyclic-gap proof, to enumerate the complete size distribution for fourteen pairs \((n,k)\), with \(n=3,\ldots,9\) for \(k=1\), \(n=3,\ldots,6\) for \(k=2\), and \(n=3,4,5\) for \(k=3\). It checks 1,767,232 initial subsets. Exact integer arithmetic tests the composition coefficients for \(3\le n\le150\) and independently computes the negative discriminant at the first obstruction. Run `python3 verify.py` from the extracted files. Finite checks corroborate but do not replace the all-parameter proof.

## Relationship to prior work

Spiro's November 17, 2026 preprint *Equivalence of Small and Large Quasi-kernels* explicitly employs directed pendant amplification in the proof of a transfer principle for quasi-kernel bounds; it does not provide an exact cardinality polynomial or a real-zero classification for this family. Ai, Gutin, Liu and Meng study general small/large quasi-kernel transfer bounds, not this enumerator. Spiro's earlier generalized quasi-kernel work investigates different extremal parameters, including attached leaves in related constructions. Earlier work by Gutin and collaborators addresses the number of quasi-kernels of digraphs in general and exceptional cases. The exact cyclic-gap spectrum and the \(k=1\) versus \(k\ge2\) real-rootedness boundary are not claimed in those inspected statements. The cubic power-sum identity is a method, not asserted as a novel recurrence.

## Limitations

The theorem is for uniformly \(k\)-amplified outward pendant arcs attached to a single consistently oriented cycle. It does not cover nonuniform numbers of leaves, noncyclic base digraphs, or the reverse reachability convention without reversing all arcs. The analytic proof establishes exact root reality, not a uniform closed form for every complex zero. Absence of an identical claim in inspected records does not prove historical priority, and there has been no independent mathematical audit.

## References

1. S. Spiro, *Equivalence of Small and Large Quasi-kernels*, arXiv:2611.22881v1, first public 2026-11-17, https://arxiv.org/abs/2611.22881v1 (especially Section 3, outward-leaf amplification).
2. Ai, Gutin, Liu, and Meng, *Small and large quasi-kernels: a weighted transfer theorem*, arXiv:2610.23487, first public 2026-10-16, https://arxiv.org/abs/2610.23487.
3. S. Spiro, *Generalized Quasikernels in Digraphs*, arXiv:2404.07305, https://arxiv.org/abs/2404.07305.
4. Gutin, Koh, Tay, and Yeo, *On the number of quasi-kernels in digraphs* (2004), author manuscript at https://repository.royalholloway.ac.uk/items/97e9c1f5-3209-d0a4-9ff3-7322a2d00a9c/8/.
