# Renewal entropy of the finite-alphabet tortoise image language

## Finding

Let \(\tau\) be the one-pass Defant–Kravitz tortoise stack map and, for each integer \(q\ge1\), let \(\mathcal I_q=\tau(\{0,\ldots,q-1\}^*)\). Write \(a_q(n)=|\mathcal I_q\cap\{0,\ldots,q-1\}^n|\), \(A_q(z)=\sum_{n\ge0}a_q(n)z^n\), and \(\lambda_q=\lim_{n\to\infty}a_q(n)^{1/n}\).

**Theorem.** For every integer \(q\ge2\), the image language is regular and has the exact recursive description
\[
\mathcal I_q=\mathcal I_{q-1}\ \cup\ \mathcal I_{q-1}\mathcal I_{q-1}(q-1)\bigl(\mathcal I_{q-1}(q-1)\bigr)^*,\qquad \mathcal I_1=0^*.
\]
Let \(R_{q-1}\) be the radius of convergence of \(A_{q-1}\). There is a unique \(r_q\in(0,R_{q-1})\) with
\[
 r_q A_{q-1}(r_q)=1.
\]
The exact exponential image count is given by
\[
 a_q(n)=\Theta_q(r_q^{-n}),\qquad \lambda_q=r_q^{-1},\qquad
 1=\lambda_1<\lambda_2<\lambda_3<\cdots.
\]
In particular, every \(\lambda_q\) is algebraic and computable by rational-language operations. For \(q\ge3\), \(\lambda_q<q\), whereas \(\lambda_2=2\) and \(a_2(n)=2^{n-1}+1\) for \(n\ge1\). This is a strict output-density transition: the reachable fraction tends to \(1/2\) on the binary alphabet, but decays exponentially for each fixed larger alphabet. Quantitatively, for \(q\ge3\),
\[
 \frac{a_q(n)}{q^n}\le (1-q^{-4})^{\lfloor n/4\rfloor}.
\]
The first previously uncounted alphabet growth constant from this recursion is the quaternary value
\[
\lambda_4=3.5503790656826695\ldots,
\]
whose reciprocal is the unique root in \((0,1/\lambda_3)\) of
\[
 z^6+8z^5-4z^4-18z^3+21z^2-8z+1=0.
\]
This is a statement about the *set of possible images* (Hartley entropy), not the Shannon entropy of the induced, nonuniform output distribution.

## Assumptions and scope

The alphabet \(\Sigma_q=\{0,\ldots,q-1\}\) is totally ordered. The empty word belongs to the language and has length zero. If a nonempty input has maximal letter \(m\), occurring \(k\ge1\) times, uniquely write it as \(u_0 m u_1 m\cdots m u_k\), with each \(u_i\) using letters below \(m\). The map satisfies
\[
 \tau(u_0 m u_1 m\cdots m u_k)
 =\tau(u_0)\tau(u_1)m\tau(u_2)m\cdots\tau(u_k)m,
 \qquad\tau(\varepsilon)=\varepsilon.
\]
All assertions quantify over all finite words, every length \(n\) and all fixed positive integral alphabet sizes within the stated ranges. No statements about multiple tortoise passes or restricted factor sets are implied.

## Proof

**1. Exact image-language grammar.** For each \(q\ge2\), let \(m=q-1\). Inputs without \(m\) map exactly onto \(\mathcal I_{q-1}\). An input with \(k\ge1\) copies of \(m\) maps to \(v_0v_1m(v_2m)\cdots(v_km)\) with every \(v_i\in\mathcal I_{q-1}\). Conversely, for any such tuple choose independent lower-alphabet preimages of the \(v_i\). This proves both inclusions in the claimed grammar. Since regular languages are closed under union, concatenation and Kleene star, induction from \(0^*\) proves regularity and hence rationality of each \(A_q(z)\). No unambiguous grammar hypothesis is used.

**2. A uniquely decodable renewal sublanguage.** Put \(U=\mathcal I_{q-1}\) and \(A=A_{q-1}(z)\). The language \((Um)^*\subseteq\mathcal I_q\) has the exact generating function \(1/(1-zA(z))\): each maximum-letter marker terminates exactly one lower-alphabet block, making the factorization unique. The full grammar, in which the two leading \(U\)-blocks can overlap in representation, nevertheless gives the *coefficientwise* bounds
\[
 \frac{1}{1-zA(z)}\ \preceq\ A_q(z)\ \preceq\ A(z)+\frac{zA(z)^2}{1-zA(z)},
\]
where \(\preceq\) compares nonnegative coefficients. The right inequality counts representations, not necessarily distinct outputs.

