# One bit of entropy can cost exponentially more FO description than maximum entropy
## Finding
Fix a monadic vocabulary \(\tau\) with \(k\ge 2\) predicates and let \(t=2^k\) be the number of unary types. For every \(n\) divisible by \(t\), compare two \(n\)-element \(\tau\)-structures. Let \(U_{k,n}\) realize every unary type exactly \(n/t\) times, and let \(B_{k,n}\) realize exactly two unary types, each exactly \(n/2\) times.

Then \(U_{k,n}\) has the maximum possible Shannon entropy \(k\) bits, whereas \(B_{k,n}\) has Shannon entropy exactly \(1\) bit. Nevertheless, for each fixed \(k\), as \(n\to\infty\) through multiples of \(2^k\), their first-order description complexities satisfy
\[
C(U_{k,n})=\frac{{3n}}{{2^k}}+O_k(1),\qquad
C(B_{k,n})=\frac{{3n}}{{2}}+O_k(1),
\]
and therefore
\[
\frac{{C(B_{k,n})}}{{C(U_{k,n})}}\longrightarrow 2^{{k-1}}.
\]
Thus a one-bit-entropy unary structure can require an asymptotically exponentially longer shortest FO description, as a function of vocabulary size, than a same-size structure of maximum entropy.
## Assumptions and scope
Description complexity is the formula-size notion of Jaakkola, Kuusisto, and Vilander: a sentence defines a model among structures of the same finite size and vocabulary, and formula size counts atomic formulas, binary connectives, and quantifiers. The asymptotic is taken with \(k\) fixed and \(n\to\infty\) through multiples of \(2^k\). The statement does not claim a uniform two-parameter asymptotic when \(k\) grows with \(n\).
## Proof
Jaakkola, Kuusisto, and Vilander prove the following for a model whose realized unary-type multiplicities are ordered increasingly, with largest multiplicity \(m_\ell\) and second-largest multiplicity \(m_{{\ell-1}}\):
\[
3m_{{\ell-1}}-3\le C(M)\le \min\bigl(3m_\ell+c_\tau,\,6m_{{\ell-1}}+c_\tau\bigr),
\]
where \(c_\tau=15k2^k\) depends only on the fixed vocabulary.

For \(U_{k,n}\), all \(t=2^k\) multiplicities equal \(n/t\), so the displayed inequalities give
\[
\frac{{3n}}{{2^k}}-3\le C(U_{k,n})\le \frac{{3n}}{{2^k}}+c_\tau.
\]
For \(B_{k,n}\), the two realized types both have multiplicity \(n/2\), giving
\[
\frac{{3n}}{{2}}-3\le C(B_{k,n})\le \frac{{3n}}{{2}}+c_\tau.
\]
Dividing by \(n\) and sending \(n\) to infinity yields the two normalized limits, and their quotient is \(2^{k-1}\).

The entropy calculation is immediate from the type distributions. The distribution for \(U_{k,n}\) is uniform on \(2^k\) points, hence has entropy \(\log_2(2^k)=k\). The distribution for \(B_{k,n}\) is uniform on two points, hence has entropy \(1\).
## Verification
The bundled `verify.py` specializes the published upper and lower bounds for \(k=2,\ldots,10\), checks the two entropy values, checks the exact leading coefficients and limiting factor \(2^{k-1}\), and verifies that the finite-\(n\) ratio is squeezed around that limit for large multiples of \(2^k\). It returns `VERIFY_OK 72 exact assertions`.
## Relationship to prior work
Jaakkola, Kuusisto, and Vilander explicitly observe that, unlike in their earlier modal setting, maximum entropy need not correspond to maximum FO description complexity for unary structures. They also prove the sharp-in-leading-order upper and lower bounds used here. The present finding extracts an explicit comparison family and quantifies the inversion: maximum entropy \(k\) bits versus one bit of entropy, with an asymptotic description-length ratio exactly \(2^{k-1}\). The checked paper and targeted searches did not state this exponential ratio.
## Limitations
This is a short corollary of published formula-size bounds, not a new lower-bound technique. Its originality is therefore quantitative rather than structural, and an uncatalogued folklore derivation remains possible. The constants hidden in \(O_k(1)\) grow with \(k\), so the result should not be read as a joint asymptotic for growing vocabularies.
## References
1. Reijo Jaakkola, Antti Kuusisto, Miikka Vilander, *Description Complexity of Unary Structures in First-Order Logic with Links to Entropy*, arXiv:2406.02108, first submitted 2024-06-04; published in CSL 2025, DOI:10.4230/LIPIcs.CSL.2025.17. The published version gives the upper bound in Theorem 1, the lower bound in Theorem 8, and the entropy discussion in Section 6.
2. Reijo Jaakkola, Antti Kuusisto, Miikka Vilander, *Relating Description Complexity to Entropy*, STACS 2023, DOI:10.4230/LIPIcs.STACS.2023.38.
