# Sharp parity-support separation for two companion binomial transforms

## Finding

For integers \(n\ge 0\), let \([a]_2\in\{0,1\}\) denote the least nonnegative residue of the integer \(a\) modulo \(2\), and let an ordinary binomial coefficient be \(0\) when its lower argument exceeds its nonnegative upper argument. Define the integer-valued sums
\[
U(n)=\sum_{k=0}^{n}\left[\binom{n+5k}{2n+2k}\binom nk\right]_2,
\qquad
V(n)=\sum_{k=0}^{n}\left[\binom{n+5k}{2k}\binom nk\right]_2.
\]

Every maximal run of ones in the binary expansion of \(n\) has a positive integer length. The following are exact, for every \(n\ge0\):
\[
U(n)\equiv1\pmod2\iff\text{each run length is in }\{0,1,2,3\}\pmod5,
\]
\[
V(n)\equiv1\pmod2\iff\text{each run length is in }\{0,3\}\pmod5.
\]
The conditions are vacuous for \(n=0\). Consequently the odd-value support of \(V\) is a proper subset of that of \(U\).

Define the dyadic support counts \(u_m=\#\{0\le n<2^m: U(n)\text{ is odd}\}\) and \(v_m=\#\{0\le n<2^m:V(n)\text{ is odd}\}\). Their complete ordinary generating functions are
\[
\boxed{\sum_{m\ge0}u_mz^m=\frac{1+z+z^2+z^3}{1-z-z^2-z^3-z^4-z^5}},
\qquad
\boxed{\sum_{m\ge0}v_mz^m=\frac{1+z^3}{1-z-z^4-z^5}}.
\]
Let \(\lambda_U\) and \(\lambda_V\) be the unique real roots greater than \(1\) of
\[
\lambda_U^5-\lambda_U^4-\lambda_U^3-\lambda_U^2-\lambda_U-1=0,
\quad
\lambda_V^5-\lambda_V^4-\lambda_V-1=0.
\]
Then \(1<\lambda_V<\lambda_U<2\), and there are strictly positive constants \(C_U,C_V\) for which
\[
u_m\sim C_U\lambda_U^m,\qquad
v_m\sim C_V\lambda_V^m,\qquad
\frac{v_m}{u_m}\sim \frac{C_V}{C_U}\left(\frac{\lambda_V}{\lambda_U}\right)^m\longrightarrow0.
\]
Writing \(\delta_U=\log_2\lambda_U\) and \(\delta_V=\log_2\lambda_V\), the unrestricted prefix counts satisfy
\[
\#\{0\le n<X:U(n)\text{ odd}\}=\Theta(X^{\delta_U}),\qquad
\#\{0\le n<X:V(n)\text{ odd}\}=\Theta(X^{\delta_V}).
\]
Numerically \(\lambda_U\approx1.965948236645485\), \(\delta_U\approx0.975225336064051\), \(\lambda_V\approx1.497094048762797\), and \(\delta_V\approx0.582164855612572\). Both odd-value sets have natural density zero, but their exact sparsity exponents differ.

## Assumptions and scope

The sums are integer sums of the individual residues \([\cdot]_2\), not sums of integer binomial products followed by a single reduction modulo \(2\). No distributional or primality hypothesis is used. The published run-length-transform identities of Rampersad and Wiebe, Theorems 13 and 14 of arXiv:2309.04012v1, are explicitly used as inputs. Everything after these identities is established below. The theorem concerns these two specified transforms, not all binomial transforms, and no statement is made about their actual non-parity values.

## Proof

**Step 1: the base sequences and their parities.** By the cited Theorems 13 and 14, \(U(n)\) and \(V(n)\) are respectively the run-length transforms of integer sequences \(s^{(U)}_j\) and \(s^{(V)}_j\). Both satisfy
\[
s_j=s_{j-1}+s_{j-2}-s_{j-3}+s_{j-4}\quad(j\ge4),
\]
with initial vectors \((1,1,1,1)\) and \((1,2,2,3)\). Reducing modulo \(2\) gives
\[
s_{j+4}\equiv s_{j+3}+s_{j+2}+s_{j+1}+s_j\pmod2.
\]
Applying this twice, \(s_{j+5}\equiv s_j\pmod2\), for every \(j\ge0\). The first five entries have parities \((1,1,1,1,0)\) and \((1,0,0,1,0)\), respectively. Thus the periodicity and each of the stated sets of allowed residues are exact, including arbitrary long runs. The run-length-transform formula is a product over maximal one-run lengths, so its parity is \(1\) exactly when every constituent factor is odd. Since \(\{0,3\}\subsetneq\{0,1,2,3\}\), the inclusion follows; it is proper already at \(n=1\), for which \(U(1)\) is odd and \(V(1)\) is even.

**Step 2: exact length enumeration.** For a set \(L\) of permitted positive one-run lengths, put \(R(z)=\sum_{\ell\in L}z^\ell\). Every finite binary word is uniquely a word of zero or more initial zeros, followed by zero or more blocks comprising an allowed one-run and a nonempty zero-run, followed optionally by one final allowed one-run. The ordinary length-generating function is therefore the formal power series
\[
A(z)=\frac1{1-z}\frac1{1-\frac{zR(z)}{1-z}}(1+R(z))
=\frac{1+R(z)}{1-z-zR(z)}.
\]
For the first parity condition and the second respectively,
\[
R_U(z)=\frac{z+z^2+z^3+z^5}{1-z^5},\qquad
R_V(z)=\frac{z^3+z^5}{1-z^5}.
\]
Substitution and cancellation give precisely the two displayed rational functions. The mapping of length-\(m\) binary words (allowing leading zeros) to integers \(0\le n<2^m\) is bijective, and adding leading zeros does not alter maximal one-runs, so the coefficients are exactly \(u_m,v_m\). In particular, the first counts are \((u_0,\ldots,u_9)=(1,2,4,8,15,30,59,116,228,448)\) and \((v_0,\ldots,v_9)=(1,1,1,2,3,5,7,10,15,23)\). For example, \(v_m=v_{m-1}+v_{m-4}+v_{m-5}\) for every \(m\ge5\).

**Step 3: dominant singularities and sharp growth.** Let \(D_U(z)=1-z-z^2-z^3-z^4-z^5\) and \(D_V(z)=1-z-z^4-z^5\). Each \(D_i\) is strictly decreasing on \((0,1)\), with \(D_i(1/2)>0\) and \(D_i(1)<0\). Thus each has a unique positive zero \(\rho_i\in(1/2,1)\), and its reciprocal \(\lambda_i\in(1,2)\) is the stated real polynomial root. Also \(D_U(z)<D_V(z)\) for \(0<z<1\), so \(\rho_U<\rho_V\), proving \(\lambda_U>\lambda_V\). Every coefficient of \(1-D_i(z)\) is nonnegative, and the exponent \(1\) occurs. If \(D_i(z)=0\) and \(|z|\le\rho_i\), the triangle inequality forces \(|z|=\rho_i\). Equality requires every nonzero monomial \(z^j\) to be positive real; the degree-one term forces \(z=\rho_i\). Hence this is the unique pole of smallest modulus; it is simple since \(D'_i(\rho_i)<0\), and is not canceled by the numerator, which is positive there. Partial fractions give
\[
a_m^{(i)}\sim C_i\rho_i^{-m},\qquad
C_i=-\frac{N_i(\rho_i)}{\rho_i D_i'(\rho_i)}>0,
\]
where \(N_U(z)=1+z+z^2+z^3\) and \(N_V(z)=1+z^3\). The ratio follows. Finally, when \(2^{m-1}\le X<2^m\), monotonicity traps the odd-value count below \(X\) between the corresponding length-\((m-1)\) and length-\(m\) counts. The asymptotics give the claimed global \(\Theta(X^{\log_2\lambda_i})\) laws. Since each \(\lambda_i<2\), both densities vanish.

## Verification

The standalone `checker.py` directly computes the individual binomial parities via Lucas's bit criterion, checks the run-length criterion for both transforms for all \(0\le n<1024\), compares exact dyadic counts with coefficient recurrences and independent word enumeration through 14 bits, and checks the period-five seed parity and approximate dominant roots and leading constants. The included `checker-output.txt` was generated by executing this code. This is finite corroboration only; the complete infinite proof is in the preceding steps.

## Relationship to prior work

The input run-length transforms are **published, not claimed as new**: Rampersad and Wiebe, arXiv:2309.04012v1 (7 September 2023), Theorems 13 and 14, explicitly identify the two transforms and note that their base sequences have the same recurrence but different initial data. The new conclusion concerns odd-value support, exact counting, entropy growth, and strict relative sparsity. Wu's earlier arXiv:1610.06166 (2016) treats earlier run-length transforms and provides a precursor, not these two identified new 2023 identities. **The first generating function's binary-word count is independently already represented in OEIS A124312**, whose 2015 comment identifies the forbidden-run enumeration. Accordingly, the first formula is used as an exact known comparison, **not independently offered as an original enumeration**. The new mathematical assertion is the arithmetic-transform support inclusion together with the second transform's exact support-growth law and the sharp exponential relative thinning. General regular-language enumeration principles are classical; their availability does not by itself provide these specific arithmetic conclusions.

## Limitations

No claim of inventing run-length transforms or general finite-automata enumeration is made. The result supplies asymptotic order for the two parity supports, not an asymptotic distribution for the magnitudes of \(U(n)\) or \(V(n)\). The source work supplies the crucial run-length identities; this proof is conditional on those proved identities. Some mathematically equivalent run-length counting formulas might be indexed under different sequence names, so novelty is assessed within the stated inspected literature. Independent validation has not been performed.

## References

1. N. Rampersad and M. Wiebe, *Sums of products of binomial coefficients mod 2 and 2-regular sequences*, arXiv:2309.04012v1, submitted 2023-09-07, especially Section 5, Theorems 13–14. https://arxiv.org/pdf/2309.04012v1
2. C. W. Wu, *Sums of products of binomial coefficients mod 2 and run length transforms of sequences*, arXiv:1610.06166v1, posted 2016-10-19. https://arxiv.org/abs/1610.06166
3. OEIS A124312, pentanacci companion sequence and 2015 binary-word forbidden-run interpretation. https://oeis.org/A124312
