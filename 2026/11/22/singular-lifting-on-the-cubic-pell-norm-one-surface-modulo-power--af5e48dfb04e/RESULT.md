# Singular lifting on the cubic Pell norm-one surface modulo powers of three

## Finding

Define the integral cubic polynomial
\[
F(x,y,z)=x^{3}+y^{3}+z^{3}-3xyz
\]
and, for each integer \(k\ge1\), let \(X_k\) be the set of all ordered triples in \((\mathbb Z/3^k\mathbb Z)^3\) satisfying \(F(x,y,z)\equiv1\pmod{3^k}\). Then
\[
\#X_k=3^{2k}\qquad(k\ge1).
\]
For every \(k\ge2\), exactly three of the nine solutions modulo three occur as reductions of points of \(X_k\):
\[
(1,0,0),\quad(0,1,0),\quad(0,0,1).
\]
Each of these three classes supports exactly \(3^{2k-1}\) points of \(X_k\), and none of the other six modulo-three classes supports a point at level \(k\ge2\).

More strongly, at **every** depth \(k\ge1\), the reduction map \(X_{k+1}\to X_k\) has an image of size \(3^{2k-1}\), and its nonempty fibers all have size \(27\). Thus exactly one third of all solutions at any given level admit a next-level lift, even though every liftable solution has all \(27\) possible coordinate-digit refinements. This persistent singular-lifting sieve is the main assertion.

## Assumptions and scope

The modulus is an *integer prime-power ring* \(\mathbb Z/3^k\mathbb Z\), not the finite field \(\mathbb F_{3^k}\). All triples are ordered and all coordinate values, including zero, are permitted. The right-hand side is exactly one, and the cubic corresponds to the norm of \(x+yt+zt^2\) in \((\mathbb Z/3^k\mathbb Z)[t]/(t^3-1)\). No nonsingularity, coprimality, or primitivity condition is imposed.

## Proof

