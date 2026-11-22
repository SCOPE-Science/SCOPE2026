# Parity-stable inversion of cyclic Rule 90 on Lucas-constrained inputs

## Finding
Let \(n\ge2\), let \(A_n\) be all indexed binary cyclic words of length \(n\) with no cyclic occurrence of `11`, and let \(\Phi_n\) be the synchronous Rule-90 update
\[
(\Phi_n(x))_i=x_{i-1}\oplus x_{i+1},\qquad i\in\mathbb Z/n\mathbb Z.
\]
Indices wrap around and \(\oplus\) denotes addition in \(\mathbb F_2\). Restrict only the **initial input** to \(A_n\); subsequent states need not satisfy the constraint. For \(t\ge1\), put \(I_{n,t}=\Phi_n^t(A_n)\) and let \(N_{n,t}(k)\) be the number of **distinct indexed output words** having exactly \(k\) source words in \(A_n\).

Write \(L_n\) for the Lucas number determined by \(L_0=2\), \(L_1=1\) and \(L_{n+2}=L_{n+1}+L_n\). Then \(|A_n|=L_n\) and the following hold.

**(i) Odd rings are perpetually lossless.** If \(n\) is odd, \(\Phi_n^t\) is injective on \(A_n\) for every \(t\ge1\); hence \(|I_{n,t}|=L_n\) and all its nonempty fibers are singletons.

**(ii) Complete even-ring one-step fiber law.** If \(n=2m\), the only nonzero fiber multiplicities at \(t=1\) are
\[
\boxed{N_{n,1}(3)=1,\quad N_{n,1}(2)=2^m-2,\quad N_{n,1}(1)=L_n-2^{m+1}+1.}
\]
In particular,
\[
\boxed{|I_{n,1}|=L_n-2^m.}
\]
The unique triple fiber is the zero output, with sources the all-zero word and the two alternating words. Every double fiber consists of a nonempty proper subset of one cyclic parity class and its complement *within that class*. All remaining admissible sources map injectively. The formulas also hold at \(n=2\), when there is only the triple fiber.

**(iii) Exact time-stability boundary.** If \(n\equiv2\pmod4\), this entire fiber law, including the actual equivalence classes of sources, holds for **every** \(t\ge1\). If \(4\mid n\), the number of distinct outputs strictly decreases between times one and two:
\[
|I_{n,2}|<|I_{n,1}|.
\]
Thus image cardinalities from the constrained initial population stabilize after one step if and only if \(4\nmid n\); for odd \(n\), no information is lost at any positive time.

For a uniform source \(X\in A_n\) and \(Y_t=\Phi_n^t(X)\), a maximum-posterior exact decoder has error probability zero for odd \(n\), and, for even \(n\) at time one (or at every positive time for \(n\equiv2\pmod4\)),
\[
\boxed{\Pr(\widehat X\ne X)=\frac{2^{n/2}}{L_n},\qquad
H(X\mid Y_t)=\frac{2^{n/2+1}-4+3\log_2 3}{L_n}\ \text{bits}.}
\]
In particular the error probability along even ring lengths is asymptotic to \((\sqrt2/\varphi)^n\), with \(\varphi=(1+\sqrt5)/2\).

## Assumptions and scope
Every word has fixed indexed coordinates; cyclic rotations, reversal and complementation are **not** identified. The no-`11` constraint includes the boundary between last and first coordinates. The Rule-90 update is synchronous and uses both neighbors modulo \(n\); at \(n=2\) they coincide and cancel over \(\mathbb F_2\). Only the starting population is restricted, not the set of allowed intermediate or output states. The zero-size fibers of unattainable words are not included in \(N_{n,t}(k)\) for \(k\ge1\).

