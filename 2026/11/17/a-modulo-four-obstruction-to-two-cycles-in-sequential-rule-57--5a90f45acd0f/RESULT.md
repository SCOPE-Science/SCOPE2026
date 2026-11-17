# A modulo-four obstruction to two-cycles in sequential Rule 57

## Finding

Let \(n\ge3\) and let \(F_n\) be one complete in-place, left-to-right sweep (sites \(0,1,\ldots,n-1\)) of elementary cellular automaton Rule 57 on a labelled binary cycle \(\mathbb Z/n\mathbb Z\). Each site's new bit is computed using the current bits of its two neighbors, including changes already made in the same sweep.

**Theorem.** The map \(F_n\) is bijective and has no fixed point. Its entire second-iterate fixed set is
\[
\operatorname{Fix}(F_n^2)=
\begin{cases}
\varnothing,&n\not\equiv2\pmod4,\\
\{x^{a,b}:a,b\in\{0,1\}\},&n\equiv2\pmod4,
\end{cases}
\]
where the four words \(x^{a,b}\) are specified by the repeated spatial block \((a,b,1-a,1-b)\), truncated to length \(n\). Every one of these words is sent to its bitwise complement. Consequently there are exactly two primitive temporal two-orbits if \(n\equiv2\pmod4\), and none otherwise; the full two-iterate fixed-point count is exactly \(4\mathbf1_{n\equiv2\ (\mathrm{mod}\ 4)}\).

## Assumptions and scope

Bits lie in \(\{0,1\}\), indices are interpreted modulo \(n\), and the complete scan order is fixed as \(0,1,\ldots,n-1\). At one single-site update with current neighboring bits \(\ell,r\) and center \(c\), the Rule-57 output equals \(c\) exactly when \((\ell,r)=(0,1)\), and equals \(1-c\) otherwise. Equivalently, the Wolfram rule table in order \(111,110,101,100,011,010,001,000\) is \(0,0,1,1,1,0,0,1\). The theorem is for all labelled rings \(n\ge3\), not for parallel updating, random schedules, or all possible site permutations. Positions are not quotiented by rotations or complement.

## Proof

1. **Bijectivity and fixed states.** For fixed neighbor values, a site update is either the identity on the center bit or its complement. Hence it is an involutive permutation of the entire configuration space, and the composite full sweep \(F_n\) is bijective. A fixed point of any sequential sweep must hold at each local update, since each site updates exactly once. The hold rule would demand that every site's left neighbor is zero and its right neighbor is one, an impossibility around a cycle. Thus \(\operatorname{Fix}(F_n)=\varnothing\).

2. **Two cycles cannot mix changing and unchanged sites.** Suppose \(F_n(x)=y\) and \(F_n(y)=x\). Define \(d_i=x_i\oplus y_i\). If \(d_i=0\), the bit at site \(i\) does not change during either sweep, so both of its updates use a left neighbor equal to zero and a right neighbor equal to one. During its two updates, each of those two neighbors has its old value on one occasion and its new value on the other. This remains true at sites \(0\) and \(n-1\), with the old/new order reversed at the scan boundary. Therefore \(d_{i-1}=d_{i+1}=0\). Connectivity of the cyclic neighbor graph propagates this to every site. That would imply \(x=y\), a forbidden fixed point. Consequently \(d_i=1\) for all \(i\), i.e. \(y_i=1-x_i\) everywhere.

3. **Interior and boundary constraints.** For \(1\le i\le n-2\), the first sweep sees neighbor pair \((y_{i-1},x_{i+1})=(1-x_{i-1},x_{i+1})\), and the second sees \((x_{i-1},y_{i+1})=(x_{i-1},1-x_{i+1})\). Both updates must toggle the center. The first fails to toggle precisely when both \(x_{i-1},x_{i+1}\) are one, and the second fails precisely when both are zero. Therefore both toggle if and only if \(x_{i-1}\ne x_{i+1}\), or \(x_{i+2}=1-x_i\) for \(0\le i\le n-3\).

   At site \(0\), the old left and right neighbors appear in the first sweep, while their complementary values appear in the second. Two toggles require \(x_{n-1}=x_1\). At site \(n-1\), the already updated neighbors are used in the first sweep and the old ones in the second; two toggles require \(x_{n-2}=x_0\). Conversely, these interior and boundary conditions guarantee both sweeps toggle every bit, so they are sufficient.

