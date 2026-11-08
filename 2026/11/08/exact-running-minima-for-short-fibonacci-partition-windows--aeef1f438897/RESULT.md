# Exact running minima for short Fibonacci-partition windows

## Finding
Let \(F_1=F_2=1\), \(F_{r+2}=F_{r+1}+F_r\), and let \(R(n)\) count representations of the nonnegative integer \(n\) as a sum of **distinct** Fibonacci numbers from \(F_2,F_3,\ldots\), with \(R(0)=1\). For every integer \(m\ge7\) and every integer \(1\le H\le F_{m-1}-1\), define \(j=j(m,H)\) to be the **largest** integer satisfying
\[
2\le j\le m-1,\qquad j\not\equiv m\pmod2,\qquad F_j-1\le H.
\]
Such a \(j\) always exists. Then the minimum and its **complete set of attaining offsets** are
\[
\boxed{\min_{1\le t\le H}R(F_m+t)=\frac{m-j+1}{2}},
\qquad
\boxed{\{t\in[1,H]\cap\mathbb Z:R(F_m+t)=\tfrac{m-j+1}{2}\}
=\{F_j-1,F_{j+1}-1\}\cap[1,H].}
\]
In particular, the minimum is attained at either one or two offsets, and its running value has an exact Fibonacci-index staircase across the entire interval immediately following \(F_m\). The zero offset \(F_2-1\) is automatically excluded by the intersection with \([1,H]\).

For each fixed \(0<\alpha<1\), taking \(H=\lfloor F_m^\alpha\rfloor\) yields, as \(m\to\infty\),
\[
\min_{1\le t\le\lfloor F_m^\alpha\rfloor}R(F_m+t)
=\frac{1-\alpha}{2}m+O_\alpha(1)
=\frac{1-\alpha}{2\log\varphi}\log F_m+O_\alpha(1),
\quad\varphi=\frac{1+\sqrt5}{2}.
\]
The exact staircase, not the asymptotic corollary alone, is the central result.

## Assumptions and scope
All representation counts use each allowed Fibonacci number at most once; \(F_1\) is omitted to avoid counting the repeated numerical value \(1\) twice. The count includes the empty partition at \(n=0\). Parameters \(m,H\) are integers in the stated closed ranges. The result concerns the first \(F_{m-1}-1\) positive offsets beyond \(F_m\), not general intervals elsewhere. Its proof uses elementary counting identities; none of the computations below is used in place of an infinite argument.

## Proof
**1. Elementary baseline and reflection.** The greedy nonconsecutive-Fibonacci (Zeckendorf) expansion ensures \(R(n)\ge1\) for every \(n\ge0\). For \(k\ge4\) and \(0\le t\le F_{k-1}-2\), split representations of \(F_k+t\) according to whether they use \(F_k\). Representations using it contribute \(R(t)\). The others use precisely a subset of \(F_2,\ldots,F_{k-1}\). Since
\[
\sum_{i=2}^{k-1}F_i=F_{k+1}-2,
\]
complementation within these parts bijects representations of \(F_k+t\) avoiding \(F_k\) with representations of \(F_{k-1}-2-t\). No larger part is possible because \(F_k+t<F_{k+1}\). Therefore
\[
R(F_k+t)=R(t)+R(F_{k-1}-2-t). \tag{1}
\]
Both summands are positive, so \(R(n)\ge2\) for every integer \(F_k\le n\le F_{k+1}-2\), for \(k\ge4\). On the other hand, \(F_{k+1}-1\) exceeds the sum of all allowed parts below \(F_k\) and therefore every representation of it uses \(F_k\); removing that part leaves \(F_{k-1}-1\). Induction, starting at \(R(0)=R(1)=R(2)=1\), proves
\[
R(n)=1\quad\Longleftrightarrow\quad n=F_i-1\text{ for some }i\ge2. \tag{2}
\]
(The uniqueness characterization was already known in the classical Fibonacci-partition literature; the proof here provides the precise boundary check needed below.)

**2. Exactly two representations at small positive offsets.** Fix \(k\ge5\) and \(1\le t\le F_{k-1}-2\). By (1) and positivity, \(R(F_k+t)=2\) if and only if both \(t\) and \(F_{k-1}-2-t\) have count one. By (2), this means \(t=F_a-1\) and \(F_{k-1}-2-t=F_b-1\), hence \(F_a+F_b=F_{k-1}\). The only sum of two (not necessarily distinct) positive Fibonacci values equal to \(F_{k-1}\) is \(F_{k-2}+F_{k-3}\): if the larger index were at most \(k-3\), the sum would be at most \(2F_{k-3}<F_{k-1}\); a larger index than \(k-2\) already exceeds the target. Consequently
\[
R(F_k+t)=2\quad\Longleftrightarrow\quad
 t\in\{F_{k-3}-1,F_{k-2}-1\}, \tag{3}
\]
within the specified positive range. For \(k=5\), the first displayed offset is zero and is correctly excluded.

