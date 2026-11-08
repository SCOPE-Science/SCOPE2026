# Exact additive diameter of Gaussian norm-one circles modulo powers of two

## Finding

For every integer \(k\ge 1\), put \(R_k=\mathbb Z/2^k\mathbb Z\), and define the Gaussian norm-one circle
\[
C_k=\{(a,b)\in R_k^2:a^2+b^2=1\}.
\]
For a positive integer \(h\), let \(hC_k\) denote sums of exactly \(h\) elements of \(C_k\), with repetition allowed. Let \(E_k\) and \(O_k\) be the classes of pairs with, respectively, even and odd coordinate sum modulo \(2\).

**Theorem.** For every \(k\ge1\):

1. Every pair with both coordinates odd belongs to \(2C_k\).
2. \(3C_k=O_k\) and \(4C_k=E_k\).
3. \(C_k=O_k\) precisely when \(k\le2\). When \(k\ge3\), \((2,2)\notin2C_k\).

Consequently the undirected Cayley graph on the additive group \(R_k^2\), with generating set \(C_k\), has **exact diameter**
\[
\operatorname{diam}\bigl(\operatorname{Cay}(R_k^2,C_k)\bigr)
=\begin{cases}2,&k=1,2,\\4,&k\ge3.\end{cases}
\]
All conclusions hold uniformly for the entire dyadic tower, not just for tested exponents.

## Assumptions and scope

The ring is the two-coordinate residue ring modulo \(2^k\), with \(k\) a positive integer. The Gaussian norm of \((a,b)\) is \(a^2+b^2\); a *norm-one point* satisfies its congruence to \(1\). The Cayley graph has an edge between \(u\) and \(v\) if \(v-u\in C_k\). This graph is undirected because \(-C_k=C_k\); it is connected by the theorem. The diameter means maximal **shortest-path** length; the equal-length sumsets in the theorem are additional, stronger statements.

## Proof

**Parity barrier.** Each point \((a,b)\in C_k\) satisfies \(a+b\equiv1\pmod2\), since \(a^2+b^2\equiv a+b\pmod2\). Consequently \(hC_k\subseteq O_k\) if \(h\) is odd and \(hC_k\subseteq E_k\) if \(h\) is even.

**Square-root lemma.** If an odd integer \(q\equiv1\pmod8\), then for every integer \(j\ge3\) there is an odd \(\lambda\) such that \(\lambda^2\equiv q\pmod{2^j}\). Indeed, \(\lambda=1\) works modulo \(8\). If \(\lambda\) works modulo \(2^j\), then replacing it, if necessary, by \(\lambda+2^{j-1}\) changes its square by \(2^j\lambda\pmod{2^{j+1}}\), hence flips exactly the next binary digit. This proves existence at each finite exponent; it does not assume compatible choices of the lifted roots.

**All odd–odd targets are two sums.** Fix arbitrary odd integer representatives \(u,v\), and write
\[
D=u^2+v^2=2h,\qquad h\equiv1\pmod4.
\]
The congruence for \(h\) follows from the fact that every odd square is \(1\) modulo \(8\). Since \(h\) is odd, define the odd residue
\[
q=2h^{-1}-1\pmod{2^{k+1}}.
\]
Its residue modulo \(8\) is \(1\), because \(h^{-1}\equiv1\pmod4\). By the square-root lemma, choose odd \(\lambda\) with \(\lambda^2\equiv q\pmod{2^{k+1}}\). (For \(k=1\), the same choice exists after lifting the target modulo \(8\).)

Define integer pairs
\[
Z=\left(\frac{u-\lambda v}{2},\frac{v+\lambda u}{2}\right),\qquad
W=\left(\frac{u+\lambda v}{2},\frac{v-\lambda u}{2}\right).
\]
Their coordinates are integers because \(u,v,\lambda\) are odd, and \(Z+W=(u,v)\) exactly. The two norms are equal to
\[
N(Z)=N(W)=\frac{D(1+\lambda^2)}4
=\frac{h(1+\lambda^2)}2
\equiv1\pmod{2^k},
\]
where the last congruence uses \(1+q=2h^{-1}\) modulo \(2^{k+1}\). Thus \(Z,W\) reduce to members of \(C_k\), proving \((u,v)\in2C_k\) for every odd–odd residue pair.

