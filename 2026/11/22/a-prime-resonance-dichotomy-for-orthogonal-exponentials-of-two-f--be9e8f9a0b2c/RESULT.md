# A prime-resonance dichotomy for orthogonal exponentials of two finite digit convolutions

## Finding

Let \(p<q\) be distinct primes and \(a,b\) be positive coprime integers. Put
\[
\nu_{r,c}=\frac1r\sum_{j=0}^{r-1}\delta_{jc},\qquad
\mu=\nu_{p,a}*\nu_{q,b}.
\]
Write \(\mathcal O(\mu)\) for the largest number of pairwise orthogonal exponentials \(e_\lambda(x)=e^{2\pi i\lambda x}\) in \(L^2(\mu)\), with frequencies allowed to be arbitrary real numbers. Then
\[
\boxed{\mathcal O(\mu)=
\begin{cases}
pq,&p\mid b\ \text{or}\ q\mid a,\\
q,&p\nmid b\ \text{and}\ q\nmid a.
\end{cases}}
\]
In the nonresonant case every \(q\)-element orthogonal family, up to a common frequency translation, is exactly
\[
\left\{\frac{k_j}{qb}:0\le j<q\right\},
\quad k_0,\ldots,k_{q-1}\in\mathbb Z,
\quad k_j\not\equiv k_\ell\pmod q\ (j\ne\ell).
\]
In the resonant case \(\mu\) has exactly \(pq\) distinct equal-mass support points and admits an explicit orthonormal exponential basis. Thus the optimal cardinality jumps directly from \(q\) to \(pq\) as the arithmetic resonance condition changes. In the nonresonant case it has no exponential orthonormal basis.

## Assumptions and scope

The measures are *finite* probability measures on \(\mathbb R\), not infinite self-similar Bernoulli convolutions. Both progressions have consecutive digits and uniform weights. The assumption \(\gcd(a,b)=1\) loses no generality for commensurable positive steps, since a common dilation changes frequencies but not orthogonality. The primes are distinct and ordered \(p<q\); no claim is made for composite digit counts, nonuniform weights, irrational step ratios, or infinite convolutions. Orthogonal exponentials are normalized automatically because \(\mu\) is a probability measure.

## Proof

**Exact zero sets.** For \(r\ge2\) and a positive integer \(c\), the geometric sum gives
\[
\widehat{\nu_{r,c}}(t)=\frac1r\sum_{j=0}^{r-1}e^{-2\pi i jct},\qquad
\mathcal Z(\widehat{\nu_{r,c}})
=\left\{\frac{k}{rc}:k\in\mathbb Z,\ r\nmid k\right\}.
\]
The displayed formula follows from the geometric-series quotient when \(e^{-2\pi ict}\ne1\); where its denominator vanishes, the sum is \(1\), not zero. Consequently \(\mathcal Z(\widehat\mu)\) is precisely the union of these two sets for \((r,c)=(p,a)\) and \((q,b)\). Pairwise orthogonality is exactly the condition that every nonzero frequency difference lies in this union.

**Nonresonance and the upper bound.** Suppose \(p\nmid b\) and \(q\nmid a\). Because \(\gcd(a,b)=1\) and \(p,q\) are distinct primes, \(\gcd(pa,qb)=1\). Let \(H=paqb\). Every Fourier zero is a multiple of \(1/H\). Translate any nonempty orthogonal frequency family by one of its elements to place \(0\) in the family; every frequency is then a residue in \(H^{-1}\mathbb Z/\mathbb Z\). The Chinese remainder theorem identifies this cyclic grid with
\[
\mathbb Z/H\mathbb Z\simeq
\mathbb Z/(pa)\mathbb Z\times\mathbb Z/(qb)\mathbb Z.
\]
A zero from \(\nu_{p,a}\) has second coordinate zero and first coordinate nonzero; a zero from \(\nu_{q,b}\) has first coordinate zero and second coordinate nonzero. If the translated family contained a nonzero frequency of each kind, their difference would have both coordinates nonzero and could not be a Fourier zero, a contradiction. Hence all translated frequencies lie on *one* coordinate axis.

On the first axis the differences take the form \((k_i-k_j)/(pa)\); their being zeros forces distinct residues \(k_i\pmod p\), so there are at most \(p\) frequencies. On the second axis the same argument forces distinct residues \(k_i\pmod q\), so there are at most \(q\). Since \(p<q\), the universal upper bound is \(q\). The family \(\{j/(qb):0\le j<q\}\) attains it. Equality with \(q>p\) forces the second axis, and all its \(q\) residue classes modulo \(q\) must occur once, establishing the asserted complete description of maximizers.

