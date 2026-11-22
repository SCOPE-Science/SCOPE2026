# Parity and the sharp primitive-Fourier cancellation gap for four-point cyclic masks

## Finding
Let \(N\ge4\), let \(\zeta_N=e^{2\pi i/N}\), and define
\[
\Delta_4(N)=\min_{A\subset\mathbb Z/N\mathbb Z,\ |A|=4}
\left|\sum_{a\in A}\zeta_N^a\right|.
\]
Then
\[
\boxed{\Delta_4(N)=
\begin{cases}
0,&N\text{ even},\\
2\bigl(\cos(\pi/N)-\cos(2\pi/N)\bigr),&N\text{ odd}.
\end{cases}}
\]
For even \(N\), equality holds exactly when \(A\) is a union of two distinct antipodal pairs \(\{a,a+N/2\}\) and \(\{b,b+N/2\}\). For odd \(N\), put \(m=(N-3)/2\). Equality holds exactly for the \(N\) translates of
\[
A_* = \{0,1,m+1,m+3\}\pmod N,
\]
whose cyclic gap multiset *in cyclic order* is \((1,m,2,m)\), up to cyclic rotation and reversal. In particular no four distinct \(N\)-th roots sum to zero when \(N\) is odd. In that case
\[
\Delta_4(N)=\frac{3\pi^2}{N^2}+O(N^{-4}).
\]

Equivalently, for every primitive frequency \(k\in(\mathbb Z/N\mathbb Z)^\times\) and any four-site mask \(A\), the unnormalized Fourier coefficient \(\widehat{\mathbf1_A}(k)=\sum_{a\in A}e^{-2\pi i k a/N}\) has modulus at least \(\Delta_4(N)\). Equality is precisely the inverse image under multiplication by \(k\) of the listed extremal masks. No statement about nonprimitive frequencies in the odd composite case is needed for this characterization.

## Assumptions and scope
The elements of \(A\) are distinct, every weight is exactly one, and the Fourier transform is **unnormalized**. Repetitions and arbitrary complex coefficient phases are excluded: both change the extremal problem. Primitive means \(\gcd(k,N)=1\); multiplication by a primitive frequency permutes the residues. The classification holds for every integer \(N\ge4\), not only prime orders or a computational range.

## Proof
First consider odd \(N\ge5\), with four points placed counterclockwise at angles \(0\le\theta_1<\theta_2<\theta_3<\theta_4<2\pi\). Their four positive cyclic gaps in units of \(2\pi/N\) sum to \(N\). At most one gap exceeds \(N/2\). By cyclically choosing a starting vertex, we can arrange the gaps as \((a,b,c,d)\), where \(1\le a,c<N/2\) and \(a+b+c+d=N\).

Pair the first two roots and the last two. Let \(\alpha=\pi a/N\), \(\gamma=\pi c/N\), and \(\delta=\pi(b-d)/N\). Their two vector sums have lengths \(2\cos\alpha\) and \(2\cos\gamma\). Their midpoint directions differ by \(\pi+\delta\). Consequently, with \(S=\sum_{a\in A}\zeta_N^a\),
\[
\tag{1}|S|^2=4\left[(\cos\alpha-\cos\gamma)^2+
2\cos\alpha\cos\gamma(1-\cos\delta)\right].
\]
The two cosines are strictly positive.

**Case \(a\ne c\).** For positive integers \(r<s<N/2\), strict concavity of \(\cos t\) on \((0,\pi/2)\) and monotonicity show
\[
\cos(\pi r/N)-\cos(\pi s/N)\ge
\cos(\pi/N)-\cos(2\pi/N),
\]
with equality precisely at \((r,s)=(1,2)\). Equation (1) proves the desired bound. Equality requires \(\{a,c\}=\{1,2\}\) and \(\delta=0\), hence \(b=d=(N-3)/2=m\).

**Case \(a=c\).** Since \(N\) is odd, the positive integers \(b,d\) sum to the odd number \(N-2a\); thus \(b\ne d\), \(N-2a\ge3\), and \(|b-d|\ge1\). Therefore
\[
\begin{aligned}
|S|&=4\cos(\pi a/N)\left|\sin\frac{\pi(b-d)}{2N}\right|\\
&\ge4\sin\frac{3\pi}{2N}\sin\frac{\pi}{2N}\\
&=2\left(\cos\frac\pi N-\cos\frac{2\pi}N\right).
\end{aligned}
\]
The first inequality uses \(a\le(N-3)/2\), decreasing cosine on \((0,\pi/2)\), and increasing sine on \([0,\pi/2]\) applied to \(|b-d|<N\). Equality forces \(a=c=m\), \(\{b,d\}=\{1,2\}\). Thus all odd-order equality gap words are cyclic rotations or reversals of \((1,m,2,m)\).

