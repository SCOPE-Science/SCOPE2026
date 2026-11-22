# Maximal collective independence and a sharp parity obstruction for Kummer carry profiles

## Finding
Fix any even integer \(d\ge2\), write \(d=2^s m\) with \(s\ge1\) and \(m\) odd, and draw \(X\) from the uniform probability measure on \([0,1)\). Define the Kummer phase carry
\[
F_j(x)=\lfloor dx\rfloor-\lfloor jx\rfloor-\lfloor(d-j)x\rfloor,\qquad 1\le j<d,
\]
and its central member \(C(x)=F_{d/2}(x)\). Write
\[
J_d=\{j\in\{1,\ldots,d-1\}:2^s\mid j\},\qquad V_d=(F_j(X))_{j\in J_d}.
\]

**Theorem (maximal joint independence and exact obstruction).** For every possible vector value \(v\) and both \(e=0,1\),
\[
\Pr(C=e,V_d=v)=\tfrac12\Pr(V_d=v).
\]
Thus \(C\) is a fair Bernoulli variable independent of the **entire** vector \(V_d\), not merely uncorrelated with its individual coordinates. The set \(J_d\) is the unique inclusion-maximal collection of indices whose full carry vector is independent of \(C\).

Explicitly, for any \(1\le j<d\), express \(j/d=a/b\) in lowest terms, where \(1\le a<b\). Then
\[
\operatorname{Cov}(C,F_j)=
\begin{cases}
0,& b\text{ odd},\\
\dfrac{1}{4a(b-a)},&b\text{ even}.
\end{cases}
\]
The complete two-bit law, for \(e,f\in\{0,1\}\), is
\[
\Pr(C=e,F_j=f)=\frac14+(2e-1)(2f-1)\operatorname{Cov}(C,F_j).
\]
In particular, a ratio with an even reduced denominator gives strictly *positive* dependence. A ratio with an odd reduced denominator belongs to \(J_d\), and all such ratios collectively form the independent vector.

## Assumptions and scope
All probabilities are with respect to **Lebesgue measure of the common real phase** \(x\in[0,1)\), and all equality and shift statements hold outside finitely many discontinuity points. The integers \(d\), \(j\), \(s\), \(m\), \(a\), \(b\) satisfy precisely the conditions in the Finding. The binomial-carry link is the Kummer phase identity
\[
\nu_p\!\left(\binom{dn}{jn}\right)=\sum_{r\ge1}F_j\!\left(\left\{\frac{n}{p^r}\right\}\right)
\]
for every prime \(p\) and positive integer \(n\), with the finite sum interpreted via eventually zero terms. **No claim is made that the phases of a particular integer are uniformly sampled or independent across prime powers.**

## Proof
**Step 1 — fair individual carries.** The floor identity
\[
\lfloor u+v\rfloor-\lfloor u\rfloor-\lfloor v\rfloor\in\{0,1\}
\]
shows \(F_j\) is binary. Its period is \(1\), since \(d=j+(d-j)\). Outside finitely many breakpoints, \(F_j(1-x)=1-F_j(x)\), because \(\lfloor-kx\rfloor=-\lfloor kx\rfloor-1\) when \(kx\notin\mathbb Z\). This measure-preserving reflection yields \(\mathbb E[F_j]=1/2\), including \(C\).

**Step 2 — a transformation that toggles the central carry and fixes the entire family.** Set \(h=2^{-s}\) and \(T(x)=x+h\pmod1\). Every index \(j\in J_d\), together with \(d\) and \(d-j\), is divisible by \(2^s\). Therefore their floor increments under the unwrapped shift by \(h\) are integers whose combination cancels, so \(F_j(Tx)=F_j(x)\) everywhere except the irrelevant breakpoints. In contrast, writing \(u=(d/2)x\) gives
\[
C(x)=\lfloor2u\rfloor-2\lfloor u\rfloor=\lfloor2\{u\}\rfloor.
\]
The shift changes \(u\) by \(m/2\), which is a half-integer since \(m\) is odd, and hence \(C(Tx)=1-C(x)\) off the boundaries. Because \(T\) preserves Lebesgue measure, for every event \(B\) determined by the full vector \(V_d\),
\[
\Pr(B,C=1)=\Pr(B,C=0)=\tfrac12\Pr(B).
\]
This proves **simultaneous** independence for arbitrarily large finite vectors \(V_d\), without assuming independent coordinates inside \(V_d\).

**Step 3 — exact two-point obstruction.** Put \(\psi(t)=\{t\}-1/2\) outside integers (values at integers are immaterial). The centered carry decomposes as
\[
F_j(x)-\frac12=\psi(jx)+\psi((d-j)x)-\psi(dx).
\]
For positive integers \(u,v\), the standard sawtooth covariance identity is
\[
K(u,v):=\int_0^1\psi(ux)\psi(vx)\,dx=\frac{\gcd(u,v)^2}{12uv}.
\]
For completeness, the \(L^2\) sine expansion \(\psi(t)=-\sum_{r\ge1}\sin(2\pi rt)/(\pi r)\) and Fourier orthogonality leave only the pairs \(ru=kv\). If \(g_0=\gcd(u,v)\), they are \(r=(v/g_0)t\), \(k=(u/g_0)t\), and the resulting \(\sum_{t\ge1}t^{-2}=\pi^2/6\) gives the identity. The \(L^2\) limit justifies the product integral.

