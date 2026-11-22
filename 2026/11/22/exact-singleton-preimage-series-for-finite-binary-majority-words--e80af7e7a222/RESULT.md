# Exact singleton-preimage series for finite binary majority words

## Finding

For every integer \(m\ge1\), define the sliding majority map
\[
\Phi_m:\{0,1\}^{m+2}\longrightarrow\{0,1\}^{m},\qquad
(\Phi_m(x))_i=\mathbf 1\{x_i+x_{i+1}+x_{i+2}\ge2\},\quad 1\le i\le m.
\]
The end bits are unrestricted: this is the finite, noncyclic version of elementary cellular-automaton Rule 232. Let \(U_m\) count outputs having **exactly one** input predecessor:
\[
U_m=\bigl|\{y\in\{0,1\}^{m}:|\Phi_m^{-1}(y)|=1\}\bigr|.
\]
Then the following all-length rational generating function is exact:
\[
\boxed{\displaystyle
\sum_{m\ge1}U_m z^m=
\frac{2z^3(1+3z-z^2+z^4-z^5-z^6)}
{1-z-z^2+z^3-2z^5-z^6-z^8-z^9}.}
\]
In particular the first values, at output lengths \(m=1,2,\ldots,16\), are
\[
0,0,2,8,8,14,16,24,42,74,130,218,354,572,928,1520.
\]
Equivalently, for every \(m\ge1\), these values obey
\[
U_{m+9}-U_{m+8}-U_{m+7}+U_{m+6}-2U_{m+4}-U_{m+3}-U_{m+1}-U_m=0.
\]
The language of uniquely invertible finite outputs is recognized by an explicit reachable thirty-state deterministic automaton with four accepting states, constructed below.

## Assumptions and scope

Inputs and outputs are *indexed linear words*, with no identification under reversal or rotation. Every one of the \(2^{m+2}\) input words is permitted. Each output bit is the strict majority of three consecutive input bits; for binary triples there are no ties. The two otherwise unobserved end bits are included in the input and counted when distinguishing predecessors. These conventions differ from cyclic updates, fixed boundary bits, and infinite-configuration injectivity.

## Proof

**1. Count predecessors by two-bit boundary states.** Number two-bit suffix states \(00,01,10,11\) by \(0,1,2,3\). For an output prefix \(y\), let \(c_p(y)\) count input-prefix realizations ending with pair \(p\). Before reading any output bit, each two-bit pair occurs once, so \(c(\epsilon)=(1,1,1,1)\). For a new output bit \(b\), append \(a\in\{0,1\}\) to the old suffix pair \(p\), yielding \(q=2(p\bmod2)+a\). The update is
\[
c_q(yb)=\sum_{p,a:\,q=2(p\bmod2)+a\atop
\lfloor((\lfloor p/2\rfloor)+(p\bmod2)+a)/2\rfloor=b}c_p(y).
\]
The floor equals the majority of the corresponding three-bit word. The total \(\sum_pc_p(y)\) is the number of distinct full input predecessors when \(|y|=m\).

**2. Saturation is exact for uniqueness.** Replace every counter by its minimum with \(2\), and apply the same updates with saturation after additions. Since all counts are nonnegative, \(\min(2,\sum c_i)=\min(2,\sum\min(2,c_i))\). Thus a saturated state \(v\in\{0,1,2\}^4\) still records precisely whether the predecessor count is zero, one, or at least two. An output is uniquely invertible exactly when \(\sum_pv_p=1\).

**3. A finite thirty-state transition certificate.** Starting at \(s_0=(1,1,1,1)\), breadth-first closure under the two output labels yields exactly thirty distinct saturated vectors. Four have coordinate sum one. Number them in breadth-first discovery order, with output label zero processed before label one, and define the integer matrix \(T\) by letting \(T_{ij}\) be the number (zero, one, or two) of output letters taking state \(i\) to state \(j\). Let \(e_0\) be the starting-state basis column and \(f\) the indicator column of the four accepting states. It follows exactly, not heuristically, that
\[
U_m=e_0^{\mathsf T}T^m f.
\]
The reproducible integer program `verify.py` constructs the entire transition graph from the eight local-rule values, without importing a precomputed state table, and checks the following *whole-vector* identity:
\[
\boxed{(T^9-T^8-T^7+T^6-2T^4-T^3-T-I)f=-2e_0.}
\]
The same complete graph has no transition into state \(s_0\), so \(Te_0=0\). Left-multiplying the displayed identity by \(e_0^{\mathsf T}T^m\) proves the ninth-order recurrence for **every** \(m\ge1\). The finite computation is a checkable exact integer certificate for an infinite recurrence, not an extrapolation from finitely many output lengths.

