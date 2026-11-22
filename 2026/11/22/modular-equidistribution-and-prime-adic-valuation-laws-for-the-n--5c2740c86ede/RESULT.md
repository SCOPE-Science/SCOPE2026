# Modular equidistribution and prime-adic valuation laws for the normalized Northshield sequence

## Finding

For integers \(n\ge0\), define Northshield's algebraic-integer sequence by
\[
b_0=0,\quad b_1=1,\quad b_{3n}=b_n,\quad
b_{3n+1}=\sqrt2\,b_n+b_{n+1},\quad
b_{3n+2}=b_n+\sqrt2\,b_{n+1}.
\]
Define the integral coefficient \(c_n\) uniquely by \(b_n=c_n\) when \(n\) is odd and \(b_n=\sqrt2\,c_n\) when \(n\) is even. This includes \(c_0=0\).

**Theorem.** For every integer \(m\ge2\), write \(m=2^kq\) with \(k\ge0\) and \(q\) odd. For each residue \(a\bmod m\), the natural density of indices with \(c_n\equiv a\pmod m\) is
\[
D_m(a)=D_{2^k}(a)D_q(a),\qquad
D_q(a)=\frac1q\prod_{p\mid q}\frac{1-\mathbf1_{p\mid a}/p}{1-p^{-2}},
\]
where \(D_1=1\), and for \(k\ge1\),
\[
D_{2^k}(a)=\begin{cases}3/2^{k+1}&a\text{ odd},\\1/2^{k+1}&a\text{ even}.\end{cases}
\]
The same density is the limit on \(0\le n<3^L\). For each fixed \(m\), convergence on those blocks is exponentially fast in \(L\); ordinary prefix counts have a power-saving error with a modulus-dependent exponent.

**Joint refinement.** The residue triples \((c_n,c_{n+1},n\bmod2)\) modulo \(m\) are equidistributed on
\[
\Omega_m=\{(a,b,e)\in(\mathbb Z/m\mathbb Z)^2\times\{0,1\}:\gcd(a,b,m)=1,\ 2\mid m\Rightarrow[(e=0\Rightarrow b\text{ odd})\land(e=1\Rightarrow a\text{ odd})]\}.
\]
Thus valuations at any finite collection of distinct primes are asymptotically independent. For \(j\ge1\),
\[
\Pr(\nu_2(c_n)=0)=\tfrac34,\quad
\Pr(\nu_2(c_n)=j)=2^{-j-2};\qquad
\Pr(\nu_p(c_n)=0)=\frac p{p+1},\quad
\Pr(\nu_p(c_n)=j)=\frac{p-1}{p^j(p+1)}\ (p\text{ odd}).
\]
Moreover the exact number of even coefficients in each complete ternary block is
\[
\#\{0\le n<3^L:2\mid c_n\}=\frac{3^L+2+(-1)^L}{4}\qquad(L\ge0).
\]

## Assumptions and scope

All indices are nonnegative integers. The singular zero \(c_0=0\) is included in finite-block counts and omitted when interpreting \(\nu_p(c_n)\); it has zero natural density. The symbol \(\Pr\) refers to limiting frequencies of indices, not a probability distribution on integer magnitudes. Products over the empty set are one. In \(\gcd(a,b,m)\), use any integer lifts. The result is for every fixed positive modulus, not a uniform-in-modulus error estimate.

## Proof

**1. Integral normalization.** The defining recurrence preserves \(b_n\in\mathbb Z\) for odd \(n\) and \(b_n\in\sqrt2\mathbb Z\) for even \(n\). Indeed the parity of \(3n\) equals that of \(n\) and the mixed terms have the required parity in the other two branches. Induction gives nonnegative integer \(c_n\). Let \(v_n=(c_n,c_{n+1})^T\) and \(e=n\bmod2\). The exact matrices mapping \(v_n\) to \(v_{3n+r}\), for \(r=0,1,2\), are respectively
\[
\begin{array}{c|ccc}
e=0&\begin{pmatrix}1&0\\2&1\end{pmatrix}&\begin{pmatrix}2&1\\1&1\end{pmatrix}&\begin{pmatrix}1&1\\0&1\end{pmatrix}\\[2pt]
e=1&\begin{pmatrix}1&0\\1&1\end{pmatrix}&\begin{pmatrix}1&1\\1&2\end{pmatrix}&\begin{pmatrix}1&2\\0&1\end{pmatrix}
\end{array}.
\]
The output parity is \(e+r\pmod2\). Each matrix has determinant one, hence \(\gcd(c_n,c_{n+1})=1\) from \((c_0,c_1)=(0,1)\). Modulo two, the attainable states are exactly \((0,1,0),(1,1,0),(1,0,1),(1,1,1)\); the stated parity restrictions follow and are preserved.