**3. Two-index descent.** If \(\ell\ge5\) and \(0\le t<F_{\ell-3}\), any representation of \(F_\ell+t\) has largest part either \(F_\ell\) or \(F_{\ell-1}\), because all parts through \(F_{\ell-2}\) sum to \(F_\ell-2\). Removing that largest part gives, respectively, a representation of \(t\) or of \(F_{\ell-2}+t\), with no inadmissible larger parts. Thus
\[
R(F_\ell+t)=R(t)+R(F_{\ell-2}+t).
\]
Iterating gives, for integers \(m\ge k\ge5\) of the same parity and \(0\le t<F_{k-1}\),
\[
R(F_m+t)=\frac{m-k}{2}R(t)+R(F_k+t). \tag{4}
\]
This descent identity is equivalent to Lemma 2.3 of Chow and Jones (2026) and is used as known input, with its counting proof recalled for completeness.

**4. Full minimum and equality cases.** First suppose \(j\le m-3\), and set \(k=j+3\), so \(k\equiv m\pmod2\). Maximality of \(j\) implies \(H<F_{j+2}-1\), hence \(1\le t\le H\le F_{k-1}-2\). Equation (4), positivity \(R(t)\ge1\), and (1) imply
\[
R(F_m+t)\ge\frac{m-k}{2}+2=\frac{m-j+1}{2}.
\]
The right-hand side is attained by \(t=F_j-1\), if positive, or \(t=F_{j+1}-1\): both are unique-representation offsets by (2), and (3) shows \(R(F_k+t)=2\). Conversely, if equality holds, (3) forces \(t\) to be one of precisely these two offsets (whether the coefficient \((m-k)/2\) vanishes or not). Therefore the entire minimizing set is the claimed intersection. At least one candidate lies in \([1,H]\): if \(j\ge3\), then \(F_j-1\ge1\) and the definition of \(j\) includes it; if \(j=2\), then necessarily \(H=1\), and \(F_3-1=1\) is included.

If \(j=m-1\), the upper bound on \(H\) forces \(H=F_{m-1}-1\). Its final value \(F_m+H=F_{m+1}-1\) has count one by (2), and every other integer in \([F_m+1,F_{m+1}-2]\) has count at least two by (1). The formula gives minimum one and its sole attaining offset \(F_{m-1}-1\), as required.

**5. Power-length windows.** By Fibonacci exponential growth, the defining inequalities \(F_j-1\le H<F_{j+2}-1\) (when \(j\le m-3\)) give \(j=(\log H)/(\log\varphi)+O(1)\). For \(H=\lfloor F_m^\alpha\rfloor\) with fixed \(0<\alpha<1\), this becomes \(j=\alpha m+O_\alpha(1)\). Substitute in the exact minimum formula to obtain the stated corollary.

## Verification
The supplied `verify.py` computes \(R(n)\) by exact subset-sum dynamic programming, directly multiplying the finite factors \(1+z^{F_i}\), and independently checks the reflection identity, all individual running minima and every attaining offset for \(7\le m\le21\) and **every** allowed \(H\). It also tests the uniqueness criterion on its computed range. A successful invocation reports `H_tests=17683`, `reflection_tests=17689`, `singleton_checks=17712`, all with integer arithmetic. Finite checks confirm examples and catch indexing mistakes; the proof above handles every allowed parameter.

## Relationship to prior work
Chow and Jones, *On short averages of the Fibonacci partition function* (2026), prove a short-average asymptotic for the same \(R\) and the descent identity used in (4). Their averaging statement does not determine exact running minima or the full set of attaining offsets for every window length. Robbins (1996) and earlier authors studied Fibonacci partition recurrences and the unique-representation cases. Weinstein's *Notes on Fibonacci Partitions* gives powerful global representation-count formulas and classifies small fixed count levels, while Chow and Slattery (2021) give an exact representation formula and summatory estimates. Their results make individual values calculable, and the elementary ingredients of the proof are familiar; the distinguishing claim here is the explicit **uniform moving-window optimization and complete extremizer staircase**. No independent historical-priority certification is asserted.

## Limitations
This theorem neither determines maxima nor the distribution of all partition counts, and it only treats windows with \(H\le F_{m-1}-1\). Previously known representation-count identities are essential; the novelty claim is confined to the exact interval-wise minimum and equality set, not to these identities or to Zeckendorf representations. An equivalent result could exist in older, unindexed partition literature. Independent mathematical review has not been performed.

## References
1. S. Chow and O. Jones, *On short averages of the Fibonacci partition function*, arXiv:2610.39817v1 (first public October 29, 2026), https://arxiv.org/abs/2610.39817.
2. S. Chow and T. Slattery, *On Fibonacci partitions*, J. Number Theory **225** (2021), 310–326; arXiv:2009.08222, https://arxiv.org/abs/2009.08222.
3. N. Robbins, *Fibonacci partitions*, Fibonacci Quarterly **34** (1996), 306–313.
4. F. V. Weinstein, *Notes on Fibonacci Partitions*, Experimental Mathematics **25** (2016), 482–499; preprint arXiv:math/0307150, https://arxiv.org/abs/math/0307150.
