# Parity-selective longitudinal magnetization of open antiferromagnetic delta chains

## Finding
For every integer \(m\ge 2\), the equal-bond classical antiferromagnetic Ising model on the open chain of \(m\) corner-sharing triangles has the following exact ground energies, magnetizations and labeled-spin degeneracies for all longitudinal fields \(h\ge0\). Put \(x=h/J\), \(J>0\), and \(E_m/J=e_m(x)\). Magnetization means the sum of all \(2m+1\) spins, not a normalized density.

At \(x=0\), \(e_m=-m\) and the degeneracy is \(2\cdot3^m\); this established zero-field count is recalled for completeness and is not claimed as new.

For **even** \(m\):

| Field range | \(e_m(x)\) | Magnetization | Degeneracy |
|---|---|---|---|
| \(0<x<4\) | \(-m-(m+1)x\) | \(m+1\) | \(1\) |
| \(x=4\) | \(-5m-4\) | several sectors | \(F_{m+1}\) |
| \(x>4\) | \(3m-(2m+1)x\) | \(2m+1\) | \(1\) |

For **odd** \(m\):

| Field range | \(e_m(x)\) | Magnetization | Degeneracy |
|---|---|---|---|
| \(0<x<2\) | \(-m-mx\) | \(m\) | \(m+2\) |
| \(x=2\) | \(-3m\) | \(m\) or \(m+2\) | \((3m+5)/2\) |
| \(2<x<4\) | \(4-m-(m+2)x\) | \(m+2\) | \((m+1)/2\) |
| \(x=4\) | \(-5m-4\) | several sectors | \(F_{m+1}\) |
| \(x>4\) | \(3m-(2m+1)x\) | \(2m+1\) | \(1\) |

Here \(F_0=0\), \(F_1=1\), \(F_{k+2}=F_{k+1}+F_k\). At the odd-parity transition \(x=2\), exactly \(m+2\) ground states have magnetization \(m\) and \((m+1)/2\) have magnetization \(m+2\). At \(x=4\), all ground states correspond bijectively to independent subsets of a path on \(m-1\) vertices. The one-sided zero-temperature entropy per spin is zero for every fixed \(0<x<4\); at the isolated field \(x=4\) it tends to \(\frac12\log\varphi\), with \(\varphi=(1+\sqrt5)/2\). The zero-field entropy \(\frac12\log3\) is established prior knowledge.

In particular, \(h=2J\) is a finite-size transition **only when \(m\) is odd**; saturation coexistence at \(h=4J\) occurs for both parities.

## Assumptions and scope
Label the lower-chain vertices \(b_0,b_1,\ldots,b_m\) and the triangle tips \(t_1,\ldots,t_m\). For every \(1\le i\le m\), include precisely the three edges \(b_{i-1}b_i\), \(b_{i-1}t_i\), \(b_it_i\). All spins are \(\sigma_v\in\{-1,+1\}\), all bonds have equal positive antiferromagnetic exchange \(J\), and the longitudinal field is \(h\ge0\):
\[
\mathcal H(\sigma)=J\sum_{uv\in E}\sigma_u\sigma_v-h\sum_v\sigma_v.
\]
There are free/open boundaries, no periodic closure, no transverse or quantum-spin interaction, and no implicit factor of \(1/2\) in spin normalization. A labeled ground state distinguishes vertex positions.

## Proof
Every triangle with both spin signs has exchange energy \(-J\), whereas a monochromatic triangle has \(3J\). If \(f(\sigma)\) counts monochromatic triangles and \(M(\sigma)=\sum_v\sigma_v\), then
\[
\mathcal H(\sigma)/J=-m+4f(\sigma)-xM(\sigma).\tag{1}
\]
At \(x=0\), each triangle independently has three choices of frustrated edge, with two choices for the first base spin; thus the count \(2\cdot3^m\), in agreement with the established zero-field calculation.

**Fields \(0<x<2\).** A monochromatic plus triangle can be made mixed by flipping its tip, lowering its energy by \(4J-2h>0\); a monochromatic minus triangle can similarly be made mixed and gains \(4J+2h>0\). Consequently \(f=0\) in all ground states. For a fixed sequence of base spins the tip that maximizes total magnetization is \(-1\) on a \((+,+)\) base pair and \(+1\) otherwise. Write \(f_b\) for the number of minus base spins and \(u_b\) for the number of adjacent \((+,+)\) base pairs. The maximal magnetization at these bases is
\[
M=2m+1-2(f_b+u_b).\tag{2}
\]
The minimum \(f_b+u_b\), over base sequences of length \(L=m+1\), is \(\lfloor L/2\rfloor\). Its number of minimizers is \(1\) if \(L\) is odd and \(L+1\) if \(L\) is even. One exact derivation uses generating polynomials \(P_L^+\) and \(P_L^-\), split by terminal base spin, with initial conditions \(P_1^+=1\), \(P_1^-=q\) and recurrences
\[
P_{L+1}^+=qP_L^++P_L^-,\qquad P_{L+1}^-=q(P_L^++P_L^-).\tag{3}
\]
The lowest nonzero power of \(q\) in their sum is \(\lfloor L/2\rfloor\), with coefficient \(1\) for odd \(L\) and \(L+1\) for even \(L\); induction in (3) proves these values. Inserting (2) into (1) yields precisely the first open-field rows of both tables, including their counts.

