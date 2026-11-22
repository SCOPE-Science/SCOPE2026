# Exact three-square obstruction densities for every higher even generalized derangement parameter

## Finding

Let \(v\ge4\) be an even integer. Define the generalized derangement numbers by
\[
D^{(v)}_0=1,\qquad D^{(v)}_1=v,\qquad
D^{(v)}_n=(n+v-1)D^{(v)}_{n-1}+(n-1)D^{(v)}_{n-2}\quad(n\ge2).
\]
Write \(S_v=\{n\ge0:D^{(v)}_n\text{ is not a sum of three integer squares}\}\), and let \(\nu_2\) denote the binary valuation. There is a unique odd \(2\)-adic integer \(\xi_v\) such that, for **every positive odd integer** \(n\),
\[
\boxed{\nu_2(D^{(v)}_n)=\nu_2(n-\xi_v).}
\]
Every even-indexed term is odd. More precisely, the odd-index interpolation of the derangements is an exact isometry from \(1+2\mathbb Z_2\) onto \(2\mathbb Z_2\). For every \(j\ge1\), there is a unique odd residue \(a_{v,j}\pmod{2^{2j+3}}\) determined constructively by
\[
D^{(v)}_{a_{v,j}}\equiv 7\cdot 2^{2j}\pmod {2^{2j+3}}.
\]
The complete exceptional set is the disjoint union
\[
\boxed{S_v=\left(\bigcup_{j\ge1}\{n\ge0:n\equiv a_{v,j}\pmod{2^{2j+3}}\}\right)
\cup\begin{cases}
\{n\ge0:n\equiv v\pmod8\},&v\equiv2\pmod4,\\
\varnothing,&v\equiv0\pmod4.
\end{cases}}
\]
Consequently, for every such \(v\),
\[
\boxed{\#\{0\le n<X:n\in S_v\}=\delta_v X+O_v(\log(2+X)),\qquad
\delta_v=\begin{cases}1/24,&4\mid v,\\1/6,&v\equiv2\pmod4.\end{cases}}
\]
This supplies an effective valuation algorithm and exact index classifications for the higher even parameters left open in Ulas (2023). The classical case \(v=0\) and the special case \(v=2\) were settled previously and are **not** claimed as new here.

## Assumptions and scope

The parameter \(v\) is a fixed positive even integer at least four; \(n\) ranges over all nonnegative ordinary integer indices. A three-square representation allows zero and negative summands. Its absence is equivalent, by Legendre's theorem, to the value being of the form \(4^j(8u+7)\), \(j,u\ge0\). The assertion is not about cycle-restricted derangements in wreath products. The unique \(2\)-adic root \(\xi_v\) need not be a rational or an ordinary integer and is defined by the convergent interpolation below.

For a finite algorithm to obtain its digits, begin with \(r_{v,1}=1\). Given the unique odd residue \(r_{v,k}\pmod{2^k}\) with \(D^{(v)}_{r_{v,k}}\equiv0\pmod{2^k}\), choose \(r_{v,k+1}\) as the unique one of \(r_{v,k}\) or \(r_{v,k}+2^k\) whose generalized derangement number vanishes modulo \(2^{k+1}\). The resulting compatible residues converge to \(\xi_v\); therefore \(\nu_2(D^{(v)}_n)\) for odd \(n\) is exactly the highest matching root-digit precision \(k\). Similarly, \(a_{v,j}\) can be found by a finite computation in one residue period of size \(2^{2j+3}\).

## Proof

**1. Interpolation and its exact odd-input metric.** Put \(P_0(X)=1\) and \(P_j(X)=X(X-1)\cdots(X-j+1)\) for \(j\ge1\). The inclusion–exclusion definition of generalized derangements gives
\[
D^{(v)}_n=(-1)^n\sum_{j=0}^{n}(-1)^j\binom{v+j}{j}P_j(n).
\]
Define the \(2\)-adic function
\[
F_v(x)=\sum_{j\ge0}(-1)^j\binom{v+j}{j}P_j(x),\qquad x\in\mathbb Z_2.
\]
The series converges uniformly: among any \(j\) consecutive integers \(x,x-1,\ldots,x-j+1\), at least \(\lfloor j/2\rfloor\) are even, uniformly for \(x\in\mathbb Z_2\). For ordinary nonnegative integers, the series terminates and \(F_v(n)=(-1)^nD^{(v)}_n\).