**Three and four sums.** Let \((s,t)\in O_k\). If \(s\) is odd and \(t\) even, subtract \((0,1)\in C_k\); otherwise subtract \((1,0)\in C_k\). The remainder has both coordinates odd, so by the previous paragraph it belongs to \(2C_k\). Hence \(O_k\subseteq3C_k\), and parity gives equality. For an even-parity target \((s,t)\), subtract \((1,0)\in C_k\); its remainder lies in \(O_k=3C_k\). Thus \(E_k\subseteq4C_k\), again with equality by parity.

**Optimality.** Modulo \(2\), and also modulo \(4\), a sum of two squares is \(1\) exactly when one coordinate is odd and the other even; hence \(C_k=O_k\) for \(k=1,2\). When \(k\ge3\), the odd-parity point \((1,2)\) is not in \(C_k\), since its norm is \(5\), not \(1\), modulo \(8\). Also, every norm-one point modulo \(8\) has exactly one odd coordinate and the other coordinate divisible by \(4\). A sum of two such points cannot be \((2,2)\pmod8\): an output coordinate congruent to \(2\) must be a sum of two odd coordinates, which would force each summand to have both coordinates odd. Thus \((2,2)\notin2C_k\) for \(k\ge3\).

The graph has diameter at most \(4\) by the three- and four-sum coverage. For \(k=1,2\), the nonzero even-parity pair \((1,1)\) requires at least two steps, so the diameter is exactly \(2\). For \(k\ge3\), the even-parity nonzero pair \((2,2)\) is not in \(2C_k\) and cannot have odd graph distance, so its shortest-path length is exactly \(4\). This establishes the diameter formula. \(\square\)

## Verification

The standalone script `verify.py` enumerates norm-one points for \(1\le k\le7\), computes their exact twofold, threefold and fourfold sumsets, checks that all odd–odd pairs occur in the double sumset, and compares the higher sumsets with the parity classes. It also independently constructs the square-root certificate for every odd–odd target through \(k=9\), checking the two norms and their exact coordinate sum. Run it with `python3 verify.py` in the directory containing this file. Successful output ends with `VERIFY_OK`. The computations check finite cases and do not replace the all-exponent proof above.

## Relationship to prior work

Grau, Oller-Marcén, Rodríguez and Sadornil, *Fermat test with Gaussian base and Gaussian pseudoprimes* (arXiv:1401.4708, first public January 19, 2014), define the Gaussian norm-one groups for modular arithmetic and determine their multiplicative structure in Section 2. Their main results concern pseudoprimes and Gaussian Carmichael numbers, not additive diameter of \(C_k\).

Covert, Demiroğlu Karabulut and Pakianathan, *Cayley Digraphs Associated to Arithmetic Groups* (arXiv:1808.06665, 2018), examine additive sums of norm-one vectors and orthogonal matrices in **finite fields of odd characteristic**. Their field results do not apply to rings \(\mathbb Z/2^k\mathbb Z\) in characteristic a power of two. Mináč, Nguyen and Tân, *Sums of Units in a Finite Ring and Applications to Cayley Graphs* (preprint dated March 21, 2026), distinguish unrestricted units from special normalized units; the examined normalized-norm results concern finite fields, not the dyadic norm-one circle here.

The present argument instead uses a square-root criterion for \(2\)-adic units and establishes a uniform, sharp four-step diameter for the dyadic family.

## Limitations

The theorem does **not** give the complete twofold sumset or its representation multiplicities; it gives the entire odd–odd portion and one sharp obstruction. No analogous claim is made for odd prime powers or general quadratic norms. A precise historical-priority assessment remains subject to older local-ring and Cayley-graph literature that may use different terminology.

## References

1. J. M. Grau, A. M. Oller-Marcén, M. Rodríguez and D. Sadornil, *Fermat test with Gaussian base and Gaussian pseudoprimes*, arXiv:1401.4708, initially public 2014-01-19, https://arxiv.org/abs/1401.4708.
2. D. Covert, Y. Demiroğlu Karabulut and J. Pakianathan, *Cayley Digraphs Associated to Arithmetic Groups*, arXiv:1808.06665 (2018), https://arxiv.org/abs/1808.06665.
3. J. Mináč, T. T. Nguyen and N. D. Tân, *Sums of Units in a Finite Ring and Applications to Cayley Graphs*, 2026 preprint, https://tungprime.github.io/articles/sums_of_units.pdf.
