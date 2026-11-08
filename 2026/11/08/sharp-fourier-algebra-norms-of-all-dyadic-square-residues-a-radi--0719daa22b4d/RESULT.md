# Sharp Fourier-algebra norms of all dyadic square residues: a radical recurrence and two-phase asymptotics

## Finding

For every integer \(k\ge1\), write \(G_k=\mathbb Z/2^k\mathbb Z\), let
\[
Q_k=\{x^2\bmod 2^k:x\in G_k\},
\]
including zero and all nonunit squares, and let \(P_k\) be the additive Fourier projection whose multiplier is \(\mathbf1_{Q_k}\). Write
\[
\Lambda_k=\|P_k\|_{\ell^1(G_k)\to\ell^1(G_k)}
           =\|P_k\|_{\ell^\infty(G_k)\to\ell^\infty(G_k)}.
\]
The equalities and the following statements are exact for every stated depth. Set \(s_j=|Q_j|\) for \(j\ge1\), so
\[
s_j=\frac{2^{j-1}+a_j}{3},\qquad
 a_j=\begin{cases}4&j\text{ even},\\5&j\text{ odd}.\end{cases}
\]
The initial norms are
\[
\Lambda_1=1,\qquad \Lambda_2=\frac{1+\sqrt2}{2},\qquad
\Lambda_3=1+\frac{\sqrt5}{4}.
\]
For each \(k\ge4\), define
\[
h_k=2^{k-3},\qquad c_k=s_{k-2},\qquad
 d_k=\begin{cases}0&k=4,\\s_{k-4}-2^{k-5}&k\ge5.\end{cases}
\]
Then the exact sharp endpoint norm obeys the two-step radical recurrence
\[
\boxed{\Lambda_k=\Lambda_{k-2}+\Delta_k},
\]
where
\[
\boxed{
\Delta_k=2^{-k}\Bigl(2h_k+2\sqrt{c_k^2+h_k^2}-4c_k
+2\sqrt{d_k^2+h_k^2+\sqrt2d_kh_k}
+2\sqrt{d_k^2+h_k^2-\sqrt2d_kh_k}-4|d_k|\Bigr).
}
\]
In particular this is an explicit finite radical evaluation for every \(k\), with no character sums remaining.

Define
\[
C=\frac{2\sqrt{10}+\sqrt{37-6\sqrt2}+\sqrt{37+6\sqrt2}}{24}
=0.767031269594249\ldots .
\]
Then \(\Delta_k\to C\), with the effective bound
\[
\boxed{|\Delta_k-C|\le\frac{80}{3\cdot2^k}\qquad(k\ge5).}
\]
Furthermore, two distinct finite constants \(B_{\mathrm{even}}\) and \(B_{\mathrm{odd}}\) exist such that
\[
\boxed{\Lambda_k=\frac C2\,k+B_{k\bmod2}+R_k,\qquad
|R_k|\le\frac{80}{9\cdot2^k}\quad(k\ge3),}
\]
where \(B_0=B_{\mathrm{even}}\), \(B_1=B_{\mathrm{odd}}\) and
\[
B_0=\Lambda_4-2C+\sum_{r=1}^\infty(\Delta_{4+2r}-C),
\qquad
B_1=\Lambda_3-\tfrac32C+\sum_{r=1}^\infty(\Delta_{3+2r}-C).
\]
Both series converge absolutely. In particular
\[
\lim_{k\to\infty}\frac{\Lambda_k}{k}=
\frac{2\sqrt{10}+\sqrt{37-6\sqrt2}+\sqrt{37+6\sqrt2}}{48}
=0.383515634797124\ldots .
\]
The two offsets are genuinely distinct: direct finite radical evaluation plus the displayed rigorous remainder bound gives
\[
0.2914<B_0<0.2917,\qquad 0.2196<B_1<0.2199.
\]
Higher-precision evaluation yields \(B_0\approx0.291543252427331\) and \(B_1\approx0.219708497280347\).

