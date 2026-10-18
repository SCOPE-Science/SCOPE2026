# The sharp sixth moment of the first dyadic Fourier resonance

## Finding
Let \(\mathbb T=\mathbb R/\mathbb Z\) carry probability Haar measure. For all \(a,b,c\in\mathbb C\), put
\[
F(x)=a+b e^{2\pi i x}+c e^{6\pi i x}.
\]
Equivalently, multiplying by a character, this is the three-term dyadic-frequency packet \(\{1,2,4\}\). There is a sharp constant \(M\) such that
\[
\int_{\mathbb T}|F(x)|^6\,dx\leq M\bigl(|a|^2+|b|^2+|c|^2\bigr)^3.
\]
It is specified exactly as follows. For positive \(A,B,C\) with \(A+B+C=1\), define
\[
P(A,B,C)=6-9(A^2+B^2+C^2)+4(A^3+B^3+C^3)+6AB^{3/2}C^{1/2}.
\]
There is exactly one solution \((A_*,B_*,C_*)\) of the two equations
\[
(C-A)(6+12B)+3B\sqrt{B/C}(2C-A)=0,
\]
\[
(C-B)(6+12A)+3A\sqrt{B/C}(3C-B)=0
\]
in the region \(A,B,C\in(1/5,1/2)\), \(A+B+C=1\). The exact constant is \(M=P(A_*,B_*,C_*)\), with certified bounds
\[
3.67669<M<3.67670.
\]
The normalized maximizing squared magnitudes are approximately
\[
(A_*,B_*,C_*)=(0.3342204971814,\ 0.3628166057269,\ 0.3029628970917).
\]
Every nonzero equality case is, for some \(\lambda\in\mathbb C\setminus\{0\}\) and \(\theta\in\mathbb R\), exactly
\[
(a,b,c)=\lambda\bigl(\sqrt{A_*},\sqrt{B_*}e^{i\theta},\sqrt{C_*}e^{3i\theta}\bigr).
\]
In particular, equal magnitudes do **not** maximize this sixth moment: the equal-magnitude value is \(11/3\), strictly below \(M\). This is the first dyadic three-frequency packet with a nontrivial triple-sum collision.

## Assumptions and scope
The inequality concerns arbitrary complex coefficients, not only unimodular coefficients. The integral is over the continuous circle with normalized measure, so no modular aliasing of frequencies is allowed. The \(L^2\) norm satisfies \(\|F\|_2^2=|a|^2+|b|^2+|c|^2\). The result is invariant under common coefficient multiplication and translation of the circle variable. It is not a statement about discrete sampling on the seventh roots of unity or about all longer dyadic blocks.

## Proof
Normalize \(|a|^2+|b|^2+|c|^2=1\), excluding the zero polynomial. In the cubic convolution of the frequency set \(\{0,1,3\}\), the sole distinct unordered triples with equal sum are \((0,0,3)\) and \((1,1,1)\). Their multinomial coefficients are respectively \(3\) and \(1\). Orthogonality therefore gives the exact identity
\[
\begin{aligned}
\|F\|_6^6={}&\sum_{j=1}^3 X_j^3+9\sum_{j\ne k}X_j^2X_k+36X_1X_2X_3\\
&+6\operatorname{Re}(a^2c\overline b^{\,3}),
\end{aligned}
\]
where \((X_1,X_2,X_3)=(|a|^2,|b|^2,|c|^2)\). The first three terms reduce, under \(\sum X_j=1\), to \(6-9\sum X_j^2+4\sum X_j^3\). Consequently \(\|F\|_6^6\leq P(A,B,C)\), with equality for positive magnitudes if and only if
\[
2\arg a+\arg c-3\arg b\equiv0\pmod{2\pi}.
\]

