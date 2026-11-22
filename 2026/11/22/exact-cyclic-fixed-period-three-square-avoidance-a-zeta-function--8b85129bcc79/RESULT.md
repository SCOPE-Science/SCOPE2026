# Exact cyclic fixed-period-three square avoidance: a zeta function and orbit census

## Finding
For each integer \(n\ge1\), let \(C_n\) be the number of **marked binary circular words** \(x_0\cdots x_{n-1}\), with indices read modulo \(n\), containing no cyclic factor \(abcabc\) of length six. The six positions may revisit the same marked positions if \(n<6\). Equivalently, no cyclic start permits an exact tandem duplication of a block of length three.

The exact Artin–Mazur generating function is
\[
\boxed{\exp\!\left(\sum_{n\ge1}\frac{C_n}{n}z^n\right)=
\frac{1}{(1-z-z^2-z^3)(1+z)(1+z^2)(1-z^3)(1+2z^3-z^6)(1+z^3+z^6-z^9)}.}
\]
The first eighteen values, beginning at \(n=1\), are
\[
0,2,0,14,20,56,70,134,216,442,814,1592,2756,5070,9080,17158,31552,58664.
\]
For all \(n\ge1\), the number of primitive (aperiodic) necklaces is exactly
\[
N_n^{\mathrm{prim}}=\frac1n\sum_{d\mid n}\mu(d)C_{n/d},
\]
while the number of all necklaces, including proper powers, is exactly
\[
N_n=\frac1n\sum_{d\mid n}\varphi(d)C_{n/d}.
\]
The growth constant is the tribonacci constant \(\rho=1.83928675521416\ldots\), the unique real root greater than one of \(\rho^3-\rho^2-\rho-1=0\). In particular \(C_n=\rho^n+O(\beta^n)\) for some \(\beta<\rho\), and \(N_n^{\mathrm{prim}}\sim\rho^n/n\).

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), and a forbidden six-letter square has **exact half-length three**: squares of different half-lengths are allowed. A circular word is counted with a fixed marked starting position, so rotations of a nonperiodic word are distinct in \(C_n\). Reflection and binary complementation are not quotiented. This is a local **cyclic** exclusion, not the ordinary linear length-\(n\) language of words avoiding six-letter squares internally. For \(n<6\) the circular condition is evaluated in the infinite periodic extension, which is essential for the stated coefficients and necklace formulas.

## Proof
Let \(x\) be a marked circular word of circumference \(n\), and define its cyclic binary difference word \(y_i=x_i\oplus x_{i+3}\). A forbidden factor at position \(i\) occurs exactly when \(y_i=y_{i+1}=y_{i+2}=0\). The linear map \(D:x\mapsto y\) on \(\mathbf F_2^n\) has kernel dimension \(g=\gcd(n,3)\): a kernel element is constant on each orbit of the shift \(i\mapsto i+3\). Its image consists exactly of the words \(y\) whose XOR sum on each such orbit is zero; necessity is telescoping, and sufficiency follows from dimension \(n-g\). Thus any admissible \(y\) with the stated parity constraints has exactly \(2^g\) inverse words \(x\).

Let \(P\) and \(Q\) be four-by-four transfer matrices indexed, in this order, by the binary pairs \(00,01,10,11\). A transition from \(ab\) to \(bc\) is present unless \(abc=000\); it has weight \(1\) in \(P\), and weight \((-1)^c\) in \(Q\). Explicitly,
\[
P=\begin{pmatrix}0&1&0&0\\0&0&1&1\\1&1&0&0\\0&0&1&1\end{pmatrix},\qquad
Q=\begin{pmatrix}0&-1&0&0\\0&0&1&-1\\1&-1&0&0\\0&0&1&-1\end{pmatrix}.
\]
The trace of a product of successive signed versions of these matrices counts cyclic \(y\) avoiding \(000\), weighted by the prescribed parity characters. There is no overcount for short circumferences: each cyclic \(y\) has exactly one compatible closed sequence of overlapping pair states with its marked start.

