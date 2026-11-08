# Two-defect Boolean Gabor tomography has a sharp eight-point conditioning rigidity

## Finding
Let \(n\ge3\), \(G=\mathbb F_2^n\), \(N=2^n\), and fix any nonzero \(d\in G\). For arbitrary complex \(z,w\), define the full-support background with two coordinate defects
\[
g_{z,w}(x)=1+z\mathbf1_{\{0\}}(x)+w\mathbf1_{\{d\}}(x).
\]
Take all \(N^2\) translation-modulation shifts of \(g_{z,w}\), and let \(\mathcal L_{z,w}\) send a complex \(N\times N\) matrix to its Hilbert--Schmidt inner products with their rank-one projectors. Write \(\kappa(\mathcal L_{z,w})\) for the ratio of the largest to the least singular value, with value \(+\infty\) if the map is singular. Then
\[
\boxed{\inf_{z,w\in\mathbb C}\kappa(\mathcal L_{z,w})=\sqrt{2N}-1.}
\]
All and only the **eight** optimal parameter pairs are obtained by placing a real defect \(-\sqrt{N/2}\) at **one** of \(0,d\), and a purely imaginary defect \(+i\sqrt{N/2}\) or \(-i\sqrt{N/2}\) at **one**, possibly the same, of \(0,d\). Thus the added second coordinate cannot improve the sharp one-coordinate stability, but permits four genuine separated-coordinate optimizers. In every separated optimizer the real-only and imaginary-only one-coordinate perturbations would each have a singular Gabor measurement lift on their own, whereas their combination has full rank.

More strongly, the theorem provides the entire \(N^2\)-element singular-value multiset for **all** \(z,w\), hence an exact rank formula at all exceptional parameter values. In the following table write \(z=u+iv\), \(w=s+it\),
\[
 h_z=|z|^2+2u,\quad h_w=|w|^2+2s,\quad
 E=w+\overline z+w\overline z,\quad H=N+h_z+h_w.
\]
Each table entry \((A,m)\) means a singular value \(\sqrt N\,|A|\) occurring with multiplicity \(m\). Coincident magnitudes contribute their multiplicities **additively**.

| Ambiguity coefficient \(A\) | Multiplicity \(m\) |
| --- | ---: |
| \(H\) | \(1\) |
| \(h_z+h_w\) | \(N/2-1\) |
| \(h_z-h_w\) | \(N/2\) |
| \(N+2\operatorname{Re}E\) | \(1\) |
| \(2\operatorname{Re}E\) | \(N/2-1\) |
| \(2i\operatorname{Im}E\) | \(N/2\) |
| \(N+2(u+s)\) | \(N-2\) |
| \(2(u+s)\) | \((N-2)(N/4-1)\) |
| \(2(u-s)\) | \((N-2)N/4\) |
| \(-2i(v+t)\) | \((N-2)N/4\) |
| \(-2i(v-t)\) | \((N-2)N/4\) |

Every listed multiplicity is positive when \(N\ge8\). The exact rank equals \(N^2\) minus the sum of multiplicities in rows whose displayed coefficient is zero. In particular, the parameter pair \(z=1\), \(w=i\) gives **full matrix recovery in all dimensions \(N\ge8\)**, although the two respective single-coordinate perturbations do not.

## Assumptions and scope
The signal Hilbert space is \(\mathbb C^G\) with counting inner product. For \(a,b\in G\), let \((T_af)(x)=f(x+a)\) and \((M_bf)(x)=(-1)^{b\cdot x}f(x)\). The projector is \(P_{a,b}=|M_bT_ag_{z,w}\rangle\langle M_bT_ag_{z,w}|\), without unit-vector normalization. The matrix domain of the lift carries the Hilbert--Schmidt norm, and its \(N^2\)-dimensional data codomain the ordinary Euclidean norm. Its condition number is unchanged if the window is normalized. Dot products and all additions on \(G\) are over \(\mathbb F_2\). There is no hidden genericity restriction: \(z,w\) range over all of \(\mathbb C\), including zero and resonant parameters. The two defect sites must be distinct, and \(n\ge3\) is essential for a counting step in the sharp lower bound. The statement concerns linear operator tomography and its stability; full rank implies pure-state phase retrieval, but not conversely.

## Proof
**1. Weyl diagonalization and exact table.** For the unnormalized self-ambiguity function set
\[
 A_g(a,b)=\sum_{x\in G}g(x+a)\overline{g(x)}(-1)^{b\cdot x}.
\]
The \(N^2\) Weyl operators form an orthogonal Hilbert--Schmidt matrix basis. Conjugation by each Weyl shift acts on any such basis element by a phase-space character. Orthogonality of those characters gives the singular-value multiset
\[
 \{\sqrt N\,|A_g(a,b)|:(a,b)\in G^2\}.
\]
This standard spectral identity is credited in the references; the computation and optimization below specialize it to the two-defect family.

