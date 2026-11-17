# Exact one-sweep image entropy of sequential Rule 110

## Finding

Consider the binary elementary cellular automaton Rule 110 on a **labelled cyclic ring**, with each site updated exactly once in the in-place order \(0,1,\ldots,n-1\). Write \(I_n\) for the number of *distinct* resulting words, not for the number of input words. For every integer \(n\ge3\),

\[
\boxed{\sum_{n\ge3}I_nz^n=\frac{z^3(5+z-7z^2-2z^3+4z^4)}{(1-z)(1-z-2z^2+z^4)}.}
\]

An explicit deterministic 26-state endpoint automaton gives a necessary-and-sufficient reachability test and reconstructs at least one predecessor of each reachable word. The count begins
\[
(I_3,\ldots,I_{16})=(5,11,20,39,75,143,274,522,996,1898,3617,6892,13131,25018).
\]

If \(\rho\) is the unique root of \(1-z-2z^2+z^4\) in \((0.524888,0.524889)\), the growth base is \(\lambda=1/\rho=1.905166167754\ldots\), and
\[
I_n\sim0.830504279677\ldots\,\lambda^n,
\qquad \lim_{n\to\infty}\frac{\log_2 I_n}{n}=0.929916834432\ldots.
\]

For comparison, the *simultaneous-update* Rule 110 image has known entropy approximately \(0.9238561093\) bits per site, strictly smaller. The two image populations are not identical even at finite size: at length four they are \(11\) and \(10\), respectively, whereas at length five they are \(20\) and \(22\). This difference is about **update order**, not about Turing universality of sequential Rule 110.

## Assumptions and scope

All bits are in \(\{0,1\}\), all subscripts are modulo \(n\), and output words are position-labelled (not necklaces). Rule 110 is the map
\[
f(000)=f(100)=f(111)=0,\qquad f(001)=f(010)=f(011)=f(101)=f(110)=1.
\]

Given the original word \(x=(x_0,\ldots,x_{n-1})\), let \(y\) be its output after the sequential in-place sweep. Then the exact scan equations are
\[
\begin{aligned}
y_0&=f(x_{n-1},x_0,x_1),\\
y_i&=f(y_{i-1},x_i,x_{i+1})&& (1\le i\le n-2),\\
y_{n-1}&=f(y_{n-2},x_{n-1},y_0).
\end{aligned}
\]

The theorem concerns the image after **one full sweep** and makes no claim about temporal recurrence, later sweeps, different update permutations, or synchronous dynamics.

## Proof

**Step 1: exact deterministic recognition of output words.** After reading the first target bit \(b=y_0\), let the candidate set \(S\subseteq\{0,1\}^2\) consist of pairs \((a,c)\) of potential old endpoint values \((x_{n-1},x_1)\) such that \(f(a,d,c)=b\) for at least one old \(x_0=d\). A set \(S\) is encoded as a four-bit mask with bit \(2a+c\) marking the pair \((a,c)\). Store the state \((b,p,S)\), where \(p\) is the most recently read output bit, initially \(p=b\).