Apply character orthogonality to the \(g\) independent even-parity constraints. The factor \(2^g\) accounting for preimages cancels the denominator \(2^g\) in this projection. If \(3\nmid n\), the single orbit has only the positive and negative characters, giving \(C_n=\operatorname{tr}(P^n)+\operatorname{tr}(Q^n)\). If \(n=3m\), the orbit constraints are exactly the three residue classes modulo three. Of their eight characters, one is all-positive, one all-negative, three have one negative residue, and three have two. Cyclic invariance of trace under rotation of factors therefore gives
\[
C_{3m}=\operatorname{tr}(P^{3m})+\operatorname{tr}(Q^{3m})+
3\operatorname{tr}((QP^2)^m)+3\operatorname{tr}((Q^2P)^m).
\]
Writing \(R=QP^2\) and \(S=Q^2P\), the exact determinant identities are
\[
\begin{aligned}
\det(I-zP)&=1-z-z^2-z^3,\\
\det(I-zQ)&=(1+z)(1+z^2),\\
\det(I-z^3R)&=(1-z^3)(1+2z^3-z^6),\\
\det(I-z^3S)&=1+z^3+z^6-z^9.
\end{aligned}
\]
All four follow by elementary determinant expansion and are independently checked by the attached integer programs. The formal identity \(-\log\det(I-tT)=\sum_{m\ge1}\operatorname{tr}(T^m)t^m/m\) applied to the trace formulas now gives the boxed zeta function, without extrapolation from finite samples.

For primitive necklaces, the disjoint decomposition by least circular period gives \(C_n=\sum_{d\mid n}dN_d^{\mathrm{prim}}\); Möbius inversion proves the first necklace formula. The second follows from Burnside's lemma. The zeta denominator factors show a unique simple eigenvalue of largest modulus, \(\rho\); every other reciprocal root has modulus strictly smaller than \(\rho\). It follows that \(C_n=\rho^n+O(\beta^n)\) with \(\beta<\rho\). Proper powers contribute at most exponentially as \(O(2^{n/2}\operatorname{poly}(n))\), hence the primitive necklace asymptotic.

## Verification
Run `python3 checks/exact_transfer.py` and `python3 checks/parity_projection.py` using Python 3 and no external packages. The first constructs the independent 32-state five-bit overlap graph, with an edge for each allowed six-bit window, and derives its entire exact degree-32 characteristic polynomial using integer Faddeev–LeVerrier arithmetic. The characteristic polynomial is precisely \(t^8\) times the reciprocal of the displayed degree-24 zeta denominator. In particular the integer identity holds for all lengths, not merely those tested. The second independently evaluates the four-by-four parity character formula through length 72 and compares each count through length 17 with direct enumeration of every binary word. Both programs were executed successfully on the embedded source files.

## Relationship to prior work
Leupold and Mitrana (2007) treat fixed-length tandem duplications, their primitive linear words, and codes, including regularity of the language, but their exact results are not a circular periodic-point enumeration or this factored zeta function. Jain, Farnoud, Schwartz, and Bruck (2016, Section III) give a linear derivative/RLL correspondence for fixed duplication length; a cyclic derivative introduces independent parity constraints indexed by \(\gcd(n,3)\) and does not have that unconstrained linear tail. The present result supplies the missing cyclic counting identity and a full primitive-orbit census. The general existence of a finite-state automaton and rational zeta for a finite-type shift is classical; neither is claimed as novel in isolation.

## Limitations
The theorem concerns binary alphabets, the single forbidden tandem-square half-length three, and all cyclic rotations with a marked origin. It is not a classification of all square-free circular words, not an error-correcting code capacity theorem, and does not establish any experimentally validated biological mechanism. Prior-art searches cannot establish absolute historical uniqueness, and the 2005 paper by Leupold, Martín-Vide and Mitrana was available only through its abstract during the comparison; the remaining historical-priority risk is stated explicitly in the review.

## References
1. P. Leupold and V. Mitrana, “Uniformly bounded duplication codes,” *RAIRO – Theoretical Informatics and Applications* **41** (2007), 411–424, https://doi.org/10.1051/ita:2007021 ; openly accessible full text: https://www.numdam.org/article/ITA_2007__41_4_411_0.pdf . Published online August 17, 2007.
2. S. Jain, F. Farnoud, M. Schwartz and J. Bruck, “Duplication-Correcting Codes for Data Storage in the DNA of Living Organisms,” https://arxiv.org/abs/1606.00397 , first submitted June 1, 2016.
3. P. Leupold, C. Martín-Vide and V. Mitrana, “Uniformly bounded duplication languages,” *Discrete Applied Mathematics* **146** (2005), 301–310, https://doi.org/10.1016/j.dam.2004.10.003 ; abstract consulted, full text unavailable for comparison.
