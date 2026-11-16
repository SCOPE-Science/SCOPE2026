# Full Fourier support of balanced primitive binary words at odd half-length

## Finding
For every odd integer \(m\ge3\), let \(G_m=(\mathbb F_2)^{2m}\) and let \(B_m\subseteq G_m\) consist of all **position-labelled binary words** with exactly \(m\) ones and least positive cyclic period \(2m\). Set \(f_m=\mathbf1_{B_m}\), and use the unnormalized Walsh transform
\[
W_m(s)=\sum_{x\in B_m}(-1)^{\langle s,x\rangle},\qquad s\in G_m.
\]
Then
\[
W_m(s)=0\quad\Longleftrightarrow\quad |s|\text{ is odd}.
\]
Consequently, counting convolution \(T_mg=f_m*g\) on \(\ell^2(G_m)\) has rank and nullity both equal to \(2^{2m-1}\). Its image is exactly the functions invariant under translation by the all-one vector. There are **no additional Fourier zeros** beyond those forced by complement symmetry.

Define
\[
M_m=\frac{m+1}{m}\binom{m}{(m-1)/2},\qquad
S_m=\sum_{a=1}^{\lfloor m/3\rfloor}\binom{2a}{a}.
\]
Every nonzero multiplier satisfies \(|W_m(s)|\ge M_m-S_m>0\). For the condition number \(\kappa_m\) restricted to the nonzero-multiplier subspace,
\[
\kappa_m\sim \frac{2^m}{\sqrt2}\qquad(m\to\infty\text{ through odd integers}).
\]

**Exact prime specialization.** If \(m=p\ge3\) is an odd prime, define \(Q_p=\binom{2p}{p}\). For every even-weight frequency \(s\) with \(|s|=2j\), put \(\varepsilon(s)=(-1)^{s_0+s_2+\cdots+s_{2p-2}}\). Then the entire signed spectrum is
\[
W_p(s)=(-1)^j Q_p\frac{\binom pj}{\binom{2p}{2j}}-2\varepsilon(s).
\]
At weight \(2j\), the value corresponding to \(\varepsilon\in\{+1,-1\}\) occurs exactly
\[
N_{j,\varepsilon}=\tfrac12\left[\binom{2p}{2j}+\varepsilon(-1)^j\binom pj\right]
\]
times, counting zero multiplicities where applicable. In particular, the smallest positive multiplier magnitude is \(M_p-2\), attained at exactly
\[
\binom{2p}{p-1}+\binom{p}{(p-1)/2}
\]
frequencies; the largest magnitude is \(Q_p-2\). The **sharp** visible condition number and inverse norm are
\[
\kappa_p=\frac{Q_p-2}{M_p-2},\qquad
\bigl\|T_p^\dagger\bigr\|_{2\to2}=\frac1{M_p-2}.
\]
The prime formula and every rank statement concern **all labelled rotations**, not one representative per necklace.

## Assumptions and scope
The group law in \(G_m\) is coordinatewise XOR, and the Fourier characters are \(\chi_s(x)=(-1)^{\langle s,x\rangle}\). Convolution is \((f*g)(y)=\sum_{x\in G_m}f(x)g(y-x)\), without probability normalization. A word has least cyclic period \(d\) if its cyclic shift by \(d\) is itself and no smaller positive shift fixes it. The condition \(|x|=m\) means exactly half the \(2m\) positions equal one. The spectral assertions are for \(m\) odd, \(m\ge3\), and the exact full signed multiplicities only for odd prime \(p\).

