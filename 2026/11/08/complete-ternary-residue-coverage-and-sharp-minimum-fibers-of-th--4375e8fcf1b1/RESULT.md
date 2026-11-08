# Complete ternary residue coverage and sharp minimum fibers of the Perrin sequence

## Finding

For the Perrin sequence \(P_0=3\), \(P_1=0\), \(P_2=2\), \(P_{n+3}=P_{n+1}+P_n\), write \(c_k(a)\) for the number of integers \(0\le n<13\cdot3^{k-1}\) with \(P_n\equiv a\pmod{3^k}\). For every \(k\ge1\), the least period modulo \(3^k\) is exactly \(13\cdot3^{k-1}\), and \(c_k(a)>0\) for every residue \(a\).

For every \(k\ge2\), the following pointwise bounds are optimal:
\[
c_k(a)\ge
\begin{cases}
3,&a\equiv0\pmod3,\\
2,&a\equiv1\pmod3,\\
4,&a\equiv2\pmod3.
\end{cases}
\]
The respective lower bounds are attained for **every** residue \(a\equiv0,1,8\pmod9\) (respectively); hence the minima over each of the three residue classes modulo three are exactly \(3,2,4\) for every exponent \(k\ge2\).

## Assumptions and scope

All indices are nonnegative integers and periods are exact periods from index zero. Every congruence is among ordinary integer residues. The theorem concerns the classical third-order Perrin recurrence, not second-order Fibonacci/Lucas sequences or arbitrary third-order recurrences. The source used to anchor the arithmetic object was first public in February 2015; the statement here is not attributed to that source.

## Proof

**(1) Étale cubic algebra and exact period.** Let \(A=\mathbb Z[t]/(t^3-t-1)\), and denote the class of \(t\) by \(\alpha\). The norm of \(\alpha\) equals one, so it is a unit. The characteristic polynomial is \(f(t)=t^3-t-1\), which has discriminant \(-23\); modulo three it takes the nonzero value \(2\) at each element of \(\mathbb F_3\), hence it is irreducible and separable. Consequently \(A/3A\) is the field of \(27\) elements. The field trace identity \(P_n=\operatorname{Tr}_{A/\mathbb Z}(\alpha^n)\) follows from the initial traces \(3,0,2\) and the relation \(\alpha^3=\alpha+1\).

Multiplying in the basis \(1,\alpha,\alpha^2\) gives the *exact identity* \(\alpha^{13}=7+12\alpha+9\alpha^2=1+3\beta\), where \(\beta=2+4\alpha+3\alpha^2\) is a unit in \(A/3A\) because its reduction \(2+\alpha\) is nonzero in the field. Thus \(\alpha\bmod3\) has order exactly \(13\): its order divides \(13\), and \(\alpha\not\equiv1\pmod3\). The binomial expansion, applied successively, yields
\[
\alpha^{13\cdot3^j}=1+3^{j+1}\beta_j,
\qquad \beta_j\equiv\beta\pmod3\quad(j\ge0).
\]
Indeed, cubing \(1+3^{j+1}\beta_j\) gives \(1+3^{j+2}\beta_j\pmod{3^{j+3}}\), while the other terms have larger valuation. Therefore \(\alpha\) has exact order \(13\cdot3^{k-1}\) modulo \(3^k\).

The trace pairing \((x,y)\mapsto\operatorname{Tr}(xy)\) on \(A\) has determinant \(-23\), a unit modulo any power of three. If the Perrin sequence has a period \(T\) modulo \(3^k\), then \(\operatorname{Tr}(\alpha^i(\alpha^T-1))=0\) for \(i=0,1,2\). Nondegeneracy of the trace pairing forces \(\alpha^T=1\pmod{3^k}\). Conversely that identity makes the sequence periodic. The least period is therefore exactly \(13\cdot3^{k-1}\).

**(2) Nine regular, four singular branches.** For \(0\le i<13\), let \(r_i=P_i\bmod3\) and \(d_i=(P_{i+13}-P_i)/3\bmod3\). The complete finite table is

