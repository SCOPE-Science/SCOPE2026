# Fourier recovery and a cubic minimum-zero threshold for height-three Dyck paths

## Finding

For every integer \(n\ge1\), let \(\mathcal D_n^{(3)}\) consist of the up-step incidence vectors of all length-\(2n\) Dyck paths that start and finish at height zero and never leave heights \(0,1,2,3\). With the unnormalized Walsh transform
\[
W_n(s)=\sum_{x\in\mathcal D_n^{(3)}}(-1)^{\langle s,x\rangle},\qquad s\in\mathbb F_2^{2n},
\]
we prove the **exact all-order recovery and sharp nonzero-multiplier law**
\[
T_n\text{ is invertible}\ \Longleftrightarrow\ n\not\equiv2\pmod3,
\qquad
\min_{s:W_n(s)\neq0}|W_n(s)|=
\begin{cases}1,&n\not\equiv2\pmod3,\\2,&n\equiv2\pmod3.\end{cases}
\]
Here \(T_n f=1_{\mathcal D_n^{(3)}}*f\) is unnormalized counting convolution on \(\mathbb F_2^{2n}\). Consequently, its inverse on the nonzero Walsh range has exact Hilbert-space operator norm \(1\) or \(1/2\), respectively.

In the **original step-coordinate degree**, and not under arbitrary changes of coordinates, the first three singular semilengths have distinct minimum vanishing-character weights:

| Semilength \(n\) | Number of paths | Walsh zeros | Convolution rank | Minimum zero-character weight |
|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 4 | none |
| 2 | 2 | 8 | 8 | 1 |
| 3 | 5 | 0 | 64 | none |
| 4 | 13 | 0 | 256 | none |
| 5 | 34 | 216 | 808 | 2 |
| 6 | 89 | 0 | 4096 | none |
| 7 | 233 | 0 | 16384 | none |
| 8 | 610 | **7032** | **58504** | **3** |

At \(n=8\) exactly ten zero characters have weight three and none has weight at most two. The coordinate character selecting up-steps at positions \(2,8,12\) divides the 610 paths into 305 positive and 305 negative contributions. The analogous earliest witnesses at \(n=2,5\) use positions \((2)\) and \((2,7)\), giving \((1,1)\) and \((17,17)\) signed partitions.

## Assumptions and scope

All coordinates are binary. Step positions are numbered \(1,\dots,2n\), with a one indicating an upward step, and heights are the integer running sum of upward minus downward steps. A Walsh frequency is a subset of step positions; its Hamming weight is the number of selected positions. The Fourier transform is **unnormalized**, so its eigenvalues for counting convolution are exactly the displayed integer multipliers. The Hilbert space is equipped with counting-measure \(\ell^2\) norm, whose Fourier transform is unitary after normalization by the group size.

For the affine identification, set \(m=2n-3\) for \(n\ge2\). For a path of height \(h_t\) after \(t\) steps, define
\[
v_t=\frac{h_t-(t\bmod2)}2\in\{0,1\},\qquad 2\le t\le2n-2,
\]
and \(y_t=v_t\oplus1\) when \(t\) is even and \(y_t=v_t\) when \(t\) is odd. The ordered word \((y_2,\ldots,y_{2n-2})\) is a Fibonacci string of length \(m\), meaning its consecutive ones are forbidden.

## Proof

**Affine Fibonacci identification.** Boundary heights force \(v_0=v_1=v_{2n-1}=v_{2n}=0\). Between consecutive even/odd intermediate times, the Dyck step condition forbids precisely \((v_t,v_{t+1})=(0,1)\) when \(t\) is even; between odd/even times it forbids \((1,0)\). Complementing the even-indexed \(v_t\) turns both restrictions into \(y_ty_{t+1}=0\). Conversely, every Fibonacci string defines these intermediate heights, and consecutive heights differ by exactly one, including the boundary steps. Thus this is a bijection. Moreover,
\[
v_t\equiv\sum_{j=1}^t x_j-\left\lceil t/2\right\rceil\pmod2,
\]
so the map is affine in the up-step incidence vector \(x\), with an affine inverse on its affine span. Since every internal Fibonacci coordinate may vary independently in a suitable string, the affine span has dimension \(m\). Consequently the original ambient Walsh magnitudes comprise eight copies of the Fibonacci-cube Walsh magnitudes, because \(2n-m=3\).

