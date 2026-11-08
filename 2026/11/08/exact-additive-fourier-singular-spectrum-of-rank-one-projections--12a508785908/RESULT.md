# Exact additive Fourier singular spectrum of rank-one projections over finite fields

## Finding
Fix a prime power \(q=p^f\ge2\), let \(F=\mathbb F_q\), and put
\[
\mathcal P=\{P\in M_2(F):P^2=P,\ \operatorname{rank}P=1\}.
\]
On \(G=M_2(F)\) with addition, let \(T_{\mathcal P}h=\mathbf1_{\mathcal P}*h\), with **unnormalized** convolution. The complete nonzero singular-value multiset of \(T_{\mathcal P}\), including multiplicities, is as follows. A row of multiplicity zero is omitted, and coincident values from different rows are added.

If \(p\) is odd, there are:

| Singular value | Multiplicity |
|:--|--:|
| \(q(q+1)\) | \(q\) |
| \(q\) | \(q(q^2-1)\) |
| \(2q\) | \(\frac{q^2(q+1)}{2}(q/p-1)\) |
| \(2q\cos(\pi j/p)\), for each \(1\le j\le(p-1)/2\) | \(q^3(q+1)/p\) |
| \(0\) | \(q^2(q-1)^2/2\) |

If \(p=2\), there are:

| Singular value | Multiplicity |
|:--|--:|
| \(q(q+1)\) | \(q\) |
| \(q\) | \(q(q^2-1)\) |
| \(2q\) | \(q^2(q+1)(q-2)/4\) |
| \(0\) | \(q^2(q-1)^2/2+q^3(q+1)/4\) |

Consequently
\[
\operatorname{rank}T_{\mathcal P}=\begin{cases}
q^4-q^2(q-1)^2/2,&p\text{ odd},\\
q^4-q^2(q-1)^2/2-q^3(q+1)/4,&p=2.
\end{cases}
\]
The **smallest positive singular value** is \(q\) if \(p=2\) or \(3\), and \(2q\sin(\pi/(2p))\) if \(p\ge5\). The exact Moore–Penrose condition number (largest divided by smallest nonzero singular value) is therefore \(q+1\) for \(p=2,3\), and \((q+1)/(2\sin(\pi/(2p)))\) for \(p\ge5\). In particular, it depends on the prime characteristic \(p\), not just the field size \(q\).

More precisely, fix \(\psi(t)=\exp(2\pi i\operatorname{Tr}_{F/\mathbb F_p}(t)/p)\). For any \(A\in M_2(F)\), let \(\mathscr E(A)\) denote the multiset of eigenvalues attached to its distinct \(F\)-rational eigenlines (one entry per line, rather than per algebraic multiplicity). The exact Fourier multiplier is
\[
\widehat{\mathbf1_{\mathcal P}}(A)=\sum_{P\in\mathcal P}\psi(\operatorname{tr}(AP))
=q\sum_{\lambda\in\mathscr E(A)}\psi(\lambda).
\]
This formula classifies *every* Fourier zero: for odd \(p\), precisely the matrices with irreducible quadratic characteristic polynomial; for \(p=2\), those matrices and also the matrices with two distinct rational eigenvalues \(\lambda,\mu\) satisfying \(\operatorname{Tr}_{F/\mathbb F_2}(\lambda+\mu)=1\).

## Assumptions and scope
The domain includes every finite field, both prime and nonprime, and all prime characteristics. \(\operatorname{tr}\) on matrices is the ordinary matrix trace; \(\operatorname{Tr}_{F/\mathbb F_p}\) is the absolute field trace. The Fourier pairing is \(\psi(\operatorname{tr}(AP))\), not an entrywise pairing without transpose. Singular values are the absolute values of Fourier multipliers, because the finite abelian group convolution is unitarily diagonalized by its characters. Values and multiplicities refer to the operator on the full \(q^4\)-dimensional complex function space. No assertion is made about larger matrix sizes or nonfield rings.

## Proof
**Projector parametrization and exact transform.** Every rank-one idempotent has a representation \(P=uv^{\mathsf T}\) with \(u\in F^2\setminus\{0\}\) and \(v^{\mathsf T}u=1\). Exactly \(q-1\) such pairs represent any fixed \(P\), via simultaneous inverse rescaling. For fixed \(u\ne0\), the inner character sum over the affine line of \(v\) satisfying \(v^{\mathsf T}u=1\) is zero unless \(Au\in Fu\), by character orthogonality along its one-dimensional direction. If \(Au=\lambda u\), that sum is \(q\psi(\lambda)\). Summing over \(u\), dividing by \(q-1\), and grouping the \(q-1\) nonzero vectors on each eigenline proves the displayed multiplier identity. It also gives \(|\mathcal P|=q(q+1)\).