## Assumptions and scope

All groups are cyclic additive groups with counting measure. Write the unnormalized discrete Fourier transform as
\[
F_k(a)=\sum_{x\in Q_k}e^{-2\pi iax/2^k},\qquad 0\le a<2^k.
\]
The projection kernel is \(K_k(a)=2^{-k}F_k(a)\). Thus \(\Lambda_k=2^{-k}\sum_a|F_k(a)|\), independently of whether normalized or unnormalized \(\ell^p\) norms are used on both domain and codomain. The frequency set includes the residue zero and all even-valuation nonunit squares; substituting the set of unit squares changes the problem.

## Proof

**1. The dyadic square stratification.** An odd square modulo \(2^k\) is \(1\bmod8\) for \(k\ge3\). Conversely, all classes \(1\bmod8\) are squares: start at modulus eight and lift an odd root from modulus \(2^j\) to \(2^{j+1}\), changing the root by \(2^{j-1}\) when necessary. The square changes by \(2^j\) modulo \(2^{j+1}\), since the root is odd. The odd-square set therefore has \(2^{k-3}\) elements. Every even square is four times a square modulo \(2^{k-2}\). The two parts are disjoint, so, for \(k\ge3\),
\[
Q_k=(1+8G_k)\ \dot\cup\ 4Q_{k-2}.
\]
Hence \(s_k=2^{k-3}+s_{k-2}\), with \(s_1=s_2=2\); solving the recurrence yields the stated \(s_k\).

**2. A character recurrence.** Set \(h=2^{k-3}\). Orthogonality of the subgroup \(8G_k\) gives, for all \(k\ge3\),
\[
F_k(a)=F_{k-2}(a\bmod2^{k-2})+
 h\,\mathbf1_{h\mid a}\,e^{-2\pi ia/2^k}.
\]
For all but eight frequencies, the second summand vanishes. Summed over the four lifts of each frequency modulo \(2^{k-2}\), the first term alone contributes exactly \(\Lambda_{k-2}\) to the normalized absolute Fourier sum.

**3. Exactly eight exceptional frequencies.** The exceptions are \(a=hu\) with \(u=0,1,\ldots,7\). If \(u\) is even, \(F_{k-2}(a\bmod2^{k-2})=s_{k-2}=c_k\). If \(u\) is odd, this value is the parity-weighted number of square residues in \(G_{k-2}\), namely \(d_k\). Indeed it is \(0\) at \(k=4\), and for \(k\ge5\) equals the number of even squares minus that of odd squares,
\[
d_k=s_{k-4}-2^{k-5}.
\]
Their additional phases are the eight eighth-roots of unity. For even \(u\), they are \(1,i,-1,-i\); for odd \(u\), the real parts are \(\pm1/\sqrt2\). Since \(c_k\le h\) for \(k\ge4\), the absolute-value change over even \(u\) is
\[
2h+2\sqrt{c_k^2+h^2}-4c_k,
\]
and that over odd \(u\) is
\[
2\sqrt{d_k^2+h^2+\sqrt2 d_kh}
+2\sqrt{d_k^2+h^2-\sqrt2 d_kh}-4|d_k|.
\]
Division by \(2^k\) proves the recurrence. Direct evaluation of \(Q_1,Q_2,Q_3\) proves the three base norms.

**4. Sharpness.** The multiplier projection is convolution by \(K_k\). Its \(\ell^1\)-operator norm equals \(\sum_a|K_k(a)|\), attained on a point mass. Its \(\ell^\infty\)-operator norm is the same, attained by choosing a function whose phases are conjugate to those of one kernel row. Therefore the computed number is the sharp operator norm, not merely an estimate.