**3. Equality of exponential rates.** Inductively suppose \(a_{q-1}(n)=\Theta(\lambda_{q-1}^n)\) and \(R_{q-1}=1/\lambda_{q-1}\). This starts at \(q=1\), for which \(A_1(z)=1/(1-z)\). Since \(A(z)\) has positive coefficients and diverges as the positive real \(z\uparrow R_{q-1}\), the strictly increasing function \(zA(z)\) crosses one at exactly one \(r_q\in(0,R_{q-1})\). Both bounding rational series have a simple pole there. Moreover, \(A(z)\) has strictly positive coefficients at every degree (the constant-zero words), so \(zA(z)\) has positive coefficients at every positive degree. The triangle inequality is strict away from the positive real point on \(|z|=r_q\), proving that no other zero of \(1-zA(z)\) lies on that circle. Rational-function coefficient estimates therefore bound the lower coefficients below by \(c_qr_q^{-n}\) and the upper coefficients above by \(C_qr_q^{-n}\) for sufficiently large \(n\), with positive finite constants. Squeezing proves \(a_q(n)=\Theta_q(r_q^{-n})\) and the claimed limit. Because \(r_q<R_{q-1}\), the growth constants increase strictly; rationality of \(A\) makes \(r_q\) algebraic.

**4. Sharp output-density dichotomy.** On two symbols, a tortoise image is either all zeros or ends in one, and every such word is realizable. Hence \(a_2(n)=2^{n-1}+1\) for \(n\ge1\). For \(q\ge3\), the length-four factor \((q-1)(q-2)(q-3)(q-1)\) cannot occur in an image: between consecutive maximum letters, the intervening word must be in \(\mathcal I_{q-1}\), but its descending two-symbol factor \((q-2)(q-3)\) cannot itself be a tortoise image, since the map sorts every word of length two. In particular, every full image avoids that four-symbol factor. Testing \(\lfloor n/4\rfloor\) disjoint aligned four-blocks of an arbitrary length-\(n\) word then yields at most \(q^n(1-q^{-4})^{\lfloor n/4\rfloor}\) possible images. This proves \(\lambda_q<q\) and the density conclusion.

**5. Explicit four-letter specialization.** Over two symbols, \(\mathcal I_2=0^*\cup\{0,1\}^*1\), giving \(A_2(z)=1/(1-z)+z/(1-2z)\). Every binary word is a product of two words in \(\mathcal I_2\) (split just after the last one if needed), so the exact ternary grammar simplifies to
\[
 \mathcal I_3=\mathcal I_2\cup\{0,1\}^*2(\mathcal I_2 2)^*,
 \quad A_3(z)=A_2(z)+\frac{z}{(1-2z)(1-zA_2(z))}.
\]
Simplification gives
\[
 A_3(z)=\frac{1-4z+2z^2+7z^3-6z^4-z^5}{(1-z)(1-2z)(1-4z+3z^2+z^3)}.
\]
Substituting this *independently derived* expression into \(1-r_4A_3(r_4)=0\), clearing denominators, and taking the unique solution in \((0,1/\lambda_3)\) gives the stated sextic and numerical constant. Here \(\lambda_3\) is the largest real root of \(x^3-4x^2+3x+1\). The earlier ternary image enumeration is not asserted to be new.

## Verification

The bundled `verify_tortoise_entropy.py` implements both the recursive definition and a separate stack simulation, constructs finite languages directly from the grammar, and compares all three at all lengths \(n\le9\) for \(q=2,3\) and \(n\le7\) for \(q=4\). This covers 52,389 labeled input words. Distinct-output sequences from length zero are, respectively,

- Binary, through length nine: `1, 2, 3, 5, 9, 17, 33, 65, 129, 257`.
- Ternary, through length nine: `1, 3, 6, 14, 35, 91, 242, 653, 1780, 4888`.
- Quaternary, through length seven: `1, 4, 10, 30, 95, 312, 1046, 3557`.

The verifier checks forbidden-pattern avoidance over the tested outputs and numerically checks the three- and four-letter renewal roots. These finite checks independently test definitions and small cases; the all-length proof is symbolic and does not depend on the finite cutoffs.

## Relationship to prior work

Defant and Kravitz [DK] defined the two word stack maps and studied preimage fertility, sorting times, and multiset-restricted sortable words. Their recursive definition underlies the present problem, but their enumerators do not imply fixed-alphabet *distinct-output* growth. Campbell and Rampersad [CR] introduced tortoise-based factor-complexity equivalences for infinite automatic binary words, focusing on paperfolding and Thue–Morse factors; that does not determine the image of the entire free monoid on arbitrary alphabets. A previously available ternary image-language computation already supplies the specialized \(A_3\); its coefficients and \(\lambda_3\) are expressly not claimed as new. The new claim concerns the uniform all-alphabet renewal entropy theorem, strict growth, exponential sparsity and the resulting quaternary constant.

## Limitations

The theorem gives algebraic growth rates through a recursively constructible rational series; it does not provide a compact closed polynomial for general \(q\). It does not determine the exact numbers \(a_q(n)\) in a simplified formula for \(q\ge4\), nor does it determine the distribution of fiber sizes or the Shannon entropy of a random input's output. Priority relative to potentially unindexed equivalent fixed-alphabet image results requires independent bibliographic assessment. Computational checks are finite, while the infinite statements are supported by the proof above.

## References

[DK] Colin Defant and Noah Kravitz, *Stack-sorting for Words*, arXiv:1809.09158 (first public September 24, 2018), https://arxiv.org/abs/1809.09158.

[CR] John M. Campbell and Narad Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811 (first public April 28, 2026), https://arxiv.org/abs/2604.25811; original public submission dated April 28, 2026, primary MSC2020 68R15.