**1. The first two levels.** Put \(s=x+y+z\) and \(t=xy+yz+zx\). The exact identity
\[
F=s^3-3st
\]
shows that \(F\equiv1\pmod3\) is equivalent to \(s\equiv1\pmod3\). Hence \(\#X_1=3^2=9\). When \(s\equiv1\pmod3\), one has \(s^3\equiv1\pmod9\). Consequently \(F\equiv1\pmod9\) requires and is equivalent to \(t\equiv0\pmod3\).

Modulo three, \(x^2+y^2+z^2=s^2-2t\equiv1\). Because the square of a residue is zero or one, exactly one of \(x,y,z\) is nonzero (the number of nonzero coordinates lies between zero and three and is congruent to one modulo three). Its value is one because \(s\equiv1\). Thus the three and only three liftable classes from level one are the three unit-coordinate triples displayed above.

**2. Complete count within one surviving class.** By permutation symmetry it is enough to fix the reduction class \((1,0,0)\). For \(k\ge2\), write uniquely
\[
x=1+3a,\qquad y=3b,\qquad z=3c,
\]
where \(a,b,c\) range independently modulo \(3^{k-1}\). Direct expansion gives the exact integer identity
\[
F(1+3a,3b,3c)-1=9H(a,b,c),
\]
where
\[
H(a,b,c)=a+3\bigl(a^2+a^3+b^3+c^3-bc-3abc\bigr).
\]
The level-\(k\) equation is therefore \(H(a,b,c)\equiv0\pmod{3^{k-2}}\), interpreted as a vacuous condition when \(k=2\). For each fixed \(b,c\), the polynomial in \(a\) obeys
\[
H(a,b,c)\equiv a\pmod3,
\qquad \frac{\partial H}{\partial a}\equiv1\pmod3.
\]
The ordinary one-variable Hensel lemma now gives exactly one solution \(a\) modulo \(3^{k-2}\) for each pair \(b,c\) (the same statement is tautological for modulus one). It has precisely three extensions modulo \(3^{k-1}\). There are \(3^{2(k-1)}\) pairs \((b,c)\), so this class contains exactly \(3\cdot3^{2(k-1)}=3^{2k-1}\) solutions. Each of the three surviving reduction classes has this size, proving \(\#X_k=3^{2k}\) for \(k\ge2\); the formula for \(k=1\) was already established.

**3. Every-level projection sieve.** All three partial derivatives of \(F\) are divisible by three as integer polynomials. For \(k\ge1\), replacing a representative triple by its translate \(3^k(u,v,w)\), with \(u,v,w\in\{0,1,2\}\), leaves its \(F\)-value unchanged modulo \(3^{k+1}\). The Taylor linear terms are multiples of \(3^{k+1}\), and all higher terms are multiples of \(3^{2k}\), which is divisible by \(3^{k+1}\). Hence each fiber of reduction \(X_{k+1}\to X_k\) has either zero or all \(27\) possible lifts. Comparing the already proved cardinalities gives
\[
\#\operatorname{im}(X_{k+1}\to X_k)
=\frac{3^{2(k+1)}}{27}=3^{2k-1}.
\]
Because \(\#X_k=3^{2k}\), the liftable fraction is exactly one third at every depth. This also supplies an exact characterization of every-level lifting by the congruence on \(H\) in step 2.

## Verification

The accompanying standalone \(\texttt{local\_checker.py}\) directly enumerates the **original cubic congruence** at 18 prime-power moduli (including \(3,9,27,81\)), compares counts with the predicted local formulas, and counts the modulo-three reduction fibers. It also independently enumerates solutions at levels \(3,9,27\) and tests which reduce to solutions at the next level, confirming the three expected liftable fractions. Execute with \(\texttt{python3 local\_checker.py}\); the saved \(\texttt{local\_checker\_output.json}\) records the passed cases. These computations corroborate finite instances only. The preceding algebraic argument, not the finite sample, proves the statements for every \(k\ge1\).

## Relationship to prior work

Dutto and Murru (first public 10 March 2022) analyze norm-one cubic Pell equations **over finite fields**. Their finite-field calculations include characteristic three and identify the relevant norm-algebra structure, but \(\mathbb F_{3^k}\) is not \(\mathbb Z/3^k\mathbb Z\), and those point counts do not determine which mod-three triples lift through the integer prime-power tower.

Seck and Nitaj (first public 1 March 2024) prove prime-power point-count formulas for the same cubic Pell family under the explicit hypothesis \(p\equiv1\pmod3\). In the cubic-residue case their known formula is \(p^{2(k-1)}(p-1)^2\). This is **not** being claimed as new. Their hypothesis excludes \(p=3\), where the gradient vanishes identically modulo three and the smooth-lifting proof is unavailable. Nitaj and Seck (2024) also construct encoding functions for squarefree products of primes congruent to two modulo three and prime powers with primes congruent to one modulo three, without treating three as a prime divisor. Shevelev (2015) studies representations of *positive integers* by this same cubic polynomial under ordering constraints; its theorem does not enumerate ordered residue-ring solutions. Murru and Saettone (2018) study a field-based cubic construction requiring a noncube parameter; the current parameter is one. The specific non-étale, characteristic-three liftable-class distribution above is not implied by these inspected statements.

## Limitations

The theorem concerns the fixed parameter \(r=1\), target norm one, and the prime three only. It does not classify arbitrary targets, other ramified parameters, or the abstract isomorphism type of the finite norm-one groups. Standard results on norm maps for ramified finite algebras could contain an implicit equivalent; no claim of exhaustive literature coverage or independent mathematical certification is made. The verification script is finite evidence, not an infinite proof.

## References

- S. Dutto and N. Murru, *On the cubic Pell equation over finite fields*, arXiv:2203.05290, first made public 10 March 2022, especially Section 5, <https://arxiv.org/html/2203.05290v1>.
- M. Seck and A. Nitaj, *A New Public Key Cryptosystem Based on the Cubic Pell Curve*, IACR ePrint 2024/385, first received 1 March 2024, especially Section 3 and Lemma 3, <https://eprint.iacr.org/2024/385>.
- V. Shevelev, *Representation of positive integers by the form* \(x^3+y^3+z^3-3xyz\), arXiv:1508.05748, first made public 24 August 2015, <https://arxiv.org/html/1508.05748v2>.
- A. Nitaj and M. Seck, *A New Public Key Encryption Scheme Based on the Cubic Pell Curve Using Encoding Functions*, received 20 October 2024, Sections 1–3, <https://ced.fst-usmba.ac.ma/p/mjaga/wp-content/uploads/2024/12/NitajSeck_MJAGA-2.pdf>.
- N. Murru and F. M. Saettone, *A novel RSA-like cryptosystem based on a generalization of the Rédei rational functions*, NuTMiC 2017 revised proceedings (2018), Section 2, <https://doi.org/10.1007/978-3-319-76620-1_6>.