## Proof
**1. Kernel of every time iterate.** Identify \(\mathbb F_2^n\) with \(R_n=\mathbb F_2[z]/(z^n-1)\) by its coordinate polynomial. A one-step synchronous update is multiplication by the unit \(z^{-1}\) times \((z+1)^2\); the position convention may reverse the unit shift but does not affect its kernel. Write \(n=2^s u\) with \(u\) odd. Since
\[
z^n-1=(z^u-1)^{2^s}
\]
in characteristic two, and \(z^u-1\) has a simple zero at \(z=1\), the root \(z=1\) has multiplicity exactly \(2^s\) in \(z^n-1\). Multiplication by a polynomial \(f\) in \(R_n\) has kernel dimension \(\deg\gcd(f,z^n-1)\), as follows by dividing \(f\) and \(z^n-1\) by their greatest common divisor. Thus for every \(t\ge1\),
\[
\boxed{\dim_{\mathbb F_2}\ker(\Phi_n^t)=\min(2t,2^s).}
\]
For odd \(n\), this kernel has dimension one and contains the all-ones vector, so it is precisely \(\{0,1^n\}\). For \(n\equiv2\pmod4\), this kernel has dimension two for all \(t\ge1\) and equals the one-step kernel, the four period-two words. Independently, the one-step equation \(x_{i-1}=x_{i+1}\) shows that its kernel is the period-two words for every even \(n\).

**2. Odd-ring injectivity.** If two admissible sources have the same time-\(t\) output on an odd ring, their XOR is either zero or all ones. In the second case the sources are bitwise complements. If both they and their complements avoid cyclic `11`, the original word must avoid both `11` and `00`, forcing strict alternation around an odd cycle, which is impossible. Therefore the sources agree. This works for every \(t\ge1\), not merely for time one.

**3. All even-ring first-step collisions.** Put \(n=2m\), and let \(E\), \(O\) be the disjoint even- and odd-coordinate masks. The one-step kernel is \(\{0,E,O,E\oplus O\}\). Let \(x\in A_n\). If \(x\oplus E\in A_n\), then no odd coordinate can be one in \(x\): otherwise its adjacent even sites are forced zero in \(x\), and toggling them to one creates an adjacent-one pair. Conversely if all odd sites of \(x\) are zero, toggling even sites preserves admissibility. The analogous statement holds with the parities reversed. Finally, both \(x\) and its full complement are admissible exactly when \(x\) is strictly alternating; there are two such sources on an even ring.

Consequently, the three sources \(0,E,O\) form one fiber. Outside these three, there are \(2^m-2\) sources supported on even positions and the same number on odd positions, each class paired with its complement inside that parity. They give \(2^m-2\) double fibers altogether. All other inputs have no second admissible element in their four-element ambient kernel coset, and thus form singleton fibers. Since \(|A_n|=L_n\), the singleton count equals \(L_n-3-2(2^m-2)=L_n-2^{m+1}+1\). Adding fiber counts proves \(|I_{n,1}|=L_n-2^m\). The argument includes \(m=1\).

**4. Count of constrained sources.** The admissible words are independent sets of the indexed cycle, so their number is \(\operatorname{tr}(T^n)\), where \(T=\begin{pmatrix}1&1\\1&0\end{pmatrix}\) records allowed cyclic neighbor pairs. The trace satisfies the Lucas recurrence and has initial values \(2,1\). Hence \(|A_n|=L_n\) for every \(n\ge2\). No large-length enumeration is assumed.

**5. Time-stability and its sharp failure.** When \(n\equiv2\pmod4\), Step 1 gives \(\ker\Phi_n^t=\ker\Phi_n\) for every \(t\ge1\). Two sources therefore have identical outputs at time \(t\) exactly when they do at time one, proving the full stable fiber law. For \(4\mid n\), let \(v\) be the cyclic repetition of `1000` to length \(n\). It belongs to \(A_n\), while \(\Phi_n(v)\ne0\) and \(\Phi_n^2(v)=0=\Phi_n^2(0)\), because \(v\) has period four and \((\Phi_n^2 v)_i=v_{i-2}\oplus v_{i+2}=0\). Thus two distinct first-step outputs coalesce at the second step, making the image cardinality strictly smaller. Since images of any deterministic map cannot increase upon further iteration, first-step stabilization is impossible when \(4\mid n\).

