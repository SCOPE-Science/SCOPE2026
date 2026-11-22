# Fixed-row threshold and staircase laws for labeled chip-firing on the quadrant lattice

## Finding

Let \(C_m(a,b)\), for integers \(m\geq1\) and \(a,b\geq0\), be the nonnegative integer array defined by
\[
C_m(a,0)=m,\qquad C_m(-1,b)=0,\qquad
C_m(a,b)=\left\lfloor\frac{C_m(a,b-1)+C_m(a-1,b)}2\right\rfloor\quad(b\geq1).
\]
The established labeled-chip interpretation of this array is that
\(\mu(a,b)=\min\{m\geq1:C_m(a,b)>0\}\) is the least label that can reach \((a,b)\) on the ordered directed quadrant lattice when arbitrarily many chips may be started at the origin.

Define the explicit degree-\(a\) polynomial
\[
Q_a(b)=2^{-a}\binom{b+a}{a}+\sum_{j=1}^a2^{-j}\binom{b+j-1}{j-1},
\qquad \Lambda_a(b)=2^{-b}Q_a(b),
\]
with the sum empty when \(a=0\).

**Theorem (fixed-row scaling).** For each fixed integer \(a\geq0\) and each fixed \(K>0\), uniformly for positive integers \(m\leq K2^b/b^a\), as \(b\to\infty\),
\[
C_m(a,b)=\left\lfloor m\Lambda_a(b)-R_{m,a,b}\right\rfloor,
\qquad 0\leq R_{m,a,b}=O_{a,K}\!\left(\frac{\log b}{b}\right).
\]
When \(a=0\), take \(R_{m,0,b}=0\), so this identity is exact at every width.
Thus, for any positive integer sequence \(m_b\) with \(m_b\Lambda_a(b)\to t\), where \(t\geq0\) is **not an integer**, eventually
\[
C_{m_b}(a,b)=\lfloor t\rfloor.
\]
In particular, for every fixed \(a\geq0\),
\[
\boxed{\displaystyle
\mu(a,b)=\frac{a!\,2^{b+a}}{b^a}\left(1+O_a\!\left(\frac{\log b}{b}\right)\right)
}\qquad (b\to\infty).
\]
Moreover \(\mu(a+1,b)/\mu(a,b)\sim 2(a+1)/b\) for every fixed \(a\geq0\). The previously known cases \(a=0\) and \(a=1\) are included for consistency; the complete fixed-row law and the cases \(a\geq2\) are the substantive extension.

## Assumptions and scope

The lattice has vertices \((a,b)\in\mathbb Z_{\geq0}^2\) and directed edges to \((a+1,b)\) and \((a,b+1)\). Each legal firing chooses two labeled chips at one vertex and sends the smaller to the first child and the larger to the second. Reachability concerns a chip arriving at a vertex during any finite legal firing sequence; it is not restricted to its final resting vertex. The least reachable label \(\mu(a,b)\) permits arbitrarily many initial chips, so there is no fixed initial budget in the limit.

The recurrence and its reachability interpretation have been established for this ordered firing rule. A directly documented form of the recurrence and its sequence interpretation appears in OEIS A397913; the detailed proof of the optimal consecutive-pairing interpretation appears in Inagaki–Khovanova–Luo (2026, arXiv:2611.25137v1, Theorem 21). The result below derives the new fixed-first-coordinate asymptotics from the stated recurrence. In every limit, the first coordinate \(a\) is fixed and \(b\) tends to infinity. No uniformity for growing \(a\) is claimed.

## Proof

**1. Continuous comparison solution.** Replace each floor by ordinary division and call the resulting array \(L_m(a,b)\), with the same boundary values. At \(a=0\), \(L_m(0,b)=m2^{-b}\). For \(a\geq1\), write \(H_a(z)=\sum_{b\geq0}L_m(a,b)z^b\). Summing the recurrence over \(b\geq1\) gives
\[
(2-z)H_a(z)=H_{a-1}(z)+m,\quad
H_0(z)=\frac{2m}{2-z}.
\]
Iteration and coefficient extraction yield
\[
H_a(z)=m\left(\sum_{j=1}^a(2-z)^{-j}+2(2-z)^{-a-1}\right),
\qquad L_m(a,b)=m2^{-b}Q_a(b).
\]
Consequently, for fixed \(a\),
\[
Q_a(b)=\frac{b^a}{2^aa!}\left(1+O_a(b^{-1})\right)
\]
when \(a\geq1\), and \(Q_0(b)=1\) exactly.

**2. Global rounding error.** Let \(\varepsilon_m(a,b)=L_m(a,b)-C_m(a,b)\). Monotonicity of floor implies nonnegativity by induction. For \(a=0\), \(0\leq\varepsilon_m(0,b)<1\). For \(a\geq1,b\geq1\), subtracting the two recurrences gives
\[
\varepsilon_m(a,b)=\frac{\varepsilon_m(a,b-1)+\varepsilon_m(a-1,b)}2+\delta_{a,b},
\quad \delta_{a,b}\in\{0,1/2\},
\]
and \(\varepsilon_m(a,0)=0\). Double induction thus establishes
\[
0\leq\varepsilon_m(a,b)\leq a+1\quad\text{for every }m,a,b.
\]
This preliminary bound alone does not give the relative asymptotic near the first positive count; the next estimate localizes the influential rounding errors.