**Signed independence recurrence.** For the length-\(m\) path let
\[
Z_m(\varepsilon)=\sum_{I\text{ independent}}\prod_{j\in I}\varepsilon_j,
\qquad\varepsilon_j\in\{-1,1\}.
\]
The one-step recurrence is \(z_0=1\), \(z_1=1+\varepsilon_1\), \(z_j=z_{j-1}+\varepsilon_j z_{j-2}\) for \(j\ge2\). The number of independent sets is \(F_{m+2}=F_{2n-1}\), where \(F_1=F_2=1\). This number is even exactly when \(n\equiv2\pmod3\). Since every signed sum has this parity, when the number is odd no Walsh coefficient can vanish, and its magnitude is at least one.

If every \(\varepsilon_j=-1\), the recurrence becomes \(z_j=z_{j-1}-z_{j-2}\), with \(z_0=1\), \(z_1=0\); the resulting sequence \(1,0,-1,-1,0,1\) repeats with period six. Thus a zero occurs exactly at \(m\equiv1\pmod3\), i.e., \(n\equiv2\pmod3\); outside this residue class it attains magnitude one. For \(m\equiv1\pmod3\), switch the last sign from negative to positive. The final value changes by \(2z_{m-2}\), which is \(\pm2\) (including \(m=1\), where the value is directly two). Every multiplier is even in this case, so two is its sharp smallest nonzero magnitude. The case \(n=1\) consists of one path, hence every multiplier has magnitude one.

**Operator norm.** Fourier diagonalization gives \(\|(T_n|_{\operatorname{ran}T_n})^{-1}\|_{2\to2}=1/\min_{W_n(s)\ne0}|W_n(s)|\). No assertion about full-space inversion is made in singular dimensions.

**Finite low-degree certificate.** For \(1\le n\le8\), independently (a) enumerate the Dyck paths by the height-restricted step recursion, (b) compute the complete integer Walsh–Hadamard transform, (c) calculate each frequency by a separate signed height-state dynamic program, and (d) compare its absolute value against the Fibonacci signed-independence recurrence under the explicit affine coordinate transformation. All \(65536\) frequencies at \(n=8\) are included. The resulting zero counts, ranks, and minimum character weights are in the displayed table. The full degree-three zero-frequency list is in the accompanying certificate. This finite verification is exhaustive for these eight dimensions only.

## Verification

Run `python3 code/height3_verify.py` using standard Python 3 (no external libraries). Successful output ends with `HEIGHT3_DYCK_FIBONACCI_WALSH_PASS`. The program checks every signed frequency against two independent algorithms through \(n=8\), verifies Parseval identities, compares the affine map and its inverse against every Fibonacci word, checks minimum zero degrees and exact nullities, and runs additional finite tests of the all-order signed recurrence. Those extra finite tests support but do not replace the analytic proof above.

## Relationship to prior work

Bacher's treatment of bounded-height Dyck excursions provides the general enumeration and transfer-matrix framework. Mollard's work develops the Fibonacci cube as a hypercube subgraph of binary words avoiding adjacent ones. These established frameworks motivate the objects; neither inspected primary text states the present **step-coordinate** Walsh singularity classification, sharp nonzero convolution magnitudes, or the ten first cubic-frequency cancellations at semilength eight. A classical identification of Fibonacci cubes with distributive lattices of fence posets is related to the affine coding, but the quantitative step-frequency claims require the transfer to the original up-step coordinates and the exact cancellation analysis.

## Limitations

The exact weight-three frequency census and full nullity claims are only for \(n\le8\). No formula for the full nullity at arbitrary singular \(n\), no classification of higher-length minimum zero-frequency weight, and no endpoint \(\ell^1\) projection norm is asserted. This work has not received an independent external mathematical audit. Historical-priority comparison is bounded; an inaccessible historical argument that explicitly combines the fence-poset coding with signed Fourier analysis may cover some of these conclusions.

## References

1. Michel Mollard, *Maximal hypercubes in Fibonacci and Lucas cubes*, first publicly available 2012-01-06, https://arxiv.org/abs/1201.1494 .
2. Axel Bacher, *Generalized Dyck paths of bounded height*, first publicly available 2013-03-11, https://arxiv.org/abs/1303.2724 .