**4. Evaluate the generating function.** Exact transfer multiplication gives
\[
(U_0,U_1,\ldots,U_9)=(0,0,0,2,8,8,14,16,24,42),
\]
where \(U_0=0\) is used only to simplify the series convention. The recurrence and these initial values give
\[
(1-z-z^2+z^3-2z^5-z^6-z^8-z^9)
\sum_{m\ge0}U_mz^m
=2z^3+6z^4-2z^5+2z^7-2z^8-2z^9,
\]
proving the claimed rational form for every coefficient.

## Verification

Run `python3 verify.py` using Python 3 and only its standard library. The checker independently reconstructs all thirty states and both transition edges of every state, asserts four terminal states, checks the entire polynomial vector identity and absence of return transitions into the initial state, and compares the rational expansion with the transfer count through output length 120. It also enumerates all input words independently for every output length from one to thirteen and directly compares singleton counts. It reports two `VERIFY_OK` lines on success. The exhaustive examples are consistency checks; the all-length claim depends on the integer vector identity and its algebraic consequence.

## Relationship to prior work

Erica Jen, *Enumeration of Preimages in Cellular Automata* (1989), §4 Case e, pp. 441–442, provides an exact recurrence for the number of predecessors of **each specified Rule-232 output**. The predecessor transfer is therefore not new. Its pointwise formulas do not state the evaluated all-length number of outputs having multiplicity exactly one; the present contribution is the global, thresholded singleton enumeration and its rational form.

Biehl and Witkowski (2021) count transformation functions induced by local environments in elementary automata, rather than one-predecessor output words. Salo (2022) studies weak generalized inverses of cellular automata as shift maps, rather than finite-word singleton-preimage spectra.

The publicly available first-image classification *The exact first-image subshift and entropy of binary majority cellular automaton* (2026) evaluates **whether** finite outputs have any predecessor, including its forbidden words and entropy, but explicitly excludes precursor multiplicities. *Exact cyclic image counts and spectral growth for elementary majority cellular automaton Rule 232* (2026) counts obtainable **cyclic** indexed outputs, explicitly not inverse-fiber sizes. Neither gives the present finite-linear one-predecessor enumeration. A broader preimage formula can support deriving related facts, but the required all-length singleton summation is not provided by these cited statements.

## Limitations

The result concerns exactly one majority update with free linear boundaries. It does not count preimages on periodic rings, prove invertibility of the full cellular automaton, classify every inverse-fiber size, or address repeated updates. The thirty-state certificate is exact and reproducible, but has not undergone independent mathematical audit. An equivalent evaluated singleton series might exist in an unindexed preimage-counting literature; historical priority remains uncertain.

## References

1. M. Biehl and O. Witkowski, *Investigating Transformational Complexity: Counting Functions a Region Induces on Another in Elementary Cellular Automata*, *Complexity* (2021), first published 2021-06-29, DOI `10.1155/2021/7501405`, https://doi.org/10.1155/2021/7501405 .
2. E. Jen, *Enumeration of Preimages in Cellular Automata*, *Complex Systems* **3** (1989), 421–456, especially pp. 441–442, https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf .
3. V. Salo, *On von Neumann regularity of cellular automata*, arXiv:`2209.13373`, first posted 2022-09-27, https://arxiv.org/abs/2209.13373 .
4. *The exact first-image subshift and entropy of binary majority cellular automaton* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-the-exact-first-image-subshift-and-entropy-of-binary-majority-ce--9a5867630f75/RESULT.md .
5. *Exact cyclic image counts and spectral growth for elementary majority cellular automaton Rule 232* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-cyclic-image-counts-and-spectral-growth-for-elementary-maj--da4a182e6a5a/RESULT.md .
