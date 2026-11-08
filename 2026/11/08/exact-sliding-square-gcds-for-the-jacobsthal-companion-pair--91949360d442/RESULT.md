# Exact sliding-square GCDs for the Jacobsthal companion pair

## Finding

Let \(J_0=0\), \(J_1=1\), \(L_0=2\), \(L_1=1\), and let each sequence obey \(X_{n+2}=X_{n+1}+2X_n\). For every integer \(k\ge1\) define

\[
G_J(k)=\gcd_{n\ge1}\sum_{i=0}^{k-1}J_{n+i}^2,\qquad
G_L(k)=\gcd_{n\ge1}\sum_{i=0}^{k-1}L_{n+i}^2.
\]

Put \(g(k)=\gcd\bigl(k,2^k-(-1)^k\bigr)\) and \(e(k)=2^{\min\{\nu_2(k),3\}}\). Then, with the denominator equal to \(3\) exactly when \(3\mid k\),

\[
\boxed{G_J(k)=\frac{e(k)g(k)}{3^{\mathbf 1_{3\mid k}}},\qquad G_L(k)=e(k)g(k).}
\]

In particular, their ratio is exactly \(3\) for lengths divisible by \(3\), and \(1\) for all other lengths; both have \(2\)-adic valuation \(\min\{\nu_2(k),3\}\). The statement classifies the complete GCD, not only selected local factors.

## Assumptions and scope

All indices, lengths, and gcds concern ordinary integers. The gcd is the **positive** common divisor of all indicated sums, each sum using \(k\) consecutive squared terms and starting at any integer \(n\ge1\). The function \(\nu_p\) denotes the usual prime-adic valuation of a nonzero integer. No probabilistic hypothesis or computational cutoff is assumed. These are the standard Jacobsthal and Jacobsthal–Lucas companion sequences, respectively; for them

\[
J_n=\frac{2^n-(-1)^n}{3},\qquad L_n=2^n+(-1)^n.
\]

## Proof

**1. Three windows suffice.** Set
\[
C=(-2)^k,\qquad A=\frac{4^k-1}{3},\qquad B=\frac{1-C}{3}.
\]
These are integers and \(A=-B(C+1)\). Geometric sums give, for each \(n\ge1\),
\[
9\sum_{i=0}^{k-1}J_{n+i}^2=A4^n-2B(-2)^n+k,
\]
\[
\sum_{i=0}^{k-1}L_{n+i}^2=A4^n+2B(-2)^n+k.
\]
Both integer sequences of window sums obey the monic recurrence with characteristic polynomial
\[
(T-4)(T+2)(T-1)=T^3-3T^2-6T+8.
\]
Thus every subsequent window sum is an integer linear combination of the first three, and each infinite gcd is the gcd of its windows starting at \(n=1,2,3\).

**2. Every prime \(p\ge5\).** The matrix of the three vectors \((4^n,(-2)^n,1)\) for \(n=1,2,3\) is a Vandermonde matrix with determinant of absolute value \(432=2^4\cdot3^3\). This is a unit over \(\mathbb Z_p\) for \(p\ge5\). Multiplying by the unit \(9\) does not alter valuations at such a prime. Consequently, for both companion sequences,
\[
\nu_p(G_X(k))=\min\{\nu_p(A),\nu_p(B),\nu_p(k)\}.
\]
Since \(A=-B(C+1)\), the minimum is \(\min\{\nu_p(B),\nu_p(k)\}=\nu_p(g(k))\), as division by \(3\) changes no such valuation.

**3. Prime \(2\).** For every \(n\ge1\), both \(J_n\) and \(L_n\) are odd, so each squared term is \(1\pmod8\). Every length-\(k\) window is therefore \(k\pmod8\), giving the exact valuation \(\nu_2(k)\) if \(8\nmid k\), and divisibility by \(8\) otherwise. If \(8\mid k\), the Jacobsthal squares are \(1\pmod{16}\) at indices \(1,2\) and \(9\pmod{16}\) at every index \(\ge3\). Hence the windows starting at \(1,2\) have residues \(k\) and \(k-8\pmod{16}\); one is \(8\pmod{16}\). For the companion squares the residues are \(1,9,1,1,\ldots\pmod{16}\); windows starting at \(1,3\) have residues \(k+8,k\pmod{16}\); again one has exact valuation \(3\). This proves \(\nu_2(G_X(k))=\min\{\nu_2(k),3\}\) for both sequences. Since \(2^k-(-1)^k\) is odd, \(g(k)\) is odd.

