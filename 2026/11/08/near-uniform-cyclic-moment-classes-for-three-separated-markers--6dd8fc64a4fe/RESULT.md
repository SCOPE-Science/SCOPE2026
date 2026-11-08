# Near-uniform cyclic moment classes for three separated markers

## Finding

Fix integers \(h\ge2\) and \(n\ge3h\). Let \(\mathcal W_{n,h}\) be the set of indexed binary circular words \(w=(w_0,\ldots,w_{n-1})\) with exactly three ones and with at least \(h-1\) zeros between any two successive ones, including across the circular boundary. Indexing is retained: rotations are generally different words. Define the first-position moment, or checksum,
\[
S(w)=\sum_{j=0}^{n-1}j w_j\pmod n,
\]
and let \(A_{n,h}(s)=|\{w\in\mathcal W_{n,h}:S(w)=s\}|\) for \(s\in\mathbb Z/n\mathbb Z\). Set
\[
Q_{n,h}=\binom{n-3h+2}{2}.
\]
Then the **complete moment-bucket distribution**, simultaneously for all admissible \(n,h,s\), is
\[
\boxed{A_{n,h}(s)=\begin{cases}
Q_{n,h}/3,&3\nmid n,\\[2pt]
(Q_{n,h}-1)/3+\mathbf1_{\{s\equiv0\ (\mathrm{mod}\ 3)\}},&3\mid n.
\end{cases}}
\]
In particular, every checksum bucket is equally large when \(3\nmid n\); when \(3\mid n\), precisely one third of the buckets have one more word than the remaining buckets. The total number of admissible indexed words is \(nQ_{n,h}/3\). Thus the largest-minus-smallest bucket discrepancy is at most one, including at the extremal boundary \(n=3h\).

## Assumptions and scope

Positions are elements of \(\mathbb Z/n\mathbb Z\), identified with \(0,\ldots,n-1\) only for the checksum. If the successive marked positions in cyclic order are \(i\), \(i+a\), \(i+a+b\), their positive circular spacings satisfy \(a,b,c\ge h\) and \(a+b+c=n\). A word retains its fixed position labels. No quotient by rotation or reflection is taken. The parameter \(h\ge2\) imposes a genuinely nontrivial circular run-length constraint; the unconstrained boundary \(h=1\) follows from the same calculation but is not a novelty claim here.

The modulus is exactly \(n\), **not** \(n+1\). The theorem counts moment classes; it neither assumes nor concludes that its individual classes correct deletions or insertions.

## Proof

**1. Marked cyclic-gap parameterization.** Mark one of the three ones as the initial marker, at position \(i\). The next two markers occur at \(i+a\) and \(i+a+b\), where \(a,b,c\ge h\) and \(a+b+c=n\). Conversely every \((i,a,b,c)\) with these conditions represents one marked admissible word. Each unmarked indexed word is represented **exactly three times**, one for each choice of initial marker. Writing \(a=h+u\), \(b=h+v\), \(c=h+t\) with \(u+v+t=n-3h\), stars and bars gives exactly \(Q_{n,h}=\binom{n-3h+2}{2}\) admissible ordered gap triples. The three positions have checksum
\[
S\equiv i+(i+a)+(i+a+b)=3i+2a+b\pmod n.
\]
Thus \(|\mathcal W_{n,h}|=nQ_{n,h}/3\), a count of distinct indexed words, not merely their marked descriptions.

**2. Length coprime to three.** Suppose \(3\nmid n\). For each gap triple and each residue \(s\), the congruence \(3i\equiv s-2a-b\pmod n\) has exactly one solution \(i\in\mathbb Z/n\mathbb Z\). There are therefore \(Q_{n,h}\) marked descriptions with checksum \(s\), and each actual word contributes exactly three. Hence \(A_{n,h}(s)=Q_{n,h}/3\). This also proves the displayed quotient is integral.

**3. Length divisible by three.** Suppose \(3\mid n\). The same congruence has three solutions for \(i\) if \(s\equiv2a+b\pmod3\), and none otherwise. Dividing the number of marked descriptions by three shows that \(A_{n,h}(s)\) equals the number of gap triples satisfying \(2a+b\equiv s\pmod3\). Since \(a=h+u\), \(b=h+v\), this condition becomes \(2u+v\equiv s\pmod3\). Here \(m=n-3h\) is a nonnegative multiple of three.