**2. Complete modular orbit.** In parity state zero, digit zero acts by \(L=\left(\begin{smallmatrix}1&0\\2&1\end{smallmatrix}\right)\) and digit two by \(U=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)\). Their positive words modulo \(m\) contain their inverses because the matrices have finite order modulo \(m\). For \(2^k\), the words \(U^t,L,U^s\) carry \((0,1)\) to
\[
(t+s(2t+1),\,2t+1)\pmod{2^k}.
\]
Every odd \(b\) arises as \(2t+1\); because \(b\) is a unit, choose \(s\) for any first coordinate. Thus all pairs with odd second coordinate are in the orbit. For an odd prime power, \(2\) is invertible: powers of \(L\) and \(U\) produce all elementary lower and upper transvections, which act transitively on primitive pairs over \(\mathbb Z/p^r\mathbb Z\) by elementary elimination. The Chinese remainder theorem isolates the local transvections (using appropriate common exponents) and proves transitivity for every \(m\). Digit one carries the even state to the odd state by \(B=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)\); its inverse maps every primitive odd-state pair (first coordinate odd if \(m\) is even) back to the preceding even-state class. Hence the orbit equals precisely \(\Omega_m\).

**3. Uniform finite-state sampling.** At each modulus, each of the three digit transformations is a permutation of \(\Omega_m\): its matrix is invertible, and the parity restrictions are preserved. Thus the transition matrix for uniformly chosen ternary digits is doubly stochastic. The walk is irreducible by the orbit calculation; inverses of its permutations are positive powers on this finite set. It is aperiodic because digit zero fixes \((0,1,0)\). The finite-chain convergence theorem therefore gives the uniform measure on \(\Omega_m\) with exponential error on \(L\)-digit words. Those words, including leading zeroes, correspond exactly to \(0\le n<3^L\). For arbitrary cutoffs, split a ternary prefix into at most two aligned free-suffix blocks of each length; apply the same uniform mixing from their fixed initial states. Summing geometric errors gives \(O_m(N^{1-\delta_m})\) for some \(\delta_m>0\), hence the natural density.

**4. Marginals and valuations.** At every odd prime power \(p^r\), uniformly primitive pairs have first-coordinate probability \(p^{-r}(1-\mathbf1_{p\mid a}/p)/(1-p^{-2})\). At \(2^k\), the even parity state permits an arbitrary first coordinate and odd second coordinate, while the odd parity state permits odd first coordinate and arbitrary second coordinate. Both states have equal population, giving the displayed three-to-one factor. CRT multiplicativity proves the stated formula for \(D_m(a)\). Consequently, for odd \(p\), \(\Pr(p^j\mid c_n)=1/(p^{j-1}(p+1))\); for \(p=2\), it is \(2^{-j-1}\), for \(j\ge1\). Subtraction at successive exponents yields the valuation laws. The complete joint distribution modulo products of prime powers factors, so any finite set of valuations is independent in the limiting sense.

**5. Exact parity population.** In the four mod-two states ordered \((0,1,0),(1,0,1),(1,1,0),(1,1,1)\), the digit-count matrix (rows are starting states) is
\[
M=\begin{pmatrix}1&0&1&1\\0&1&1&1\\1&1&1&0\\1&1&0&1\end{pmatrix}.
\]
Its eigenvalues are \(3,-1,1,1\). Starting with the first state, the first coordinate of \((1,0,0,0)M^L\) is exactly \((3^L+2+(-1)^L)/4\). Only that state has even first coefficient. This proves the complete-block count, including \(L=0\).

## Verification

Run `python3 check.py` using Python 3 standard library. The checker independently constructs the original algebraic-integer sequence as pairs of integer coefficients in \(\mathbb Z[\sqrt2]\), checks it against the digit matrices on 19,683 indices and 13 moduli, enumerates and compares complete orbits and rational marginal probabilities for every modulus from 2 to 48, and checks the exact parity count at levels 0 through 9. All tests passed. The infinite modular orbit, mixing, and distribution assertions are proved above, not inferred from finite tests.

## Relationship to prior work

Northshield introduced the algebraic-integer sequence and its rational-enumeration and recurrence properties in 2015. Spiegelhofer proved its base-three digit reversal symmetry in a preprint first made public on 17 September 2017. Neither source's inspected relevant sections supplies this all-modulus equidistribution law, the exact two-adic parity bias, the independent valuation law, or the finite-block parity formula. Ponton's different ternary rational tree gives enumeration formulas but does not imply these frequencies. Standard congruence-subgroup and finite Markov-chain arguments are used as tools, not claimed as new.

## Limitations

The convergence exponent depends on the fixed modulus and is not optimized. No joint law for valuation magnitudes at infinitely many primes is asserted. Bibliographic searches cannot rule out all unindexed equivalent work. The result is a property of the specific normalized ternary sequence, not of all generalized Stern sequences. No independent validation or external certification has been performed.

## References

- S. Northshield, *An Analogue of Stern's Sequence for \(\mathbb Z[\sqrt2]\)*, Journal of Integer Sequences 18 (2015), Article 15.11.6, https://cs.uwaterloo.ca/journals/JIS/VOL18/Northshield/north4.pdf.
- L. Spiegelhofer, *A Digit Reversal Property for an Analogue of Stern's Sequence*, arXiv:1709.05651v1, public 2017-09-17, https://arxiv.org/pdf/1709.05651.
- L. Ponton, *Two Trees Enumerating the Positive Rationals*, Integers 18A (2018), A17, https://math.colgate.edu/~integers/sjs17/sjs17.pdf.