The mask \(A_*=\{0,1,m+1,m+3\}\) has gaps \((1,m,2,m)\) and realizes equality. The gap word has no proper period, so its translation orbit contains exactly \(N\) sets; reversal is already a cyclic rotation of this gap word and does not create another orbit. The cosine Taylor expansion gives the stated asymptotic.

For even \(N\), choosing any two distinct antipodal pairs produces \(S=0\). Conversely, suppose four distinct unit complex numbers sum to zero. If the first two sum to zero they are antipodes and so are the remaining two. Otherwise write their nonzero sum as \(w\). The unordered pair of unit-circle points with prescribed nonzero sum \(w\) is unique: its members are the two intersections of the unit circle with the perpendicular bisector of the segment joining \(0\) and \(w\), centered around direction \(w\). Since the last two sum to \(-w\), they must be the negatives of the first pair. Every exact zero thus consists of two antipodal pairs. This completes the equality characterization for even \(N\).

Finally, for primitive \(k\), the map \(a\mapsto ka\) is a permutation of \(\mathbb Z/N\mathbb Z\); complex conjugation does not change modulus. Thus the same exact constants and equality families apply to \(|\widehat{\mathbf1_A}(k)|\). \(\square\)

## Verification
The proof of (1), the two global cases and the even-order zero-classification are analytic and independent of finite computation. As a supplementary diagnostic, `CHECK.py` enumerates every four-element subset for each \(4\le N\le26\), evaluates the corresponding complex root sum, compares it to the closed formula and tests the complete predicted minimizer orbit. All 80,730 tested subsets passed. The test uses floating-point arithmetic with a declared tolerance and neither certifies infinitely many orders nor replaces the proof. Run `python CHECK.py` using Python 3 standard libraries only.

## Relationship to prior work
Kalogirou (arXiv:2607.06098, first posted 2026-07-07) studies small sums of roots of unity with a prescribed number of terms, using general constructions and asymptotics. Barber (arXiv:2104.15057, first posted 2021-04-30, Section 2, Proposition 3(c)) analyzes the unrestricted four-term minimum with **repetitions allowed**. In contrast, a Fourier transform of an indicator of a four-site set has four distinct roots at each primitive frequency. The multiplicity-permitting odd-order optimum is approximately \(\pi^2/N^2\), while the new distinct-mask optimum is approximately \(3\pi^2/N^2\), and the extremizer configurations differ. The unrestricted result therefore supplies a weaker lower bound, not this distinctness-constrained sharp formula.

Cheng (arXiv:2610.27231, first posted 2026-10-19) gives exceptional-set bounds for a symmetric five-term class and a conditional separation theorem for fixed numbers of distinct prime-order roots. Those bounds do not specialize to the present unconditional exact four-root formula. An accessible published result on four-point cyclic Wiener minimizers (published-finding corpus, 2026-11-02, identifier `2026/11/2/SCOPE-certified-four-point-cyclic-wiener-minimizers-through-modulus-12--8f6d57abce9f`) optimizes the **sum over all nonzero frequency magnitudes** through finite modulus 128, not the least magnitude at one primitive frequency over every modulus. Its odd-order minimizing sets are arithmetic progressions rather than the present gap pattern. These objectives and implications are distinct.

## Limitations
The sharp lower bound is asserted for primitive Fourier frequencies only; composite-order nonprimitive frequencies can identify different support residues with repetitions. The result concerns equal unit weights on exactly four distinct sites and gives no general lower bound for arbitrary signed or complex-weighted four-tap signals, nor for five or more sites. An older unindexed treatment of four *distinct* roots might exist despite the source comparisons, so novelty has not been independently certified. No independent mathematical audit has been performed.

## References
1. A. Kalogirou, *Small sums of roots of unity*, arXiv:2607.06098, first posted 2026-07-07, https://arxiv.org/abs/2607.06098.
2. B. Barber, *Small sums of five roots of unity*, arXiv:2104.15057, first posted 2021-04-30, Section 2, Proposition 3, https://arxiv.org/abs/2104.15057; published in *Bulletin of the London Mathematical Society* 55 (2023), 1890–1906.
3. Q. Cheng, *Small sums of roots of unity: polylogarithmic exceptional sets and conditional separation*, arXiv:2610.27231, first posted 2026-10-19, https://arxiv.org/abs/2610.27231.
4. *Certified four-point cyclic Wiener minimizers through modulus 128*, published published-finding corpus record `2026/11/2/SCOPE-certified-four-point-cyclic-wiener-minimizers-through-modulus-12--8f6d57abce9f`, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-certified-four-point-cyclic-wiener-minimizers-through-modulus-12--8f6d57abce9f.
