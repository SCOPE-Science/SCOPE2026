# Sparse exact inverse and geometric sensitivity of odd-ring Rule 45

## Finding

Let \(n=2m+1\ge1\), with binary configurations indexed by \(\mathbb Z/n\mathbb Z\). Let the synchronous elementary cellular automaton Rule 45 be
\[
(F_n(x))_i=1\oplus x_{i-1}\oplus x_{i+1}\oplus(x_i x_{i+1}).
\]
All additions in the displayed Boolean polynomials are XOR; multiplication is AND. For any output \(y\), put \(B_{i,0}(y)=1\) and \(B_{i,k}(y)=\prod_{r=1}^{k}y_{i+2r}\) for \(1\le k\le m\), with subscripts reduced modulo \(n\).

**Theorem.** The map \(F_n\) is a bijection and its inverse \(H_n=F_n^{-1}\) is explicitly
\[
\boxed{(H_n(y))_i=\bigoplus_{k=0}^{m}B_{i,k}(y)(1\oplus y_{i+2k+1}).}
\tag{1}
\]
Each output-coordinate polynomial has exactly \(n+1=2m+2\) distinct squarefree monomials and algebraic degree \(m+1\).

For \(e_j\), the unit flip at site \(j\), and uniform \(y\in\{0,1\}^n\), the *inverse single-site influence* \(p_i(j)=2^{-n}|\{y:(H_n(y))_i\ne(H_n(y\oplus e_j))_i\}|\) is exactly
\[
\boxed{p_i(i+2k)=2^{-k}\ (1\le k\le m),\qquad
p_i(i+2k+1)=2^{-k}\ (0\le k\le m).}
\tag{2}
\]
The \(2m+1\) sites in (2) are distinct modulo \(n\). In particular every output bit is essential to the inverse at every site; the minimum symmetric inverse neighborhood radius on the length-\(n\) ring is \(m=(n-1)/2\). The inverse nevertheless has a linear-size nested Boolean circuit.

## Assumptions and scope

The rule is applied synchronously on **indexed periodic** binary configurations, not on half-lines, bracelets, or asynchronously updated arrays. All site indices are taken modulo the same positive odd integer \(n\). A Boolean monomial uses squarefree variables, with the constant \(1\) counted as a monomial. The influence probability uses independent uniformly distributed output configurations, not a distribution on forward trajectories. Formula (2) holds also at \(n=1\), where \(m=0\) and \(H_1(y)_0=1\oplus y_0\).

## Proof

**Step 1: a two-site backward identity.** Writing \(y=F_n(x)\), the local rule at site \(i+1\) gives
\[
1\oplus y_{i+1}=x_i\oplus(1\oplus x_{i+1})x_{i+2}.
\]
The local rule at \(i+2\), multiplied by \(x_{i+2}\), gives
\[
y_{i+2}x_{i+2}=(1\oplus x_{i+1})x_{i+2},
\]
because \(x_{i+2}(1\oplus x_{i+2})=0\). Hence
\[
x_i=1\oplus y_{i+1}\oplus y_{i+2}x_{i+2}.\tag{3}
\]

**Step 2: close the odd cycle without an unjustified division.** Iterating (3) exactly \(m\) times (the case \(m=0\) is separate and immediate) yields
\[
x_i=\bigoplus_{k=0}^{m-1}B_{i,k}(1\oplus y_{i+2k+1})\oplus B_{i,m}x_{i-1}.\tag{4}
\]
The local rule at \(i\) says
\[
x_{i-1}=1\oplus y_i\oplus x_{i+1}(1\oplus x_i).\tag{5}
\]
We claim that \(B_{i,m}x_{i+1}(1\oplus x_i)=0\) for every \(x\). If the product were \(1\), then \(x_i=0\), \(x_{i+1}=1\), and each \(y_{i+2r}=1\) for \(r=1,\dots,m\). Since
\[
y_{i+2r}=1\oplus x_{i+2r-1}\oplus(1\oplus x_{i+2r})x_{i+2r+1},
\]
induction forces \((x_{i+2r},x_{i+2r+1})=(0,1)\) for each \(r\): the assertion is true for the initial odd-indexed site \(x_{i+1}=1\), and each next output \(y_{i+2r}=1\) forces the displayed pair. At \(r=m\), the last forced equation is \(x_{i+2m+1}=x_i=1\), contradicting \(x_i=0\). Thus multiplying (5) by \(B_{i,m}\) and substituting into (4) proves formula (1) for every actual input and its output.

The right side of (1) depends only on \(y\), so any two inputs with equal output are equal coordinatewise. The map \(F_n\) is therefore injective, hence bijective on the finite set \(\{0,1\}^n\); consequently the right side is its inverse for every \(y\), not merely reachable outputs. When \(m=0\), the one-site rule is \(y_i=1\oplus x_i\), which agrees with (1).

