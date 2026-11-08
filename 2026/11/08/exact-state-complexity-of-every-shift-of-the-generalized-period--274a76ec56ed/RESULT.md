# Exact state complexity of every shift of the generalized period-doubling word

## Finding

For each integer \(m\ge 2\), let \(P_m\) be the infinite word on \(\{0,\ldots,m-1\}\) fixed by the substitution \(\mu_m(a)=0\,(a+1\bmod m)\), beginning in \(0\). For every shift \(c\ge0\), define \(P_{m,c}(n)=P_m(n+c)\) for \(n\ge0\). The minimum number of states in a deterministic finite automaton with output (DFAO) which computes \(P_{m,c}(n)\) from the base-two digits of \(n\) **least significant digit first** is exactly

\[
\boxed{\operatorname{sc}_{\mathrm{LSD}}(P_{m,c})=\lceil\log_2(c+1)\rceil+2m.}
\]

This is the same as the exact number of distinct subsequences in the binary \(2\)-kernel of \(P_{m,c}\):

\[
\bigl|\{(P_{m,c}(2^e n+r))_{n\ge0}:e\ge0,\ 0\le r<2^e\}\bigr|=\lceil\log_2(c+1)\rceil+2m.
\]

In particular the binary case has exactly \(\lceil\log_2(c+1)\rceil+4\) states, and the complexity depends only on the binary length of \(c\), not its bit pattern. A complete minimal DFAO is described explicitly below.

## Assumptions and scope

All indices start at zero; \(m\) is any integer at least two; \(c\) is any nonnegative integer. \(\nu_2(t)\) denotes the exponent of two dividing a **positive** integer \(t\). A binary digit string \(b_0b_1\cdots b_{e-1}\), read least significant digit first, represents \(\sum_{i=0}^{e-1}b_i2^i\). The empty string represents zero. Appending any number of zeros does not change the represented integer. DFAO correctness is required for **all** strings, including redundant leading zeros in conventional most-significant-digit notation, which are trailing zeros in this least-significant-digit convention. No claim is made about most-significant-digit-first state complexity.

A residual after reading a finite digit prefix \(b_0\cdots b_{e-1}\) is the function of a further digit-string value \(n\) defined by \(P_{m,c}(r+2^e n)\), where \(r=\sum_{i<e}b_i2^i\). The minimal DFAO has as many states as there are distinct such residual functions: equal residuals are indistinguishable by every continuation, and distinct residuals require distinct states.

## Proof

**1. Arithmetic form of the fixed point.** Since \(\mu_m(a)\) has first letter zero and second letter \(a+1\bmod m\), the fixed point obeys \(P_m(2n)=0\) and \(P_m(2n+1)=P_m(n)+1\bmod m\). These are precisely the recurrences for the \(2\)-adic valuation of \(n+1\): if \(n=2j\), \(\nu_2(n+1)=0\), and if \(n=2j+1\), \(\nu_2(n+1)=1+\nu_2(j+1)\). Thus induction gives

\[
P_{m,c}(n)=\nu_2(n+c+1)\bmod m\quad(n\ge0).
\]

Put \(T=c+1\ge1\). For \(q\ge1\) and \(\epsilon\in\mathbb Z/m\mathbb Z\), write

\[
G_{q,\epsilon}(n)=(\nu_2(n+q)+\epsilon)\bmod m,
\]

and for \(j\in\mathbb Z/m\mathbb Z\) let \(C_j(n)=j\) be the constant sequence. The initial residual is \(G_{T,0}\).

**2. Exact residual transitions.** Reading the next low-order bit \(b\in\{0,1\}\) transforms a residual function \(F\) into \(n\mapsto F(2n+b)\). For any \(G_{q,\epsilon}\): if \(q+b\) is odd, then \(2n+q+b\) is always odd, and the new residual is \(C_\epsilon\). If \(q+b\) is even, then

\[
G_{q,\epsilon}(2n+b)=G_{(q+b)/2,\epsilon+1}(n).
\]

Every \(C_j\) stays fixed on both input bits. Hence these rules specify a complete DFAO if only finitely many such \(G\)-states are reachable, with output \(G_{q,\epsilon}(0)=(\nu_2(q)+\epsilon)\bmod m\) and \(C_j(0)=j\).

**3. Exact set of reachable states.** After reading \(e\) bits with numerical value \(r\) in \(0\le r<2^e\), the residual sequence is

\[
F_{e,r}(n)=\nu_2(2^en+r+T)\bmod m.
\]

Unless \(r+T\) is divisible by \(2^e\), the valuation \(\nu_2(2^en+r+T)\) is independent of \(n\), so \(F_{e,r}\) is constant. There is exactly one residue \(r_e\) in the range satisfying \(r_e\equiv-T\pmod{2^e}\). For it, \(T+r_e=2^e q_e\), with

\[
q_e=\left\lceil\frac{T}{2^e}\right\rceil,
\qquad F_{e,r_e}=G_{q_e,e\bmod m}.
\]