For \(a=0\), the zero shift gives \(H\), whereas nonzero \(b\) gives \(h_z+(-1)^{b\cdot d}h_w\). For \(a=d\), a direct expansion at the two exceptional sites gives \(N\mathbf1_{\{b=0\}}+E+(-1)^{b\cdot d}\overline E\). For each \(a\notin\{0,d\}\), the four exceptional sites \(0,d,a,a+d\) are pairwise distinct, so
\[
 A_g(a,b)=N\mathbf1_{\{b=0\}}+\overline z+(-1)^{b\cdot d}\overline w
       +(-1)^{b\cdot a}\bigl(z+(-1)^{b\cdot d}w\bigr).
\]
The independent linear functionals \(b\mapsto b\cdot a\) and \(b\mapsto b\cdot d\) have exactly \(N/4\) characters in each joint-sign class. The both-even class contains \(b=0\), so only \(N/4-1\) nonzero characters remain there. This supplies all eleven rows and their multiplicities, which sum to \(N^2\). It also proves the exact zero-row rank formula. Since \(|A_g(a,b)|\le\sum_x |g(x+a)||g(x)|\le\|g\|_2^2=H\), the largest singular value is \(\sqrt N H\).

**2. Universal conditioning obstruction.** Put \(U=u+s\), \(V=u-s\), \(P=v+t\), \(Q=v-t\), and
\[
 r=\min\{|U|,|V|,|P|,|Q|\}.
\]
When \(r=0\), at least one nonzero-multiplicity table row vanishes and the lift is singular. For \(r>0\), the four nonexceptional rows show that the least ambiguity modulus is at most \(2r\). On the other hand, the norm identity is
\[
 H=N+2U+\frac{U^2+V^2+P^2+Q^2}{2}.
\]
Because the four absolute values are at least \(r\), minimizing this expression over \(U\) with \(|U|\ge r\) gives
\[
 H\ge \begin{cases}
 N-2+\frac32r^2,&0<r\le2,\\
 N-2r+2r^2,&r\ge2.
 \end{cases}
\]
Indeed, \(V^2+P^2+Q^2\ge3r^2\), and the minimizer of \(U^2/2+2U\) subject to \(|U|\ge r\) is \(U=-2\) for \(r\le2\) and \(U=-r\) for \(r\ge2\).

Therefore \(\kappa\ge H/(2r)\). For \(0<r\le2\), the expression \((N-2)/(2r)+3r/4\) decreases on that interval when \(N\ge8\), so it is at least \((N+4)/4\). The identity \((N+8)^2-32N=(N-8)^2\ge0\) gives
\[
 (N+4)/4\ge\sqrt{2N}-1.
\]
For \(r\ge2\), the arithmetic--geometric mean inequality yields
\[
 \frac N{2r}-1+r\ge\sqrt{2N}-1,
\]
with equality exactly at \(r=\sqrt{N/2}\), which belongs to this regime. Hence the displayed condition-number lower bound holds for every complex parameter pair, including singular ones.

**3. Equality and eight optimizers.** Equality forces \(r=\sqrt{N/2}\), \(U=-r\), and \(|V|=|P|=|Q|=r\). For \(N=8\) this also follows from the strict monotonicity below \(r=2\) and the unique shared endpoint; for higher \(N\) it follows from strict arithmetic--geometric mean equality. Solving the four linear equations shows that exactly one of \(u,s\) equals \(-r\) and the other equals zero, while exactly one of \(v,t\) equals \(+r\) or \(-r\) and the other equals zero. These are precisely the eight asserted pairs.

To verify attainment, first place both the real and imaginary parts at the same site. All nonidentity ambiguity magnitudes are among \(2r\), \(2r(r-1)\), and \(N-2r\), with \(2r\) present. Place them at distinct sites: the same three magnitudes occur (possibly with different labels). Since \(r\ge2\), \(2r(r-1)\ge2r\) and \(N-2r=2r(r-1)\ge2r\); the least nonidentity modulus is exactly \(2r\). The identity modulus is \(H=N-2r+2r^2=2r(2r-1)\). Thus all eight pairs have finite condition number \(H/(2r)=\sqrt{2N}-1\). The equality argument excludes all others, proving sharpness and classification.