| \(i\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(r_i\) | 0 | 0 | 2 | 0 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 1 | 2 |
| \(d_i\) | 0 | 2 | 1 | 2 | 0 | 0 | 2 | 0 | 2 | 2 | 2 | 1 | 1 |

The table is certified by the recurrence through index \(25\). For any integers \(u,v\ge0\), if \(u\ne v\), put \(s=\nu_3(u-v)\). Using \(\alpha^{13}=1+3\beta\) and the unit property of \(\beta\), a binomial expansion in the 3-adic algebra gives
\[
\frac{\alpha^{13(u-v)}-1}{3^{s+1}}\equiv
\frac{u-v}{3^s}\beta\pmod3.
\]
Taking traces after multiplication by \(\alpha^{i+13v}\), one obtains, whenever \(d_i\ne0\),
\[
\nu_3(P_{i+13u}-P_{i+13v})=1+\nu_3(u-v).
\]
Thus for fixed regular \(i\), the \(3^{k-1}\) values indexed by \(0\le u<3^{k-1}\) run **bijectively** over all \(3^{k-1}\) residues \(a\bmod3^k\) with \(a\equiv r_i\pmod3\). Among the regular indices, \(r_i=0\) occurs three times (\(i=1,3,9\)); \(r_i=1\) occurs twice (\(i=8,11\)); and \(r_i=2\) occurs four times (\(i=2,6,10,12\)). These yield all pointwise lower bounds and residue-completeness.

When \(d_i=0\), the expansion gives \(P_{i+13u}\equiv P_i\pmod9\) for every integer \(u\). The singular base indices are \(i=0,4,5,7\), with respective initial residues \(P_i\equiv3,2,5,7\pmod9\). Consequently, no singular branch contributes at residues \(a\equiv0\pmod9\), \(a\equiv1\pmod9\), or \(a\equiv8\pmod9\), proving the sharpness assertions at every \(k\ge2\). At \(k=1\) the frequencies are respectively \(4,3,6\), as the table also shows.

## Verification

Run the accompanying Python 3 standard-library script `verify.py`. It verifies the exact cubic-power relation, irreducibility modulo three, the thirteen branch rows, all predicted least periods through the fifth power of three, complete coverage, the conditional minima for every target in those periods, and sharpness at the specified classes modulo nine. These are **finite consistency checks**; the binomial valuation and nondegenerate trace arguments above prove the statements for all exponents.

## Relationship to prior work

Yilmaz and Taskara (2015, first arXiv version February 27) study iterated binomial transforms of Padovan/Perrin matrix sequences, including their generating functions. Their inspected full text treats transforms, not frequencies of values modulo powers of three. Jacobsen's 2016 Perrin primer explains the third-order recurrence, cubic discriminant, and applications to primality signatures, rather than exact fiber minima. OEIS A104217 already tabulates least Perrin periods for individual moduli, notably \(13,39,117\) at \(3,9,27\): the period data alone are **not asserted novel**. The present contribution is the uniform residue coverage plus sharp, persistent residue-conditioned frequency minima, explained by explicit regular and singular 3-adic branches. Work on Fibonacci/Lucas residue completeness and distributions concerns a different (second-order) characteristic polynomial and does not imply this Perrin theorem.

## Limitations

The theorem gives exact conditional *minimum* multiplicities and the complete regular-branch contribution, not a closed formula for the additional multiplicities contributed by the four singular branches at all 3-adic depths. It treats no primes other than three and does not imply any Perrin-primality testing theorem. Independent mathematical validation has not been performed. Historical priority remains uncertain outside the full texts and indexed records inspected, especially older third-order recurrence and finite-ring literature.

## References

1. N. Yilmaz and N. Taskara, *On the properties of iterated binomial transforms for the Padovan and Perrin matrix sequences*, arXiv:1502.07919v1 (2015-02-27), full-text arXiv:1502.07919v4, https://arxiv.org/abs/1502.07919 .
2. OEIS A104217, *Period of Perrin sequence mod n*, https://oeis.org/A104217 (original entry 2005).
3. D. Jacobsen, *Perrin Primality Tests*, 2016-08-08, https://ntheory.org/primality/perrin.html .
4. C. L. Lang and M. L. Lang, *Fibonacci system and residue completeness*, arXiv:1304.2892 (2013); second-order Fibonacci/Lucas results.
5. R. Bundschuh and P. Bundschuh, *Distribution of Fibonacci and Lucas Numbers Modulo Powers of Three*, Fibonacci Quarterly 49 (2011), 201–210; second-order comparison.
