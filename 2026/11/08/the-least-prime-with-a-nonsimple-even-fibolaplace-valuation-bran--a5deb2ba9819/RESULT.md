# The least prime with a nonsimple even FiboLaplace valuation branch is \(971\)

## Finding

Let \(e_1=e_2=1\), and, for every integer \(n\ge3\), let
\[
e_n=(n-1)e_{n-1}-e_{n-2}+1-(-1)^n.
\]
For each odd prime \(p\), define the polynomial over \(\mathbb F_p\)
\[
\mathcal P_p(X)=1+\sum_{k=1}^{p-1}\prod_{j=1}^{k}(X^2-j^2).
\]
An *even internal valuation branch* \(T_p(2a)\), for \(1\le a<p\), is a branch rooted at the residue class of indices \(2a\pmod{2p}\), when \(p\mid e_{2a}\). Following Givens--Moll, a branch is *simple* when every level has exactly one nonterminal vertex; a terminal root is not simple.

**Theorem.** Every even internal branch for every odd prime \(p<971\) is simple. The least odd prime with a nonsimple even internal branch is \(p=971\). At this prime the complete set of even internal roots is \(\{388,1554\}\), and both branches are terminal. Equivalently, the only nonzero repeated roots of \(\mathcal P_{971}\) are \(194,777\), each of exact multiplicity two.

More precisely, among all \(163\) odd primes through \(971\), there are \(144\) nonzero polynomial roots counted as distinct field elements, of which \(142\) occur for primes below \(971\); **none** of those \(142\) is repeated. A complete prime-by-prime table is supplied in `data/roots_by_prime.csv`.

## Assumptions and scope

All sums and products defining \(\mathcal P_p\) are evaluated in the finite field \(\mathbb F_p\), and a *nonzero root* means \(a\in\{1,\ldots,p-1\}\). No assertion is made about odd internal branches, the distinguished residue \(0\pmod p\), or primes greater than \(971\). There is no probabilistic extrapolation from the finite census.

The link between \(\mathcal P_p\) and the valuation tree is the identity \(e_{2a}=a\mathcal P_p(a)\) for \(1\le a<p\), and the simple-root sufficiency theorem proved in Flórez--Higuita-Diaz--Ramírez, Theorem 4.3. Its Proposition 3.1 characterizes terminality when the initial valuation equals one and the derivative is zero.

## Proof

**1. Exact finite-field evaluation.** Write \(U_0=1\), \(D_0=0\), \(H_0=0\), and for each \(1\le k<p\) put \(f_k=a^2-k^2\) and update
\[
\begin{aligned}
U_k&=U_{k-1}f_k,\\
D_k&=D_{k-1}f_k+2aU_{k-1},\\
H_k&=H_{k-1}f_k+4aD_{k-1}+2U_{k-1}.
\end{aligned}
\]
These are, respectively, the value, first derivative, and second derivative of \(\prod_{j=1}^{k}(X^2-j^2)\) at \(X=a\). Thus summing \(1+\sum U_k\), \(\sum D_k\), and \(\sum H_k\) gives \(\mathcal P_p(a)\), \(\mathcal P_p'(a)\), and \(\mathcal P_p''(a)\) modulo \(p\), exactly.

**2. Exhaustive certificate.** `scripts/census.cpp` performs an ordinary sieve through \(971\), then evaluates this recurrence for **every** odd prime \(3\le p\le971\) and **every** nonzero residue \(a\in\mathbb F_p\), with no sampling or pruning. All intermediate values are reduced modulo \(p\). There are exactly \(163\) primes, and the code executes \(45,304,276\) product steps. It finds exactly \(144\) roots, including \(142\) at smaller primes, with \(\mathcal P_p'(a)\neq0\) at every smaller-prime root. For \(p=971\) its only roots are \(a=194,777\), both satisfying
\[
\mathcal P_{971}(a)=\mathcal P_{971}'(a)=0,\qquad
\mathcal P_{971}''(a)\equiv471\not\equiv0\pmod{971}.
\]
Since \(971\) is odd, the nonzero second derivative proves both roots have multiplicity exactly two. A second implementation, `scripts/independent_census.py`, derives and evaluates a logarithmic-derivative recurrence on the half-domain \(1\le a\le(p-1)/2\), using reflection to recover the other half. It independently reproduces all root and multiplicity counts and generates the attached CSV.

**3. Consequence below the bound.** Since \(e_{2a}=a\mathcal P_p(a)\) and \(p\nmid a\), the nonzero roots are exactly the even internal valuation roots. For every \(p<971\), the census proves all such roots simple. Theorem 4.3 of the cited 2026 paper then proves all corresponding valuation branches simple, at *all* levels, not merely at the first few levels.

**4. Sharpness.** Independently iterating the recurrence for \(e_n\) modulo \(971^2=942841\) gives
\[
e_{388}\equiv473848=971\cdot488\pmod{971^2},\qquad
e_{1554}\equiv468993=971\cdot483\pmod{971^2}.
\]
Hence both initial valuations are exactly one. Their polynomial derivatives vanish modulo \(971\), and by Theorem 4.2 and Proposition 3.1 of the cited 2026 paper each branch root is terminal. The first of these residues was already exhibited there; the novelty claimed here is the sharp least-prime cutoff and its complete below-cutoff census. This completes the theorem.

## Verification

From the same directory as the extracted files, execute `g++ -std=c++17 -O2 -Wall -Wextra scripts/census.cpp -o census && ./census` and `python3 scripts/independent_census.py --table data/reproduced_roots.csv`. The generated `data/reproduced_roots.csv` must match the supplied `data/roots_by_prime.csv` byte-for-byte. Both programs are self-contained and require no downloaded mathematical packages. The C++ program also verifies the second derivatives and the two \(p^2\)-residues of \(e_n\).

The certificate proves a *finite* claim because every possible prime and residue within the bound is covered. The infinite-depth conclusion for simple branches invokes the published lifting theorem explicitly; it is not inferred from a bounded simulation.

## Relationship to prior work

Givens and Moll (2020) formulate the even-branch simplicity question and give numerical data for small primes, but no least counterexample. Flórez, Higuita-Diaz, and Ramírez (2026) disprove universal simplicity by their example \(p=971\), and establish the polynomial derivative criterion that permits the exhaustive first-obstruction proof. The present finding does **not** claim invention of the polynomial criterion, discovery of the first terminal root \(388\), or the general simple-root lifting theorem; it establishes that no smaller odd prime gives a nonsimple even internal branch, and certifies the exact boundary root profile.

The finite bound is motivated by the published counterexample, not by an arbitrary cutoff. Existing computational searches might have checked smaller primes without publishing that result; priority therefore remains subject to additional historical verification.

## Limitations

The exact arithmetic implementations must themselves be inspected for complete domain coverage and correct modular calculations; agreement between two implementations is supporting evidence, not external certification. The result is a finite least-prime statement, not a classification above \(971\). It does not address odd-indexed branches or the distinguished even class \(2p\), and no independent mathematical audit is claimed.

## References

1. R. Flórez, R. Higuita-Diaz and J. L. Ramírez, *On \(p\)-Adic Valuation Trees Arising from Laplace Transform of Fibonacci Polynomials*, arXiv:2610.37356v1 (first posted 2026-10-27), especially Sections 3, 4.1 and Theorems 4.2--4.3. https://arxiv.org/html/2610.37356v1
2. B. Givens and V. H. Moll, *Integrals of Fibonacci Polynomials and Their Valuations*, *The Fibonacci Quarterly* **58** (2020), 261--273, especially Section 4. https://www.fq.math.ca/Papers/58-3/moll011720.pdf