**6. Decoding and entropy.** Given a uniform source on a set of size \(L_n\), each nonempty output fiber of size \(k\) has total probability \(k/L_n\) and conditional uniform distribution on its members. MAP correct-decoding probability is the number of distinct outputs divided by \(L_n\). Conditional entropy is \(L_n^{-1}\sum_{k\ge1}kN_{n,t}(k)\log_2 k\). Substituting Step 3 gives the stated expressions. The usual Binet formula \(L_n=\varphi^n+(-\varphi)^{-n}\) establishes the even-length asymptotic.

## Verification
Run the complete standalone Python standard-library program `CHECK.py`. It enumerates every indexed binary state for \(2\le n\le16\), cross-checks two separately implemented Rule-90 update routines, restricts source fibers to cyclic no-`11` words, and compares every nonempty one-step fiber size against the stated formula. It additionally checks times two, three and five at every \(n\) not divisible by four, and verifies the explicit strict-collapse witness at time two for every tested multiple of four. The program prints `VERIFY_OK` on success. These checks support the proof but are not substitutes for the unlimited-\(n,t\) polynomial kernel argument.

## Relationship to prior work
Classical additive cellular-automaton algebra gives the full-state one-step kernel and the unrestricted two-versus-four predecessor law for cyclic Rule 90; it does not impose the independent-set input language [1]. The cycle-independent-set language and Lucas cardinalities are standard [2,3]. A related full XOR difference profile for **linear** Fibonacci-cube words is available in [4] but explicitly excludes the cyclic Lucas cube, as well as any Rule-90 time-iterate conclusion. Existing Rule-90 necklace-inversion work [5] quotients all binary configurations by rotations, rather than restricting indexed inputs to a forbidden-factor language. The present claim combines the cyclic constraint with time-dependent kernel cosets and determines each nonempty constrained fiber, including exact lossless-time behavior. Source comparison is bounded; no proof of global priority is asserted.

## Limitations
This theorem does not determine the complete fiber distribution at time two or later on lengths divisible by four, nor does it prove noise robustness, performance for unconstrained inputs, or any property of a different update rule. The finite checker cannot certify the general polynomial identity. The 2004 Rule-90 source has a year-resolved publication statement but no verified exact first-public day; the earliest **day-verified** cited public antecedent is the 2009 arXiv record [3]. Independent review and exhaustive historical priority assessment have not been performed.

## References
1. N. R. Miller and M. J. Bardzell, *The Evolution Homomorphism and Permutation Actions on Group Generated Cellular Automata*, Complex Systems **15** (2004), 121–136, especially Section 3 and Corollaries 3–5. https://content.wolfram.com/uploads/sites/13/2018/02/15-2-2.pdf
2. M. Mollard, *Maximal hypercubes in Fibonacci and Lucas cubes*, arXiv:1201.1494 (first submitted 2012-01-06), especially Section 1 and Proposition 2.6. https://arxiv.org/abs/1201.1494
3. S. Cabello, D. Eppstein and S. Klavžar, *The Fibonacci dimension of a graph*, arXiv:0903.2507 (first submitted 2009-03-13), background on Fibonacci-cube constraints. https://arxiv.org/abs/0903.2507
4. *Exact XOR representation profile and fourth Walsh moment of Fibonacci cubes*, accessible published research record (2026-11-16), especially its explicitly path-only scope. https://github.com/published-finding corpus/2026/blob/main/2026/11/16/SCOPE-exact-xor-representation-profile-and-fourth-walsh-moment-of-fibo--04d47201df94/RESULT.md
5. *The four-valued predecessor law for cyclic Rule 90 necklaces*, accessible published research record (2026-11-08), especially its labeled-fiber and necklace-quotient scope. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-four-valued-predecessor-law-for-cyclic-rule-90-necklaces--1b4786197dbc/RESULT.md
