# Exact maximal nilpotency-index census in layered incidence-algebra radicals

## Finding

Let \(P=E_1\oplus\cdots\oplus E_h\) be the ordinal sum of \(h\ge2\) nonempty antichains, with \(|E_i|=n_i\ge1\). Thus every element in an earlier level is less than every element in a later level, while elements in one level are incomparable. Let \(A=I(P,\mathbb F_q)\) be its incidence algebra, \(J=\operatorname{rad}(A)\), and let \(x\) range uniformly over \(J\). Define

\[
M=\sum_{1\le i<j\le h}n_i n_j,\qquad D=\sum_{i=1}^{h-1}n_i n_{i+1}.
\]

For all prime powers \(q\), the exact number of \(x\in J\) for which the canonical incidence-matrix representation of \(x^{h-1}\) has rank \(s\) is \(q^{M-D}C_h(s)\), where the following integer recurrence determines \(C_h\). Initialize \(C_1(n_1)=1\) and all other \(C_1(r)=0\). For \(1\le i<h\), set

\[
C_{i+1}(s)=\sum_{r=0}^{n_i}C_i(r)\,q^{(n_i-r)n_{i+1}}
\begin{bmatrix}r\\s\end{bmatrix}_q
\prod_{j=0}^{s-1}(q^{n_{i+1}}-q^j),
\]

where \(\begin{bmatrix}r\\s\end{bmatrix}_q\) is the Gaussian binomial coefficient, zero unless \(0\le s\le r\), and an empty product is one. Because \(J^h=0\), the number of elements of *maximal possible nilpotency index exactly* \(h\) is

\[
q^{M-D}\sum_{s\ge1}C_h(s).
\]

For the uniform-width-two family \(n_1=\cdots=n_h=2\), put

\[
L=h-1,\quad c=1-q^{-2},\quad a=(1-q^{-1})(1-q^{-2}).
\]

Then the complete distribution of \(R=\operatorname{rank}(x^{h-1})\) is

\[
\begin{aligned}
\Pr(R=2)&=a^L,\\
\Pr(R=1)&=\frac{q+1}{q}(c^L-a^L),\\
\Pr(R=0)&=1-\frac{q+1}{q}c^L+\frac1q a^L.
\end{aligned}
\]

Therefore the fraction of elements having maximal nilpotency index is

\[
\Pr(x^{h-1}\ne0)=\frac{q+1}{q}c^L-\frac1q a^L.
\]

For each fixed finite field, that fraction is asymptotic to \(\frac{q+1}{q}(1-q^{-2})^{h-1}\). Conditional on maximal nilpotency index, \(\operatorname{rank}(x^{h-1})=1\) with probability tending to one; the complementary conditional probability decays at rate \(O_q((1-q^{-1})^{h-1})\).

## Assumptions and scope

The field \(\mathbb F_q\) can have any characteristic, including characteristic two, and need not be a prime field. Each width \(n_i\) is positive and \(h\ge2\). The incidence algebra consists of matrices whose blocks from level \(E_i\) to \(E_j\) are arbitrary for \(i<j\), with diagonal blocks restricted to *diagonal* matrices, not arbitrary full matrices. Its Jacobson radical \(J\) has zero diagonal and all strictly upward blocks arbitrary. Thus \(\dim_{\mathbb F_q}J=M\). The canonical representation is the natural matrix action on \(\mathbb F_q^{n_1+\cdots+n_h}\). The intrinsic nilpotency-index conclusion is independent of representation; the finer rank distribution refers explicitly to this canonical one.

The nilpotency index of zero is taken to be one; more generally the index of a nilpotent element is the least positive integer \(m\) with \(x^m=0\). The claim characterizes the **maximal** index stratum, not every smaller index stratum. If \(h=2\), the formula still applies to the single possibly nonzero radical power \(x\).

## Proof

**Step 1 (radical and top-power support).** The diagonal quotient of \(A\) is a product of \(\sum_i n_i\) copies of \(\mathbb F_q\), so the strictly upward block space is the Jacobson radical. Multiplying a radical matrix follows a strictly increasing sequence of levels; therefore \(J^h=0\). A nonzero entry of \(x^{h-1}\) must follow a sequence of exactly \(h-1\) strict level increases. The only such sequence uses every level consecutively, beginning at \(E_1\) and ending at \(E_h\). Consequently, if \(B_i\) denotes the freely chosen \(n_i\times n_{i+1}\) block of \(x\) on consecutive levels, the *only* possibly nonzero block in \(x^{h-1}\) is

\[
B_1B_2\cdots B_{h-1},
\]

of size \(n_1\times n_h\). Every nonconsecutive block of \(x\) is irrelevant to this product and contributes an independent factor \(q^{M-D}\) to every count. There exist choices with a nonzero product (use a single compatible chain of unit entries), so \(h\) is indeed the largest nilpotency index attained by an element of \(J\).

**Step 2 (rank transition).** Suppose a fixed partial product of size \(n_1\times n_i\) has rank \(r\). By invertible changes of basis in the intermediate dimension and injectivity of a full-column-rank matrix, multiplication on the right by a uniformly chosen \(n_i\times n_{i+1}\) matrix gives the same rank distribution as a uniformly chosen \(r\times n_{i+1}\) matrix. Every possible latter matrix occurs with exactly \(q^{(n_i-r)n_{i+1}}\) choices of the original right factor. The exact number of \(r\times b\) matrices of rank \(s\) over \(\mathbb F_q\) is

