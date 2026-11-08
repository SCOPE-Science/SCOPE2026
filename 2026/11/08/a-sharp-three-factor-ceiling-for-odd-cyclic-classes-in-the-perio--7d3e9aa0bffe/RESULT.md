# A sharp three-factor ceiling for odd cyclic classes in the period-doubling word

## Finding
Let \(p=p_0p_1\cdots\) be the binary fixed point of \(\mu(0)=01\), \(\mu(1)=00\). Let \(F_n\) denote its set of distinct contiguous factors of length \(n\), and, for \(u\in F_n\), let
\[
\kappa_n(u)=\bigl|F_n\cap\{u_i\cdots u_{n-1}u_0\cdots u_{i-1}:0\le i<n\}\bigr|.
\]
For **every odd positive integer** \(n\) and **every** \(u\in F_n\), one has
\[
\boxed{\kappa_n(u)\le3.}
\]
This uniform ceiling is sharp at infinitely many odd lengths: for every \(j\ge1\) there exists a factor \(u\) of length \(2^{2j}+1\) with \(\kappa_{2^{2j}+1}(u)=3\).

Writing \(c_p(n)\) for the number of represented cyclic-conjugacy classes and \(P_p(n)=|F_n|\), it follows that
\[
\boxed{c_p(n)\ge\left\lceil P_p(n)/3\right\rceil\ge\left\lceil(n+1)/3\right\rceil\quad(n\ \mathrm{odd}).}
\]
Combined with the established values \(c_p(2^k)=2\), this gives \(\liminf_{n\to\infty}c_p(n)/n=0\) while \(\limsup_{n\to\infty}c_p(n)/n\ge1/3\).

## Assumptions and scope
Indices are zero-based. A cyclic-conjugacy class is intersected with the *actual factor language* \(F_n\); absent rotations do not count. The bound concerns class cardinalities at odd lengths, not the complete numerical function \(c_p(n)\), not Lie complexity (which requires all rotations to occur), and not other binary automatic words. For length one the bound holds trivially. All occurrences are contiguous, not scattered.

## Proof
**1. Two elementary restrictions.** By the substitution,
\[
p_{2r}=0,\qquad p_{2r+1}=1-p_r\qquad(r\ge0).
\]
Thus every occurrence of \(1\) in the infinite word is at an odd absolute position; in any factor, all \(1\)'s therefore have local indices of one common parity. There is no occurrence of `11`, because every other position is zero. There is also no occurrence of `0000`: any four consecutive zeros include two consecutive *odd-position* entries \(p_{2r+1}=p_{2r+3}=0\), which would force \(p_r=p_{r+1}=1\), impossible. Consequently the initial and terminal zero runs of any factor have length at most three.

**2. The unique even cyclic gap.** Fix odd \(n\) and a factor \(u\in F_n\) containing at least one \(1\). List the locations of its \(1\)'s in linear order. Every internal zero gap between successive ones has odd size, since the ones share a parity. The *remaining* cyclic gap, connecting the last one back to the first one around the circle, has even size: explicitly, if the first and last one have positions \(a,b\) of the same parity, this gap is \(n-1-b+a\), which is even because \(n\) is odd. Hence the cyclic gap list has exactly one even gap.

Any rotation which is also a factor of \(p\) likewise has all ones in a single local parity. Its internal gaps must therefore be odd, so its boundary must cut the same unique even cyclic gap. Call the number of zeros in this gap \(g\). A cut distributes them as \(\ell\) leading and \(g-\ell\) trailing zeros, with both quantities at most three by Step 1. Therefore \(g\in\{0,2,4,6\}\), and the number of *possible* cuts is at most
\[
\#\{\ell\in\mathbb Z:0\le\ell\le g,\ \ell\le3,\ g-\ell\le3\}
=\begin{cases}1,&g=0,6,\\3,&g=2,4.\end{cases}
\]
These are upper bounds, irrespective of whether the resulting rotations actually appear. Consequently \(\kappa_n(u)\le3\). If \(u\) contains no \(1\), it is a constant word and has exactly one distinct rotation. This proves the bound for every odd \(n\), including \(n=1\).