For each of the **internal** bits \(w=y_i\), \(1\le i\le n-2\), update deterministically to \((b,w,S')\), with
\[
S'=\{(a,d):\exists c\ ((a,c)\in S\ \text{and}\ f(p,c,d)=w)\}.
\]

After the internal bits, the possible final output bits are exactly
\[
E(b,p,S)=\{f(p,a,b):(a,a)\in S\}.
\]

A target \(y\) is reachable if and only if \(y_{n-1}\in E(b,p,S)\). Following any successful choices backwards through the finite transitions reconstructs the original word. This is a genuine iff: each update transition is just the relevant scan equation with the unobserved old bit existentially eliminated; terminal equality forces the original last bit to agree with the stored endpoint \(a\).

**Step 2: finite deterministic transfer counts distinct targets.** For \(b\in\{0,1\}\), start from the state \((b,b,S_b)\) just defined. Close these two states under the internal transitions labelled \(0\) and \(1\). The complete closure contains **26** distinct states, including empty-mask states. Its breadth-first ordered states, both transitions and the terminal weights \(v_s=|E(s)|\) are given explicitly in `transfer_table.json`. Let \(T\) be the resulting \(26\times26\) integer transition matrix, with \(T_{s,t}\) the number of bit labels sending state \(s\) to state \(t\). Let \(u\) place a unit mass at each of the two initial states. Then
\[
I_n=uT^{n-2}v,\qquad n\ge3.
\]

A read target prefix has exactly one deterministic state trajectory, and the terminal weight counts **distinct** compatible last bits rather than the number of old inputs. Thus this is a distinct-output count, even when the sweep is not injective.

**Step 3: all-length rational identity by an exact finite certificate.** Write \(c_k=uT^kv\) for \(k\ge0\), where \(c_0=4\) is a formal length-two extension used only to initialize the recurrence. Set
\[
Q(z)=(1-z)(1-z-2z^2+z^4)=1-2z-z^2+2z^3+z^4-z^5.
\]

Direct integer operations on the 26-state table show
\[
\sum_{j=0}^{5}[z^j]Q(z)\,c_{k-j}=0
\quad\text{for every }5\le k\le30,
\]

and the first five coefficients of \(Q(z)\sum_{k\ge0}c_kz^k\) are exactly \((4,-3,-3,1,2)\). Crucially, this is an *all-length* certificate, not a numerical extrapolation: for \(k\ge5\), each recurrence residual is \(uT^{k-5}P(T)v\), with \(P(t)=t^5-2t^4-t^3+2t^2+t-1\). By Cayley--Hamilton, the sequence of residuals satisfies the characteristic recurrence of the 26-dimensional matrix \(T\), so the 26 consecutive zeros imply all later residuals are zero. Therefore
\[
\sum_{k\ge0}c_kz^k=\frac{4-3z-3z^2+z^3+2z^4}{Q(z)}.
\]

Subtract the formal length-two term \(4z^2\) from \(z^2\sum c_kz^k\); direct polynomial subtraction gives precisely the boxed generating function for \(n\ge3\). The standalone `proof_transfer.py` reconstructs the table from the eight Rule-110 truth-table entries, checks the 26 residuals exactly, and verifies the polynomial numerator using only Python integer arithmetic.

**Step 4: entropy and asymptotics.** The polynomial \(q(z)=1-z-2z^2+z^4\) is positive at \(0.524888\) and negative at \(0.524889\). It is negative at \(1.49\) and positive at \(1.50\). The derivative \(q'(z)=-1-4z+4z^3\) has exactly one positive zero, which shows that these are its only two positive roots. For negative real \(z=-t\), \(q(-t)=(t^2-1)^2+t>0\), hence there are no negative roots. The other two roots are conjugate and, because the product of all four roots is one, their modulus exceeds \(\sqrt{1/(0.524889\cdot1.50)}>1.12\). Together with the extra denominator root \(z=1\), the unique smallest-modulus pole is \(\rho\). Its numerator does not vanish, and standard rational-function coefficient extraction gives the asymptotic constant \(-N(\rho)/(\rho Q'(\rho))=0.830504279677\ldots\), with \(N(z)=z^3(5+z-7z^2-2z^3+4z^4)\). The displayed entropy follows.

## Verification

`proof_transfer.py` and `transfer_table.json` constitute the exact finite-state recurrence certificate. `independent_forward.py` implements Rule 110 using the independent Boolean expression \(f(l,c,r)=(1-c)r\lor c(1-lr)\), exhaustively enumerates all binary inputs on lengths \(3\) through \(16\), and additionally checks complete target reachability by a separately written predecessor search for lengths \(3\) through \(13\). Both scripts were executed from the package and their standard output is provided in matching text files. These finite experiments corroborate the result; the proof of the infinite family is Step 3.

## Relationship to prior work

Wolfram's original elementary-automata work defines the synchronous model. Cook's computational-universality construction is likewise explicitly synchronous, and does not provide the image enumerator for an in-place sweep. Macauley, McCammond and Mortveit's *Order Independence in Asynchronous Cellular Automata* studies which rules have update-order-independent sets of periodic points, including Rule 110, not the number of one-sweep outputs. Donoso-Leiva, Goles, Ríos-Wilson and Sené prove a different Rule-110 statement (Theorem 16): the all-zero fixed point is isolated under sequential updating, and their paper classifies convergence to fixed points rather than one-sweep image sizes. Two available exact, all-length Rule-110 image enumerations concern **simultaneous** cyclic updates; their generating denominator \((1-z)(1-z-z^4)(1-2z+z^2-z^3-z^4)\) and image counts differ. The present result gives a scan-order-sensitive image language, its exact enumerator and its entropy, without asserting that the general transfer-matrix technique is new.

## Limitations

No result about repeated sequential sweeps, other update orders, minimal automaton size, exact historical priority, or computational universality is asserted. The finite-state recurrence is independently reproducible but has not received external mathematical audit. Available searches and inspected published statements do not prove absolute novelty over every historical source.

## References

1. S. Wolfram, *Statistical mechanics of cellular automata*, Reviews of Modern Physics **55** (1983), 601–644, published 1983-07-01. https://doi.org/10.1103/RevModPhys.55.601
2. M. Macauley, J. McCammond and H. S. Mortveit, *Order Independence in Asynchronous Cellular Automata*, arXiv:0707.2360, first released 2007-07-16. https://arxiv.org/abs/0707.2360
3. M. Cook, *A Concrete View of Rule 110 Computation*, arXiv:0906.3248, first released 2009-06-17. https://arxiv.org/abs/0906.3248
4. I. Donoso-Leiva, E. Goles, M. Ríos-Wilson and S. Sené, *On the Convergence of Elementary Cellular Automata under Sequential Update Modes*, arXiv:2509.07797, first released 2025-09-09. https://arxiv.org/abs/2509.07797
5. *Exact one-step image counts for cyclic elementary cellular automaton Rule 110*, publicly available research record, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-one-step-image-counts-for-cyclic-elementary-cellular-autom--ce660bdc5af3
6. *Exact cyclic one-step image enumeration for cellular automaton Rule 110*, publicly available research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-cyclic-one-step-image-enumeration-for-cellular-automaton-r--cd588ef2be4e