4. **Solve the constraints.** Put \(a=x_0\) and \(b=x_1\). The interior recurrence forces
\[
(x_0,x_1,\ldots,x_{n-1})=(a,b,1-a,1-b,a,b,1-a,1-b,\ldots)
\]
truncated to length \(n\). If \(n\equiv0\pmod4\), the first boundary equation says \(1-b=b\), impossible. If \(n\equiv1\pmod4\), it requires \(a=b\), whereas the second requires \(1-b=a\), impossible. If \(n\equiv3\pmod4\), it requires \(1-a=b\) and \(b=a\), impossible. If \(n\equiv2\pmod4\), both boundary equations hold identically for all four \((a,b)\). These four are distinct, since they have different first two bits. They are complemented by one sweep and grouped into exactly two two-element orbits. This proves every assertion. \(\square\)

## Verification

Two standalone Python programs in `checks/` reproduce independent checks using only the standard library. From the directory containing this document, execute `python3 checks/exhaustive.py` and `python3 checks/symbolic.py`. The first implements Rule 57 by its eight-bit truth table and exhaustively enumerates all \(2^n\) initial words for every \(3\le n\le17\), independently comparing direct two-sweep return with the four-block classification. The second independently checks the local hold/toggle truth table and verifies the two boundary congruences for every \(3\le n\le256\). Their recorded output files are included. These finite checks are corroboration, not the infinite proof; the latter is the preceding local argument.

## Relationship to prior work

Vielhaber, *Computing by Temporal Order: Asynchronous Cellular Automata* (arXiv:1208.2762, initially publicly submitted 2012-08-14), establishes the role of Rule 57 as a particularly expressive rule under variable deterministic update schedules, including bijectivity of individual-site updates and permutation group results for bounded sizes. The relevant statements concern transformations obtainable by varying schedules, not the exact two-cycle set for the repeatedly fixed sweep. Donoso-Leiva, Goles, Ríos-Wilson and Sené, *On the Convergence of Elementary Cellular Automata under Sequential Update Modes* (arXiv:2509.07797), classify Rule 57 among rules without fixed points, but do not provide the two-cycle congruence. De Oliveira et al., *Non-maximal Sensitivity to Synchronism in Periodic Elementary Cellular Automata: Exact Asymptotic Measures* (arXiv:2004.07128), study equivalence of schedules rather than fixed-sweep primitive two-cycles. The current theorem concerns the complete *low-period sector* of one fixed permutation, not complexity or universality under schedule variation.

## Limitations

Only temporal periods one and two, and only the specified left-to-right scan, are classified; higher primitive periods can be large and are not claimed here. The proof does not determine the general cycle spectrum, nor address infinite nonperiodic configurations. Literature comparison supports a distinct claim but does not certify absolute historical novelty; specifically, a 2025 study of maximum cycle periods was inspected only at abstract level. Independent external mathematical validation has not been performed.

## References

- M. Vielhaber, *Computing by Temporal Order: Asynchronous Cellular Automata*, EPTCS 90 (2012), pp. 166–176, arXiv:1208.2762, https://arxiv.org/abs/1208.2762, DOI:10.4204/EPTCS.90.14 (initial public date 2012-08-14).
- I. Donoso-Leiva, E. Goles, M. Ríos-Wilson, and S. Sené, *On the Convergence of Elementary Cellular Automata under Sequential Update Modes*, arXiv:2509.07797, https://arxiv.org/abs/2509.07797.
- P. P. B. de Oliveira, E. Formenti, K. Perrot, S. Riva, and E. L. P. Ruivo, *Non-maximal Sensitivity to Synchronism in Periodic Elementary Cellular Automata: Exact Asymptotic Measures*, arXiv:2004.07128, https://arxiv.org/abs/2004.07128.
- I. Donoso-Leiva, E. Goles, M. Ríos-Wilson, and S. Sené, *Impact of (a)Synchronism on ECA: Towards a New Classification*, arXiv:2505.10645, https://arxiv.org/abs/2505.10645 (abstract-level comparison only).