**3. Infinite sharpness.** For \(j\ge1\), put \(B=\mu^{2j}(0)\), of length \(m=2^{2j}\). The block \(B\) begins with `01` and ends with `00`. The latter is immediate for \(j=1\), when \(\mu^2(0)=0100\), and persists under each pair of substitution iterations: if a nonempty word ends with `00`, its image under \(\mu^2\) ends with \(\mu^2(0)=0100\). Since `00` is a factor of \(p\), applying \(\mu^{2j}\) shows \(BB\) is also a factor of \(p\).

The following three length-\(m+1\) words all occur inside \(BB\):
\[
B0,\qquad 0B,\qquad 00B[0:m-1],
\]
where \(B[0:m-1]\) means the length-\(m-1\) prefix of \(B\). They are the first word and its right rotations by one and two positions, respectively, since \(B\) ends in `00`. They are distinct because their respective initial patterns are `01`, `001`, and `0001`. Thus one cyclic class has at least three represented factors, and Step 2 makes that number exactly three.

**4. Growth consequence.** The word \(p\) is aperiodic: the elementary identity \(p_i=\nu_2(i+1)\bmod2\) follows from Step 1. If a tail had period \(t\ge1\), taking \(i=2^s-1\) with \(s>\nu_2(t)\) arbitrarily large would give \(p_i=s\bmod2\) but \(p_{i+t}=\nu_2(t)\bmod2\), contradicting tail periodicity as the parity of \(s\) varies. Morse–Hedlund therefore yields \(P_p(n)\ge n+1\). Since each represented class contains at most three factors at odd length, \(c_p(n)\ge\lceil P_p(n)/3\rceil\). The normalized-growth assertions now follow using the known dyadic equality \(c_p(2^k)=2\) from the first cited paper.

## Verification
The attached standalone Python program `verify.py` checks the odd-length class bound by explicit factor-set and cyclic-rotation enumeration for all 65 odd lengths through 129. It compares factor sets obtained from substitution prefixes of lengths \(2^{14}\) and \(2^{15}\) before counting, and checks the three explicit sharpness witnesses for \(j=1,\ldots,5\) against a prefix of length \(2^{16}\). The observed output is `VERIFY_OK odd_lengths=65 sharp_constructions=5`. These finite checks do not establish the universal statement; the proof above does. Run with `python3 verify.py` using only the Python standard library.

## Relationship to prior work
Cassaigne, Fici, Sciortino, and Zamboni introduced cyclic complexity and established \(c_p(2^k)=2\) for the period-doubling word; their relevant proof in Section 5.1 does not bound how many *represented* cyclic rotations one odd-length factor can have. Charlier, Puzynina, and Zamboni study general group-action complexity lower bounds; these do not force a uniform odd-length class-cardinality ceiling. Bell and Shallit study *complete* rotation orbits (Lie complexity), whereas this theorem counts the members of arbitrary partially represented orbits. The odd-length ceiling is not a reformulation of any of these theorems, nor does the dyadic equality entail it.

## Limitations
No exact formula for the odd-length class counts \(c_p(n)\) or the distribution of class sizes is claimed. Sharpness is proved for the stated infinite sequence of odd lengths, not for every odd length. The comparison with known work is based on the inspected relevant portions of accessible primary sources and searched records; a comprehensive independent historical-priority audit has not been conducted.

## References
1. J. Cassaigne, G. Fici, M. Sciortino, L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843, first submitted February 24, 2014, especially Section 5.1. https://arxiv.org/abs/1402.5843
2. E. Charlier, S. Puzynina, L. Q. Zamboni, *On a group theoretic generalization of the Morse-Hedlund theorem*, arXiv:1505.03848, first submitted May 14, 2015, especially Sections 1–2. https://arxiv.org/abs/1505.03848
3. J. P. Bell, J. Shallit, *Lie Complexity of Words*, arXiv:2102.03821, first submitted February 7, 2021, especially Sections 1–2 and 7. https://arxiv.org/abs/2102.03821
