# Reflection complexity equals factor complexity for generalized Thue--Morse words modulo \(\ell\ge3\)
## Finding
For every integer \(\ell\ge3\), define
\[
\mathbf t_\ell(n)=s_2(n)\pmod{\ell},
\]
where \(s_2(n)\) is the number of \(1\)'s in the binary expansion of \(n\). Then
\[
r_{\mathbf t_\ell}(n)=\rho_{\mathbf t_\ell}(n)
\qquad\text{for every }n\ge3.
\]

More strongly, no factor of \(\mathbf t_\ell\) of length at least \(4\) has its reversal as a factor. At length \(3\), a factor can have its reversal occur only when the factor is already a palindrome.

## Assumptions and scope
The factor complexity \(\rho_{\mathbf x}(n)\) is the number of distinct length-\(n\) factors of an infinite word \(\mathbf x\). The reflection complexity \(r_{\mathbf x}(n)\) counts these factors up to identifying a word with its reversal.

The theorem concerns the standard generalized binary Thue--Morse words obtained by reducing the binary digit sum modulo \(\ell\). The case \(\ell=2\) is excluded: the ordinary Thue--Morse word has many factors whose reversals also occur, and its reflection complexity is genuinely smaller than its factor complexity at many lengths.

## Proof
Write
\[
x_n=\mathbf t_\ell(n).
\]
For \(n\ge0\), let
\[
d_n=x_{n+1}-x_n\pmod{\ell}.
\]
If \(\nu_2(n+1)\) is the exponent of \(2\) dividing \(n+1\), adding \(1\) to \(n\) changes the binary digit sum by
\[
1-\nu_2(n+1).
\]
Hence
\[
d_n\equiv1-\nu_2(n+1)\pmod{\ell}.
\]

Consider first a length-\(3\) factor
\[
x_i\,x_{i+1}\,x_{i+2}.
\]
Its difference pair is
\[
(d_i,d_{i+1}).
\]
Among the consecutive integers \(i+1,i+2\), one is odd, so at least one coordinate of this pair is \(1\). If the reversed factor also occurs, then its difference pair
\[
(-d_{i+1},-d_i)
\]
must likewise have a coordinate equal to \(1\). Therefore the original pair has one coordinate equal to \(1\) and one coordinate equal to \(-1\). Since \(\ell\ge3\), these residues are distinct, so the pair is either
\[
(1,-1)\quad\text{or}\quad(-1,1).
\]
In either case the first and third letters coincide. Thus every reversible length-\(3\) factor is a palindrome, and no two distinct length-\(3\) factors are identified by reflection.

Now consider a length-\(4\) factor. Its difference triple is
\[
(d_i,d_{i+1},d_{i+2}).
\]
There are two parity cases.

If \(i+2\) is even, then both \(i+1\) and \(i+3\) are odd. Hence
\[
(d_i,d_{i+1},d_{i+2})=(1,a,1)
\]
for some residue \(a\).

If \(i+2\) is odd, then \(d_{i+1}=1\). The integers \(i+1\) and \(i+3\) are consecutive even integers after division by \(2\), so exactly one of them has \(2\)-adic valuation \(1\). Consequently one of the outer differences is \(0\), and the triple has the form
\[
(a,1,b)
\]
with \(a=0\) or \(b=0\).

Reversal sends a difference triple
\[
(a,b,c)
\]
to
\[
(-c,-b,-a).
\]
For a triple of the first type \((1,a,1)\), the reversed triple is
\[
(-1,-a,-1).
\]
It cannot be of the first type because \(-1\ne1\), and it cannot be of the second type because neither outer entry equals \(0\).

For a triple of the second type \((a,1,b)\), with \(a=0\) or \(b=0\), the reversed triple is
\[
(-b,-1,-a).
\]
It cannot be of the second type because its middle entry is \(-1\ne1\). It cannot be of the first type either, because that would require \(a=b=-1\), contradicting \(a=0\) or \(b=0\).

Thus no length-\(4\) factor has its reversal as a factor.

Finally, suppose a factor \(w\) of length at least \(4\) and its reversal \(w^R\) both occurred. The length-\(4\) prefix of \(w\) would then have its reversal as the length-\(4\) suffix of \(w^R\), contradicting the preceding paragraph. Hence no factor of length at least \(4\) is reflected.

Therefore reflection equivalence never merges two distinct factors for \(n\ge3\), and
\[
r_{\mathbf t_\ell}(n)=\rho_{\mathbf t_\ell}(n)
\]
for every \(\ell\ge3\) and \(n\ge3\).

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier checks the exact digit-sum difference identity on \(900000\) instances for moduli \(3\) through \(20\), and checks the complete local length-\(4\) obstruction on \(899946\) consecutive positions.

As a separate factor-language stress test, it enumerates factors in long prefixes for moduli \(3\) through \(9\) and lengths through \(48\). Every observed length-\(3\) reversible factor is palindromic, and every observed factor of length at least \(4\) lacks its reversal.

For modulus \(4\), the first factor/reflection-complexity pairs are
\[
(4,4),(16,10),(28,28),(44,44),(56,56),(72,72)
\]
at lengths \(1,\ldots,6\), respectively.

The infinite theorem follows from the symbolic difference-pattern proof above, not from extrapolation of these finite tests.

## Relationship to prior work
Allouche, Campbell, Li, Shallit, and Stipulanti introduced reflection complexity and asked how their Thue--Morse results extend to standard generalizations. In their Question 62 they state that for the digit-sum word modulo \(3\),
\[
r_{\mathbf t_3}(n)=\rho_{\mathbf t_3}(n)
\]
for all \(n\ge3\), and report that a similar property appears experimentally for moduli \(\ell>4\). Their statement does not provide a proof for that infinite family and does not include the modulus-\(4\) case.

The theorem above proves the property uniformly for every \(\ell\ge3\), including the previously omitted modulus \(4\). The argument is local: a simple \(2\)-adic difference rule excludes every reflected length-\(4\) factor and thereby all longer ones.

A 2026 follow-up paper on reflection complexity resolves and discusses several other conjectures from the original article but, in the inspected discussion of open problems, does not give this generalized Thue--Morse theorem.

Targeted searches using the generalized Thue--Morse name, digit-sum modulo \(\ell\), reflection complexity, reversal factors, the modulus-\(4\) case, and the exact Question 62 formulation did not locate a published covering statement.

## Limitations
The theorem determines only that reflection and factor complexity agree from length \(3\) onward; it does not give a closed formula for the factor complexity \(\rho_{\mathbf t_\ell}(n)\).

The binary case \(\ell=2\) behaves differently and is not covered.

The result addresses the digit-sum-modulo-\(\ell\) family singled out in Question 62, not every possible generalization of the Thue--Morse sequence.

An unindexed note or unpublished proof may contain the same local obstruction.

## References
1. J.-P. Allouche, J. M. Campbell, S. Li, J. Shallit, and M. Stipulanti, “The reflection complexity of sequences over finite alphabets,” arXiv:2406.09302v1, first public version 2024-06-13; Theory of Computing Systems 69 (2025), DOI 10.1007/s00224-025-10234-x.
2. L. Dvořáková and E. Pelantová, “Reflection on the Reflection Complexity,” Theory of Computing Systems 70 (2026), DOI 10.1007/s00224-026-10278-7.
