# The first nontrivial squarefull gcd of neighboring cyclotomic values occurs at index \(29\)

## Finding
For each positive integer \(m\), let \(\Phi_m\) be the monic cyclotomic polynomial and set
\[
G_m(n)=\gcd(|\Phi_m(n)|,|\Phi_m(n+1)|),\qquad n\in\mathbb Z.
\]
Every \(G_m(n)\) is squarefree for \(1\le m\le28\), but
\[
G_{29}(298)=3481=59^2.
\]
Thus \(29\) is both the least index admitting a nonsquarefree gcd of consecutive values and the least index admitting a **nontrivial squarefull** such gcd.

## Assumptions and scope
The argument \(n\) ranges over all integers, including negatives. Squarefree means that no prime square divides the positive integer in question; a nontrivial squarefull gcd is a gcd greater than one in which every prime divisor has exponent at least two. The gcd is positive because simultaneous vanishing is impossible (as shown below). The result concerns the least index, not the least argument or a classification of arguments at index \(29\).

## Proof
Fix \(m\) and put \(f(X)=\Phi_m(X)\), \(g(X)=f(X+1)\) and \(R_m=|\operatorname{Res}_X(f,g)|\). If \(z\) and \(z+1\) both lie on the unit circle, then \(z=-1/2\pm i\sqrt3/2\) is primitive of order three and \(z+1\) primitive of order six. Thus \(f\) and \(g\) have no common complex root and \(R_m\ne0\). The integer resultant identity expresses the signed resultant as a \(\mathbb Z[X]\)-linear combination of \(f\) and \(g\) (equivalently, use the adjugate of the Sylvester matrix). Evaluating at \(n\) shows that \(G_m(n)\mid R_m\).

If a prime square \(p^2\) divides \(G_m(n)\), then \(p\mid R_m\) and \(a=n\bmod p\) is a simultaneous root of \(f\) and \(g\) modulo \(p\). With \(0\le a<p\), every candidate lift modulo \(p^2\) is represented by \(a+pt\), \(0\le t<p\). Taylor expansion modulo \(p^2\) shows that the lift is simultaneous precisely if
\[
 f(a)/p+t f'(a)\equiv g(a)/p+t g'(a)\equiv 0\pmod p.
\]
The quotients are integers, and the test includes zero derivatives. The factorizations in `certificate.json` are checked for primality and completeness against the integer resultants, so they exclude every other prime. The checker verifies all 97 index–prime entries, checks all common-root residues (178 in total), and exhausts the possible \(t\) at each such residue. There is no simultaneous lift for \(m\le28\). Since the modulus reductions cover all integer arguments, this proves the uniform squarefree assertion.

At the prime index \(29\), \(\Phi_{29}(X)=1+X+\cdots+X^{28}\). Exact evaluation of the two integer values and the Euclidean gcd give
\[
\gcd\!\left(\frac{298^{29}-1}{297},\frac{299^{29}-1}{298}\right)=3481.
\]
This calculation, verified in `checker.py`, gives the **whole gcd**, not just the existence of a square divisor. Since \(59\) is prime, the witness is nontrivial squarefull. Below index \(29\) a squarefree gcd cannot be nontrivial squarefull, proving both least-index statements.

## Verification
Run `python3 checker.py` with Python 3 and SymPy, with the unchanged `certificate.json` in the working directory. The checker verifies both the complete lower-index exclusion by exact integer and modular arithmetic and the exact gcd at \(m=29,n=298\). It prints the common-root count and the gcd, not a search bound on \(n\).

## Relationship to prior work
Known formulas for resultants and identities of cyclotomic polynomials at related indices do not directly give the simultaneous prime-square lifts for neighboring evaluations. De Nápoli's Theorem 1.1 relates index products at a composed argument. Sanna and Szikszai study coprimality within long blocks of polynomial values, not the squarefreeness of every adjacent pair for consecutive cyclotomic indices. Exact adjacent-gcd profiles for the three quadratic and the four degree-six cyclotomic polynomials cover some lower indices; they do not determine the uniform cutoff through index \(28\) or the index-\(29\) gcd. No equivalent cutoff was found in the sources compared; unlocated equivalent results remain possible.

## Limitations
The exhaustive step is over a finite set of prime-square residues under an exact resultant bound, not over a bounded range of integer arguments. Neither all arguments at index \(29\), higher indices, nor the largest possible prime-power exponents are classified.

## References
1. P. L. De Nápoli, *An Identity involving the Cyclotomic Polynomials*, https://arxiv.org/html/2010.02668v2, Theorem 1.1.
2. C. Sanna and M. Szikszai, *A coprimality condition on consecutive values of polynomials*, https://arxiv.org/html/1704.01738, Theorem 1.1.
3. C. A. Cheng, J. H. McKay and S. S. Wang, *Resultants of cyclotomic polynomials*, Proc. Amer. Math. Soc. 123 (1995), 1053–1059 (historical reference for the composition identity as cited by De Nápoli).
