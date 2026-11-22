# GC-content spectrum of short-tandem-irreducible DNA words

## Finding

Let \(\Sigma=\{A,T,C,G\}\), with GC indicator \(g(C)=g(G)=1\) and \(g(A)=g(T)=0\). Let \(c_{n,w}\) be the number of indexed, length-\(n\) words over \(\Sigma\) having exactly \(w\) GC symbols and containing neither a square of block length one nor a square of block length two. In other words, their adjacent symbols are unequal and they have no contiguous factor of the form \(abab\), where \(a,b\in\Sigma\).

The complete length-by-GC-content enumerator is the following explicit rational function:

\[
F(z,u)=\sum_{n\ge 0}\sum_{w=0}^{n}c_{n,w}z^nu^w=\frac{N(z,u)}{D(z,u)},
\]

where

\[
\begin{aligned}
D(z,u)={}&1-3uz^2-4u(u+1)z^3\\
 &-u(4u^2+3u+4)z^4-2u^2(u+1)z^5\\
 &+2u^2(u^2+1)z^6+4u^3(u+1)z^7+4u^4z^8,\\[4pt]
N(z,u)={}&1+2(u+1)z+(u+2)(2u+1)z^2\\
 &+2(u+1)^3z^3+u(6u^2+5u+6)z^4\\
 &+2u(u+1)(u^2+u+1)z^5\\
 &-2u^2(u+1)(u^2+u+1)z^7\\
 &-4u^3(u^2+u+1)z^8-4u^4(u+1)z^9.
\end{aligned}
\]

In particular, for even length \(n\), the exactly GC-balanced count has the sharp asymptotic

\[
\boxed{\displaystyle
c_{n,n/2}\sim
\frac{6\sqrt3}{\sqrt{\pi(7\sqrt3-6)}}\,
\frac{(1+\sqrt3)^n}{\sqrt n}}
\quad (n\to\infty,\ 2\mid n).
\]

For a uniformly chosen legal word of length \(n\), with \(X_n\) its number of GC symbols, the associated fluctuations satisfy

\[
\frac{X_n-n/2}{\sqrt{\frac{7\sqrt3-6}{72}\,n}}
\ \Longrightarrow\ \mathcal N(0,1).
\]

The exponential growth rate \(\log_2(1+\sqrt3)\) bits per base was already known; the exact composition enumerator, Gaussian variance, and evaluated balanced prefactor are the additional statements here.

## Assumptions and scope

All words are linear, indexed strings (not circular words, necklaces, or codebooks). The alphabet comprises four distinct symbols; any relabeling respecting the two GC and two AT symbols gives the same counts. A forbidden square is an adjacent repetition of a nonempty block of length exactly one or two; squares of longer block length are not forbidden unless they incidentally contain a shorter forbidden square. No strand-complement, secondary-structure, or inter-codeword-distance constraint is imposed. Empty words are counted once; the count is zero outside \(0\le w\le n\).

The formulas hold for every integer \(n\ge0\), and the coefficient asymptotic is along even integers only. The central limit theorem is for the uniform distribution on the nonempty finite set of legal words of each length.

## Proof

**1. A finite deterministic enumeration.** Map \(A,T,C,G\) to \(0,1,2,3\). For a legal suffix triple \((a,b,c)\), append \(d\) if and only if \(d\ne c\) and it is not the case that both \(a=c\) and \(b=d\). The first condition excludes new length-one squares; the second excludes new length-two squares. Each newly appended \(d\) contributes a factor \(u^{g(d)}\). Since these are precisely the forbidden factors that can first appear upon appending, the rule is necessary and sufficient.

The 36 legal triples form a finite directed graph. Independent swaps of the two AT letters and of the two GC letters commute with both the rule and the weighting. Quotient by this four-element group. There are ten orbits, with representatives, orbit sizes, and initial GC weights respectively:

| Index | Representative | Orbit size | GC weight |
|---:|:---:|---:|---:|
| 1 | `010` | 2 | 0 |
| 2 | `012` | 4 | 1 |
| 3 | `020` | 4 | 1 |
| 4 | `021` | 4 | 1 |
| 5 | `023` | 4 | 2 |
| 6 | `201` | 4 | 1 |
| 7 | `202` | 4 | 2 |
| 8 | `203` | 4 | 2 |
| 9 | `230` | 4 | 2 |
| 10 | `232` | 2 | 3 |

Let \(M\) be the ten-by-ten matrix with transition polynomial \(M_{ij}\) equal to the total weights of letters taking representative \(i\) into orbit \(j\). Its nonzero entries (all other entries are zero) are

\[
\begin{aligned}
&M_{1,2}=2u;\quad M_{2,3}=1,\ M_{2,4}=1,\ M_{2,5}=u;\\
&M_{3,6}=1,\ M_{3,8}=u;\quad M_{4,6}=1,\ M_{4,7}=u,\ M_{4,8}=u;\\
&M_{5,9}=2,\ M_{5,10}=u;\quad M_{6,1}=1,\ M_{6,2}=2u;\\
&M_{7,4}=1,\ M_{7,5}=u;\quad M_{8,3}=1,\ M_{8,4}=1,\ M_{8,5}=u;\\
&M_{9,6}=1,\ M_{9,7}=u,\ M_{9,8}=u;\quad M_{10,9}=2.
\end{aligned}
\]

The initial row vector is

\[
 b=(2,4u,4u,4u,4u^2,4u,4u^2,4u^2,4u^2,2u^3).
\]

Thus the combinatorial decomposition gives the exact formal-power-series identity

\[
F(z,u)=1+2(1+u)z+(2+8u+2u^2)z^2
   +z^3b(I-zM)^{-1}\mathbf1.
\]