**4. Separate one-coordinate singularity.** For a real-only defect, \(v=t=0\), so the two imaginary rows vanish. For a purely imaginary-only defect, \(u=s=0\), so the two real rows vanish. Hence either separately gives a singular lift. Their mixed, separated sharp optimizer is full rank, as its least ambiguity modulus is \(2r>0\). The small fixed example \(z=1,w=i\) is also full rank: in the eleven-row table its nonidentity coefficients have respective nonzero magnitudes \(4,2,N+2,2,4,N+2,2,2,2,2\), with identity coefficient \(H=N+4\).

## Verification
The standalone standard-library script `CHECK.py` constructs actual windows and computes every ambiguity coefficient independently of the branch formulas on \(\mathbb F_2^3\), \(\mathbb F_2^4\), and \(\mathbb F_2^5\), at ten integer Gaussian parameter pairs per dimension (30 complete enumerations). It also constructs actual vectorized rank-one Weyl orbit projectors, computes their modular ranks by exact Gaussian elimination over \(\mathbb F_{1009}\), and compares against the zero-row count for five parameters at \(N=8\). For these integer Gaussian windows the chosen reduction has no false rank matches in the tested cases; the symbolic proof gives exact complex ranks for all parameters. Finally the script checks all eight sharp parameters in each of \(N=8,16,32,64\). Executed command `python3 CHECK.py` produced `TWO_DEFECT_BOOLEAN_GABOR_EXACT_CHECKS_PASS 30 spectral enumerations, 5 exact modular projector ranks, 32 sharp optimizers`. The finite checks corroborate rather than replace the analytic proof.

## Relationship to prior work
Bojarovska--Flinth [1], especially Theorem 2.2 and its matrix-lifting formulation, establish the standard Gabor phase-retrieval and ambiguity framework, but do not optimize two-site complex defects on a binary vector group. Zhu--Wang [2], Theorem 8 and formulas (69)--(75), analyze the **one-site** characteristic-two fiducial obtained by adding a single coordinate spike to a flat window. Their constructed phase \(3\pi/4\) already realizes one of the same-site sharp optimizers here and gives its complete two-level nonidentity spectrum; that known optimizer and its performance are **not** claimed as new. The distinction is the global inequality over **all complex two-site defects**, its complete eight-optimizer equality classification (including four separated-site pairs), and the complete parameter-dependent eleven-row rank discriminant, none of which follows from the stated one-site theorem without the new four-variable obstruction.

Goldberger--Kang--Okoudjou [3] establish general cyclic Gabor projector-Gram facts, not this dyadic two-defect result. Published findings on two-hole **cyclic** Gabor windows and on one-frequency binary **affine-group** projectors [4--5] use different group actions and do not imply the computed Boolean Weyl spectrum or the optimal eight-point design boundary. Related single-impulse cyclic chirp tomography [6] is likewise a different family. The comparison uses statements and hypotheses, not merely titles; hidden equivalent results in more general frame optimization literature remain a priority risk.

## Limitations
The sharp optimum is restricted to the two-defect-plus-flat-background window family and to the full \(N^2\)-outcome Boolean translation-modulation orbit. It is **not** a universal minimax statement over arbitrary Weyl windows, whose SIC benchmark is lower. The separated-coordinate optimizers have the same optimal condition number as the already-known one-coordinate construction; their novelty is the exact absence of improvement under the larger design class and the newly available separated-site equality configurations. Noise robustness beyond the linear Hilbert--Schmidt condition number is not established. No independent external mathematical audit has been performed.

## References
1. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800, first posted 2015-03-19; full accessible preprint, Section 2 and Theorem 2.2.
2. X. Zhu and Y. Wang, *Uniformly Stable Minimal Weyl--Heisenberg Measurements Approaching the SIC Benchmark*, arXiv:2608.11850, first posted 2026-08-12; full accessible manuscript, Section IV.1, Theorem 8 and equations (69)--(75).
3. A. Goldberger, S. Kang and K. A. Okoudjou, *Towards a classification of incomplete Gabor POVMs in* \(\mathbb C^d\), arXiv:2106.01509, first posted 2021-06-02; general Gabor POVM spectral framework.
4. *Exact arithmetic rank of two-hole cyclic Gabor measurements*, published-finding identifier `2026/10/11/SCOPE-exact-arithmetic-rank-of-two-hole-cyclic-gabor-measurements--6aad25598ee0`.
5. *Exact projector-span ranks for binary affine Fourier windows*, published-finding identifier `2026/10/11/SCOPE-exact-projector-span-ranks-for-binary-affine-fourier-windows--038706e64864`; RESULT.md examined.
6. *Single-impulse quadratic chirps: exact cyclic Gabor tomography spectrum and arithmetic rank obstruction*, published-finding identifier `2026/10/11/SCOPE-single-impulse-quadratic-chirps-exact-cyclic-gabor-tomography-sp--03361b3cff9c`; RESULT.md examined.