Let \(\omega\) be a primitive cube root of unity. The ordinary finite composition-counting generating function has the weighted identity
\[
\sum_{u,v,t\ge0}\omega^{2u+v}z^{u+v+t}
=\frac{1}{(1-\omega^2z)(1-\omega z)(1-z)}
=\frac1{1-z^3}.
\]
The same identity holds with \(\omega\) replaced by \(\omega^2\). Therefore the two nontrivial Fourier sums of the \(Q_{n,h}\) triples, in degree \(m\), are both exactly one. If \(C_r\) counts triples with \(2u+v\equiv r\pmod3\), then Fourier inversion yields
\[
C_0=\frac{Q_{n,h}+2}{3},\qquad C_1=C_2=\frac{Q_{n,h}-1}{3}.
\]
Consequently \(A_{n,h}(s)=C_{s\bmod3}\), which is precisely the claimed formula. Since \(m\) is a multiple of three, \(Q_{n,h}\equiv1\pmod3\), consistent with integrality. All endpoints, including \(m=0\), are included.

## Verification

The independent standard-library program `verify.py` enumerates unordered three-position subsets directly, tests all three wrapped spacings and computes the labeled checksum. It compares the resulting \(n\) integer bucket counts with the closed formula for every \(6\le n\le42\) and \(2\le h\le\lfloor n/3\rfloor\), a total of 247 parameter pairs. Its successful local output is `VERIFY_OK 247 independent parameter checks (6 <= n <= 42, h >= 2)`. The finite program is a consistency check, **not** the proof for arbitrarily large parameters; the proof above is exact for all \(n,h\).

Reproduce using the Python standard library alone: `python verify.py`.

## Relationship to prior work

Cheng, Ferreira and Broere [1] study first-order moment balancing in \((d,k)\)-constrained binary sequences, motivated by constrained error correction. Their public full text defines the moment and designs balancing templates, but does not give this all-length, exactly-three-one, **circular** gap-restricted distribution. Kulkarni and Kiyavash [2] study bounds on deletion-correcting code sizes for several constrained families, including run-length-limited constraints; their code-size bounds do not imply these per-residue counts. Chan [3] relates unrestricted modular subset sums to necklaces; the unconstrained \(h=1\) case is not presented as new, and an unrestricted counting formula does not itself evaluate the minimum-spacing restriction \(h\ge2\). The independent-set representation using a power of a cycle gives an equivalent formulation: exact distribution of the index sum over size-three independent sets in the cyclic distance graph.

The distinct claims in earlier local work on three-marked circular words concern *palindromic-factor counts*, not position-moment residues. The mathematical invariants are different, and no equivalence or dominating implication was found in the compared statements. The present theorem is self-contained; a failed search alone is not evidence of historical uniqueness.

## Limitations

The result is restricted to indexed circular binary words of Hamming weight exactly three, a uniform lower bound on **all three** circular spacings, and checksum modulus \(n\). It provides no per-bucket formula at higher Hamming weights, mixed individual gap bounds, or different moment moduli. No claim is made about deletion correction, asymptotic code capacity, or uniqueness in the full historical literature. Potential older combinatorial treatments of cycle independent-set weights remain a historical-priority risk.

## References

[1] L. Cheng, H. C. Ferreira and I. Broere, *Moment Balancing Templates for (d,k) Constrained Codes*, IEEE ISIT 2010, pp. 1218–1222. https://doi.org/10.1109/ISIT.2010.5513415 . Public author text: https://www.researchgate.net/publication/221136979_Moment_Balancing_Templates_for_d_k_Constrained_Codes .

[2] A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128, first posted November 13, 2012. https://arxiv.org/abs/1211.3128 .

[3] S. H. Chan, *A bijection between necklaces and multisets with divisible subset sum*, arXiv:1802.03507, first posted February 10, 2018. https://arxiv.org/abs/1802.03507 . Supporting literature only; this newer reference does not determine the archive classification.
