# Short-cycle arithmetic of a quadratic finite-field permutation

## Finding

Let \(q=p^f\) be an odd prime power, and let \(\delta\in\mathbb F_q\) be a nonsquare. The quadratic map
\[
T_\delta(x,y,z)=(x+zy,\ y+\delta zx,\ z)
\]
permutes \(\mathbb F_q^3\) and has exactly \(q^2+q-1\) fixed points. Its permutation sign is always even. For all cycle lengths \(2\le d\le15\), its complete primitive-cycle spectrum is:

| Length \(d\) | Necessary and sufficient field condition | Number of cycles |
|---|---|---|
| \(8\) | \(p=3\) and \(f\) odd | \((q^2-1)/4\) |
| \(12\) | \(p=5\) and \(f\) odd | \((q^2-1)/6\) |
| \(15\) | \(p\in\{11,19\}\) and \(f\) odd | \(2(q^2-1)/15\) |
| Every other \(d\) with \(2\le d\le15\) | All odd prime powers | \(0\) |

These statements are independent of the choice of nonsquare \(\delta\). At every length, not only below the displayed cutoff, the full cycle spectrum is determined by a univariate polynomial greatest common divisor: define
\[
N_m(q)=\deg\gcd_{\mathbb F_q[X]}(X^m-1,X^q+X-2)-1.
\]
For \(d>1\) dividing \(q^2-1\), the number of cycles of exact length \(d\) is
\[
\frac{q^2-1}{d}\sum_{e\mid d}\mu(d/e)N_e(q).
\]
Other nontrivial lengths do not occur. The short-cycle classification above is the explicit characteristic-by-characteristic evaluation of the first arithmetically possible exceptional lengths, not merely an algorithm.

## Assumptions and scope

The field is \(\mathbb F_q\) with odd characteristic, \(q=p^f\), \(f\ge1\). The parameter \(\delta\) is an arbitrary nonsquare in \(\mathbb F_q^\times\). All cycles are cycles of the finite-set permutation \(T_\delta\) on \(\mathbb F_q^3\). A primitive cycle of length \(d\) means an orbit with least positive period exactly \(d\). The assertion for the complete small-period spectrum covers every integer \(2\le d\le15\); it does not assert absence of longer cycles.

## Proof

**1. Fiber diagonalization and cycle formula.** Choose \(\beta\in\mathbb F_{q^2}\) satisfying \(\beta^2=\delta\). Since \(\delta\) is a nonsquare, \(\beta^q=-\beta\). The \(\mathbb F_q\)-linear coordinate \(u=x+\beta^{-1}y\) identifies the \((x,y)\) plane with \(\mathbb F_{q^2}\), and on the fiber of fixed \(z\) the transformation is multiplication by \(\alpha_z=1+\beta z\). Its norm is \(1-\delta z^2\ne0\), hence every fiber is bijective. The map \(z\mapsto\alpha_z\) bijects \(\mathbb F_q\) with the roots of \(X^q+X-2\), because \(\alpha_z+\alpha_z^q=2\), and this polynomial has exactly \(q\) distinct roots. The fiber \(z=0\) is the identity. Each other fiber has one fixed point and \((q^2-1)/\operatorname{ord}(\alpha_z)\) cycles of common length \(\operatorname{ord}(\alpha_z)>1\). Therefore the fixed count is \(q^2+q-1\), and Möbius inversion of the count of \(\alpha_z\) whose orders divide \(m\) proves the displayed formula for every \(d\mid q^2-1\).

**2. Why the first possible nontrivial lengths are \(8,12,15\).** Suppose \(\alpha=\alpha_z\ne1\) has exact order \(d\ge2\). Then \(p\nmid d\), \(\alpha^q=2-\alpha\), and \(\alpha^{q^2}=\alpha\). Consequently \(q^2\equiv1\pmod d\). If \(q\equiv1\pmod d\), the trace equation gives \(2\alpha=2\), a contradiction. If \(q\equiv-1\pmod d\), it gives \(\alpha+\alpha^{-1}=2\), hence \((\alpha-1)^2=0\), another contradiction. For every \(d\) from \(2\) to \(15\), the unit group \((\mathbb Z/d\mathbb Z)^\times\) has a square root of one distinct from \(\pm1\) only at \(d=8,12,15\). Their remaining residues are \(3,5\), \(5,7\), and \(4,11\), respectively.

**3. Exact arithmetic and multiplicity.** For each possible residue \(r\), calculate the absolute integer resultant
\[
R_{d,r}=\left|\operatorname{Res}_X(\Phi_d(X),X^r+X-2)\right|.
\]
Here are all residues needed, including \(\pm1\) as controls:

| \(d\) | Residue \(r\) and exact \(R_{d,r}\) |
|---|---|
| \(8\) | \(1:32,\ 3:36,\ 5:16,\ 7:4\) |
| \(12\) | \(1:16,\ 5:25,\ 7:16,\ 11:1\) |
| \(15\) | \(1:256,\ 4:361,\ 11:121,\ 14:1\) |