**3. Concentrating the floor losses.** Combining all nested floors down a fixed row gives, for \(a\geq1\), the exact identity
\[
C_m(a,b)=\left\lfloor\frac{m+\sum_{r=1}^b2^{r-1}C_m(a-1,r)}{2^b}\right\rfloor.
\]
Indeed, repeatedly use \(\lfloor(\lfloor x\rfloor+k)/2\rfloor=\lfloor(x+k)/2\rfloor\) for integer \(k\). The same identity without the outside floor holds for \(L_m(a,b)\). Therefore
\[
C_m(a,b)=\left\lfloor m\Lambda_a(b)-R_{m,a,b}\right\rfloor,
\quad
R_{m,a,b}=2^{-b}\sum_{r=1}^b2^{r-1}\varepsilon_m(a-1,r)\geq0.
\]
For \(b\geq8\), put \(h=\lceil2\log_2 b\rceil\). In the terms \(r\leq b-h\), the uniform bound \(\varepsilon_m(a-1,r)\leq a\) shows that the contribution is at most \(a2^{-h}\). In the remaining at most \(h\) terms, use \(\varepsilon_m(a-1,r)\leq L_m(a-1,r)=m2^{-r}Q_{a-1}(r)\). Since \(Q_{a-1}(r)\leq c_a(b+1)^{a-1}\) throughout \(r\leq b\) for a constant \(c_a\), the latter contribution is at most
\[
\frac{c_a m h(b+1)^{a-1}}{2^{b+1}}.
\]
If \(m\leq K2^b/b^a\), these two terms are \(O_{a,K}((\log b)/b)\). This proves the claimed uniform estimate, including the case \(a=1\) and, separately, the exact case \(a=0\).

**4. Scaling and first-positive thresholds.** If \(m_b\Lambda_a(b)\to t\notin\mathbb Z\), then \(m_b=O_a(2^b/b^a)\), so Step 3 forces \(R_{m_b,a,b}\to0\). Thus the integer \(C_{m_b}(a,b)\) is eventually \(\lfloor t\rfloor\). Let \(\mu(a,b)\) denote the least \(m\) giving positive count. The nonnegativity of \(R\) implies \(\mu(a,b)\geq1/\Lambda_a(b)\). Conversely, for sufficiently large \(b\), choose
\[
m=\left\lceil\frac{1+c_a(\log b)/b}{\Lambda_a(b)}\right\rceil
\]
with a sufficiently large constant \(c_a\). This choice is \(O_a(2^b/b^a)\), and Step 3 ensures \(m\Lambda_a(b)-R_{m,a,b}\geq1\), so \(\mu(a,b)\leq m\). The resulting sandwich and Step 1 give the stated asymptotic. Taking ratios at adjacent fixed first coordinates gives the final limit. For \(a=0\), directly \(\mu(0,b)=2^b\).

## Verification

`verify.py` is a standalone Python 3 checker requiring only the standard library. It uses exact rational arithmetic to compare the polynomial solution with the integer recurrence on 7,497 triples, checks the nested-floor identity, and independently simulates the actual labeled firing process for every lattice target through depth eight. It also checks the proposed scales for six fixed rows at four large widths and verifies sixty nonintegral staircase predictions by exact integer arithmetic. Run `python verify.py`; successful output ends in `VERIFY_OK`.

These finite tests corroborate the derived identities but are not a substitute for the all-parameter rounding-error proof above.

## Relationship to prior work

The earlier directed-tree work establishes reachability and ranges for labeled chip-firing without lattice path mergers. The quadrant-lattice study from January 2026 treats unlabeled firing and its intermediate counts. OEIS A397913 directly records the exact labeled-quadrant recurrence and finite values. The later ordered-directed-graph study proves the reachability interpretation and obtains the exact boundary row \(\mu(0,b)=2^b\) and the one-step asymptotic \(\mu(1,b)\sim2^{b+1}/b\), but does not give the new complete fixed-\(a\geq2\) scale or the nonintegral limiting staircase. The distinction is mathematical rather than terminological: the recurrence supplies exact computability, while the proof here extracts a uniform asymptotic by localizing floor errors close to the final diagonal.

## Limitations

Constants hidden in \(O_{a,K}\) can depend on the fixed first coordinate and the bounded scaling range. The theorem deliberately excludes integer limiting staircase levels, where a vanishing rounding correction can change the floor. It does not determine the smallest finite initial-chip budget sufficient for the eventual minimum, nor the boundary regime where both coordinates grow. Priority against obscure or unindexed treatments of the exact recurrence remains an external research risk. Independent validation has not been performed.

## References

1. Ryota Inagaki, Tanya Khovanova and Austin Luo, *Labeled Chip-Firing on Directed k-ary Trees and Where Chips Land*, arXiv:2506.20656v1 (first public 2025-06-25). https://arxiv.org/abs/2506.20656
2. Ryota Inagaki, Tanya Khovanova and Austin Luo, *Chip-firing on the Lattice of Nonnegative Integer Points*, arXiv:2601.09125v1 (first public 2026-01-14). https://arxiv.org/abs/2601.09125
3. OEIS Foundation, *A397913: smallest reachable chip in the directed quadrant lattice*, entry credited to Inagaki, Khovanova and Luo with author date 2026-10-09. https://oeis.org/A397913
4. Ryota Inagaki, Tanya Khovanova and Austin Luo, *Labeled Chip-Firing on Ordered Directed Graphs*, arXiv:2611.25137v1 (2026-11-18), especially Sections 5.3–5.4. https://arxiv.org/abs/2611.25137