**2. Exact rational evaluation and infinite-length certificate.** Integer polynomial arithmetic gives \(\det(I-zM)=D(z,u)\). Multiplying the preceding expression by \(D(z,u)\) and expanding by the adjugate identity gives precisely \(N(z,u)\). This finite identity may be checked without trusting a guessed recurrence: the accompanying standalone verifier obtains all ten characteristic coefficients with the Faddeev--LeVerrier trace identities, checks that the characteristic determinant equals the displayed \(D\), and computes the first 13 coefficients of \(D F\). The adjugate formula makes \(D F\) a polynomial of degree at most twelve in \(z\), because an adjugate entry has degree at most nine, its term has the prefactor \(z^3\), and the initial polynomial is quadratic. Therefore these thirteen exact polynomial coefficients exhaust the entire identity, proving the formula for every \(n\), not just the finitely enumerated examples.

**3. The unweighted dominant singularity.** At \(u=1\) the rational expression simplifies to

\[
F(z,1)=\frac{(1+2z)(1+2z^2)}{1-2z-2z^2}.
\]

Its simple smallest-modulus pole is \(r=(\sqrt3-1)/2\), with reciprocal \(1+\sqrt3\), and its residue supplies

\[
\sum_{w}c_{n,w}\sim\sqrt3(1+\sqrt3)^n.
\]

**4. Quasi-powers, variance, and the exact central coefficient.** The 36-state transition graph is strongly connected: from each of its 36 vertices, a finite breadth-first search reaches all 36; this complete finite statement is replayed in the verifier. The periodic legal words `012` and `0121` give closed walks with respective (length, GC-weight) vectors \((3,1)\) and \((4,1)\). These generate \(\mathbb Z^2\), since their determinant is \(-1\). Consequently the graph is primitive and the GC statistic is strongly aperiodic on the full lattice. Standard finite-state Perron--Frobenius perturbation and the lattice local central limit theorem apply, including at exactly \(w=n/2\) when \(n\) is even.

Let \(r(u)\) be the analytic branch of \(D(r(u),u)=0\) satisfying \(r(1)=r\). Differentiation with respect to \(t=\log u\) gives

\[
\left.-\frac{d}{dt}\log r(e^t)\right|_{t=0}=\frac12,
\qquad
\left.-\frac{d^2}{dt^2}\log r(e^t)\right|_{t=0}
=\frac{7\sqrt3-6}{72}>0.
\]

The exchange of the AT and GC groups also directly proves the finite symmetry \(c_{n,w}=c_{n,n-w}\), and therefore exact mean \(n/2\). The finite-state local limit then gives

\[
\frac{c_{n,n/2}}{\sum_w c_{n,w}}
\sim\frac1{\sqrt{2\pi n(7\sqrt3-6)/72}},
\]

which, together with Step 3, simplifies to the boxed prefactor. This also proves the stated central limit theorem.

## Verification

`verification.py` uses only Python's standard library. It builds the orbit matrix from the actual four-symbol append rule, computes \(\det(I-zM)\) by exact integer-polynomial Faddeev--LeVerrier arithmetic, checks the numerator identity coefficient-by-coefficient beyond the algebraically sufficient degree twelve, enumerates all words through length eight independently, verifies the GC-exchange symmetry, and checks strong connectivity of the 36-state graph. These exact finite computations support the finite matrix identities used in the proof; the extrapolation to arbitrary length follows algebraically, not from finite sampling.

Examples of exact GC-balanced counts are \(c_{4,2}=48\), \(c_{6,3}=320\), \(c_{8,4}=2192\), and \(c_{10,5}=15104\).

## Relationship to prior work

Chee, Chrisnata, Kiah and Nguyen explicitly study the same GC balance and length-at-most-two irreducibility constraints. In their 2020 paper, immediately preceding Corollary 4, they state that they do not provide an explicit recurrence for the balanced irreducible count; the corollary proves equality of its exponential rate to the unbalanced rate. The present count refines rather than replaces that known rate: it determines every length-and-composition coefficient and the asymptotic constant, not just the exponential base.

Their 2018 irreducible-word preprint gives unweighted encoding and counting theory. Yu and Schwartz (2024) construct duplication-free codes for related error models but do not give this fixed-GC enumerator. The full-text comparisons support the stated distinction; they do not establish an exhaustive historical-priority claim.

## Limitations

This is a language-enumeration result, not an assertion that the full legal language is itself a tandem-duplication-correcting code. GC balance is only a compositional constraint; no claim about actual DNA folding, thermodynamics, strand cross-hybridization, or correction of substitutions/deletions is made. The Gaussian and coefficient asymptotics are valid in the indicated large-length limits, not exact probability laws for finite length. Possible equivalent older transfer-matrix or constrained-system formulations not identified in the checked literature remain a priority risk.

## References

1. Y. M. Chee, J. Chrisnata, H. M. Kiah and T. T. Nguyen, *Efficient Encoding/Decoding of Irreducible Words for Codes Correcting Tandem Duplications*, preprint first posted January 8, 2018, https://arxiv.org/abs/1801.02310.
2. Y. M. Chee, J. Chrisnata, H. M. Kiah and T. T. Nguyen, *Efficient Encoding/Decoding of GC-Balanced Codes Correcting Tandem Duplications*, IEEE Transactions on Information Theory 66 (2020), 4892–4903, https://doi.org/10.1109/TIT.2020.2981069; author-hosted full text: https://ymchee66.github.io/home/PDF/encgcbalancedjournal.pdf.
3. W. Yu and M. Schwartz, *On Duplication-Free Codes for Disjoint or Equal-Length Errors*, preprint first posted January 9, 2024, https://arxiv.org/abs/2401.04675.