**5. Asymptotic slope and separated phases.** For \(k\ge5\) put \(a=a_k\in\{4,5\}\). The exact square count gives
\[
\frac{c_k}{h_k}=\frac13+\frac a{3h_k},\qquad
\frac{d_k}{h_k}=-\frac16+\frac a{3h_k}.
\]
After dividing the eight-term absolute-value expression by \(8h_k\), its limit is
\[
\frac18\left[\sum_{u\text{ even}}\bigl(|\tfrac13+\zeta_8^u|-\tfrac13\bigr)
+\sum_{u\text{ odd}}\bigl(|-\tfrac16+\zeta_8^u|-\tfrac16\bigr)\right]=C.
\]
Here \(\zeta_8=e^{2\pi i/8}\); evaluating the eight moduli yields the displayed radicals. For a real variable \(v\), each function \(|v+\zeta_8^u|-|v|\) is \(2\)-Lipschitz. Summing four even and four odd terms and dividing by eight shows
\[
|\Delta_k-C|\le\left|\frac{c_k}{h_k}-\frac13\right|
+\left|\frac{d_k}{h_k}+\frac16\right|
\le\frac{10}{3h_k}=\frac{80}{3\cdot2^k}.
\]
Applying this to successive increments of a fixed parity proves absolute convergence of both \(B\)-series. The tail after depth \(k\) is at most
\[
\frac{80}{3}\sum_{r=1}^\infty2^{-(k+2r)}
=\frac{80}{9\cdot2^k},
\]
which establishes the expansion and explicit remainder. Evaluating the finite recurrence at depths \(16\) and \(17\), then applying this tail bound, places the two offsets in the stated disjoint rational intervals.

## Verification

The accompanying `verify_square_norm.py` uses only the Python standard library and a separate iterative radix-two FFT. It constructs the complete square sets and checks, for every depth \(1\le k\le12\), their cardinalities, every Fourier coefficient in the character recurrence, Parseval's identity, and the exact two-step norm recurrence. It also tests the limiting coefficient and explicit error bound at additional depths. Run `python verify_square_norm.py`; the terminal marker is `DYADIC_SQUARE_WIENER_NORM_PASS`.

## Relationship to prior work

Green and Sanders' quantitative idempotent theorem gives the general Fourier-algebra norm framework and structural consequences for arbitrary finite abelian groups. Its quantitative coset-decomposition theorem does not determine the sharp norm of this particular nested square set. Stangl's classical square-counting formula supplies the number of residues, but cardinality alone cannot determine the absolute Fourier norm: the exceptional eight character phases and their cancellations must be evaluated. General cyclic spectral/tiling results examine zeros of mask polynomials, not the absolute-sum norm of this square-residue indicator. A separate odd-prime complete-square norm formula does not include characteristic two; here odd squares form one additive coset modulo eight and generate a distinct radical coefficient and two phase offsets. These implications are logically different; exhaustive historical priority is not claimed.

## Limitations

The result is restricted to powers of two, the complete square-residue set, and endpoint projection norms. It makes no claim about sharp intermediate \(\ell^p\) norms, arbitrary composite moduli, or extremizer uniqueness. The original full text of Stangl's counting paper was not accessible for direct examination; a counting-only comparison is supported by the bibliographic record and secondary presentation of its formula, not an assertion about every result in the inaccessible article. Numerical checks at finite depths do not certify the all-depth theorem independently.

## References

1. B. Green and T. Sanders, *A quantitative version of the idempotent theorem in harmonic analysis*, arXiv:math/0611286v1 (public 2006-11-09); Annals of Mathematics 168 (2008), 1025–1054. https://arxiv.org/abs/math/0611286
2. W. D. Stangl, *Counting Squares in* \(\mathbb Z_n\), Mathematics Magazine 69 (1996), 285–289, https://doi.org/10.1080/0025570X.1996.11996456 (original full text not inspected).
3. R. D. Malikiosis, *On the structure of spectral and tiling subsets of cyclic groups*, Forum of Mathematics, Sigma (2022), https://doi.org/10.1017/fms.2022.14 (full online article inspected for relevant theorem statements).
