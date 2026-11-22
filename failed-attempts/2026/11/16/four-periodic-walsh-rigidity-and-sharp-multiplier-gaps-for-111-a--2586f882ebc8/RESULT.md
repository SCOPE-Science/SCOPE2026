# Four-periodic Walsh rigidity and sharp multiplier gaps for \(111\)-avoiding cubes

## Finding
For every integer \(n\ge3\), define \(A_n\subseteq\mathbb F_2^n\) to consist of all binary strings with no substring \(111\). For every \(u\in\mathbb F_2^n\), let the **unnormalized** Walsh multiplier be
\[
 W_n(u)=\sum_{x\in A_n}(-1)^{u\cdot x}.
\]
The greatest common divisor of all these signed integers equals their smallest positive absolute value:
\[
 \gcd_{u\in\mathbb F_2^n} W_n(u)
 =\min_{W_n(u)\ne0}|W_n(u)|
 =\delta_n,
 \qquad
 \delta_n=\begin{cases}
 1,&n\equiv0,3\pmod4,\\
 2,&n\equiv1\pmod4,\\
 4,&n\equiv2\pmod4.
 \end{cases}
\]
In particular, **every** multiplier is divisible by four when \(n\equiv2\pmod4\), and this bound is attained. Counting convolution by \(\mathbf 1_{A_n}\) on the additive Boolean group is invertible exactly for \(n\equiv0,3\pmod4\). Its Hilbert-space Moore–Penrose inverse has exact norm \(\|T_n^\dagger\|_{2\to2}=1/\delta_n\). The novelty-bearing assertion is the **uniform signed-frequency divisibility and sharp nonzero gap**, not the unsigned tribonacci recurrence or its signed uniform specialization.

## Assumptions and scope
Binary strings are linearly ordered, with no wraparound restriction on the first and last bits. The condition forbids three consecutive ones, but allows two. The inner product \(u\cdot x\) is over \(\mathbb F_2\). The transform has no normalization factor. The counting convolution is
\[
 (T_n h)(z)=\sum_{x\in A_n}h(z+x)
\]
on complex functions with the ordinary counting \(\ell^2(\mathbb F_2^n)\) norm. The frequency \(u\) corresponds to coordinate signs \(s_i=(-1)^{u_i}\).

## Proof
**1. Exact transfer.** Let \(v_j=(a_j,b_j,c_j)^\top\) record signed weights of admissible prefixes of length \(j\) ending in zero, one, or two consecutive ones. The empty-prefix state is \(v_0=(1,0,0)^\top\). Appending a coordinate of sign \(s\in\{+1,-1\}\) changes the state by
\[
 M(s)=\begin{pmatrix}1&1&1\\s&0&0\\0&s&0\end{pmatrix},
 \qquad v_j=M(s_j)v_{j-1},\qquad W_n(u)=(1,1,1)v_n.
\]
Direct integer multiplication gives \(M(-1)^4=I_3\). For all-negative signs, the multipliers in lengths zero through three are \(1,0,0,1\), hence the all-negative frequency gives zero when \(n\equiv1,2\pmod4\) and gives one when \(n\equiv0,3\pmod4\). The same matrix identity shows that signs \((+,-,\dots,-)\), with a multiple of four trailing minus signs, give exactly \(2\) when \(n\equiv1\pmod4\); signs \((+,+,-,\dots,-)\) give exactly \(4\) when \(n\equiv2\pmod4\). These are explicit witnesses in every admissible dimension.

**2. Odd-multiplier cases.** Put \(P=M(+1)\), \(e=(1,0,0)^\top\), and \(w=(1,1,1)\). The cardinality \(N_n=|A_n|=wP^n e\) obeys the tribonacci recurrence with initial values \(N_0=1,N_1=2,N_2=4\). Since \(P^4\equiv I_3\pmod2\), we have \(N_n\equiv1\pmod2\) for \(n\equiv0,3\pmod4\), while \(N_n\) is even for the remaining classes. Every Walsh sum has the same parity as \(N_n\), so all multipliers are odd, and hence nonzero, when \(n\equiv0,3\pmod4\). The explicit all-negative frequency attains magnitude one.