**The field \(x=2\).** At a \((+,+)\) base pair, the tip may instead be plus, creating one monochromatic triangle but gaining two units of magnetization; the changes cancel in (1). All other tip choices remain forced. Thus each base sequence is weighted by \(2^{u_b}\). Replace the first recurrence in (3) by
\[
P_{L+1}^+=2qP_L^++P_L^-,\tag{4}
\]
leaving the other recurrence unchanged. The minimum power remains \(\lfloor L/2\rfloor\); induction gives leading coefficient \(1\) for odd \(L\) and \(3L/2+1\) for even \(L\). Hence the even-\(m\) count is one and the odd-\(m\) count is \((3m+5)/2\). The lower-field \(m+2\) configurations persist; the additional \((m+1)/2\) configurations have magnetization larger by two. In particular, the two energy branches cross only for odd \(m\).

**Fields \(x>2\) and saturation.** Let \(S\) be the set of minus spins, and \(I=\{b_1,\ldots,b_{m-1}\}\), the interior base vertices, each of degree four; all other vertices have degree two. Let \(e(S)\) count edges internal to \(S\). Directly comparing to the fully plus configuration gives
\[
\mathcal H(S)-\mathcal H(\varnothing)=2J\big[(x-4)|S\cap I|+(x-2)|S\setminus I|+2e(S)\big].\tag{5}
\]
For \(x>2\), no minimizing set contains a vertex outside \(I\): deleting one decreases (5), and cannot add internal edges. The induced graph on \(I\) is a path on \(m-1\) vertices. For \(2<x<4\), each occupied component of this path has cost \(2J[(x-2)\ell-2]\), with \(\ell\) its number of vertices. Since \(x-2>0\), a minimizing component must be a singleton. Each additional independent singleton reduces the energy, as \(x-4<0\), so minimizing sets are **maximum-cardinality independent sets** of the path. Their cardinality is \(\lfloor m/2\rfloor\), and their number is \(1\) when \(m\) is even and \((m+1)/2\) when \(m\) is odd. Substitution in (5) yields both middle-field branches. At \(x=4\), the surviving subsets are *all* independent sets of that path, counted by \(F_{m+1}\). For \(x>4\), only the empty set minimizes (5), giving full polarization. This completes all field ranges.

## Verification
The accompanying standalone `check.py` uses only Python 3's standard library. Run `python3 check.py` to obtain `OPEN_DELTA_EXACT_CHECKS_PASSED 694`. It compares the closed formulas with independent exact two-state dynamic programming for \(m=2,\ldots,45\) and eleven half-integer fields from zero through five; it also uses exhaustive spin enumeration for \(m=2,\ldots,7\) and verifies the leading-coefficient recurrences for base lengths three through seventy-four. The all-size theorem is proved above; finite verification is supplementary, not its substitute.

## Relationship to prior work
Priour, Gelfand and Sondhi [1] introduced this fully frustrated Ising triangle chain and explicitly obtained the zero-longitudinal-field free-boundary multiplicity \(2\cdot3^m\). They investigated how a *transverse quantum field* lifts that entropy; the zero-field count is therefore prior art, not a claimed discovery here. Kunisada and Fukumoto [2] analyzed transverse susceptibilities and a different, periodic-field formulation. Derzhko and Richter [3] discussed finite residual entropies at saturation fields in quantum localized-magnon systems; the broad entropy mechanism and Fibonacci connection are not asserted to be new. The distinct contribution here is the exact *classical longitudinal-field*, *open-boundary*, *all-size* parity classification, including the odd-only crossing at \(2J\), its magnetization-resolved multiplicity, and the precise Fibonacci count at \(4J\).

## Limitations
The result concerns a zero-temperature classical model, not finite-temperature nonanalyticities or quantum transverse fields. The entropy spikes are isolated-field, thermodynamic-sequence limits, and do not assert a positive-temperature phase transition. The energy and degeneracy count depend on free boundaries and equal exchange weights; they should not be transferred to rings or anisotropic chains without fresh analysis. While relevant open literature was compared with the exact statements, priority beyond the examined sources remains subject to comprehensive independent scholarly review.

## References
[1] D. J. Priour Jr., M. P. Gelfand and S. L. Sondhi, *Disorder from Disorder in a Strongly Frustrated Transverse Field Ising Chain*, arXiv:cond-mat/0005185v1 (first public 2000-05-11). https://arxiv.org/abs/cond-mat/0005185

[2] N. Kunisada and Y. Fukumoto, *An exact calculation of the transverse susceptibility for an antiferromagnetic Ising Delta chain*, arXiv:0712.4306v1 (2007-12-28). https://arxiv.org/abs/0712.4306

[3] O. Derzhko and J. Richter, *Finite low-temperature entropy of some strongly frustrated quantum spin lattices in vicinity of the saturation field*, arXiv:cond-mat/0404204 (2004-04-08). https://arxiv.org/abs/cond-mat/0404204