**Similarity types and numbers.** Every \(2\times2\) matrix lies in exactly one of four types: scalar, repeated-eigenvalue nonscalar Jordan, split distinct-eigenvalue semisimple, or irreducible quadratic. Their total numbers are respectively \(q\), \(q(q^2-1)\), \(q^2(q^2-1)/2\), and \(q^2(q-1)^2/2\). The corresponding numbers of rational eigenlines are \(q+1\), one, two, and zero. A nonscalar Jordan class at a fixed eigenvalue has \(q^2-1\) matrices; a split distinct unordered eigenvalue pair has \(q(q+1)\) matrices; an irreducible quadratic class has \(q(q-1)\) matrices. These class sizes follow by orbit–stabilizer in \(\mathrm{GL}_2(F)\), with centralizer orders \(q(q-1)\), \((q-1)^2\), and \(q^2-1\), respectively. There are \(q(q-1)/2\) monic irreducible quadratics.

**Split classes and trace fibres.** For split distinct eigenvalues \(\lambda\ne\mu\), the modulus is \(q|\psi(\lambda)+\psi(\mu)|\). For any \(\delta\ne0\) the ordered pairs \((\lambda,\mu)\) with \(\lambda-\mu=\delta\) number \(q\). Dividing by two after summing over an invariant set of nonzero differences gives unordered pairs. The field trace has exactly \(q/p\) elements in each fibre. In odd characteristic, the count for trace-difference zero is \(q(q/p-1)/2\), and the count for each union of trace-difference fibres \(\{j,-j\}\), \(1\le j\le(p-1)/2\), is \(q^2/p\). Their moduli are respectively \(2q\) and \(2q\cos(\pi j/p)\), all positive. In characteristic two, the corresponding unordered-pair counts are \(q(q-2)/4\) for trace difference zero and \(q^2/4\) for trace difference one, giving respectively modulus \(2q\) and zero. Multiplication by the class size \(q(q+1)\) yields every displayed split multiplicity.

**Remaining types and extrema.** The scalar multipliers are \(q(q+1)\psi(\lambda)\), the Jordan multipliers are \(q\psi(\lambda)\), and the irreducible multipliers vanish. These yield the entire singular-value table and kernel dimension; the multiplicities sum to \(q^4\). Since the maximum multiplier modulus is the number of summands \(|\mathcal P|\), the spectral maximum is \(q(q+1)\), attained at frequency zero. For odd \(p\), cosine decreases strictly on \([0,\pi/2]\), and the smallest split magnitude occurs at \(j=(p-1)/2\) and equals \(2q\sin(\pi/(2p))\). It equals \(q\) when \(p=3\) and is strictly less than \(q\) for \(p\ge5\). When \(p=2\), the only nonzero magnitudes are \(q\), \(2q\) (possibly absent), and \(q(q+1)\). The Jordan sector always exists, so the minimum is \(q\). The precise condition number follows.

## Verification
The standalone `CHECK.py` enumerates all rank-one idempotents and all additive matrix frequencies for fields of sizes \(2,3,4,5,7,9\). It constructs field extensions exactly, compares direct Fourier character-count vectors to the eigenline formula modulo the cyclotomic relation \(1+\zeta_p+\cdots+\zeta_p^{p-1}=0\), checks the exact Fourier-zero criterion, and checks every multiplicity. No numerical zero tolerance is used for these identities. Run `python CHECK.py` using Python 3 standard library. Finite checks corroborate but do not prove the all-fields theorem; the proof above is the infinite argument.

## Relationship to prior work
The calculation uses the classical additive-character orthogonality underlying finite-field Fourier analysis and the standard similarity classification of \(2\times2\) matrices. Gadouleau–Yan (2007) develop rank-metric character transforms, but their rank-invariant framework does not distinguish trace-one rank-one idempotents from other rank-one matrices. Iosevich–Koh (2008) examine nondegenerate finite-field quadratic surfaces and derive Fourier decay estimates from Gauss, Salié and Kloosterman sums; the current result is an exact phase-and-multiplicity classification of a particular affine quadric, including characteristic two and the sharp least nonzero multiplier, rather than a decay estimate. De Seguins Pazzis (2009) studies sums of idempotent matrices and does not determine their additive Fourier singular spectrum. Classical quadratic-form/Salié formulas may supply alternate derivations of the individual multipliers; the additional orbit counts and global extremal optimization are essential to the stated complete spectrum.

## Limitations
This is a self-review, not an independently audited or published theorem. No generalization beyond \(2\times2\) matrices over finite fields is asserted. Although direct coverage was not located in the inspected literature, an unlocated exact conjugacy-class transform or specialized quadratic-sphere theorem might subsume the calculation. The full singular-value multiset and conditioning do not alone imply new coding or expansion bounds without further analysis.

## References
1. M. Gadouleau and Z. Yan, *MacWilliams Identity for Codes with the Rank Metric*, arXiv:0706.1751, first public 2007-06-12, https://arxiv.org/abs/0706.1751.
2. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505, first public 2008-04-28, https://arxiv.org/abs/0804.4505.
3. C. de Seguins Pazzis, *On sums of idempotent matrices over a field of positive characteristic*, arXiv:0907.5360, first public 2009-07-30, https://arxiv.org/abs/0907.5360.
