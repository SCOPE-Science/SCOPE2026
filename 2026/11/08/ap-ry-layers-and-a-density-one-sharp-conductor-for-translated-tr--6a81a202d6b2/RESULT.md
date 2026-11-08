# Apéry layers and a density-one sharp conductor for translated triangular-number semigroups

## Finding
For an integer \(a\ge2\), put \(T_j=j(j+1)/2\) for \(j\ge0\) and consider the numerical semigroup
\[
S_a=\langle a+T_j:j\ge0\rangle=\langle a,a+1,a+3,a+6,\ldots\rangle.
\]
For each \(1\le r<a\), define \(h_a(r)\in\{1,2,3\}\) by the following exhaustive rules:

1. \(h_a(r)=1\) if \(r\) is triangular.
2. Otherwise, \(h_a(r)=2\) if \(r\) is a sum of two nonnegative triangular numbers, or if \(r+a\) is triangular.
3. In every remaining case, \(h_a(r)=3\).

Then the Apéry representative of the residue \(r\) modulo \(a\) is exactly
\[
w_a(r)=r+a h_a(r),\qquad w_a(0)=0.
\]
In particular, the genus is given exactly by
\[
g(S_a)=\sum_{r=1}^{a-1}h_a(r)
=3(a-1)-2E_1(a)-E_2(a),
\]
where \(E_i(a)=\#\{1\le r<a:h_a(r)=i\}\) for \(i=1,2\). The conductor has the **sharp exact criterion**
\[
c(S_a)=3a \quad\Longleftrightarrow\quad
 a-1\text{ is not a sum of two nonnegative triangular numbers and }2a-1\text{ is not triangular}.
\]
Moreover, as \(a\to\infty\), with absolute implicit constants,
\[
g(S_a)=3a+O\!\left(\frac{a}{\sqrt{\log a}}\right),\qquad
c(S_a)=3a+O\!\left(\frac{a}{\sqrt{\log a}}\right),\qquad
\frac{g(S_a)}{c(S_a)}=1+O\!\left(\frac1{\sqrt{\log a}}\right).
\]
The conductor equality \(c(S_a)=3a\) holds for all but \(O(X/\sqrt{\log X})\) integer parameters \(2\le a\le X\). Thus it holds on a density-one set of parameters, not merely along a subsequence.

## Assumptions and scope
All generators and coefficients are nonnegative integers. The generator with \(j=0\) is \(a\), and \(a+1\) is a generator, so \(S_a\) is cofinite and has multiplicity \(a\). A triangular number includes \(T_0=0\) when used in additive representations; for a positive residue the one-triangular condition necessarily has \(j\ge1\). The genus counts nonnegative gaps; the conductor is the least integer after which there are no gaps. The asymptotic conclusions use the classical Gauss three-triangular-number theorem and the Landau–Ramanujan upper bound for sums of two squares.

## Proof
Define \(\lambda(n)\) to be the fewest positive triangular numbers summing to \(n\), for \(n\ge1\), and set \(\lambda(0)=0\). Gauss's three-triangular-number theorem gives \(1\le\lambda(n)\le3\) for every \(n\ge1\). A representation by \(q\ge1\) generators \(a+T_j\) has total value \(qa+N\), where \(N\) is a sum of at most \(q\) positive triangular numbers (padding with \(T_0\) if needed). Conversely, any representation of \(N\) by \(\lambda(N)\) positive triangular numbers yields an element \(a\lambda(N)+N\) of the semigroup, and extra copies of \(a\) are allowed.

For \(1\le r<a\), write \(N=r+\ell a\), where \(\ell\ge0\). This yields the **exact optimization formula**
\[
 w_a(r)=r+a\min_{\ell\ge0}\bigl(\ell+\lambda(r+\ell a)\bigr).
\]
At \(\ell=0\) the parenthesis is at most three. For \(\ell\ge2\) it is at least three, since \(r+\ell a>0\). At \(\ell=1\) it is two if \(r+a\) is triangular, and at least three otherwise. Thus the minimum is one exactly when \(r\) is triangular, two exactly when \(r\) is a sum of two triangular numbers or \(r+a\) is triangular, unless the first case applies, and three otherwise. This proves the Apéry formula. The stated genus identity follows from the standard Apéry genus identity \(g(S_a)=\sum_{r=1}^{a-1}(w_a(r)-r)/a\).

Every nonzero Apéry value is at most \(3a+r\le4a-1\). Since the conductor is \(c(S_a)=\max_{0\le r<a}w_a(r)-a+1\), it satisfies \(c(S_a)\le3a\). Equality can occur only if \(w_a(a-1)=4a-1\), equivalently \(h_a(a-1)=3\). By the layer classification, this means that \(a-1\) is not a sum of two triangular numbers and \(2a-1\) is not triangular. (The former condition already excludes one-triangular representations because \(T_0=0\).) This proves the exact criterion.

To count the shallow layers, note that there are \(O(\sqrt a)\) triangular numbers below \(2a\). If \(n=T_i+T_j\), then
\[
8n+2=(2i+1)^2+(2j+1)^2.
\]
The Landau–Ramanujan theorem implies that only \(O(a/\sqrt{\log a})\) integers \(n\le a\) can be represented as sums of two triangular numbers. It follows that
\[
B(a):=\#\{1\le r<a:h_a(r)\le2\}
=O\!\left(\frac a{\sqrt{\log a}}\right).
\]
The genus identity now gives \(g(S_a)=3(a-1)+O(B(a))=3a+O(a/\sqrt{\log a})\). For sufficiently large \(a\), the final \(B(a)+1\) residues include some \(r\) with \(h_a(r)=3\). Consequently \(\max w_a(r)\ge3a+(a-1-B(a))\), whence \(3a-B(a)\le c(S_a)\le3a\). The conductor and ratio estimates follow.

Finally, when \(c(S_a)\ne3a\), the exact criterion implies that either \(a-1\) is a sum of two triangular numbers or \(2a-1\) is triangular. Among \(2\le a\le X\), the first obstruction occurs \(O(X/\sqrt{\log X})\) times by the same two-square bound, and the second \(O(\sqrt X)\) times. Therefore the sharp conductor equality fails for at most \(O(X/\sqrt{\log X})\) parameters. All constants are independent of \(a\) and \(X\).

## Verification
The standalone `verify.py` independently computes Apéry representatives by Dijkstra's shortest-path algorithm on residues modulo \(a\), using generators of value less than \(4a\). This truncation is exact because the proof bounds every Apéry representative by \(4a-1\). The checker compares the complete Apéry vector against the three-layer formula, then checks the genus and the exact conductor criterion. It evaluates all \(2\le a\le300\) and eight additional parameters through \(a=2000\), covering 51,992 nonzero residue classes. Run `python3 verify.py`. Finite tests corroborate the proof; the density-one and asymptotic conclusions use the two cited classical theorems.

## Relationship to prior work
Komatsu's 2022 study determines generalized Frobenius invariants for **three consecutive unshifted triangular generators**. Robles-Pérez and Rosales (2017) likewise study consecutive triangular-number triples. Neto and Iglésias (2023) define a distinct family generated by all triangular numbers **above a triangular cutoff**; this is different from adding the same parameter \(a\) to every triangular number. Chomicz (2026) treats numerical semigroups generated by four consecutive square or triangular numbers, again a distinct finite-generator family. None of their accessible statements gives the exact three-layer formula or the density-one sharp conductor for the translated family above. General Apéry identities are used as tools, not claimed as new.

## Limitations
The result does not determine a second asymptotic term for the genus, or classify the exceptional parameters for which the conductor is less than \(3a\) by a finite list of congruences. The Landau–Ramanujan bound is not a sharp asymptotic for the two-triangular exceptions, and finite computations do not prove the asymptotic. The full text of the plausibly relevant Neto–Iglésias paper was unavailable during the literature comparison; its published abstract describes a different generator family, but an unindexed reduction or coincident result cannot be excluded. No independent audit has been performed.

## References
- T. Komatsu, “The Frobenius number for sequences of triangular numbers associated with number of solutions,” arXiv:2206.13054 (first public 27 June 2022), https://arxiv.org/abs/2206.13054.
- A. M. Robles-Pérez and J. C. Rosales, “The Frobenius number for sequences of triangular and tetrahedral numbers,” arXiv:1706.04378, https://arxiv.org/abs/1706.04378.
- A. M. Neto and L. Iglésias, “Triangular Numerical Semigroups,” Indian J. Pure Appl. Math. 54 (2023), 1262–1267, doi:10.1007/s13226-022-00339-1.
- K. Chomicz, “On numerical semigroups with embedding dimension four,” arXiv:2604.25653 (2026), https://arxiv.org/abs/2604.25653.
- C. F. Gauss, three-triangular-number theorem (Eureka theorem), classical result.
- E. Landau, “Über die Einteilung der positiven ganzen Zahlen in vier Klassen nach der Mindestzahl der zu ihrer additiven Zusammensetzung erforderlichen Quadrate,” Archiv Math. Phys. 13 (1908), 305–312 (Landau–Ramanujan theorem).
