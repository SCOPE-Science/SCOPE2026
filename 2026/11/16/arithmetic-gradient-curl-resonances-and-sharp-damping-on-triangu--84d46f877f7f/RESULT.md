# Arithmetic gradient–curl resonances and sharp damping on triangulated cyclic annuli

## Finding
For each integer \(n\ge3\), the standard unweighted triangulation of a two-rail cyclic annulus has a complete four-band Fourier decomposition of its edge Hodge Laplacian. Put \(c_j=|\cos(\pi j/n)|\), for \(0\le j<n\). For \(a,b>0\), the eigenvalues of \(H_n(a,b)=aB_1^{\mathsf T}B_1+bB_2B_2^{\mathsf T}\) consist of one zero, the gradient band
\[
 a(6-4c_j^2\pm2c_j),
\]
with the zero value for \(j=0\) omitted, and the curl band
\[
 b(3\pm2c_j).
\]
Each Fourier-sector value is counted with its specified Fourier multiplicity. There is exactly one harmonic edge flow, representing circulation around the annulus.

Set \(g_n=6-4\cos^2(\pi/n)-2\cos(\pi/n)\). The smallest positive eigenvalue is exactly \(\min\{a g_n,b\}\). Under the budget \(a+b=2\), its unique maximizer is
\[
 a_*={2\over 1+g_n},\qquad b_*={2g_n\over1+g_n},\qquad
 \max\lambda_{\min}^+={2g_n\over1+g_n}.
\]
The preferred weight changes from curl-dominant \(b_*>a_*\) for \(3\le n\le6\) to gradient-dominant \(a_*>b_*\) for \(n\ge7\). At large \(n\), \(g_n\sim5\pi^2/n^2\), and the optimal positive gap is asymptotic to \(10\pi^2/n^2\).

For equal weights \(a=b=1\), two exact arithmetic resonances hold:

* Eigenvalue \(4\) occurs in the gradient sector for every \(n\), and also in the curl sector **if and only if** \(3\mid n\).
* Eigenvalue \(5\) occurs in the curl sector for every \(n\), and also in the gradient sector **if and only if** \(5\mid n\).

For every \(n\) divisible by three or five, these shared eigenvalues imply that no scalar spectral multiplier \(f(H_n(1,1))\), in particular no polynomial filter in the full Hodge Laplacian, can act as the identity on every gradient flow and as zero on every curl flow. The assertion does not exclude separate lower- and upper-Hodge filtering, which distinguishes those sectors.

## Assumptions and scope
Indices are taken modulo \(n\). There are \(2n\) vertices \(t_j,b_j\), four oriented edges per cell \(T_j=(t_j,t_{j+1})\), \(B_j=(b_j,b_{j+1})\), \(V_j=(b_j,t_j)\), and \(D_j=(b_j,t_{j+1})\), and two oriented triangular faces per cell. Their boundary chains are \(\partial F_j^+=D_j-T_j-V_j\) and \(\partial F_j^-=B_j+V_{j+1}-D_j\). This defines real incidence matrices \(B_1\in\mathbb R^{2n\times4n}\), \(B_2\in\mathbb R^{4n\times2n}\), with \(B_1B_2=0\). Edges have counting-measure inner product; no length or area weights are implicit. The complex is a triangulated annulus with exactly one hole. The positive spectral gap omits its harmonic zero.

## Proof
The boundary identities show directly that \(B_1B_2=0\), so the orthogonal gradient and curl ranges are invariant and mutually orthogonal. Their respective nonzero spectra agree with those of the vertex Laplacian \(B_1B_1^{\mathsf T}\) and face Laplacian \(B_2^{\mathsf T}B_2\). Fourier transform in the cyclic cell index gives the Hermitian symbols, for \(z=e^{2\pi i j/n}\),
\[
 L_0(z)=\begin{pmatrix}4-z-z^{-1}&-(1+z^{-1})\\-(1+z)&4-z-z^{-1}\end{pmatrix},
\qquad
 L_2(z)=\begin{pmatrix}3&-(1+z^{-1})\\-(1+z)&3\end{pmatrix}.
\]
The exact diagonalization uses \(|1+z|=2|\cos(\pi j/n)|\) and \(4-z-z^{-1}=6-4\cos^2(\pi j/n)\), proving both pairs of band formulas. The vertex symbol has one zero at \(j=0\), while every face eigenvalue is at least one. Thus \(\operatorname{rank}B_1=2n-1\), \(\operatorname{rank}B_2=2n\), and \(\dim\ker H_n=4n-(2n-1)-2n=1\).