For two odd \(2\)-adic integers \(x,y\), the difference quotient of \(P_j\) is an integral polynomial \(Q_j(x,y)=(P_j(x)-P_j(y))/(x-y)\). The telescoping product identity expresses \(Q_j\) as a sum of \(j\) terms, each containing all but one of the factors with offsets \(0,\ldots,j-1\), evaluated at \(x\) or \(y\). Each summand is divisible by at least \(2^{\lfloor j/2\rfloor-1}\), hence the quotient series also converges uniformly. Modulo two, because \(x,y\) are odd, \(Q_j(x,y)\) is the formal derivative \(P'_j(1)\). It equals one for \(j=1,2,3\) and zero for \(j=0\) or \(j\ge4\) (for \(j\ge4\), at least two factors of \(P_j\) vanish at one modulo two). Therefore
\[
\frac{F_v(x)-F_v(y)}{x-y}\equiv
\binom{v+1}{1}+\binom{v+2}{2}+\binom{v+3}{3}\equiv1\pmod2.
\]
The last congruence holds for every even \(v\): when \(v\equiv0\pmod4\), all three summands are odd; when \(v\equiv2\pmod4\), only the first is odd. By continuity, the same difference-quotient formula applies also at the diagonal. Thus
\[
\nu_2(F_v(x)-F_v(y))=\nu_2(x-y),\qquad x,y\in1+2\mathbb Z_2,\quad x\ne y.
\]
In particular, \(F_v\) is an isometry on the entire odd domain.

**2. Complete even output ball and valuation root.** The recurrence modulo two gives \(D^{(v)}_n\) odd exactly when \(n\) is even. Thus \(F_v(1+2\mathbb Z_2)\subseteq2\mathbb Z_2\). At precision \(2^k\), the isometry maps the \(2^{k-1}\) odd residues injectively to the \(2^{k-1}\) even residues, and hence bijectively. Passing to compatible inverse limits shows that the image is exactly \(2\mathbb Z_2\); there is exactly one odd root \(\xi_v\) of \(F_v\). Taking \(y=\xi_v\) proves \(\nu_2(F_v(n))=\nu_2(n-\xi_v)\), hence the stated valuation for odd \(n\). The finite root-lifting algorithm follows from the same exact residue bijection.

**3. Even-indexed residues.** For every even \(v\) and integer \(t\ge0\), the recurrence gives
\[
D^{(v)}_{2t}\equiv 1-vt\pmod8.
\]
For completeness this finite-modulus identity can be verified without assuming any infinite periodicity: the recursion has coefficients periodic in both \(n\) and \(v\) modulo eight. Direct application of the recursion at \(n=0,1,\ldots,9\) for the four cases \(v\equiv0,2,4,6\pmod8\) gives \((D^{(v)}_8,D^{(v)}_9)\equiv(D^{(v)}_0,D^{(v)}_1)\pmod8\); induction then proves eight-periodicity in \(n\). The four resulting rows of even-index values at \(n\equiv0,2,4,6\pmod8\) are, respectively, \((1,1,1,1)\), \((1,7,5,3)\), \((1,5,1,5)\), and \((1,3,5,7)\). They are precisely \(1-vt\pmod8\). Since even-indexed terms are odd, Legendre's theorem excludes exactly \(n\equiv v\pmod8\) when \(v\equiv2\pmod4\), and no even index otherwise.

**4. Odd-indexed exceptions and density.** For odd \(n\), the term is even, and its valuation can only be of forbidden three-square shape if its valuation is \(2j\) with \(j\ge1\), and its odd part is \(7\pmod8\). This condition is equivalent to
\[
D^{(v)}_n\equiv7\cdot2^{2j}\pmod{2^{2j+3}}.
\]
By the odd-domain isometry and bijection in step 2, this is exactly one index residue class \(a_{v,j}\) modulo \(2^{2j+3}\), and the classes are pairwise disjoint because they have distinct exact valuations. Their total density is
\[
\sum_{j\ge1}2^{-(2j+3)}=\frac1{24}.
\]
To justify an effective counting error, fix \(X\ge2\) and choose \(J\) with \(2^{2J}>X\) and \(J=O(\log X)\). The contributions from the first \(J-1\) progressions differ from their predicted density terms by \(O(J)\). All remaining progressions impose \(n\equiv\xi_v\pmod{2^{2J}}\) and therefore contribute at most one index in \(0\le n<X\); the omitted density tail contributes \(O(1)\). This proves an \(O(\log X)\) error. Add the disjoint even-index progression from step 3, of density \(1/8\) when \(v\equiv2\pmod4\), to obtain \(1/24\) or \(1/24+1/8=1/6\), as claimed.

## Verification

Run `python3 CHECK.py` using only the Python 3 standard library. It independently generates the recurrence modulo each \(2^k\), for all \(16\) even parameters \(0\le v\le30\) and each \(1\le k\le11\), including the previously known boundary parameters as controls. It exhaustively checks \(32,752\) odd-index fibers, verifies each is bijective onto the even residues, checks the even-index modulo-eight formula, confirms low-shell three-square obstruction multiplicities, verifies unique roots at each modulus, and directly checks the difference-valuation identity for pairs of small odd indices with exact integers. Example new exception residues: \(v=4\) gives \(9\pmod{32}\), \(53\pmod{128}\); \(v=6\) gives \(11\pmod{32}\), \(87\pmod{128}\). Finite checks are corroboration, not the universal proof.

## Relationship to prior work

Ulas, *Representing Generalized Derangements as Sums of Three Squares* (*Fibonacci Quarterly*, 2023), Section 4, explicitly poses the even-parameter classification (Problem 4.1), the unresolved dyadic valuations (Problem 4.2), and existence of the density (Question 4.3). It proves results for \(v=0\) and odd \(v\), and obtains lower bounds for even \(v\); the exact higher-even-parameter density and one-residue-per-shell description above are not in that paper. O'Desky and Richman (arXiv:2012.04615, first publicly posted 2020-12-08) study continuity and other derangement-family \(p\)-adic interpolations, which motivates the method but does not give this parameter-indexed family and its three-square exceptional density. An existing separate result completely covers the case \(v=2\) with a stronger global isometry, and previous work covers the classical case \(v=0\); neither is claimed to be discovered here. Published classical-derangement dyadic fiber results concern \(v=0\), not the new uniform family \(v\ge4\).

## Limitations

The root \(\xi_v\) is specified as a computable unique \(2\)-adic integer rather than by a closed elementary formula. The theorem is not about arbitrary odd parameters or sums of two squares, nor does it claim priority for the previously settled \(v=0,2\) cases. Literature priority remains subject to unindexed or implicitly stronger results; a full-text comparison was completed for Ulas and for the general \(p\)-adic framework, while full source material for some indexed contemporary findings was inaccessible. No independent mathematical audit has been performed.

## References

- M. Ulas, *Representing Generalized Derangements as Sums of Three Squares*, *Fibonacci Quarterly* 61 (2023), 231–239, especially Section 4, Problems 4.1–4.2 and Question 4.3. https://www.fq.math.ca/Papers/61-3/ulas11202022.pdf
- A. O'Desky and D. H. Richman, *Derangements and the p-adic incomplete gamma function*, arXiv:2012.04615, initial preprint 2020-12-08; *Transactions of the American Mathematical Society* 376 (2023), 1065–1087. https://arxiv.org/html/2012.04615v4
- P. Miska, *Arithmetic properties of the sequence of derangements*, *Journal of Number Theory* 163 (2016), 114–145, for classical derangement congruences.
- Legendre's three-squares theorem: a nonnegative integer is excluded precisely when it is of the form \(4^j(8u+7)\) for integers \(j,u\ge0\).
