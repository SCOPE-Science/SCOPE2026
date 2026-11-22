# Complete modulo-nine residue spectra of central trinomial coefficients and sharp ternary-block bias

## Finding
For every integer \(n\ge0\), put \(T_n=[x^0](x^{-1}+1+x)^n\). Read the ordinary ternary expansion \(w(n)\) from most significant to least significant digit, taking \(w(0)=0\), and let \(d_{10}(n)\) be the number of adjacent occurrences of the word \(10\). The following is a **complete residue classification modulo nine**.

1. If \(w(n)\) contains no \(2\), then \(T_n\equiv1+6d_{10}(n)\pmod9\).
2. If \(w(n)\) contains at least two digits \(2\), then \(T_n\equiv0\pmod9\).
3. Otherwise, let the unique \(2\) have preceding digit \(p\in\{0,1\}\), with a virtual initial \(0\) when the \(2\) is first. If this \(2\) is terminal, \(T_n\equiv3\pmod9\) for \(p=0\) and \(T_n\equiv6\pmod9\) for \(p=1\). If at least one digit follows the \(2\), \(T_n\equiv6\pmod9\) for \(p=0\) and \(T_n\equiv0\pmod9\) for \(p=1\).

For every integer \(L\ge0\) and residue \(r\in\{0,1,\ldots,8\}\), write \(N_r(L)=\#\{0\le n<3^L:T_n\equiv r\pmod9\}\). For \(L\ge2\), the entire histogram is
\[
\begin{aligned}
N_0(L)&=3^L-(L+6)2^{L-2},\\
N_3(L)&=2^{L-2},\\
N_6(L)&=(L+1)2^{L-2},\\
N_{1+6s\bmod9}(L)&=\sum_{\substack{j\ge0\\j\equiv s\pmod3}}\binom{L+1}{2j+1}\quad(s=0,1,2),\\
N_2(L)&=N_5(L)=N_8(L)=0.
\end{aligned}
\]
For \(L=0\), only \(N_1(0)=1\) is nonzero. For \(L=1\), \(N_1(1)=2\), \(N_3(1)=1\), and all others vanish. The formula for \(N_0(L)\) alone was established earlier; the new content is the remaining full residue classification, associated exact counts, and the following optimal bias law.

The three classes congruent to one modulo three are asymptotically balanced on the ternary Cantor support, but have a **sharp exponential discrepancy**:
\[
\boxed{\max_{r\in\{1,4,7\}}\left|N_r(L)-\frac{2^L}{3}\right|=\Theta(3^{L/2})\qquad(L\to\infty).}
\]

## Assumptions and scope
All integer ranges and residues are quantified above. Leading zeros are harmless: the digit word \(10\) is unaffected by prepending zeros, and a unique initial \(2\) has virtual predecessor \(0\). No claims are made about moduli other than nine or arbitrary real cutoffs. The term \(\Theta\) asserts two positive absolute bounding constants for all sufficiently large integer \(L\). This is a classification by exact residues, not a claim that the basic divisibility-by-nine test is new.

## Proof
**1. Exact ternary recurrences.** Let \(A(x)=x^{-1}+1+x\). The identity
\[
A(x)^3=A(x^3)+3\bigl(x^{-2}+2x^{-1}+2+2x+x^2\bigr)
\]
holds over the integers. Expanding \(A(x)^{3m+r}\), taking constant coefficients and discarding terms with at least two factors of \(3\) modulo nine gives, for every integer \(m\ge1\),
\[
\begin{aligned}
T_{3m}&\equiv T_m+6mT_{m-1},\\
T_{3m+1}&\equiv T_m+3m(T_m-T_{m-1}),\\
T_{3m+2}&\equiv3(m+1)T_m\pmod9.
\end{aligned}
\tag{1}
\]
For completeness, if \(c_j=[x^j]A(x)^{m-1}\), the three correction constant coefficients are \(2T_{m-1}\), \(6T_{m-1}+2c_1\), and \(16T_{m-1}+8c_1\), respectively; \(2c_1=T_m-T_{m-1}\). Substitution yields the displayed recurrences, with the second using \(5\equiv-1\pmod3\) after extracting its factor \(3m\). For \(m=0\), the initial values \(T_0=T_1=1\), \(T_2=3\) give the same formulas whenever the coefficient of \(T_{-1}\) is read as zero.

Modulo three, (1) yields \(T_{3m}\equiv T_{3m+1}\equiv T_m\) and \(T_{3m+2}\equiv0\). Starting at \(T_0=1\) this proves the binary-support criterion:
\[
T_m\equiv \begin{cases}1\pmod3,&\text{if the ternary expansion contains no digit }2,\\0\pmod3,&\text{otherwise.}\end{cases}
\tag{2}
\]

**2. Residues with no digit two.** Start at prefix \(0\), with \(T_0=1\). Whenever a digit \(0\) or \(1\) is appended to a prefix \(m\) using only these digits, (1) changes the value modulo nine only when the new digit is \(0\) and the old last digit is \(1\). Indeed, the digit \(1\) recurrence has correction \(3m(T_m-T_{m-1})\), which vanishes modulo nine when \(m\equiv1\pmod3\) (both values are \(1\pmod3\)) or \(m\equiv0\pmod3\) (factor \(3m\) is divisible by nine). The digit \(0\) recurrence changes the residue by \(6\pmod9\) exactly when \(m\equiv1\pmod3\), because then \(T_{m-1}\equiv1\pmod3\); otherwise it has zero correction. Each occurrence of \(10\) hence adds six, proving clause 1.

**3. Residues with one or more digits two.** When the first digit \(2\) is appended to a prefix \(m\) with no digit \(2\), (1) and (2) give \(T_{3m+2}\equiv3(m+1)\pmod9\). The preceding digit of the new \(2\) is precisely \(m\bmod3\), taking \(m=0\) for an initial \(2\); hence this residue is \(3\) if the predecessor is \(0\) and \(6\) if it is \(1\). Appending its first subsequent \(0\) or \(1\) adds \(3\pmod9\): the old prefix \(u\) ends in \(2\), so \(u\equiv2\pmod3\), \(T_u\equiv0\pmod3\), and \(T_{u-1}\equiv1\pmod3\). All further \(0\) or \(1\) digits have zero correction because a digit \(2\) then survives in the upper digits of both relevant arguments (or the old prefix is divisible by three). A second digit \(2\) gives \(3(m+1)T_m\equiv0\pmod9\) by (2), and zero thereafter remains zero under all three recurrences. This proves clauses 2 and 3.

**4. Exact ternary-power histogram.** Consider all padded length-\(L\) ternary words. Among words avoiding \(2\), define \(d\) as their number of \(10\) boundaries. Adjoin a fixed sentinel \(0\) before the word and a fixed sentinel \(1\) after it. The resulting \(L+1\) boundary positions have exactly \(2d+1\) transitions, since every \(10\) is paired with a \(01\) except for one extra \(01\) forced by the endpoint values. Conversely, choosing any \(2d+1\) transition boundaries uniquely determines the word. Therefore precisely \(\binom{L+1}{2d+1}\) words have \(d\) descents, proving the formula for all three unit residues.

Among words with exactly one digit \(2\), position-by-position counting gives \(N_3(L)=2^{L-2}\) for the terminal \(2\) preceded by \(0\); \(N_6(L)=(L+1)2^{L-2}\) from terminal \(2\) preceded by \(1\), or nonterminal \(2\) preceded by \(0\). For the exceptional zero residue, the unique \(2\) must be nonterminal and preceded by \(1\), giving \((L-2)2^{L-2}\) words; the words with two or more digits \(2\) number \(3^L-2^L-L2^{L-1}\). Summing yields \(N_0(L)=3^L-(L+6)2^{L-2}\), agreeing with the previously established divisibility-only census. The boundary lengths are read from \(T_0,T_1,T_2\).

**5. Sharpness of unit-class balance.** Let \(\omega=e^{2\pi i/3}\) and define
\[
F_L(t)=\sum_{d\ge0}\binom{L+1}{2d+1}t^d=\frac{(1+\sqrt{t})^{L+1}-(1-\sqrt{t})^{L+1}}{2\sqrt{t}},
\]
where the right-hand expression is a polynomial and independent of the square-root branch. Set \(\sqrt{\omega}=e^{i\pi/3}\). Then
\[
F_L(\omega)=\frac12\left(3^{(L+1)/2}e^{i(L-1)\pi/6}-e^{-i(L+2)\pi/3}\right),
\]
so \(|F_L(\omega)|=\Theta(3^{L/2})\), by the triangle and reverse-triangle inequalities. Fourier inversion on three residue classes and \(F_L(1)=2^L\) show
\[
\sum_{s=0}^2\left(N_{1+6s\bmod9}(L)-\frac{2^L}{3}\right)^2=\frac23|F_L(\omega)|^2.
\]
The maximum of three absolute values is between their root-mean-square and their Euclidean norm, proving matching upper and lower bounds of order \(3^{L/2}\) for all sufficiently large \(L\). \(\square\)

## Verification
A standalone standard-library Python checker, `verify_trinomial_residues9.py`, computes the first \(3^8=6561\) terms by the independent exact integer recurrence \((n+1)T_{n+1}=(2n+1)T_n+3nT_{n-1}\). It checks every residue against the digit classification and recomputes all nine residue histograms for \(0\le L\le8\). The executed result was `VERIFY_OK exact_terms=6561 block_censuses=0..8 digit_formula=PASS`. This is bounded evidence; the infinite assertions follow from the proved identities and root-of-unity argument.

## Relationship to prior work
A prior published result, *An exact ternary-language criterion for nine dividing central trinomial numbers* (2026), establishes the language for the zero class and the exact formula \(N_0(L)=3^L-(L+6)2^{L-2}\). Its proof also supplies congruence recurrences equivalent to (1); these ingredients are credited, and neither the zero criterion nor the recurrence is presented as new here. The present contribution distinguishes all five nonzero classes actually attained, gives every exact class count and establishes the sharp \(3^{L/2}\) nonuniformity on the ternary Cantor support. Mikić (2023) studies related divisibilities of generalized central trinomial numbers and exact valuations of central Delannoy numbers, but not these complete ordinary residue frequencies. Beukers (2022), Kohen (2025) and Rowland–Yassawi (2014) give general prime-power automaton and recurrence methods and a central-trinomial example modulo four; algorithmic computability by those methods does not assert this explicit modulo-nine classification or sharp discrepancy.

## Limitations
These statements concern modulus nine, not higher powers of three; the bias estimate applies to complete ternary-power blocks, not all arbitrary cutoffs. The count for residue zero is previously published. Generic automatic congruence methods may implicitly entail the result after additional computation, and an unindexed explicit classification could affect bibliographic priority. The claim has undergone internal self-review only; no independent audit is represented.

## References
1. J. Mikić, *On new divisibility properties of generalized central trinomial coefficients and Legendre polynomials*, arXiv:2311.14623 (first public version 2023-11-24), especially definition (9) and main theorems.
2. F. Beukers, *p-Linear schemes for sequences modulo p^r*, arXiv:2211.15240 (2022), Theorem 1.4 and Corollary 1.5.
3. E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635 (2013/2014), Section 4.2.
4. N. Kohen, *A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence*, arXiv:2503.21988 (2025), Section 5, Theorem 20.
5. N. Rampersad and J. Shallit, *Congruence Properties of Combinatorial Sequences via Walnut and the Rowland–Yassawi–Zeilberger Automaton*, arXiv:2110.06244 (2021), Section 3.
6. *An exact ternary-language criterion for nine dividing central trinomial numbers*, published-finding corpus (2026): https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-an-exact-ternary-language-criterion-for-nine-dividing-central-tr--f302476becb1/RESULT.md
7. OEIS A002426, central trinomial numbers: https://oeis.org/A002426
