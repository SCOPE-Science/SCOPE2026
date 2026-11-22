# Nine-site commensurate locking in the three-state range-three Potts antiferromagnet

## Finding
For every integer \(n\ge7\), consider the three-colour uniform antiferromagnetic Potts energy on the third power of a cycle. Its ground energy satisfies \(E_n\ge nJ/3\), with equality **if and only if** \(9\mid n\). On the divisible-by-nine subsequence, exactly 18 configurations attain equality: the three inequivalent shifts and all six named-colour permutations of the repeated word \(001220112\). Thus this frustrated family has ground-energy density \(J/3\), strictly finite degeneracy and zero ground-state entropy density on the commensurate subsequence.

## Assumptions and scope
Take integer \(n\ge7\), colours \(s_i\in\{0,1,2\}\) with indices modulo \(n\), and \(J>0\). Define
\[
E_n(s)=J\sum_{i=0}^{n-1}\sum_{d=1}^{3}\mathbf1\{s_i=s_{i+d}\}.
\]
For \(n\ge7\), every undirected edge of \(C_n^3\) occurs exactly once in this expression. The zero-field, zero-temperature problem is to minimize this energy over all \(3^n\) named configurations. No positive-temperature or finite-field claim is made.

## Proof
Let \(m_d=\sum_i\mathbf1\{s_i=s_{i+d}\}\) and let \(W_i\) count monochromatic pairs among the four consecutive sites indexed \(i,i+1,i+2,i+3\). Those four sites induce a complete graph, and three colours force \(W_i\ge1\) by the pigeonhole principle. Counting how often a pair belongs to such windows gives
\[
n\le\sum_{i=0}^{n-1}W_i=3m_1+2m_2+m_3\le3(m_1+m_2+m_3)=3E_n/J.
\]
Consequently \(E_n/J\ge n/3\). Suppose equality holds. The two inequalities must both be tight, so \(m_2=m_3=0\), \(W_i=1\) for every \(i\), and the only bad edges are nearest-neighbour ones. Writing \(b_i=\mathbf1\{s_i=s_{i+1}\}\), equality of each window implies \(b_i+b_{i+1}+b_{i+2}=1\). Subtraction of adjacent equalities yields \(b_{i+3}=b_i\). Hence exactly one of each three adjacent nearest-neighbour pairs is monochromatic; in particular \(3\mid n\).

Rotate indices so that \(b_0=1\). The first two sites carry the same colour \(a\). The next two sites have distinct colours \(b,c\), different from \(a\), because pairwise distances one to three are forbidden except across the designated nearest-neighbour bad bonds. Repeated use of the constraints \(m_2=m_3=0\) and the pattern \((b_0,b_1,b_2)=(1,0,0)\) forces the nine-site word
\[
a,a,b,c,c,a,b,b,c
\]
and the next site is again \(a\); this construction repeats with period nine. A cyclic sequence of this form can close with the required bond indicator pattern only if \(9\mid n\). Conversely, for every positive multiple \(n=9k\), repeating this word has exactly \(n/3\) monochromatic distance-one edges and none at distances two or three, hence attains the bound.

There are three possible phases for the position of the nearest-neighbour bad bond modulo three and six permutations of the named colours. Once those data are fixed, the preceding forcing argument fixes every spin. These 18 configurations are distinct, proving the exact degeneracy. The ground-state entropy density along \(n=9k\) is \(\lim_{k\to\infty}\log(18)/(9k)=0\). For \(3\mid n\) but \(9\nmid n\), the energy is at least \((n/3+1)J\) by integrality and strictness; for other sizes only the universal bound and the exact equality criterion are claimed.

## Verification
The included `verify.py` independently enumerates all named configurations for small rings and uses an integer min-plus transfer count on the 27 possible ordered triples for larger rings. It checks the complete equality condition, the 18-state degeneracy, a direct word construction, and the explicit finite-size energy gap away from equality. Exhaustive finite checks corroborate rather than replace the all-\(n\) proof above.

## Relationship to prior work
Tonegawa–Takasaki–Kaburagi (1985) rigorously determined the ground states of a one-dimensional three-state Potts system with first and **second** neighbour couplings and external fields; its stated interaction radius does not include the uniform third-neighbour ring considered here. Glumac–Uzelac (1993) developed finite-range transfer matrices for a power-law long-range Potts model and studied critical-temperature/exponent scaling, not this exact antiferromagnetic ground-state equality and nine-site rigidity. The transfer framework is standard; the claim here is the precise commensurate equality criterion and constant 18-fold ground-state degeneracy for the specified third-power cyclic family.

## Limitations
The theorem characterizes equality in a sharp lower bound and does not give exact ground energies or degeneracies for all other orders. No claim is made about a positive-temperature transition, unique physical infinite-volume Gibbs state, or complete historical priority; other equivalent treatments of equal frustrated range-three chains may exist.

## References
1. T. Tonegawa, K. Takasaki, and M. Kaburagi, “Exact Ground State of the Finite-Field Three-State Potts Model on the One-Dimensional Lattice with First and Second Neighbor Interactions,” *J. Phys. Soc. Japan* **54** (1985), 4312–4320, https://doi.org/10.1143/JPSJ.54.4312.
2. Z. Glumac and K. Uzelac, “Critical behaviour of the 1D q-state Potts model with long-range interactions,” arXiv:hep-lat/9303016 (first public 1993-03-31), https://arxiv.org/html/hep-lat/9303016v1.