**Step 3: monomials and circuit.** Expanding (1) gives the two monomials \(B_{i,k}\) and \(B_{i,k}y_{i+2k+1}\) for each \(0\le k\le m\). All \(2m+2=n+1\) monomials are distinct: prefixes \(B_{i,k}\) strictly increase along the \(m\) distinct even-offset variables, and each odd-offset variable occurs in only one corresponding second monomial. The largest degree is \(m+1\), attained only in \(B_{i,m}y_i\). The nested evaluation of these prefixes uses \(O(n)\) Boolean gates for each coordinate.

**Step 4: exact influences.** For the odd-offset site \(j=i+2k+1\) where \(0\le k\le m\), the only occurrence of \(y_j\) in the expanded polynomial is \(B_{i,k}y_j\). Its Boolean derivative is \(B_{i,k}\), which is \(1\) on exactly \(2^{n-k}\) of the \(2^n\) output configurations.

For an even-offset site \(j=i+2k\) with \(1\le k\le m\), differentiating all terms involving that variable gives \(B_{i,k-1}Q\), where \(Q\) starts with \(1\oplus y_{i+2k+1}\) and all of its other terms are independent of \(y_{i+2k+1}\). The prefix \(B_{i,k-1}\) is also independent of that variable. Thus on the \(2^{-(k-1)}\) proportion of outputs with prefix \(B_{i,k-1}=1\), the factor \(Q\) is balanced as \(y_{i+2k+1}\) varies. The derivative therefore equals \(1\) on exactly the fraction \(2^{-k}\) of all outputs. This proves (2), including its terminal \(k=m\) case.

Every influence is strictly positive. Hence no inverse coordinate can be computed from any proper subset of the \(n\) output positions. An inverse rule of symmetric radius less than \(m\) omits a position, while radius \(m\) reads the entire odd ring. This proves the radius claim.

## Verification

The accompanying standalone `verify.py` constructs the Rule 45 truth table directly from the eight elementary neighborhoods, computes the closed formula without calling an inverse solver, and checks the forward/inverse identity for every output of each odd length \(1,3,5,\ldots,15\). It separately computes all \(64\) coordinate-zero single-bit influence counts against (2). For lengths through \(13\) it obtains algebraic-normal-form coefficients using the finite Boolean Möbius transform and compares the complete monomial support, size, and degree to (1). It reports `VERIFY_OK odd_sizes=8 single_bit_checks=64 n_max=15`. This is finite corroboration; Steps 1–4 are the all-length proof.

## Relationship to prior work

Wolfram introduced the standard elementary cellular automaton setting. Hudcová's *Complexity in Cellular Automata*, Section 3.3, particularly Theorem 28, already establishes the **odd-ring bijectivity of Rule 45** and classifies its indexed predecessor counts; that known result is not claimed here. The 2022 summer-school report by Gadnayak and Bhattacharjee studies inverse rules for semireversible automata, including Rule 45 at lengths one and three. Martin, Odlyzko, and Wolfram's algebraic treatment mainly concerns additive automata and separately discusses nonlinear Rule 18. The present statement addresses a different and stronger invariant: the explicit all-odd-length coordinate ANF, exact bit-by-bit inverse differential probabilities, and optimal inverse radius. The known existence of an inverse, or a finite predecessor classification, does not state these quantities.

## Limitations

The theorem is restricted to one synchronous step of Rule 45 on odd-sized binary rings. It does not characterize even-ring inverse fibers, iterate the inverse over time, or assert pseudorandomness or cryptographic security. The claim has had mathematical self-review and finite checker replay but no independent external audit. Priority over any unindexed or unavailable work using a different equivalent rule numbering remains a residual uncertainty.

## References

1. S. Wolfram, *Statistical Mechanics of Cellular Automata*, Reviews of Modern Physics 55 (1983), 601–644, https://doi.org/10.1103/RevModPhys.55.601.
2. B. Hudcová, *Complexity in Cellular Automata* (thesis), Section 3.3, Theorem 28, https://dspace.cuni.cz/bitstream/handle/20.500.11956/178259/150057672.pdf?isAllowed=y&sequence=1.
3. K. K. Gadnayak and K. Bhattacharjee, *Finding the Inverse Cellular Automata of a given 1-D Reversible CA*, Indian Summer School on Cellular Automata (2022), https://www.cellularautomata.in/SummerSchool/SummerSchool1/IndianSummerSchool2022.pdf.
4. O. C. Martin, A. M. Odlyzko and S. Wolfram, *Algebraic Properties of Cellular Automata*, Communications in Mathematical Physics 93 (1984), 219–258, https://doi.org/10.1007/BF01223745.