## Proof
**1. Periodic competitors and complement symmetry.** Let \(H_m=\{x\in G_m:|x|=m\}\). If a word of \(H_m\) has proper period \(d\), it consists of \(r=2m/d\) repetitions of a block. Since its total number of ones is \(m\), the repetition count \(r\) divides \(m\), and is therefore odd and at least three. Thus \(d=2a\), with \(a=m/r\le m/3\), and its root block has exactly \(a\) ones. Hence the number \(R_m=|H_m\setminus B_m|\) obeys
\[
0\le R_m\le S_m=\sum_{a=1}^{\lfloor m/3\rfloor}\binom{2a}{a}.
\]
Complementation \(x\mapsto x+\mathbf1\) preserves \(H_m\), all cyclic periods, and consequently \(B_m\). Pairing each word with its complement shows \(W_m(s)=0\) whenever \(|s|\) is odd.

**2. Central slice multipliers.** The unnormalized Walsh transform of \(\mathbf1_{H_m}\) depends only on \(t=|s|\) and is the binary Krawtchouk value
\[
K_m(t;2m)=\sum_{i=0}^{m}(-1)^i\binom ti\binom{2m-t}{m-i},
\]
where out-of-range binomial coefficients are zero. Binomial double counting gives
\[
\binom{2m}{t}K_m(t;2m)=\binom{2m}{m}K_t(m;2m).
\]
Since \(\sum_{t\ge0}K_t(m;2m)z^t=(1-z)^m(1+z)^m=(1-z^2)^m\), every odd-index value is zero, and for \(t=2j\)
\[
K_m(2j;2m)=(-1)^j\binom{2m}{m}\frac{\binom mj}{\binom{2m}{2j}}.
\]
The absolute value \(A_j\) in the last display obeys
\[
\frac{A_{j+1}}{A_j}=\frac{2j+1}{2m-2j-1}\qquad(0\le j<m).
\]
Thus its minimum over \(0\le j\le m\) occurs at the adjacent indices \(j=(m-1)/2,(m+1)/2\) and equals \(M_m\).

**3. The periodic-deletion bound is strictly below the Krawtchouk gap.** For \(m=3,5,7,9,11\), the pairs \((S_m,M_m)\) are respectively \((2,4),(2,12),(8,40),(28,140),(28,504)\). For every odd \(m\ge13\), elementary binomial bounds yield
\[
S_m<\frac{4^{m/3+1}}3,\qquad M_m\ge\frac{2^m}{m+1}.
\]
The inequality \(2^{m/3}>4(m+1)/3\) holds at \(m=13\) and remains true under each increment \(m\mapsto m+2\), because the ratio \(2^{m/3}/(m+1)\) increases. Therefore \(S_m<M_m\) for every odd \(m\ge3\). Fourier transformation of \(\mathbf1_{B_m}=\mathbf1_{H_m}-\mathbf1_{H_m\setminus B_m}\) now gives, for even \(|s|\),
\[
|W_m(s)|\ge |K_m(|s|;2m)|-R_m\ge M_m-S_m>0.
\]
Together with the odd-frequency symmetry zero this proves the exact support and rank. On a finite abelian group convolution is diagonalized by the unitary-normalized Fourier basis with eigenvalues \(W_m(s)\); the image is the complement-invariant subspace because even-weight frequencies form its complete character support.

**4. Sharp prime formulas.** For \(m=p\) prime, the only proper repetition count of a balanced word is \(r=p\), so \(H_p\setminus B_p\) comprises exactly the two alternating words \(1010\cdots10\) and \(0101\cdots01\). Their total character sum is zero at odd \(|s|\), and at even \(|s|\) is \(2\varepsilon(s)\). Subtracting it from the Krawtchouk value proves the formula for \(W_p(s)\). A frequency of weight \(2j\) is obtained by choosing an even-position selection of size \(u\) and an odd-position selection of size \(2j-u\). The difference between the numbers with \(\varepsilon=+1\) and \(\varepsilon=-1\) is the coefficient of \(z^{2j}\) in \((1-z)^p(1+z)^p=(1-z^2)^p\), namely \((-1)^j\binom pj\). Combining this with their total \(\binom{2p}{2j}\) gives \(N_{j,\varepsilon}\).

