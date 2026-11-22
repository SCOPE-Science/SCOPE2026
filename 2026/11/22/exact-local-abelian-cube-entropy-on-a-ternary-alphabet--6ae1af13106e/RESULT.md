# Exact local-Abelian-cube entropy on a ternary alphabet

## Finding
Let \(\Sigma=\{0,1,2\}\), and let \(a_n\) be the number of indexed words of length \(n\) over \(\Sigma\) containing neither an Abelian cube with block length one nor one with block length two. An Abelian cube of block length \(k\) is a factor \(UVW\) with \(|U|=|V|=|W|=k\) and identical letter-multiplicity vectors. Then, for all \(n\ge0\),
\[
\sum_{n\ge0}a_n z^n=\frac{1+2z+4z^2+5z^3+8z^4+16z^5+19z^6+5z^7-8z^8-9z^9-3z^{10}}{1-z-2z^2-4z^3-4z^4-2z^5+z^6+2z^7+z^8}.
\]
In particular, for every integer \(n\ge11\),
\[
a_n=a_{n-1}+2a_{n-2}+4a_{n-3}+4a_{n-4}+2a_{n-5}-a_{n-6}-2a_{n-7}-a_{n-8}.
\]
The initial values for \(0\le n\le10\) are
\[
(1,3,9,24,66,180,468,1206,3150,8232,21462).
\]
Let \(\alpha\) be the unique real root greater than one of
\[
Q(t)=t^8-t^7-2t^6-4t^5-4t^4-2t^3+t^2+2t+1.
\]
Then \(\alpha\approx2.60791474910528\), and \(a_n\sim C\alpha^n\), where \(C\approx1.47440545080927\) is positive. Consequently the topological entropy of this finite-type language is \(\log\alpha\).

## Assumptions and scope
Words are linear, have a distinguished first position, and use the three individually labeled symbols. The empty word is counted. Only contiguous Abelian cubes with the two specified block lengths are forbidden; blocks of length three or longer are permitted. These are not the counts of words avoiding *all* Abelian cubes. No asymptotic statement about the fully Abelian-cube-free language is asserted.

## Proof
A forbidden factor with block length one is a constant triple, and a forbidden factor with block length two consists of three successive length-two blocks with the same unordered pair of letters (with multiplicity). Every forbidden factor has length at most six. Hence, in extending a valid word by a symbol, it is necessary and sufficient to examine its last five letters.

Identify two length-at-most-five suffixes if one can be obtained from the other by a permutation of the ternary alphabet. Write each orbit in *restricted-growth canonical form*: its first occurring letter is 0, the next previously unseen letter is 1, and any third previously unseen letter is 2. Begin with the empty suffix. From state \(s\), append each of the three literal symbols to its canonical representative, reject a transition precisely if it creates a forbidden terminal factor, retain only the last five letters, and canonicalize. If distinct appended symbols produce the same canonical state, record their number as the edge multiplicity. Relabeling preserves both forbidden conditions and is a bijection on future extensions, so this weighted quotient counts **all labeled words**, not just canonical representatives.

This rule yields exactly 49 reachable states. Let \(M\) be its 49-by-49 nonnegative integer adjacency matrix, and \(e\) be the unit vector at the empty state. Exact integer determinant computation, reconstructible from `check_transfer.py`, gives
\[
\det(tI-M)=t^{41}Q(t).
\]
The count is \(a_n=e^\mathsf{T}M^n\mathbf1\) with the row/column convention interpreted accordingly. By Cayley–Hamilton, the denominator recurrence holds for every \(n\ge49\). Exact transition arithmetic checks it for the remaining \(11\le n\le48\), and gives the initial eleven values. Multiplying their generating series by the reciprocal characteristic factor yields the numerator displayed in the finding, with degree ten. This establishes the rational identity and the recurrence for **every** required integer, not merely for the finite test range.

The weighted graph has exactly one cyclic strongly connected component, comprising 30 states; that component has a self-loop and hence is primitive. All other components are acyclic and contribute only zero eigenvalues. Perron–Frobenius theory therefore gives a simple, strictly dominant positive spectral root and a positive leading coefficient because the initial state reaches the recurrent component. The two positive roots of \(Q\) are separated by \((0,1)\) and \((2,3)\), and Descartes' sign rule permits at most two; hence the Perron root is the unique root greater than one. Writing \(D(z)=z^8Q(1/z)\), \(P(z)\) for the displayed numerator, and \(r=1/\alpha\), the simple-pole coefficient is
\[
C=-\frac{P(r)}{rD'(r)}>0.
\]
The stated numerical approximations are evaluations of these exact algebraic expressions.

## Verification
Run `python check_transfer.py` with Python 3 and SymPy. It reconstructs all 49 states without a hard-coded transition table, checks the exact characteristic polynomial, checks the cyclic strongly connected components, derives the exact numerator, and uses Cayley–Hamilton plus all earlier needed integer coefficient checks. Run `python check_direct.py` with standard Python 3. It independently enumerates all labeled words of lengths zero through eleven using the original forbidden-factor definitions, and separately performs a literal-symbol suffix dynamic program through length 130. Both programs were executed successfully against the actual packaged sources.

The restricted-language count first differs from the published fully Abelian-cube-free ternary sequence at length nine: 8232 versus 7998. This independently checks that the scope of the new statement is a strict local approximation rather than the complete avoidance language.

## Relationship to prior work
Aberkane, Currie and Rampersad (2004) prove exponential growth for ternary words avoiding Abelian cubes of **every** positive block length, and tabulate their initial counts. Their general avoidance property is stronger than the present two-period restriction, but their results do not give the rational generating function for the latter. Samsonov and Shur (2012) construct finite-antidictionary automata to bound growth rates for Abelian-power-free languages, including a 2.371237 upper bound for full ternary Abelian-cube avoidance. Their general technique can construct finite truncation automata, but the cited work does not state the present two-period polynomial, recurrence, or exact entropy. Comparing \(2.607914749\ldots\) with \(2.371237\) quantifies how much the shortest two forbidden periods alone fail to reproduce the globally constrained exponential rate.

## Limitations
The result concerns exactly two forbidden block lengths on a ternary alphabet. The value of the growth rate for complete Abelian-cube avoidance is not determined, and the 2012 upper bound is not improved. The finite-state determinant is certified by fully supplied, reproducible exact-arithmetic code, not an independent formal proof assistant or outside audit. An older equivalent closed form that escaped the literature search remains possible.

## References
1. A. Aberkane, J. D. Currie, N. Rampersad, *The Number of Ternary Words Avoiding Abelian Cubes Grows Exponentially*, Journal of Integer Sequences 7 (2004), Article 04.2.7. https://cs.uwaterloo.ca/journals/JIS/VOL7/Currie/currie18.html ; full text https://cs.uwaterloo.ca/journals/JIS/VOL7/Currie/currie18.pdf .
2. A. V. Samsonov and A. M. Shur, *On Abelian Repetition Threshold*, RAIRO Theoretical Informatics and Applications 46 (2012), 147–163. https://www.numdam.org/article/ITA_2012__46_1_147_0.pdf .
3. OEIS A096168, *Number of Abelian cubefree words over a 3-letter alphabet*. https://oeis.org/A096168 .