Let \(k=\lceil\log_2 T\rceil\). The successive \(q_e\) for \(e=0,\ldots,k-1\) are all strictly decreasing positive integers greater than one; for every \(e\ge k\), \(q_e=1\). Thus exactly \(k\) possible nonconstant residuals have \(q>1\), and beyond them there are precisely the \(m\) states \(G_{1,\epsilon}\), as \(e\) varies through \(k,k+1,\ldots\) modulo \(m\). All of these are reached by the unique prefixes \(r_e\). Furthermore, from \(G_{1,\epsilon}\), reading zero yields \(C_\epsilon\), so all \(m\) constants occur. Therefore the number of reachable residual functions is at most \(k+2m\), and all listed states are indeed reachable.

**4. Pairwise inequivalence.** The \(m\) constants are distinct. Every \(G_{q,\epsilon}\) is nonconstant: for each sufficiently large \(H\), substituting \(n=2^H-q\ge0\) gives \(G_{q,\epsilon}(n)=H+\epsilon\bmod m\), which takes all \(m\ge2\) values as \(H\) varies. If two states have the same \(q\) but distinct phases, they disagree on every input \(n\). If \(q\ne q'\), set \(d=q'-q\ne0\) and choose \(H>\nu_2(|d|)\) large enough that \(2^H-q\ge0\). At \(n=2^H-q\), one state has value \(H+\epsilon\bmod m\); the other has the fixed value \(\nu_2(|d|)+\epsilon'\bmod m\), because \(\nu_2(2^H+d)=\nu_2(|d|)\). Varying \(H\) modulo \(m\) separates them. Thus no two reachable residual functions coincide.

**5. Minimality and padding.** Each distinct residual needs a distinct automaton state by the standard residual distinguishability argument. The transition rules in step 2 realize exactly those states and compute the correct final output. Because the computation is a function only of the represented nonnegative integer, appended zero digits leave outputs unchanged. The minimum state number, and hence the exact binary \(2\)-kernel size, is \(k+2m\). This proves the asserted formulas for every \(m\ge2\) and \(c\ge0\). \(\square\)

## Verification

The standalone script `verify_shift_dfa.py` builds the reachable residual machine from the explicit transition rules, minimizes it by iterative output/transition partition refinement without assuming the predicted count, and compares output against direct \(2\)-adic valuations. It checked all \(8\times256=2048\) choices \(2\le m\le9\), \(0\le c\le255\), and \(80\) inputs for each, including padded representations; in addition, it compared the first \(8192\) substitution symbols against valuations for eight alphabet sizes. Its output was:

`PASS: 2048 shift/modulus automata; 163840 numerical input checks; 8192-symbol fixed-point checks for 8 alphabet sizes`

The infinite theorem rests on the proof above, not on exhaustion of finite data. For reproduction run `python3 verify_shift_dfa.py` beside this file; Python standard library only.

## Relationship to prior work

Bognini and Ammar (first public version November 25, 2025) study the same \(m\)-letter period-doubling substitution and its kernel-word and gap factorizations. Their structural factorization does not furnish a shifted binary DFAO count. Moradi, Popoli, Shallit and Vukusic (March 19, 2026) study state complexity under shifts for the **Fibonacci word in Zeckendorf representation**, giving an exact formula for Fibonacci LSD-first state complexity (Theorem 3.2) and logarithmic bounds in the MSD-first case. Their general base-\(b\) transducer observation supplies upper bounds for a shifted automatic sequence, but no exact count for these valuation-based generalized period-doubling words. The 2021 work of Charlier, Cisternino and Massuir concerns multiplying and translating the **Thue–Morse set**, not a shifted period-doubling word. In particular none of these results by statement alone implies the exact formula or the fully distinguished residual family above. Related accessible indexed mathematical records on period-doubling attractors and lifts also concern different invariants.

## Limitations

Only least-significant-digit-first, base-two DFAOs with all representations allowed are considered. No bound for most-significant-digit-first automata, arbitrary base, non-cyclic label substitutions, or arbitrary automatic words is asserted. Full historical priority remains subject to literature not found by the recorded searches. The verification is finite and not independent mathematical certification.

## References

1. K. Ernest Bognini and H. Ammar, *A new factorization of the generalized period-doubling sequences through kernel words and gaps sequences*, arXiv:2511.20881v1 (first public November 25, 2025), https://arxiv.org/abs/2511.20881 .
2. D. Moradi, P. Popoli, J. Shallit, and I. Vukusic, *State Complexity of Shifts of the Fibonacci Word*, arXiv:2603.18858v1 (first public March 19, 2026), https://arxiv.org/html/2603.18858v1 .
3. E. Charlier, C. Cisternino, and A. Massuir, *Minimal automaton for multiplying and translating the Thue-Morse set*, Electron. J. Combin. 28 (2021), P3.12, https://doi.org/10.37236/9068 .
