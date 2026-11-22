# A parity-sensitive attraction basin for the alternating Rule 178 oscillator

## Finding

Let \(F_n\) be the synchronous binary elementary cellular automaton Rule 178 on a labelled path of \(n\ge3\) sites with both exterior neighbors held at zero. Denote its fully alternating primitive two-cycle by \(\mathcal A_n=\{0101\ldots,1010\ldots\}\), with each word truncated to \(n\) sites, and let \(B_n\) be the number of initial length-\(n\) words eventually entering this particular two-cycle. This is a **basin population**, not a number of recurrent points or a transient count.

An initial word with at least two maximal monochromatic runs enters \(\mathcal A_n\) if and only if (i) every run strictly between its first and last runs has odd length and (ii) any boundary run of ones has either odd length or length exactly two. A boundary run of zeros has no length restriction. Among uniform words, all zeros never enters \(\mathcal A_n\), while all ones enters if and only if \(n\) is odd.

Put
\[
A(z)=\frac{z}{1-z},\qquad O(z)=\frac{z}{1-z^2},\qquad R(z)=O(z)+z^2.
\]
Then the **exact all-length basin size** is
\[
\boxed{B_n=[z^n]\left(O(z)+\frac{2A(z)R(z)+(A(z)^2+R(z)^2)O(z)}{1-O(z)^2}\right),\qquad n\ge3.}
\]
Equivalently the expression inside the coefficient brackets reduces to
\[
\frac{z+z^2+2z^3+2z^4-5z^5-z^6+z^7+z^8}{1-z-3z^2+3z^3+z^4-z^5}.
\]
With Fibonacci numbers \(F_0=0\), \(F_1=1\), and Lucas numbers \(L_0=2\), \(L_1=1\), both extended by the Fibonacci recurrence, one has
\[
B_{2m}=2L_{2m}-2\quad(m\ge2),\qquad
B_{2m+1}=2L_{2m+1}+F_{2m-5}-2\quad(m\ge3),
\]
and \(B_3=7\), \(B_5=21\). In particular, writing \(\varphi=(1+\sqrt5)/2\),
\[
\lim_{m\to\infty}\frac{B_{2m}}{\varphi^{2m}}=2,\qquad
\lim_{m\to\infty}\frac{B_{2m+1}}{\varphi^{2m+1}}=2+\frac{\varphi^{-6}}{\sqrt5}.
\]
Thus a uniformly random initial word reaches the completely alternating oscillator with probability asymptotic, along the two parities, to the corresponding positive constant times \((\varphi/2)^n\). This is exponentially small although almost every initial word reaches *some* oscillator.

## Assumptions and scope

The sites are indexed \(1,\ldots,n\); initial symbols \(x_i\in\{0,1\}\), and the missing exterior symbols are fixed at \(x_0=x_{n+1}=0\) at **every** update. All sites are updated simultaneously according to
\[
(F_nx)_i=\begin{cases}x_{i-1}\lor x_{i+1},&x_i=0,\\
x_{i-1}\land x_{i+1},&x_i=1.
\end{cases}
\]
A basin includes its recurrent states. A maximal monochromatic run is a maximal consecutive block of equal symbols. For nonuniform words there are at least two such runs; first/last runs are called boundary runs. This is the synchronous Rule 178 model, not the sequential sweep model, and it has zero exterior boundaries rather than a cyclic wraparound.

## Proof

**Persistent walls.** Put \(d_i(t)=x_i(t)\oplus x_{i+1}(t)\) for each interior edge \(1\le i<n\). Whenever \(d_i(t)=1\), both incident symbols are different and therefore **both flip** at the next update: a zero has a neighboring one and a one has a neighboring zero. Thus \(d_i(t+1)=1\). Every initial wall therefore remains in place forever and separates the evolution of its neighboring monochromatic runs for the purpose of detecting a surviving equal pair.

**Interior runs.** Consider a run of length \(r\) strictly between two initial walls. At each update its two boundary symbols flip and the unchanged interior, if nonempty, is a run of length \(r-2\) of the original color between new walls. Iterate this two-ended erosion. If \(r\) is odd, the final singleton flips and the interval eventually has a wall at each of its edges, with no equal neighboring symbols. If \(r\) is even, it ends with two adjacent equal symbols, both flipping together forever, so their mutual wall stays zero. Persistence of the walls enclosing the original run makes this conclusion independent of neighboring runs.

**Boundary runs.** A boundary run of zeros is eroded one symbol per update from its single interior wall and therefore leaves no equal pair. At a boundary run of ones, the exterior zero makes its outermost one flip in the first update; the internal wall makes the innermost one flip. If its length is one, it causes no defect; if its length is two, both ones flip and the resulting boundary zeros are subsequently eroded. If the initial length is at least three, the first update leaves a new two-wall *interior* run of ones of length \(r-2\). By the preceding argument this produces a permanent adjacent equal pair exactly when \(r-2\) is a positive even number, namely when \(r\ge4\) is even. The right endpoint behaves symmetrically.