**4. Prime \(3\).** When \(3\nmid k\), all companion squares are \(1\pmod3\), so their sums are \(k\not\equiv0\pmod3\). For Jacobsthal terms, the recurrence modulo \(3\) gives \(J_n^2\equiv0\pmod3\) exactly when \(3\mid n\), and \(J_n^2\equiv1\pmod3\) otherwise. Since a difference of adjacent windows is \(J_{n+k}^2-J_n^2\), a nonzero difference modulo \(3\) occurs at \(n=2\) if \(k\equiv1\pmod3\) and \(n=1\) if \(k\equiv2\pmod3\); hence \(\nu_3(G_J(k))=0\).

Now let \(3\mid k\), and write \(t=\nu_3(k)\ge1\), \(m=k/3\). The binomial expansion of \(C=(-8)^m=(1-9)^m\) gives
\[
C\equiv1-3k\pmod{3^{t+3}},\qquad B\equiv k\pmod{3^{t+2}},\qquad \nu_3(B)=t.
\]
Indeed each term \(9^j\binom mj\), \(j\ge2\), has valuation at least \(2j+\nu_3(m)-\nu_3(j)\ge t+3\). For the companion, using \(A=-B(C+1)\),
\[
\sum_{i=0}^{k-1}L_{n+i}^2=k+B\{2(-2)^n-(C+1)4^n\}.
\]
The bracket is divisible by \(3\), so each such sum is congruent to \(k\pmod{3^{t+1}}\), of valuation exactly \(t\).

For Jacobsthal, \(9S^J_n=k-B\{(C+1)4^n+2(-2)^n\}\). Modulo \(3^{t+2}\), we may replace \(C+1\) by \(2\), since \(\nu_3(B(C-1))\ge2t+1\ge t+2\). Furthermore \(4^n+(-2)^n\equiv2\pmod9\), because \(4=1+3\) and \(-2=1-3\). Therefore
\[
9S^J_n\equiv k-4B\equiv-3k\pmod{3^{t+2}}.
\]
Its valuation is \(t+1\), and thus \(\nu_3(S^J_n)=t-1\) for every window. Finally \(\nu_3(g(k))=t\): the above congruence implies \(\nu_3(1-C)=t+1\), whereas \(\nu_3(k)=t\). Hence the claimed factor of \(3\) distinguishes the two sequences. Combining all prime valuations finishes the proof. \(\square\)

## Verification

Run `python3 verify.py` from the folder containing this document. It constructs both sequences by exact recurrence, takes each length \(1\le k\le700\), directly computes the gcd of \(12\) shifted windows starting with \(n=1\), and compares with both closed formulas. Its saved output is `verification_output.txt`. The finite checker corroborates arithmetic and indexing but is not substituted for the preceding infinite proof. No external libraries or data are required.

## Relationship to prior work

Čerin's 2007 paper gives identities for sums of even-index and odd-index Jacobsthal squares. Soykan's 2020 preprint treats formulas for square sums across generalized Fibonacci families. Mbirika and Spilker's 2022 paper asks for and studies GCDs of sliding squares for Fibonacci-recurrence sequences, while Mbirika, Schrader, and Spilker's 2023 paper studies sliding-GCDs of Pell and balancing families. Neither recurrence is \(X_{n+2}=X_{n+1}+2X_n\), so the exact Jacobsthal companion formula above is not a specialization of their stated sliding-GCD results. The arithmetic expression \(\gcd(k,2^k-(-1)^k)\) itself is elementary; the asserted new statement is its exact role as the complete sliding-GCD for both companion sequences, including the distinct \(3\)-adic correction and the saturated \(2\)-part.

## Limitations

No independent mathematical audit has been performed. The result is restricted to standard Jacobsthal and Jacobsthal–Lucas sequences, exponent two, and positive starting indices; it does not give a general theorem for arbitrary Lucas recurrences or higher powers. A 2023 project publicly listed as concerning GCDs of sums and sums of squares of consecutive Jacobsthal numbers has no located mathematical report or theorem available for statement comparison. A potentially overlapping unpublished result from that project is the most important residual originality risk; no priority or exclusivity is asserted.

## References

- Z. Čerin, “Sums of Squares and Products of Jacobsthal Numbers,” *Journal of Integer Sequences* 10 (2007), Article 07.2.5. https://cs.uwaterloo.ca/journals/JIS/VOL10/Cerin/cerin45.pdf
- Y. Soykan, “Closed Formulas for the Sums of Squares of Generalized Fibonacci Numbers,” public preprint, 24 February 2020. https://www.preprints.org/manuscript/202002.0352
- A. Mbirika and P. Spilker, “GCD of sums of k consecutive squares of generalized Fibonacci numbers,” arXiv:2204.12626 (first posted 26 April 2022). https://arxiv.org/abs/2204.12626
- A. Mbirika, J. Schrader, and P. Spilker, “Pell and Associated Pell Braid Sequences as GCDs of Sums of k Consecutive Pell, Balancing, and Related Numbers,” arXiv:2301.05758 (first posted 13 January 2023). https://arxiv.org/abs/2301.05758