To locate the global magnitude optimum, observe that \(6AB^{3/2}C^{1/2}\leq1/(2\sqrt3)<3/10\) by weighted arithmetic–geometric mean. For any fixed one of \(A,B,C\), call it \(x\), the sum of the other two squares and cubes is maximized in the displayed base polynomial when the other two variables are equal. Indeed, if their sum is \(u=1-x\) and their product is \(v\), the base polynomial has coefficient \(18-12u>0\) on \(v\), and \(v\leq u^2/4\). Hence the base is at most
\[
Q(x)=3x^3-\frac{21}{2}x^2+6x+\frac52.
\]
Because \(Q'(x)=3(x-2)(3x-1)\), if some magnitude square is at most \(1/5\) then \(P\leq Q(1/5)+3/10=413/125+3/10<11/3\); if some magnitude square is at least \(1/2\), then \(P\leq Q(1/2)+3/10=13/4+3/10<11/3\). But at \((1/3,1/3,1/3)\), the value is exactly \(11/3\). Thus every maximizer lies in the interior of the convex region \(K=\{A,B,C\in[1/5,1/2], A+B+C=1\}\).

Set \(C=1-A-B\), \(t=\sqrt{B/C}\), and write \(H\) for the \(2\)-by-\(2\) Hessian of \(P(A,B,1-A-B)\). Direct differentiation gives
\[
\begin{aligned}
H_{11}&=-12-24B-6Bt-\tfrac32 At^3,\\
H_{12}&=-18+24C+t(9C-3B-\tfrac92 A)-\tfrac32 At^3,\\
H_{22}&=-12-24A+\tfrac92 A/t-9At-\tfrac32 At^3.
\end{aligned}
\]
The standalone script `verify_lacunary.py` uses exact rational interval arithmetic to cover **the whole region** \(K\) with 51 intersecting rectangles of mesh \(1/20\), enclosing \(t\) on each rectangle by exact integer-square-root bounds. In every rectangle it proves \(-H-I_2\) positive definite: the two diagonal intervals have strictly positive lower endpoints and the determinant interval has lower endpoint greater than \(180\). Thus \(H\preceq-I_2\) everywhere on \(K\); strict concavity follows on the continuum, not just on grid nodes. Compactness gives existence of a maximum, the preceding boundary argument places it in the interior, and strict concavity gives one and only one stationary point. Differentiating \(P\) gives the two equations in the finding, completing the exact characterization.

For a rational point \((A_0,B_0)=(3342205/10^7,3628166/10^7)\), the same script encloses \(P(A_0,B_0)\) and the two gradient components by exact rational square-root bounds. Strong concavity yields
\[
P(A_0,B_0)\leq M\leq P(A_0,B_0)+\tfrac12\|\nabla P(A_0,B_0)\|_2^2.
\]
The resulting rational enclosure lies strictly between \(367669/100000\) and \(367670/100000\). Finally, all optimizing magnitudes are nonzero, and the unique cosine alignment is exactly the phase family in the finding. At equal magnitudes, the first stationarity derivative is positive, so \(M>11/3\), as asserted.

## Verification
Run `python3 verify_lacunary.py` using Python's standard library. Its checks independently enumerate every cubic frequency sum; establish all 51 rational interval Hessian certificates on a continuum; and produce a rational sharp-constant enclosure using a certified strong-concavity remainder bound. Expected terminal marker: `VERIFY_OK`. The finite enumeration is not used as a substitute for the analytic orthogonality argument. The continuum Hessian step is backed by rational interval bounds, not floating-point samples.

## Relationship to prior work
Even-exponent Hardy–Littlewood majorization gives the reduction to coefficient magnitudes, but it does not give their optimizing unequal values. Krenedits studies the same frequencies \(\{0,1,3\}\), particularly the signed unimodular trinomials, for **non-even** exponents; the present sharp arbitrary-magnitude sixth moment is not one of those results. Aistleitner–Berkes–Tichy analyze lacunary series and their Diophantine relations in asymptotic probabilistic questions, not this finite sharp coefficient optimization. A separately published three-frequency even-moment resonance formula treats **unimodular** coefficients and explicitly leaves non-unimodular magnitude optimization outside its scope. The present result fills that specific gap at the first dyadic resonance. The sharp sixth-moment computation on \(\{0,1,3\}\subset\mathbb Z/7\mathbb Z\) is a distinct modular problem with additional aliasing and does not imply the continuous-circle constant here.

## Limitations
Only the first nontrivial dyadic three-frequency packet and exponent six are classified. No sharp constant for longer dyadic packets or other exponents is claimed. The exact constant is defined implicitly by a unique algebraic stationary system plus a certified rational enclosure, rather than by radicals. The argument establishes mathematical correctness of this statement, not absolute historical priority; an older exact norm computation under another notation could cover it.

## References
1. Sándor Krenedits, *Three-term idempotent counterexamples in the Hardy–Littlewood majorant problem*, arXiv:1006.0409v1, first public 2010-06-02. Full text: https://arxiv.org/html/1006.0409v3.
2. Christoph Aistleitner, István Berkes and Robert Tichy, *Lacunary sequences and permutations*, arXiv:1312.0666v1, first public 2013-12-03. Full text: https://arxiv.org/html/1312.0666v2.
3. *Even phase moments recover the normalized geometry of a three-frequency spectrum*, published research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-even-phase-moments-recover-the-normalized-geometry-of-a-three-fr--7849dda51c79; full `RESULT.md` compared for the precise unimodular scope.
