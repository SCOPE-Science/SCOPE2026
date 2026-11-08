# Exact isomorphism-class enumerator for two-state bireversible Mealy automata

## Finding
For every integer \(k\ge1\), let \(U_k\) count isomorphism types of *total* two-state, \(k\)-letter bireversible Mealy automata. Isomorphism permits any single permutation of the states and any single permutation of the alphabet, applied **simultaneously to input and output labels**; no initial state is marked. The count is

\[
U_k=\frac12\sum_{\lambda\vdash k}\left[z_\lambda\prod_{j\ge1}(m_j+1)+\frac{1}{z_\lambda}\prod_{j\ge1}\left(j^{N_j}\sum_{r=0}^{N_j}c_{j,r}^2r!(N_j-r)!\right)\right],
\]
where, for the partition \(\lambda\), \(m_j\) is the multiplicity of the part \(j\), \(z_\lambda=\prod_{j\ge1}j^{m_j}m_j!\), \(N_j=\mathbf1_{j\text{ odd}}m_j+2m_{2j}\), and \(c_{j,r}\) is the coefficient of \(x^r\) in \((1+x)^{\mathbf1_{j\text{ odd}}m_j}(1+x^2)^{m_{2j}}\). Factors with \(N_j=0\) equal one. The first nine values for \(k=1,\ldots,9\) are \(2,8,28,124,570,3446,24084,203188,1950918\).

## Assumptions and scope
A Mealy automaton is a pair of maps \(\delta:Q\times X\to Q\), \(\rho:Q\times X\to X\), with \(Q=\{0,1\}\) and \(X=\{1,\ldots,k\}\). It is invertible when each \(\rho(q,\cdot)\) is a permutation, reversible when each \(\delta(\cdot,x)\) is a permutation, and bireversible when both it and its inverse letter transducer are reversible. Isomorphisms of automata relabel \(Q\) and \(X\) independently but preserve the input/output alphabet identification. This is a finer relation than arbitrary four-coordinate isotopy and coarser than literal equality of labeled machines. No claim about isomorphism of their generated groups is made.

## Proof
**1. Parametrization.** Reversibility with two states means there is a switch function \(e:X\to\{0,1\}\) with \(\delta(q,x)=q\oplus e(x)\). Invertibility gives two output permutations \(a=\rho(0,\cdot)\), \(b=\rho(1,\cdot)\). The inverse transducer is reversible precisely when \(e(a^{-1}(y))=e(b^{-1}(y))\) for every output letter \(y\). Equivalently, \(h=a^{-1}b\) preserves the two color classes of \(e\). Thus the complete labeled data are \((e,a,h)\) with \(a\in S_k\) and \(h\in S_{e^{-1}(0)}\times S_{e^{-1}(1)}\). For \(r=|e^{-1}(1)|\) there are \(\binom kr k!r!(k-r)!= (k!)^2\) choices; summing \(r\) gives \((k+1)(k!)^2\).

**2. Burnside without state swap.** Let an alphabet relabeling \(\tau\in S_k\) have cycle type \(\lambda\). A fixed triple has \(e\circ\tau=e\), and both \(a,h\) commute with \(\tau\). The centralizer \(C(\tau)\) has order \(z_\lambda\). Color the \(m_j\) cycles of length \(j\), choosing \(r_j\) of them for color 1. The subgroup \(C(\tau)\) preserving those colors has size \(\prod_j j^{m_j}r_j!(m_j-r_j)!\). Summing over cycle-colorings gives \(z_\lambda\prod_j(m_j+1)\) choices of \((e,h)\), then multiplying by the \(z_\lambda\) choices of \(a\) gives \(z_\lambda^2\prod_j(m_j+1)\) fixed machines.

**3. Burnside with state swap.** A fixed machine for simultaneous state exchange and alphabet relabeling \(\tau\) must satisfy \(e\circ\tau=e\), \(b=\tau a\tau^{-1}\), and \(a=\tau b\tau^{-1}\). Hence \(a\in C(\tau^2)\), while the inverse-reversibility condition says \(a(e^{-1}(1))\) is invariant under \(\tau\). The cycles of length \(j\) of \(\tau^2\) comprise one cycle from every odd-length-\(j\) cycle of \(\tau\), and two cycles from every length-\(2j\) cycle of \(\tau\). Thus their number is \(N_j\). On these cycles, \(\tau\) fixes \(\mathbf1_{j\text{ odd}}m_j\) cycles and swaps \(m_{2j}\) pairs. A \(\tau\)-invariant chosen color class can select \(r\) of these \(N_j\) cycles in exactly \(c_{j,r}\) ways. For a fixed input color class, the permutation \(a\in C(\tau^2)\) can send it to any \(\tau\)-invariant output class of the same size. That gives another \(c_{j,r}\) choices, followed by \(r!(N_j-r)!\) permutations of the \(\tau^2\)-cycles and \(j^{N_j}\) rotations on them. Multiplying over \(j\), the number of fixed machines with state exchange is
\[
F_{\rm swap}(\tau)=\prod_{j\ge1}j^{N_j}\sum_{r=0}^{N_j}c_{j,r}^2r!(N_j-r)!.
\]
There is no hidden assumption that \(\tau\) has odd order: the paired cycles from even-length \(\tau\)-cycles are explicitly counted.

**4. Orbit count.** Burnside's lemma for the commuting action of \(S_k\times C_2\) divides the total fixed-point sum by \(2k!\). A conjugacy class of type \(\lambda\) has size \(k!/z_\lambda\). Inserting both preceding fixed-point counts gives exactly the displayed formula for every \(k\ge1\).

## Verification
The self-contained Python checker `checker.py` evaluates the cycle-index formula using integer arithmetic for \(1\le k\le9\) and, independently of the formula, enumerates every labeled automaton and explicitly constructs relabeling orbits for \(1\le k\le4\). It verifies the labeled count, the orbit count, and the nine reported values. The exhaustive enumeration covers **all** automata in these finite cases, but the formula for arbitrary \(k\) is justified by the preceding Burnside proof, not by computation.

## Relationship to prior work
Curtin and Savchuk (2026) develop general combinatorial characterizations of bireversible automata and their symmetries via Latin-type encodings. The present computation fixes the narrower standard notion of Mealy isomorphism and derives its complete two-state orbit enumerator by a cycle-splitting Burnside count. Woryna (2017), particularly the displayed two-state partition identities in the proof of Theorem 3, supplies a closely related structural description but not the stated simultaneous-relabeling orbit count. Godin (2019, Proposition 3.2) bounds the prevalence of bireversibility in random invertible reversible transducers, but does not enumerate their isomorphism types. The exact labeled count is an intermediate lemma, not the main contribution.

## Limitations
The count concerns complete two-state machines and standard state/alphabet isomorphism only. It is not a count of distinct automaton groups, parastrophy orbits, or four-coordinate isotopy classes. The full text of the highly relevant 2026 Curtin--Savchuk paper was not accessible for a final implicit-coverage check; the originality conclusion is provisional and historical priority could change. No independent mathematical audit has been performed.

## References
- B. Curtin and D. Savchuk, *Combinatorial structures connecting Latin squares and bireversible automata*, arXiv:2607.26013, first posted July 28, 2026, https://arxiv.org/abs/2607.26013.
- A. Woryna, *On groups generated by bi-reversible automata: The two-state case over a changing alphabet*, Journal of Computer and System Sciences 86 (2017), 181–190, https://doi.org/10.1016/j.jcss.2017.01.004.
- T. Godin, *Generic properties in some classes of automaton groups*, 2019, arXiv:1903.11315, https://arxiv.org/abs/1903.11315.