Consequently a nonuniform word loses every equal neighboring pair after finitely many updates if and only if all its interior runs have odd length and neither boundary run of ones has even length at least four. A word with every interior neighboring pair unequal is one of the two configurations in \(\mathcal A_n\), and both configurations flip to each other. Conversely, a permanent equal pair precludes ever reaching \(\mathcal A_n\). The all-zero input is fixed. The all-one input experiences two-ended erosion from the exterior zeros; it ends with a singleton (and hence full alternation) precisely for odd \(n\), whereas even \(n\) leaves a permanent equal pair. This proves the complete basin-membership criterion.

**Exact enumeration.** A run of zeros at an endpoint has arbitrary positive length and hence ordinary length generating series \(A(z)\). An allowed boundary run of ones has odd length or length two, hence series \(R(z)\). Every interior run must have odd positive length, giving series \(O(z)\). A nonuniform word has \(r\ge2\) runs with alternating colors. When \(r\) is even, its boundary colors differ and its contribution is \(2A(z)R(z)O(z)^{r-2}\). When \(r\ge3\) is odd, its boundary colors agree and its contribution is \((A(z)^2+R(z)^2)O(z)^{r-2}\). Summing both geometric series with step two gives the stated rational expression. Adding \(O(z)\) counts the all-one words of odd length; all-zero words are excluded. Coefficient extraction for \(n\ge3\) yields \(B_n\).

Expanding and simplifying that rational series gives the displayed polynomial fraction. Elementary partial fractions, using the Lucas and Fibonacci recurrences, yield the asserted even- and odd-length formulas (with \(n=3,5\) evaluated directly). The Binet formulas \(L_n=\varphi^n+(-\varphi)^{-n}\) and \(F_n=(\varphi^n-(-\varphi)^{-n})/\sqrt5\) then give the two asymptotic constants. Dividing \(B_n\) by \(2^n\) proves the probability statement.

## Verification

The standalone standard-library Python program `verify_rule178_basin.py` independently enumerates finite trajectories from each initial configuration, identifies whether their eventual orbit is the alternating two-cycle, and compares that answer with the run-language criterion. It separately computes the coefficients of the rational generating function and checks the claimed Fibonacci/Lucas formulas. All inputs were checked for every \(3\le n\le18\) (\(524280\) configurations in total), with exact integer arithmetic and no sampling. Reproduce by running `python3 verify_rule178_basin.py` beside this document; the recorded output is `verification_output.txt`. These finite checks corroborate, but do not substitute for, the unrestricted-length proof above.

## Relationship to prior work

Inokuchi and Sato (2000), in their Section 3.35, Lemma 3.80, Proposition 3.81 and Theorem 3.82, already prove the fixed/period-two classification, an ordinary Fibonacci recurrence for the number of two-cycle *attractors*, and a sharp worst transient length for Rule 178 with fixed boundaries. Those results, as well as local run erosion, are explicitly **prior work**, not newly claimed here. Their cited statements do not count initial words in the basin of any *particular* two-cycle and do not give the parity-sensitive rational basin series or the two limiting constants established above.

Kuhlman, Mortveit, Murrugarra and Kumar (2011) prove general fixed/two-cycle restrictions for synchronous bi-threshold networks; they do not determine this selected attractor's basin. The published study *Exact relaxation shells and a logarithmic typical clock for cyclic Rule 178* (2026) treats periodic boundary conditions and computes global transient shells and attractor counts, rather than the present fixed-boundary specific-attractor basin. The published study *Ballistic ascent transport and exact extinction shells in sequential bi-threshold paths* (2026) concerns in-place left-to-right updates, where every state instead becomes zero. Fukś gives an explicit space-time iterate formula for Rule 178 on the infinite cellular automaton; extracting the present finite-boundary basin language and its exact enumeration requires the separate boundary/run analysis above. No covering basin enumeration was identified in the sources inspected, but equivalently expressed or unindexed prior work remains possible.

## Limitations

The theorem concerns one specific, naturally distinguished alternating two-cycle on a zero-boundary path; it does **not** supply a complete individual-basin distribution or prove that this is the largest basin. It does not extend to arbitrary boundary values, asynchronous schedules, other elementary rules, or general graphs. The originality finding is bounded by accessible literature and records; it is not a proof of global historical priority or an independent external scientific audit.

## References

- S. Inokuchi and T. Sato, *On limit cycles and transient lengths of cellular automata with threshold rules*, Bulletin of Informatics and Cybernetics 32 (2000), 23–66, Section 3.35. https://doi.org/10.5109/13492 ; full open text: https://catalog.lib.kyushu-u.ac.jp/opac_download_md/13492/p023.pdf
- C. J. Kuhlman, H. S. Mortveit, D. Murrugarra and V. S. A. Kumar, *Bifurcations in Boolean Networks*, arXiv:1108.2974v1, first public 2011-08-15. https://arxiv.org/abs/1108.2974
- H. Fukś, *Solvable cellular automata*, Rule 178 iterate formula. https://lie.ac.brocku.ca/~hfuks/solvableca.html
- *Exact relaxation shells and a logarithmic typical clock for cyclic Rule 178* (2026), public mathematical research record. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-relaxation-shells-and-a-logarithmic-typical-clock-for-cycl--b1a85fec924d
- *Ballistic ascent transport and exact extinction shells in sequential bi-threshold paths* (2026), public mathematical research record. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-ballistic-ascent-transport-and-exact-extinction-shells-in-sequen--2d6ad6be9642