**Resonance and attainment.** Suppose first \(p\mid b\). Then \(p\nmid a\), by coprimality. Define
\[
\Lambda=\left\{\frac{i}{p}+\frac{j}{qb}:
0\le i<p,\ 0\le j<q\right\}.
\]
If two indexed frequencies have unequal \(j\), their difference \(t\) satisfies
\[
bt=\frac bp(i-i')+\frac{j-j'}q,
\]
where the first term is an integer and the second is a noninteger whose numerator is not divisible by \(q\); hence \(\widehat{\nu_{q,b}}(t)=0\). If their \(j\) are equal but \(i\) differ, then \(at=a(i-i')/p\) is a noninteger of order \(p\), so \(\widehat{\nu_{p,a}}(t)=0\). All \(pq\) frequency labels are distinct: otherwise the same argument applied to two different labels would force \(\widehat\mu(0)=0\), contrary to \(\widehat\mu(0)=1\).

If \(q\mid a\), interchange the two factors, using
\[
\Lambda=\left\{\frac{i}{q}+\frac{j}{pa}:
0\le i<q,\ 0\le j<p\right\};
\]
now \(q\nmid b\). This again gives \(pq\) orthogonal exponentials.

To see that the support has exactly \(pq\) points in either resonant case, suppose \(ia+jb=i'a+j'b\), with \(0\le i,i'<p\) and \(0\le j,j'<q\). Coprimality gives \(b\mid(i-i')\) and \(a\mid(j-j')\). When \(p\mid b\), one has \(b\ge p\), forcing \(i=i'\), then \(j=j'\). When \(q\mid a\), one has \(a\ge q\), forcing \(j=j'\), then \(i=i'\). The \(pq\) orthogonal exponentials therefore constitute a basis of the \(pq\)-dimensional space \(L^2(\mu)\), and no larger orthogonal family is possible.

Finally, in the nonresonant case the support has at least \(p+q-1>q\) distinct elements: the strictly increasing sequence of sums \(0,a,\ldots,(p-1)a,(p-1)a+b,\ldots,(p-1)a+(q-1)b\) has that length. Since the orthogonal capacity is only \(q\), no exponential orthonormal basis exists. The two stated cases are exhaustive because \(\gcd(pa,qb)>1\) is equivalent, under the hypotheses, to \(p\mid b\) or \(q\mid a\). \(\square\)

## Verification

The proof above covers all admissible primes and coprime steps, without relying on finite enumeration. For exact finite sanity checks, run `python3 check.py` from the directory containing this document. The standard-library-only script checks \(2550\) explicit frequency constructions by rational arithmetic and independently calculates clique numbers of \(88\) complete Fourier-zero residue graphs for small primes and steps. It prints `PASS` when those checks succeed. In particular, for \((p,q)=(2,3)\), the nonresonant steps \((a,b)=(1,1)\) have capacity \(3\), whereas \((1,2)\) and \((3,1)\) each have capacity \(6\). The checks are supplementary; they are not an exhaustive verification of all integer parameters.

## Relationship to prior work

The Fourier-zero criterion for orthogonal exponentials is standard in spectral-measure theory [1]. The 1998 convolution theorem of Jorgensen and Pedersen [1] constructs spectra under compatible factors; it does not provide the present nonresonant maximal-cardinality theorem. Zhou's 2026 theorem [2] characterizes spectrality of certain convolutions under the hypothesis that the first factor's Fourier-zero set together with zero is an additive subgroup. That hypothesis fails here: adding the zero \(1/(pa)\) to itself \(p\) times gives \(1/a\), which is not a zero of \(\nu_{p,a}\). The 2026 frame-measure obstruction for infinite uniform consecutive-digit convolutions [3] concerns infinitely many contraction levels, rather than the finite two-factor maximum. Classical cyclotomic tiling conditions [4] and more recent product-form spectral constructions [5] are relevant to existence of bases in the resonant case, but their existence statements do not imply the exact value \(q\) or classify every maximal nonresonant orthogonal family. The mathematical addition here is the exhaustive prime-resonance capacity and rigidity dichotomy, not the elementary fact that compatible uniform progressions can possess Fourier bases.

## Limitations

The positive spectral constructions are part of a known general theme of convolution-compatible spectra. Originality of the *quantitative nonresonant capacity and rigidity assertion* is supported by the sources checked, not by a proof that no equivalent theorem exists anywhere. This is a finite atomic result; it does not imply conclusions about infinite Bernoulli convolutions, Fourier frames with nonorthogonal elements, arbitrary weights, or composite digit counts. The infinite-dimensional or incommensurable analogues are not addressed.

## References

[1] P. E. T. Jorgensen and S. Pedersen, *Orthogonal harmonic analysis of fractal measures*, Electronic Research Announcements AMS 4 (1998), 35–42, https://ftp.gwdg.de/pub/misc/EMIS/journals/ERA-AMS/1998-01-006/1998-01-006.tex.html.

[2] T. Zhou, *Spectrality of convolution and product measures: a block decomposition approach*, first released October 25, 2026, arXiv:2610.33987, https://arxiv.org/html/2610.33987v1.

[3] X.-Y. Fu and W.-J. Wang, *Nonexistence of Frame Measures for Separated Uniform Consecutive-Digit Bernoulli Convolutions*, August 20, 2026, arXiv:2608.19676, https://arxiv.org/abs/2608.19676.

[4] E. M. Coven and A. D. Meyerowitz, *Tiling the integers with translates of one finite set*, arXiv:math/9802122, https://arxiv.org/abs/math/9802122.

[5] *Spectral Measures from Tiling Levels*, first released October 5, 2026, https://mrly.net/research/papers/spectral-tiling-levels/.