The smaller vertex branch is \(6-4c^2-2c\), strictly decreasing for \(c\ge0\). Over \(j\ne0\), its minimum is at \(j=1,n-1\), equal to \(g_n\). The remaining \(j=0\) vertex eigenvalue is \(4\ge g_n\). The curl minimum is \(3-2=1\), attained at \(j=0\). Hence the positive gap is \(\min\{ag_n,b\}\). For \(a+b=2\), this minimum strictly increases up to its unique equalization point and strictly decreases afterward. Since \(g_n\) strictly decreases in \(n\), \(g_6=3-\sqrt3>1\), and \(g_7<1\) (for example by \(\cos(\pi/7)>1-242/2401>43/48>(\sqrt{21}-1)/4\)), the sole transition is between six and seven cells. Taylor expansion at \(n=\infty\) gives \(g_n=5\pi^2/n^2+O(n^{-4})\).

For \(a=b=1\), \(4\) is the nonzero \(j=0\) vertex eigenvalue; \(5\) is the upper \(j=0\) face eigenvalue. A face eigenvalue equals four exactly when \(3\pm2c_j=4\), hence \(c_j=1/2\), equivalent to \(j/n\in\{1/3,2/3\}\), thus \(3\mid n\). A vertex eigenvalue equals five exactly when \(6-4c_j^2\pm2c_j=5\), equivalently \(c_j\in\{(\sqrt5-1)/4,(1+\sqrt5)/4\}=\{\cos(2\pi/5),\cos(\pi/5)\}\); therefore \(5\mid n\). On a shared eigenvalue, any scalar function of \(H_n\) acts by the same scalar on the gradient and curl eigenvectors, making exact separation impossible. These are two proven infinite resonance families, not a complete classification of *all* possible cross-sector eigenvalue coincidences.

## Verification
The self-contained Python script `verify_hodge.py` builds both incidence matrices directly from the stated faces, asserts \(B_1B_2=0\), computes the \(4n\)-dimensional full edge-Hodge spectrum and compares it to the four Fourier bands for every integer \(3\le n\le60\), using three different pairs of positive weights. It additionally tests the gap optimizer, the six/seven-cell transition, and the exact \(3\)- and \(5\)-divisibility resonance rules. It passed 22,272 scalar comparisons. Execution: `OPENBLAS_NUM_THREADS=1 python verify_hodge.py` with NumPy installed. Finite numerical tests support, but do not replace, the proof for all \(n\ge3\).

## Relationship to prior work
Yang, Isufi, Schaub and Leus (2021) introduced Hodge-Laplacian finite-impulse-response filters and emphasized that gradient and curl Fourier spectra need distinct treatments. Roddenberry, Frantzen, Schaub and Segarra (2021) developed Hodge-aware spectral wavelets for simplicial edge flows. Their inspected constructions give the general Hodge decomposition and filtering motivation. The present result concerns the complete explicit spectrum, sharp two-weight gap tuning, and the arithmetic impossibility of scalar spectral separation for a particular triangulated cyclic annulus. General lower/upper Hodge spectral identities are established background, not claimed as new.

## Limitations
The spectrum and gap classification apply only to this precisely specified unweighted cyclic triangulation; the coefficients \(a,b\) are positive global multipliers. The arithmetic \(4\)- and \(5\)-resonance equivalences hold at \(a=b=1\); no exhaustive classification of other possible cross-sector coincidences is asserted. The scalar-filter obstruction concerns exact preservation of **every** gradient and annihilation of **every** curl flow, not arbitrary approximate filtering or independent lower/upper filtering. Prior mathematical literature could contain an equivalent specialized diagonalization not located in the sources inspected. Independent external validation and absolute historical-priority determination have not been performed.

## References
1. M. Yang, E. Isufi, M. T. Schaub, and G. Leus, *Finite Impulse Response Filters for Simplicial Complexes*, arXiv:2103.12587, first submitted 2021-03-23. https://arxiv.org/abs/2103.12587
2. T. M. Roddenberry, F. Frantzen, M. T. Schaub, and S. Segarra, *Hodgelets: Localized Spectral Representations of Flows on Simplicial Complexes*, arXiv:2109.08728, first submitted 2021-09-17. https://arxiv.org/abs/2109.08728
3. V. P. Grande and M. T. Schaub, *Disentangling the Spectral Properties of the Hodge Laplacian: Not All Small Eigenvalues Are Equal*, arXiv:2311.14427, 2023; bibliographic abstract consulted, full text not obtained. https://arxiv.org/abs/2311.14427
