# Sharp three-basis support uncertainty in prime dimensions five and seven

## Finding
For \(p\in\{5,7\}\), take the standard complete collection of \(p+1\) mutually unbiased bases of \(\mathbb C^p\), comprising the coordinate basis and the \(p\) quadratic Fourier bases. For **every** choice of three distinct bases \(\mathcal B_1,\mathcal B_2,\mathcal B_3\), the sharp total-support inequality is
\[
\min_{0\ne v\in\mathbb C^p}\ \sum_{j=1}^3 |\operatorname{supp}_{\mathcal B_j}(v)|=2p.
\]
Equivalently, at most \(p\) of the \(3p\) amplitude coordinates can vanish simultaneously. In dimensions five and seven the sharp minima are, respectively, \(10\) and \(14\). This statement is for the standard finite-field family of bases, not an arbitrary unrelated triple of complex Hadamard bases.

## Assumptions and scope
Let \(p\) be \(5\) or \(7\), \(\omega=\exp(2\pi i/p)\), and index coordinate locations by \(t\in\mathbb F_p\). The coordinate basis \(\mathcal B_\infty\) consists of the unit impulses \(\delta_t\). For \(a\in\mathbb F_p\), the basis \(\mathcal B_a\) consists of the vectors
\[
\phi_{a,b}(t)=p^{-1/2}\omega^{a t^2+b t},\qquad b\in\mathbb F_p.
\]
The quadratic Gauss-sum identity proves these bases are pairwise mutually unbiased. The support of \(v\) relative to a basis counts its nonzero inner-product coordinates, not the magnitudes or their approximate numerical values. There are no restrictions on the complex coefficients of \(v\).

## Proof
**1. Rank formulation.** A zero coefficient \(\langle\phi_{a,b},v\rangle\) is a linear constraint on \(v\). Its row is, up to a nonzero normalization and replacement of \((a,b)\) by \((-a,-b)\), the vector \((\omega^{a t^2+b t})_{t\in\mathbb F_p}\). The coordinate-basis constraints are standard unit rows. For three bases this produces \(3p\) distinct rows. If a nonzero \(v\) had at least \(p+1\) zero coefficients, some \((p+1)\)-row submatrix would have rank at most \(p-1\) over \(\mathbb C\).

**2. Rigorous rank certificate.** All row entries belong to \(\mathbb Z[\omega]\). For \(p=5\) reduce \(\omega\) modulo a prime ideal by \(\omega\mapsto95\) in \(\mathbb F_{101}\); for \(p=7\), use \(\omega\mapsto16\) in \(\mathbb F_{29}\). In each case the image has *exact* multiplicative order \(p\), hence annihilates \(1+X+\cdots+X^{p-1}\) and defines a ring homomorphism \(\mathbb Z[\omega]\to\mathbb F_q\). An \(p\times p\) minor that is nonzero after reduction was nonzero over \(\mathbb C\).

The accompanying `CHECK.cpp` enumerates **every** three-element subset of the \(p+1\) bases and, within each triple, **every** subset of \(p+1\) of the \(3p\) analysis rows. It performs modular Gaussian elimination and checks that each selected matrix has rank \(p\). The exhaustive counts are
\[
\begin{array}{c|c|c|c}
p&q&\binom{p+1}{3}&\binom{p+1}{3}\binom{3p}{p+1}\\\hline
5&101&20&100100\\
7&29&56&11395440
\end{array}
\]
with no rank failures. This is a finite *exact* certificate, not floating-point evidence. Thus no nonzero vector can have more than \(p\) zeros across any three selected bases, and its total support is at least \(3p-p=2p\).

**3. Equality for every triple.** Multiplication by a quadratic chirp, \(D_c v(t)=\omega^{c t^2}v(t)\), permutes the standard bases by \(a\mapsto a+c\), fixing \(\infty\). The finite Fourier transform exchanges the bases labelled \(0\) and \(\infty\) and maps every other quadratic basis to another quadratic basis, by completion of the square. Hence an invertible unitary transformation from these operations maps any chosen basis in a triple to \(\mathcal B_\infty\), while permuting the remaining two into distinct finite bases.

In these coordinates take \(v=\delta_0-\delta_1\). It has exactly \(p-2\) zero coordinate entries, and in **each** quadratic basis the analysis coefficients are proportional to
\[
1-\omega^{-(a+b)},
\]
which vanishes exactly at \(b=-a\). Thus the three selected bases have \((p-2)+1+1=p\) zero outcomes, or total support \(2+(p-1)+(p-1)=2p\). Transporting back gives equality for the original arbitrary triple.

## Verification
`CHECK.cpp` is a standalone ISO C++17 exact-integer implementation. Execute `c++ -O3 -std=c++17 CHECK.cpp -o check && ./check`. Successful output is exactly:

```
CHECK_OK p=5 modulus=101 root=95 triples=20 rank_certificates=100100
CHECK_OK p=7 modulus=29 root=16 triples=56 rank_certificates=11395440
```

No external data are needed. The checker builds all three-basis row matrices from the stated formulas, validates every rank over a prime field, and terminates with a nonzero status at the first counterexample. Since the proof uses only implications from nonzero reduced minors to nonzero complex minors, modular bad reduction cannot yield a false positive proof. The analytic equality construction is independent of the enumeration.

## Relationship to prior work
Fiorentino and Weigert (2022) derived from pairwise prime-Fourier uncertainty the three-basis lower bound \(3(p+1)/2\), namely \(9\) in dimension five and \(12\) in dimension seven. They explicitly identify sharp triple-basis inequalities as future work and report preliminary evidence against saturation of their bound outside dimension three. The present inequality gives the **sharp** values \(10\) and \(14\) for the first two such prime dimensions.

Li (2026) solved the **complete** \((p+1)\)-basis total-support problem and proved a parity-sensitive bound on zeros across *all* quadratic Fourier bases. Those results do not give the stated sharp bound for an **arbitrary selected triple**: restricting a complete-family total-zero estimate to three bases loses the necessary positional information. The present exact rank certificate supplies that missing finite-family incidence statement. Related published finite-parabola support classifications address a fixed spatial support, not the arbitrary-triple support minimum of this theorem.

## Limitations
This theorem proves only \(p\in\{5,7\}\), not a universal prime-dimension formula; it does not classify all minimizing rays or establish noise stability. It applies to the standard quadratic finite-field MUB family, not arbitrary triples of mutually unbiased bases in other constructions. The proof uses exhaustive exact modular elimination for the upper bound rather than a conceptual non-enumerative argument. Publication priority relative to unindexed equivalent finite-dimensional computations is not fully settled.

## References
1. V. Fiorentino and S. Weigert, *Uncertainty relations for the support of quantum states*, J. Phys. A 55 (2022), 495305; first public arXiv version 2022-09-20, https://arxiv.org/abs/2209.09817. In particular Section 3.2, equation (31), and Section 6.
2. D. Li, *Parity-Sensitive Fourier Uncertainty and Zero-Set Rigidity on the Finite Parabola*, first public arXiv version 2026-09-11, https://arxiv.org/abs/2609.16030. Related complete-MUB and parabolic zero theorems; not a triple-basis support classification.
3. T. Tao, *An uncertainty principle for cyclic groups of prime order*, Math. Res. Lett. 12 (2005), 121–127, https://arxiv.org/abs/math/0308286.