These resultants are integer identities, independently reconstructed by the accompanying exact Bareiss-determinant verifier. Their only admissible odd-characteristic prime factors in the nontrivial-residue positions are \(3,5,19,11\), respectively. The corresponding reductions have monic polynomial gcds of degree exactly two:
\[
\begin{aligned}
(d,p,r)=(8,3,3)&:\quad X^2+X-1,\\
(12,5,5)&:\quad X^2-2X-1,\\
(15,19,4)&:\quad X^2-2X+7,\\
(15,11,11)&:\quad X^2-2X+4.
\end{aligned}
\]
For each case \(q=p^f\) has the required residue precisely when \(f\) is odd. The roots of \(\Phi_d\) are simple since \(p\nmid d\). Thus precisely two values of \(z\ne0\) have order \(d\) in each listed case and none otherwise. Multiplying the two nonzero fiber contributions \((q^2-1)/d\) gives the table. There are no other primitive lengths through \(15\) by the unit-group obstruction.

**4. Parity.** As a permutation on the additive group of a two-dimensional \(\mathbb F_q\)-space, an invertible linear transformation of determinant \(t\) has sign \(\chi_q(t)\), the quadratic character. This follows because elementary transvections are even in odd characteristic and diagonal generators reduce to the one-dimensional quadratic-character sign. The sign of the entire map is hence
\[
\chi_q\left(\prod_{z\in\mathbb F_q}(1-\delta z^2)\right).
\]
Since \(\beta^{q-1}=-1\), the finite-field product identity yields \(\prod_z(1+\beta z)=1-\beta^{q-1}=2\), and similarly \(\prod_z(1-\beta z)=2\). The product of determinants is \(4\), a square, so the sign is even.

## Verification

Run the included standalone Python 3 file `verify.py`. It computes all twelve integer resultants by a fraction-free determinant, checks the four characteristic-specific polynomial gcd degrees, verifies 132 prime-power short-spectrum gcd instances (including odd and even extension degrees), and checks 224 nonzero fibers across twelve prime fields for exact matrix order, forbidden periods, characteristic exceptions and norm-product parity. All checks completed successfully. They are finite consistency checks; the proof above establishes the results for all odd prime powers.

## Relationship to prior work

Chen's 2026 work supplies a general quadratic-plus-linear permutation criterion but no arithmetically resolved short-cycle spectrum. The bivariate classification of Pang, Li, Yuan and Zeng does not classify cycles of three-dimensional maps. Gerike and Kyureghyan analyze cycle invariance along one-dimensional additive lines in a different class. Bian, Chen and Zheng provide a general cycle-structure treatment for linearized permutation polynomials, applicable in principle to individual linear fibers; that broad apparatus does not itself provide the displayed uniform characteristic-resonance classification across this family. The underlying three-variable polynomial map was already explicitly discussed in a posted finite-field quadratic-permutation counterexample, and is **not** claimed as a new construction. The contribution assessed here is solely its explicit arithmetic small-cycle census, its extension to a general gcd formula, and its global parity statement.

## Limitations

The theorem describes nontrivial cycles of all lengths algorithmically but evaluates the cycle-count formula uniformly in closed characteristic form only for lengths at most \(15\). Its sign and fixed-point results are global. It makes no claim about conjugacy under polynomial automorphisms or about the full cycle distribution for lengths exceeding \(15\). Prior general linearized-cycle theorems and an unverified discussion of the underlying map create residual risk of an implicit earlier derivation of the special resonance table; a fully accessible text of the relevant 2026 linearized-cycle preprint was not available for complete comparison.

## References

1. Ruikai Chen, *Permutation polynomials from quadratic and linear forms*, arXiv:2611.09629v1, first submitted November 6, 2026. https://arxiv.org/html/2611.09629v1
2. Xuan Pang, Yangcheng Li, Pingzhi Yuan, Yuanpeng Zeng, *Determination of Some Types of Permutations over \(\mathbb F_q^2\) with Low-Degree*, arXiv:2508.01143, 2025. https://arxiv.org/html/2508.01143
3. Daniel Gerike and Gohar M. Kyureghyan, *Permutations on finite fields with invariant cycle structure on lines*, Designs, Codes and Cryptography 88 (2020), 1723–1740. https://doi.org/10.1007/s10623-020-00721-2
4. Huajun Bian, Shaoshi Chen, Dabin Zheng, *Cycle structures and parities of linearized permutation polynomials*, arXiv:2610.11574, first submitted October 8, 2026. https://arxiv.org/abs/2610.11574
5. *Classification conjecture for quadratic permutation systems over finite fields of odd characteristic*, MathDB discussion and posted construction, status as of August 2026. https://mathdb.com/p/369612/classification-conjecture-for-quadratic-permutation-systems