**3. Fourfold divisibility in the remaining even class.** For a set of negative-sign positions \(S\subseteq[n]\), let \(d_i\) be the number of admissible strings with the \(i\)-th bit equal to one. Expansion of the sign product gives the exact congruence
\[
 W_n(S)\equiv N_n-2\sum_{i\in S}d_i\pmod4.
\]
Write
\[
 B=\begin{pmatrix}0&0&0\\1&0&0\\0&1&0\end{pmatrix},\qquad
 d_i=wP^{n-i}BP^{i-1}e.
\]
Direct matrix arithmetic gives \(P^8\equiv I_3\pmod4\). The values \(N_2=4\) and \(N_6=44\) imply \(N_n\equiv0\pmod4\) for every \(n\equiv2\pmod4\). Moreover, from \(P^4\equiv I_3\pmod2\) and the four cases \(i\equiv1,2,3,0\pmod4\),
\[
 \big(wP^{(2-i)\bmod4}BP^{(i-1)\bmod4}e\big)_{i=1}^{4}
 \equiv(0,0,0,0)\pmod2.
\]
Thus all \(d_i\) are even in the class \(n\equiv2\pmod4\), so every multiplier is divisible by four. The two-positive-sign witness from step 1 attains four exactly.

**4. Sharpness and consequences.** For \(n\equiv1\pmod4\), parity gives universal divisibility by two, and the first-positive-sign witness attains two. Together with steps 2 and 3, this proves all four exact minimum nonzero magnitudes and gcds. Fourier characters diagonalize \(T_n\) with eigenvalues \(W_n(u)\), proving the invertibility criterion and the exact Hilbert pseudoinverse norm. No assertion about the number of zero multipliers in the singular cases is needed or made.

## Verification
The included `verify.py` uses two independent methods to compute each signed multiplier: (i) a full integer Walsh–Hadamard transform of the explicitly enumerated indicator, and (ii) the three-state signed transfer. It verifies **every frequency** for \(1\le n\le16\), matrix identities for the infinite proof, divisibility and sharp witnesses, and additional witnesses in dimensions through \(100\). Run `python verify.py`. Its exact-integer output is included as `verification_output.txt`; success ends with `TRIBONACCI_CUBE_WALSH_PERIOD_FOUR_PASS`. The finite checks corroborate but do not replace the symbolic all-dimensional proof.

## Relationship to prior work
Generalized Fibonacci cubes and the specific vertex set defined by avoiding \(111\) were studied well before this result. Azarija et al. (2014) investigate isomorphisms of forbidden-factor cubes; Rho and Vesel (2016) study recursion and recognition of the \(111\)-avoiding graph and give its tribonacci cardinality. A separate study of fan-graph dissociation polynomials derives the **univariate** weight enumerator of precisely these binary words: in that guise, all coordinates receive the same weight. These earlier results supply the object and unsigned or uniform-weight information. Indeed, the all-negative cancellation pattern and the odd-cardinality cases follow from uniform-weight specialization and parity; they are not claimed alone as new. In contrast, the theorem's assertion that **every independent-coordinate signing** has valuation at least two in one residue class, with exact attainable gaps in all classes, requires the additional multivariate matrix congruences above and is not supplied by those scalar enumerators. Related Fourier work on ordinary Fibonacci and Lucas cubes concerns different vertex sets or restricted sampling Gramians, rather than this full family of additive-convolution multipliers.

## Limitations
The theorem is specific to words avoiding three consecutive ones, not words avoiding arbitrary forbidden factors, cyclic words, or all higher-order generalized Fibonacci cubes. It gives exact divisibility and the minimum nonzero magnitude, but not a closed formula for full multiplier multiplicities, ranks in the singular cases, or endpoint \(\ell^1/\ell^\infty\) projection constants. Published-priority comparison is bounded; differently named multivariate signed-word enumerations remain a residual risk. Independent review has not been performed.

## References
1. J. Azarija, S. Klavžar, J. Lee, J. Pantone and Y. Rho, *On Isomorphism Classes of Generalized Fibonacci Cubes*, arXiv:1402.6377, first posted 25 February 2014; https://arxiv.org/abs/1402.6377.
2. Y. Rho and A. Vesel, *Linear recognition of generalized Fibonacci cubes \(Q_h(111)\)*, Discrete Mathematics & Theoretical Computer Science 17:3 (2016), 349–362, DOI 10.46298/dmtcs.2165; https://dmtcs.episciences.org/en/articles/2165.
3. *Dissociation polynomial and extremal coefficients of fan graphs* (2026), publicly indexed study of the scalar dissociation polynomial and its \(111\)-avoiding path component; the claim here does not assert originality of that scalar recurrence.