\[
\begin{bmatrix}r\\s\end{bmatrix}_q
\prod_{j=0}^{s-1}(q^b-q^j).
\]

To verify this count independently, choose the \(s\)-dimensional image in \(\mathbb F_q^r\) and then count surjections from \(\mathbb F_q^b\) onto it; the latter number is the displayed product. Multiplying the number of prior sequences in rank \(r\) by the number of extensions in rank \(s\) proves the recurrence and its initial condition. In particular, \(\sum_s C_h(s)=q^D\), so after the free nonconsecutive choices the populations sum to \(q^M\).

**Step 3 (maximal nilpotency index).** An element of \(J\) satisfies \(x^h=0\). It has index exactly \(h\) if and only if \(x^{h-1}\ne0\), equivalent to positive rank in the block product. This establishes the stated maximal-index count.

**Step 4 (width-two diagonalization).** For any \(2\times2\) matrix over \(\mathbb F_q\), its probabilities of ranks two, one, zero are respectively

\[
a=(1-q^{-2})(1-q^{-1}),\quad b=\frac{(q-1)(q+1)^2}{q^4},\quad q^{-4}.
\]

A rank-one partial product remains rank one upon multiplication by an independent uniform \(2\times2\) matrix with probability \(c=1-q^{-2}\). Its rank can never increase. Starting from the identity partial product of rank two at time zero gives

\[
p_2(L+1)=a p_2(L),\quad p_1(L+1)=b p_2(L)+c p_1(L),
\]

with \(p_2(0)=1\) and \(p_1(0)=0\). Since \(c-a=c/q\) and \(b/(c-a)=(q+1)/q\), solving yields the three formulas in the finding. The rank-two survival probability divided by the nonzero survival probability is asymptotically \(\frac q{q+1}(a/c)^L=\frac q{q+1}(1-q^{-1})^L\). The asserted asymptotics and rank-one concentration follow.

## Verification

The two standalone programs `verify.py` and `verify_gf4.py` reproduce the recorded files `verification_output.txt` and `verification_gf4_output.txt`, respectively. They use only the Python standard library. The first computes actual incidence matrices, their powers, and their ranks over prime fields and exhausts the entire radical in six small examples; it also exhausts consecutive blocks in three larger examples and checks the width-two formula as exact fractions for five fields and ten heights each. The second implements \(\mathbb F_4\) arithmetically via the irreducible polynomial \(t^2+t+1\) and independently exhausts three extension-field cases, including entire radicals. The tests verify the original product and power identities rather than merely comparing two ways to evaluate the same recurrence.

For example, at \(q=2\) and widths \((2,2,2)\), the complete radical has \(4096\) elements; ranks \(0,1,2\) of \(x^2\) occur respectively \(928,2592,576\) times. At widths \((2,2,2,2)\), exhaustive consecutive-block enumeration over \(\mathbb F_2\) yields ranks \(0,1,2\) in \(1612,2268,216\) of the \(4096\) consecutive-block assignments. Independent random full-radical examples confirm that the nonconsecutive blocks do not affect the result. These finite enumerations check, but do not replace, the proof for arbitrary field sizes and level widths.

## Relationship to prior work

Ladkani's 2007 preprint studies derived equivalences of incidence algebras and establishes the finite-poset incidence-algebra setting; it does not count maximal-index radical elements. Quinn's 2015 arXiv version of the 2013 paper develops incidence algebras through quotients of poset path algebras and Gröbner bases, not distributions of ranks of extreme radical powers. The standard count of finite-field matrices of a prescribed rank is classical, and Fulman and Goldstein's 2012 preprint develops its probability distribution and limit theory. These established ingredients are not claimed as new.

The specific algebraic-to-probabilistic identification, complete varying-width top-power distribution, explicit width-two formula, and conditional rank-one concentration form the assessed claim. They are **elementary consequences after the key identification**, and a more general published theorem about products of random finite-field matrices could subsume the rank-transfer part without mentioning incidence algebras. The claim does not assert independence from such a theorem. A later paper by Petrov and Sokolov studies Jordan forms of random nilpotent matrices associated with posets; only its abstract was accessible in this review, so its possible implications are a named originality risk.

## Limitations

The full nilpotency-index distribution below the maximum is not determined, nor are all Jordan forms or conjugacy classes of radical elements. The width-two asymptotic takes the number of levels to infinity with the finite field fixed. Rank refers to the canonical incidence-matrix action, not the left regular action on the algebra. No scheme-theoretic multiplicity or independent priority certification is claimed.

## References

1. S. Ladkani, *Which canonical algebras are derived equivalent to incidence algebras of posets?*, arXiv:0708.1412, first submitted 2007-08-10, https://arxiv.org/abs/0708.1412.
2. D. Quinn, *The incidence algebras of posets and acyclic categories*, arXiv:1501.02481, first submitted 2015-01-11; journal version 2013, https://arxiv.org/abs/1501.02481.
3. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, arXiv:1211.0504, first submitted 2012-11-02, https://arxiv.org/abs/1211.0504.
4. F. Petrov and V. Sokolov, *Asymptotics of the Jordan Normal Form of a Random Nilpotent Matrix*, Journal of Mathematical Sciences 224 (2017), 339–344, DOI 10.1007/s10958-017-3419-z (abstract inspected only).