The prime multipliers satisfy \(|W_p(s)|\ge A_j-2\ge M_p-2>0\). At either central weight \(2j=p\pm1\), frequencies with \(\varepsilon=(-1)^j\) exist and attain exactly \(M_p-2\). Summing their two multiplicities gives \(\binom{2p}{p-1}+\binom{p}{(p-1)/2}\). The triangle inequality bounds every multiplier by \(|B_p|=Q_p-2\), with equality at \(s=0\); the singular-value and condition-number assertions follow.

**5. Asymptotic sharp conditioning for every odd half-length.** The bound \(R_m\le S_m=O(4^{m/3})\) and the central-binomial estimate give \(R_m/M_m\to0\). The least positive multiplier lies between \(M_m-R_m\) and \(M_m+R_m\), the upper bound obtained by evaluating a frequency of Hamming weight \(m-1\), where the central slice multiplier has magnitude \(M_m\). The largest multiplier is exactly \(|B_m|=\binom{2m}{m}-R_m\), attained at the zero frequency. Stirling's formula yields
\[
M_m\sim 2^m\sqrt{\frac2{\pi m}},\qquad \binom{2m}{m}\sim\frac{4^m}{\sqrt{\pi m}},
\]
so the visible condition number satisfies \(\kappa_m\sim2^m/\sqrt2\).

## Verification
The standalone \(\texttt{check_exact.py}\) constructs all fixed-weight words, tests their least period directly, and computes the complete integer Walsh transform by the butterfly algorithm for half-lengths \(m=3,5,7,9\). It verifies support, Parseval, positive multiplier bounds and the exact prime formulas. The independent \(\texttt{check_symbolic.py}\) enumerates the signed prime multiplier multiplicities by binomial counts for \(p=3,5,7,11,13\), checks their totals and sharp extrema, and tests the finite bound at the five small odd cases. Both programs use only the Python standard library. Their finite computations corroborate, but are not substitutes for, the all-odd proof above.

## Relationship to prior work
Ruskey and Sawada's 1999 work gives fixed-density necklaces and Lyndon-word enumeration, including the Möbius formula for their numbers, but does not give a character-by-character Fourier transform or its inverse conditioning. Kopparty, Kumar and Saks (2015) study necklace indexing, again rather than additive convolution on the full labelled fixed-content orbit set. The classical Krawtchouk transform describes the whole Hamming layer; the present claim instead determines how deleting **all nonprimitive balanced words** affects its Fourier support, and gives exact prime-order signed multiplier multiplicities and sharp stability. Neither the necklace-count formula nor the full-layer transform alone supplies this deletion theorem. Earlier results on unrestricted primitive words give a different support set and do not imply that a prescribed fixed-weight subfamily has no additional zeros.

## Limitations
The rank theorem requires odd half-length \(m\ge3\), and the fully explicit multiplier multiplicities require \(m\) prime; for composite odd \(m\), no exact smallest multiplier is claimed. The Fourier transform is on all position-labelled words, not orbit representatives. The result does not classify even half-lengths, different weights, nonbinary alphabets, or arbitrary subfamilies. The originality comparison is bounded by accessible historical records and primary sources; it is not an independent priority determination. Numerical tests cover only the stated finite ranges and do not certify the infinite assertions.

## References
1. F. Ruskey and J. Sawada, *An Efficient Algorithm for Generating Necklaces with Fixed Density*, SIAM Journal on Computing **29** (1999), 671–684, DOI: [10.1137/S0097539798344112](https://doi.org/10.1137/S0097539798344112). Author-accessible text: https://skeeter.socs.uoguelph.ca/~sawada/papers/fix.pdf. First verified online publication: 1999-11-23.
2. S. Kopparty, M. Kumar and M. Saks, *Efficient Indexing of Necklaces and Irreducible Polynomials over Finite Fields*, arXiv:1504.00572, first version 2015-04-02; https://arxiv.org/abs/1504.00572. The earlier ICALP 2014 conference version is acknowledged in this source.