By bilinearity, using \(C-1/2=2\psi((d/2)x)-\psi(dx)\) and canceling the \(\psi(dx)\) terms,
\[
\operatorname{Cov}(C,F_j)=2K(d/2,j)+2K(d/2,d-j)-K(d,j)-K(d,d-j).
\]
Write \(g=\gcd(d,j)\), \(d=gb\), \(j=ga\), with \(\gcd(a,b)=1\), and \(h_0=\gcd(2,b)\). Then
\[
\gcd(d/2,j)=\gcd(d/2,d-j)=\frac{g h_0}{2},
\]
where the right side is an integer because \(d\) is even. Substitution yields
\[
\operatorname{Cov}(C,F_j)
=\frac{h_0^2-1}{12a(b-a)}.
\]
Since \(h_0=1\) when \(b\) is odd and \(h_0=2\) when \(b\) is even, the stated dichotomy follows. The two-bit probability formula follows by using both fair Bernoulli marginals: the \((1,1)\) probability equals \(1/4+\operatorname{Cov}\), both unequal outcomes equal \(1/4-\operatorname{Cov}\), and the \((0,0)\) probability equals the \((1,1)\) probability.

**Step 4 — sharpness.** The reduced denominator \(b=d/\gcd(d,j)\) is odd **if and only if** \(2^s\mid j\). Hence every index outside \(J_d\) has a strictly positive covariance with \(C\) and cannot even be individually independent. Any jointly independent family must be a subset of \(J_d\), while Step 2 shows that all of \(J_d\) works. This proves unique inclusion-maximality.

## Verification
The self-contained Python 3 standard-library program `CHECK.py` independently integrates the piecewise-constant floor functions using **exact rational interval endpoints**. It checks every binary joint-probability cell for every even \(d\) from \(2\) to \(100\), and every nonempty complete-vector fiber of \(V_d\) at these denominators. Running `python3 CHECK.py` completed successfully: **10,000** exact two-bit probability checks and **6,232** vector-fiber conditional-independence checks. The proof above, rather than finite testing, establishes all infinitely many cases.

For example, when \(d=30\), \(s=1\), and \(j=5\), the reduced ratio is \(1/6\), so \(\operatorname{Cov}(C,F_5)=1/20\) and \(\Pr(C=F_5=1)=3/10\). By contrast, for \(j=6\) the reduced ratio is \(1/5\), and both \(F_6\) alone and the entire even-index carry vector are independent of \(C=F_{15}\).

## Relationship to prior work
Wu (first submitted 18 June 2026, arXiv:2606.20940v1) studies greatest common divisors across the family \(\binom{mn}{mk}\), drawing on Kummer's theorem. The family in the present theorem, \(\binom{dn}{jn}\) with different ratios \(j/d\), is distinct: it asks how all carry restrictions at one common real phase interact. Guo and collaborators (22 June 2026, arXiv:2606.22997v1) analyze a further binomial GCD family through Lucas congruences; their prime-power digit-box stabilizer does not state this cross-ratio phase law. Cui and Yang (19 November 2026, arXiv:2611.25794v1), later than those motivating sources, directly define the same phase carry and establish half-measure for each individual zero set, while counting simultaneous restrictions at **different prime-power phases**. That later work does not state same-phase joint-vector independence across ratios. Ford and Konyagin (2019 preprint, 2021 publication, arXiv:1909.03903) investigate central coefficients and correlations across prime-power phases. The sawtooth \(\gcd\)-integral is classical, so the pairwise covariance is not alone claimed new. The structural distinction is the joint-vector independence and its sharp maximal boundary.

## Limitations
No independence is claimed between coordinates inside \(V_d\), between different prime-power inputs \(\{n/p^r\}\), or between binomial-coefficient valuations as integer \(n\) varies. The theorem concerns the Lebesgue phase model only. Earlier implicit coverage through broader Fourier or dynamical formulations remains possible.

## References
1. C. W. Wu, *Computing the Greatest Common Divisor of Binomial Coefficients* \(\binom{mn}{mk}\), arXiv:2606.20940v1, first posted 18 June 2026, https://arxiv.org/abs/2606.20940.
2. D. Guo, R. Qiu, Y. Cao, R. Feng and X.-S. Gao, *A Greatest Common Divisor Criterion of Certain Binomial Coefficients*, arXiv:2606.22997v1, 22 June 2026, https://arxiv.org/abs/2606.22997; primary MSC2020 11B65.
3. K. Ford and S. Konyagin, *Divisibility of the central binomial coefficient*, arXiv:1909.03903 (2019; Transactions of the American Mathematical Society 374 (2021), 923–953), https://arxiv.org/abs/1909.03903.
4. Z. Cui and Z. Yang, *The distribution of greatest common divisors of binomial coefficients and their upper indices*, arXiv:2611.25794v1, first submitted 19 November 2026, https://arxiv.org/html/2611.25794v1 (later directly related work, included for priority comparison).
5. Classical integer-frequency sawtooth integral identity, \(\int_0^1\psi(ux)\psi(vx)\,dx=\gcd(u,v)^2/(12uv)\), proved directly in Step 3; also recorded at https://ysharificalc.wordpress.com/tag/fractional-part-function/.
